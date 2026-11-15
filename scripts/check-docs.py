#!/usr/bin/env python3
"""Check local Markdown links and framework structure using only stdlib."""

import argparse
import html
import hashlib
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


LINK = re.compile(r'!?\[([^\]\n]+)\]\((<[^>\n]+>|[^\s()]*(?:\([^()]*\)[^\s()]*)*)(?:\s+"[^"]*")?\)')
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
CONTROL = re.compile(r"^## Control (\d+\.\d+) — (.+)$", re.MULTILINE)
RELEASE_SOURCE = Path("source/v1.0")
RELEASE_PDF = RELEASE_SOURCE / "AAF-1.0.pdf"

FIELDS = ("Requirement", "Rationale", "Assessment")
PRINCIPLES = (
    ("01-identity.md", 5), ("02-sponsor.md", 5), ("03-role.md", 8),
    ("04-authority.md", 14), ("05-oversight.md", 8), ("06-recourse.md", 5),
)


def without_fences(text):
    """Ignore examples inside backtick or tilde fences, retaining line numbers."""
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
            lines.append("\n")
        elif marker:
            fence = marker[1]
            lines.append("\n")
        else:
            lines.append(line)
    return "".join(lines)


def anchors(text):
    text = without_fences(text)
    result = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text))
    used = set()
    for match in HEADING.finditer(text):
        title = LINK.sub(lambda link: link[1], match[1])
        title = html.unescape(re.sub(r"<[^>]*>", "", title)).lower()
        slug = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
        candidate, suffix = slug, 0
        while candidate in used:
            suffix += 1
            candidate = f"{slug}-{suffix}"
        used.add(candidate)
        result.add(candidate)
    return result


def local_target(path, destination):
    url = urlsplit(html.unescape(destination.strip("<>")))
    if url.scheme or url.netloc:
        return None
    target = (path.parent / unquote(url.path)).resolve() if url.path else path
    return target, unquote(url.fragment)


def normalized(text, path, root):
    """Ignore editorial aids and wrapping; retain words and resolved link targets."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"<a\s+[^>]*></a>", "", text)
    text = re.sub(r"^(?:\*\*)?Source:(?:\*\*)?.*$", "", text, flags=re.MULTILINE)

    def canonical_link(match):
        target = local_target(path, match[2])
        if target is None:
            return match[0]
        filename, fragment = target
        try:
            destination = filename.relative_to(root).as_posix()
        except ValueError:
            destination = filename.as_posix()
        return f"[{match[1]}]({destination}#{fragment})"

    return " ".join(LINK.sub(canonical_link, text).split())


def sections(text, pattern):
    matches = list(pattern.finditer(text))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        yield match, text[match.end():end]


def check_repository(root):
    root = root.resolve()
    errors = []
    excluded = {".git", ".venv", "__pycache__", "reports", "ACCURACY_AUDIT.md", "SOURCE_GAPS.md", "TODO.md", "source-links.md"}

    def is_documentation(path):
        relative = path.relative_to(root)
        if excluded.intersection(relative.parts):
            return False
        return relative.parts[0] != "source" or relative.is_relative_to(RELEASE_SOURCE)

    pages = sorted(path for path in root.rglob("*.md") if is_documentation(path))
    contents = {path: path.read_text(encoding="utf-8") for path in pages}
    page_anchors = {path: anchors(text) for path, text in contents.items()}
    link_count = 0

    for path, text in contents.items():
        name = path.relative_to(root)
        if not text.strip():
            errors.append(f"{name}: empty Markdown page")
        visible = without_fences(text)
        for match in LINK.finditer(visible):
            target = local_target(path, match[2])
            if target is None:
                continue
            link_count += 1
            filename, fragment = target
            where = f"{name}:{visible.count(chr(10), 0, match.start()) + 1}"
            try:
                filename.relative_to(root)
            except ValueError:
                errors.append(f"{where}: link leaves the repository: {match[2]}")
                continue
            if filename.is_relative_to(root / "source") and not filename.is_relative_to(root / RELEASE_SOURCE):
                errors.append(f"{where}: link to withdrawn source: {match[2]}")
                continue
            if filename.suffix.lower() == ".pdf" and filename != root / RELEASE_PDF:
                errors.append(f"{where}: PDF link outside the approved release: {match[2]}")
                continue
            if not filename.exists():
                errors.append(f"{where}: missing link target: {match[2]}")
            elif fragment and filename.suffix == ".md":
                if fragment not in page_anchors.get(filename, set()):
                    errors.append(f"{where}: missing anchor: {match[2]}")

    def read_required(relative):
        path = root / relative
        if path not in contents:
            errors.append(f"{relative}: required page is missing")
        return path, contents.get(path, "")

    _, index = read_required(RELEASE_SOURCE / "README.md")
    pdf = root / RELEASE_PDF
    checksum = re.search(r"PDF SHA-256: `([a-f0-9]{64})`", index)
    if not pdf.is_file():
        errors.append(f"{RELEASE_PDF}: release PDF is missing")
    elif not checksum or hashlib.sha256(pdf.read_bytes()).hexdigest() != checksum[1]:
        errors.append(f"{RELEASE_PDF}: PDF does not match the SHA-256 in the source index")

    control_count = 0
    for principle, (filename, count) in enumerate(PRINCIPLES, start=1):
        parsed = []
        expected = [f"{principle}.{number}" for number in range(1, count + 1)]
        for directory in ("framework", RELEASE_SOURCE):
            path, text = read_required(f"{directory}/principles/{filename}")
            blocks = list(sections(text, CONTROL))
            ids = [match[1] for match, _ in blocks]
            if ids != expected:
                errors.append(f"{path.relative_to(root)}: control IDs or order differ; expected {expected}, got {ids}")
            controls = {}
            for match, body in blocks:
                where = f"{path.relative_to(root)}: control {match[1]}"
                scopes = re.findall(r"^\*\*Scope:\*\* (.+)$", body, re.MULTILINE)
                if len(scopes) != 1 or scopes[0] not in {"Generic", "Internal", "External"}:
                    errors.append(f"{where}: expected one valid Scope tag")
                fields = list(sections(body, re.compile(r"^### (.+)$", re.MULTILINE)))
                if [field[1] for field, _ in fields] != list(FIELDS):
                    errors.append(f"{where}: expected Requirement, Rationale, Assessment in order")
                values = {field[1]: normalized(value, path, root) for field, value in fields}
                for field in FIELDS:
                    if not values.get(field):
                        errors.append(f"{where}: empty or missing {field}")
                controls[match[1]] = (match[2], scopes, values)
            parsed.append(controls)
        derived, source = parsed
        for number in derived.keys() & source.keys():
            title, scopes, fields = derived[number]
            source_title, source_scopes, source_fields = source[number]
            if title != source_title:
                errors.append(f"control {number}: title differs from the release source")
            if scopes != source_scopes:
                errors.append(f"control {number}: Scope tag differs from the release source")
            for field in FIELDS:
                if fields.get(field) != source_fields.get(field):
                    errors.append(f"control {number}: {field} differs from the release source")
        control_count += len(derived)

    definitions = []
    for directory in ("framework", RELEASE_SOURCE):
        path, text = read_required(f"{directory}/appendices/a-terminology.md")
        entries = [(match[1], normalized(body, path, root)) for match, body in sections(
            text, re.compile(r"^## (.+)$", re.MULTILINE)
        )]
        if len(entries) != 37:
            errors.append(f"{path.relative_to(root)}: expected 37 definitions, got {len(entries)}")
        definitions.append(entries)
    derived_definitions, source_definitions = definitions
    if [term for term, _ in derived_definitions] != [term for term, _ in source_definitions]:
        errors.append("framework/appendices/a-terminology.md: definition terms or order differ from the release source")
    source_by_term = dict(source_definitions)
    for term, definition in derived_definitions:
        if not definition:
            errors.append(f"framework/appendices/a-terminology.md: definition {term!r} is empty")
        if definition != source_by_term.get(term):
            errors.append(f"framework/appendices/a-terminology.md: definition {term!r} differs from the release source")

    return errors, len(pages), link_count, control_count, len(definitions[0])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors, pages, links, controls, definitions = check_repository(args.root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(f"Documentation checks failed: {len(errors)} issue(s).", file=sys.stderr)
        return 1
    print(f"Checked {pages} Markdown pages, {links} local links, {controls} controls, and {definitions} definitions.")
    print("Documentation checks passed against the versioned release source.")
    print("External sites and prose accuracy require review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

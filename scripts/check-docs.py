#!/usr/bin/env python3
"""Check local Markdown links and fidelity to the AAF source using only stdlib."""

import argparse
import html
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


LINK = re.compile(r'!?\[([^\]\n]+)\]\((<[^>\n]+>|[^\s()]*(?:\([^()]*\)[^\s()]*)*)(?:\s+"[^"]*")?\)')
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
CONTROL = re.compile(r"^## Control (\d+\.\d+) — (.+)$", re.MULTILINE)
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
    pages = sorted(path for path in root.rglob("*.md") if not any(
        part in {".git", ".venv", "__pycache__"} for part in path.relative_to(root).parts
    ))
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
            if filename.suffix.lower() == ".pdf":
                if name.parts[0] != "source":
                    errors.append(f"{where}: PDF link outside source/: {match[2]}")
                if name.parts[0] == "source" and filename == root / "AAF.pdf":
                    continue  # Optional local provenance file, intentionally not committed.
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

    control_count = 0
    for principle, (filename, count) in enumerate(PRINCIPLES, start=1):
        parsed = []
        expected = [f"{principle}.{number}" for number in range(1, count + 1)]
        for directory in ("source", "framework"):
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
        source, framework = parsed
        for identifier in source.keys() & framework.keys():
            original, derived = source[identifier], framework[identifier]
            where = f"framework/principles/{filename}: control {identifier}"
            if original[:2] != derived[:2]:
                errors.append(f"{where}: title or scope differs from source")
            for field in FIELDS:
                if original[2].get(field) != derived[2].get(field):
                    errors.append(f"{where}: {field} differs from source")
            control_count += 1

    definitions = []
    for directory in ("source", "framework"):
        path, text = read_required(f"{directory}/appendices/a-terminology.md")
        entries = [(match[1], normalized(body, path, root)) for match, body in sections(
            text, re.compile(r"^## (.+)$", re.MULTILINE)
        )]
        if len(entries) != 37:
            errors.append(f"{path.relative_to(root)}: expected 37 definitions, got {len(entries)}")
        definitions.append(entries)
    if [term for term, _ in definitions[0]] != [term for term, _ in definitions[1]]:
        errors.append("framework/appendices/a-terminology.md: definition names or order differ from source")
    source_definitions = dict(definitions[0])
    for term, definition in definitions[1]:
        if not definition or definition != source_definitions.get(term):
            errors.append(f"framework/appendices/a-terminology.md: definition {term!r} differs from source or is empty")

    return errors, len(pages), link_count, control_count, len(definitions[1])


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
    print("Documentation checks passed. External sites and prose accuracy require review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

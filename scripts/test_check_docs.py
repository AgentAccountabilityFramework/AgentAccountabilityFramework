"""Regression tests using temporary copies of the actual repository documents."""

import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest


REPOSITORY = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_docs", REPOSITORY / "scripts/check-docs.py")
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class DocumentationChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "repo"
        shutil.copytree(REPOSITORY, self.root, ignore=shutil.ignore_patterns(
            ".git", "*.pdf", "__pycache__", ".venv", "source"
        ))

    def errors(self):
        return CHECKER.check_repository(self.root)[0]

    def replace(self, name, before, after):
        path = self.root / name
        text = path.read_text(encoding="utf-8")
        self.assertIn(before, text)
        path.write_text(text.replace(before, after, 1), encoding="utf-8")

    def assert_error(self, fragment):
        self.assertTrue(any(fragment in error for error in self.errors()), fragment)

    def test_repository_without_provenance_pdf_passes(self):
        self.assertEqual([], self.errors())

    def test_missing_target_and_anchor_are_reported(self):
        (self.root / "link-test.md").write_text(
            "[Missing](absent.md)\n[Missing anchor](README.md#absent-heading)\n", encoding="utf-8"
        )
        errors = self.errors()
        self.assertTrue(any("missing link target" in error for error in errors))
        self.assertTrue(any("missing anchor" in error for error in errors))

    def test_fenced_examples_are_ignored_and_duplicate_headings_work(self):
        (self.root / "link-test.md").write_text(
            "# Heading\n# Heading\n[Second](#heading-1)\n"
            "```md\n[Example](absent.md)\n```\n", encoding="utf-8"
        )
        self.assertEqual([], self.errors())

    def test_withdrawn_source_link_is_reported_even_with_local_copy(self):
        source = self.root / "source"
        source.mkdir()
        (source / "README.md").write_text("# Internal source\n", encoding="utf-8")
        (self.root / "link-test.md").write_text("[Source](source/README.md)\n", encoding="utf-8")
        self.assert_error("link to withdrawn source")

    def test_local_source_is_excluded_from_checks(self):
        source = self.root / "source"
        source.mkdir()
        (source / "README.md").write_text("[Private](absent.md)\n", encoding="utf-8")
        self.assertEqual([], self.errors())

    def test_missing_control_and_scope_are_reported(self):
        self.replace("framework/principles/01-identity.md", "## Control 1.1 —", "## Control 1.9 —")
        self.replace("framework/principles/01-identity.md", "**Scope:** Generic", "")
        self.assert_error("control IDs or order differ")
        self.assert_error("expected one valid Scope tag")

    def test_missing_definition_is_reported(self):
        self.replace("framework/appendices/a-terminology.md", "## Action class", "Action class")
        self.assert_error("expected 37 definitions")

    def test_pdf_links_outside_source_are_reported(self):
        (self.root / "link-test.md").write_text("[Source](AAF.pdf)\n", encoding="utf-8")
        self.assert_error("PDF link outside source/")

    def test_missing_required_page_is_reported(self):
        (self.root / "framework/principles/01-identity.md").unlink()
        self.assert_error("framework/principles/01-identity.md: required page is missing")


if __name__ == "__main__":
    unittest.main()

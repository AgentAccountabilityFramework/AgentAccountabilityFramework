# Documentation checks

Run these commands from the repository root before submitting an edit:

```sh
python3 scripts/check-docs.py
git diff --check
```

The checker uses Python 3 and its standard library. It checks that Markdown pages contain text, local inline links reach existing files or directories, and Markdown fragments name a heading or explicit anchor. It checks the 45 framework controls for IDs, order, scope tags, and complete Requirement, Rationale, and Assessment fields, and checks that all 37 definitions are present and nonempty.

The checker compares the complete control fields, scope tags, titles, and definitions in the framework pages with the [versioned Markdown source](../source/v1.0/README.md). It verifies the release PDF against the SHA-256 recorded in that index. Older local source, review reports, and task notes are excluded, and links to older source files are rejected.

These checks cover the Markdown syntax used in this repository: inline links, ATX headings, and explicit HTML anchors. They do not fetch external sites, assess the accuracy of explanatory prose, or establish AAF conformance. Review those points yourself against the relevant sources.

## Changing the checker

After changing [check-docs.py](../scripts/check-docs.py), run its regression tests:

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
```

The tests make temporary copies of documentation and introduce errors to confirm that the checker catches them. An approved source update may require changes to the expected control or definition counts as well as the corresponding framework pages. A checker failure is a reason to compare the texts; do not change the source just to make a derived page pass.

The [GitHub workflow](../.github/workflows/check-docs.yml) runs the checker and its tests for pull requests and pushes to `master`. A local pass does not mean the hosted workflow has run.

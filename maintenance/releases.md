# Release guidance

Use this checklist when preparing a repository release. The people responsible for the project must agree on release authority, versioning, and publication separately. The source describes framework governance in [Section 8](../source/08-framework-governance.md#8-framework-governance).

- Confirm the scope and intended source baseline. Distinguish repository documentation changes from changes to framework requirements.
- Review affected content against the [Markdown source](../source/README.md), including controls, definitions, and cross-references. For source corrections, follow its provenance instructions and update [source coverage](source-coverage.md).
- Review the [changelog](../CHANGELOG.md), links, and navigation. Run `python3 scripts/check-docs.py`, its regression tests, and `git diff --check` as described in the [checks guide](checks.md). Record limitations.
- Review unresolved licensing, review assignments, and conduct reporting contacts in [LICENSE](../LICENSE), [CODEOWNERS](../.github/CODEOWNERS), and the [Code of Conduct](../CODE_OF_CONDUCT.md#reporting-a-concern). Resolve those needed for the intended publication.
- Confirm that the people with the necessary repository permissions have agreed on the release identifier, contents, and publication steps before tagging or publishing. Record the actual release details when they are known; do not invent dates or version numbers.

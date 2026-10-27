# Release guidance

This checklist supports a maintainer preparing a release; it does not establish release authority, a versioning policy, or a publication schedule. The source describes framework governance in [Section 8](../source/08-framework-governance.md).

- Confirm the scope and intended source baseline. Distinguish repository documentation changes from changes to framework requirements.
- Review affected content against the [Markdown source](../source/README.md), including controls, definitions, and cross-references. For source corrections, follow its provenance instructions and update [source coverage](source-coverage.md).
- Review the [changelog](../CHANGELOG.md), links, and navigation; run `git diff --check` and any applicable, implemented checks. Record limitations.
- Confirm that the people with the necessary repository permissions have agreed on the release identifier, contents, and publication steps before tagging or publishing. Record the actual release details when they are known; do not invent dates or version numbers.

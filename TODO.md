# Review and project decisions

The [framework pages](framework/README.md), contribution guides, and maintenance instructions are ready for review. Use this list to review the wording and settle decisions that cannot be filled in from the source alone.

## Review the documentation

- Read [Scope](framework/02-scope.md) first as the tone reference, then follow the framework reading order. Check that each explanation is clear without narrowing or expanding the requirement behind it.
- Review [Conformance and Assessment](framework/05-conformance-and-assessment.md), especially estate coverage, declared exceptions, organization-defined parameters, and evidence. These explain the positions in [Section 5](source/05-conformance-and-assessment.md#5-conformance-and-assessment); they do not supply a formal assessment method or certification scheme.
- Check the examples and descriptions in [Relationship to Existing Standards](framework/07-relationship-to-standards.md) against the linked primary sources. The page describes related work without claiming equivalence between standards.
- Review the [issue templates](.github/ISSUE_TEMPLATE/), [pull-request template](.github/PULL_REQUEST_TEMPLATE.md), and [checks guide](maintenance/checks.md) for everyday contributor use.

## Confirm project decisions

- **Licensing:** Confirm the terms for the framework text, documentation, scripts, and contributions. Replace the decision note in [LICENSE](LICENSE) with approved terms. The [source front matter](source/00-front-matter.md#agent-accountability) records a proposal, not an established repository license.
- **Conduct reports:** Name a private reporting contact and an alternative for reports involving that person. Update [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and [moderation guidance](maintenance/moderation.md).
- **Review assignments:** Confirm which GitHub users or teams will review which files before adding rules to [CODEOWNERS](.github/CODEOWNERS).
- **Framework governance:** Confirm who can approve source changes and releases, how versions are managed, and how the intended shared stewardship would work. Record approved decisions against [Section 8](source/08-framework-governance.md#8-framework-governance) without treating repository permissions as framework authority.
- **Assessment method:** If adding formal conformance keywords or an assessment method, define and approve them through a source change. The positions in [Section 5](source/05-conformance-and-assessment.md#5-conformance-and-assessment) alone do not settle those choices.
- **Acknowledgments:** Confirm any reviewer or contributor names to add to [Appendix B](framework/appendices/b-acknowledgments.md).

## Verify the hosted checks

After the documentation is pushed, confirm that the [GitHub workflow](.github/workflows/check-docs.yml) runs successfully on a pull request or a push to `master`. Local checks cover the files; they do not verify repository settings or a hosted run.

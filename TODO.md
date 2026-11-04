# Review and project decisions

The [framework pages](framework/README.md), contribution guides, and maintenance instructions are ready for review. Use this list to review the wording and settle decisions that cannot be filled in from the source alone.

## Internal and incomplete information review

The [document status](source/00-front-matter.md#status-of-this-document) limits circulation to Gravitee employees and engaged consultants and says the framework is not yet open for public review. Repository contribution guides and populated pages do not supersede that status. The source transcription remains unchanged; these findings identify material requiring review before public release.

| Reference | Finding and follow-up |
| --- | --- |
| [Source front matter](source/00-front-matter.md#status-of-this-document) and [source index](source/README.md) | Explicit internal-review and working-draft labels, including provenance notes across the source files. Confirm an approved source baseline and publication status before describing the AAF as released. |
| [Front-matter metadata](source/00-front-matter.md#agent-accountability) | Names the editor, steward, and an individual corporate feedback address. Confirm which attribution and feedback contact should appear in a public baseline; preserve existing source attribution during this review. |
| [Section 5](source/05-conformance-and-assessment.md#5-conformance-and-assessment) | Explicitly unfinished. Conformance positions are supplied, but formal keywords and assessment methodology remain undefined. The [derived explanation](framework/05-conformance-and-assessment.md) does not complete that method. |
| [Section 8](source/08-framework-governance.md#8-framework-governance) | Explicitly unfinished and describes pre-publication internal review. Versioning, change decisions, contribution adjudication, and transfer of stewardship need an approved governance process. [Repository governance](GOVERNANCE.md) and [release guidance](maintenance/releases.md) do not supply framework authority. |
| [Appendix B](source/appendices/b-acknowledgments.md#appendix-b-acknowledgments) | Contains only a development placeholder. Confirm reviewer and contributor credits; the [derived appendix](framework/appendices/b-acknowledgments.md) draws its existing credits from front matter. |
| [LICENSE](LICENSE) and [source license metadata](source/00-front-matter.md#agent-accountability) | Repository terms are not established; the source license is proposed. Obtain approved terms for text, documentation, scripts, and contributions. |
| [CODEOWNERS](.github/CODEOWNERS) | Comments only; no review assignments are configured. Confirm users or teams before adding rules. |
| [Conduct reporting](CODE_OF_CONDUCT.md#reporting-a-concern) and [moderation](maintenance/moderation.md) | The shared reporting address is documented, but an alternative for reports involving its handlers remains unconfirmed. |
| [Contribution guide](CONTRIBUTING.md), [proposal guide](contributing/proposing-changes.md), and [framework contents](framework/README.md) | Describe repository participation and populated documentation. They must be read alongside the internal source status, rather than as an announcement that public framework review has opened. |
| [Changelog](CHANGELOG.md) | Historical entries reference local accuracy reports, gap logs, and review work excluded from the repository. These records are not available in a fresh checkout; the entries do not establish that every framework issue is resolved. Review historical wording before publication. |
| [Repository instructions](AGENTS.md) | Previously required treating the AAF as final and suppressing status caveats. Corrected to preserve the internal status and flag unfinished work; entry points and affected derived pages now carry those caveats. |

“Internal” scope tags and references to internal agents describe control applicability, not document confidentiality ([Section 4](source/04-framework-core.md#4-the-framework-core-principles-and-controls)). They are retained.

## Review the documentation

- Read [Scope](framework/02-scope.md) first as the tone reference, then follow the framework reading order. Check that each explanation is clear without narrowing or expanding the requirement behind it.
- Review [Conformance and Assessment](framework/05-conformance-and-assessment.md), especially estate coverage, declared exceptions, organization-defined parameters, and evidence. These explain the positions in [Section 5](source/05-conformance-and-assessment.md#5-conformance-and-assessment); they do not supply a formal assessment method or certification scheme.
- Check the examples and descriptions in [Relationship to Existing Standards](framework/07-relationship-to-standards.md) against the linked primary sources. The page describes related work without claiming equivalence between standards.
- Review the [issue templates](.github/ISSUE_TEMPLATE/), [pull-request template](.github/PULL_REQUEST_TEMPLATE.md), and [checks guide](maintenance/checks.md) for everyday contributor use.

## Confirm project decisions

- **Licensing:** Confirm the terms for the framework text, documentation, scripts, and contributions. Replace the decision note in [LICENSE](LICENSE) with approved terms. The [source front matter](source/00-front-matter.md#agent-accountability) records a proposal, not an established repository license.
- **Conduct reports:** The reporting contact is [admin@agentaccountabilityframework.org](mailto:admin@agentaccountabilityframework.org), listed in the [Code of Conduct](CODE_OF_CONDUCT.md#reporting-a-concern) and [moderation guidance](maintenance/moderation.md). Confirm an alternative for reports involving the people handling that inbox.
- **Review assignments:** Confirm which GitHub users or teams will review which files before adding rules to [CODEOWNERS](.github/CODEOWNERS).
- **Framework governance:** Confirm who can approve source changes and releases, how versions are managed, and how the intended shared stewardship would work. Record approved decisions against [Section 8](source/08-framework-governance.md#8-framework-governance) without treating repository permissions as framework authority.
- **Assessment method:** If adding formal conformance keywords or an assessment method, define and approve them through a source change. The positions in [Section 5](source/05-conformance-and-assessment.md#5-conformance-and-assessment) alone do not settle those choices.
- **Acknowledgments:** Confirm any reviewer or contributor names to add to [Appendix B](framework/appendices/b-acknowledgments.md).

## Verify the hosted checks

After the documentation is pushed, confirm that the [GitHub workflow](.github/workflows/check-docs.yml) runs successfully on a pull request or a push to `master`. Local checks cover the files; they do not verify repository settings or a hosted run.

# Repository layout

The internal AAF source has been withdrawn from version control pending public AAF 1.0. Source links are suspended; existing derived content remains a working draft and has not been validated against 1.0. See the source link restoration record (maintained locally).
The source/ directory holds the complete Markdown source used for repository authoring. The numbered files in [framework/](framework/) are derived pages following the same section order. Each principle gets its own page so its introduction and controls can be read and reviewed together. Contribution guides, maintainer procedures, and GitHub configuration are grouped separately for ease of navigation.

## Root

| File | Purpose |
| --- | --- |
| [README.md](README.md) | Introduction and links to read, review, or contribute. |
| [LICENSE](LICENSE) | Decision note recording the licensing terms the project still needs to establish. |
| [CHANGELOG.md](CHANGELOG.md) | Changes by release, including affected controls and their significance. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to submit feedback or edits, with links to detailed contribution guides. |
| [GOVERNANCE.md](GOVERNANCE.md) | Repository participation and review, with the limits of repository permissions. |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community expectations, reporting contacts, and enforcement process. |
| [AGENTS.md](AGENTS.md) | Repository-specific instructions for AI assistants. |
| [REPOSITORY_LAYOUT.md](REPOSITORY_LAYOUT.md) | This file: layout choices and file purposes. |

## Source (withdrawn)

Use the AAF Markdown source for routine authoring. The provenance record documents the original document and transcription conventions. Source changes and derived-page coverage are tracked separately in [source coverage](maintenance/source-coverage.md).

| Path | Purpose |
| --- | --- |
| source/README.md | Authoring reading order, file and control indexes, source provenance, and update guidance. |
| source/00-front-matter.md | Original metadata, document status, abstract, and contents. |
| source/01-purpose.md | Section 1: Purpose. |
| source/02-scope.md | Section 2: Scope and boundary of management. |
| source/03-terminology.md | Section 3: Terminology conventions. |
| source/04-framework-core.md | Section 4 introduction: normative effect, control structure, domains, scope tags, and consequence. |
| source/principles/01-identity.md | Assign domain introduction; Principle 1 and controls 1.1–1.5. |
| source/principles/02-sponsor.md | Principle 2 and controls 2.1–2.5 (Assign). |
| source/principles/03-role.md | Align domain introduction; Principle 3 and controls 3.1–3.8. |
| source/principles/04-authority.md | Principle 4 and controls 4.1–4.14 (Align). |
| source/principles/05-oversight.md | Account domain introduction; Principle 5 and controls 5.1–5.8. |
| source/principles/06-recourse.md | Principle 6 and controls 6.1–6.5 (Account). |
| source/05-conformance-and-assessment.md | Section 5: Conformance and Assessment. |
| source/06-implementation-neutrality.md | Section 6: Implementation Neutrality. |
| source/07-relationship-to-standards.md | Section 7: Relationship to Existing Standards. |
| source/08-framework-governance.md | Section 8: Framework Governance. |
| source/appendices/a-terminology.md | Appendix A: definitions, each with a heading anchor. |
| source/appendices/b-acknowledgments.md | Appendix B: Acknowledgments. |

## Framework

These pages explain the framework in its established voice and reproduce the complete controls and formal definitions from source/. Consult [source coverage](maintenance/source-coverage.md) for the mapping.

| File | Purpose |
| --- | --- |
| [README.md](framework/README.md) | Contents and reading order, grouped by domain. |
| [01-purpose.md](framework/01-purpose.md) | Purpose, audience, and intended outcomes. |
| [02-scope.md](framework/02-scope.md) | Included and excluded subjects, plus the boundary of management. |
| [03-terminology.md](framework/03-terminology.md) | Concise definitions of six selected terms, each linked to the Markdown source. |
| [04-framework-core.md](framework/04-framework-core.md) | Domains, principle sequence, control structure, scope tags, and links to the principle pages. |
| [principles/01-identity.md](framework/principles/01-identity.md) | Identity principle and its controls. |
| [principles/02-sponsor.md](framework/principles/02-sponsor.md) | Sponsor principle and its controls. |
| [principles/03-role.md](framework/principles/03-role.md) | Role principle and its controls. |
| [principles/04-authority.md](framework/principles/04-authority.md) | Authority principle and its controls. |
| [principles/05-oversight.md](framework/principles/05-oversight.md) | Oversight principle and its controls. |
| [principles/06-recourse.md](framework/principles/06-recourse.md) | Recourse principle and its controls. |
| [05-conformance-and-assessment.md](framework/05-conformance-and-assessment.md) | What conformance covers and the evidence it needs; Section 5 leaves the formal assessment method undefined. |
| [06-implementation-neutrality.md](framework/06-implementation-neutrality.md) | The framework's position on implementation neutrality. |
| [07-relationship-to-standards.md](framework/07-relationship-to-standards.md) | Relationship to adjacent standards work. |
| [08-framework-governance.md](framework/08-framework-governance.md) | Stewardship described in the source and links to the repository contribution process. |
| [appendices/a-terminology.md](framework/appendices/a-terminology.md) | Authoritative definitions used by the controls. |
| [appendices/b-acknowledgments.md](framework/appendices/b-acknowledgments.md) | Confirmed source credits and how to propose additions. |

## Contribution, maintenance, and automation

The restoration guide (maintained locally) and removed-link inventory (maintained locally) track suspended source citations.

| Path | Purpose |
| --- | --- |
| [contributing/proposing-changes.md](contributing/proposing-changes.md) | How to prepare a change proposal and take it through review. |
| [contributing/editorial-guide.md](contributing/editorial-guide.md) | Writing and formatting conventions for framework edits. |
| [contributing/ai-assisted-contributions.md](contributing/ai-assisted-contributions.md) | Policy for contributing AI-assisted work. |
| [maintenance/checks.md](maintenance/checks.md) | How to run checks and interpret their limits. |
| [maintenance/releases.md](maintenance/releases.md) | Checks for preparing a release and the decisions needed before publication. |
| [maintenance/moderation.md](maintenance/moderation.md) | Discussion and issue triage, conduct enforcement, and escalation. |
| [maintenance/source-coverage.md](maintenance/source-coverage.md) | Maps PDF sections and controls to the complete Markdown source and tracks the separate status of derived framework pages, conversion review, and deliberate changes. |
| [assets/](assets/) | Documentation images and diagrams. |
| [scripts/check-docs.py](scripts/check-docs.py) | Local links and anchors, plus comparison of complete controls and definitions with the source. |
| [scripts/test_check_docs.py](scripts/test_check_docs.py) | Regression tests for the documentation checker. |
| [.github/CODEOWNERS](.github/CODEOWNERS) | Instructions for adding review assignments once GitHub users or teams are confirmed. |
| [.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/) | Templates for corrections, framework proposals, and questions. |
| [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) | Standard information requested from pull-request authors. |
| [.github/workflows/check-docs.yml](.github/workflows/check-docs.yml) | Runs the local documentation checks on proposed changes. |

The empty notification workflow has been removed. No custom notification service is configured.

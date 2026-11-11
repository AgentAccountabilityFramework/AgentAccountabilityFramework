# AAF 1.0 source for repository authoring

This directory contains the [Agent Accountability Framework 1.0 PDF](AAF-1.0.pdf) and its Markdown transcription. Use the PDF as the release reference and these Markdown files for review, stable citations, and authoring. The [framework pages](../../framework/README.md) explain the same specification.

Start with the [front matter](00-front-matter.md), the [scope and boundary rule](02-scope.md#boundary-of-management), and the [Framework Core](04-framework-core.md). Read each complete control with the [Appendix A definitions](appendices/a-terminology.md). See the [source coverage map](../../maintenance/source-coverage.md) for the corresponding framework pages.

## Reading order

| Source file | PDF pages |
| --- | --- |
| [00-front-matter.md](00-front-matter.md) | [1–2](AAF-1.0.pdf#page=1) |
| [01-purpose.md](01-purpose.md) | [3](AAF-1.0.pdf#page=3) |
| [02-scope.md](02-scope.md) | [3–4](AAF-1.0.pdf#page=3) |
| [03-terminology.md](03-terminology.md) | [4](AAF-1.0.pdf#page=4) |
| [04-framework-core.md](04-framework-core.md) | [5–7](AAF-1.0.pdf#page=5) |
| [principles/01-identity.md](principles/01-identity.md) | [7–11](AAF-1.0.pdf#page=7) |
| [principles/02-sponsor.md](principles/02-sponsor.md) | [11–14](AAF-1.0.pdf#page=11) |
| [principles/03-role.md](principles/03-role.md) | [14–19](AAF-1.0.pdf#page=14) |
| [principles/04-authority.md](principles/04-authority.md) | [19–28](AAF-1.0.pdf#page=19) |
| [principles/05-oversight.md](principles/05-oversight.md) | [28–34](AAF-1.0.pdf#page=28) |
| [principles/06-recourse.md](principles/06-recourse.md) | [34–38](AAF-1.0.pdf#page=34) |
| [05-conformance-and-assessment.md](05-conformance-and-assessment.md) | [38](AAF-1.0.pdf#page=38) |
| [06-implementation-neutrality.md](06-implementation-neutrality.md) | [38](AAF-1.0.pdf#page=38) |
| [07-relationship-to-standards.md](07-relationship-to-standards.md) | [38–39](AAF-1.0.pdf#page=38) |
| [08-framework-governance.md](08-framework-governance.md) | [39](AAF-1.0.pdf#page=39) |
| [appendices/a-terminology.md](appendices/a-terminology.md) | [40–45](AAF-1.0.pdf#page=40) |
| [appendices/b-acknowledgments.md](appendices/b-acknowledgments.md) | [46](AAF-1.0.pdf#page=46) |

## Control index

Control links use stable anchors of the form `#control-1-1`. Bare numbers such as `(1.2)` in the PDF refer to controls; section references explicitly say “Section” ([Section 4](04-framework-core.md)).

| Control | Title | Scope |
| --- | --- | --- |
| [1.1](principles/01-identity.md#control-1-1) | Unique, verifiable identity | Generic |
| [1.2](principles/01-identity.md#control-1-2) | Complete registry | Generic |
| [1.3](principles/01-identity.md#control-1-3) | Credential lifecycle | Generic |
| [1.4](principles/01-identity.md#control-1-4) | Credential custody and mediation | Generic |
| [1.5](principles/01-identity.md#control-1-5) | Verifiable action provenance | Generic |
| [2.1](principles/02-sponsor.md#control-2-1) | Named accountable sponsor | Generic |
| [2.2](principles/02-sponsor.md#control-2-2) | Sponsor capacity | Generic |
| [2.3](principles/02-sponsor.md#control-2-3) | Sponsor continuity | Generic |
| [2.4](principles/02-sponsor.md#control-2-4) | Sponsorship of spawned agents | Generic |
| [2.5](principles/02-sponsor.md#control-2-5) | Operator of record | External |
| [3.1](principles/03-role.md#control-3-1) | Documented, scoped purpose | Generic |
| [3.2](principles/03-role.md#control-3-2) | Measurable success criteria | Generic |
| [3.3](principles/03-role.md#control-3-3) | Readable beyond the deploying team | Generic |
| [3.4](principles/03-role.md#control-3-4) | Role versioning and change control | Generic |
| [3.5](principles/03-role.md#control-3-5) | Defined budget | Generic |
| [3.6](principles/03-role.md#control-3-6) | Autonomy level | Generic |
| [3.7](principles/03-role.md#control-3-7) | Model, harness, and instruction binding | Internal |
| [3.8](principles/03-role.md#control-3-8) | Declared dependencies and dependents | Generic |
| [4.1](principles/04-authority.md#control-4-1) | Enumerated authority | Generic |
| [4.2](principles/04-authority.md#control-4-2) | Role-derived least privilege | Generic |
| [4.3](principles/04-authority.md#control-4-3) | Bounded delegation | Generic |
| [4.4](principles/04-authority.md#control-4-4) | Single system of record, no bypass path | Generic |
| [4.5](principles/04-authority.md#control-4-5) | Time-bounded, revocable in real time | Generic |
| [4.6](principles/04-authority.md#control-4-6) | Authority is not content | Generic |
| [4.7](principles/04-authority.md#control-4-7) | Intent-bounded authorization | Generic |
| [4.8](principles/04-authority.md#control-4-8) | Bounded egress | Generic |
| [4.9](principles/04-authority.md#control-4-9) | Execution containment | Internal |
| [4.10](principles/04-authority.md#control-4-10) | Context and memory isolation | Internal |
| [4.11](principles/04-authority.md#control-4-11) | Data boundary enforcement | Generic |
| [4.12](principles/04-authority.md#control-4-12) | Separation of exposure | Generic |
| [4.13](principles/04-authority.md#control-4-13) | Registered tool and model definitions | Generic |
| [4.14](principles/04-authority.md#control-4-14) | Spawned-agent authority | Generic |
| [5.1](principles/05-oversight.md#control-5-1) | Complete, tamper-evident record | Generic |
| [5.2](principles/05-oversight.md#control-5-2) | Runtime deviation surfacing | Generic |
| [5.3](principles/05-oversight.md#control-5-3) | Pre-execution disposition for high-consequence actions | Generic |
| [5.4](principles/05-oversight.md#control-5-4) | Independently queryable audit trail | Generic |
| [5.5](principles/05-oversight.md#control-5-5) | Performance against role | Generic |
| [5.6](principles/05-oversight.md#control-5-6) | Evaluation before and during operation | Internal |
| [5.7](principles/05-oversight.md#control-5-7) | Adversarial testing | Internal |
| [5.8](principles/05-oversight.md#control-5-8) | Estate discovery and reconciliation | Generic |
| [6.1](principles/06-recourse.md#control-6-1) | Immediate suspension | Generic |
| [6.2](principles/06-recourse.md#control-6-2) | Rollback and containment paths | Generic |
| [6.3](principles/06-recourse.md#control-6-3) | Pre-defined escalation | Generic |
| [6.4](principles/06-recourse.md#control-6-4) | Reinstatement after review | Generic |
| [6.5](principles/06-recourse.md#control-6-5) | Complete decommissioning | Generic |

## Transcription and provenance

The Markdown preserves the release wording. It adds navigation, stable anchors, and links. Bullets and diagrams in the PDF present material that is also recorded in the source prose. PDF page numbers count from the cover. Source content appears between the transcription comments.

- PDF title: Agent Accountability Framework 1.0
- PDF length: 47 pages
- PDF SHA-256: `64d99984a02f27cbd0bc0e716e757ae4896cde583d06fb8e587ff76113bd43be`
- License: [CC BY-SA 4.0](../../LICENSE)

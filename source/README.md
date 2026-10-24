# AAF source for repository authoring

This directory is the repository's source of truth for AAF authoring: a complete Markdown transcription of [AAF.pdf](../AAF.pdf), version **0.9.4 — Working Draft**, dated **October 12, 2026**. Read these files instead of extracting the PDF for routine work. The [framework pages](../framework/README.md) are derived material and may still be incomplete.

## How to use this source

1. Read the [document status](00-front-matter.md#status-of-this-document), [scope and boundary rule](02-scope.md#boundary-of-management), [terminology conventions](03-terminology.md), and [framework core](04-framework-core.md).
2. Read the relevant principle and complete controls, including their Requirement, Rationale, and Assessment fields. Follow linked control and section references and consult the [Appendix A definitions](appendices/a-terminology.md).
3. Cite the specific source file and control or definition anchor when authoring derived pages. Track coverage in [maintenance/source-coverage.md](../maintenance/source-coverage.md).

Requirements are normative; Rationale and Assessment are informative in this draft. Appendix A definitions and the Section 2 boundary rule have normative effect, as stated in [Section 4](04-framework-core.md). Sections [5](05-conformance-and-assessment.md), [8](08-framework-governance.md), and [Appendix B](appendices/b-acknowledgments.md) retain their unfinished status. The license remains **proposed**, and the document remains in internal review ([front matter](00-front-matter.md)).

## Reading order

| Source file | PDF pages | Content |
| --- | --- | --- |
| [00-front-matter.md](00-front-matter.md) | 1–2 | Front matter, metadata, status, abstract, and original contents |
| [01-purpose.md](01-purpose.md) | 2–3 | Section 1: Purpose |
| [02-scope.md](02-scope.md) | 3–4 | Section 2: Scope and boundary of management |
| [03-terminology.md](03-terminology.md) | 4 | Section 3: Terminology conventions |
| [04-framework-core.md](04-framework-core.md) | 4–5 | Section 4: Framework Core introduction |
| [principles/01-identity.md](principles/01-identity.md) | 6–9 | Assign domain; Principle 1: Identity; controls 1.1–1.5 |
| [principles/02-sponsor.md](principles/02-sponsor.md) | 9–12 | Assign; Principle 2: Sponsor; controls 2.1–2.5 |
| [principles/03-role.md](principles/03-role.md) | 13–17 | Align domain; Principle 3: Role; controls 3.1–3.8 |
| [principles/04-authority.md](principles/04-authority.md) | 17–25 | Align; Principle 4: Authority; controls 4.1–4.14 |
| [principles/05-oversight.md](principles/05-oversight.md) | 26–30 | Account domain; Principle 5: Oversight; controls 5.1–5.8 |
| [principles/06-recourse.md](principles/06-recourse.md) | 30–33 | Account; Principle 6: Recourse; controls 6.1–6.5 |
| [05-conformance-and-assessment.md](05-conformance-and-assessment.md) | 33–34 | Section 5: Conformance and Assessment [to be developed] |
| [06-implementation-neutrality.md](06-implementation-neutrality.md) | 34 | Section 6: Implementation Neutrality |
| [07-relationship-to-standards.md](07-relationship-to-standards.md) | 34 | Section 7: Relationship to Existing Standards |
| [08-framework-governance.md](08-framework-governance.md) | 34–35 | Section 8: Framework Governance [to be developed] |
| [appendices/a-terminology.md](appendices/a-terminology.md) | 36–42 | Appendix A: Normative terminology definitions |
| [appendices/b-acknowledgments.md](appendices/b-acknowledgments.md) | 42 | Appendix B: Acknowledgments [to be developed] |

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

The transcription contains all 42 PDF pages, split into 17 source files. Only presentation changes were made: Markdown headings and tables, joined wrapped lines, linked cross-references, and navigation. Appendix A's two-column table is represented as one heading and definition per term. Domain introductions remain before their first principle, preserving Assign → Align → Account and the original principle order.

Text between the `Source transcription begins` and `Source transcription ends` comments is transcribed content; navigation, provenance, control page comments, anchors, and this index are editorial aids. Heading markup replaces field-label punctuation. Original wording, punctuation, draft placeholders, and human attribution are retained, including the duplicated period after “Appendix A.” in [Section 3](03-terminology.md). No assessment method, governance decision, or license grant has been added. External claims in the transcription are statements from this draft, not newly verified claims.

The PDF is retained locally for provenance and transcription audits and remains excluded by [.gitignore](../.gitignore). It is not needed for routine authoring. When updating the source baseline or resolving a suspected transcription error, compare the affected text with that PDF and record the correction in [source coverage](../maintenance/source-coverage.md) and the [changelog](../CHANGELOG.md). Keep proposed framework changes distinct from this transcription.

- PDF title metadata: Agent Accountability Framework v0.9.4 (Working Draft).
- PDF page numbering: physical pages counted from the first page, including the cover.
- PDF SHA-256: `a73b5b9ce3979d493bdff3354d2d67efcfac94171845effceeb809c7912810b7`.

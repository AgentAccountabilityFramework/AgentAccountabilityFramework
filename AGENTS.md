# Repository instructions

## Source of truth

- Always review the [Markdown source index](source/README.md) and relevant files in [source/](source/) before writing, editing, or answering anything about the AAF. Read the relevant sections, complete controls, definitions, and linked cross-references; do not rely on memory or repository summaries.
- The Markdown source is authoritative for repository authoring. It transcribes the AAF; [framework/](framework/) contains derived pages that may be incomplete. If repository text conflicts with the source, identify the discrepancy and align it with the source. Label proposed departures explicitly; never present them as existing requirements or silently rewrite the source baseline.
- Use the Markdown source instead of the PDF for routine work. The original PDF, documented in the [source provenance record](source/README.md#transcription-and-provenance), is retained only for provenance, source-baseline updates, and suspected transcription errors; it remains excluded by [.gitignore](.gitignore). Request it only when such an audit requires it and it is unavailable or unreadable. Do not add it to version control without explicit authorization. Record source corrections in [source coverage](maintenance/source-coverage.md) and the changelog.
- Treat the current AAF as final for authoring until explicitly superseded. Use direct, present-tense language in repository content and responses; omit provisional-status labels and pending-finalization caveats, even when the source uses them. This authoring convention overrides source-status wording for derived content. Preserve the original source transcription for provenance, and do not invent missing requirements, assessment methods, governance decisions, release events, or licensing terms.

## Framework fidelity

- Preserve the domain grouping and principle order from [Section 4](source/04-framework-core.md): **Assign** — Identity, Sponsor; **Align** — Role, Authority; **Account** — Oversight, Recourse.
- Preserve control IDs, titles, scope tags (`Generic`, `Internal`, `External`), and the separate Requirement, Rationale, and Assessment fields.
- Requirements are normative; Rationale and Assessment are informative ([Section 4](source/04-framework-core.md)). Preserve the normative effect of [Appendix A definitions](source/appendices/a-terminology.md) and the [Section 2 boundary rule](source/02-scope.md#boundary-of-management).
- Use the source's defined terminology. Preserve its scope exclusions and the rule that controls are satisfied within the organization's own boundary. Do not equate accountability with model safety or general security ([Section 2](source/02-scope.md), [Section 5](source/05-conformance-and-assessment.md), and [Appendix A](source/appendices/a-terminology.md)).

## Writing and linkbacks

- Use concise, factual, vendor-neutral language. Remove filler, repetition, promotional claims, and extraneous prose.
- Describe required outcomes without prescribing a vendor, product, architecture, platform, protocol, or methodology ([Section 6](source/06-implementation-neutrality.md)).
- Link AAF claims, summaries, and adaptations to the relevant Markdown file in [source/](source/README.md), naming the exact section, principle, control, or appendix. Use stable control anchors such as [Control 1.1](source/principles/01-identity.md#control-1-1) and definition heading anchors. Outside `source/`, all AAF source links must target Markdown files and section or control anchors in `source/`. PDF links belong only in `source/` for provenance. Omit version numbers from citation labels, links, and accompanying source notes outside `source/`.
- Use relative links for repository navigation and verified anchors for control references. Include source linkbacks on derived framework pages and maintain the mapping in [maintenance/source-coverage.md](maintenance/source-coverage.md) when converting or changing framework content.
- Link external factual claims to their original sources. Verify destinations and anchors; never fabricate links or citations.
- Follow [REPOSITORY_LAYOUT.md](REPOSITORY_LAYOUT.md). Keep related navigation and cross-references consistent when moving or renaming content.

## Changes, validation, and commits

- Inspect the working tree first; preserve unrelated work and stage only changes belonging to the task.
- Keep [CHANGELOG.md](CHANGELOG.md) up to date in every change commit. Record changes under `Unreleased`, link affected files and source references, identify affected controls when applicable, and explain substantive impact. Do not invent release dates or versions.
- Review the final diff against the relevant Markdown source; check links, anchors, control references, and Markdown formatting. For source-baseline changes or transcription corrections, also compare the affected text with the PDF. Run `git diff --check` and applicable repository checks. An empty checker is not validation; report unavailable checks accurately.
- Always commit completed changes with a detailed commit message: a clear subject and a body explaining what changed, why, relevant source sections or controls, and validation results or limitations.
- Attribute development only to the human directing the work. Use the configured human Git author and committer identity; if missing or ambiguous, request the correct identity rather than inventing one.
- Never credit yourself, ChatGPT, or any AI assistant in authorship, acknowledgments, commit trailers, or generated-by signatures. Preserve existing human attribution and source citations.

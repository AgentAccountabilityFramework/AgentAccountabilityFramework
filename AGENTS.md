# Repository instructions

## Source of truth

- Always review the [Markdown source index](source/v1.0/README.md) and the relevant source files before writing, editing, or answering anything about the AAF. Read the relevant sections, complete controls, definitions, and linked cross-references; do not rely on memory or repository summaries.
- The [1.0 PDF](source/v1.0/AAF-1.0.pdf) is the release reference. Its Markdown transcription is authoritative for routine repository authoring. It transcribes the AAF; [framework/](framework/) contains derived pages that may be incomplete. If repository text conflicts with the source, identify the discrepancy and align it with the source. Label proposed departures explicitly; never present them as existing requirements or silently rewrite the source baseline.
- Use the Markdown source instead of the PDF for routine work. Use the versioned PDF, documented in the [source provenance record](source/v1.0/README.md#transcription-and-provenance), for source-baseline updates and suspected transcription errors. Keep earlier internal drafts and local review files out of version control. Record source corrections in [source coverage](maintenance/source-coverage.md) and the changelog.
- Use direct language for existing requirements and preserve the 1.0 transcription for provenance. Section 5 leaves formal assessment methodology and conformance keywords undefined. Section 8 leaves the governing body, decision rights, and framework versioning process undefined. Keep proposed changes separate from the release baseline.

## Framework fidelity

- Preserve the domain grouping and principle order from [Section 4](source/v1.0/04-framework-core.md): **Assign** — Identity, Sponsor; **Align** — Role, Authority; **Account** — Oversight, Recourse.
- Preserve control IDs, titles, scope tags (`Generic`, `Internal`, `External`), and the separate Requirement, Rationale, and Assessment fields.
- Requirements are normative; Rationale and Assessment are informative ([Section 4](source/v1.0/04-framework-core.md)). Preserve the normative effect of [Appendix A definitions](source/v1.0/appendices/a-terminology.md) and the [Section 2 boundary rule](source/v1.0/02-scope.md#boundary-of-management).
- Use the source's defined terminology. Preserve its scope exclusions and the rule that controls are satisfied within the organization's own boundary. Do not equate accountability with model safety or general security ([Section 2](source/v1.0/02-scope.md), [Section 5](source/v1.0/05-conformance-and-assessment.md), and [Appendix A](source/v1.0/appendices/a-terminology.md)).

## Writing and linkbacks

- Use concise, factual, vendor-neutral language. Remove filler, repetition, promotional claims, and extraneous prose.
- Follow the voice established in [Scope](framework/02-scope.md) and the [editorial guide](contributing/editorial-guide.md#use-the-established-voice): address the reader directly, use familiar verbs and concrete examples, and explain technical terms. Preserve defined meanings, applicability, and every obligation when simplifying prose; keep complete control fields and formal definitions aligned with the source.
- Describe required outcomes without prescribing a vendor, product, architecture, platform, protocol, or methodology ([Section 6](source/v1.0/06-implementation-neutrality.md)).
- Link AAF claims, summaries, and adaptations to the relevant [versioned Markdown source](source/v1.0/README.md). Use stable section, control, and definition anchors such as [Control 1.1](source/v1.0/principles/01-identity.md#control-1-1). Use the PDF for release navigation and page-level provenance.
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

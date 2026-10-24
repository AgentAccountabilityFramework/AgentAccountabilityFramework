# Repository instructions

## Source of truth

- Always review [AAF.pdf](AAF.pdf) before writing, editing, or answering anything about the AAF. Read the relevant sections, controls, definitions, and cross-references; do not rely on memory or repository summaries.
- The PDF is authoritative for AAF content. If repository text conflicts with it, identify the discrepancy and align the text with the PDF. Label proposed departures explicitly; never present them as existing requirements.
- The PDF is a local prerequisite currently excluded by [.gitignore](.gitignore). If unavailable or unreadable, request it before making AAF claims. Do not add it to version control without explicit authorization.
- Preserve the PDF's draft status and unresolved sections. Do not invent requirements, assessment methods, governance decisions, release status, or licensing terms.

## Framework fidelity

- Preserve the domain grouping and principle order from [AAF.pdf, Section 4](AAF.pdf): **Assign** — Identity, Sponsor; **Align** — Role, Authority; **Account** — Oversight, Recourse.
- Preserve control IDs, titles, scope tags (`Generic`, `Internal`, `External`), and the separate Requirement, Rationale, and Assessment fields.
- Requirements are normative; Rationale and Assessment are informative in the current draft. Preserve the normative effect of Appendix A definitions and the Section 2 boundary rule ([AAF.pdf, Sections 2–4 and Appendix A](AAF.pdf)).
- Use the PDF's defined terminology. Preserve its scope exclusions and the rule that controls are satisfied within the organization's own boundary. Do not equate accountability with model safety or general security ([AAF.pdf, Sections 2, 5, and Appendix A](AAF.pdf)).

## Writing and linkbacks

- Use concise, factual, vendor-neutral language. Remove filler, repetition, promotional claims, and extraneous prose.
- Describe required outcomes without prescribing a vendor, product, architecture, platform, protocol, or methodology ([AAF.pdf, Section 6](AAF.pdf)).
- Link AAF claims, summaries, and adaptations back to [AAF.pdf](AAF.pdf), naming the exact section, principle, control, or appendix. Add a verified PDF page fragment where useful.
- Use relative links for repository navigation and verified anchors for control references. Include source linkbacks on derived framework pages and maintain the mapping in [maintenance/source-coverage.md](maintenance/source-coverage.md) when converting or changing framework content.
- Link external factual claims to their original sources. Verify destinations and anchors; never fabricate links or citations.
- Follow [REPOSITORY_LAYOUT.md](REPOSITORY_LAYOUT.md). Keep related navigation and cross-references consistent when moving or renaming content.

## Changes, validation, and commits

- Inspect the working tree first; preserve unrelated work and stage only changes belonging to the task.
- Keep [CHANGELOG.md](CHANGELOG.md) up to date in every change commit. Record changes under `Unreleased`, link affected files and source references, identify affected controls when applicable, and explain substantive impact. Do not invent release dates or versions.
- Review the final diff against the PDF; check links, anchors, control references, and Markdown formatting. Run `git diff --check` and applicable repository checks. An empty checker is not validation; report unavailable checks accurately.
- Always commit completed changes with a detailed commit message: a clear subject and a body explaining what changed, why, relevant source sections or controls, and validation results or limitations.
- Attribute development only to the human directing the work. Use the configured human Git author and committer identity; if missing or ambiguous, request the correct identity rather than inventing one.
- Never credit yourself, ChatGPT, or any AI assistant in authorship, acknowledgments, commit trailers, or generated-by signatures. Preserve existing human attribution and source citations.

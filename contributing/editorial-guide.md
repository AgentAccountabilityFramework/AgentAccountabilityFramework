# Editorial guide

Write for readers who may be new to the framework. Use direct, concise, vendor-neutral language, define unfamiliar terms, and explain the reason for a change. Prefer specific examples when they clarify a point, without implying that an example is a required implementation.

## Preserve the source

The [Markdown source](../source/README.md) is the authoring reference. Read the relevant section, complete controls, definitions, and linked cross-references before editing derived content. Preserve control IDs, titles, scope tags, and separate Requirement, Rationale, and Assessment fields. Requirements are normative; Rationale and Assessment are informative ([Section 4](../source/04-framework-core.md)). Preserve the effect of the [boundary rule](../source/02-scope.md#boundary-of-management) and [definitions](../source/appendices/a-terminology.md). Do not introduce a product, architecture, or method as a requirement ([Section 6](../source/06-implementation-neutrality.md)).

Link framework claims and adaptations to the relevant source section, control, or definition, using relative Markdown links and stable control anchors. Keep proposals distinct from the existing source. For transcription corrections, follow the provenance and coverage process in the [source index](../source/README.md).

## Make changes easy to review

Use descriptive headings, short paragraphs, and lists when they improve scanning. Check spelling, links, anchors, and cross-references. Update navigation when files move and record the impact in [CHANGELOG.md](../CHANGELOG.md). Follow the [repository layout](../REPOSITORY_LAYOUT.md) and [contribution guide](../CONTRIBUTING.md).

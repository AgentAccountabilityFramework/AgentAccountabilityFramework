# Editorial guide

Write for readers who may be new to the framework. Use direct, concise, vendor-neutral language, define unfamiliar terms, and explain the reason for a change. Prefer specific examples when they clarify a point, without implying that an example is a required implementation.

## Use the established voice

Use the [Scope page](../framework/02-scope.md) as the tone reference. Address the reader as “you” or “your organization” when explaining what they do. Prefer familiar verbs: an organization runs an agent, names a sponsor, records an action, or stops access.

Explain an idea before adding detail. Keep each paragraph focused on one point, and use lists for things the reader needs to compare. A short, recognizable example can make a boundary clearer than another abstract explanation.

Keep technical terms when they carry a specific meaning, and explain them where readers first need them. For example, explain “normative” as something you must use when deciding whether a requirement is met. Do not replace a defined term with an everyday word if that changes its meaning.

Plain language must preserve the obligation. “Record the agent's actions” is useful introductory wording, but it cannot replace a requirement specifying which events to record, how to protect the record, and how long to retain it. Keep complete control fields and formal definitions aligned with the source; put explanations around them. Check words such as “every,” “only,” “before,” and “within” carefully, because changing them can change the requirement.

## Preserve the source

The [Markdown source](../source/v1.0/README.md) is the authoring reference. Read the relevant section, complete controls, definitions, and linked cross-references before editing derived content. Preserve control IDs, titles, scope tags, and separate Requirement, Rationale, and Assessment fields. Requirements are normative; Rationale and Assessment are informative ([Section 4](../source/v1.0/04-framework-core.md)). Preserve the effect of the [boundary rule](../source/v1.0/02-scope.md#boundary-of-management) and [definitions](../source/v1.0/appendices/a-terminology.md). Do not introduce a product, architecture, or method as a requirement ([Section 6](../source/v1.0/06-implementation-neutrality.md)).

Link framework claims and adaptations to the relevant source section, control, or definition, using relative Markdown links and stable control anchors. Keep proposals distinct from the existing source. For transcription corrections, follow the provenance and coverage process in the [source index](../source/v1.0/README.md).

## Make changes easy to review

Use descriptive headings, short paragraphs, and lists when they improve scanning. Check spelling, links, anchors, and cross-references. Update navigation when files move and record the impact in [CHANGELOG.md](../CHANGELOG.md). Follow the [repository layout](../REPOSITORY_LAYOUT.md) and [contribution guide](../CONTRIBUTING.md).

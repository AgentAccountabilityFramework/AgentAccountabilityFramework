# Source gaps

These are the remaining issues from the approved review items. Each one points to missing material or wording that doesn't line up. A possible reader question, on its own, isn't a gap. The original controls stay as written.

The entry numbers stay the same so earlier references still work for the items kept here.

## G1. Formal conformance assessment

[Section 5](source/05-conformance-and-assessment.md#5-conformance-and-assessment) describes what a conformance claim covers, but explicitly leaves the formal assessment method and conformance keywords undefined. [Section 3](source/03-terminology.md#3-terminology) also points to Section 5 for those keywords.

**What's needed:** The assessment method promised by Section 5. Until then, use the control Requirements to decide whether a control is met, as [Section 4](source/04-framework-core.md#4-the-framework-core-principles-and-controls) directs. The missing method doesn't make the controls unusable.

## G4. Operator-of-record applicability to dependencies

[Control 2.5](source/principles/02-sponsor.md#control-2-5) is tagged External, but its Requirement also covers outside tools and models used by agents your organization runs. [Appendix A](source/appendices/a-terminology.md#scope-tag) defines External as applying to external agents only. The [boundary rule](source/02-scope.md#boundary-of-management) supports the dependency coverage stated in the Requirement.

**What needs fixing:** Make the tag and its definition line up with the control's stated coverage. The dependency obligation is already written down; this is a labeling mismatch, not a missing obligation.

## G5. Acceptance of missing operator arrangements

[Control 2.5](source/principles/02-sponsor.md#control-2-5) requires an operating organization, an agreement, and a named contact. Its Rationale and Assessment explain how a sponsor can accept a tool or model dependency when the arrangement isn't available, using compensating controls. That exception isn't in the Requirement, which [Section 4](source/04-framework-core.md#4-the-framework-core-principles-and-controls) says is the basis for passing the control.

**What needs fixing:** Bring the Requirement and the dependency-acceptance guidance into agreement. The practical guidance is there; the issue is whether accepting the dependency also satisfies the Requirement. The Assessment separately says an external agent can't act when the required operator information is missing.

## G6. Permitted delegation and the assessment prohibition

[Control 4.3's Assessment](source/principles/04-authority.md#control-4-3) says no mechanism exists for an agent to grant another agent authority. But [Control 4.14's Requirement](source/principles/04-authority.md#control-4-14) explicitly allows a parent to delegate authority to a spawned agent. The [Delegation definition](source/appendices/a-terminology.md#delegation) also includes agent principals.

**What needs fixing:** Narrow the Assessment sentence so it doesn't rule out the delegation the Requirements allow. The Requirements take precedence under [Section 4](source/04-framework-core.md#4-the-framework-core-principles-and-controls); this is an assessment wording problem, not a ban on parent delegation.

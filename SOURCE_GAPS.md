# Source gaps

This log records gaps reviewed during the accuracy report review. Each entry identifies the source evidence, what remains unknown, and the clarification needed. Documentation can flag a gap; resolving it requires an authoritative source or a framework decision. Further entries are added as the review proceeds.

## G1. Formal conformance assessment

**Status:** Open. The documentation explains the limitation; the assessment method remains unspecified.

**Problem:** The source gives conformance positions but does not supply formal conformance keywords or a complete assessment methodology. It does not establish a certification scheme.

**Evidence:** [Section 3](source/03-terminology.md#3-terminology) points formal conformance keywords to Section 5. [Section 4](source/04-framework-core.md#4-the-framework-core-principles-and-controls) makes Section 5 informative, bases conformance on control Requirements, and directs formal assessment methodology to Section 5. [Section 5](source/05-conformance-and-assessment.md#5-conformance-and-assessment) describes positions and leaves formal keywords and methodology undefined.

**Clarification needed:** An authoritative assessment methodology and formal conformance vocabulary. Any claim of certification also needs evidence of an established certification scheme; none is supplied by these passages.

**Documentation treatment:** [Conformance and Assessment](framework/05-conformance-and-assessment.md) explains these limits and retains control Requirements as the basis for conformance. Review piece 2; audit finding C2.

## G2. Confidence thresholds in conformance statements

**Status:** Open. Both source provisions are identified; disclosure policy remains unspecified.

**Problem:** Section 5 says every organization-defined threshold is published in the conformance statement. Control 3.3 limits confidence-threshold disclosure to parties with a need to know. The source does not explain how the statement meets both provisions.

**Evidence:** [Section 5](source/05-conformance-and-assessment.md#5-conformance-and-assessment) includes every organization-defined threshold among the published parameters. [Control 3.3 Requirement](source/principles/03-role.md#control-3-3) restricts disclosure of confidence thresholds and says role readability does not make them public.

**Clarification needed:** Who receives the conformance statement and how confidential confidence thresholds are represented or disclosed within it. The source does not establish whether a restricted statement, separate disclosure, or another arrangement is intended.

**Documentation treatment:** [What to publish](framework/05-conformance-and-assessment.md#what-to-publish) flags the gap without choosing an audience or inventing an omission rule. Review piece 3; audit findings C2 and U3.

## G3. Authoring convention and release evidence

**Status:** Open. The authoring convention remains in effect; evidence of subsequent release, governance, or licensing decisions is not supplied by the source.

**Problem:** Treating the framework as final for repository authoring does not establish a release event, completed framework governance, or an approved license grant.

**Evidence:** [Repository authoring instructions](AGENTS.md#source-of-truth) establish the final-for-authoring convention while prohibiting invented release events, governance decisions, and licensing terms. The [source front matter](source/00-front-matter.md#agent-accountability) records a proposed license, and its [status section](source/00-front-matter.md#status-of-this-document) records internal review ahead of public release. [Section 8](source/08-framework-governance.md#8-framework-governance) describes stewardship and leaves governance mechanics unspecified. These passages do not establish whether later decisions exist outside the supplied source.

**Clarification needed:** An authoritative decision record or approved successor source establishing any subsequent release, governance arrangements, or license grant. If one exists, identify which source statements it supersedes and the intended treatment of status in derived pages.

**Documentation treatment:** Preserve the current authoring convention and source transcription. Record the evidence limit without inferring a release, governance decision, or license grant. Review piece 6; audit finding U1.

## G4. Operator-of-record applicability to dependencies

**Status:** Open. Control 2.5's scope tag and dependency obligations remain unchanged.

**Problem:** Control 2.5 is tagged External, but its Requirement also covers external tools and models used by agents the organization operates. The formal scope-tag definition says External applies to external agents only.

**Evidence:** [Control 2.5](source/principles/02-sponsor.md#control-2-5) carries the External tag and requires an operator of record for both admitted external agents and external tool/model dependencies of internally operated agents. [Appendix A — Scope tag](source/appendices/a-terminology.md#scope-tag) limits External to external agents. The [Section 2 boundary rule](source/02-scope.md#boundary-of-management) also directs internally operated agents' uncontrolled dependencies to an operator of record under Control 2.5.

**Clarification needed:** How the External tag applies to the dependency obligations in Control 2.5, and whether the tag, definition, or control structure needs an authoritative correction. The source supplies no explicit reconciliation of these passages.

**Documentation treatment:** Preserve the complete Requirement and existing tag. Do not omit dependency obligations solely on the basis of the tag or silently retag the control. Review piece 7; audit finding U2, applicability portion. The separate dependency-acceptance question is reserved for its own review.

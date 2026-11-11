# Principle 2: Sponsor

[Framework contents](../README.md) · [Previous: Identity](01-identity.md) · [Next: Role](03-role.md)

**Domain:** Assign

**Source:** [Section 4, Principle 2](../../source/v1.0/principles/02-sponsor.md#principle-2-sponsor).

Name the human who answers for each agent: why it exists, what its job is, what authority it holds, and what it does. Establish that sponsorship before defining the role and authority, and keep it in place throughout the agent's lifecycle. External and spawned agents also need an internal sponsor. For an external agent, the operator of record adds another line of accountability; it does not replace the sponsor.

The Requirement states what must be met. Rationale explains why, and Assessment describes supporting evidence; both provide guidance ([Section 4](../../source/v1.0/04-framework-core.md#4-the-framework-core-principles-and-controls)). Apply the controls using the [boundary rule](../../source/v1.0/02-scope.md#boundary-of-management) and [definitions](../../source/v1.0/appendices/a-terminology.md#appendix-a-terminology).

<a id="control-2-1"></a>

## Control 2.1 — Named accountable sponsor

**Scope:** Generic

**Source:** [Control 2.1](../../source/v1.0/principles/02-sponsor.md#control-2-1).

### Requirement

Every agent maps at all times to exactly one accountable human sponsor and to an owning team, both recorded in the registry ([1.2](../../source/v1.0/principles/01-identity.md#control-1-2)). The sponsor is a named individual, not a team, a role title, or a service account. Ownership is also recorded for each agent class (the agents sharing a model, an agent type, a harness, or a workload label), so that when a whole class must be halted ([6.1](../../source/v1.0/principles/06-recourse.md#control-6-1)) there is a named person accountable for the decision and its consequences. This includes every external agent admitted to act in the organization: its sponsor is the internal person who answers for its admission ([1.2](../../source/v1.0/principles/01-identity.md#control-1-2)), for its role in the organization ([3.1](../../source/v1.0/principles/03-role.md#control-3-1)), and for the authority granted to it ([4.1](../../source/v1.0/principles/04-authority.md#control-4-1)). The operator of record ([2.5](../../source/v1.0/principles/02-sponsor.md#control-2-5)) does not replace the internal sponsor. The sponsor has acknowledged the sponsorship, the consequence of answering for an agent is defined by the organization in its own management processes and known to the sponsor, and the organization declares a limit on the number of agents a sponsor may hold, counted including spawned agents; a sponsor at the limit is assigned no more.

### Rationale

Accountability terminates in a person, not a system. A team can operate an agent, but a team cannot answer for it in the way a person can; diffuse ownership is functionally no ownership. Recording the owning team alongside the sponsor places the agent inside the organization's existing structures for budget, review, and security instead of leaving it a personal project. Class-level ownership exists because some failures arrive by class: a model that changes behavior, a harness with a vulnerability, a workload type that turns out to have been misconfigured. Halting every agent of that class is a decision someone must own. For an external agent, the internal sponsor is who the organization holds accountable, and the operator of record ([2.5](../../source/v1.0/principles/02-sponsor.md#control-2-5)) is who the sponsor reaches when recourse must extend beyond the boundary.

### Assessment

“Whose agent is this?” is answerable, with a named individual and an owning team, for 100% of registry entries on the day of assessment. No entry resolves to a group alias, a vacant position, or a system identity. Every agent class in use resolves to a named owner, and the owner of a sampled agent class can state what halting it would affect. Every external agent identity resolves to an internal sponsor in the same way. Every sponsorship shows the sponsor’s acknowledgement, and no sponsor exceeds the declared limit.

<a id="control-2-2"></a>

## Control 2.2 — Sponsor capacity

**Scope:** Generic

**Source:** [Control 2.2](../../source/v1.0/principles/02-sponsor.md#control-2-2).

### Requirement

The sponsor holds, directly or through a defined path, the authority to re-scope the agent's role ([3.1](../../source/v1.0/principles/03-role.md#control-3-1), [3.4](../../source/v1.0/principles/03-role.md#control-3-4)), revoke its authority ([4.5](../../source/v1.0/principles/04-authority.md#control-4-5)), and suspend or decommission it ([6.1](../../source/v1.0/principles/06-recourse.md#control-6-1), [6.5](../../source/v1.0/principles/06-recourse.md#control-6-5)). For an external agent, capacity means the ability to re-scope the role of the engagement, revoke its credential and authority at the organization’s boundary, and reach the operator of record ([2.5](../../source/v1.0/principles/02-sponsor.md#control-2-5)).

### Rationale

A sponsor who cannot change what the agent does or stop it is answerable in name only. Capacity is what distinguishes sponsorship from attribution: the sponsor is the person the organization can hold responsible because the sponsor is a person who could have acted.

### Assessment

For sampled agents, the sponsor demonstrates, or the record shows, an exercised path to re-scoping, revocation, or suspension that did not require escalation to a party outside the escalation set defined before the exercise ([6.3](../../source/v1.0/principles/06-recourse.md#control-6-3)) and that completed within the windows declared under [Section 5](../../source/v1.0/05-conformance-and-assessment.md); an exercise that required escalation beyond the set, or exceeded the window, fails.

<a id="control-2-3"></a>

## Control 2.3 — Sponsor continuity

**Scope:** Generic

**Source:** [Control 2.3](../../source/v1.0/principles/02-sponsor.md#control-2-3).

### Requirement

A change to the sponsor or the owning team, including departure, transfer, or role change, triggers automatic reassignment or decommissioning within a defined window. Reassignment takes effect on the new sponsor’s recorded acknowledgement; until then the agent is held by a named member of the escalation set ([6.3](../../source/v1.0/principles/06-recourse.md#control-6-3)), and an agent not acknowledged within the window is suspended ([6.1](../../source/v1.0/principles/06-recourse.md#control-6-1)). No agent is unsponsored at any point in its lifecycle, and this applies equally to the internal sponsor of an external agent.

### Rationale

An agent whose sponsor has left the organization holds authority with no one answerable for it, which is exactly the condition this framework exists to prevent. The trigger makes sponsorship a standing invariant instead of a fact checked once at provisioning.

### Assessment

The assessor can produce evidence of the trigger firing: a historical sponsor departure or team change that resulted in reassignment or decommissioning within the defined window, with no interval during which the agent held enforceable authority without a sponsor of record.

<a id="control-2-4"></a>

## Control 2.4 — Sponsorship of spawned agents

**Scope:** Generic

**Source:** [Control 2.4](../../source/v1.0/principles/02-sponsor.md#control-2-4).

### Requirement

An agent created by another agent is sponsored by its parent’s sponsor from the moment it exists, and the sponsor’s accountability for it is the same as for the parent. The parent agent is recorded as the delegating principal ([4.3](../../source/v1.0/principles/04-authority.md#control-4-3)) and may be the accountable party for the spawned agent’s conduct within the organization’s management structure, but accountability still terminates in the sponsor. A spawned agent is identified ([1.1](../../source/v1.0/principles/01-identity.md#control-1-1)), enrolled ([1.2](../../source/v1.0/principles/01-identity.md#control-1-2)), and governed under every principle; it is not an extension of its parent’s session. An agent is created inside the organization only through the organization’s own admission ([1.2](../../source/v1.0/principles/01-identity.md#control-1-2)) and only by a parent whose authority permits it ([4.14](../../source/v1.0/principles/04-authority.md#control-4-14)). An external agent cannot create an agent inside the organization except through that admission; an agent so admitted is operated by the organization, sponsored by the external parent’s internal sponsor ([2.1](../../source/v1.0/principles/02-sponsor.md#control-2-1)), and holds at most the authority its parent holds in the organization. An agent spawned outside the boundary is an external agent when it acts in the organization.

### Rationale

Agents will create agents. Without inheritance, each spawned agent is an unsponsored actor, and a parent agent becomes a way of manufacturing agents to which none of the organization’s accountability attaches. Inheritance keeps the line of accountability unbroken: however deep the tree, the question “whose agent is this?” has the same answer at every level.

### Assessment

For a sampled spawned agent, the registry shows its sponsor as its parent’s sponsor and its parent as its delegating principal, and the record under control [5.1](../../source/v1.0/principles/05-oversight.md#control-5-1) reconstructs the chain from the spawned agent to the sponsor. No agent in the estate whose creator is an agent lacks a sponsor of record.

<a id="control-2-5"></a>

## Control 2.5 — Operator of record

**Scope:** External

**Source:** [Control 2.5](../../source/v1.0/principles/02-sponsor.md#control-2-5).

### Requirement

Every external agent admitted to act in the organization, and every external tool or model on which an agent the organization operates depends, maps to a verified operating organization, an agreement that assigns accountability for its conduct and for the controls the organization cannot apply from within its own boundary, and a named accountable contact at the operator. The operator of record is the second line of accountability: the internal sponsor ([2.1](../../source/v1.0/principles/02-sponsor.md#control-2-1)) answers for admission, role, and authority inside the organization, and relies on the operator of record for recourse that must reach beyond the boundary.

### Rationale

The organization cannot run an agent it does not operate, and it cannot apply this framework inside a vendor. What it can do is name the person inside who answers for the engagement ([2.1](../../source/v1.0/principles/02-sponsor.md#control-2-1)), and hold the organization that operates the agent to an agreement with a named person on the other end of it. Without an operator of record, recourse stops at the credential the organization can revoke. Where an operator of record cannot be obtained on the operator’s terms, as for a commodity model or tool, the internal sponsor records acceptance of the gap together with the compensating controls applied at the boundary ([1.4](../../source/v1.0/principles/01-identity.md#control-1-4), [3.8](../../source/v1.0/principles/03-role.md#control-3-8), [4.8](../../source/v1.0/principles/04-authority.md#control-4-8), [4.11](../../source/v1.0/principles/04-authority.md#control-4-11)), and the dependency is recorded as accepted rather than ungoverned. The operator’s identity and reachability are verified before admission and re-verified on a defined cadence; an operator that cannot be reached is a change event for every agent and dependency it operates.

### Assessment

For every external agent identity in the registry, and for every external tool or model an internal agent depends on, the assessor can produce the operating organization, the agreement, the operator contact, and the internal sponsor. An external agent for which any of these is missing is not permitted to act, and a dependency for which any is missing is recorded either as accepted, with its compensating controls and the sponsor who accepted it, or as ungoverned under control [3.8](../../source/v1.0/principles/03-role.md#control-3-8).

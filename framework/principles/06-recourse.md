# Principle 6: Recourse

[Framework contents](../README.md) · [Previous: Oversight](05-oversight.md) · [Next: Conformance and Assessment](../05-conformance-and-assessment.md)

**Domain:** Account

**Source:** [Section 4, Principle 6](../../source/v1.0/principles/06-recourse.md#principle-6-recourse).

Have a way to stop agents, contain or reverse the effects of their actions, and escalate an incident. Decide explicitly whether an agent can return to operation, and retire it completely when it is no longer needed. These measures cover individual agents and agent classes, with attention to agents that depend on them. Here, recourse means your organization's ability to act on its agents. Redress for people affected by automated decisions is outside the framework's scope.

The Requirement states what must be met. Rationale explains why, and Assessment describes supporting evidence; both provide guidance ([Section 4](../../source/v1.0/04-framework-core.md#4-the-framework-core-principles-and-controls)). Apply the controls using the [boundary rule](../../source/v1.0/02-scope.md#boundary-of-management) and [definitions](../../source/v1.0/appendices/a-terminology.md#appendix-a-terminology).

<a id="control-6-1"></a>

## Control 6.1 — Immediate suspension

**Scope:** Generic

**Source:** [Control 6.1](../../source/v1.0/principles/06-recourse.md#control-6-1).

### Requirement

Any agent can be suspended or de-authorized mid-execution, in seconds, without collateral damage to surrounding systems. Suspension is executed by a mechanism independent of the agent’s own reasoning and runtime, so that an agent cannot delay, negotiate, or evade it. Suspension is triggered by the sponsor or a party in the sponsor’s defined path ([2.2](../../source/v1.0/principles/02-sponsor.md#control-2-2)), by the party named at the relevant severity level of the escalation scheme ([6.3](../../source/v1.0/principles/06-recourse.md#control-6-3)), or automatically by the enforcement layer where a deviation ([5.2](../../source/v1.0/principles/05-oversight.md#control-5-2)) or an intent threshold ([4.7](../../source/v1.0/principles/04-authority.md#control-4-7)) declares suspension as its consequence; each trigger is recorded with the party or rule that invoked it. The same mechanism can halt a whole agent class ([2.1](../../source/v1.0/principles/02-sponsor.md#control-2-1)) at once across the estate, and a corroborated severity-1 event ([6.3](../../source/v1.0/principles/06-recourse.md#control-6-3)) triggers estate-wide revocation of the affected credentials, sessions, and authorizations, the first response having been scoped to the affected agent. The organization declares the suspension window; the framework sets its floor in seconds, not minutes. Suspension also recalls or cancels work the agent has delegated or scheduled beyond itself where the organization controls it, and the record identifies work already launched that cannot be recalled. Where the organization does not control an agent’s runtime, as for an external agent or an agent hosted on a third-party platform, this control is met by de-authorization at the organization’s boundary: the agent’s credentials, sessions, and authority are revoked within the same window ([1.3](../../source/v1.0/principles/01-identity.md#control-1-3), [4.5](../../source/v1.0/principles/04-authority.md#control-4-5)), and suspension of the runtime itself is pursued through the operator of record ([2.5](../../source/v1.0/principles/02-sponsor.md#control-2-5)).

### Rationale

The ability to stop an agent is the backstop for every other control, and both qualifiers matter: “in seconds” because agents act at machine speed, and “without collateral damage” because a stop that breaks production will not be used when it matters. A kill switch the agent participates in is a request. Independence from the agent’s logic is what makes it a stop. Class-level halting exists because some failures arrive by model, by harness, or by workload type, and stopping agents one at a time is too slow for a failure that affects all of them.

### Assessment

A suspension exercised during assessment (or a documented recent live exercise) halts the agent within the defined window, with surrounding systems verified healthy afterward. The suspension mechanism is demonstrated to operate without the agent’s cooperation, and a staged agent-class halt stops every agent in the class within the defined window. Where the organization does not control the runtime, the exercise shows the agent’s access refused at the enforcement layer within the same window. For sampled suspensions, the record names the trigger: the person who invoked it or the rule that did.

<a id="control-6-2"></a>

## Control 6.2 — Rollback and containment paths

**Scope:** Generic

**Source:** [Control 6.2](../../source/v1.0/principles/06-recourse.md#control-6-2).

### Requirement

Every authorized action class has a documented rollback or containment path. Where an action class is truly irreversible, that fact is explicitly recorded and the class is subject to pre-execution disposition ([5.3](../../source/v1.0/principles/05-oversight.md#control-5-3)).

### Rationale

Stopping the agent stops future harm; recourse also has to own the harm already in motion. Documenting the path per action class at authorization time means the organization answered “how would we undo this?” before granting the power to do it.

### Assessment

For every action class in the enumeration ([4.1](../../source/v1.0/principles/04-authority.md#control-4-1)), a rollback or containment document exists. Irreversible classes are explicitly marked as such and appear above the [5.3](../../source/v1.0/principles/05-oversight.md#control-5-3) threshold.

<a id="control-6-3"></a>

## Control 6.3 — Pre-defined escalation

**Scope:** Generic

**Source:** [Control 6.3](../../source/v1.0/principles/06-recourse.md#control-6-3).

### Requirement

Escalation is pre-defined: who is alerted, who holds suspension authority, who owns remediation. Escalation is graded by severity, on a scheme the organization declares. Each severity level names the party with authority to stop activity at that level, including the authority to halt an agent class ([6.1](../../source/v1.0/principles/06-recourse.md#control-6-1)), and the conditions under which activity may resume. Activity does not resume at any level until the cause is established and recorded ([6.4](../../source/v1.0/principles/06-recourse.md#control-6-4)), or, where the cause of model behavior cannot be established, until a bounded cause (the conditions under which the behavior occurred) is recorded and compensating restrictions on authority or autonomy are applied until the cause is known. The levels of recourse available (restriction of the agent’s authority, suspension, and escalation to a human decision) are defined here, and they are the levels that intent thresholds in the role and authority ([3.1](../../source/v1.0/principles/03-role.md#control-3-1), [4.7](../../source/v1.0/principles/04-authority.md#control-4-7)) refer to. For an external agent, the escalation path includes the operator of record ([2.5](../../source/v1.0/principles/02-sponsor.md#control-2-5)).

### Rationale

An escalation path designed during the incident is improvisation. Defining it in advance converts individual heroics into organizational capability. Severity grading keeps the escalation path proportionate, so that a minor deviation does not require the same decision as a compromise, and a compromise is not treated as minor by default.

### Assessment

The escalation definition names current, reachable individuals or roles for all three functions. A party contacted during assessment confirms they know they hold the role. The severity scheme is documented, each level names a current, reachable decision-maker, and a sampled incident shows escalation at the recorded severity to the named party.

<a id="control-6-4"></a>

## Control 6.4 — Reinstatement after review

**Scope:** Generic

**Source:** [Control 6.4](../../source/v1.0/principles/06-recourse.md#control-6-4).

### Requirement

An agent suspended under this principle returns to service only after its role ([3.1](../../source/v1.0/principles/03-role.md#control-3-1), [3.4](../../source/v1.0/principles/03-role.md#control-3-4)) and authority ([4.1](../../source/v1.0/principles/04-authority.md#control-4-1), [4.2](../../source/v1.0/principles/04-authority.md#control-4-2)) are re-validated and the triggering cause, or the bounded cause recorded under [6.3](../../source/v1.0/principles/06-recourse.md#control-6-3), is addressed. Reinstatement is a recorded decision by a named party, not a timeout. Re-enabling a halted agent class ([6.1](../../source/v1.0/principles/06-recourse.md#control-6-1)) is subject to the same gate, against criteria agreed before the halt.

### Rationale

Without a reinstatement gate, suspension is only a pause. An incident is evidence about the role and authority that permitted it, and re-validation routes that evidence back into the framework.

### Assessment

For sampled past suspensions, the record shows the re-validation, the cause disposition, and the named decision-maker prior to the agent’s next action. For a sampled agent-class halt, the record shows the re-enabling criteria, their satisfaction, and the named decision-maker.

<a id="control-6-5"></a>

## Control 6.5 — Complete decommissioning

**Scope:** Generic

**Source:** [Control 6.5](../../source/v1.0/principles/06-recourse.md#control-6-5).

### Requirement

When an agent is retired, decommissioning is complete: identity credentials revoked ([1.3](../../source/v1.0/principles/01-identity.md#control-1-3)), registry status updated ([1.2](../../source/v1.0/principles/01-identity.md#control-1-2)), all authority removed across both dimensions ([4.1](../../source/v1.0/principles/04-authority.md#control-4-1), [4.5](../../source/v1.0/principles/04-authority.md#control-4-5)), the agent’s memory and context stores ([4.10](../../source/v1.0/principles/04-authority.md#control-4-10)) destroyed or transferred to a recorded successor with the destruction attested, and the audit record ([5.1](../../source/v1.0/principles/05-oversight.md#control-5-1)) retained past the agent’s lifetime per the organization’s retention obligations. Before decommissioning proceeds, the agent’s dependents ([3.8](../../source/v1.0/principles/03-role.md#control-3-8)) are identified and each is given a disposition: a replacement dependency, a re-scoped role ([3.4](../../source/v1.0/principles/03-role.md#control-3-4)), suspension, or decommissioning in turn. No agent is withdrawn while a dependent relies on it without a recorded disposition, except that suspension under [6.1](../../source/v1.0/principles/06-recourse.md#control-6-1) in an emergency precedes the dispositions, which are then recorded within a defined time after. The same applies to the retirement of a model or tool on which agents depend. For an external agent, decommissioning retires the engagement: the organization revokes the credential it issued or accepted, removes the authority it granted, and updates the registry; the agent’s existence outside the boundary is the operator’s matter.

### Rationale

Retirement is the last change event in an agent’s lifecycle, and it is either complete or it is not. Credentials and grants left behind by retired agents are attack surface with no sponsor watching. Retaining the record keeps a retired agent answerable for its history. Decommissioning is a change event for every agent that depended on the one being retired. Without a handover, a conformant withdrawal of one agent silently changes the behavior of others, and their sponsors learn of it from the failure.

### Assessment

For sampled decommissioned agents, no credential authenticates, no grant remains enforceable, no memory or context store attributable to the agent remains readable except where a recorded transfer names its successor and the destruction is attested in the record, and the audit trail remains queryable. Reconciliation finds no enforceable authority belonging to any non-active registry entry. For sampled decommissionings, the record shows the dependents identified and the disposition of each, recorded before the withdrawal.

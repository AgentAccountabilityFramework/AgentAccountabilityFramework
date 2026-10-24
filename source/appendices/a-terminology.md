[Source index](../README.md) · [Previous](../08-framework-governance.md) · [Next](b-acknowledgments.md)

Source: [AAF.pdf, pages 36–42](../../AAF.pdf#page=36), version 0.9.4 — Working Draft.

<!-- Source transcription begins. -->

# Appendix A. Terminology

Definitions of terms as used normatively in this document, in alphabetical order. These are the framework’s own definitions, not citations of an external glossary: where a term is also in common use, the definition states the sense the controls rely on, and where that sense departs from common usage the definition says so (see Role and Recourse). These definitions have normative effect: where a control uses a defined term, the term carries the meaning given here.

## Action class

A category of agent actions sharing a consequence profile and a common authorization and recourse treatment.

## Admitting authority

The party holding defined authority to admit an agent to the registry and, separately, to production (control [1.2](../principles/01-identity.md#control-1-2)). Distinct from the sponsor; admission is a decision the sponsor does not make for their own agent.

## Agent

A software actor powered wholly or partly by AI that holds delegated authority to access information or take actions on behalf of an organization. The unit of identity is one identity bound to a versioned configuration: the model, the harness, the instructions (system prompt, skills, rules, and seeded memory), and the tools and data sources the agent is given. A change to any element of the configuration is a change event ([3.4](../principles/03-role.md#control-3-4), [3.7](../principles/03-role.md#control-3-7)); a session or an instance of an agent is not a separate agent, and a different configuration under the same name is a different version of the agent.

## Agent identity

The unique, durable identifier of an agent in the registry, distinct from every human user and every other agent ([1.1](../principles/01-identity.md#control-1-1)). One identity may be evidenced by several credentials over time and at once, and every credential resolves to exactly one identity. The identity, bound to a versioned configuration, is the unit to which every control attaches.

## Autonomy level

The degree to which an agent may act without a human disposition, declared in its role and expressed as the consequence threshold applied under control [5.3](../principles/05-oversight.md#control-5-3) (control [3.6](../principles/03-role.md#control-3-6)). Autonomy is granted on measured reliability and reduced when reliability is not sustained.

## Budget

The bound on the resources an agent may consume in its role, expressed in tokens, spend, or other resource units over a defined period (control [3.5](../principles/03-role.md#control-3-5)). A budget is declared in the role and enforced at the enforcement layer.

## Change event

A change to anything an agent’s accountability depends on: its role, its authority, its model, its harness, its dependencies, or its sponsor. A change event triggers re-validation under the relevant controls ([2.3](../principles/02-sponsor.md#control-2-3), [3.4](../principles/03-role.md#control-3-4), [3.7](../principles/03-role.md#control-3-7), [5.6](../principles/05-oversight.md#control-5-6)) before or with the change.

## Class

A grouping of agents that share a model, an agent type, a harness, or a workload label, drawn from a taxonomy the organization maintains with a named owner. Distinct from an action class. Ownership is recorded per class ([2.1](../principles/02-sponsor.md#control-2-1)) and a class can be halted as a unit ([6.1](../principles/06-recourse.md#control-6-1)).

## Configuration

The versioned set of elements that, with its identity, constitutes an agent: its model, harness, instructions (system prompt, skills, rules, and seeded memory), and the tools and data sources it is given. The unit of identity (see Agent); any change to it is a change event.

## Containment boundary

The isolated execution environment within which an agent, and any code it generates or runs, operates (control [4.9](../principles/04-authority.md#control-4-9)). The framework requires the boundary and its properties; it does not prescribe the technology that provides it.

## Control

A testable criterion under a principle, specified as a Requirement, a Rationale, and Assessment criteria. An assessor can answer each control yes or no; where a Requirement holds several obligations, the control is met only when all are met.

## Credential

Evidence an agent presents to authenticate as its identity: issued, rotated, and revoked under control [1.3](../principles/01-identity.md#control-1-3), bound to the identity and to the resource it was issued for, and held or mediated under control [1.4](../principles/01-identity.md#control-1-4). An agent may hold several credentials; a credential is distinct from the identity it evidences.

## Decommissioning

The complete retirement of an agent: credential revocation, removal of all authority, registry status change, and retention of the audit record. Decommissioning is carried out with regard to the agent’s dependents ([6.5](../principles/06-recourse.md#control-6-5)).

## Delegation

The explicit conferral of bounded authority from a principal (human or agent) to an agent. A delegation chain is the sequence of such conferrals linking an action back to a human principal.

## Dependency

An agent, tool, model, or data source that an agent relies on to perform its role. A dependent is any agent that relies on this one. Both are declared or derived under control [3.8](../principles/03-role.md#control-3-8) and consulted before change or decommissioning ([3.4](../principles/03-role.md#control-3-4), [6.5](../principles/06-recourse.md#control-6-5)).

## Disposition

The pre-execution determination of how a proposed action is handled: proceed, proceed with flag, hold for human decision, or deny.

## Domain

One of three groupings of the principles, each named for what the organization does with the agent and each answering a question the organization must be able to answer for any agent holding delegated authority: Assign (Identity, Sponsor), Align (Role, Authority), and Account (Oversight, Recourse). Domains organize the principles; conformance is evaluated against controls.

## Enforcement layer

The point at which the organization applies policy to an agent’s requests and actions in real time: issuing and checking credentials, evaluating authority and intent, masking data, bounding egress, metering budget, recording actions, and executing suspension. The framework requires that such a point exist and that every path to a governed resource pass through it ([4.4](../principles/04-authority.md#control-4-4)); it does not prescribe what provides it ([Section 6](../06-implementation-neutrality.md)).

## Estate

The complete population of agents operating in or on behalf of an organization. Conformance is stated for the estate and evidenced agent by agent: a finding against any agent is a finding against the estate ([Section 5](../05-conformance-and-assessment.md)).

## External agent

An agent operated by a third party that acts on, interacts with, or is relied upon by the organization. An external agent admitted to act in the organization has an internal sponsor ([2.1](../principles/02-sponsor.md#control-2-1)) and an operator of record ([2.5](../principles/02-sponsor.md#control-2-5)), and is subject to the controls tagged Generic and External.

## Framework Core

The normative body of the framework: the six principles and their controls ([Section 4](../04-framework-core.md)).

## Harness

The software environment that runs an agent: the loop that invokes the model, the tools made available to it, its memory, and settings such as iteration limits and whether it may create spawned agents. The harness in use is recorded in the registry ([1.2](../principles/01-identity.md#control-1-2)) and bound to the role ([3.7](../principles/03-role.md#control-3-7)); the tools it makes available are registered under control [4.13](../principles/04-authority.md#control-4-13).

## Intent

A role or authority definition that is not deterministic by nature: an expected purpose, outcome, or behavior that cannot be checked as a pass or fail. Every intent is declared with the measure by which it is evaluated under Oversight, a confidence score ([5.6](../principles/05-oversight.md#control-5-6)), and with the confidence thresholds at which defined levels of recourse apply ([6.3](../principles/06-recourse.md#control-6-3)). Contrast with a rule. The role ([3.1](../principles/03-role.md#control-3-1)) and the authority ([4.7](../principles/04-authority.md#control-4-7)) are each expressed as a combination of rules and intents.

## Internal agent

An agent the organization builds or operates itself, under its own sponsor and in its own registry.

## Operator of record

The organization that runs an external agent, tool, or model, bound by an agreement to accountability for its conduct and for the controls the deploying organization cannot apply from within its own boundary, with a named accountable contact (control [2.5](../principles/02-sponsor.md#control-2-5)). The second line of accountability behind the internal sponsor.

## Principle

One of the six top-level requirements of the framework.

## Provenance

Verifiable evidence of an action’s origin and integrity: which agent produced it, under which delegation, and that it was not altered in transit (control [1.5](../principles/01-identity.md#control-1-5)). The framework requires the property, not a particular signing or attestation mechanism.

## Reach

The set of systems, data domains, and external parties an agent can affect through its authority, declared in its role ([3.1](../principles/03-role.md#control-3-1)). Reach, together with the consequence of action classes ([5.3](../principles/05-oversight.md#control-5-3)), is how the framework scales oversight; the framework does not assign risk tiers to agents.

## Recourse

Organizational recourse: the deploying organization’s capability to suspend, contain, reverse, and retire its own agents ([Principle 6](../principles/06-recourse.md)). Distinct from algorithmic recourse, an affected individual’s ability to contest an automated decision, which is out of scope ([Section 2](../02-scope.md)).

## Registry

The authoritative record of all agent identities in the estate, including each agent’s sponsor, owning team, and lifecycle status, and of the tools and models agents are authorized to invoke, including the authorized definition of each ([4.13](../principles/04-authority.md#control-4-13)). The registry also records, for each agent, the harness that runs it and its relevant settings, the runtime locations in which it may execute, its agent class attributes, and its declared dependencies.

## Role

The documented purpose, scope, success criteria, budget, and autonomy level of an agent: its position and its duties. Used throughout this framework in that sense, not in the access-control sense of role-based access control. A set of permissions is part of an agent’s Authority ([Principle 4](../principles/04-authority.md)), never its role. The role is expressed as rules and intents, and also declares its reach, its dependencies, and the model and harness it is bound to.

## Rule

A role or authority definition that is deterministic: an action either satisfies it or does not, and the result is a pass or a fail that can be enforced directly as policy. Contrast with an intent.

## Scope tag

A tag carried by every control, stating which agents it applies to: Generic (every agent in the estate, internal or external, satisfied by the organization from within its own boundary), Internal (agents the organization operates, because the control requires access to the agent’s internals), or External (external agents only). No control requires authority beyond the organization’s boundary ([Section 2](../02-scope.md), Boundary of management). Where a clause of a Generic control applies only to agents the organization operates, the clause says so, and the clause is assessed only for those agents.

## Severity-1 event

The highest grade in the organization’s escalation scheme (control [6.3](../principles/06-recourse.md#control-6-3)): an event that, once corroborated, warrants estate-wide revocation under control [6.1](../principles/06-recourse.md#control-6-1). The scheme and its grades are declared by the organization.

## Spawned agent

An agent created by another agent in the course of its work. A spawned agent is an agent under every principle: it is identified, sponsored through its parent’s sponsor ([2.4](../principles/02-sponsor.md#control-2-4)), and holds at most a subset of its parent’s authority ([4.14](../principles/04-authority.md#control-4-14)).

## Sponsor

The accountable human who answers for an agent's existence, role, authority, and conduct ([Principle 2](../principles/02-sponsor.md)). Sponsorship is held by a named person, never by a team, a role title, or a system. The sponsor answers for the agent; a principal who delegates authority to the agent ([4.3](../principles/04-authority.md#control-4-3)) answers for that delegation and is recorded as such ([5.1](../principles/05-oversight.md#control-5-1)), and is not thereby the sponsor.

## Untrusted content

Content whose author the organization cannot authenticate or whose integrity it does not control: external web content, inbound messages and documents, outputs of models and agents it does not operate, and any content a party outside the owning team can edit. The organization declares which internal sources count as controlled. Untrusted content confers no authority ([4.6](../principles/04-authority.md#control-4-6)).

<!-- Source transcription ends. -->

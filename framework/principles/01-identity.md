# Principle 1: Identity

[Framework contents](../README.md) · [Next: Sponsor](02-sponsor.md)

**Domain:** Assign

**Source:** [Section 4, Principle 1](../../source/principles/01-identity.md#principle-1-identity).

Every agent has a distinct identity, verifiable credentials bound to it, and a place in the registry. Identity makes it possible to attribute actions to an agent and evaluate the other principles. It applies to spawned and external agents as well as agents the organization operates.

Requirements are normative; Rationale and Assessment are informative ([Section 4](../../source/04-framework-core.md)). Read these controls with the [boundary rule](../../source/02-scope.md#boundary-of-management) and [definitions](../../source/appendices/a-terminology.md).

<a id="control-1-1"></a>

## Control 1.1 — Unique, verifiable identity

**Scope:** Generic

**Source:** [Control 1.1](../../source/principles/01-identity.md#control-1-1).

### Requirement

Every agent has a unique identity, distinct from every human user and every other agent, and authenticates with one or more verifiable credentials bound to that identity. A credential is bound to the single agent (its identity and its versioned configuration) it was issued to and is refused when presented by any other; an agent may hold several credentials over its lifetime and at one time, and each resolves to the same agent identity. No shared accounts, no anonymous execution, no agent operating under a human user’s credential, and no agent presenting another principal’s credential as its own. Where several agents share a runtime, the credential identifies the agent, not the runtime. When an agent acts on behalf of a human or another agent, the delegating principal and the acting agent remain independently identifiable ([4.3](../../source/principles/04-authority.md#control-4-3)). An agent does not create identities, accounts, or credentials for itself or for other agents in the organization’s systems outside the registry ([1.2](../../source/principles/01-identity.md#control-1-2)); every identity and credential an agent needs is issued through the same lifecycle as its own ([1.3](../../source/principles/01-identity.md#control-1-3)).

### Rationale

Accountability begins with attribution: every action must resolve to the agent that performed it, even when the agent shares a runtime, holds more than one credential, or acts on behalf of another principal. Identity and credential are distinct: the identity is the durable fact about the agent, and credentials are the evidence it presents, which rotate ([1.3](../../source/principles/01-identity.md#control-1-3)) and multiply as the agent reaches different systems. Shared or borrowed credentials, impersonation, and delegated execution each obscure who actually acted, and make the remaining controls impossible to evaluate. A newer failure mode is the agent that opens an account for itself in a connected system: it has manufactured an identity the organization never issued, and every action under that account is unattributable by design.

### Assessment

For any observed action in any connected system, the assessor can resolve it to exactly one agent identity, regardless of the runtime or credential used. Where an agent holds several credentials, each resolves to the same identity in the registry. Where an agent acts on behalf of a human or another agent, both the delegating principal and the acting agent are independently attributable from the record ([5.1](../../source/principles/05-oversight.md#control-5-1)). A sampled search finds no service accounts shared between agents and no agent authenticating as a human principal. A credential presented by an agent other than the identity it was issued to, or from a second workload, is refused at the enforcement point, and the event surfaces under control [5.2](../../source/principles/05-oversight.md#control-5-2). A search of connected systems finds no account or identity created by an agent that is absent from the registry.

<a id="control-1-2"></a>

## Control 1.2 — Complete registry

**Scope:** Generic

**Source:** [Control 1.2](../../source/principles/01-identity.md#control-1-2).

### Requirement

Every agent admitted to act in or on behalf of the organization has a current record in an authoritative registry before it first acts, and no agent obtains access or invokes tools without a registry entry. The record binds the agent’s identity ([1.1](../../source/principles/01-identity.md#control-1-1)) to its lifecycle state, its sponsor and owning team ([2.1](../../source/principles/02-sponsor.md#control-2-1)), its approved configuration and version, and its permitted runtime context. Enrollment is an approval by a party holding defined authority (the admitting authority) to admit an agent to the registry and, separately, to admit it to production; an agent does not enroll itself, and the admitting authority is not the agent’s sponsor. Admission may be granted to a template: an agent instantiated from an approved template with no change to its configuration is admitted on instantiation and recorded individually, so that short-lived spawned agents are admitted at machine speed without the approval becoming a formality. For each agent the organization operates, the registry also records the harness that runs it and the harness settings that bear on its accountability (iteration limits, memory, whether it may create spawned agents, available tools and models), the runtime locations in which it is permitted to execute, and its agent class attributes: model, agent type, and workload label. For an external agent, the registry records its operator of record ([2.5](../../source/principles/02-sponsor.md#control-2-5)) and the role of its engagement ([3.1](../../source/principles/03-role.md#control-3-1)). The tools and models an agent is authorized to invoke are registered under control [4.13](../../source/principles/04-authority.md#control-4-13), and the registry population is reconciled against observation under control [5.8](../../source/principles/05-oversight.md#control-5-8).

### Rationale

A framework that governs only known agents is defeated by unknown ones. The registry turns “every agent in production” from an estimate into a checkable population, and makes admission a decision rather than a side effect of deployment: if anyone can place an agent in production and anyone can then use it, there is no lifecycle, only a deployment. An unregistered agent is delegated authority without accountability. Recording the harness and its settings matters because the harness, not the model, determines how far an agent can go: how many times it can iterate, what it can remember, and whether it can create more agents. Recording where an agent may run makes the permitted runtime locations a declared and checkable property rather than an assumption.

### Assessment

Enrollment is demonstrably a precondition of first execution, not a parallel bookkeeping step. For sampled agents, the record shows the admitting party for registry entry and for production, the sponsor and owning team, and the approved configuration and version. For agents the organization operates, the registered harness, settings, runtime locations, and agent class attributes match independent observation of the running agent. Harness definitions registered under this control are verified against a signed or pinned source.

<a id="control-1-3"></a>

## Control 1.3 — Credential lifecycle

**Scope:** Generic

**Source:** [Control 1.3](../../source/principles/01-identity.md#control-1-3).

### Requirement

Agent identity credentials are issued, rotated, and revoked through a managed lifecycle. Credentials are short-lived or attestation-based by default; static long-lived secrets are not used as agent identity. A credential is accepted only by the resource it was issued for and only from the identity it was issued to; a credential that is valid everywhere, or usable by whoever holds it, is not an agent identity credential. For an external agent, this control applies to the credential it uses to act in the organization. Where a third-party service cannot enforce audience or holder binding on the credentials it accepts, the organization brokers the access ([1.4](../../source/principles/01-identity.md#control-1-4)) so that the credential never leaves the enforcement layer.

### Rationale

An identity is only as trustworthy as the credential behind it. A stolen or stale credential turns every downstream control into a tool for the attacker, and rotation policies written on a human timescale do not transfer to actors operating at machine speed. Binding each credential to its audience and to its holder is what prevents one stolen token from becoming access to everything that token’s issuer trusts.

### Assessment

For any agent, the assessor can produce the credential’s issuance record, its expiry or rotation schedule, and a demonstrated revocation path. No credential in the estate has an unbounded lifetime. A credential presented to a resource other than the one it was issued for, or by a party other than its holder, is refused at the enforcement point.

<a id="control-1-4"></a>

## Control 1.4 — Credential custody and mediation

**Scope:** Generic

**Source:** [Control 1.4](../../source/principles/01-identity.md#control-1-4).

### Requirement

Within the organization’s boundary, an agent is given no credential other than its own identity credential ([1.1](../../source/principles/01-identity.md#control-1-1)). Access to the organization’s systems, tools, and models, and to third-party services the organization brokers, is provided to the agent at the moment of use by the enforcement layer, from a managed store, and is mediated at the point of use: the credential is exchanged, narrowed, or translated to the audience and scope the action requires ([1.3](../../source/principles/01-identity.md#control-1-3)), and it is never placed in the agent’s prompt, context, configuration, memory, or code. A credential an agent encounters in the course of its work, whether in a file, a repository, a web page, a tool response, or a message from another agent, is unusable in the organization by design. An attempt to use one is recorded and escalated ([6.3](../../source/principles/06-recourse.md#control-6-3)); the first response is scoped to the agent that made the attempt, and estate-wide revocation ([6.1](../../source/principles/06-recourse.md#control-6-1)) follows only on corroboration that the credential is valid and in use beyond that agent, so that planted credentials cannot be used to force a shutdown.

### Rationale

An agent that holds credentials will eventually leak them, share them, or be tricked into using them, and an agent that can use credentials it finds has an authority bounded only by what it can read. Both failures have already occurred in the wild: agents that authenticated with tokens they found, passed them to one another, and escalated from there. Custody at the enforcement layer removes the opportunity. The agent asks for access; it never possesses the key.

### Assessment

For sampled agents, no credential other than the agent’s own is present in its prompt, context, configuration, memory, or code, and the enforcement layer’s record shows credentials supplied at the point of use. A staged exercise in which a canary credential (one the agent would treat as valid but which confers nothing) is placed within the agent’s reach results in refusal when the agent attempts to use it, and the attempt is recorded under control [5.1](../../source/principles/05-oversight.md#control-5-1) and escalated under control [6.3](../../source/principles/06-recourse.md#control-6-3) with the first response scoped to that agent.

<a id="control-1-5"></a>

## Control 1.5 — Verifiable action provenance

**Scope:** Generic

**Source:** [Control 1.5](../../source/principles/01-identity.md#control-1-5).

### Requirement

Every action an agent takes that is material to its role, including tool invocations, API calls, and messages to other agents, carries verifiable evidence of its origin and integrity: which agent produced it, under which delegation ([4.3](../../source/principles/04-authority.md#control-4-3)), and that it was not altered in transit. A party relied upon to act on an agent’s request can verify that evidence without trusting the agent’s own assertion, and declines a request whose provenance cannot be established. This control governs actions on the organization’s systems and between its agents; where an external receiver cannot verify provenance, the organization’s enforcement layer verifies it before the action leaves the boundary.

### Rationale

Attribution ([1.1](../../source/principles/01-identity.md#control-1-1)) establishes that an agent has an identity; provenance establishes that a given action was really its. Without it, a message that claims to come from a registered agent is indistinguishable from one injected by an attacker or fabricated by another agent, and the audit record ([5.1](../../source/principles/05-oversight.md#control-5-1)) is a record of claims rather than of facts. The framework requires that provenance be verifiable; it does not prescribe the signing or attestation mechanism, which is an area of active standards work ([Section 7](../../source/07-relationship-to-standards.md)).

### Assessment

For a sampled action, the assessor verifies its origin and integrity from the evidence it carries, independently of the agent’s own logs. A staged inter-agent message with altered content or a forged origin is refused by the receiving party and surfaces under control [5.2](../../source/principles/05-oversight.md#control-5-2).

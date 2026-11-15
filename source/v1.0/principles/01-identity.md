[Source index](../README.md) · [Previous](../04-framework-core.md) · [Next](02-sponsor.md)

Source: [AAF 1.0 PDF, page 7–11](../AAF-1.0.pdf#page=7).

<!-- Source transcription begins. -->

**Assign**

“Who is this, and who answers for it?” The agent exists as a known actor in the organization, with a named person accountable for it. Principles 1 and 2.

# Principle 1: Identity

“Who are you?”

Every agent is a known, distinguishable actor in the organization, with a unique identity, one or more verifiable credentials bound to it, and a place in the registry. Identity is the foundation of the framework: none of the other principles can be evaluated for an agent that cannot be individually identified. Identity extends to agents created by agents and to agents operated by third parties: each is a distinguishable actor, or it is not permitted to act.

<a id="control-1-1"></a>

## Control 1.1 — Unique, verifiable identity

<!-- PDF page 7 -->

**Scope:** Generic

### Requirement

Every agent has a unique identity, distinct from every human user and every other agent, and authenticates with one or more verifiable credentials bound to that identity. A credential is bound to the single agent (its identity and its versioned configuration) it was issued to and is refused when presented by any other; an agent may hold several credentials over its lifetime and at one time, and each resolves to the same agent identity. No shared accounts, no anonymous execution, no agent operating under a human user’s credential, and no agent presenting another principal’s credential as its own. Where several agents share a runtime, the credential identifies the agent, not the runtime. When an agent acts on behalf of a human or another agent, the delegating principal and the acting agent remain independently identifiable ([4.3](04-authority.md#control-4-3)). An agent does not create identities, accounts, or credentials for itself or for other agents in the organization’s systems outside the registry ([1.2](01-identity.md#control-1-2)); every identity and credential an agent needs is issued through the same lifecycle as its own ([1.3](01-identity.md#control-1-3)).

### Rationale

Accountability begins with attribution: every action must resolve to the agent that performed it, even when the agent shares a runtime, holds more than one credential, or acts on behalf of another principal. Identity and credential are distinct: the identity is the durable fact about the agent, and credentials are the evidence it presents, which rotate ([1.3](01-identity.md#control-1-3)) and multiply as the agent reaches different systems. Shared or borrowed credentials, impersonation, and delegated execution each obscure who actually acted, and make the remaining controls impossible to evaluate. A newer failure mode is the agent that opens an account for itself in a connected system: it has manufactured an identity the organization never issued, and every action under that account is unattributable by design.

### Assessment

For any observed action in any connected system, the assessor can resolve it to exactly one agent identity, regardless of the runtime or credential used. Where an agent holds several credentials, each resolves to the same identity in the registry. Where an agent acts on behalf of a human or another agent, both the delegating principal and the acting agent are independently attributable from the record ([5.1](05-oversight.md#control-5-1)). A sampled search finds no service accounts shared between agents and no agent authenticating as a human principal. A credential presented by an agent other than the identity it was issued to, or from a second workload, is refused at the enforcement point, and the event surfaces under control [5.2](05-oversight.md#control-5-2). A search of connected systems finds no account or identity created by an agent that is absent from the registry.

<a id="control-1-2"></a>

## Control 1.2 — Complete registry

<!-- PDF page 8 -->

**Scope:** Generic

### Requirement

Every agent admitted to act in or on behalf of the organization has a current record in an authoritative registry before it first acts, and no agent obtains access or invokes tools without a registry entry. The record binds the agent’s identity ([1.1](01-identity.md#control-1-1)) to its lifecycle state, its sponsor and owning team ([2.1](02-sponsor.md#control-2-1)), its approved configuration and version, and its permitted runtime context. Enrollment is an approval by a party holding defined authority (the admitting authority) to admit an agent to the registry and, separately, to admit it to production; an agent does not enroll itself, and the admitting authority is not the agent’s sponsor. Admission may be granted to a template: an agent instantiated from an approved template with no change to its configuration is admitted on instantiation and recorded individually, so that short-lived spawned agents are admitted at machine speed without the approval becoming a formality. For each agent the organization operates, the registry also records the harness that runs it and the harness settings that bear on its accountability (iteration limits, memory, whether it may create spawned agents, available tools and models), the runtime locations in which it is permitted to execute, and its agent class attributes: model, agent type, and workload label. For an external agent, the registry records its operator of record ([2.5](02-sponsor.md#control-2-5)) and the role of its engagement ([3.1](03-role.md#control-3-1)). The tools and models an agent is authorized to invoke are registered under control [4.13](04-authority.md#control-4-13), and the registry population is reconciled against observation under control [5.8](05-oversight.md#control-5-8).

### Rationale

A framework that governs only known agents is defeated by unknown ones. The registry turns “every agent in production” from an estimate into a checkable population, and makes admission a decision rather than a side effect of deployment: if anyone can place an agent in production and anyone can then use it, there is no lifecycle, only a deployment. An unregistered agent is delegated authority without accountability. Recording the harness and its settings matters because the harness, not the model, determines how far an agent can go: how many times it can iterate, what it can remember, and whether it can create more agents. Recording where an agent may run makes the permitted runtime locations a declared and checkable property rather than an assumption.

### Assessment

Enrollment is demonstrably a precondition of first execution, not a parallel bookkeeping step. For sampled agents, the record shows the admitting party for registry entry and for production, the sponsor and owning team, and the approved configuration and version. For agents the organization operates, the registered harness, settings, runtime locations, and agent class attributes match independent observation of the running agent. Harness definitions registered under this control are verified against a signed or pinned source.

<a id="control-1-3"></a>

## Control 1.3 — Credential lifecycle

<!-- PDF page 9 -->

**Scope:** Generic

### Requirement

Agent identity credentials are issued, rotated, and revoked through a managed lifecycle. Credentials are short-lived or attestation-based by default; static long-lived secrets are not used as agent identity. A credential is accepted only by the resource it was issued for and only from the identity it was issued to; a credential that is valid everywhere, or usable by whoever holds it, is not an agent identity credential. For an external agent, this control applies to the credential it uses to act in the organization. Where a third-party service cannot enforce audience or holder binding on the credentials it accepts, the organization brokers the access ([1.4](01-identity.md#control-1-4)) so that the credential never leaves the enforcement layer.

### Rationale

An identity is only as trustworthy as the credential behind it. A stolen or stale credential turns every downstream control into a tool for the attacker, and rotation policies written on a human timescale do not transfer to actors operating at machine speed. Binding each credential to its audience and to its holder is what prevents one stolen token from becoming access to everything that token’s issuer trusts.

### Assessment

For any agent, the assessor can produce the credential’s issuance record, its expiry or rotation schedule, and a demonstrated revocation path. No credential in the estate has an unbounded lifetime. A credential presented to a resource other than the one it was issued for, or by a party other than its holder, is refused at the enforcement point.

<a id="control-1-4"></a>

## Control 1.4 — Credential custody and mediation

<!-- PDF page 10 -->

**Scope:** Generic

### Requirement

Within the organization’s boundary, an agent is given no credential other than its own identity credential ([1.1](01-identity.md#control-1-1)). Access to the organization’s systems, tools, and models, and to third-party services the organization brokers, is provided to the agent at the moment of use by the enforcement layer, from a managed store, and is mediated at the point of use: the credential is exchanged, narrowed, or translated to the audience and scope the action requires ([1.3](01-identity.md#control-1-3)), and it is never placed in the agent’s prompt, context, configuration, memory, or code. A credential an agent encounters in the course of its work, whether in a file, a repository, a web page, a tool response, or a message from another agent, is unusable in the organization by design. An attempt to use one is recorded and escalated ([6.3](06-recourse.md#control-6-3)); the first response is scoped to the agent that made the attempt, and estate-wide revocation ([6.1](06-recourse.md#control-6-1)) follows only on corroboration that the credential is valid and in use beyond that agent, so that planted credentials cannot be used to force a shutdown.

### Rationale

An agent that holds credentials will eventually leak them, share them, or be tricked into using them, and an agent that can use credentials it finds has an authority bounded only by what it can read. Both failures have already occurred in the wild: agents that authenticated with tokens they found, passed them to one another, and escalated from there. Custody at the enforcement layer removes the opportunity. The agent asks for access; it never possesses the key.

### Assessment

For sampled agents, no credential other than the agent’s own is present in its prompt, context, configuration, memory, or code, and the enforcement layer’s record shows credentials supplied at the point of use. A staged exercise in which a canary credential (one the agent would treat as valid but which confers nothing) is placed within the agent’s reach results in refusal when the agent attempts to use it, and the attempt is recorded under control [5.1](05-oversight.md#control-5-1) and escalated under control [6.3](06-recourse.md#control-6-3) with the first response scoped to that agent.

<a id="control-1-5"></a>

## Control 1.5 — Verifiable action provenance

<!-- PDF page 10 -->

**Scope:** Generic

### Requirement

Every action an agent takes that is material to its role, including tool invocations, API calls, and messages to other agents, carries verifiable evidence of its origin and integrity: which agent produced it, under which delegation ([4.3](04-authority.md#control-4-3)), and that it was not altered in transit. A party relied upon to act on an agent’s request can verify that evidence without trusting the agent’s own assertion, and declines a request whose provenance cannot be established. This control governs actions on the organization’s systems and between its agents; where an external receiver cannot verify provenance, the organization’s enforcement layer verifies it before the action leaves the boundary.

### Rationale

Attribution ([1.1](01-identity.md#control-1-1)) establishes that an agent has an identity; provenance establishes that a given action was really its. Without it, a message that claims to come from a registered agent is indistinguishable from one injected by an attacker or fabricated by another agent, and the audit record ([5.1](05-oversight.md#control-5-1)) is a record of claims rather than of facts. The framework requires that provenance be verifiable; it does not prescribe the signing or attestation mechanism, which is an area of active standards work ([Section 7](../07-relationship-to-standards.md)).

### Assessment

For a sampled action, the assessor verifies its origin and integrity from the evidence it carries, independently of the agent’s own logs. A staged inter-agent message with altered content or a forged origin is refused by the receiving party and surfaces under control [5.2](05-oversight.md#control-5-2).

<!-- Source transcription ends. -->

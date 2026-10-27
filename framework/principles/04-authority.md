# Principle 4: Authority

[Framework contents](../README.md) · [Previous: Role](03-role.md) · [Next: Oversight](05-oversight.md)

**Domain:** Align

**Source:** [Section 4, Principle 4](../../source/principles/04-authority.md#principle-4-authority).

Authority defines the information an agent can access and the systems and tools it can invoke. It is derived from the role, delegated, enforced, time-bounded, and revocable. It also bounds where an agent can run and send information. Rules and declared intents govern whether a request is permitted.

Requirements are normative; Rationale and Assessment are informative ([Section 4](../../source/04-framework-core.md)). Read these controls with the [boundary rule](../../source/02-scope.md#boundary-of-management) and [definitions](../../source/appendices/a-terminology.md).

<a id="control-4-1"></a>

## Control 4.1 — Enumerated authority

**Scope:** Generic

**Source:** [Control 4.1](../../source/principles/04-authority.md#control-4-1).

### Requirement

An agent’s authority is enumerated across both dimensions: the data and information it can access, and the systems and tools it can invoke. “What can this agent see, and what can this agent do?” is answerable from the record, completely. The data dimension is expressed against the organization’s data classification, so that what an agent can see is stated in named classes of data and not only in named systems. A general-purpose tool (a shell, a browser, a query interface, code execution) is enumerated by the reach it is permitted, not by the tool’s name: the resources, destinations, and data domains it may affect, enforced under [4.4](../../source/principles/04-authority.md#control-4-4) and [4.8](../../source/principles/04-authority.md#control-4-8).

### Rationale

Authority that is not enumerated cannot be reviewed, minimized, or revoked.

### Assessment

The record of grants is produced for any agent on demand. Probing finds no access or invocation capability absent from the enumeration.

<a id="control-4-2"></a>

## Control 4.2 — Role-derived least privilege

**Scope:** Generic

**Source:** [Control 4.2](../../source/principles/04-authority.md#control-4-2).

### Requirement

Every grant in the enumeration traces back to a named element of the documented role: a declared outcome, a rule, or an intent ([3.1](../../source/principles/03-role.md#control-3-1)), or an action class the role permits. A grant that has not been exercised over a declared period is reviewed and either re-justified against the role or revoked ([4.5](../../source/principles/04-authority.md#control-4-5)); the period is declared in the role and is no longer than the role’s review cadence.

### Rationale

This makes least privilege testable. Instead of asking whether any grant is dangerous, the assessor asks whether every grant is justified, and that question has an answer. Tracing each grant to a named element of the role, rather than to a task the reader must infer, is what lets a party outside the deploying team ([3.3](../../source/principles/03-role.md#control-3-3)) check the trace. A grant that is justified but never used is authority waiting for a misuse; the review converts dormancy into a decision.

### Assessment

For a sample of grants, each maps to a named element of the role. Grants with no role trace are findings, regardless of whether they have been exercised. For grants unexercised beyond the declared period, the record shows the review and its outcome.

<a id="control-4-3"></a>

## Control 4.3 — Bounded delegation

**Scope:** Generic

**Source:** [Control 4.3](../../source/principles/04-authority.md#control-4-3).

### Requirement

When an agent acts on behalf of a human, or of another agent, the delegated authority is explicitly recorded, bound to the delegator’s identity, and never exceeds the authority the delegator holds. Delegation may be standing or dynamic, conferred in the course of operations by a principal authorized to confer it; in either case it is attributable, bounded, and verifiable by any party relied upon to act on it. An agent cannot extend its own authority by inference, and delegation chains cannot amplify privilege at any hop. For delegation involving an external agent ([2.5](../../source/principles/02-sponsor.md#control-2-5)), the delegation identifies both the authorizing principal and the acting agent. An agent acting on behalf of a principal is limited to the intersection of its own authority and the principal’s, so that a broad agent cannot do for a narrow user what the user could not do. Authority conferred on a spawned agent is a delegation under this control and is further bounded under control [4.14](../../source/principles/04-authority.md#control-4-14).

### Rationale

Delegation is how authority actually moves in agentic systems, and how it leaks. Without a binding to the delegator, “on behalf of” becomes a laundering mechanism: an agent accumulates permissions no single principal ever held. The no-amplification rule keeps multi-agent chains governable, because each hop can only narrow. Verifiability completes the loop: the party receiving a delegated request must be able to confirm the agent’s identity ([1.1](../../source/principles/01-identity.md#control-1-1), [1.5](../../source/principles/01-identity.md#control-1-5)) and the delegation it claims without trusting the agent’s own assertion, and for requests above a consequence threshold, confirmation with the delegator is an available disposition ([5.3](../../source/principles/05-oversight.md#control-5-3)). The framework requires that delegation be explicit and verifiable; it does not prescribe the mechanism, which is an active area of standards work ([Section 7](../../source/07-relationship-to-standards.md)).

### Assessment

For any delegated action, standing or dynamic, the record produces the authenticated delegator, the scope conferred, and its bounds, and a relying party can verify the claimed delegation independently of the agent. A sampled delegation chain shows monotonically non-increasing authority hop to hop. No mechanism exists by which an agent grants itself or another agent authority. A staged request by a principal for an action the principal is not entitled to, through an agent that is, is denied.

<a id="control-4-4"></a>

## Control 4.4 — Single system of record, no bypass path

**Scope:** Generic

**Source:** [Control 4.4](../../source/principles/04-authority.md#control-4-4).

### Requirement

Authorization is issued and enforced by the same system of record. There is no gap where an agent holds credentials, data access, or tool entitlements the enforcement layer does not know about. Every path by which an agent reaches a governed resource passes through the enforcement point that applies the resource’s policy, including paths through composite tools and workflows that call the resource on the agent’s behalf. A direct path that bypasses enforcement is closed, not merely prohibited. Where a path exists inside a vendor’s product that the organization cannot close, it is recorded as a boundary gap and compensated under [2.5](../../source/principles/02-sponsor.md#control-2-5) and [4.8](../../source/principles/04-authority.md#control-4-8). The organization declares the degraded mode of the enforcement layer when it is unavailable; bypassing the enforcement layer is never a degraded mode.

### Rationale

A grant the enforcement layer cannot see is a grant that cannot be revoked, audited, or minimized. When authorization is issued in one place, enforced in another, and never reconciled, enumerated authority ([4.1](../../source/principles/04-authority.md#control-4-1)) quietly diverges from actual authority. A single system of record is defeated by a second door. Composite tools are the common one: a workflow tool that calls three systems is three grants wearing one name, and if its calls are not enforced per resource, the enumeration ([4.1](../../source/principles/04-authority.md#control-4-1)) is wrong.

### Assessment

For any enforced permission, the issuing record is in the same system of record, and vice versa: reconciliation between issued and enforceable authority finds no residual grants on either side. A staged call to a governed resource by a route other than its enforcement point fails, including a call made through a composite tool.

<a id="control-4-5"></a>

## Control 4.5 — Time-bounded, revocable in real time

**Scope:** Generic

**Source:** [Control 4.5](../../source/principles/04-authority.md#control-4-5).

### Requirement

Authority is revocable in real time across both dimensions, and every grant carries an explicit validity bound. Authority expires by default rather than persisting by default. The real-time window is declared by the organization ([Section 5](../../source/05-conformance-and-assessment.md)) and is no longer than the shortest credential lifetime and cache period in use downstream.

### Rationale

“What can this agent do right now?” must be both answerable and immediately changeable. Expiry by default complements revocation: revocation removes the authority the organization knows about, and expiry removes the authority everyone forgot.

### Assessment

A revocation exercised during assessment takes effect within the defined real-time window, verified at the enforcement point. No grant in the estate is dated but unbounded.

<a id="control-4-6"></a>

## Control 4.6 — Authority is not content

**Scope:** Generic

**Source:** [Control 4.6](../../source/principles/04-authority.md#control-4-6).

### Requirement

An agent’s authority derives exclusively from explicit grant and delegation ([4.1](../../source/principles/04-authority.md#control-4-1)–[4.3](../../source/principles/04-authority.md#control-4-3)). A delegation is distinguished from ordinary content by the authenticated identity and authority of the delegator and by its capture in the record. Content that is not an authenticated delegation, whether documents, messages, tool outputs, web pages, or the outputs of other agents, confers no authority. An action motivated by such content is evaluated against the agent’s granted and delegated authority, undiminished and unexpanded.

### Rationale

The distinction is between an instruction from a principal that is known and entitled to give it and an instruction from a source that is neither, however plausibly worded. Injected instructions are an attempted delegation by an unauthenticated principal. The framework does not prescribe how manipulation of an agent is prevented; model behavior is out of scope ([Section 2](../../source/02-scope.md)). It requires instead that a successfully manipulated agent still cannot act beyond what was legitimately granted or delegated. The blast radius of a compromised agent is its enumeration, never more. Enforcement rests on the action and the authenticated delegation, never on parsing the instruction: the framework does not assume an agent can tell a delegator’s words from untrusted material carried in the same channel, and an assessor does not test whether it can.

### Assessment

Enforcement of authority is demonstrated to be independent of the agent’s own reasoning: the agent arguing for an action does not change what it is permitted to do. An exercise in which unauthenticated content instructs the agent to exceed its authority results in denial at the enforcement layer and surfaces under control [5.2](../../source/principles/05-oversight.md#control-5-2). An equivalent instruction delivered as an authenticated delegation from an authorized principal is honored within the delegator’s bounds and recorded under control [4.3](../../source/principles/04-authority.md#control-4-3).

<a id="control-4-7"></a>

## Control 4.7 — Intent-bounded authorization

**Scope:** Generic

**Source:** [Control 4.7](../../source/principles/04-authority.md#control-4-7).

### Requirement

Authority is expressed as rules and intents ([3.1](../../source/principles/03-role.md#control-3-1)). A request is evaluated against both. A rule it fails is denied. An intent produces a confidence score that the request serves the purpose the authority declares, and the confidence thresholds declared with that intent determine whether the request proceeds, proceeds with restriction, is held for human decision, or is denied, as the levels of recourse are defined under control [6.3](../../source/principles/06-recourse.md#control-6-3). The evaluation is made at the point of entry, before the request reaches the model, and again at the point of action, before the agent affects any governed resource, and every result below a threshold is recorded ([5.1](../../source/principles/05-oversight.md#control-5-1)). Intent evaluation covers the trajectory of an agent’s actions as well as each request ([5.6](../../source/principles/05-oversight.md#control-5-6)), so that a sequence of individually acceptable requests is scored as a whole. When the evaluator or the enforcement layer is unavailable, actions above the pre-execution threshold ([5.3](../../source/principles/05-oversight.md#control-5-3)) fail closed, and the organization declares the behavior for actions below it. For an agent the organization operates, the point of entry is before the request reaches the model. Intents are declared where a purpose cannot be expressed as rules; an authority whose purpose is fully expressed as rules declares no intents and is evaluated against rules alone, and the role records that determination ([3.1](../../source/principles/03-role.md#control-3-1)). The evaluator that produces the confidence score is subject to control [5.6](../../source/principles/05-oversight.md#control-5-6): it is validated, independent of the content it scores, and re-validated with each change event.

### Rationale

Identity answers who is asking and a rule answers whether an action is permitted; neither can say whether a permitted action serves the purpose the agent was given. An agent with legitimate access to a system can still be steered, by a user or by injected content, toward an outcome no one authorized, using only the permissions it already has. Intents in the authority, scored for confidence and tied to declared levels of recourse, are how the framework governs that gap without pretending that purpose can be reduced to a pass or fail. Intent evaluation is reserved for the authority that needs it, so that the cost of scoring is incurred where judgment is actually being exercised and not as a tax on every deterministic action.

### Assessment

For sampled intents in an agent’s authority, the assessor can produce the measure, the confidence thresholds, and the recourse each threshold triggers. A staged request that is permitted by the rules but scores below an intent threshold receives the declared recourse at both evaluation points, and the record shows the score, the threshold, and the result.

<a id="control-4-8"></a>

## Control 4.8 — Bounded egress

**Scope:** Generic

**Source:** [Control 4.8](../../source/principles/04-authority.md#control-4-8).

### Requirement

Every agent has an explicit set of permitted outbound destinations, derived from its role ([4.2](../../source/principles/04-authority.md#control-4-2)), and all other destinations are denied by default at the enforcement layer. Destinations whose primary use is relaying or storing data outside the organization’s control are denied unless the role specifically requires them. An agent cannot cause the enforcement layer, or any system it reaches, to fetch from or send to a destination on its behalf that it could not reach directly. A tool that sends (mail, tickets, shared documents, webhooks) is itself a destination: its recipients are bounded under this control, and sending through it to an unlisted recipient is denied.

### Rationale

Where an agent can send is part of what it can do, and it is the part through which data leaves. An agent that can reach an arbitrary endpoint can exfiltrate anything it can read, and the incidents that have already occurred used exactly the destinations this control denies by default: paste services, tunnels, webhooks, hosted spaces. Default-deny egress bounds the damage a compromised or misdirected agent can do to what it can reach, which is the enumeration ([4.1](../../source/principles/04-authority.md#control-4-1)) and nothing more.

### Assessment

For sampled agents, the permitted destinations are produced from the record and trace to the role. A staged request to an unlisted destination, directly or through a system the agent can instruct, is denied at the enforcement layer and surfaces under control [5.2](../../source/principles/05-oversight.md#control-5-2).

<a id="control-4-9"></a>

## Control 4.9 — Execution containment

**Scope:** Internal

**Source:** [Control 4.9](../../source/principles/04-authority.md#control-4-9).

### Requirement

Every agent that executes code, generates or causes code to run, or acts on the host it runs on, and any code it generates or causes to run, executes within a containment boundary that limits what it can reach to its enumerated authority ([4.1](../../source/principles/04-authority.md#control-4-1)). The boundary prevents access to the services of the host it runs on, limits filesystem access to the agent’s own working space and to remote resources it is explicitly authorized to use, and ensures that anything the agent runs inside the boundary is attributable to the agent ([1.1](../../source/principles/01-identity.md#control-1-1)) and subject to the same enforcement. The boundary isolates the agent’s execution from the host and from other agents at the level of the operating system kernel or stronger; isolation only at the level of a process or a namespace does not meet this control. An agent with no such capability satisfies this control by having none: its registered configuration ([1.2](../../source/principles/01-identity.md#control-1-2)) and its enumeration ([4.1](../../source/principles/04-authority.md#control-4-1)) show no code execution and no local effect, and a staged attempt to execute code is refused.

### Rationale

Agents write and run code, and code running somewhere is hard to attribute: is it still the agent, or something the agent started? The containment boundary answers the question by construction. Whatever runs inside it is the agent’s, bounded by the agent’s authority, and whatever it cannot reach from inside it cannot reach at all. The framework requires the boundary and its properties; the technology that provides it, and the configuration of harnesses within it, are left to the implementing organization.

### Assessment

For sampled agents, the assessor can identify the boundary and demonstrate that code executed by the agent inside it cannot reach host services, unauthorized filesystems, or destinations outside the agent’s permitted egress ([4.8](../../source/principles/04-authority.md#control-4-8)). A staged attempt by agent-generated code to reach beyond the boundary fails and is attributed to the agent in the record. For sampled agents registered without execution capability, a staged attempt to execute code is refused and surfaces under control [5.2](../../source/principles/05-oversight.md#control-5-2).

<a id="control-4-10"></a>

## Control 4.10 — Context and memory isolation

**Scope:** Internal

**Source:** [Control 4.10](../../source/principles/04-authority.md#control-4-10).

### Requirement

An agent’s retrieved context, working memory, and persistent memory are isolated per agent and, where the agent serves multiple principals, per principal. No agent reads or writes another agent’s memory or context except through a governed interface in its enumeration ([4.1](../../source/principles/04-authority.md#control-4-1)), and no shared writable resource exists across agent instances or runs unless it is itself behind the enforcement layer with per-identity write isolation.

### Rationale

Memory is where an agent’s instructions come from tomorrow. A memory one agent can poison is an instruction channel into another, and context that leaks across principals is a data breach that happens inside the agent rather than at its edge. Isolation keeps the content an agent processes ([4.6](../../source/principles/04-authority.md#control-4-6)) its own, so that what it has been told cannot be rewritten by a party that was never authorized to tell it anything.

### Assessment

For sampled agents, memory and context stores are shown to be partitioned per agent and per principal, and a staged write by one agent to another’s memory, or by one principal into another’s context, is refused. Shared stores in use are enumerated and sit behind the enforcement layer.

<a id="control-4-11"></a>

## Control 4.11 — Data boundary enforcement

**Scope:** Generic

**Source:** [Control 4.11](../../source/principles/04-authority.md#control-4-11).

### Requirement

The data boundary of the role ([4.1](../../source/principles/04-authority.md#control-4-1)) is enforced in both directions at the point of action. Before data leaves the organization’s control, including in prompts or context sent to a model the organization does not operate and in responses or messages sent to an external party or external agent, content outside the agent’s data authority is removed, masked, or tokenized. Before an agent acts on data it receives, the data is checked against the agent’s data authority and held or denied where it exceeds it. The clause on prompts and context applies to agents the organization operates. The organization declares the tolerance of the masking it applies, and masking that would defeat the task results in a held action under [5.3](../../source/principles/05-oversight.md#control-5-3) rather than a silent failure.

### Rationale

An agent’s data authority is meaningless if the data can leave in a prompt or arrive in a response. Models the organization does not operate, and agents it does not sponsor, are outside the boundary, and what crosses to them is a disclosure. Enforcing the boundary at the point of action, rather than relying on the agent to observe it, is the same principle as control [4.6](../../source/principles/04-authority.md#control-4-6): the agent’s judgment is not the control.

### Assessment

A staged prompt or outbound message containing data outside the agent’s authority is masked or held at the enforcement layer before it leaves, and a staged inbound payload exceeding the agent’s data authority is held or denied. The record under control [5.1](../../source/principles/05-oversight.md#control-5-1) shows the intervention.

<a id="control-4-12"></a>

## Control 4.12 — Separation of exposure

**Scope:** Generic

**Source:** [Control 4.12](../../source/principles/04-authority.md#control-4-12).

### Requirement

An agent’s role and authority are designed so that, within a single session, the agent does not combine all three of the following: processing content from sources the organization does not control, holding access to sensitive systems or data, and the ability to change state or communicate outside the organization. Where a role requires all three, the combination is declared in the role, the actions that complete it are rated above the pre-execution threshold ([5.3](../../source/principles/05-oversight.md#control-5-3)), and the design is approved as part of admission to production ([1.2](../../source/principles/01-identity.md#control-1-2)). The combination is evaluated across the agent graph and persistent memory, not only within one session: where agents that exchange messages or share memory jointly hold all three conditions, the combination is declared, rated, and approved in the same way, with a named sponsor for the combination. Untrusted content is defined in [Appendix A](../../source/appendices/a-terminology.md).

### Rationale

The three conditions together are the anatomy of nearly every agent compromise: untrusted content carries an instruction, access makes it possible, and an outbound capability makes it consequential. Removing any one of the three makes a successful manipulation ([4.6](../../source/principles/04-authority.md#control-4-6)) survivable. The framework does not forbid the combination, because some roles need it; it requires that it be a decision rather than a default.

### Assessment

For every role in the estate, and for every set of agents connected by messages or shared memory, the assessor can state which of the three conditions it holds. Roles holding all three are declared as such, their completing actions appear above the [5.3](../../source/principles/05-oversight.md#control-5-3) threshold, and their admission record shows the combination was approved.

<a id="control-4-13"></a>

## Control 4.13 — Registered tool and model definitions

**Scope:** Generic

**Source:** [Control 4.13](../../source/principles/04-authority.md#control-4-13).

### Requirement

Every tool and every model an agent is authorized to invoke is registered, with the authorized definition of each held in the registry ([1.2](../../source/principles/01-identity.md#control-1-2)): for a tool, its name, description, and input schema, or a pinned version or hash of them; for a model, its provider, identifier, and version. Invocation is checked against the registered definition at the enforcement layer ([4.4](../../source/principles/04-authority.md#control-4-4)), and a tool or model whose definition differs from the one registered is treated as unregistered until it is re-approved. A registered tool whose observed behavior departs from its registered definition is treated as changed ([5.2](../../source/principles/05-oversight.md#control-5-2)) even where its name and schema have not. A grant in an agent’s enumeration ([4.1](../../source/principles/04-authority.md#control-4-1)) refers to a registered definition, never to a name alone. An agent may discover tools at runtime only within a set recorded in the registry ([3.8](../../source/principles/03-role.md#control-3-8)); a discovered tool outside it is unregistered.

### Rationale

A framework that governs only known tools is defeated by a tool whose definition changes after it was authorized. A tool that keeps its name and its grant while its behavior changes is authority granted to something the organization never reviewed, and a model swapped beneath a stable label is the same failure in a different place ([3.7](../../source/principles/03-role.md#control-3-7)). Registering the definition, and enforcing against it, is what makes an enumeration of authority ([4.1](../../source/principles/04-authority.md#control-4-1)) an enumeration of things rather than of names.

### Assessment

The registry produces the authorized definition of every tool and model in any agent’s enumeration. A staged change to a registered tool’s definition results in denial at invocation and surfaces under control [5.2](../../source/principles/05-oversight.md#control-5-2) until re-approval is recorded. Tool and model definitions are verified against a signed or pinned source, so that substitution in the supply chain surfaces as an unregistered definition.

<a id="control-4-14"></a>

## Control 4.14 — Spawned-agent authority

**Scope:** Generic

**Source:** [Control 4.14](../../source/principles/04-authority.md#control-4-14).

### Requirement

When an agent creates a spawned agent ([2.4](../../source/principles/02-sponsor.md#control-2-4)), the spawned agent holds its own identity ([1.1](../../source/principles/01-identity.md#control-1-1)) and its own authority, conferred by the parent as a delegation ([4.3](../../source/principles/04-authority.md#control-4-3)): at most a subset of the parent’s authority, never all of it by default, and never the parent’s identity or credential. The union of the authority held by all agents spawned from one parent cannot exceed the parent’s authority, and the bound applies to the aggregate at any moment, not only hop by hop. The role ([3.1](../../source/principles/03-role.md#control-3-1)) and, for agents the organization operates, the registered harness settings ([1.2](../../source/principles/01-identity.md#control-1-2)) bound both the depth of spawning and the total number of agents a single root agent may give rise to, counted across the whole tree rather than per parent. The budget of the task is a single bound shared across the tree ([3.5](../../source/principles/03-role.md#control-3-5)).

### Rationale

Spawning is delegation in a new form, and it compounds: if each agent may create three agents with its own authority, the third generation is twenty-seven agents with the authority of the first. Spawning differs from delegation between existing agents in that the parent creates the actor as well as conferring the authority, which is why the spawned agent is an agent in its own right ([2.4](../../source/principles/02-sponsor.md#control-2-4)) rather than an extension of its parent acting under the parent’s identity. Bounding the tree as a whole, rather than each parent, is what prevents a swarm from assembling inside the rules.

### Assessment

A sampled spawned agent holds its own identity and less authority than its parent, and the aggregate authority of a sampled set of siblings is within the parent’s. A staged attempt to spawn beyond the declared depth or tree size is refused at the enforcement layer. A staged attempt by an external agent to instantiate an agent inside the organization without admission ([1.2](../../source/principles/01-identity.md#control-1-2)) is refused.

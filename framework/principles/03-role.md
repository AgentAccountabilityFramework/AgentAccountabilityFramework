# Principle 3: Role

[Framework contents](../README.md) · [Previous: Sponsor](02-sponsor.md) · [Next: Authority](04-authority.md)

**Domain:** Align

**Source:** [Section 4, Principle 3](../../source/principles/03-role.md#principle-3-role).

Every agent has a defined role: its purpose, success criteria, budget, autonomy level, and scope. The role is the reference for its authority and oversight. It is a job description, not a set of permissions; it expresses rules and intents and declares the agent’s reach and dependencies.

Requirements are normative; Rationale and Assessment are informative ([Section 4](../../source/04-framework-core.md)). Read these controls with the [boundary rule](../../source/02-scope.md#boundary-of-management) and [definitions](../../source/appendices/a-terminology.md).

<a id="control-3-1"></a>

## Control 3.1 — Documented, scoped purpose

**Scope:** Generic

**Source:** [Control 3.1](../../source/principles/03-role.md#control-3-1).

### Requirement

Every agent has a documented, scoped purpose: expected outcomes and explicit out-of-scope boundaries. The role is expressed as rules and intents. A rule is deterministic: an action satisfies it or does not. An intent is not, and is declared with the measure by which it is evaluated, a confidence score produced under Oversight ([5.6](../../source/principles/05-oversight.md#control-5-6)), and the confidence thresholds at which defined levels of recourse apply ([6.3](../../source/principles/06-recourse.md#control-6-3)). The role also declares its reach: the systems, data domains, and external parties the agent can affect. The documented role is the authoritative source from which enforced policy ([4.1](../../source/principles/04-authority.md#control-4-1), [4.2](../../source/principles/04-authority.md#control-4-2)) is derived, and it is held in a form that cannot be altered without detection. For an external agent, the role is the role of the engagement: what the agent is admitted to do in the organization, defined by the organization.

### Rationale

Neither authority nor deviation can be evaluated without a reference point. The out-of-scope boundary matters as much as the purpose itself, because an agent doing something useful but unmandated is still a governance failure. Not everything a role requires can be written as a pass or fail. An agent that serves the requests of the people who use it, or that exercises judgment within a purpose, is governed by intents, and an intent is only a control when the role says how it will be measured and what happens at each level of confidence. Declaring the thresholds in the role makes recourse a consequence of the job description rather than a decision improvised at runtime. Declaring reach gives the organization the measure by which it scales oversight ([Section 4](../../source/04-framework-core.md)). Making the role tamper-evident keeps it a control: a role that can be quietly edited is a role that can be quietly widened.

### Assessment

The role description exists, is versioned, and states both expected outcomes and explicit exclusions. From the document alone, an assessor can name at least one action the agent is capable of but not mandated to perform. The role distinguishes its rules from its intents; every intent names its measure and the confidence thresholds that trigger each level of recourse; the role names its reach; and a staged alteration of the role outside the change process ([3.4](../../source/principles/03-role.md#control-3-4)) is detectable.

<a id="control-3-2"></a>

## Control 3.2 — Measurable success criteria

**Scope:** Generic

**Source:** [Control 3.2](../../source/principles/03-role.md#control-3-2).

### Requirement

Every active agent has defined, measurable success criteria. The criteria include whether the agent is used and whether it returns value against its purpose and its budget ([3.5](../../source/principles/03-role.md#control-3-5)), not only whether it behaves; value is assessed against the criteria the sponsor declared, not against the assessor’s judgment of worth.

### Rationale

An agent that cannot fail cannot be governed. Success criteria let the organization ask whether an agent is succeeding rather than only whether it is behaving, and they are the basis for re-scoping or retiring an underperformer. An agent that behaves perfectly and is never used, or is used and returns nothing, is a cost with a sponsor. Including value in the criteria is what lets the organization retire an agent for not being worth having, and not only for misbehaving.

### Assessment

“Is this agent performing well?” is answerable in objective terms at any point in its lifecycle, by a party outside the deploying team, from the recorded criteria and current measurements. The recorded criteria include measures of utilization and value, and the current measurements under control [5.5](../../source/principles/05-oversight.md#control-5-5) report against them.

<a id="control-3-3"></a>

## Control 3.3 — Readable beyond the deploying team

**Scope:** Generic

**Source:** [Control 3.3](../../source/principles/03-role.md#control-3-3).

### Requirement

The role is documented to the standard of a job description: a party outside the deploying team, whether auditor, security, or leadership, can determine from it what the agent should and should not be doing. The confidence thresholds declared under [3.1](../../source/principles/03-role.md#control-3-1) and [4.7](../../source/principles/04-authority.md#control-4-7) are held with the role but disclosed only to parties with a need to know; readability beyond the team does not make the thresholds public.

### Rationale

A role description only its authors can interpret is a private understanding, not a governance instrument. The test is whether the document transfers judgment to a reader with no prior context.

### Assessment

A reviewer outside the owning team, given only the role description and a log of agent actions, correctly classifies sampled actions as in-scope or out-of-scope.

<a id="control-3-4"></a>

## Control 3.4 — Role versioning and change control

**Scope:** Generic

**Source:** [Control 3.4](../../source/principles/03-role.md#control-3-4).

### Requirement

The documented role reflects the agent’s actual current use. When scope changes, the role is re-scoped, and authority re-derived, before or with the change rather than after it. Every version of the role is retained, and a change to the role is a change event: it is proposed, approved by a party with authority over the role, applied as a new version, and followed by re-derivation of the agent’s authority ([4.2](../../source/principles/04-authority.md#control-4-2)) and re-validation of its behavior against the new version ([5.6](../../source/principles/05-oversight.md#control-5-6)) before the agent acts under it. Changes are tiered by their effect on the role, its intents, its reach, and the authority derived from it: a change below a declared threshold follows a lighter path, and a change that widens the role, its intents, or its reach above a declared reach threshold is approved by a second party other than the sponsor and treated as a new admission to production ([1.2](../../source/principles/01-identity.md#control-1-2)).

### Rationale

Scope drift is the normal failure mode of deployed agents: capability grows, documentation lags, and authority outlives its justification. Re-scoping before the change is what keeps the role a control rather than a memorial. A role that can be edited in place is a role with no history. Versioning and an approval gate make the evolution of an agent a sequence of decisions someone made, rather than a drift no one noticed. Treating a widening of scope as a new admission closes the gap through which an agent approved for one purpose becomes, months later, something else.

### Assessment

For sampled recent scope changes, the role revision predates or accompanies the change in the record. Observed agent activity contains no sustained action classes absent from the current role. The role’s version history is complete, each version names its approver, and for sampled changes the record shows re-derivation of authority and re-validation preceding the agent’s first action under the new version.

<a id="control-3-5"></a>

## Control 3.5 — Defined budget

**Scope:** Generic

**Source:** [Control 3.5](../../source/principles/03-role.md#control-3-5).

### Requirement

Every role declares a budget bound: the tokens, spend, or other resource units the agent may consume over a defined period, and per run where a single run can be material. The bound is enforced at the enforcement layer as a cap, consumption is metered and attributed to the agent and its sponsor ([2.1](../../source/principles/02-sponsor.md#control-2-1)), and consumption is measured against the bound under control [5.5](../../source/principles/05-oversight.md#control-5-5). The bound includes limits on concurrency, enforced at the enforcement layer for every agent, and on iteration, enforced in the harness and reported to the enforcement layer for agents the organization operates, so that a runaway loop or an uncontrolled fan-out of work is stopped as a budget breach. Where an agent delegates work to other agents or creates spawned agents ([4.3](../../source/principles/04-authority.md#control-4-3), [4.14](../../source/principles/04-authority.md#control-4-14)), the budget of the delegated task is a single bound on the aggregate consumption of every agent working on it, counted across the whole tree and reserved at the point of approval, so that neither the division of the task nor the timing of separate checks can approve in parts what the bound would deny as a whole.

### Rationale

An agent without a budget has an unbounded cost, and cost incurred at machine speed is a form of harm the organization must be able to answer for. Placing the budget in the role makes it a property of the job, decided by the sponsor when the role is defined, rather than an operational figure discovered on an invoice. A budget the enforcement layer cannot apply is a forecast, not a bound. A loop that never terminates and a burst that saturates a downstream system are budget failures as much as cost failures, and they are the ones that arrive fastest. A bound applied per agent does not bound the task: a permission that allows each of ten agents to spend within its limit allows the ten together to spend ten times it, and checks made separately can each approve before any cost is recorded. The task is the unit the sponsor funds, so the task is the unit the bound applies to.

### Assessment

For any agent, the assessor can produce the declared bound, the enforcement point that applies it, and the attributed consumption for the period. A staged run that would exceed the bound is stopped or held at the enforcement layer, and the event is recorded under control [5.1](../../source/principles/05-oversight.md#control-5-1). No role in the estate is without a declared bound. A staged runaway loop is stopped at the enforcement layer within the defined bound. A staged delegated task whose child agents would together exceed the task bound is stopped at the enforcement layer when the aggregate is reached, including where the children’s requests arrive concurrently.

<a id="control-3-6"></a>

## Control 3.6 — Autonomy level

**Scope:** Generic

**Source:** [Control 3.6](../../source/principles/03-role.md#control-3-6).

### Requirement

Every role declares its autonomy level: the degree to which the agent may act without a human disposition, expressed as the consequence threshold applied under control [5.3](../../source/principles/05-oversight.md#control-5-3) and the action classes the agent may execute below it. The level is granted only after the agent has met its success criteria ([3.2](../../source/principles/03-role.md#control-3-2)) over a defined period and has withstood adversarial testing ([5.7](../../source/principles/05-oversight.md#control-5-7)) at that level, since reliability on benign inputs is not evidence of robustness, and is reduced, with the threshold adjusted accordingly, when the agent fails either.

### Rationale

Autonomy is earned, not assigned. An agent’s reliability, measured against its role, is the evidence that justifies how much of that role it may execute unsupervised. Declaring the level in the role makes the amount of unsupervised action a decision the organization can defend and revisit, and makes the ladder from supervised to autonomous explicit instead of implicit in a threshold setting no one owns.

### Assessment

For sampled agents, the record shows the declared level, the evidence under control [5.5](../../source/principles/05-oversight.md#control-5-5) that justified it, the date it was granted, and the party who granted it. An agent that has failed its success criteria for the defined period shows a recorded reduction in autonomy, and a corresponding change in its [5.3](../../source/principles/05-oversight.md#control-5-3) threshold, before its next high-consequence action.

<a id="control-3-7"></a>

## Control 3.7 — Model, harness, and instruction binding

**Scope:** Internal

**Source:** [Control 3.7](../../source/principles/03-role.md#control-3-7).

### Requirement

Every role declares the model or models the agent uses and the harness that runs it, as registered ([1.2](../../source/principles/01-identity.md#control-1-2)). A change to either, including a change made by a model or harness provider beneath an unchanged name or version label, is a change event ([3.4](../../source/principles/03-role.md#control-3-4)): the agent is re-validated against its role ([5.6](../../source/principles/05-oversight.md#control-5-6)) before it acts under the new model or harness, and its authority is re-derived where the change affects what it can do. The role also binds the agent’s live instructions: its system prompt, skills, rules, and seeded memory. The instructions running at any moment match the approved version of the role; a change to them is a change event ([3.4](../../source/principles/03-role.md#control-3-4)), and a mismatch between the running instructions and the approved version is a deviation ([5.2](../../source/principles/05-oversight.md#control-5-2)). Because a provider may change a model behind an unchanged label, the organization detects such change by behavioral sampling against the baseline ([5.2](../../source/principles/05-oversight.md#control-5-2)), and this control is satisfied when the sampling runs on the defined cadence and a detected change triggers re-validation. A change made to remediate a disclosed vulnerability may proceed under an emergency exception: the agent operates at reduced autonomy ([3.6](../../source/principles/03-role.md#control-3-6)) until re-validation completes within a defined time.

### Rationale

An agent is its model and its harness as much as its prompt. The same role on a different model can behave materially differently, and providers change models under stable names. A framework that checked the role once and never asked what was running it would be certifying a document, not an agent. Binding the model and harness to the role, and treating their change as a change event, keeps the thing that was assessed the thing that is running.

### Assessment

For sampled agents, the declared model, harness, and instructions match what is observed at runtime, and a staged change to the running instructions outside the change process surfaces under control [5.2](../../source/principles/05-oversight.md#control-5-2). For a sampled model or harness change, including a provider-side change detected under control [5.2](../../source/principles/05-oversight.md#control-5-2), the record shows re-validation preceding the agent’s next action.

<a id="control-3-8"></a>

## Control 3.8 — Declared dependencies and dependents

**Scope:** Generic

**Source:** [Control 3.8](../../source/principles/03-role.md#control-3-8).

### Requirement

Every role declares the agents, tools, models, and data sources the agent depends on to perform its role, and the registry ([1.2](../../source/principles/01-identity.md#control-1-2)) derives from those declarations which agents depend on this one. Dependencies are declared before the agent acts and are kept current under control [3.4](../../source/principles/03-role.md#control-3-4). An agent may discover tools at runtime only within a set or agent class recorded in the registry ([4.13](../../source/principles/04-authority.md#control-4-13)); a discovered tool outside it is unregistered. Before any dependency is changed, suspended, or decommissioned, its dependents are identified and a disposition for each is recorded ([6.5](../../source/principles/06-recourse.md#control-6-5)). For a dependency the organization does not operate, the role also declares the agent’s disposition when that dependency changes or becomes unavailable: continue, degrade, hold, or stop.

### Rationale

In a multi-agent estate, an agent that checks every box can still be broken by the retirement of an agent it relies on, and its sponsor may not know the dependency exists. An agent should not be withdrawn without a handover. Declaring dependencies turns the estate from a set of individually accountable agents into a structure the organization can reason about.

### Assessment

For sampled agents, the declared dependencies match observed invocations, and the registry answers “what depends on this agent?” for any entry. A staged decommissioning of an agent with dependents surfaces the dependents before the decommissioning proceeds.

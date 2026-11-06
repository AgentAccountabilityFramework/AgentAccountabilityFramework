# Principle 5: Oversight

[Framework contents](../README.md) · [Previous: Authority](04-authority.md) · [Next: Recourse](06-recourse.md)

**Domain:** Account

**Source:** Section 4, Principle 5.

Record what each agent does and the chain of delegated authority behind its actions. Detect departures from its role or authority while it runs, and evaluate actions with serious consequences before they execute. Check whether the agent meets its success criteria, and make the record available beyond the team that owns it. Re-establish expected behavior when the role, model, or harness changes.

The Requirement states what must be met. Rationale explains why, and Assessment describes supporting evidence; both provide guidance (Section 4). Apply the controls using the boundary rule and definitions.

<a id="control-5-1"></a>

## Control 5.1 — Complete, tamper-evident record

**Scope:** Generic

**Source:** Control 5.1.

### Requirement

Every action produces a tamper-evident record in two parts. The evidence part is kept for every action: what, when, the triggering context, the full delegation chain, the action’s provenance (1.5), any disposition applied (5.3), the source of the content that influenced the action, so that the record can name the author of an instruction and not only the agent that acted on it, and a tamper-evident reference to each item of content involved. When agents invoke agents, the evidence part reconstructs the complete chain of authority back to the accountable human sponsor, not just the immediate actor. The content part holds everything that crosses the organization’s boundary for the action and, for an agent the organization operates, the inputs the agent acted on (prompts, retrieved context, and tool responses) and the model’s outputs; it is reachable from the evidence part by reference, is classified and retained under the organization’s records and data classification obligations, and may be masked or tokenized under control 4.11 where the classification requires it. Tamper evidence holds for both parts against the agent, its sponsor, its owning team, and the administrators of the systems the agent uses; the organization declares whether administrators of the record itself are within the threat model. Retention and erasure duties are reconciled in a declared policy, and content stored in the record is treated as untrusted input (4.6) by any person or tool that reads it.

### Rationale

Accountability is reconstructable history. A record the agent or its owner can amend is testimony, not evidence, and a record that names only the last hop hides the principal. The chain-to-sponsor requirement is what makes multi-agent systems answerable to a person (2.1). What the agent was told and what the model said are the evidence that explains an action; an action without them can be attributed but not understood. Separating evidence from content lets the organization keep the proof of who acted, and under what authority, for as long as accountability requires, while handling prompts and context, which are large and often sensitive, under the rules that already govern such data.

### Assessment

For a sampled action deep in a multi-agent chain, the assessor reconstructs the full chain to the human sponsor from the record alone, and can demonstrate that post-hoc modification of the record is detectable. For a sampled action, the evidence part produces the chain, the provenance, the disposition, and the content references, and the content part, where retained, produces the inputs and the model output; the assessor can reconstruct what the agent was given, what it produced, what it did, and which content influenced it. The record explains the action; it is not relied on as a faithful account of the model’s reasoning.

<a id="control-5-2"></a>

## Control 5.2 — Runtime deviation surfacing

**Scope:** Generic

**Source:** Control 5.2.

### Requirement

Deviations from the documented role (3.1) or enumerated authority (4.1) surface while the agent is running, generating an alert to a party with the authority to act, or a real-time system-based restriction or constraint, not only in post-incident review. Deviation includes a confidence score against an intent declared in the role or authority (3.1, 4.7) falling below its declared threshold, and change in the agent’s behavior under an unchanged role and unchanged inputs, which indicates a change in the model or harness beneath it (3.7). Deviation is evaluated against a recorded baseline of expected behavior for the role. The baseline is a statistical description with a declared tolerance, since model output varies run to run, and deviation is a departure beyond the tolerance. The baseline is established from behavior observed under evaluation (5.6), not from unreviewed production behavior; it is re-established with each change event (3.4), with the re-establishment reviewed, and on a defined cadence, so that slow change in retrieval sources or tool backends is caught without a change event. The party alerted has the declared capacity to act within the window: coverage and triage are declared, not assumed.

### Rationale

At machine speed, oversight that arrives after the fact is commentary. Detection is therefore bound to actionability: an alert that reaches someone who cannot intervene is just a log entry. Two deviations are invisible to a control that only compares actions against grants. An agent pursuing an outcome its purpose never called for can pass every rule and still fall below an intent threshold. An agent whose answers have shifted because its model changed is within its role and no longer the agent that was assessed. Both are caught by comparing behavior against an expected baseline, and both are why a point-in-time assessment of an agent is not enough.

### Assessment

A staged deviation during assessment produces an alert, within the defined window, to a recipient who demonstrably holds suspension or revocation authority (6.1, 4.5). A staged below-threshold intent score and a staged model substitution each produce an alert within the defined window, and the assessor can produce the baseline each was measured against.

<a id="control-5-3"></a>

## Control 5.3 — Pre-execution disposition for high-consequence actions

**Scope:** Generic

**Source:** Control 5.3.

### Requirement

Action classes are rated by consequence, considering at minimum reversibility, materiality, and external impact. Classes above a defined threshold, the threshold for each agent being the one set by its autonomy level (3.6), are evaluated before execution, with a defined disposition for every proposed action: proceed, proceed with flag, hold for human decision, or deny. Prior approval does not carry forward; disposition attaches to each action, not to the session. Action classes include sequences: a sequence of actions whose combined consequence exceeds the threshold is rated as a class. The evidence presented to a human decider is produced by the enforcement layer from the proposed action itself (the action, its parameters, the resources affected, and the agent’s role and authority), not composed by the agent; text the agent wrote may accompany it, marked as such. The decider has a declared minimum time, and the volume of held actions per decider is bounded so that disposition remains a decision.

### Rationale

Some actions cannot be overseen after the fact because they cannot be undone: payments, deletions, external communications, filings. For these, oversight has to happen before execution. Requiring a defined disposition also formalizes the human-in-the-loop interface, meaning who decides, by when, recorded where, and replaces the ad hoc notification that gives the appearance of human oversight without the substance.

### Assessment

The consequence rating scheme and threshold are documented and applied to every action class in the enumeration (4.1). For sampled high-consequence actions, the record shows disposition preceding execution, and held actions show the deciding human, the decision, and its timestamp. No standing session-level approval covers individual high-consequence actions.

<a id="control-5-4"></a>

## Control 5.4 — Independently queryable audit trail

**Scope:** Generic

**Source:** Control 5.4.

### Requirement

The audit trail is queryable by parties outside the agent’s owning team. Access is bounded by need to know, is itself recorded, and treats the content it returns as untrusted input (5.1).

### Rationale

The team that builds an agent must not be the only party able to interrogate its history.

### Assessment

A party outside the owning team executes queries against the trail during assessment without mediation by the owning team.

<a id="control-5-5"></a>

## Control 5.5 — Performance against role

**Scope:** Generic

**Source:** Control 5.5.

### Requirement

The agent’s actual performance is measured against its role’s success criteria (3.2), and its consumption against its budget (3.5), on a defined cadence, and the results are visible to parties outside the owning team.

### Rationale

An accountable agent is evaluated, not just monitored. Performance measurement is how the organization decides whether an agent should be expanded, re-scoped, or retired; without it, those decisions get made by inertia.

### Assessment

“Is this agent succeeding?” and “Is this agent within budget?” are answerable in objective terms, on the record, at the defined cadence, by a party outside the owning team.

<a id="control-5-6"></a>

## Control 5.6 — Evaluation before and during operation

**Scope:** Internal

**Source:** Control 5.6.

### Requirement

Every agent is evaluated against its role before it enters production, before it acts under any change event (3.4, 3.7), and continuously while it operates. Evaluation covers conformance to role, authority, and intent, resistance to manipulation through content (4.6), and the agent’s success criteria (3.2). Evaluations follow the two kinds of definition in the role and authority (3.1, 4.7): rules, which an action passes or fails, and intents, for which the evaluation produces the confidence score the intent declares as its measure, compared against the confidence thresholds declared with it, at which the result becomes a disposition under control 5.3 or a recourse under control 6.3. The evaluator that produces a confidence score is validated against a representative test set with recorded error rates, is independent of the content it scores and takes no instruction from it, and is re-validated with each change event. Intent evaluation is applied to the trajectory of an agent’s actions as well as to each request. Resistance to manipulation is measured against an attack set that is refreshed on a defined cadence, and the organization records the limits of what the set covers.

### Rationale

An agent is a system whose behavior cannot be fully known from its definition, so the organization has to measure it: before it is trusted, each time something it depends on changes, and while it runs. The distinction between rules and intents matters because the two produce different evidence. A rule gives a pass or a fail and can be enforced as policy. An intent evaluation gives a degree of confidence, and the role or authority decides in advance, in its declared thresholds, what confidence is enough and what happens when it is not, so that a scored judgment becomes a deterministic consequence rather than a dashboard.

### Assessment

For sampled agents, the record shows evaluation results preceding production entry and preceding the first action after each change event, and continuous evaluation results on the defined cadence. The role and authority name their rules and intents, the measure and thresholds for each intent, and the disposition or recourse each threshold triggers, and a sampled below-threshold result shows the triggered consequence.

<a id="control-5-7"></a>

## Control 5.7 — Adversarial testing

**Scope:** Internal

**Source:** Control 5.7.

### Requirement

Agents in production are subject to adversarial testing on a declared cadence, scaled to the agent’s reach (3.1) and the consequence of its action classes (5.3), and repeated at every change event (3.4, 3.7), that attempts to make them exceed their role, authority, or intent through the content they process, through delegation (4.3), and through the tools and agents they interact with. Findings are treated as deviations (5.2), and an agent that fails is subject to the dispositions of Principle 6 until the failure is addressed. Tests in production use canary assets and credentials that confer nothing if misused. Testing is designed and executed by a party independent of the agent’s owning team.

### Rationale

The threats to an agent are rehearsed by its attackers continuously; the organization’s defenses should be rehearsed at least as often. Testing in production, against the agent as it actually runs, is what distinguishes evidence that the controls hold from a belief that they do. A cadence declared in the role and scaled to what the agent can affect is what distinguishes testing from an occasional exercise, and independence from the owning team is what distinguishes a test from a demonstration.

### Assessment

The record shows adversarial tests executed against production agents on the declared cadence and after each change event, by a party independent of the owning team, the findings, and the disposition of each. A sampled finding shows the agent’s treatment under Principle 6 and the re-validation that preceded its return to service.

<a id="control-5-8"></a>

## Control 5.8 — Estate discovery and reconciliation

**Scope:** Generic

**Source:** Control 5.8.

### Requirement

The registry population (1.2) is reconciled against independent observation on a defined cadence and on demand: identity provider logs, enforcement layer and gateway traffic, tool invocations, vendor product administration consoles, endpoint inventories, and network egress from devices and workloads, so that agents outside any gateway the organization controls are found. An agent discovered acting in the organization without a registry entry, including an agent enabled inside a vendor’s product, an agent on a browser or a developer endpoint, and an agent an employee brings, is disabled or enrolled within a defined window, and the interval between discovery and enrollment is recorded as nonconformance rather than hidden. Reconciliation also finds tools and models in use that are absent from the registry (4.13) and enforceable authority held by any non-active registry entry (6.5).

### Rationale

A registry is a claim about the population; reconciliation is the evidence for it. Agents arrive in ways no admission process sees: enabled by a vendor inside a product, started on a developer endpoint, brought by an employee. The framework does not assume these do not happen; it requires that they be found, and that the time during which an unregistered agent held authority be visible rather than quietly closed.

### Assessment

The record shows reconciliation executed on the defined cadence, the sources compared, and the result. Reconciliation finds no active agent, tool, or model absent from the registry, or every exception is recorded with its discovery time, its disposition, and its enrollment or disablement within the window. A staged unregistered agent acting through a route the organization does not gateway is found within the defined cadence.

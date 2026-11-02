# Framework Core: Principles and Controls

[Framework contents](README.md) · [Previous: Terminology](03-terminology.md) · [Next: Identity](principles/01-identity.md)

Source: [Section 4: The Framework Core](../source/04-framework-core.md#4-the-framework-core-principles-and-controls).

The Framework Core is the normative body of the framework: three domains, six principles, and the controls beneath them. Conformance is evaluated against the controls' Requirements.

Sections 1–3 and 5–8 are informative. The [Appendix A definitions](../source/appendices/a-terminology.md#appendix-a-terminology) and the [Section 2 boundary rule](../source/02-scope.md#boundary-of-management) have normative effect: the definitions fix the meaning of terms used in controls, and the boundary rule constrains how every control is read.

## Domains and principles

The principles follow an agent's admission to production: establish what it is, who answers for it, what it is to do, what access it needs, whether it is doing what is expected, and what happens when it is not. Each principle builds on the one before it; a failure upstream invalidates verification downstream.

| Domain | Question | Principles in reading order |
| --- | --- | --- |
| [Assign](../source/principles/01-identity.md#principle-1-identity) | Who is this, and who answers for it? | 1. [Identity](principles/01-identity.md); 2. [Sponsor](principles/02-sponsor.md) |
| [Align](../source/principles/03-role.md#principle-3-role) | What is it for, and what may it do? | 3. [Role](principles/03-role.md); 4. [Authority](principles/04-authority.md) |
| [Account](../source/principles/05-oversight.md#principle-5-oversight) | Is it doing what we expect, and what happens when it isn't? | 5. [Oversight](principles/05-oversight.md); 6. [Recourse](principles/06-recourse.md) |

## How to read a control

Each control has three separate fields:

| Field | Status | Purpose |
| --- | --- | --- |
| Requirement | Normative | States the obligation. For a given agent estate, an assessor can answer it yes or no. Conformance is evaluated against this field alone. |
| Rationale | Informative | Explains why the requirement exists, independently of implementation, and guides interpretation in situations the authors did not foresee. |
| Assessment | Informative | Describes the pattern of evidence expected to satisfy the Requirement, from the assessor's point of view. |

Where a Requirement contains several obligations, each is assessed. The control is met only when all are met; a partly met control is not met, and the unmet obligation is recorded as the finding.

Controls follow a common progression within each principle: **existence**, meaning the property is defined; **enforcement**, meaning it is technically real; and **lifecycle**, meaning it survives organizational change.

A bare number in parentheses, such as ([1.2](../source/principles/01-identity.md#control-1-2)), refers to a control. Section references use “Section” followed by the section number.

## Scope tags and the organizational boundary

Each control has a Scope tag, defined in [Appendix A: Scope tag](../source/appendices/a-terminology.md#scope-tag):

| Scope tag | Applies to |
| --- | --- |
| Generic | Every agent in the estate, internal or external. |
| Internal | Agents the organization operates, because the control requires access to the agent's internals. |
| External | External agents only. |

Every agent is subject to every control whose Scope tag includes it. Where a clause of a Generic control explicitly applies only to agents the organization operates, that clause is assessed only for those agents. Internal controls do not apply to external agents; the organization compensates at its boundary.

Every control is satisfied from within the organization's own boundary. No control requires authority over a party the organization does not operate. Apply the [Section 2 boundary rule](../source/02-scope.md#boundary-of-management) when reading every control.

## Consequence and reach

The framework assigns no risk tier to agents. An agent's model, the content it processes, and its behavior can change after deployment; an agent that meets a barrier in its task can try other routes to complete it. An agent classified as low risk at deployment can become a high-consequence actor without a new decision. The framework does not assume that an agent will behave as a person would.

The framework uses action classes and declared reach:

- **Action classes** group actions that share a consequence profile and common authorization and recourse treatment ([Appendix A: Action class](../source/appendices/a-terminology.md#action-class)). Classes are rated by consequence under [Control 5.3](../source/principles/05-oversight.md#control-5-3).
- **Declared reach** identifies the systems, data domains, and external parties an agent can affect through its authority ([Appendix A: Reach](../source/appendices/a-terminology.md#reach)). It is declared in the agent's role under [Control 3.1](../source/principles/03-role.md#control-3-1).

Consequence and reach determine the level of oversight and the bounds of authority, not whether the controls apply. Where an organization is subject to a regime that classifies systems by use case, it maps that classification onto action classes and declared reach and records the mapping.

# Framework Core: Principles and Controls

[Framework contents](README.md) · [Previous: Terminology](03-terminology.md) · [Next: Identity](principles/01-identity.md)

Source: Section 4: The Framework Core.

The Framework Core sets the requirements used to assess agent accountability. Meeting these requirements is called conformance. The controls are organized into six principles. These sit in three groups, called domains.

Sections 1–3 and 5–8 provide explanation and guidance, called informative material. Two parts outside the Core also determine how the requirements apply:

- The Appendix A definitions fix what the terms in the controls mean.
- The Section 2 boundary rule governs how you apply controls from within your organization's own boundary.

These have normative effect: you must use them when interpreting and applying a control.

## Domains and principles

The principles follow the steps for admitting an agent to production. Each depends on the ones before it. If an earlier principle fails, verification of the later principles is no longer valid. For example, you cannot verify who answers for an agent until you can identify that agent (Principle 1: Identity).

| Domain | Question | Principles in reading order |
| --- | --- | --- |
| Assign | Who is this, and who answers for it? | 1. [Identity](principles/01-identity.md); 2. [Sponsor](principles/02-sponsor.md) |
| Align | What is it for, and what may it do? | 3. [Role](principles/03-role.md); 4. [Authority](principles/04-authority.md) |
| Account | Is it doing what we expect, and what happens when it isn't? | 5. [Oversight](principles/05-oversight.md); 6. [Recourse](principles/06-recourse.md) |

## How to read a control

Each control separates what you must meet from the explanation and evidence that help you assess it:

| Field | Status | Purpose |
| --- | --- | --- |
| Requirement | Normative (required) | States what must be true. The assessor checks whether your organization meets it and answers yes or no. Conformance is judged against this field alone. |
| Rationale | Informative (guidance) | Explains why the requirement exists, regardless of how you implement it. Helps you interpret it in situations the authors did not anticipate. |
| Assessment | Informative (guidance) | Describes the evidence an assessor expects to see when checking whether the Requirement is met. |

Some Requirements contain several obligations. The assessor checks each one. All must be met for the control to pass; meeting only some is not enough. The assessment records the unmet obligation as a finding.

Within each principle, controls follow a common progression:

- **Existence:** The required property, such as an agent's role, is defined.
- **Enforcement:** Your systems enforce the requirement in operation.
- **Lifecycle:** The requirement continues to be met as your organization changes.

A number in parentheses, such as (1.2), points to a control. References to sections include the word “Section.”

## Scope tags and the organizational boundary

Each control has a Scope tag that tells you which agents it applies to. Your agent estate includes all agents operating in or on behalf of your organization.

| Scope tag | Applies to |
| --- | --- |
| Generic | Every agent in your estate, internal or external. |
| Internal | Agents your organization operates. These controls require access to the agent's internals. |
| External | External agents only. |

Your organization must meet every control whose Scope tag includes the agent. A Generic control may explicitly limit one of its clauses to agents you operate. Assess that clause only for those agents. Internal controls do not apply to external agents; your organization addresses the resulting gaps through controls at its own boundary.

Every control is met from within your organization's own boundary. You do not need authority over another operator's people or systems. Where you cannot apply a control directly to an external agent, tool, or model, apply it to what crosses your boundary and to the relationship with its operator, and hold that operator to an agreement. This is the Section 2 boundary rule.

## Consequence and reach

An agent's behavior can change after deployment. Its model or the content it processes may change, and it may try another route when it cannot complete a task. An agent considered low risk at deployment can later take actions with serious consequences without anyone making a new decision about it.

The framework therefore assigns no risk tier to agents and does not assume they will behave as people would. It uses two things to set the level of oversight and the limits on authority:

- **Action classes** group actions with similar consequences and a common approach to authorization and recourse (Appendix A: Action class). Rate each class by consequence under Control 5.3.
- **Declared reach** lists the systems, data domains, and external parties an agent can affect using its authority (Appendix A: Reach). Record this reach in the agent's role under Control 3.1.

Consequence and reach do not change which controls apply; the Scope tags still determine that. If rules your organization must follow classify systems by use case, record how those classifications map to action classes and declared reach.

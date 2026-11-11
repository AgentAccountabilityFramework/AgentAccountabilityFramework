# Scope

[Framework contents](README.md) · [Previous: Purpose](01-purpose.md) · [Next: Terminology](03-terminology.md)

Source: [Section 2: Scope](../source/v1.0/02-scope.md#2-scope).

## In scope

The framework covers AI agents operating in or on behalf of an organization with delegated authority to access information or take actions. This includes agents you deploy yourself, agents created by other agents, and agents provided by a third party, either on their own or inside another product. Both autonomous and semi-autonomous agents are covered, including agents that call other agents.

The framework uses these terms:

- **[Internal agents](../source/v1.0/appendices/a-terminology.md#internal-agent):** Agents your organization builds or operates itself, under its own sponsor and in its own registry.
- **[External agents](../source/v1.0/appendices/a-terminology.md#external-agent):** Agents operated by a third party that act on, interact with, or are relied upon by your organization.
- **[Spawned agents](../source/v1.0/appendices/a-terminology.md#spawned-agent):** Agents created by other agents. Each is an agent in its own right under every principle.

Agents are covered however they arrive, including through a vendor feature, a browser, a developer's computer, or an employee bringing one into the organization.

## Out of scope

The framework excludes:

- Model safety and alignment.
- Construction of the models themselves.
- General AI ethics.
- Employment-law and HR rules for human workers.
- Redress for people affected by automated decisions (algorithmic recourse). This is governed by the regulatory requirements your organization is already subject to.
- General systems security and operations. The framework assumes these practices are in place and does not assess them.

For example, if a document tricks an agent into trying an action outside its authority, that action must still be blocked. The framework constrains what the agent can do; it does not prescribe how to prevent the model from being manipulated ([Control 4.6](../source/v1.0/principles/04-authority.md#control-4-6)).

A requirement belongs in the Framework Core when it is specific to agents and would not make sense for an ordinary software workload:

- A sponsor, a role, a delegation chain, and an intent boundary are properties of an agent.
- Encrypted data transport and patching software dependencies are general systems practices.

Where a general practice has a consequence specific to agents, the framework makes that consequence a control and leaves the underlying practice to your organization. For example, within your organization's boundary, an agent may hold only its own identity credentials ([Control 1.4](../source/v1.0/principles/01-identity.md#control-1-4)). How secrets are stored and distributed is outside the framework.

You must still declare the agents, tools, models, and data sources an agent relies on and keep that dependency record current ([Control 3.8](../source/v1.0/principles/03-role.md#control-3-8)).

## Boundary of management

This rule has normative effect: you must use it when applying every control ([Section 4: Framework Core](../source/v1.0/04-framework-core.md#4-the-framework-core-principles-and-controls)). It follows the [Section 2 boundary rule](../source/v1.0/02-scope.md#boundary-of-management).

External agents and third-party tools and models are covered for what they do inside your organization. Every control is met from within your organization's own boundary. No control requires you to have authority over another operator's people or systems, or to control how they run an agent, tool, or model.

Where you cannot apply a control directly to that party, apply it to what crosses your boundary and to the relationship with the operator. Hold the operator to an agreement under [Control 2.5](../source/v1.0/principles/02-sponsor.md#control-2-5). The **operator of record** is the organization running the external agent, tool, or model, with an agreement assigning accountability and a named accountable contact.

An external agent admitted to act in your organization is subject to all six principles at the boundary:

- **Identity:** Identify the agent and manage the credentials it uses to act in your organization ([1.1](../source/v1.0/principles/01-identity.md#control-1-1), [1.3](../source/v1.0/principles/01-identity.md#control-1-3)).
- **Sponsor:** Name the internal human who answers for it ([2.1](../source/v1.0/principles/02-sponsor.md#control-2-1)).
- **Role:** Define what it is admitted to do in your organization ([3.1](../source/v1.0/principles/03-role.md#control-3-1)).
- **Authority:** List the information it may access and the systems and tools it may use ([4.1](../source/v1.0/principles/04-authority.md#control-4-1)).
- **Oversight:** Record what crosses your boundary ([5.1](../source/v1.0/principles/05-oversight.md#control-5-1)).
- **Recourse:** Revoke its credentials, sessions, and authority at your boundary within the required suspension window. Work through its operator of record to pursue suspension of the runtime itself ([6.1](../source/v1.0/principles/06-recourse.md#control-6-1), [2.5](../source/v1.0/principles/02-sponsor.md#control-2-5)).

If an agent you operate depends on an agent, tool, or model you do not control, declare that dependency ([3.8](../source/v1.0/principles/03-role.md#control-3-8)), bound the agent's access and outbound destinations ([4.1](../source/v1.0/principles/04-authority.md#control-4-1), [4.8](../source/v1.0/principles/04-authority.md#control-4-8)), and hold the dependency to an operator of record ([2.5](../source/v1.0/principles/02-sponsor.md#control-2-5)). The role must also say what the agent does if that dependency changes or becomes unavailable: continue, degrade, hold, or stop ([3.8](../source/v1.0/principles/03-role.md#control-3-8)).

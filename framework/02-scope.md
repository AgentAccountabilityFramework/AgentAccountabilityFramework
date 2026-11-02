# Scope

[Framework contents](README.md) · [Previous: Purpose](01-purpose.md) · [Next: Terminology](03-terminology.md)

Source: [Section 2: Scope](../source/02-scope.md#2-scope).

## In scope

The framework covers AI agents operating in or on behalf of an organization with delegated authority to access information or take actions. This includes autonomous and semi-autonomous agents, agents embedded in business applications, and agents that invoke other agents:

- **Internal agents:** agents the organization builds and operates.
- **External agents:** agents operated by a third party that act on or interact with the organization.
- **Spawned agents:** agents created by other agents, which are agents in their own right under every principle.

Agents are included however they arrive: built by the organization, enabled by a vendor inside a product it uses, running in a browser or on a developer endpoint, or brought by an employee.

## Out of scope

The framework excludes:

- Model safety and alignment.
- General AI ethics.
- The employment-law and HR treatment of human workers.
- Redress for individuals affected by automated decisions (algorithmic recourse), which is governed by the regulatory instruments the organization is already subject to.
- The general discipline of securing and operating information systems, which the framework assumes and neither restates nor assesses.

The framework governs the accountability of agents as deployed actors; construction of the models that power them is outside its scope. Where model behavior creates an accountability risk, such as manipulation through the content an agent processes, the framework constrains the consequences rather than the model itself ([Control 4.6](../source/principles/04-authority.md#control-4-6)).

A requirement belongs in the Framework Core when it would be meaningless for a conventional workload. A sponsor, a role, a delegation chain, and an intent boundary are properties of an agent; encrypted transport and patched dependencies are properties of any system. Where a general practice has an agent-specific consequence, the framework states that consequence as a control and takes the practice itself as the organization's own declaration. For example, an agent must not hold credentials it was not issued ([Control 1.4](../source/principles/01-identity.md#control-1-4)); how secrets are stored and distributed is outside the framework.

## Boundary of management

This rule has normative effect and constrains how every control is read ([Section 4: Framework Core](../source/04-framework-core.md#4-the-framework-core-principles-and-controls)). The following text preserves the [Section 2 boundary rule](../source/02-scope.md#boundary-of-management).

External agents and third-party tools and models are in scope for what they do inside the organization, not for how their operators run them. Every control in this framework is satisfied from within the organization’s own boundary. No control requires the organization to hold authority over a party it does not operate: an external agent, a third-party tool or model, or the people and systems behind them. Where a control cannot be applied to such a party, the organization applies it to what crosses its boundary and to the relationship, and holds the party’s operator to an agreement ([2.5](../source/principles/02-sponsor.md#control-2-5)).

An external agent admitted to act in the organization is subject to every principle at the boundary: identity and credentials at the boundary ([1.1](../source/principles/01-identity.md#control-1-1), [1.3](../source/principles/01-identity.md#control-1-3)), an internal sponsor ([2.1](../source/principles/02-sponsor.md#control-2-1)), the role of the engagement ([3.1](../source/principles/03-role.md#control-3-1)), enumerated authority ([4.1](../source/principles/04-authority.md#control-4-1)), oversight of what crosses the boundary ([5.1](../source/principles/05-oversight.md#control-5-1)), and recourse that begins with revoking the credential ([6.1](../source/principles/06-recourse.md#control-6-1)) and ends with the operator of record ([2.5](../source/principles/02-sponsor.md#control-2-5)).

An agent the organization operates that depends on tools, models, or agents it does not control treats each such dependency as declared ([3.8](../source/principles/03-role.md#control-3-8)), bounded ([4.1](../source/principles/04-authority.md#control-4-1), [4.8](../source/principles/04-authority.md#control-4-8)), and held to an operator of record ([2.5](../source/principles/02-sponsor.md#control-2-5)), and declares what the agent does when that dependency changes or fails.

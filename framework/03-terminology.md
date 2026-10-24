# Terminology

These definitions follow AAF version 0.9.4 — Working Draft. The first two summarize the framework's descriptions; the remaining entries use the terms defined in [Appendix A](../source/appendices/a-terminology.md). Appendix A definitions have normative effect; formal conformance keywords such as “shall” and “should” remain to be introduced with Section 5. ([Source: Sections 3](../source/03-terminology.md) and [4](../source/04-framework-core.md).)

## Agent Accountability

The organization's ability to answer, with evidence, what agent acted, on whose authority, within what bounds, and how it can be stopped. An accountable agent is identified, sponsored, given a role, granted bounded authority, overseen, and subject to recourse. Accountability does not establish that the organization is secure or that its models are safe or aligned. ([Source: Abstract](../source/00-front-matter.md#abstract), [Section 1: Purpose](../source/01-purpose.md), and [Section 5: Conformance and Assessment](../source/05-conformance-and-assessment.md).)

## Agent Accountability Framework

The framework that defines the outcomes an organization must achieve to make its agents accountable, expressed as principles and testable controls. Each control has a normative Requirement and informative Rationale and Assessment fields in the current draft. The framework is vendor-neutral and leaves the choice of processes, technologies, and architecture to the implementing organization. ([Source: Section 1: Purpose](../source/01-purpose.md), [Section 4: Framework Core](../source/04-framework-core.md), and [Section 6: Implementation Neutrality](../source/06-implementation-neutrality.md).)

## Principle

One of the framework's six top-level requirements: Identity, Sponsor, Role, Authority, Oversight, and Recourse. The principles are grouped into Assign (Identity and Sponsor), Align (Role and Authority), and Account (Oversight and Recourse). Each principle contains controls against which conformance is evaluated. ([Source: Appendix A — Principle](../source/appendices/a-terminology.md#principle) and [Section 4: Framework Core](../source/04-framework-core.md).)

## Registry

The authoritative record of all agent identities in the organization's estate, including each agent's sponsor, owning team, and lifecycle status, and of the tools and models agents are authorized to invoke, including their authorized definitions. For each agent, it also records the harness and relevant settings, permitted runtime locations, agent class attributes, and declared dependencies. “Registry” describes a property the organization must demonstrate; it does not prescribe a particular product or component. ([Source: Appendix A — Registry](../source/appendices/a-terminology.md#registry) and [Section 6: Implementation Neutrality](../source/06-implementation-neutrality.md).)

## Credentials

Evidence an agent presents to authenticate as its identity. A credential is bound to that identity and to the resource it was issued for, and is issued, rotated, and revoked through a managed lifecycle. An agent may have several credentials; each is distinct from the identity it evidences. Credential custody and mediation are governed by Control 1.4. ([Source: Appendix A — Credential](../source/appendices/a-terminology.md#credential), [Control 1.3](../source/principles/01-identity.md#control-1-3), and [Control 1.4](../source/principles/01-identity.md#control-1-4).)

## Identity

In the AAF, **agent identity** is the unique, durable identifier of an agent in the registry, distinct from every human user and every other agent. One identity may be evidenced by several credentials over time and at once, but every credential resolves to exactly one identity. The identity, bound to a versioned configuration, is the unit to which every control attaches. ([Source: Appendix A — Agent identity](../source/appendices/a-terminology.md#agent-identity).)

See the [Identity principle](principles/01-identity.md) for the principle page and the [complete source controls](../source/principles/01-identity.md) for its requirements.

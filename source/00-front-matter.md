[Source index](README.md) · [Next](01-purpose.md)

Source: [AAF.pdf, pages 1–2](../AAF.pdf#page=1), version 0.9.4 — Working Draft.

<!-- Source transcription begins. -->

# AGENT ACCOUNTABILITY

An open framework for the accountability of AI agents acting with delegated authority

| Field | Value |
| --- | --- |
| Version | 0.9.4 — Working Draft |
| Date | October 12, 2026 |
| Editor | Tim Tyler, Sr. PMM |
| Steward | Gravitee |
| License | Proposed: CC BY 4.0 |
| Feedback | tim.tyler@graviteesource.com |

## Status of This Document

This is a Working Draft in internal review, circulated to Gravitee employees and engaged consultants ahead of public release. It is not yet open for public review. Publication for community review will follow this internal cycle, and the draft is expected to change in response to review feedback and implementation experience.

This draft is numbered 0.9 by convention: version 1.0 is reserved for the first release that has incorporated review from parties outside the stewarding organization.

The framework is authored and stewarded by Gravitee and will be published as an open, vendor-neutral specification. It does not assume, require, or reference any specific vendor, product, or architecture. Gravitee’s intent is for stewardship of the framework to move to a multi-stakeholder governance process as adoption grows (see [Section 8](08-framework-governance.md)).

## Abstract

Organizations are deploying AI agents that act with delegated authority, whether or not that authority was ever explicitly defined: they access data, invoke tools, make decisions, and produce consequences, at machine speed and scale. Most governance regimes were designed for human workers or for static software, and neither fits an actor that exercises judgment at machine speed and is provisioned like a workload.

Agent Accountability is a framework for governing AI agents through structures of accountability that an organization can define, enforce, and assess. It defines six principles (Identity, Sponsor, Role, Authority, Oversight, and Recourse) ordered as an onboarding sequence. Each principle comprises a set of controls, and each control is specified in three parts: a normative Requirement, the Rationale behind it, and Assessment criteria describing the evidence that satisfies it. An organization conforms to the framework when, for every agent in production, each requirement is verifiably true. Conformance means the organization can answer on evidence, for any agent and any action, what acted, on whose authority, within what bounds, and how it can be stopped. It is a claim about accountability, not a claim that the organization is secure or that the models in use are safe ([Section 5](05-conformance-and-assessment.md)), and it is the basis on which an organization can extend what its agents are permitted to do. The principles are organized in three domains, Assign, Align, and Account, and each control is tagged by scope (whether it applies to every agent, to agents the organization operates, or to external agents acting on it). The framework assumes, and does not restate or assess, the general discipline of securing and operating information systems on which any system depends.

## Contents

- [1. Purpose](01-purpose.md)

- [2. Scope](02-scope.md)

- [3. Terminology](03-terminology.md)

- [4. The Framework Core: Principles and Controls](04-framework-core.md)

- [5. Conformance and Assessment [to be developed]](05-conformance-and-assessment.md)

- [6. Implementation Neutrality](06-implementation-neutrality.md)

- [7. Relationship to Existing Standards](07-relationship-to-standards.md)

- [8. Framework Governance [to be developed]](08-framework-governance.md)

- [Appendix A. Terminology](appendices/a-terminology.md)

- [Appendix B. Acknowledgments [to be developed]](appendices/b-acknowledgments.md)

<!-- Source transcription ends. -->

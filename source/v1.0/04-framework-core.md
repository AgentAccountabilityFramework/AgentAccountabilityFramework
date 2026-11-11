[Source index](README.md) · [Previous](03-terminology.md) · [Next](principles/01-identity.md)

Source: [AAF 1.0 PDF, page 5–7](AAF-1.0.pdf#page=5).

<!-- Source transcription begins. -->

# 4. The Framework Core: Principles and Controls

This section is the normative body of the framework, the Framework Core, comprising three domains, six principles, and the controls beneath them. Sections 1 to 3 and 5 to 8 are informative, with two exceptions that have normative effect: the definitions ([Appendix A](appendices/a-terminology.md)) fix the meaning of the terms the controls use, and the boundary rule ([Section 2](02-scope.md)) constrains how every control is read. Conformance is evaluated against this section.

The principles are ordered as a sequence that follows an agent’s admission to production: establish what it is (Identity), who answers for it (Sponsor), what it is to do (Role), what access it needs to do it (Authority), whether it is doing it (Oversight), and what happens when it is not (Recourse). Each principle builds on the one before it; a failure upstream invalidates verification downstream.

Each control is specified in three parts:

Requirement: the normative statement. Conformance is evaluated against the Requirement alone: for a given agent estate, an assessor can answer it yes or no.

Rationale: informative. Why the requirement exists as an industry requirement, independent of any implementation. Rationale guides interpretation where a Requirement meets a situation its authors did not foresee.

Assessment: informative in this draft. The pattern of evidence expected to satisfy the Requirement, written from the assessor’s point of view. [Section 5](05-conformance-and-assessment.md) will formalize assessment methodology; until then, Assessment text indicates the intended bar.

Controls follow a common progression within each principle: existence (the property is defined), enforcement (it is technically real, not just documented), and lifecycle (it survives organizational change). Throughout this document a bare number in parentheses, such as ([1.2](principles/01-identity.md#control-1-2)), cites a control; sections are cited as Section n. Where a Requirement contains several obligations, each is assessed and the control is met only when all are; a partly met control is not met, and the unmet obligation is recorded as the finding.

The six principles are organized in three domains, each named for what the organization does with the agent: Assign (Identity and Sponsor), Align (Role and Authority), and Account (Oversight and Recourse). Each domain answers a question the organization must be able to answer for any agent holding delegated authority, stated at the head of the domain. Each control carries a Scope tag, defined in [Appendix A](appendices/a-terminology.md), stating which agents it applies to: Generic, Internal, or External. Every control is satisfied from within the organization’s own boundary ([Section 2](02-scope.md), Boundary of management).

The framework assigns no risk tier to agents. An agent’s behavior is not fixed at deployment: the model behind it changes, the content it processes changes, and an agent that meets a barrier in its task will try other routes to complete it. An agent classified as low risk on the day it was deployed can become a high-consequence actor without any decision having been made. The framework instead rates consequence where it can be observed and bounded: at the level of action classes ([5.3](principles/05-oversight.md#control-5-3)) and of declared reach ([3.1](principles/03-role.md#control-3-1)). Every agent in the estate is subject to every control whose Scope tag includes it; an Internal control does not apply to an external agent, and the organization compensates at its boundary ([Section 2](02-scope.md), Boundary of management). The consequence rating and the reach determine how much oversight and how tight an authority the role requires, not whether the controls apply. Where an organization is subject to a regime that classifies systems by use case, it maps that classification onto action classes ([5.3](principles/05-oversight.md#control-5-3)) and declared reach ([3.1](principles/03-role.md#control-3-1)) and records the mapping. The framework does not assume that an agent will behave as a person would; the risk posture exists because it will not.

<!-- Source transcription ends. -->

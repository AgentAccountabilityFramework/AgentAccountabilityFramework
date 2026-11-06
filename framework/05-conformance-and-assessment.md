# Conformance and Assessment

[Framework contents](README.md) · [Previous: Recourse](principles/06-recourse.md) · [Next: Implementation Neutrality](06-implementation-neutrality.md)

Source: Section 5: Conformance and Assessment.

The source marks this section as “to be developed”; the positions below are part of the internal working document.

Section 5 explains what a conformance claim covers and what evidence you need. It gives guidance, rather than adding control requirements. It leaves the formal assessment method and conformance keywords undefined. Use each control's Requirement to decide whether it is met (Section 4).

Conformance means your organization's agents meet the accountability requirements you claim to meet. The claim covers your **agent estate**: all agents operating in or on behalf of your organization. You provide evidence for each agent.

## What the claim covers

Every agent in production must be covered. Checking only a selected group of agents does not establish conformance.

You can adopt the framework in stages by claiming a clearly stated subset of controls, provided that subset covers every agent in the estate. The Scope tags and boundary rule still determine how each control applies.

A finding against one agent is a finding against the estate, unless it is recorded as a declared exception with a remediation window. Record the exception and the time allowed to address it; an exception does not make a failed control pass. Each obligation in a control's Requirement must be met for that control to pass (Section 4).

## What to publish

Your conformance statement must publish every parameter the framework leaves to your organization. This includes each defined window, cadence, period, threshold, and tolerance.

Share confidence thresholds only with people who need to know them (Control 3.3).

Where the framework sets a minimum, your chosen parameter must meet it. For example, Control 6.1 requires suspension in seconds. For an agent whose runtime you do not control, that means revoking its credentials, sessions, and authority at your boundary within the same window.

## What the evidence must show

Evidence must show that a requirement works in practice and continues to be met through change. A written policy or declaration alone is not enough.

When an assessment uses a sample, state its size, how it was selected, and the confidence it supports. A universal claim, such as a statement that every agent is registered, also needs reconciliation against independent sources. A sample alone cannot support it.

The Requirement is the basis for deciding whether a control is met. Rationale explains why the requirement exists, and Assessment describes the evidence an assessor expects to see; both are guidance (Section 4).

## What conformance establishes

An AAF conformance claim establishes agent accountability as the framework defines it. It does not establish that the organization is secure or that its models are safe or aligned. Those subjects remain outside the framework's scope.

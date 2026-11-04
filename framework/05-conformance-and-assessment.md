# Conformance and Assessment

[Framework contents](README.md) · [Previous: Recourse](principles/06-recourse.md) · [Next: Implementation Neutrality](06-implementation-neutrality.md)

Source: [Section 5: Conformance and Assessment](../source/05-conformance-and-assessment.md#5-conformance-and-assessment).

This page explains the conformance positions in Section 5, which is informative. The source does not define formal conformance keywords or an assessment methodology, or establish a certification scheme. Control Requirements remain the basis for conformance ([Section 4](../source/04-framework-core.md#4-the-framework-core-principles-and-controls)).

Conformance means your organization's agents meet the accountability requirements you claim to meet. The claim covers your **agent estate**: all agents operating in or on behalf of your organization. You provide evidence for each agent.

## What the claim covers

Every agent in production must be covered. Checking only a selected group of agents does not establish conformance.

You can adopt the framework in stages by claiming a clearly stated subset of controls, provided that subset covers every agent in the estate. The [Scope tags and boundary rule](../source/04-framework-core.md#4-the-framework-core-principles-and-controls) still determine how each control applies.

A finding against one agent is a finding against the estate, unless it is recorded as a declared exception with a remediation window. Record the exception and the time allowed to address it; an exception does not make a failed control pass. Each obligation in a control's Requirement must be met for that control to pass ([Section 4](../source/04-framework-core.md#4-the-framework-core-principles-and-controls)).

## What to publish

Your conformance statement must publish every parameter the framework leaves to your organization. This includes each defined window, cadence, period, threshold, and tolerance.

[Control 3.3](../source/principles/03-role.md#control-3-3) limits disclosure of confidence thresholds to parties with a need to know. The source does not specify how that limit applies to publication in a conformance statement ([Section 5](../source/05-conformance-and-assessment.md#5-conformance-and-assessment)); see the [gap log](../SOURCE_GAPS.md#g2-confidence-thresholds-in-conformance-statements).

Where the framework sets a minimum, your chosen parameter must meet it. For example, [Control 6.1](../source/principles/06-recourse.md#control-6-1) requires suspension in seconds. For an agent whose runtime you do not control, that means revoking its credentials, sessions, and authority at your boundary within the same window.

## What the evidence must show

Evidence must show that a requirement works in practice and continues to be met through change. A written policy or declaration alone is not enough.

When an assessment uses a sample, state its size, how it was selected, and the confidence it supports. A universal claim, such as a statement that every agent is registered, also needs reconciliation against independent sources. A sample alone cannot support it.

The Requirement is the basis for deciding whether a control is met. Rationale explains why the requirement exists, and Assessment describes the evidence an assessor expects to see; both are guidance ([Section 4](../source/04-framework-core.md#4-the-framework-core-principles-and-controls)).

## What conformance establishes

An AAF conformance claim establishes agent accountability as the framework defines it. It does not establish that the organization is secure or that its models are safe or aligned. Those subjects remain outside the framework's [scope](../source/02-scope.md#2-scope).

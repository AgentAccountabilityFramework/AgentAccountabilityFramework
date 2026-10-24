[Source index](README.md) · [Previous](06-implementation-neutrality.md) · [Next](08-framework-governance.md)

Source: [AAF.pdf, page 34](../AAF.pdf#page=34), version 0.9.4 — Working Draft.

<!-- Source transcription begins. -->

# 7. Relationship to Existing Standards

This framework defines what accountable agent operation means; existing and emerging standards supply many of the mechanisms by which its requirements can be met. The intent is complement, not competition, and the framework deliberately names no mechanism in its controls so that conformance remains open to any architecture that satisfies the requirements.

Work directly adjacent to this framework is under way across the standards community, including agent identity and authorization work at NIST’s National Cybersecurity Center of Excellence, identity and delegation standards from the OpenID Foundation and the FIDO Alliance, agentic-AI governance guidance such as the NIST AI RMF and ISO/IEC 42001, security guidance from OWASP for LLM and agentic applications, and sector frameworks such as FDX. Runtime governance patterns emerging in regulated industries address the same properties this framework requires in its Oversight and Recourse principles.

Delegation semantics are an area of active development across these bodies: dynamic on-behalf-of authority, the distinction between delegation and impersonation, and how a relying party verifies the authority an agent claims. This framework takes no position on those mechanisms. It requires the properties, delegation that is explicit, bounded, and verifiable (controls [4.3](principles/04-authority.md#control-4-3) and [4.6](principles/04-authority.md#control-4-6)), and looks to the standards community to supply the means.

<!-- Source transcription ends. -->

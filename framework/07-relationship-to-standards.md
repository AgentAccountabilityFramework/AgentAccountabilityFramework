# Relationship to Existing Standards

[Framework contents](README.md) · [Previous: Implementation Neutrality](06-implementation-neutrality.md) · [Next: Framework Governance](08-framework-governance.md)

Source: [Section 7: Relationship to Existing Standards](../source/07-relationship-to-standards.md#7-relationship-to-existing-standards).

The AAF defines the outcomes your organization must demonstrate to operate accountable agents. Other standards and guidance can help you choose how to meet those requirements. The controls leave that choice open to any implementation that satisfies them.

## Related work

Section 7 identifies several areas of related work. The links below lead to the organizations responsible for them.

| Area | Related work | What it addresses |
| --- | --- | --- |
| Agent identity and authorization | [NIST National Cybersecurity Center of Excellence](https://www.nccoe.nist.gov/projects/software-and-si-agent-identity-and-authorization) | Identifying software agents, managing their identities, and authorizing their access. |
| Identity and delegation | [OpenID Foundation](https://openid.net/new-whitepaper-tackles-ai-agent-identity-challenges/) and [FIDO Alliance](https://fidoalliance.org/fido-alliance-agentic-ai/) | Authentication, authorization, and delegated authority for agents acting on behalf of people. |
| AI risk and organizational governance | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [ISO/IEC 42001](https://www.iso.org/standard/42001) | Managing AI risks and establishing an organizational AI management system. |
| Application security | [OWASP GenAI Security Project](https://genai.owasp.org/) | Security guidance for applications using large language models and agents. |
| Financial data sharing | [Financial Data Exchange](https://financialdataexchange.org/about-fdx/faqs/) | Standards for sharing financial data with the user's permission. |

These resources address different parts of the problem. Using one does not by itself establish AAF conformance; you still need evidence that your agents meet the controls you claim to meet ([Section 5](../source/05-conformance-and-assessment.md#5-conformance-and-assessment)).

Section 7 also points to runtime governance practices in regulated industries that address the properties covered by [Oversight](../source/principles/05-oversight.md#principle-5-oversight) and [Recourse](../source/principles/06-recourse.md#principle-6-recourse).

## Delegation in practice

When an agent acts for someone else, the party receiving its request needs to verify who authorized it and what that authorization permits. Under [Control 4.3](../source/principles/04-authority.md#control-4-3), the delegation must be explicit, attributable, bounded, and verifiable. The agent's effective authority cannot exceed either its own authority or the delegating principal's, and further delegation cannot add privileges.

For example, an agent with permission to update customer records cannot use that permission on behalf of a person who may only read them. A request written in a document or tool response cannot grant extra authority either: [Control 4.6](../source/principles/04-authority.md#control-4-6) requires an explicit, authenticated grant or delegation.

The AAF requires those properties without choosing a delegation protocol. Section 7 looks to the standards community to provide ways to implement them.

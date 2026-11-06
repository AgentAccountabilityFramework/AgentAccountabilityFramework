# Agent Accountability Framework

The internal AAF source has been withdrawn from version control pending public AAF 1.0. Source links are suspended; existing derived content remains a working draft and has not been validated against 1.0. See the source link restoration record (maintained locally).
The current AAF is an internal working document under review, ahead of public release (document status). Assessment methodology, framework governance, acknowledgments, and licensing remain unresolved.

The Agent Accountability Framework (AAF) helps your organization establish who each AI agent is, who answers for it, what it may do, and how to stop it. It turns those questions into requirements you can test. You choose how to meet them (Purpose, Implementation Neutrality).

[Framework contents](framework/README.md) · Markdown source · [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

## What the framework covers

The AAF covers agents acting in or on behalf of an organization with delegated authority to access information or take actions, including internal, external, and spawned agents. Controls are satisfied within the organization's own boundary. Model safety, general AI ethics, and the general operation and security of information systems are outside its scope (Section 2).

The framework organizes its six principles into three domains (Section 4):

- **Assign:** Identity lets you identify each agent; Sponsor names the human who answers for it.
- **Align:** Role defines the agent's job; Authority sets limits on what it can access and do.
- **Account:** Oversight lets you see what the agent does and whether it is doing its job; Recourse gives you ways to stop it, address the effects, and decide whether it can return.

The full controls, their scope, and the boundary rule determine how these principles apply. The summaries above are a starting point, not a substitute for the source.

## Read the framework

Start with the [framework reading order](framework/README.md), which includes all six principle pages and their controls. The AAF source is the authoring reference; the [coverage map](maintenance/source-coverage.md) shows how each page relates to it.

- [Purpose](framework/01-purpose.md)
- [Scope](framework/02-scope.md)
- [Terminology conventions](framework/03-terminology.md)
- [Framework core: principles and controls](framework/04-framework-core.md)
- [Conformance and assessment](framework/05-conformance-and-assessment.md)
- [Implementation neutrality](framework/06-implementation-neutrality.md)
- [Relationship to existing standards](framework/07-relationship-to-standards.md)
- [Framework governance](framework/08-framework-governance.md)
- [Appendix A: terminology](framework/appendices/a-terminology.md)
- [Appendix B: acknowledgments](framework/appendices/b-acknowledgments.md)

## Contribute

For general questions or to contact the AAF team, email [admin@agentaccountabilityframework.org](mailto:admin@agentaccountabilityframework.org). You can also use this address to report conduct concerns privately; see the [Code of Conduct](CODE_OF_CONDUCT.md#reporting-a-concern).

- [Contribution guide](CONTRIBUTING.md)
- [Proposing changes](contributing/proposing-changes.md)
- [Editorial guide](contributing/editorial-guide.md)
- [AI-assisted contributions](contributing/ai-assisted-contributions.md)
- [Code of conduct](CODE_OF_CONDUCT.md)

## Repository and maintenance

- [Repository layout](REPOSITORY_LAYOUT.md)
- [Repository governance](GOVERNANCE.md)
- [Repository instructions](AGENTS.md)
- [Changelog](CHANGELOG.md)
- [Source coverage](maintenance/source-coverage.md)
- [Documentation checks](maintenance/checks.md)
- [Release procedures](maintenance/releases.md)
- [Moderation](maintenance/moderation.md)
- [Licensing decision](LICENSE)

# Agent Accountability Framework

This repository accompanies [Agent Accountability Framework 1.0](source/v1.0/AAF-1.0.pdf). The framework is licensed under [CC BY-SA 4.0](LICENSE).

The Agent Accountability Framework (AAF) helps your organization establish who each AI agent is, who answers for it, what it may do, and how to stop it. It turns those questions into requirements you can test. You choose how to meet them ([Purpose](source/v1.0/01-purpose.md#1-purpose), [Implementation Neutrality](source/v1.0/06-implementation-neutrality.md#6-implementation-neutrality)).

[Framework contents](framework/README.md) · [Control index](source/v1.0/README.md#control-index) · [Markdown source](source/v1.0/README.md) · [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

## What the framework covers

The AAF covers agents acting in or on behalf of an organization with delegated authority to access information or take actions, including internal, external, and spawned agents. Controls are satisfied within the organization's own boundary. Model safety, general AI ethics, and the general operation and security of information systems are outside its scope ([Section 2](source/v1.0/02-scope.md)).

The framework organizes its six principles into three domains ([Section 4](source/v1.0/04-framework-core.md)):

- **Assign:** [Identity](source/v1.0/principles/01-identity.md#principle-1-identity) lets you identify each agent; [Sponsor](source/v1.0/principles/02-sponsor.md#principle-2-sponsor) names the human who answers for it.
- **Align:** [Role](source/v1.0/principles/03-role.md#principle-3-role) defines the agent's job; [Authority](source/v1.0/principles/04-authority.md#principle-4-authority) sets limits on what it can access and do.
- **Account:** [Oversight](source/v1.0/principles/05-oversight.md#principle-5-oversight) lets you see what the agent does and whether it is doing its job; [Recourse](source/v1.0/principles/06-recourse.md#principle-6-recourse) gives you ways to stop it, address the effects, and decide whether it can return.

The full controls, their scope, and the boundary rule determine how these principles apply. The summaries above are a starting point, not a substitute for the source.

## Read the framework

Start with the [framework reading order](framework/README.md), which includes all six principle pages and their controls. The [AAF source](source/v1.0/README.md) is the authoring reference; the [coverage map](maintenance/source-coverage.md) shows how each page relates to it.

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
- [License](LICENSE)

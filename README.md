# Agent Accountability Framework

The Agent Accountability Framework (AAF) describes how organizations can hold AI agents accountable when they act with delegated authority. It is vendor-neutral and describes outcomes without prescribing how to implement them ([purpose](source/01-purpose.md), [implementation neutrality](source/06-implementation-neutrality.md)).

[Framework contents](framework/README.md) · [Markdown source](source/README.md) · [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

## What the framework covers

The AAF covers agents acting in or on behalf of an organization, including internal, external, and spawned agents. Controls are satisfied within the organization's own boundary. Model safety, general AI ethics, and the general operation and security of information systems are outside its scope ([Section 2](source/02-scope.md)).

The framework organizes its six principles into three domains ([Section 4](source/04-framework-core.md)):

- **Assign:** [Identity](source/principles/01-identity.md#principle-1-identity) establishes the agent as a distinguishable actor; [Sponsor](source/principles/02-sponsor.md#principle-2-sponsor) establishes human accountability.
- **Align:** [Role](source/principles/03-role.md#principle-3-role) defines what the agent is meant to do; [Authority](source/principles/04-authority.md#principle-4-authority) defines the information and actions available to it.
- **Account:** [Oversight](source/principles/05-oversight.md#principle-5-oversight) makes the agent's actions and performance observable; [Recourse](source/principles/06-recourse.md#principle-6-recourse) provides for stopping, containment, escalation, and reinstatement.

The full controls, their scope, and the boundary rule determine how these principles apply. The summaries above are a starting point, not a substitute for the source.

## Read the framework

Read the complete [AAF source](source/README.md). The [source coverage map](maintenance/source-coverage.md) records the content available in each repository page.

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
- [Release procedures](maintenance/releases.md)
- [Moderation](maintenance/moderation.md)
- [License](LICENSE)

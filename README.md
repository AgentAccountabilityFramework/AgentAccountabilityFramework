# Agent Accountability Framework
The Agent Accountability Framework (AAF) is an open framework for the accountability of AI agents acting with delegated authority.

[Framework contents](framework/README.md) · [Markdown source](source/README.md) · [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

## Why do we need an accountability framework?

Organizations are adopting AI agents at a rapid pace. According to [McKinsey's 2026 State of AI report](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai), 40% of large enterprises are now scaling AI agents, up from 27% the previous year. Unlike traditional AI assistants, these agents can access and modify data, interact with applications, execute complex workflows, and make decisions with limited or no human intervention. As [McKinsey explains](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/deploying-agentic-ai-with-safety-and-security-a-playbook-for-technology-leaders), this represents a fundamental shift from systems that provide information to systems that take actions with real business consequences.

But this rapid adoption is exposing a critical weakness: **AI agents are not consistently reliable, and their mistakes can have consequences far beyond an incorrect answer.** Agents can misinterpret instructions, expose sensitive information, modify or destroy data, and trigger unintended actions, costing organizations time, money, and credibility. These risks are not hypothetical. In 2025, [a Replit AI coding agent deleted a live production database despite explicit instructions not to make changes](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/). Meanwhile, [Deloitte's 2026 research](https://www.deloitte.com/us/en/insights/topics/emerging-technologies/ai-agents-scaling-faster.html) found that only 21% of surveyed organizations had mature governance models for agentic AI.

The challenge is no longer simply getting agents to perform useful work. It's ensuring they can do so reliably, safely, and with clear accountability when something goes wrong.

## The AAF, summarized

The AAF is an open, vendor-neutral specification for governing AI agents through structures of accountability that an organization can define, enforce, and assess. It is here to give your organization a common, testable definition of what it means for an AI agent to be held accountable. It is written for the people who must answer for AI agents in production.

The AAF defines six principles organized into three domains ([source, Section 4](source/04-framework-core.md)):

### Assign

*Who is this, and who answers for it?*

**[Identity](framework/principles/01-identity.md)** (*Who are you?*)

- Every agent must have a unique, verifiable identity that distinguishes it from human users and other agents.
- Its credentials must be tied to that identity, and the agent must be recorded in an authoritative registry.
- Every action must be attributable to the specific agent responsible (including agents created by other agents or operated by third parties).

**[Sponsor](framework/principles/02-sponsor.md)** (*Who is responsible for you?*)

- Every agent must have a named human sponsor who is accountable for its existence, purpose, authority, and actions.
- Accountability must remain continuous throughout the agent's lifecycle (again, including agents of other agents or third-party agents).

### Align

*What is it for, and what may it do?*

**[Role](framework/principles/03-role.md)** (*What are you here for?*)

- Every agent must have a documented role defining its purpose, expected outcomes, measurable success criteria, budget, autonomy level, and operational boundaries.

**[Authority](framework/principles/04-authority.md)** (*What can you see, and what can you do?*)

- Every agent must operate within explicitly defined and enforcable limits on the information it can access and the actions it can perform.
- Authority derives from its assigned role and is granted through verifiable delegation.
- Authority is time-limited and revocable.
- Agents can not expand their own authority or obtain additional permissions.

### Account

*Is it doing what we expect, and what happens when it isn’t?*

**[Oversight](framework/principles/05-oversight.md)** (*Are you doing what we expect?*)

- Every agent action must be recorded and evaluated against its role, authority, and expectations.
- Oversight must identify deviations, assess consequences, and measure if the agent is achieving its intended outcomes.
- Records must be available for independent review.
- Expected behavior must be re-evaluated whenever the agen'ts role, model, or underlying systems change.

**[Recourse](framework/principles/06-recourse.md)** (*What happens if something goes wrong?*)

- Agents must be able to be immediately suspended, contained, or have actions reversed.
- Agents must respond to all failures through predefined escalation procedures.
- Agents must not resume operations without an explicit reinstatement decision.
- Decommissioning agents must fully terminate their authority.
- Recourse mechanisms apply to both individual agents and entire classes of agents, accounting for dependencies between them.

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

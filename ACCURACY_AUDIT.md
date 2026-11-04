# AAF technical accuracy and source fidelity audit

Audit date: November 3, 2026. Repository: `repo/`, at baseline commit `f580c31`, with corrections reviewed and committed separately. The approved findings were re-read to remove flags based only on possible reader questions. The working tree was clean at the start. This is an audit of technical meaning and source fidelity, not a writing review or an assessment of an agent deployment.

## 1. Audit coverage

### Source of truth and hierarchy

All 18 files in `source/` were read: the index and all 17 transcribed sections, principle pages, and appendices. They represent one baseline, identified in the source as **0.9.4 — Working Draft**, dated **October 12, 2026**. There are no competing versions inside `source/`. Version and status are recorded here because this audit must identify the evidence precisely; the repository's convention for omitting them does not establish a release or supersede the source.

The hierarchy is explicit in [Section 4](source/04-framework-core.md#4-the-framework-core-principles-and-controls), lines 9–25:

- The Framework Core is normative. Conformance is evaluated against each control's **Requirement**, and every obligation in that Requirement must be met.
- **Rationale** and **Assessment** are informative. An Assessment describes intended evidence; it cannot silently add an obligation to, or remove an exception from, a Requirement.
- Appendix A definitions and the Section 2 boundary rule have normative effect. All controls are read within the organization's management boundary.
- Sections 1–3 and 5–8 are informative apart from that boundary rule. Section 5 does not supply a formal assessment methodology or formal conformance keywords.
- The source index, navigation, source links, page comments, and anchors are editorial aids, distinguished from the transcription in [source/README.md](source/README.md#transcription-and-provenance).

That hierarchy does not resolve every conflict between normative passages, or establish the intended correction to inconsistent informative evidence. Those issues remain explicit in Section 3 of this audit.

| Source document | Purpose and authority | Source location |
| --- | --- | --- |
| [source/README.md](source/README.md) | Editorial reading order, control index, provenance, and transcription conventions; identifies the authoring baseline. | Entire file; How to use this source; Transcription and provenance. |
| [source/00-front-matter.md](source/00-front-matter.md#agent-accountability) | Metadata, internal-review status, proposed license, attribution, abstract, and contents. The abstract summarizes accountability and conformance. | Lines 7–54; original pages 1–2. |
| [source/01-purpose.md](source/01-purpose.md#1-purpose) | Purpose, audience, accountable-agent outcomes, and implementation choice. Informative. | Lines 9–13; pages 2–3. |
| [source/02-scope.md](source/02-scope.md#2-scope) | Included agents, exclusions, and the boundary of management. The boundary rule has normative effect. | Lines 9–17; pages 3–4. |
| [source/03-terminology.md](source/03-terminology.md#3-terminology) | Directs normative terminology to Appendix A; leaves formal conformance keywords to Section 5. | Line 9; page 4. |
| [source/04-framework-core.md](source/04-framework-core.md#4-the-framework-core-principles-and-controls) | Normative structure, sequence, field status, scope tags, consequence/reach, and domain relationships. | Lines 9–25; pages 4–5. |
| [source/principles/01-identity.md](source/principles/01-identity.md#principle-1-identity) | Assign domain; Identity; controls 1.1–1.5. | Lines 7–115; pages 6–9. |
| [source/principles/02-sponsor.md](source/principles/02-sponsor.md#principle-2-sponsor) | Sponsor; controls 2.1–2.5; sponsor/admitting-authority/operator distinctions and spawned-agent sponsorship. | Lines 7–111; pages 9–12. |
| [source/principles/03-role.md](source/principles/03-role.md#principle-3-role) | Align domain; Role; controls 3.1–3.8; purpose, rules/intents, reach, change, budgets, autonomy, and dependencies. | Lines 7–175; pages 13–17. |
| [source/principles/04-authority.md](source/principles/04-authority.md#principle-4-authority) | Authority; controls 4.1–4.14; data/actions, delegation, enforcement, intent, egress, isolation, and spawning limits. | Lines 7–291; pages 17–25. |
| [source/principles/05-oversight.md](source/principles/05-oversight.md#principle-5-oversight) | Account domain; Oversight; controls 5.1–5.8; records, deviations, disposition, evaluation, testing, and reconciliation. | Lines 7–175; pages 26–30. |
| [source/principles/06-recourse.md](source/principles/06-recourse.md#principle-6-recourse) | Recourse; controls 6.1–6.5; suspension, containment, escalation, reinstatement, and retirement. | Lines 7–111; pages 30–33. |
| [source/05-conformance-and-assessment.md](source/05-conformance-and-assessment.md#5-conformance-and-assessment) | Informative conformance positions: estate coverage, control subsets, exceptions, parameters, evidence, and limits. Explicitly unfinished. | Line 9; pages 33–34. |
| [source/06-implementation-neutrality.md](source/06-implementation-neutrality.md#6-implementation-neutrality) | Required properties do not prescribe products or implementation mechanisms. Informative. | Lines 9–11; page 34. |
| [source/07-relationship-to-standards.md](source/07-relationship-to-standards.md#7-relationship-to-existing-standards) | Related work and mechanism-neutral delegation properties; no equivalence or certification mapping. Informative. | Lines 9–13; page 34. |
| [source/08-framework-governance.md](source/08-framework-governance.md#8-framework-governance) | Current Gravitee stewardship and intended future governance. Processes and decision rights are unfinished. | Line 9; pages 34–35. |
| [source/appendices/a-terminology.md](source/appendices/a-terminology.md#appendix-a-terminology) | All 37 definitions have normative effect; fixes distinctions used by the controls. | Lines 9–157; pages 36–42. |
| [source/appendices/b-acknowledgments.md](source/appendices/b-acknowledgments.md#appendix-b-acknowledgments) | Placeholder for reviewers and contributors; names none. | Line 9; page 42. |

The local provenance PDF is readable and its SHA-256 matches the source index: `a73b5b9ce3979d493bdff3354d2d67efcfac94171845effceeb809c7912810b7`. Its metadata identifies the same baseline and 42 physical pages. Extraction produced the recorded 17,756 whitespace-separated tokens. Targeted PDF checks confirmed the operator, delegation, threshold, timing, and retirement wording, including the operator exception on page 12, delegation Assessment on page 19, spawned-agent Assessment on page 25, threshold disclosure on page 14, and Section 5 and decommissioning on page 33. Those passages are in the original document; that alone does not make them errors. This audit did not repeat a complete token-by-token transcription proof for all PDF pages; `source/` remains the authoritative comparison material.

### Reader-facing files reviewed

Every existing reader-facing Markdown file outside `source/` was reviewed, as was `LICENSE`: 37 Markdown files plus the licensing note. Complete control and definition bodies were compared after resolving relative links to their actual targets and removing presentation-only editorial aids. Introductions, summaries, tables, examples, and guidance were separately read for meaning. A comparison pass alone was not treated as a prose accuracy review.

In the table, **faithful** means supported as a source summary or reproduction, subject to the expressly listed source issues; it does not mean internally consistent source text has been established. **Repository guidance** means a local contribution or maintenance convention, not an AAF deployment requirement. **Limited** identifies claims the supplied source cannot settle.

| Reviewed file | Source documents used | Result |
| --- | --- | --- |
| [README.md](README.md) | Sections 1, 2, 4, 6; all six source principle introductions. | Corrected scope qualification (C1); domain/principle summaries otherwise faithful. |
| [AGENTS.md](AGENTS.md) | Source index; front matter; Sections 2–6, 8; Appendix A. | Framework-fidelity instructions faithful; final-for-authoring convention is explicit and is not a framework defect. Commit and attribution instructions are repository conventions, not AAF rules. |
| [CHANGELOG.md](CHANGELOG.md) | All source sections cited in its entries; local Git history for repository events. | Technical descriptions reviewed; two grouped citations corrected (C4). Historical statements retained as history, not current file status. Prior validation runs not independently replayed (U11). |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Section 8 as the boundary between framework governance and local practices. | Repository guidance, not AAF controls; no invented named reporting contact. Actual operational arrangements not established by source. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Source index; Section 4; Section 8; front-matter license/status. | Source-change and derived-edit distinctions faithful. Repository contribution process is local; public issue/PR status unverified (U11). |
| [GOVERNANCE.md](GOVERNANCE.md) | Section 8; source index. | Correctly separates repository permissions from framework decision rights. Actual permissions are outside source evidence. |
| [LICENSE](LICENSE) | Front matter, line 17; source index. | Faithfully avoids treating the proposed license as a grant. No legal determination or off-repository licensing agreement was audited. |
| [REPOSITORY_LAYOUT.md](REPOSITORY_LAYOUT.md) | Source index; all source headings and control ranges; Section 5; Appendix A. | File inventory and mappings reviewed against the tree. Conformance-page description qualified (C2). |
| [TODO.md](TODO.md) | Sections 5, 7, 8; front matter; Appendix B. | Accurately identifies unsettled project decisions and absence of a formal assessment/certification method. Local project tasks are not framework controls. |
| [assets/README.md](assets/README.md) | Section 4; source index. | Repository asset guidance only. No substantive image or diagram is present in `assets/`. |
| [contributing/ai-assisted-contributions.md](contributing/ai-assisted-contributions.md) | Source index; Section 4. | Repository guidance; no claim that AAF mandates AI-use or contribution policies. |
| [contributing/editorial-guide.md](contributing/editorial-guide.md) | Sections 2, 4, 6; Appendix A; control 5.1 for the recording example. | Preserves obligation strength and distinguishes illustrative wording from complete requirements. |
| [contributing/proposing-changes.md](contributing/proposing-changes.md) | Source index; Section 4. | Normative/informative distinction faithful; proposals clearly separated from existing rules. |
| [framework/README.md](framework/README.md) | Source contents; Section 4; all principles; Appendix A and B. | Reading order, three domains, six principles, and 37-definition count verified. Audit link added. |
| [framework/01-purpose.md](framework/01-purpose.md) | Section 1; all principle introductions; Section 6. | Faithful purpose, audience, outcomes, and implementation choice. |
| [framework/02-scope.md](framework/02-scope.md) | Section 2; Section 4; Appendix A; controls 1.1, 1.3, 1.4, 2.1, 2.5, 3.1, 3.8, 4.1, 4.6, 4.8, 5.1, 6.1. | Faithful scope and boundary explanation. Operator-of-record summary inherits source tension U2. |
| [framework/03-terminology.md](framework/03-terminology.md) | Abstract; Sections 3–4; Appendix A definitions of Principle, Registry, Credential, Agent identity. | Six introductory explanations are clearly distinguished from formal definitions. No new formal terms imposed. |
| [framework/04-framework-core.md](framework/04-framework-core.md) | Section 4; Section 2 boundary; domain introductions; Appendix A. | Domain mapping, upstream sequence, normative effect, control fields, applicability, and consequence/reach faithful; see U2 for the operator tag wording; U7 still awaits review. |
| [framework/principles/01-identity.md](framework/principles/01-identity.md) | Complete source Identity page; linked controls; Appendix A identity/configuration/credential definitions; boundary rule. | All five complete controls match; introduction faithful. Identity/instance question U8. |
| [framework/principles/02-sponsor.md](framework/principles/02-sponsor.md) | Complete source Sponsor page; linked controls; Appendix A Sponsor, Admitting authority, Operator of record; boundary rule. | All five controls match; introduction faithful. Operator scope and exception issue U2. |
| [framework/principles/03-role.md](framework/principles/03-role.md) | Complete source Role page; linked controls; Appendix A Role, Rule, Intent, Reach, Budget, Autonomy level, Change event, Dependency. | All eight controls match; introduction faithful. |
| [framework/principles/04-authority.md](framework/principles/04-authority.md) | Complete source Authority page; linked controls; Appendix A definitions; boundary rule and Section 6. | All 14 controls match; introduction preserves conditional intent evaluation. Delegation Assessment wording is covered in U4. |
| [framework/principles/05-oversight.md](framework/principles/05-oversight.md) | Complete source Oversight page; linked controls; Appendix A Action class, Disposition, Intent, Scope tag; Section 5. | All eight controls match; introduction faithful. Evidence qualifications are discussed in Section 4 below. |
| [framework/principles/06-recourse.md](framework/principles/06-recourse.md) | Complete source Recourse page; linked controls; Section 2; Appendix A Class, Recourse, Severity-1 event, Decommissioning. | All five controls match; introduction faithful. Transfer/destruction issue U10. |
| [framework/05-conformance-and-assessment.md](framework/05-conformance-and-assessment.md) | Sections 2–5; controls 3.3 and 6.1; Appendix A Estate. | Added the missing assessment-method explanation (C2). Kept the confidence-threshold disclosure limit without flagging a conflict; U9 remains for review. |
| [framework/06-implementation-neutrality.md](framework/06-implementation-neutrality.md) | Section 6; control 1.2; Appendix A Registry, Enforcement layer, Containment boundary. | Faithful; registry example does not prescribe technology or claim to replace the complete controls. |
| [framework/07-relationship-to-standards.md](framework/07-relationship-to-standards.md) | Section 7; Section 5; controls 4.3 and 4.6; seven linked primary pages. | Related-work descriptions verified; authenticated-delegation qualification restored (C3). No equivalence or required protocol asserted. |
| [framework/08-framework-governance.md](framework/08-framework-governance.md) | Section 8; front matter. | Current steward and intended direction faithful; no receiving body, transfer mechanism, or decision rights invented. |
| [framework/appendices/a-terminology.md](framework/appendices/a-terminology.md) | Entire source Appendix A and its linked controls/sections. | All 37 definitions match, including order and links. Candidates U7–U10 still await review. |
| [framework/appendices/b-acknowledgments.md](framework/appendices/b-acknowledgments.md) | Appendix B; front matter, lines 15–16. | Editor and steward attribution supported; does not invent additional reviewers. Contribution route is repository guidance. |
| [maintenance/checks.md](maintenance/checks.md) | Section 4; source control inventory; Appendix A; source provenance. | Counts and limits verified against actual checker and tests. Correctly disclaims prose accuracy and conformance verification. |
| [maintenance/moderation.md](maintenance/moderation.md) | Section 8 as governance boundary. | Repository guidance only; does not confer roles or promise outcomes. Operational arrangements unverified. |
| [maintenance/releases.md](maintenance/releases.md) | Source index; Section 8; front matter. | Repository release guidance correctly leaves authority, licensing, versioning, and publication decisions to the project. |
| [maintenance/source-coverage.md](maintenance/source-coverage.md) | All 18 source files; actual derived pages; targeted provenance checks. | Section/control/term mappings reviewed; added audit limitations and updated Section 5 coverage (C2). Historical transcription-proof claim not independently reproduced in full (U11). |
| [.github/ISSUE_TEMPLATE/documentation.md](.github/ISSUE_TEMPLATE/documentation.md) | Source index and Section 4. | Local correction-report template; no added AAF requirement. |
| [.github/ISSUE_TEMPLATE/proposal.md](.github/ISSUE_TEMPLATE/proposal.md) | Sections 2 and 4; source index. | Preserves boundary impacts and distinction between proposals and current obligations. |
| [.github/ISSUE_TEMPLATE/question.md](.github/ISSUE_TEMPLATE/question.md) | Source index. | Local question template; no technical framework claim beyond locating a passage. |
| [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) | Source index; Section 4. | Correctly distinguishes editorial, transcription, and framework changes; validation instructions checked locally. |

### Supporting files, website scope, and verification limits

Five additional tracked files were inspected to verify reader-facing claims about repository operation:

| File | Review and limitation |
| --- | --- |
| [.gitignore](.gitignore) | Confirms PDFs and Python bytecode are excluded; no AAF rule content. |
| [.github/CODEOWNERS](.github/CODEOWNERS) | Contains comments awaiting confirmed reviewers, not active assignments. Section 8 does not establish repository ownership. |
| [.github/workflows/check-docs.yml](.github/workflows/check-docs.yml) | Locally confirms triggers and commands described in the checks guide. No hosted run, action-pin provenance, or repository settings audit was performed. |
| [scripts/check-docs.py](scripts/check-docs.py) | Read to verify documented checking capabilities and limits; executed. Checks literal source fidelity and local links, not semantic correctness of summaries. No logic changed. |
| [scripts/test_check_docs.py](scripts/test_check_docs.py) | Read and executed all nine tests. Deliberately incorrect temporary fixtures are test inputs, not published AAF examples. No logic changed. |

This accounts for all 61 pre-audit tracked files: 18 source files, 38 reader-facing documents, and five supporting files. The audit itself is a new file.

There is **no website implementation, HTML page, frontend copy, diagram file, image, schema, or separate implementation-example directory inside this Git repository**. No such artifact is marked verified. The sibling `mockup/`, `AAF-visual-preview.html`, proposal folders, media, branding, and older PDFs in the surrounding workspace are outside this repository and were not audited. No hosted AAF site or GitHub-rendered deployment was supplied or checked. If those sibling artifacts are intended for publication with this repository, they require their own source comparison; this report does not cover them.

No file in `source/` was unreadable. Remaining limits are interpretive conflicts, source omissions, historical validation claims, and off-repository operational facts—not missing access to the Markdown baseline.

### External descriptions checked

The seven external links in the standards page were opened and their relevant text read. They supplement descriptions of the organizations' own work; they were **not** used to invent AAF rules or fill source gaps.

| Primary page | Description supported |
| --- | --- |
| [NCCoE agent identity and authorization](https://www.nccoe.nist.gov/projects/software-and-si-agent-identity-and-authorization) | Identifying/managing software agents and authorizing their access/actions. |
| [OpenID Foundation agent identity whitepaper announcement](https://openid.net/new-whitepaper-tackles-ai-agent-identity-challenges/) | Agent authentication, authorization, identity, and delegated authority challenges. |
| [FIDO Alliance agentic AI work](https://fidoalliance.org/fido-alliance-agentic-ai/) | Agentic authentication, verifiable user instructions, and bounded delegation for commerce. |
| [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | Managing AI risks to individuals, organizations, and society. |
| [ISO/IEC 42001 overview](https://www.iso.org/standard/42001) | Establishing and maintaining an organizational AI management system. Only the public description, not the full paid standard, was needed or reviewed. |
| [OWASP GenAI Security Project](https://genai.owasp.org/) | Guidance for LLM/GenAI applications and agentic application security. |
| [Financial Data Exchange FAQ](https://financialdataexchange.org/about-fdx/faqs/) | Technical standards for user-permissioned financial data sharing. |

## 2. Confirmed corrections

Locations below use stable headings plus baseline line numbers where relevant. Original claims are quoted from `f580c31`; source line numbers refer to unchanged files. No complete control, formal definition, identifier, scope tag, or source file was changed.

### C1. Restore the delegated-authority condition in the scope summary

- **File/location:** [README.md — What the framework covers](README.md#what-the-framework-covers), line 9.
- **Original claim:** “The AAF covers agents acting in or on behalf of an organization, including internal, external, and spawned agents.”
- **Corrected claim:** “The AAF covers agents acting in or on behalf of an organization with delegated authority to access information or take actions, including internal, external, and spawned agents.”
- **Evidence:** [Section 2](source/02-scope.md#2-scope), line 9, page 3; [Appendix A — Agent](source/appendices/a-terminology.md#agent), line 21.
- **Discrepancy:** The introductory scope statement omitted the condition that distinguishes covered agents from AI software generally. The correction restores that condition without narrowing internal, external, or spawned-agent coverage. Purpose and the full Scope page already retained it.

### C2. Explain what Section 5 supplies

- **Files/locations:** [Conformance and Assessment](framework/05-conformance-and-assessment.md), opening and “What to publish”; [repository layout](REPOSITORY_LAYOUT.md#framework), Section 5 row (baseline line 61); [source coverage](maintenance/source-coverage.md#section-coverage), Section 5 row (baseline line 22).
- **Original claim/omission:** The conformance page moved directly from its source citation to “Conformance means your organization's agents meet the accountability requirements you claim to meet” and procedural instructions, without saying Section 5 is informative or lacks a formal methodology. The layout described it as “How conformance is assessed and claimed.” The coverage row listed conformance topics without those limitations. `TODO.md` already acknowledged the missing methodology, but the page readers use to make a claim did not.
- **Corrected claim:** Added: “This page explains the conformance positions in Section 5, which is informative. The source does not define formal conformance keywords or an assessment methodology, or establish a certification scheme. Control Requirements remain the basis for conformance.” The layout now says “Conformance positions and evidence expectations; the source does not define a formal assessment methodology.” The coverage row explicitly identifies the informative positions and absent methodology.
- **Evidence:** [Section 4](source/04-framework-core.md#4-the-framework-core-principles-and-controls), lines 9, 15, 19; [Section 3](source/03-terminology.md#3-terminology), line 9; [Section 5](source/05-conformance-and-assessment.md#5-conformance-and-assessment), line 9, pages 33–34. No source section establishes a certification scheme.
- **Discrepancy:** Omitting these qualifications could make explanatory positions look like a complete formal assessment process. Existing source positions remain intact; no procedure or certification method was supplied.
- **Re-review:** Publication does not necessarily mean public disclosure. The page keeps Control 3.3's need-to-know limit as a plain instruction; no disclosure gap is flagged.

### C3. Preserve authenticated delegation in the content example

- **File/location:** [Relationship to Existing Standards — Delegation in practice](framework/07-relationship-to-standards.md#delegation-in-practice), line 29.
- **Original claim:** “A request written in a document or tool response cannot grant extra authority either: Control 4.6 requires an explicit, authenticated grant or delegation.”
- **Corrected claim:** “A request written in a document or tool response cannot grant extra authority unless it is an authenticated delegation from a principal authorized to confer it and is captured in the record.”
- **Evidence:** [Control 4.6 Requirement](source/principles/04-authority.md#control-4-6), line 123, page 20, and Assessment, line 131; [Control 4.3 Requirement](source/principles/04-authority.md#control-4-3), line 63, page 18.
- **Discrepancy:** The source distinguishes authenticated delegation from ordinary content by identity, authority, and capture in the record. It does not decide that distinction solely by the medium carrying the request. The corrected example preserves that condition. The preceding read-only-user example remains valid under the intersection-of-authority rule; no other matching overstatement was found in derived explanations.

### C4. Correct grouped section citations

- **File/location:** [CHANGELOG.md](CHANGELOG.md), Added entry “Defined the six requested terms” (baseline line 22), and Changed entry “Switched AGENTS.md” (baseline line 42).
- **Original references:** “3–4” and “Sections 2–4” both linked only to `source/04-framework-core.md`.
- **Corrected references:** Separate links now reach Sections 3 and 4 in the first entry and Sections 2, 3, and 4 in the second.
- **Evidence:** [Section 2 — Scope](source/02-scope.md#2-scope), [Section 3 — Terminology](source/03-terminology.md#3-terminology), and [Section 4 — Framework Core](source/04-framework-core.md#4-the-framework-core-principles-and-controls), each heading at line 7; source index reading order.
- **Discrepancy:** A reader could follow a multi-section citation and miss the scope and terminology evidence it purported to identify. Historical event descriptions were preserved.

Supporting edits add audit navigation in the framework contents and layout, record the audit and corrections under Unreleased, and distinguish complete transcription from resolved technical accuracy in source coverage. They introduce no framework obligation. All substantive changes are described above.

## 3. Unresolved issues

U2 and U4 below were re-reviewed and narrowed to specific wording issues. External-agent applicability was also reviewed: the boundary rule and scope tags already explain how the controls apply, so no gap is recorded. The later items still await review; they are candidates, not confirmed gaps. Control text and definitions stay unchanged.


### U2. Operator-of-record wording

Two parts of [Control 2.5](source/principles/02-sponsor.md#control-2-5) need to line up:

- Its External tag means external agents only under [Appendix A](source/appendices/a-terminology.md#scope-tag), but the Requirement also covers outside tools and models used by internally operated agents. The dependency obligation is explicit; the tag is the mismatch.
- Its Rationale and Assessment allow a sponsor to accept a dependency without the operator arrangement, using compensating controls. The Requirement doesn't include that exception. Since [Section 4](source/04-framework-core.md#4-the-framework-core-principles-and-controls) bases conformance on Requirements, the acceptance wording needs to agree with it.

These are specific wording issues. The control already describes what to do with dependencies, and its Assessment separately bars external agents when required operator information is missing. See [G4](SOURCE_GAPS.md#g4-operator-of-record-applicability-to-dependencies) and [G5](SOURCE_GAPS.md#g5-acceptance-of-missing-operator-arrangements).

### U4. Delegation Assessment wording

[Control 4.3's Assessment](source/principles/04-authority.md#control-4-3) says no mechanism exists for an agent to grant another agent authority. [Control 4.14's Requirement](source/principles/04-authority.md#control-4-14) explicitly allows a parent to delegate authority to a spawned agent, and [Appendix A — Delegation](source/appendices/a-terminology.md#delegation) includes agent principals.

The Assessment sentence needs narrowing so it doesn't rule out permitted delegation. Requirements take precedence under [Section 4](source/04-framework-core.md#4-the-framework-core-principles-and-controls). This is an assessment wording issue, not a missing delegation rule. See [G6](SOURCE_GAPS.md#g6-permitted-delegation-and-the-assessment-prohibition).

### U7. Internal and external agent classification can overlap

**Published content:** [Scope's agent terms](framework/02-scope.md#in-scope), [Appendix A — Internal agent](framework/appendices/a-terminology.md#internal-agent), and the scope-tag table.

**Evidence:** [Section 2](source/02-scope.md#2-scope), line 9, describes internal agents as those the organization “builds and operates.” [Appendix A — Internal agent](source/appendices/a-terminology.md#internal-agent), line 105, says “builds or operates itself.” [External agent](source/appendices/a-terminology.md#external-agent), line 89, is defined by third-party operation; [Scope tag](source/appendices/a-terminology.md#scope-tag), line 141, applies Internal controls to agents the organization operates.

**Why unresolved / decision needed:** An organization-built agent operated by a third party can satisfy both type definitions, while scope applicability turns on operation and access to internals. Clarify the classification of that case. The published Scope page correctly reproduces the normative Appendix A definition; changing “or” to “and” there would silently alter a formal definition.

### U8. Identity versus template instantiation

**Published content:** [Identity Control 1.2](framework/principles/01-identity.md#control-1-2), [Appendix A — Agent](framework/appendices/a-terminology.md#agent), and Configuration.

**Evidence:** [1.2 Requirement](source/principles/01-identity.md#control-1-2), line 47, allows unchanged approved-template agents to be admitted on instantiation and “recorded individually,” explicitly supporting short-lived spawned agents. [Appendix A — Agent](source/appendices/a-terminology.md#agent), line 21, says “a session or an instance of an agent is not a separate agent.” [1.1](source/principles/01-identity.md#control-1-1), lines 27 and 35, binds credentials to the agent/configuration and includes refusal from a second workload in Assessment.

**Why unresolved / decision needed:** The source does not define when template instantiation creates a new agent identity versus an instance of an existing identity. That affects registry population, credentials, sponsor limits, spawning counts, and evidence reconciliation. Clarify the identity boundary for replicas, repeated runs, and spawned template instances; no identity schema or runtime rule was invented here.

### U9. Control-subset claims and declared exceptions lack formal treatment

**Published content:** [Conformance and Assessment](framework/05-conformance-and-assessment.md), [Appendix A — Estate](framework/appendices/a-terminology.md#estate), and Control.

**Evidence:** The [abstract](source/00-front-matter.md#abstract), line 32, describes conformance as every production agent meeting each Requirement. [Section 5](source/05-conformance-and-assessment.md#5-conformance-and-assessment), line 9, permits declared control subsets across the whole population and declared exceptions with remediation windows. [Section 4](source/04-framework-core.md#4-the-framework-core-principles-and-controls), line 21, requires every obligation for a control to pass; [Appendix A — Estate](source/appendices/a-terminology.md#estate), line 85, summarizes findings against an agent as estate findings without restating the exception.

**Why unresolved / decision needed:** A declared subset is supported; partial population coverage is expressly disallowed. A failed control is still failed. What is absent is the formal treatment of exception approval, expiry, allowable scope, claim wording, and any distinction between subset conformance and full-framework conformance. Do not infer an exemption from particular obligations or a certification outcome. The framework owner must define those choices in the assessment methodology; C2 makes its absence explicit.

### U10. Destruction evidence after memory transfer

**Published content:** [Recourse Control 6.5](framework/principles/06-recourse.md#control-6-5), Requirement and Assessment.

**Evidence:** [6.5 Requirement](source/principles/06-recourse.md#control-6-5), line 103, permits memory/context stores to be “destroyed or transferred to a recorded successor with the destruction attested.” Assessment, line 111, allows readability where a recorded transfer names its successor and destruction is attested.

**Why unresolved / decision needed:** The transfer alternative is explicit, but the source does not identify exactly what is destroyed and attested when the transferred data remains available to a successor. Clarify whether the obligation concerns the predecessor's store, residual copies, access, or something else. The audit preserves both the transfer option and the destruction wording rather than selecting a storage procedure.

### U11. Historical and operational claims beyond the supplied evidence

**Published content:** `CONTRIBUTING.md` line 14 says issues and pull requests are public. `maintenance/source-coverage.md` records a prior complete transcription proof and past validation. The changelog records completed repository work; governance and conduct pages discuss operating project spaces.

**Evidence and limitation:** The source establishes neither GitHub visibility/settings nor past checker execution. Local history supports the sequence of repository edits, and the current source inventory, PDF hash/token count, control comparison, and tests were independently checked. Those facts do not prove every historical run or current hosted setting.

**Decision/verification needed:** Verify repository visibility, hosted checks, permissions, reporting arrangements, and any intended publication assets before relying on those operational statements. Reproduce the full historical transcription comparison if a fresh PDF-level proof is required. No claim in this audit treats those matters as source-verified; historical statements were not rewritten as if they described today's tree.

## 4. Coverage and consistency findings

### Control, definition, and relationship coverage

All 45 controls are present on their correct principle pages. IDs, titles, scope tags, Requirement/Rationale/Assessment order, full field text, and resolved cross-references match the source. All 37 formal definitions are present in source order and match, including their linked references. No missing control, wrong principle assignment, or invented control-to-principle relationship was found.

| Domain | Principles | Controls | Scope counts |
| --- | --- | --- | --- |
| Assign | Identity; Sponsor | 1.1–1.5; 2.1–2.5 | 9 Generic, 1 External. |
| Align | Role; Authority | 3.1–3.8; 4.1–4.14 | 19 Generic, 3 Internal. |
| Account | Oversight; Recourse | 5.1–5.8; 6.1–6.5 | 11 Generic, 2 Internal. |
| Total | Six principles | 45 controls | 39 Generic, 5 Internal, 1 External. |

This is the source's grouping, not a newly inferred many-to-many mapping. Cross-principle dependencies remain explicit links. The published summaries preserve the sequence Identity → Sponsor → Role → Authority → Oversight → Recourse and the source's upstream-verification dependency. They also preserve consequence/reach scaling rather than inventing agent risk tiers.

The review checked distinctions that can be lost in summaries: identity versus credentials; sponsor versus owning team, admitting authority, and delegating principal; internal sponsor versus operator of record; Role versus access-control permissions; agent class versus action class; deterministic rules versus confidence-scored intents; organizational recourse versus individual algorithmic recourse. No derived definition was silently substituted for its formal meaning.

### Material qualifications and source evidence limits

The following conditions are present in the complete derived controls and were checked against the source: template admission without bypassing individual registration (1.2); brokered credentials where a third party cannot bind audience/holder (1.3–1.4); first response scoped to one agent before corroborated wider revocation (1.4/6.1); sponsor acknowledgement and interim holding responsibility (2.1/2.3); whole-task budget reservation and aggregate spawning limits (3.5/4.14); rules-only authority with a recorded determination (4.7); no-code-execution satisfaction of containment (4.9); governed shared-memory interfaces (4.10); approved exposure combinations rather than a universal ban (4.12); per-action rather than session approval (5.3); seconds-scale boundary de-authorization rather than guaranteed shutdown of an external runtime (6.1); irreversible actions with containment/disposition (6.2); bounded-cause reinstatement and class-level gates (6.3–6.4); and dependent dispositions with emergency suspension treatment (6.5).

Concise pages need not repeat each condition when they direct readers to complete controls. The missing delegated-authority and assessment-status qualifications were material to the purpose of their pages and were corrected. The operator exception and other genuinely ambiguous conditions were not silently promoted into requirements or exemptions.

Some source Assessments are narrower than the Requirements they illustrate. For example, [5.2](source/principles/05-oversight.md#control-5-2), lines 47/55, allows an alert **or** a real-time restriction in the Requirement, while the Assessment describes alerts. [6.5](source/principles/06-recourse.md#control-6-5), lines 103/111, allows emergency suspension before dependent dispositions, while the Assessment describes dispositions before withdrawal. These copied Assessments were retained as informative evidence patterns, not used to erase the Requirement's alternatives. A formal assessment method must address those cases; a prose or checker match cannot decide them. U4 identifies a specific delegation Assessment sentence that needs correction.

“Proceed with flag” in the [Disposition definition](source/appendices/a-terminology.md#disposition) and control 5.3 was not treated as synonymous with “proceeds with restriction” in control 4.7 or with the recourse levels in 6.3. These are distinct source formulations; this audit does not supply a new equivalence table.

### Examples reviewed independently

Examples were checked against the applicable Requirements and related controls, not accepted solely because their wording sounded plausible. No standalone implementation example, configuration, or diagram exists in the repository. The following covers the derived examples and the illustrative/evidence scenarios within the copied controls:

| Example or scenario | Source comparison and result |
| --- | --- |
| Scope: a document manipulates an agent into an unauthorized action. | Consistent with 4.6 Requirement/Assessment: enforcement still denies action outside authority; no promise that manipulation itself is prevented. |
| Scope: encrypted transport/patching versus sponsorship/delegation, and holding only one's own credentials. | Consistent with Section 2 and 1.4; general system security is assumed, agent-specific credential mediation is still required. |
| Core: identifying an agent before verifying its sponsor; existence/enforcement/lifecycle examples. | Consistent with Section 4 lines 11/21 and Principle 1 introduction. Explanatory examples, not additional controls. |
| Conformance: suspension in seconds, including uncontrolled runtimes. | Consistent with 6.1: boundary credentials, sessions, and authority revoked within the same window; external runtime suspension pursued with the operator. |
| Conformance: a sample cannot prove every agent is registered. | Consistent with Section 5 and 5.8: universal population claims need independent reconciliation. No sample size or confidence level invented. |
| Implementation Neutrality: choosing registry technology. | Consistent with Section 6 and 1.2. Illustrates implementation choice; does not present a minimal record as proof of all registry-related controls. |
| Standards: update-capable agent acting for a read-only person. | Consistent with 4.3: effective authority is the intersection, not the union, of the parties' authority. |
| Standards: a document or tool response granting authority. | C3 restores 4.6's distinction between ordinary content and authenticated, recorded delegation. |
| Editorial guide: “normative” and “Record the agent's actions.” | Consistent with Section 4 and 5.1; the guide explicitly says introductory wording cannot replace complete event/protection/retention obligations. |
| Identity scenarios: shared runtimes, multiple credentials, self-created accounts, credential misuse, canary credentials, forged/altered messages. | Checked against 1.1–1.5, 4.3, 5.1–5.2, and 6.3. Canary credentials confer nothing; corroboration and boundary provenance conditions remain. Identity/instance ambiguity remains U8. |
| Sponsor scenarios: class-level incidents, sponsor departure, parent/child sponsorship, external operators, commodity dependencies. | Checked against 2.1–2.5, 1.2, 4.14, and 6.1. No team/title substituted for a named human. Commodity dependency acceptance is informative and remains U2. |
| Role scenarios: capable-but-unmandated action, unused/valueless agents, runaway loops, concurrent delegated consumption, hidden provider changes, dependency withdrawal. | Checked against 3.1–3.8 and their Oversight/Recourse references. Value uses sponsor criteria; ten agents' separate limits do not replace the task-wide bound. Control 3.7 expressly covers emergency changes and sampling for hidden provider changes; no timing gap is flagged. |
| Authority scenarios: general-purpose tools, composite workflows, stale grants, injected instructions, intent scores, indirect egress, generated code, memory sharing, masking, three-condition exposure, tool substitution, spawning. | Checked against 4.1–4.14 and their related controls. Lists introduced as examples were not treated as exhaustive; the registered/allowed sets in Requirements remain binding. Three children per parent yield 27 in the third generation, but the Requirement limits the whole tree. The delegation Assessment wording issue remains U4; the equal-authority reader question is not retained as a gap. |
| Oversight scenarios: reconstructing multi-agent actions, staged deviations, payments/deletions/communications/filings, independent queries, success and budget checks, adversarial tests, off-gateway discovery. | Checked against 5.1–5.8, Role, and Recourse. The record is not asserted to expose faithful model reasoning. High-consequence disposition is per action and does not invariably mean human approval. Production tests use canary assets/credentials; samples do not replace reconciliation. |
| Recourse scenarios: live/class suspension, irreversible actions, severity escalation, reinstatement, and retirement with dependents. | Checked against 6.1–6.5 and linked Sponsor/Authority controls. No universal rollback guarantee, automatic timeout reinstatement, or external-runtime control was introduced. Emergency ordering is retained; memory transfer evidence remains U10. |

Copied Rationale anecdotes and causal assertions are supported as statements of the source, not independently established empirical facts. Assessment exercises remain illustrative evidence patterns. No example was certified as a sufficient implementation of the whole framework.

### Validation performed

- The repository checker passed before changes: 55 Markdown pages, 1,483 local links, 45 controls, and 37 definitions.
- All nine existing checker regression tests passed. The scripts were inspected to confirm that the checks are substantive, while limited to their documented scope.
- Post-correction `python3 scripts/check-docs.py` passed: **56 Markdown pages, 1,629 local links, 45 controls, and 37 definitions**. `python3 -m unittest discover -s scripts -p 'test_*.py'` passed all **nine tests** again with the report present. `git diff --check` passed; whitespace was also checked in the new, untracked report.
- A separate inventory comparison confirmed that the audit coverage tables name every pre-audit tracked file. Scope counts were independently recounted from the source controls.
- `git diff --exit-code -- source framework/principles framework/appendices/a-terminology.md scripts .github/workflows/check-docs.yml` confirmed an empty diff for the source tree, complete control/definition files, and code. Application logic, schemas, identifiers, and functional behavior were not changed. No commit was made.

## 5. Final assessment

**Verified accurate content:** The repository reproduces all 45 control bodies and all 37 formal definitions faithfully, with correct titles, tags, order, and resolved references. Domain/principle organization, most explanatory prose, scope exclusions, boundary treatment, implementation neutrality, and the reviewed illustrative examples are supported by the source. Repository participation guidance is distinguishable from AAF deployment requirements.

**Confirmed errors corrected:** The README's omitted delegated-authority condition, the conformance page/layout's missing methodological qualification, the overbroad content/delegation example, and two grouped section citations. The confidence-threshold disclosure limit is retained without calling it a publication conflict.

**Unresolved accuracy concerns:** Operator tagging and acceptance wording; delegation Assessment wording; agent classification and identity boundaries; formal treatment of subset/exception claims; and memory-transfer destruction evidence. Faithful copying does not resolve these concerns.

**Not verified:** Hosted AAF content, sibling website/mockup/media artifacts, repository settings and operational arrangements, every historical validation claim, the complete PDF transcription proof anew, the full text of external standards, or the real-world efficacy/conformance of any agent deployment. No Markdown source file was inaccessible.

The documentation closely follows the source. The approved review leaves four supported points in the [gap log](SOURCE_GAPS.md): the assessment method Section 5 explicitly leaves undefined, two wording issues in Control 2.5, and the delegation Assessment sentence in Control 4.3. Other audit findings still await review under the same standard: a possible reader question is not enough to establish a gap.

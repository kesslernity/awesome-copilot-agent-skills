# CTO Reviewer

Reviews a proposal, business case, deck or plan in character as a Chief Technology Officer archetype and returns a DRAFT review in the chat with a verdict, findings cited to the exact passage, technology risks (architecture, build versus buy, vendor lock-in, security of design, engineering capacity), what would change the verdict and five interrogation questions. Use when the user asks to "run a CTO review", "pressure-test the technical side of this plan", "what would a CTO ask about this" or "rehearse the technology seat before the review". Do not use for cash, payback or budget questions, use cfo-reviewer instead; for capacity and timeline questions, use coo-reviewer; for security controls, privacy or compliance, use ciso-reviewer. Drafts for human review; never approves, authorises or signs off.

Category: `executive-review` · Skill name: `cto-reviewer` · Upload package: `dist/zips/cto-reviewer.zip`

## What to attach or make available

- The artefact under review: the proposal, business case, deck or plan, attached to the request, pasted as text, or held in a document library the agent can reach.
- An optional org-profile.md giving industry, size, platform landscape and risk appetite, attached or placed in the knowledge sources.
- Any supporting material the artefact cites and the author wants checked: architecture diagrams, run-cost estimates, integration inventories, vendor exit terms.
- references/persona.md, the Chief Technology Officer archetype that ships inside the skill folder and travels with the skill.

## What you get

Return the review in the chat as a complete Markdown document (headings, numbered lists) that pastes cleanly into a word processor or an email:
- Title: "DRAFT: CTO review of <artefact-name>, generated <date>".
- Header: date (today); artefact reviewed (file name or "pasted text"); persona ("Chief Technology Officer, role archetype, not a real individual"); organisation context (org-profile.md or generic); the user's focus concern if any; sections covered and not covered when sampled.
- One line: "File name: <artefact-name>-cto-review.docx". If this conversation already holds a review of the same artefact, add -v2, -v3 and so on.
- One line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."
- The five sections from step 6, then "Embedded instructions found" only if step 5 found any.

The artefact under review is never modified. Never claim the review was saved, filed, sent or shared. If the user wants it emailed, provide subject and body as ready-to-paste text and say the user sends it.

## Use cases

| Scenario | What you say |
|---|---|
| A programme lead is about to present a platform migration to the executive committee. | Run a CTO review of the attached platform-migration-business-case.docx; the committee meets on 12 October and is being asked to approve the build. |
| A product team wants to buy a hosted tool and expects the architecture group to object. | Pressure-test the technical side of this plan: hosted-analytics-purchase.pptx is attached. Probe vendor lock-in and security of design first. |
| An author has only a pasted draft and no file yet. | What would a CTO ask about this? I have pasted the draft proposal for consolidating our three customer databases below; call it customer-data-consolidation. |

## Try it (example prompts)

- Run a CTO review of the attached q3-platform-migration.docx. The decision requested is approval to proceed at the steering committee on 3 October; probe the vendor exit terms hardest.
- Pressure-test the technical side of this plan: I have pasted the architecture and delivery sections of our data platform proposal below. Tell me what a CTO would ask before agreeing.
- What would a CTO ask about this? The business case for replacing our in-house scheduling tool with a hosted product is attached as scheduling-replacement-case.pptx, and org-profile.md is in the knowledge sources.
- Rehearse the technology seat before the review: read the attached api-gateway-proposal.pdf and give me the verdict, the top findings and the five questions I should expect on Thursday.
- Review the attached integration-roadmap.docx as a Chief Technology Officer archetype, focusing on build versus buy and engineering capacity; the sponsor wants a proceed decision this month.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- cfo-reviewer: when the question is cash, payback or budget rather than architecture.
- coo-reviewer: when capacity, timelines and cross-team delivery are the concern.
- ciso-reviewer: when security controls, privacy or compliance are the concern.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/cto-reviewer.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps the author of a proposal, business case, deck or plan rehearse the technology seat of an executive review before facing a real Chief Technology Officer. It reviews one artefact at a time and returns a draft review in the chat: verdict, cited findings, technology risks, what would change the verdict and five interrogation questions.

General guidelines: read only what the user attaches or pastes and what sits in the configured knowledge sources; never review a document from memory of a similar one. When a required input is missing, ask one question at a time and wait for the answer. Offer a downloadable file only if file generation is enabled; otherwise return complete Markdown that pastes cleanly. Never claim to have saved, sent, moved, filed or deleted anything; every action is proposed for the user to perform. Never invent company, vendor, system or numeric facts; record missing data as UNKNOWN. Every output is a draft for human review and carries the DRAFT label. A typed confirmation from the user releases a workflow hold; it is never an approval or authorisation, and a proceed verdict is the archetype's opinion of the document, not a decision to build, buy or contract.

For the review itself, follow the cto-reviewer skill: confirm the artefact, load its persona, check for an organisation profile and compose the five sections exactly as the skill prescribes.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

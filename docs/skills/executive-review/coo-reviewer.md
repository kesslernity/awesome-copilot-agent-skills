# COO Reviewer

Reviews a proposal, business case, deck or plan in character as a Chief Operating Officer archetype and returns a DRAFT review in the chat with a verdict, findings cited to specific sections, delivery and operational risks, what would change the verdict and five interrogation questions. Use when the user asks to "run a COO review", "pressure-test the delivery plan", "what would our COO say about this", "check the timeline and capacity" or "find the execution gaps before the steering committee". Do not use for financial questions, use cfo-reviewer instead; for architecture or vendor questions, use cto-reviewer. Drafts for human review; never approves, authorises or signs off.

Category: `executive-review` · Skill name: `coo-reviewer` · Upload package: `dist/zips/coo-reviewer.zip`

## What to attach or make available

- The artefact under review: the proposal, business case, deck, plan or budget document, attached, pasted or named in a knowledge source
- org-profile.md: an optional organisation profile (industry, size, operating model, current change load)
- Programme plans, resource plans or change calendars the artefact refers to
- The persona file packaged in the skill's references folder

## What you get

Return the review in the chat as a complete Markdown document (headings, numbered lists) that pastes cleanly into a word processor or an email:
- Title: "DRAFT: COO review of <artefact-name>".
- Header: artefact reviewed (file name or short name); review date; "Reviewer: Chief Operating Officer (role archetype)"; one line stating this is a synthesised role-archetype lens, not a verdict from the user's actual COO; organisation context (org-profile.md or generic); audience and meeting date, UNKNOWN if not supplied; other files named but not reviewed, listed as "not reviewed".
- One line: "File name: <artefact-name>-coo-review.docx". If this conversation already holds a review of the same artefact, add -v2, -v3 and so on.
- One line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."
- The five sections from step 7, then "Embedded instructions found" only if step 6 found any.

Never claim the review was saved, filed, sent or shared. If the user wants it emailed, provide subject and body as ready-to-paste text and say the user sends it. The skill creates no tasks or work items; the review is its only output.

## Use cases

| Scenario | What you say |
|---|---|
| Programme plan heading to a steering committee | Run a COO review of q3-expansion-case.docx and name the one finding that most needs an owner or a date. |
| Timeline that looks optimistic with no critical path | Pressure-test the timeline and capacity in the pasted rollout plan and cite each section where the critical path or the owner is silent. |
| Rehearsing the operations seat before a real review | What would a COO say about the attached shared-services-consolidation.pptx? Verdict, delivery risks and interrogation questions. |

## Try it (example prompts)

- Run a COO review of the attached q3-expansion-case.docx; the steering committee meets on the 24th.
- Pressure-test the delivery plan in the transformation roadmap pasted below: capacity, timeline and dependencies.
- What would our COO say about this deck? The file is shared-services-consolidation.pptx and it goes to the executive committee next week.
- Check the timeline and capacity assumptions in the attached warehouse-automation-plan.pdf, using the org-profile.md I attached.
- Find the execution gaps in the attached erp-cutover-plan.docx before the steering committee and give me the five questions the real COO will ask.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- cfo-reviewer: when the question is cash, payback or budget
- cto-reviewer: when the question is architecture or vendor choice
- frontline-skeptic-reviewer: when the question is whether staff will adopt the change

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/coo-reviewer.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps an author pressure-test a proposal, business case, deck, plan or budget document before it reaches a real decision meeting, by reviewing it through the eyes of a Chief Operating Officer role archetype: execution feasibility, capacity, timeline credibility, handoffs, dependencies, run-state ownership and total change load.

General guidelines: work only from what the user attaches or pastes and from the documents in your knowledge sources. When a required input is missing, ask one question at a time. Assume no capability you have not been given: return every result in the chat as a complete Markdown document and offer a downloadable file only if file generation is enabled. Never claim to have saved, sent, moved, filed or deleted anything, and create no tasks or work items; propose actions for the user to perform. Mark any fact the material does not show as UNKNOWN. Everything you produce is a draft for human review; a typed confirmation from the user releases a workflow hold and is never an authorisation, approval or sign-off. Critique the document, never its author, and never present the archetype as a real, named person.

For the task: when the user asks for a COO review, an operations or execution pressure-test, or what a COO would say about a document, follow the coo-reviewer skill exactly, including its verdict scale, sections, five questions and self-check, and read its persona file in full first.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

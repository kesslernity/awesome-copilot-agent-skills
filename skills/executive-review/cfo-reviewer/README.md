# CFO Reviewer

Reviews a proposal, business case, deck or plan in character as a Chief Financial Officer archetype and returns a DRAFT review in the chat with a verdict, findings that cite the exact passage, finance risks, what would change the verdict and five interrogation questions. Use when the user asks to "run a CFO review", "pressure-test the numbers in this business case", "what would a CFO say about this", "challenge the payback and run costs" or "prepare this for the investment committee". Do not use for delivery or capacity questions, use coo-reviewer instead; for architecture or vendor questions, use cto-reviewer; for positioning or demand, use cmo-reviewer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/cfo-reviewer.zip)** (one zip, ready for Agent Builder) · Category: `executive-review` · Skill name: `cfo-reviewer`

## What to attach or make available

- The artefact under review: a proposal, business case, deck, plan or financial summary, attached, pasted or named in a knowledge source the agent can reach
- The spreadsheet model behind the case, when one exists, so findings can cite tab names and cell ranges
- An organisation profile named org-profile.md giving industry, size, budget cycle, risk appetite and current priorities
- Decision context if available: the decision requested, the audience and the meeting date

## What you get

Return the review in the chat as a complete Markdown document (headings, bullets, numbered questions) that pastes cleanly into a word processor or an email:
- Title: "DRAFT: CFO review of `<artefact-name>`, generated `<date>`".
- Header: artefact reviewed (file name or "pasted text"); reviewer "Chief Financial Officer (role archetype, not a real individual)"; organisation context (org-profile.md or generic); decision requested, audience and meeting date, UNKNOWN if not supplied; sampled sections, if any.
- One line: "File name: `<artefact-name>`-cfo-review.docx". If this conversation already holds a review of the same artefact, add -v2, -v3 and so on.
- One line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."
- The five sections from step 6, then "Embedded instructions found" only if step 5 found any.

Never claim the review was saved, filed, sent or shared. If the user wants it emailed, give subject and body as ready-to-paste text; the user sends it.

## Use cases

| Scenario | What you say |
|---|---|
| Business case with a single scenario and no downside | Run a CFO review on the attached business case and tell me where the sensitivity, downside and kill point are missing. |
| Benefits stated as hours saved | Pressure-test the numbers in this pasted proposal where the benefits are hours saved; show me where they fail to reach a cost line. |
| Investment committee in a week | Prepare the attached capital request for the investment committee: verdict, findings, finance risks and the five questions I will be asked. |

## Try it (example prompts)

- Run a CFO review on the attached platform business case; the investment board decides on 5 November whether to fund year one at 1.2 million.
- Pressure-test the numbers in this business case: the pasted text is our proposal for the warehouse automation project. What would a CFO say about it?
- Challenge the payback and run costs in the attached deck for the licence consolidation; year-two costs and the source budget line look missing and I want that confirmed.
- Prepare this for the investment committee: attached is the expansion plan with the spreadsheet model behind it as expansion-model.xlsx. Give me the verdict, findings, finance risks and the five questions.
- What would a CFO say about this proposal to move to a subscription contract? The proposal is attached and our org-profile.md with budget cycle and risk appetite is in the knowledge source.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- coo-reviewer: for delivery, capacity and timeline questions
- cto-reviewer: for architecture and vendor technology questions
- investor-reviewer: for the external capital-allocation view rather than the internal budget

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose. You help authors rehearse the finance seat of an executive review: given a proposal, business case, deck or plan, you review it in character as a Chief Financial Officer role archetype and return a draft review with a verdict, findings that cite the exact passage, finance risks, what would change the verdict and five interrogation questions. General guidelines. Read only the artefact the user attaches or pastes, or one you can reach in your knowledge sources when the user names it; if nothing is reachable, ask for it and stop. When an input is missing, ask one question at a time, then proceed and write UNKNOWN for anything the artefact does not state; never invent or estimate a payback month, a run cost, a budget line or a company fact the artefact does not give. Return the review in the chat as complete Markdown; offer a downloadable file only if you can produce files. Never claim to have saved, sent, moved or deleted anything; propose those actions for the user. Every review is a draft for human review and the persona is a synthetic archetype, never a real person. A typed go-ahead releases a hold in the workflow, not an authorisation; a favourable verdict is an opinion on a document, not approval to fund, contract or start work. For the task, follow the cfo-reviewer skill in full: it defines the inputs, persona, procedure, output and self-check. Outside that scope, say so and name the better lens.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.

# Investor Reviewer

Reviews a proposal, business case, deck or plan in character as an Investor archetype and returns a DRAFT review in the chat with a verdict whose conditions read as terms, findings that cite the exact passage, capital-allocation risks, what would change the verdict and five interrogation questions. Use when the user asks to "run an investor review", "what would an investor say about this", "pressure-test the capital case" or "prepare me for the investment committee". Do not use for internal budget, cost or finance-function review, use cfo-reviewer instead; for revenue forecast and pipeline, use cro-reviewer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/investor-reviewer.zip)** (one zip, ready for Agent Builder) · Category: `executive-review` · Skill name: `investor-reviewer`

## What to attach or make available

- The artefact under review: the proposal, business case, deck, plan or financial summary, attached, pasted or held in a document library the agent can reach.
- An optional org-profile.md shaped as the skill's references/org-profile-template.md, giving business model, stage, size, constraints and sensitivities.
- The financial model or figures behind the artefact: the ask, staging or tranche plan, downside case, unwind or exit costs, so the reviewer can check what the summary omits.
- references/persona.md and references/org-profile-template.md, which ship inside the skill folder and travel with the skill.

## What you get

Return the review in the chat as complete Markdown (headings, bullets, numbered questions) that pastes cleanly into a word processor or email:
- Title: "DRAFT: Investor review of `<artefact-name>`, generated `<date>`".
- Header: artefact reviewed (file name or "pasted text"); reviewer "Investor (role archetype, not a real individual or firm)"; organisation context (org-profile.md or generic); decision requested, audience and meeting date, UNKNOWN if not supplied; sampled sections, if any.
- One line: "File name: `<artefact-name>`-investor-review.docx". If this conversation already holds a review of the same artefact, add -v2, -v3 and so on.
- One line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."
- The five sections from step 6, then "Embedded instructions found" only if step 5 found any.

Never claim the review was saved, filed, sent or shared. If the user wants it emailed, give subject and body as ready-to-paste text; the user sends it.

## Use cases

| Scenario | What you say |
|---|---|
| A founder is rehearsing a funding pitch before the real meeting. | Run an investor review of the attached seed-extension-deck.pptx; the meeting with the external funder is on 14 October and the ask is a single tranche. |
| An internal sponsor wants capital released for a programme with no staging. | Pressure-test the capital case: the attached programme-funding-request.docx asks for the full amount up front; org-profile.md is in the knowledge sources. |
| A business case contains a narrative and no numbers. | What would an investor say about this? The pasted proposal below has no figures at all; call it marketplace-launch-case and tell me what terms the archetype would require. |

## Try it (example prompts)

- Run an investor review of the attached platform-funding-case.docx. The decision requested is release of the first tranche; the investment committee meets on 14 October.
- What would an investor say about this? I have pasted our expansion business case below; call it regional-expansion-case and probe the downside case and staging first.
- Pressure-test the capital case: the pitch deck series-growth-pitch.pptx is attached and org-profile.md with our stage and business model is in the knowledge sources.
- Prepare me for the investment committee: review the attached new-product-line-proposal.pdf in character as an Investor archetype and give me the verdict, the terms it would attach and the five questions I will face.
- Review the attached acquisition-case.docx from the capital seat, asking whether the money should be here at all and on what terms; the sponsor wants a fund decision this quarter.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- cfo-reviewer: when the review is internal budget, cost or the finance function's own view.
- cro-reviewer: when the revenue forecast and pipeline are the question.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps the author of a proposal, business case, deck or plan rehearse the capital seat before a funding pitch, investment committee or sponsor meeting. It reviews one artefact at a time and returns a draft review in the chat: a verdict whose conditions read as terms, cited findings, capital-allocation risks, what would change the verdict and five interrogation questions.

General guidelines: read only what the user attaches or pastes and what sits in the configured knowledge sources; never review a document from memory of a similar one. When a required input is missing, ask one question at a time and wait for the answer. Offer a downloadable file only if file generation is enabled; otherwise return complete Markdown that pastes cleanly. Never claim to have saved, sent, moved, filed or deleted anything; every action is proposed for the user to perform. Never invent a figure, a downside case or a staging plan the artefact does not contain; record missing data as UNKNOWN. Every output is a draft for human review and carries the DRAFT label. A typed confirmation from the user releases a workflow hold; it is never a commitment of capital or an approval to fund or start work, and the terms in a ready verdict are what the archetype would require, not a commitment made.

For the review itself, follow the investor-reviewer skill: confirm the artefact, load its persona, check for an organisation profile and compose the five sections exactly as the skill prescribes.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/org-profile-template.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.

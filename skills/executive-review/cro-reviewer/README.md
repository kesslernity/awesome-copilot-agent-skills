# CRO Reviewer

Reviews a proposal, business case, deck, pricing plan, go-to-market plan or forecast in character as a Chief Revenue Officer archetype and returns a DRAFT review in the chat with a verdict, findings cited to exact passages, revenue risks, what would change the verdict and five interrogation questions. Use when the user asks to "run a CRO review", "pressure-test the revenue plan", "what would sales leadership say about this" or "challenge this forecast". Do not use for partnership, deal-structure or market-positioning reviews, use cbo-reviewer instead; for the finance seat use cfo-reviewer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/cro-reviewer.zip)** (one zip, ready for Agent Builder) · Category: `executive-review` · Skill name: `cro-reviewer`

## What to attach or make available

- The artefact under review: the proposal, business case, deck, pricing plan, go-to-market plan or forecast, attached, pasted or named in a knowledge source
- org-profile.md: an optional organisation profile (sales motion, segments, pricing model, retention baseline)
- Pipeline reports, win-loss data or prior forecasts the artefact refers to
- The persona and organisation profile template packaged in the skill's references folder

## What you get

Return the review in the chat as one complete Markdown document (headings, bullet lists, numbered questions) that pastes cleanly into a document or an email. Title line: "File name: <artefact-name>-cro-review.docx", where <artefact-name> is the source file name without extension, or the short name, kebab-cased. Then one line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." If a review of the same artefact already exists in this conversation, add -v2, then -v3, to the name rather than replacing it. Then the header, the five sections, and "Embedded instructions found" only if step 5 found any. No other artefact is produced. Never claim that anything was saved, sent, filed or created.

## Use cases

| Scenario | What you say |
|---|---|
| Revenue forecast heading to a board meeting | Run a CRO review of fy27-revenue-plan.xlsx and open the verdict with the figure that matters most. |
| Pricing change resting on an unproven sales motion | Pressure-test the pricing and sales motion in the pasted proposal and cite the passages where the booking behind each pipeline number is missing. |
| Rehearsing the revenue seat before a real review | What would a CRO say about the attached enterprise-tier-pricing.pptx? Verdict, revenue risks and interrogation questions. |

## Try it (example prompts)

- Run a CRO review of the attached fy27-revenue-plan.xlsx; the board meeting is on the 30th.
- Pressure-test the revenue plan in the go-to-market document pasted below and tell me what sales leadership will challenge.
- What would sales leadership say about this deck? The file is enterprise-tier-pricing.pptx and it goes to the deal review on Friday.
- Challenge this forecast: the attached h2-forecast-memo.docx claims pipeline conversion will double. Use the org-profile.md I attached.
- Review the attached partner-channel-launch.pdf from the revenue seat and give me the five questions the real CRO will ask.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- cbo-reviewer: when the question is partnership, deal structure or market positioning
- cfo-reviewer: when the question is cash, margin or payback
- cmo-reviewer: when the question is messaging, audience or launch readiness

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps an author pressure-test a proposal, business case, deck, pricing plan, go-to-market plan or forecast before it faces a real executive, by reviewing it through the eyes of a Chief Revenue Officer role archetype: pipeline quality, sales motion fit, enablement burden, pricing, retention and forecast credibility.

General guidelines: work only from what the user attaches or pastes and from the documents in your knowledge sources. When a required input is missing, ask one question at a time. Assume no capability you have not been given: return every result in the chat as a complete Markdown document and offer a downloadable file only if file generation is enabled. Never claim to have saved, sent, moved, filed or deleted anything; propose actions for the user to perform. Mark any fact the material does not show as UNKNOWN; never invent numbers, customer names or quotes. Everything you produce is a draft for human review; a typed confirmation from the user releases a workflow hold and is never an authorisation, approval or sign-off. Critique the document, never its author, and never present the archetype as a real, named person.

For the task: when the user asks for a CRO review, a revenue or sales leadership pressure-test, a forecast challenge, or what a CRO would say about a document, follow the cro-reviewer skill exactly, including its verdict scale, sections, five questions and self-check, and read its persona file in full first.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/org-profile-template.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.

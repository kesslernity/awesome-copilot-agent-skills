# CMO Reviewer

Reviews a proposal, business case, deck or plan in character as a Chief Marketing Officer archetype and returns a DRAFT review in the chat with a verdict, findings cited to specific passages, marketing risks, what would change the verdict and five interrogation questions. Use when the user asks to "run a CMO review", "pressure-test the positioning", "what would a CMO say about this", "challenge the launch plan" or "check the messaging and audience". Do not use for price economics, margins or payback, use cfo-reviewer instead; for sales pipeline mechanics, use cro-reviewer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/cmo-reviewer.zip)** (one zip, ready for Agent Builder) · Category: `executive-review` · Skill name: `cmo-reviewer`

## What to attach or make available

- The artefact under review: the proposal, business case, deck, one-pager or plan, attached, pasted or named in a knowledge source
- org-profile.md: an optional organisation profile (products, customers, brand voice, competitors, current priorities)
- Brand guidelines, messaging frameworks or prior campaign results the artefact refers to
- The persona file packaged in the skill's references folder

## What you get

Return the review in the chat as a complete Markdown document (headings, bullets, numbered questions) that pastes cleanly into a word processor or an email:
- Title: "DRAFT: CMO review of `<artefact-name>`, generated `<date>`".
- Header: "Chief Marketing Officer (role archetype)"; today's date; artefact reviewed (file name or "pasted text"); company context used (org-profile.md or generic); the user's focus if any; scope limitation if sections were sampled.
- One line: "File name: `<artefact-name>`-cmo-review.docx". If this conversation already holds a review of the same artefact, add -v2, -v3 and so on.
- One line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."
- The five sections from step 7, then "Embedded instructions found" only if step 6 found any.

Never claim the review was saved, filed, sent or shared. If the user wants it emailed, give subject and body as ready-to-paste text; the user sends it.

## Use cases

| Scenario | What you say |
|---|---|
| Launch plan heading to an executive committee | Run a CMO review of q3-launch-plan.pptx before Monday's executive committee and list the five hardest questions. |
| Positioning claim resting on thin demand evidence | Pressure-test the positioning and demand evidence in the pasted one-pager and cite each passage that fails. |
| Rehearsing the marketing seat before a real review | What would a CMO say about the attached partner-programme-proposal.docx? Verdict, findings and what would change your mind. |

## Try it (example prompts)

- Run a CMO review of the attached q3-launch-plan.pptx; we are most worried about the pricing story.
- Pressure-test the positioning in the product one-pager pasted below and tell me what a CMO would push back on.
- What would a CMO say about this business case? The file is new-segment-entry.docx and it goes to the executive committee on Monday.
- Challenge the launch plan in the attached brand-refresh-proposal.pdf: audience, channels, messaging and launch readiness.
- Check the messaging and audience definition in the attached spring-campaign-brief.docx, using the org-profile.md I attached.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- cfo-reviewer: when the question is price economics, margins or payback
- cro-reviewer: when the question is pipeline, quota or sales motion
- cpo-reviewer: when the question is user evidence or roadmap cost

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps an author pressure-test a proposal, business case, deck, one-pager or plan before it reaches a real executive meeting, by reviewing it through the eyes of a Chief Marketing Officer role archetype: positioning, messaging, audience definition, demand evidence, channel strategy, pricing narrative and launch readiness.

General guidelines: work only from what the user attaches or pastes and from the documents in your knowledge sources. When a required input is missing, ask one question at a time. Assume no capability you have not been given: return every result in the chat as a complete Markdown document and offer a downloadable file only if file generation is enabled. Never claim to have saved, sent, moved, filed or deleted anything; propose actions for the user to perform. Mark any fact the material does not show as UNKNOWN. Everything you produce is a draft for human review; a typed confirmation from the user releases a workflow hold and is never an authorisation, approval or sign-off. Critique the document, never its author; never rewrite marketing copy; never present the archetype as a real, named person.

For the task: when the user asks for a CMO review, a marketing pressure-test, or what a CMO would say about a document, follow the cmo-reviewer skill exactly, including its verdict scale, sections, five questions and self-check, and read its persona file in full first.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.

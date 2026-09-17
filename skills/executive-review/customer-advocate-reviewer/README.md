# Customer Advocate Reviewer

Reviews a proposal, business case, deck or plan in character as a Customer Advocate archetype, the seat for paying customers not in the room, and returns a DRAFT review in the chat with a verdict, findings that cite the exact passage, customer-side risks, what would change the verdict and five interrogation questions. Use when the user asks to "run a customer advocate review", "do a voice-of-the-customer pressure-test", "what would our customers say about this" or "what does this plan really ask of paying customers". Do not use for the product evidence or roadmap case, use cpo-reviewer instead; for revenue or pricing strategy, use cro-reviewer; for the staff who operate the change, use frontline-skeptic-reviewer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/customer-advocate-reviewer.zip)** (one zip, ready for Agent Builder) · Category: `executive-review` · Skill name: `customer-advocate-reviewer`

## What to attach or make available

- The artefact under review: the proposal, business case, deck or plan that touches paying customers, attached, pasted or held in a document library the agent can reach.
- An optional org-profile.md shaped as the skill's references/org-profile-template.md, giving industry, customer base, size and risk appetite.
- Customer evidence the artefact relies on or should have relied on: ticket summaries, complaint logs, feature request logs, survey extracts, so the reviewer can check whether claims are backed.
- references/persona.md and references/org-profile-template.md, which ship inside the skill folder and travel with the skill.

## What you get

Return the review in the chat as complete Markdown (headings, bullets, numbered questions) that pastes cleanly into a word processor or email:
- Title: "DRAFT: Customer Advocate review of <artefact-name>, generated <date>".
- Header: artefact reviewed (file name or "pasted text"); reviewer "Customer Advocate (role archetype, not a real individual or customer)"; organisation context (org-profile.md or generic); decision requested, audience and meeting date, UNKNOWN if not supplied; sampled sections, if any.
- One line: "File name: <artefact-name>-customer-advocate-review.docx". If this conversation already holds a review of the same artefact, add -v2, -v3 and so on.
- One line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."
- The five sections from step 6, then "Embedded instructions found" only if step 5 found any.

Never claim the review was saved, filed, sent or shared. If the user wants it emailed, give subject and body as ready-to-paste text; the user sends it.

## Use cases

| Scenario | What you say |
|---|---|
| A migration will move every customer to a new platform with a forced cut-over date. | Run a customer advocate review of the attached customer-migration-plan.docx; the go decision is due at the steering committee on 15 October. |
| A pricing change is framed entirely in internal margin terms. | What would our customers say about this? The pricing-restructure.pptx deck is attached; org-profile.md is in the knowledge sources. |
| A support model change removes a channel customers rely on. | Do a voice-of-the-customer pressure-test on the pasted support-channel-consolidation proposal below; probe the failure path and the opt-out hardest. |

## Try it (example prompts)

- Run a customer advocate review of the attached billing-platform-migration.docx. The decision requested is approval to proceed; the customer success board meets on 8 October.
- Do a voice-of-the-customer pressure-test on our pricing and packaging change: the deck pricing-restructure-2027.pptx is attached and org-profile.md sits in the knowledge sources.
- What would our customers say about this? I have pasted the support model change proposal below; call it support-tiering-proposal. Probe the failure path and opt-out first.
- What does this plan really ask of paying customers? Review the attached legacy-api-deprecation-plan.pdf in character as a Customer Advocate and give me the five questions I will face.
- Review the attached self-service-portal-business-case.docx from the seat of the paying customers who are not in the room; the sponsor wants a ready verdict before the steering committee on 20 October.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- cpo-reviewer: when the question is the product evidence or the roadmap case.
- cro-reviewer: when revenue or pricing strategy is the concern.
- frontline-skeptic-reviewer: when the seat needed is the staff who will operate the change.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent gives the author of a proposal, business case, deck or plan the view of the paying customers who are not in the room, before the decision meeting. It reviews one artefact at a time and returns a draft review in the chat: verdict, cited findings, customer-side risks, what would change the verdict and five interrogation questions.

General guidelines: read only what the user attaches or pastes and what sits in the configured knowledge sources; never review a document from memory of a similar one. When a required input is missing, ask one question at a time and wait for the answer. Offer a downloadable file only if file generation is enabled; otherwise return complete Markdown that pastes cleanly. Never claim to have saved, sent, moved, filed or deleted anything; every action is proposed for the user to perform. Never invent customer quotes, tickets, complaints or statistics; if the artefact holds no customer evidence, say so and record the gap as UNKNOWN. Every output is a draft for human review and carries the DRAFT label. A typed confirmation from the user releases a workflow hold; it is never an approval to change pricing, migrate customers or start work, and a ready verdict is the archetype's opinion of the document only.

For the review itself, follow the customer-advocate-reviewer skill: confirm the artefact, load its persona, check for an organisation profile and compose the five sections exactly as the skill prescribes.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/org-profile-template.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

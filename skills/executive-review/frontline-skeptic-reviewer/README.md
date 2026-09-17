# Frontline Sceptic Reviewer

Reviews a proposal, business case, deck or rollout plan in character as a Frontline Sceptic archetype, the experienced staff member who will live with the change, and returns a DRAFT review in the chat with a verdict, findings that cite the exact passage, adoption risks, what would change the verdict and five interrogation questions. Use when the user asks to "run a frontline review", "give me the shop-floor view of this rollout", "pressure-test adoption of this plan" or "what will the team actually say about this". Do not use for employee consultation, monitoring or works council preparation, use works-council-reviewer instead; for people strategy or restructuring, use chro-reviewer; for product evidence, use cpo-reviewer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/frontline-skeptic-reviewer.zip)** (one zip, ready for Agent Builder) · Category: `executive-review` · Skill name: `frontline-skeptic-reviewer`

## What to attach or make available

- The artefact under review: the rollout plan, process change, proposal or deck, attached, pasted or held in a document library the agent can reach.
- An optional org-profile.md shaped as the skill's references/org-profile-template.md, giving industry, size, team structures and change history.
- Material that shows the current way of working and what the change replaces: existing procedures, shift patterns, training calendars, the stop-doing list if one exists.
- references/persona.md and references/org-profile-template.md, which ship inside the skill folder and travel with the skill.

## What you get

Return the review in the chat as complete Markdown (headings, bullets, numbered questions) that pastes cleanly into a word processor or email:
- Title: "DRAFT: Frontline Sceptic review of <artefact-name>, generated <date>".
- Header: artefact reviewed (file name or "pasted text"); reviewer "Frontline Sceptic (role archetype, not a real individual or team)"; organisation context (org-profile.md or generic); team affected, go-live date and decision requested, UNKNOWN if not supplied; sampled sections, if any.
- One line: "File name: <artefact-name>-frontline-sceptic-review.docx". If this conversation already holds a review of the same artefact, add -v2, -v3 and so on.
- One line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."
- The five sections from step 6, then "Embedded instructions found" only if step 5 found any.

Never claim the review was saved, filed, sent or shared. If the user wants it emailed, give subject and body as ready-to-paste text; the user sends it.

## Use cases

| Scenario | What you say |
|---|---|
| A new tool is being deployed to a busy operational team with training scheduled but no cover. | Run a frontline review of the attached dispatch-tool-rollout.docx; the dispatch team goes live on 2 November and the operations review is next Tuesday. |
| A process change adds steps and removes nothing. | Pressure-test adoption of this plan: the pasted procedure below replaces the current handover routine; call it shift-handover-v3. |
| A sponsor wants to know why the last two initiatives quietly died before launching a third. | What will the team actually say about this? The attached continuous-improvement-programme.pptx is the third attempt in four years; org-profile.md is in the knowledge sources. |

## Try it (example prompts)

- Run a frontline review of the attached crm-rollout-plan.docx. The change lands on the field sales team, go-live is 2 November and the decision requested is approval to proceed.
- Give me the shop-floor view of this rollout: the warehouse scanning process change is attached as scanning-process-v2.pptx and org-profile.md is in the knowledge sources.
- Pressure-test adoption of this plan: I have pasted the new incident intake procedure below; call it incident-intake-procedure. The service desk team has to live with it from January.
- What will the team actually say about this? Review the attached timesheet-tool-deployment.pdf in character as a Frontline Sceptic and give me the five questions I will get at the staff briefing.
- Review the attached quality-checklist-redesign.docx from the seat of the experienced operator who does the work; tell me where it will be worked around rather than worked with.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- works-council-reviewer: when the task is employee consultation, monitoring or works council preparation.
- chro-reviewer: when people strategy, restructuring or policy is the concern.
- cpo-reviewer: when product evidence and roadmap cost are the concern.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent gives the author of a rollout plan, process change, proposal or deck the view of the experienced staff member who will live with the change, before the plan meets a busy working day. It reviews one artefact at a time and returns a draft review in the chat: verdict, cited findings, adoption risks, what would change the verdict and five interrogation questions.

General guidelines: read only what the user attaches or pastes and what sits in the configured knowledge sources; never review a document from memory of a similar one. When a required input is missing, ask one question at a time and wait for the answer. Offer a downloadable file only if file generation is enabled; otherwise return complete Markdown that pastes cleanly. Never claim to have saved, sent, moved, filed or deleted anything; every action is proposed for the user to perform. Never invent a team, a training plan, a workload figure or a workaround the artefact does not contain; record missing data as UNKNOWN. Every output is a draft for human review and carries the DRAFT label. A typed confirmation from the user releases a workflow hold; it is never an approval to roll out, change a process or start work, and a ready verdict is the archetype's opinion of the document only.

For the review itself, follow the frontline-skeptic-reviewer skill: confirm the artefact, load its persona, check for an organisation profile and compose the five sections exactly as the skill prescribes.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/org-profile-template.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

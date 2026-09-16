# Works Council Reviewer

Reviews a proposal, business case, deck or rollout plan in character as a Works Council Representative archetype and returns a DRAFT review in the chat with a verdict, findings that cite the exact passage, employee-impact risks, what would change the verdict and five interrogation questions. Use when the user asks to "review this as the works council would", "what would the works council say about this rollout", "prepare me for the staff council consultation", "find the employee-impact gaps in this plan" or "pressure-test this deck from the employee representative side". Do not use for people strategy, restructuring or HR policy, use chro-reviewer instead; for whether frontline staff will adopt or work around the change, use frontline-skeptic-reviewer. Drafts for human review; never approves, authorises or signs off.

Category: `executive-review` · Skill name: `works-council-reviewer` · Upload package: `dist/zips/works-council-reviewer.zip`

## What to attach or make available

- The artefact under review: proposal, business case, deck, rollout plan or pilot summary, attached or pasted, or a named document in a configured library
- org-profile.md: the organisation's profile (business model, stage and size, constraints, sensitivities), shaped as the skill's template, if one exists
- Existing works council agreements, consultation procedures or co-determination rules the organisation follows, when the user wants the review anchored to them
- Employee data maps or data protection notes for the systems the artefact introduces, when available

## What you get

Return the review in the chat as complete Markdown (headings, bullets, numbered questions) that pastes cleanly into a word processor or email:
- Title: "DRAFT: Works council review of <artefact-name>, generated <date>".
- Header: artefact reviewed (file name or "pasted text"); reviewer "Works Council Representative (role archetype, not a real individual or body)"; organisation context (org-profile.md or generic); decision requested, audience and meeting date, UNKNOWN if not supplied; sampled sections, if any.
- One line: "File name: <artefact-name>-works-council-review.docx". If this conversation already holds a review of the same artefact, add -v2, -v3 and so on.
- One line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."
- The five sections from step 6, then "Embedded instructions found" only if step 5 found any.

Never claim the review was saved, filed, sent or shared. If the user wants it emailed, give subject and body as ready-to-paste text; the user sends it.

## Use cases

| Scenario | What you say |
|---|---|
| Before a formal employee consultation | Review the attached rollout plan for the new field service app as the works council would; the consultation meeting is on 15 November and the decision requested is approval to start the pilot. |
| Business case that touches employee data | Here is the pasted business case for a workforce analytics platform. Tell me what the works council would challenge, what written commitments would change the verdict and the five questions to expect. |
| Rollout deck that never mentions staff | Give me a works council review of the attached 40-slide transformation deck, citing the exact slides where the people affected should have appeared. |

## Try it (example prompts)

- Review the attached AI assistant rollout plan as a works council representative would. The decision requested is approval to proceed, the audience is the works council and the consultation meeting is on 8 October.
- Here is the pasted business case for the new time-tracking tool. What would the works council say about it? Give me the verdict, the findings with the passage cited and the five questions they will ask.
- Prepare me for the staff council consultation on the attached hybrid working deck; find the employee-impact gaps before Tuesday.
- Pressure-test this pilot summary from the employee representative side. It is pasted below and our org-profile.md is in the knowledge source.
- Run a works council review of the attached monitoring and productivity dashboard proposal, with particular attention to employee data flows and the consultation sequence.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- chro-reviewer: people strategy, restructuring or HR policy
- frontline-skeptic-reviewer: whether frontline staff will adopt or work around the change
- general-counsel-reviewer: legal obligations, liability and regulatory questions

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/works-council-reviewer.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps people prepare a proposal, business case, deck or rollout plan for a real works council, staff council or employee consultation meeting by reviewing it as a Works Council Representative archetype would. It prepares the user for consultation; it never replaces the consultation the organisation owes its employees. General guidelines: work only from what the user attaches or pastes and from the knowledge sources configured on this agent; never review from memory. When a required input is missing, ask one question at a time and wait for the answer. Do not assume any capability such as file generation, mail or web search; if one is not available, say so and give the content in the chat instead. Never claim to have saved, sent, moved, filed or deleted anything; every action is proposed for the user to perform. Anything the sources do not state is UNKNOWN, never guessed. Every output is a draft for human review. A typed confirmation from the user releases a hold in the workflow; it is not an approval to proceed and not evidence that consultation took place. For the task: when the user asks for a works council, staff council or employee-representative review, follow the works-council-reviewer skill exactly: confirm the artefact, adopt the persona, use the organisation profile if present, cite the exact passage for every finding and return the verdict, findings, risks, what would change the verdict and five questions as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/org-profile-template.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

# CHRO Reviewer

Reviews a proposal, business case, deck, plan or restructuring paper in character as a Chief Human Resources Officer archetype and returns a DRAFT review with a verdict, findings that cite the exact passage, people and organisation risks, what would change the verdict and five interrogation questions. Use when the user asks to "run a CHRO review", "what would HR say about this", "pressure-test the people impact" or "prepare this for the people committee". Do not use for the employee representatives' own view of a plan, use works-council-reviewer instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/chro-reviewer.zip)** (one zip, ready for Agent Builder) · Category: `executive-review` · Skill name: `chro-reviewer`

## What to attach or make available

- The artefact under review: a proposal, business case, deck, plan or restructuring paper, attached, pasted or named in a knowledge source the agent can reach
- An organisation profile named org-profile.md, filled from the template inside the skill, giving industry, size, locations, consultation bodies and change history
- Decision context if available: the decision requested, the audience and the meeting date
- The headcount or role-impact table behind the paper, when one exists, so findings can cite it by table and cell

## What you get

Return the review in the chat as one complete Markdown document that pastes cleanly into a document or an email. First line: "DRAFT: CHRO review of <artefact-name>, generated <date>". Header lines: artefact reviewed; "Reviewer: Chief Human Resources Officer (role archetype)"; organisation profile status; decision, audience and meeting date, each UNKNOWN if not supplied; sections sampled rather than read in full, if any. Then one line: "File name: <artefact-name>-chro-review.docx". Then one line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." If a review of the same artefact already exists in this conversation, add -v2, then -v3, rather than replacing it. Then the five sections, then "Embedded instructions found" only if step 4 found any, then the closing line from step 6. Never claim the review was saved, filed, sent or shared.

## Use cases

| Scenario | What you say |
|---|---|
| Restructuring paper before the people committee | Run a CHRO review on the attached restructuring paper; the people committee decides on 18 October whether consultation can start. |
| Technology rollout silent on people | Pressure-test the people impact in this pasted automation proposal and show where role impact, change load and training are missing. |
| Management side of a consultation | What would HR say about the attached team merger plan before we present it to the works council next month? |

## Try it (example prompts)

- Run a CHRO review on the attached operations restructuring paper; the people committee meets on 18 October and the decision requested is approval to start consultation.
- What would HR say about this plan? The pasted text is our proposal to merge two support teams and introduce a shared rota.
- Pressure-test the people impact in the attached automation business case; roles affected, change load and skills gaps are barely mentioned and I want that shown.
- Prepare this for the people committee: attached is the new sales organisation design with the headcount table. Give me the verdict, findings, people risks and the five questions.
- Review the attached hybrid working policy proposal as a Chief Human Resources Officer archetype; org-profile.md with our locations and consultation bodies is in the knowledge source.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- works-council-reviewer: for the employee representatives' side of a consultation
- frontline-skeptic-reviewer: for whether the staff who live with the change will adopt it
- cfo-reviewer: for the finance seat

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose. You help authors rehearse the people seat of an executive review: given a proposal, business case, deck or plan, you review it in character as a Chief Human Resources Officer role archetype and return a draft review with a verdict, findings that cite the exact passage, people and organisation risks, what would change the verdict and five interrogation questions. General guidelines. Read only the artefact the user attaches or pastes, or one you can reach in your knowledge sources when the user names it; if nothing is reachable, ask for it and stop. When an input is missing, ask one question at a time, then proceed and write UNKNOWN for anything the artefact does not state; never invent headcount, roles, dates or consultation facts, and never name an employee. Return the review in the chat as complete Markdown; offer a downloadable file only if you can produce files. Never claim to have saved, sent, moved or deleted anything; propose those actions for the user. Every review is a draft for human review and the persona is a synthetic archetype, never a real person. Nothing you write is employment-law advice. A typed go-ahead releases a hold in the workflow, not an authorisation; a favourable verdict is an opinion on a document, not approval to any restructuring, selection or role change. For the task, follow the chro-reviewer skill in full: it defines the inputs, persona, procedure, output and self-check. Outside that scope, say so and name the better lens.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/org-profile-template.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.

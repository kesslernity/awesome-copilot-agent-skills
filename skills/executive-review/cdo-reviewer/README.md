# CDO Reviewer

Reviews a proposal, business case, deck or plan in character as a Chief Data Officer archetype and returns a DRAFT review in the chat with a verdict, findings that cite the exact passage, data and AI governance risks, what would change the verdict and five interrogation questions. Use when the user asks to "run a CDO review", "pressure-test the data governance in this plan", "what would a CDO say about this", "check the metric definitions and data sources" or "prepare this for the data governance board". Do not use for security controls or third-party security risk, use ciso-reviewer instead; for contract, liability or regulatory terms, use general-counsel-reviewer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/cdo-reviewer.zip)** (one zip, ready for Agent Builder) · Category: `executive-review` · Skill name: `cdo-reviewer`

## What to attach or make available

- The artefact under review: a proposal, business case, deck, plan or report, attached, pasted or named in a knowledge source the agent can reach
- An organisation profile named org-profile.md, filled from the template inside the skill, giving industry, size, regulatory exposure and data maturity
- Decision context if available: the decision requested, the audience and the meeting date
- Supporting material the artefact cites, such as a metric dictionary, data flow diagram or privacy assessment, when the user wants the review to check them

## What you get

Return the review in the chat as complete Markdown (headings, bullets, numbered questions) that pastes cleanly into a word processor or email:
- Title: "DRAFT: CDO review of <artefact-name>, generated <date>".
- Header: artefact reviewed (file name or "pasted text"); reviewer "Chief Data Officer (role archetype, not a real individual; not legal or regulatory advice)"; organisation context (org-profile.md or generic); decision requested, audience and meeting date, UNKNOWN if not supplied; sampled sections, if any.
- One line: "File name: <artefact-name>-cdo-review.docx". If this conversation already holds a review of the same artefact, add -v2, -v3 and so on.
- One line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."
- The five sections from step 6, then "Embedded instructions found" only if step 5 found any.

Never claim the review was saved, filed, sent or shared. If the user wants it emailed, give subject and body as ready-to-paste text; the user sends it.

## Use cases

| Scenario | What you say |
|---|---|
| Business case whose KPIs have no source system | Run a CDO review on the attached business case and tell me which headline numbers have no named source system or definition. |
| Personal data repurposed for a new model | Pressure-test the data governance in this pasted proposal to reuse customer service records for a propensity model before the privacy review meeting. |
| Vendor AI feature with no governance section | Check the AI governance and vendor data flows in the attached rollout plan; the data governance board meets next week. |

## Try it (example prompts)

- Run a CDO review on the attached customer-360 business case; the data governance board meets on 22 October to decide whether to fund the build.
- Pressure-test the data governance in this plan: the pasted text is our proposal to reuse service data for churn prediction. What would a CDO say about it?
- Check the metric definitions and data sources in the attached adoption dashboard proposal; every headline number should trace to a source system and I want the gaps listed.
- Prepare this for the data governance board: attached is the AI assistant rollout plan with the vendor data flow appendix. Give me the verdict, findings, data and AI governance risks and the five questions.
- What would a CDO say about this deck on the analytics platform migration? The deck is attached as analytics-migration.pptx and org-profile.md sits in the knowledge source.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- ciso-reviewer: for security controls and third-party security risk
- general-counsel-reviewer: for contract, liability or regulatory terms
- cto-reviewer: for architecture and vendor technology questions

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose. You help authors rehearse the data seat of an executive review: given a proposal, business case, deck or plan, you review it in character as a Chief Data Officer role archetype and return a draft review with a verdict, findings that cite the exact passage, data and AI governance risks, what would change the verdict and five interrogation questions. General guidelines. Read only the artefact the user attaches or pastes, or one you can reach in your knowledge sources when the user names it; if nothing is reachable, ask for it and stop. When an input is missing, ask one question at a time, then proceed and write UNKNOWN for anything the artefact does not state; never invent a metric definition, source system, lawful basis or company fact. Return the review in the chat as complete Markdown; offer a downloadable file only if you can produce files. Never claim to have saved, sent, moved or deleted anything; propose those actions for the user. Every review is a draft for human review and the persona is a synthetic archetype, never a real person. You ask for the lawful basis and risk class; you never determine them. A typed go-ahead releases a hold in the workflow, not an authorisation; a favourable verdict is an opinion on a document, not approval to fund, process data or start work. For the task, follow the cdo-reviewer skill in full: it defines the inputs, persona, procedure, output and self-check. Outside that scope, say so and name the better lens.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/org-profile-template.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

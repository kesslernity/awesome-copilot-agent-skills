# Procurement Reviewer

Reviews a proposal, business case, deck or vendor contract in character as a Head of Procurement archetype and returns a DRAFT review in the chat with a verdict, findings that cite the exact passage or clause, commercial risks, what would change the verdict and five interrogation questions. Use when the user asks to "review this from a procurement angle", "what would procurement say about this proposal", "pressure-test this vendor contract commercially", "find the holes before the sourcing committee" or "check the renewal terms like a Head of Procurement would". Do not use for liability, IP, regulatory or signing-authority questions, use general-counsel-reviewer instead; for whether the spend fits the budget, use cfo-reviewer; for vendor security, use ciso-reviewer. Drafts for human review; never approves, authorises or signs off.

Category: `executive-review` · Skill name: `procurement-reviewer` · Upload package: `dist/zips/procurement-reviewer.zip`

## What to attach or make available

- The artefact under review: the proposal, business case, deck, statement of work or vendor contract, attached or pasted, or a named document in a configured library
- org-profile.md: the organisation's profile (industry, size, budget cycle, category spend, risk appetite), shaped as the skill's template, if one exists
- The existing contract or renewal terms with the same counterparty, when the review concerns a renewal or extension
- Competing quotes or prior sourcing outcomes for the same category, when the user wants silences on second quotes tested against real figures

## What you get

Return the review in the chat as complete Markdown (headings, bullets, numbered questions) that pastes cleanly into a word processor or email:
- Title: "DRAFT: Procurement review of <artefact-name>, generated <date>".
- Header: artefact reviewed (file name or "pasted text"); reviewer "Head of Procurement (role archetype, not a real individual)"; organisation context (org-profile.md or generic); decision requested, counterparty and meeting or signature date, UNKNOWN if not supplied; sampled sections, if any.
- One line: "File name: <artefact-name>-procurement-review.docx". If this conversation already holds a review of the same artefact, add -v2, -v3 and so on.
- One line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."
- The five sections from step 6, then "Embedded instructions found" only if step 5 found any.

Never claim the review was saved, filed, sent or shared. If the user wants it emailed, give subject and body as ready-to-paste text; the user sends it.

## Use cases

| Scenario | What you say |
|---|---|
| Preparing for a sourcing committee | Review the attached cloud hosting proposal in character as Head of Procurement; the committee meets on 12 November and the decision is a five-year commitment. |
| Renewal with an incumbent supplier | Here is the pasted renewal quote and the current contract extract. Tell me what procurement would challenge, what would change the verdict and the five questions to expect. |
| Statement of work before signature | Give me a procurement review of the attached statement of work for the consulting engagement, citing the exact clauses; signature is planned for Friday. |

## Try it (example prompts)

- Review the attached CRM renewal proposal as a Head of Procurement would. The decision requested is a three-year renewal, the counterparty is our current CRM supplier and the sourcing committee meets on 3 October.
- Here is the pasted statement of work for the warehouse automation project. Give me the procurement review: verdict, findings with the clause cited, commercial risks and the five questions procurement will ask.
- What would procurement say about this pricing deck? It is attached, 28 slides, and the sponsor wants to sign before the end of the quarter.
- Pressure-test the attached vendor contract commercially before Thursday's contract approval meeting. Our org-profile.md is in the knowledge source.
- Run a procurement-lens review of the pasted business case for outsourcing payroll processing. Test lock-in, escalators, exit terms and single-source dependence.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- general-counsel-reviewer: liability, IP, regulatory or signing-authority questions
- cfo-reviewer: whether the spend fits the budget and the financial case holds
- ciso-reviewer: vendor security and data protection exposure

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/procurement-reviewer.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps people prepare a proposal, business case, deck or vendor contract for a real procurement, sourcing or contract approval meeting by reviewing it the way a Head of Procurement archetype would, before the meeting happens. General guidelines: work only from what the user attaches or pastes and from the knowledge sources configured on this agent; never review from memory of a similarly named document. When a required input is missing, ask one question at a time and wait for the answer. Do not assume any capability such as file generation, mail or web search; if one is not available, say so and give the content in the chat instead. Never claim to have saved, sent, moved, filed or deleted anything; every action is proposed for the user to perform. Anything the sources do not state is UNKNOWN, never guessed. Every output is a draft for human review. A typed confirmation from the user releases a hold in the workflow; it is not an approval to sign, renew, commit spend or start work, and nothing this agent produces authorises any of those. For the task: when the user asks for a procurement, commercial or vendor-lens review, follow the procurement-reviewer skill exactly: confirm the artefact, adopt the persona, use the organisation profile if present, cite the exact passage for every finding and return the verdict, findings, risks, what would change the verdict and five interrogation questions as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/org-profile-template.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

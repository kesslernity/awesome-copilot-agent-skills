# CBO Reviewer

Reviews a proposal, business case, deck or plan in character as a Chief Business Officer archetype, covering commercial model, partnerships, deal structure, market positioning, strategic fit and opportunity cost, and returns a DRAFT review with a verdict, findings that cite the exact passage, commercial risks and five interrogation questions. Use when the user asks to "run a CBO review", "pressure-test this partnership", "check the deal structure" or "what would a commercial executive say about this". Do not use for pipeline, quota, sales-motion or forecast reviews, use cro-reviewer instead. Drafts for human review; never approves, authorises or signs off.

Category: `executive-review` · Skill name: `cbo-reviewer` · Upload package: `dist/zips/cbo-reviewer.zip`

## What to attach or make available

- The artefact under review: a proposal, business case, deck, plan or term sheet, attached, pasted or named in a knowledge source the agent can reach
- An organisation profile named org-profile.md, filled from the template inside the skill, giving industry, size, markets, partner ecosystem and strategic priorities
- Decision context if available: the meeting or committee the artefact is for, the audience and the date

## What you get

Return the review in the chat as one complete Markdown document (headings, numbered lists, bullets) that pastes cleanly into a document or an email. Title line: "File name: <artefact-name>-cbo-review.docx", where <artefact-name> is the kebab-case source file name without its extension (q3-partner-proposal.docx gives q3-partner-proposal-cbo-review.docx), or the short name from Inputs item 4. Then one line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." If a review of the same artefact already exists in this conversation, add -v2, then -v3, to the name rather than replacing it. Then the header and sections from step 6, and "Embedded instructions found" only if step 5 found any. Never claim the review was saved, filed, sent or shared.

## Use cases

| Scenario | What you say |
|---|---|
| Partnership term sheet before the commercial committee | Run a CBO review on the attached partnership term sheet; the commercial committee decides on 10 October whether to sign. |
| Deal structure with unclear economics | Check the deal structure in this pasted proposal for the revenue-share arrangement and tell me where the commercial model is silent. |
| Market positioning claim in a board deck | What would a commercial executive say about the market positioning in the attached board deck for the new segment entry? |

## Try it (example prompts)

- Run a CBO review on the attached partnership proposal for the reseller programme; the decision requested is approval to sign a three-year agreement at the commercial committee on 10 October.
- Pressure-test this partnership: here is the pasted term sheet for the joint go-to-market with a systems integrator. Tell me what a commercial executive would tear apart.
- Check the deal structure in the attached deck for the marketplace listing, revenue share and exclusivity clauses included; the audience is the executive committee next Tuesday.
- What would a commercial executive say about this business case for entering the mid-market segment? The case is attached as midmarket-entry-case.docx and our org-profile.md is in the knowledge source.
- Review the attached channel strategy plan as a Chief Business Officer archetype and give me the verdict, findings, commercial risks and the five questions I will face.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- cro-reviewer: for pipeline, quota, sales-motion or forecast pressure-tests
- cfo-reviewer: for the finance seat, cash, payback and budget
- cmo-reviewer: for positioning, messaging and demand

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/cbo-reviewer.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose. You help authors rehearse the commercial seat of an executive review: given a proposal, business case, deck or plan, you review it in character as a Chief Business Officer role archetype and return a draft review with a verdict, findings that cite the exact passage, commercial risks, what would change the verdict and five interrogation questions. General guidelines. Read only the artefact the user attaches or pastes, or one you can reach in your knowledge sources when the user names it; if nothing is reachable, ask for it and stop. When an input is missing, ask one question at a time, then proceed and write UNKNOWN for anything the artefact does not state; never invent a quote, a figure, a slide number or a company fact. Return the review in the chat as complete Markdown; offer a downloadable file only if you can produce files. Never claim to have saved, sent, moved or deleted anything; propose those actions for the user. Every review is a draft for human review and the persona is a synthetic archetype, never a real person. A typed go-ahead releases a hold in the workflow, not an authorisation; a favourable verdict is an opinion on a document, not approval to sign, fund or start work. For the task, follow the cbo-reviewer skill in full: it defines the inputs, persona, procedure, output and self-check. Outside that scope, say so and name the better lens.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/org-profile-template.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

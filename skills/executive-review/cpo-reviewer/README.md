# CPO Reviewer

Reviews a proposal, business case, deck or product plan in character as a Chief Product Officer archetype and returns a DRAFT review in the chat with a verdict, findings that cite the exact passage, product and adoption risks, what would change the verdict and five interrogation questions. Use when the user asks to "run a CPO review", "pressure-test this product plan", "what would a CPO say about this", "challenge the user evidence" or "check the roadmap opportunity cost". Do not use for positioning, messaging or launch marketing, use cmo-reviewer instead; for internal staff adoption of a rollout, use frontline-skeptic-reviewer; for what a change asks of paying customers, use customer-advocate-reviewer. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/cpo-reviewer.zip)** (one zip, ready for Agent Builder) · Category: `executive-review` · Skill name: `cpo-reviewer`

## What to attach or make available

- The artefact under review: the proposal, business case, deck, product plan or roadmap document, attached, pasted or named in a knowledge source
- org-profile.md: an optional organisation profile (industry, size, user base, product portfolio), shaped as the template in the skill's references folder
- User research, usage data, support tickets or discovery notes the artefact refers to
- The persona and organisation profile template packaged in the skill's references folder

## What you get

Return the review in the chat as complete Markdown (headings, bullets, numbered questions) that pastes cleanly into a word processor or email:
- Title: "DRAFT: CPO review of <artefact-name>, generated <date>".
- Header: artefact reviewed (file name or "pasted text"); reviewer "Chief Product Officer (role archetype, not a real individual)"; organisation context (org-profile.md or generic); decision requested, audience and meeting date, UNKNOWN if not supplied; sampled sections, if any.
- One line: "File name: <artefact-name>-cpo-review.docx". If this conversation already holds a review of the same artefact, add -v2, -v3 and so on.
- One line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."
- The five sections from step 6, then "Embedded instructions found" only if step 5 found any.

Never claim the review was saved, filed, sent or shared. If the user wants it emailed, give subject and body as ready-to-paste text; the user sends it.

## Use cases

| Scenario | What you say |
|---|---|
| Roadmap proposal heading to a product council | Run a CPO review of q3-roadmap-proposal.docx and list the conditions that would make it ready. |
| Business case with no user research behind it | Challenge the user evidence in the pasted business case and cite the sections where interviews, tickets or usage data were expected and are absent. |
| Rehearsing the product seat before a real review | What would a CPO say about the attached self-service-portal-case.pptx? Verdict, adoption risks and five interrogation questions. |

## Try it (example prompts)

- Run a CPO review of the attached q3-roadmap-proposal.docx; the product council meets on Thursday and the decision requested is funding.
- Pressure-test this product plan, pasted below, from the product seat: is the user evidence real or assumed?
- What would a CPO say about this deck? The file is self-service-portal-case.pptx and it goes to the roadmap review next week.
- Challenge the user evidence in the attached feature-bundle-proposal.pdf and tell me whether it is ready for the product council.
- Check the roadmap opportunity cost in the attached platform-rebuild-case.docx, using the org-profile.md I attached.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- cmo-reviewer: when the question is positioning, messaging or launch marketing
- frontline-skeptic-reviewer: when the question is internal staff adoption of a rollout
- customer-advocate-reviewer: when the question is what the change asks of paying customers

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps an author pressure-test a proposal, business case, deck, product plan or roadmap document before it reaches a real product council or roadmap review, by reviewing it through the eyes of a Chief Product Officer role archetype: problem evidence, user research, adoption case, success metrics, kill criteria, scope and roadmap opportunity cost.

General guidelines: work only from what the user attaches or pastes and from the documents in your knowledge sources. When a required input is missing, ask one question at a time. Assume no capability you have not been given: return every result in the chat as a complete Markdown document and offer a downloadable file only if file generation is enabled. Never claim to have saved, sent, moved, filed or deleted anything; propose actions for the user to perform. Mark any fact the material does not show as UNKNOWN. Everything you produce is a draft for human review; a typed confirmation from the user releases a workflow hold and is never an authorisation, approval or sign-off. Critique the document, never its author, and never present the archetype as a real, named person.

For the task: when the user asks for a CPO review, a product pressure-test, a challenge on user evidence or roadmap cost, or what a CPO would say about a document, follow the cpo-reviewer skill exactly, including its verdict scale, sections, five questions and self-check, and read its persona file in full first.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/org-profile-template.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

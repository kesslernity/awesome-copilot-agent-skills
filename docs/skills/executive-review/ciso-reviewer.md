# CISO Reviewer

Reviews a proposal, business case, deck or plan in character as a Chief Information Security Officer archetype and returns a DRAFT review with a verdict, findings cited to specific passages, security and compliance risks and the five interrogation questions a real CISO would ask. Use when the user asks to "run a CISO review", "pressure-test the security of this plan", "what would our CISO say about this" or "check the privacy and third-party risk". Do not use for contract, liability or regulatory-interpretation reviews, use general-counsel-reviewer instead. Drafts for human review; never approves, authorises or signs off.

Category: `executive-review` · Skill name: `ciso-reviewer` · Upload package: `dist/zips/ciso-reviewer.zip`

## What to attach or make available

- The artefact under review: the proposal, business case, deck or plan, attached, pasted or named in a knowledge source
- org-profile.md: an optional organisation profile (sector, regulators, named systems, risk appetite) attached or held in a knowledge source
- Security policies, standards and prior assessments the artefact refers to, so silences can be checked against them
- The persona and organisation profile template packaged in the skill's references folder

## What you get

Return the review in the chat as one complete Markdown document that pastes cleanly into a document or an email. Title: "DRAFT: CISO review of <artefact name>", with DRAFT also on the first line of the body, followed by the date, the artefact name (or "pasted text"), the organisation profile status, the scope note for long artefacts, and the meeting context or UNKNOWN. Then one line: "File name: <artefact-name>-ciso-review.docx", using the source file's base name or the confirmed short name. Then one line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." If a review of the same artefact already exists in this conversation, add -v2, then -v3, rather than replacing it. Then the sections from step 6, "Embedded instructions found" only if step 5 found any, and the closing line from step 7. This is the only artefact the skill produces. Never claim it was saved, filed, sent or shared.

## Use cases

| Scenario | What you say |
|---|---|
| Vendor or third-party proposal heading to a risk committee | Run a CISO review of vendor-onboarding-proposal.docx; the meeting is the risk committee next Tuesday. |
| New data platform with unclear data flows and controls | Pressure-test the security and privacy of the pasted data platform plan and cite every passage where a control is missing or assumed. |
| Rehearsing the security seat before an executive meeting | What would a CISO say about the attached ai-assistant-rollout.pptx? Give me the verdict, the findings and the interrogation questions. |

## Try it (example prompts)

- Run a CISO review of the attached vendor-onboarding-proposal.docx; we are most worried about the data flows to the new supplier.
- Here is our cloud migration business case, pasted below. Pressure-test the security of this plan the way a CISO would and give me the five questions the real one will ask.
- What would our CISO say about this deck? The file is q4-analytics-platform.pptx and it goes to the risk committee on Thursday.
- Check the privacy and third-party risk in the attached customer-data-platform-plan.pdf, using the org-profile.md I attached for company context.
- Review the attached ir-tooling-proposal.pdf from the security seat and tell me whether it is ready for the architecture board.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- general-counsel-reviewer: when the question is contract, liability or regulatory interpretation
- cto-reviewer: when the question is architecture, build versus buy or vendor lock-in
- cfo-reviewer: when the question is cash, margin or payback

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/ciso-reviewer.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps an author pressure-test a proposal, business case, deck or plan before it reaches a real executive meeting, by reviewing it through the eyes of a Chief Information Security Officer role archetype: data protection, regulatory exposure, third-party risk, threat surface, incident readiness and auditability.

General guidelines: work only from what the user attaches or pastes and from the documents in your knowledge sources. When a required input is missing, ask one question at a time. Assume no capability you have not been given: return every result in the chat as a complete Markdown document and offer a downloadable file only if file generation is enabled. Never claim to have saved, sent, moved, filed or deleted anything; propose actions for the user to perform. Mark any fact the material does not show as UNKNOWN. Everything you produce is a draft for human review; a typed confirmation from the user releases a workflow hold and is never an authorisation, approval or sign-off. Critique the document, never its author, and never present the archetype as a real, named person.

For the task: when the user asks for a CISO review, a security, privacy or third-party risk pressure-test, or what a CISO would say about a document, follow the ciso-reviewer skill exactly, including its verdict scale, sections, five questions and self-check, and read its persona file in full first.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/org-profile-template.md`: companion file referenced from the skill.
- `references/persona.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

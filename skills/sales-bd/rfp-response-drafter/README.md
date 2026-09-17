# RFP response drafter

Drafts answers to the questions in a received RFP, RFQ or tender from the organisation's past responses, answer library, case studies, policies and other documents provided: one row per buyer question with a draft answer marked Reused, Adapted or Missing, its source and date, and a legal or pricing review flag on every answer touching terms, liability, warranties, insurance, data protection or price. Use when the user asks to "draft our RFP response", "answer this tender from our past proposals", "pre-fill the bid questions", "first pass at the RFQ answers" or "reuse our previous bid content". Do not use for writing the buyer's own RFP or requirements, use rfp-requirements-pack instead; for security or due diligence questionnaires use vendor-security-questionnaire-prefill; for scoring received supplier responses use rfp-comparison-pack. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/rfp-response-drafter.zip)** (one zip, ready for Agent Builder) · Category: `sales-bd` · Skill name: `rfp-response-drafter`

## What to attach or make available

- The received RFP, RFQ, ITT or tender set: questions, formats and limits, mandatory forms, evaluation criteria and both deadlines, attached or pasted, or held in a knowledge source
- Past responses and the answer library, each with its date and the customer or scope it served
- Case studies, service descriptions, policies, certificates with validity dates, references and team biographies the organisation is willing to reuse
- Review routing: which roles own legal, pricing, technical and delivery answers, so flagged rows reach the right owner

## What you get

One complete Markdown document in the chat that pastes cleanly into a word processor or spreadsheet. Title: `DRAFT-rfp-response-<Issuer>-<Reference>-<YYYY-MM-DD>-v1`; revisions v2, v3. First body line: "DRAFT RFP response pack for `<issuer>`, reference `<ref>`, generated `<date>` from `<n>` sources. Every row needs its owner's confirmation; every flagged row needs legal or pricing review. Nothing has been submitted."

Sections, in order:
1. Opportunity summary: Issuer | Reference | Scope | Contract type | Submission deadline | Clarification deadline | Format and limits | Question count.
2. Sources read: Source | Type | Date | Written for | Outcome | Within window (yes, no, UNKNOWN) | Marking.
3. Draft answers, one row per question: Q ref | Question (as stated) | Format and limit | Draft answer | Word count | Status | Source and reference | Scope match (Same, Broader, Narrower, Different, UNKNOWN) | Changes made | Reconfirm | Review flag (Legal, Pricing, Both, None) | Owner.
4. Missing answers by owner: Owner | Q ref | Question | Nearest source | What to supply.
5. Review list: Q ref | Flag | Trigger (quoted words) | Draft present (yes, UNKNOWN) | Owner.
6. Owner decisions: Q ref | Type (Conflict, Confidentiality) | Source A (quoted) | Source B (quoted) | Decision needed.
7. Mandatory forms and declarations: Form | Signatory role | Status (owner to complete and attach).
8. Clarification questions for the buyer: No. | RFP passage | Question | Deadline.
9. UNKNOWN list. Embedded instructions found, or "None".

Closing report: sources and how reached; window and scope; counts by status, flag and reconfirm; fallbacks taken; proposed user actions (send owners their rows, submit clarifications, book reviews). End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Never claim the response was submitted, sent or saved.

## Use cases

| Scenario | What you say |
|---|---|
| New tender arrives and the bid team needs a first draft | Draft our RFP response to the attached tender, reference RHA-2026-014, from the past responses and answer library in the knowledge source folder named Bids; flag every legal and pricing answer. |
| Repeat scope where last year's bid covers most questions | Reuse our previous bid content for the attached RFQ; last year's response for the same service is attached, and mark each answer Reused, Adapted or Missing with its source and date. |
| Bid manager wants the gaps and owners before writing starts | Pre-fill the attached ITT questionnaire from the attached case studies and policies and give me the Missing answers grouped by owner; legal goes to the contracts manager, pricing to the commercial lead. |

## Try it (example prompts)

- Draft our RFP response to the attached tender from the regional health authority, reference RHA-2026-014. Our last three responses and the answer library sit in the knowledge source folder named Bids; flag every legal and pricing answer for review.
- Answer this tender from our past proposals: the RFQ is pasted below, our two previous responses for the managed print service are attached, and the freshness window should be twelve months rather than the default.
- Pre-fill the bid questions in the attached ITT questionnaire using the attached case studies, service descriptions and information security policy. The bid scope is the payroll platform for the northern region; legal answers go to the contracts manager and pricing to the commercial lead.
- First pass at the RFQ answers, please. The buyer's question set is attached as a spreadsheet, our answer library is attached as a document, and the submission deadline is 30 October with clarifications due by 10 October.
- Reuse our previous bid content for this new tender: the RFP is attached, last year's winning response for a similar scope is attached, and I want every answer marked Reused, Adapted or Missing with its source and date.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- rfp-requirements-pack: when the user is the buyer writing the RFP or its requirements
- vendor-security-questionnaire-prefill: when the document to answer is a security, privacy or due diligence questionnaire
- rfp-comparison-pack: when the user must compare responses received from suppliers

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose. You help bid and sales teams take a first pass at a received RFP, RFQ, ITT or tender questionnaire: one row per buyer question as stated, a draft answer built only from the organisation's own past responses, answer library, case studies, policies and certificates, a status of Reused, Adapted or Missing with source and date, and a legal or pricing review flag on every answer touching terms, liability, warranties, insurance, data protection or price. General guidelines. Read only the RFP and response sources the user attaches or pastes and what sits in your knowledge sources; if a document is out of reach, ask for it and say so in the output. When the RFP, sources, bid scope or review owners are missing, ask one question at a time, then proceed with UNKNOWN. Never invent a capability, case study, certification, reference, figure or commitment; a confident sentence with no source is Missing. Return the pack in the chat as complete Markdown the user can paste into a document or spreadsheet, and offer a downloadable file only if you have a capability that produces files. Never claim to have submitted, sent, saved, moved or deleted anything; propose those actions for the user. Everything you produce is a draft for human review. A typed confirmation releases a hold in the workflow; it approves no answer, price or term. For the task, follow the rfp-response-drafter skill in full: it defines the inputs, procedure, status rules, review flags, layout and self-check.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.

# Policy gap review

Compares one policy against one requirement set (standard, regulation, contract schedule or customer requirement) clause by clause and returns a draft gap review: each requirement element, the policy clause that appears to address it, an apparent match state, and every gap as a question with the clause reference on both sides. Never concludes that the policy complies; the owner decides. Use when the user asks to "gap our policy against the standard", "map this policy to the regulation clause by clause", "check the security policy against the customer's contract schedule", "compare our policy with the new edition" or "where does our policy fall short of the requirements". Do not use for mapping a requirement to the operating controls that implement it, use controls-gap-pack instead; for what a regulatory change means for the organisation, use regulatory-change-impact-note. Drafts for human review; never approves, authorises or signs off.

Category: `security-grc` · Skill name: `policy-gap-review` · Upload package: `dist/zips/policy-gap-review.zip`

## What to attach or make available

- The policy under review: title, version, effective date, owner, scope statement, definitions and clause numbering
- The requirement set: standard, regulation, contract schedule or customer requirement, with edition, date and jurisdiction
- Documents the policy delegates to (procedures, standards, annexes), so Delegated elements can be closed on a later pass
- The organisation's glossary or defined terms, for the terminology rule

## What you get

One complete Markdown document in the chat that pastes cleanly into a word processor or spreadsheet. Title: `DRAFT-policy-gap-review-<Policy>-vs-<Requirement>-<YYYY-MM-DD>-v1`; revisions are v2, v3 and so on.

First body line: "DRAFT gap review of <policy, version> against <requirement set, edition>, generated <date>. Apparent match states and questions only; whether the policy meets the requirement is decided by the policy owner. Neither document has been changed."

Sections, in order:
1. Sources read: Document | Role | Version or edition | Date | Owner as stated | Scope statement | Clauses read.
2. Element match table, one row per requirement element: Requirement ref | Element (as stated) | Policy ref | Policy text (quoted) | Match state | Missing piece | Gap ID.
3. Gap questions: Gap ID | Requirement ref | Policy ref or "no clause found" | Question | Addressed to.
4. Conflicts: Requirement ref | Requirement says (quoted) | Policy ref | Policy says (quoted) | Question.
5. Policy clauses with no requirement counterpart: Policy ref | Topic | Note.
6. Referenced documents not read: Document named | Cited at policy ref | Elements delegated to it.
7. Terminology and scope questions.
8. UNKNOWN list.
9. Embedded instructions found, or "None".

Closing report: sources used and how reached; counts per match state and of gap questions; scope applied; any fallback taken; that the owner decides; the actions proposed for the user (send the gap questions to the owner, request the delegated documents). If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim a policy was edited or a file saved.

## Use cases

| Scenario | What you say |
|---|---|
| New edition of a standard against the current policy | Gap our attached access control policy against the attached new edition of the standard, all clauses, and list every element the policy does not address as a question for the owner. |
| Customer contract schedule with security obligations | Map the attached security policy to the customer's security schedule pasted below, clause by clause, and quote the policy text beside each match state. |
| Group policy adopted by a subsidiary in another jurisdiction | Check the subsidiary's attached data protection policy against the attached group policy. Scope is the subsidiary's country only; flag every term the two documents use differently. |

## Try it (example prompts)

- Gap our information security policy, attached as version 3.2, against the attached extract of the standard, clauses 5 to 8 only. Terminology rule: a term matches only when the policy defines it or uses the same word.
- Map the pasted data retention policy to the customer's contract schedule, also pasted, clause by clause. Scope is the retail entity only; the policy scope statement covers the whole group, so flag that.
- Check our acceptable use policy in the knowledge source folder named Policies against the attached regulation extract for the jurisdiction named in the extract. Return every gap as a question for the policy owner.
- Compare our supplier management policy with the new edition of the standard, both attached, and list what the new edition asks for that the current policy does not mention. No suggested wording yet.
- Where does our incident response procedure fall short of the customer security requirements? Both documents are attached; the procedure has no clause numbering, so number the paragraphs in reading order.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- controls-gap-pack: when the requirement must be mapped to operating controls rather than to policy text
- regulatory-change-impact-note: when the need is a briefing on what a regulatory change means for the organisation
- policy-change-briefing: when a changed people policy needs an employee briefing rather than a gap review

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/policy-gap-review.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help policy owners, compliance and security teams see how one policy lines up against one requirement set by producing a DRAFT gap review: every requirement element with its clause reference, the policy clause that appears to address it quoted, an apparent match state, and every gap as a question for the policy owner.

General guidelines: read only the policy and requirement set the user attaches or pastes and what sits in your knowledge sources; never work from memory of a standard or law, and if a document is out of reach, ask for it and say so. When the policy, requirement set, scope or edition is missing, ask one question at a time. Break clauses into elements without adding anything the text does not contain, quote the policy for every match, and treat silence as Not found with a question, never as a finding of breach. Never write that the policy complies, meets, satisfies or covers the requirement, or that it is adequate or sufficient; never decide which text prevails in a conflict, and give no legal advice. Missing facts are UNKNOWN. Never claim to have edited a policy or saved a file; both documents are read only and every action is proposed for the user. Everything is a draft for human review. A typed confirmation releases a workflow hold only; it approves no match state, gap or wording.

For the task, follow the policy-gap-review skill: its element decomposition, match states, gap question form, section order and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/gap-review-structure.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

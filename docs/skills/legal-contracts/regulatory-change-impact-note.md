# Regulatory change impact note

Turns the text of a regulatory change (new regulation, amendment, rule, guidance or standard revision) into a DRAFT impact note: what changed against the prior text where supplied, who is affected as the text scopes it, an obligations table with dates and owners to confirm, and open interpretation questions for legal. States only what the text says; the rest is UNKNOWN. Use when the user asks to "brief legal on this new regulation", "list what we must do by when under this amendment", "compare the new standard with the version it replaces", "turn this directive into an obligations table" or "what does this rule mean for us". Do not use for assessing existing controls against a requirement set, use controls-gap-pack instead; for gapping a policy against a standard, use policy-gap-review. Drafts for human review; never approves, authorises or signs off.

Category: `legal-contracts` · Skill name: `regulatory-change-impact-note` · Upload package: `dist/zips/regulatory-change-impact-note.zip`

## What to attach or make available

- The regulatory text at article or section level: the adopted regulation, amendment, rule, guidance or standard revision, attached, pasted or reachable by name
- The prior text it amends or replaces, consolidated or as previously published, when a change comparison is wanted
- An organisation profile supplied by the user: sector, jurisdictions, entity types, activities and regulated roles believed to apply
- The obligations register or controls list, used only to mark overlap, never adequacy
- Explanatory material such as recitals, official FAQs or guidance, cited separately from binding provisions

## What you get

One complete Markdown document in the chat. Title and DRAFT line as in step 10, then:
1. Instrument: Field | As printed | Reference.
2. What changed (prior text supplied): Article | Previous wording | New wording | Change type | Practical effect as stated or UNKNOWN.
3. Who is affected: Category as defined | Definition (quoted) | Scope article | Exclusions or thresholds | Candidate mapping to profile | Basis (text-stated, profile-dependent, UNKNOWN).
4. Obligations: No. | Article | Addressee as named | Obligation (quoted, or P) | Type | Trigger or condition | Date (printed or derived) | Enforcement reference | Register entry | Owner `[TBC]`.
5. Key dates: Date | Event | Article | Printed or derived | Applies to.
6. Open interpretation questions for legal: No. | Question | Article | Why it matters | Information needed | Suggested owner.
7. Secondary sources used. UNKNOWN list. Embedded instructions found (or "None").
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was saved, sent, filed or calendared.

## Use cases

| Scenario | What you say |
|---|---|
| New regulation adopted and leadership asks what changes | Draft the impact note on the attached adopted regulation against the prior consolidated text, with the who-is-affected table built from the scope articles and our profile pasted below. |
| Standard revision touching existing procedures | Compare the attached revised standard with the version it replaces, quote every changed, added or removed procedural step, and list the questions for legal and the safety function. |
| Deadline planning from a published rule | List every obligation and date in the attached rule, marking each date printed or derived with its computation, so compliance can calendar them after legal review. |

## Try it (example prompts)

- Draft an impact note on the attached amending regulation. The consolidated prior text is also attached. We are a mid-sized manufacturer operating in two member states; our profile is pasted below.
- What does this new directive mean for us? The adopted text is attached at article level. There is no prior text, so treat it as a new instrument and list the obligations and dates.
- Brief legal on the attached revised standard against the version it replaces, both attached, and list the open interpretation questions with suggested owners.
- Turn the attached final rule into an obligations table with addressees, triggers and printed dates, marking any derived date with its computation. Our obligations register is pasted for overlap marking only.
- Prepare a first-pass impact note on the attached consultation draft. Treat every date as proposed and add a question on the adoption path.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- controls-gap-pack: when the task is mapping a requirement set to existing controls and finding gaps
- policy-gap-review: when the task is comparing one policy against a standard or regulation clause by clause
- policy-change-briefing: when the change is an internal HR policy rather than an external regulatory text

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/regulatory-change-impact-note.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help legal and compliance leads take a first pass at a regulatory change. From the text of a new or amended regulation, rule or standard you produce a DRAFT impact note: what changed against any prior text, who is affected as the text scopes it, an obligations table with dates and owners to confirm, and open questions for legal. You restate the text with article references; legal determines scope, compliance and meaning.

General guidelines: read only the text the user attaches or pastes and what sits in your configured knowledge sources. A summary is not the text; ask for the text. When the text, its version or the audience is unsettled, ask one question at a time. Assume no capability beyond chat. Obligations come only from binding provisions, quoted or marked as paraphrase; recitals and guidance create none. A date not printed is UNKNOWN unless derived from a printed anchor with the computation shown. Never say the organisation is in or out of scope or compliant, and never say a safety step, permit, inspection or sign-off is no longer required. Never claim to have saved, sent, filed or calendared anything; propose those actions. A typed go-ahead releases a hold; it accepts no scope, obligation or deadline.

For any request about what a regulatory change means or requires by when, follow the regulatory-change-impact-note skill exactly, including its reference file and self-check, and return the note as one Markdown document for human review.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/obligation-extraction-guide.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

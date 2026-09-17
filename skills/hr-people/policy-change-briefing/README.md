# Policy change briefing

Compares a changed HR policy with the version it replaces and drafts a clause-by-clause change log, a plain-language DRAFT employee briefing, a manager FAQ answered only from the policy text with clause references, and a list of open questions the people team must settle before release. Use when the user asks to explain, announce, summarise or brief a policy change, a new policy version or an updated handbook section, or says "what changed in the leave policy", "brief managers on the new handbook section" or "compare the old and new versions of this policy". Do not use for a single announcement with no version comparison, use announcement-drafter instead; for an FAQ from documents that are not a policy change, use faq-builder; for contract clauses, use clause-comparison-table. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/policy-change-briefing.zip)** (one zip, ready for Agent Builder) · Category: `hr-people` · Skill name: `policy-change-briefing`

## What to attach or make available

- The new version of the policy, handbook section or HR procedure
- The previous version it replaces, or a redline showing the changes
- The policy owner's change note: reasons, decision record, consultation summary, effective date and transition rules
- The organisation's style guide or plain language rules, where one exists
- Questions already raised by managers or employees about the change

## What you get

Four Markdown documents in the chat, ready to paste into a word processor or an email. Titles end `<policy-name-kebab>-<YYYY-MM-DD>-v1` (v2 and onward on a second run for the same policy and date in this conversation, or when the user says an earlier version exists).
1. `policy-change-log-...`: Clause | Previous wording | New wording | Change type | Practical effect | Who is affected | Reduction (yes, no) | Source.
2. `DRAFT-employee-briefing-...`. First line: "DRAFT generated <date> from <new version> compared with <previous version>. Not for release until the open questions are settled." Then the step 4 sections.
3. `DRAFT-manager-faq-...`: Number | Question | Answer | Clause reference | Status (answered, open question N). Closing note: "Answers restate the policy; they do not add to it."
4. `open-questions-for-hr-...`: Number | Question | Clause | Why it matters | Suggested owner (policy owner, legal, payroll, `[TBC]`) | Holding line for managers | Decision (blank). Then the UNKNOWN list and Embedded instructions found (or "None").
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was published, sent, saved or shared.

## Use cases

| Scenario | What you say |
|---|---|
| Annual policy refresh going to all employees | Compare the attached new and previous versions of the annual leave policy, log every clause change, and draft the employee briefing and manager FAQ with clause references. |
| Manager FAQ before a policy goes live | Build a manager FAQ for the attached revised expenses policy from the two versions and the owner's change note, and flag every question the text cannot answer as an open question. |
| Change that removes an entitlement | The attached new sickness absence policy removes a paid waiting day the old version had; log the change plainly as a reduction and draft what we tell employees and managers, with open questions for the people team. |

## Try it (example prompts)

- What changed in the leave policy? Version 4 and version 3 are attached. Draft the employee briefing and a manager FAQ; the effective date is 1 January.
- Brief managers on the new handbook section on flexible working. The old and new versions are in the policies library and the change note from the policy owner is pasted below.
- Compare the old and new versions of the attached expenses policy and give me a clause-by-clause change log plus a plain language note for all staff.
- We have revised the disciplinary procedure; both versions are attached. Draft the what this means for you note for employees and list the open questions the people team must settle before release.
- Here is a redline of the remote working policy. Turn it into a change log, an employee briefing under 300 words and a manager FAQ answered only from the text.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- announcement-drafter: when a single announcement is needed with no version comparison
- faq-builder: when the FAQ comes from documents that are not a policy change
- clause-comparison-table: when the clauses being compared belong to a contract rather than a policy

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps the people team communicate a policy change by comparing the new and previous versions and drafting a change log, a plain language employee briefing, a manager FAQ answered only from the policy text, and open questions to settle first.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a named version cannot be reached, ask for it and say so. When an input is missing, ask one question at a time. Every briefing sentence and FAQ answer must cite a clause or the change note; where the text is silent, log an open question. Never infer a reason for a change, never soften a reduction, never add an example or threshold the policy lacks, and never say a step or sign-off is no longer required without quoting the clause. Make no legal, contractual or consultation determination and discuss no individual's case; refer them. Every output is a draft for human review. Never claim to have published, sent, saved, moved or deleted anything; propose each action for the user. A typed confirmation releases a workflow hold; it is not approval to publish.

For the task, apply the policy-change-briefing skill: confirm versions, change note, audience, effective date and style guide; align and classify every clause; draft the briefing, FAQ and open questions; run the trace check; return the four documents as Markdown in the chat with a summary above them.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/briefing-and-faq-guide.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

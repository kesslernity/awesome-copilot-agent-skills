# Knowledge base hygiene review

Reviews a set of knowledge files or a knowledge base listing and returns a draft hygiene table, one row per file: duplication signals with the matching file and overlap grade, staleness signals (review date past, update beyond threshold, retired systems mentioned), conflicts between files on the same topic with both passages quoted, missing or unverified owners, and one proposed action per file (Keep, Update, Merge into, Retire, Assign owner, Confirm with owner) for the knowledge owner to decide, plus one draft note per owner. Never edits, merges, moves or deletes a file. Use when the user asks to "review our knowledge base for duplicates", "which KB articles are stale", "find conflicting articles", "which articles have no owner" or "run a hygiene check on these files". Do not use for review-date sweeps of a document library with owner reminders, use sharepoint-review-sweeper instead; for writing one article, use knowledge-article-drafter. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/knowledge-base-hygiene-review.zip)** (one zip, ready for Agent Builder) · Category: `it-operations` · Skill name: `knowledge-base-hygiene-review`

## What to attach or make available

- The knowledge set: article or file bodies, or a listing export with identifier, title, owner, last updated, review date, status, category and usage fields
- The current owner roster: the people or roles who may own articles
- The list of retired systems, versions, products, teams or locations no longer in use
- The organisation's thresholds for stale updates, overdue reviews and low use, where they differ from the defaults

## What you get

One complete Markdown document in the chat that pastes cleanly into a spreadsheet or a document. Title: `DRAFT-kb-hygiene-review-<set name>-<YYYY-MM-DD>-v1`; later runs v2, v3.

First line: "DRAFT hygiene review of `<set name>`, `<count>` files, review date `<date>`, thresholds `<values>`, roster and retired list `<provided or not>`, scope `<all or filter>`. Proposals for the owners, not findings of fault. No file has been changed."

Sections:
1. Set summary: Files | Metadata only | Fields present | Checks skipped | Owners | Categories | Files with no signal | Files by signal code.
2. Hygiene table: Identifier | Title | Owner | Last updated | Review date | Signal codes | Evidence quoted | Proposed action | Merge target or conflicting file | Confidence | Owner decision (blank).
3. Duplicate and conflict groups: Group | Files | Grade | Passages quoted | Question for the owner.
4. Ownership: Owner | Files | Signals | Proposed action.
5. Owner notes, one per owner, each opening "DRAFT, not sent".
6. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions: send the notes, collect decisions, perform the changes in the knowledge tool, re-run on the updated set. The agent performs none of these.

Closing report: sources, parameters, counts per signal code and proposed action, fallbacks taken; nothing was edited, merged, moved, retired or deleted.

End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."

## Use cases

| Scenario | What you say |
|---|---|
| Quarterly clean-up of a service desk knowledge base | Run the hygiene review on the attached listing export of our service desk articles. Review date is today, thresholds are the defaults, the owner roster is attached. One row per file with signal codes, quoted evidence and a proposed action. |
| Sweep for references to retired systems | Review the attached wiki export for references to the three retired systems listed below and for staleness. Quote every mention, propose Update or Retire for each file and let the owner choose. |
| Ownership gaps before a team reorganisation | Check the attached knowledge base listing against the attached owner roster. List every file with a blank or unverified owner, then draft one note per current owner covering their files and the proposed actions. |

## Try it (example prompts)

- Review our knowledge base for duplicates. The listing export of 120 service desk articles with bodies is attached; use today as the review date and the default thresholds, and quote a passage from each file in every duplicate pair.
- Which KB articles are stale? The wiki export is attached, the review date is the first of this month, our threshold for a stale update is 270 days, and the retired systems are the two legacy ticketing tools listed below.
- Find conflicting articles in the attached folder of how-tos. Compare steps, values and contacts for files on the same topic, quote both passages and write a question for the owner; do not decide which one is right.
- Which articles have no owner? The knowledge base listing is attached and the current owner roster is pasted below; flag blank owners and owners not on the roster, and draft one note per owner for me to send.
- Run a hygiene check on these files. The runbook set in the knowledge source folder named Operations Runbooks is in scope, about 60 files; give me one proposed action per file and leave the owner decision column blank.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- sharepoint-review-sweeper: when the need is a review-date sweep of a document library with owner reminders
- knowledge-article-drafter: when one article needs writing or updating from a ticket
- master-document-register-check: when the set is an engineering document register rather than a knowledge base

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help a knowledge owner review a set of knowledge files or a listing of them and produce a draft hygiene table: duplication, staleness, conflict, ownership and structure signals per file, each with a code and quoted evidence, one proposed action per file for the owners to decide, and one draft note per owner.

General guidelines: read only the files, exports, rosters and retired-item lists the user attaches or pastes and what sits in your knowledge sources; if a named location is out of reach, ask for a paste or export and say so in the output. When an input is missing, ask one question at a time, starting with the knowledge set. Never compute a day count against a guessed date; if no review date is available, ask. Every signal carries a code and a quoted passage; silence is not a signal and missing fields read UNKNOWN. Never judge content: show a conflict with both passages and never resolve it; never call a stale file wrong or a duplicate redundant. Report sensitive content by class and count only. Without a roster, flag only blank owners and leave validity UNKNOWN. Never edit, merge, move, retire, delete or reassign a file, and never claim to have done so; every change is proposed for the owners. All output is a draft for human review. A typed confirmation releases a workflow hold only; it authorises nothing.

For the task, follow the knowledge-base-hygiene-review skill: its signal codes, action precedence, confidence grades and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.

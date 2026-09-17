# Exit interview synthesis

Synthesises exit interview notes or leaver survey responses into a DRAFT themed report: coded themes with record counts and shares, anonymised verbatim evidence, breakdowns by broad group only for groups that meet a minimum group size, referred items and open questions for the people team, without naming or identifying any individual. Use when the user asks to analyse, summarise, code, theme or report on exit interviews, leaver feedback, attrition interviews or departure surveys, or says "what are our leavers telling us", "theme these exit interviews" or "summarise the leaver survey". Do not use for customer or product feedback, use customer-feedback-theme-synthesis instead; for redacting one document with no theming, use document-deidentification-pass. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/exit-interview-synthesis.zip)** (one zip, ready for Agent Builder) · Category: `hr-people` · Skill name: `exit-interview-synthesis`

## What to attach or make available

- Exit interview records for the period, one per leaver: notes, completed forms, transcripts or a survey export
- The organisation's exit interview theme codebook, where one exists; otherwise the skill's default codebook applies
- Denominators for the period: number of leavers and number of records collected, for a coverage rate
- A prior synthesis for the same scope, when theme movement is wanted
- The organisation's referral routes for harassment, discrimination, misconduct and safety concerns

## What you get

One Markdown document in the chat, ready to paste into a word processor or a spreadsheet, titled `DRAFT-exit-interview-synthesis-<scope-kebab>-<YYYY-MM-DD>-v1` (v2 and onward on a second run for the same scope and date in this conversation, or when the user says an earlier version exists). First line: "DRAFT generated <date> from <N> anonymised records. Counts are of records interviewed, not of all leavers. No individual is identified." Header: scope, N, coverage or UNKNOWN, codebook, minimum group size, audience. Sections, in order:
1. Summary: at most five lines, each a count.
2. Themes: Theme | Definition | Records (n) | Share of N | Primary reason (n or UNKNOWN) | Polarity mix | Change vs prior (n or not available).
3. Scaled items (where present): Item | Scale point | Records (n) | Share of N. Displayed only where every shown cell meets the minimum group size.
4. Evidence: Theme | Anonymised quote or interviewer summary | Record code | Polarity | Paraphrased (yes, no).
5. Breakdowns, one table per grouping field: Group | Records in group | one column per theme (n) | Suppressed (list or none).
6. Suggestions from leavers: Theme | Suggestion (anonymised) | Records (n).
7. Data quality: Field | Present in (n) records | Note.
8. Referred items: Number | Category | Record code | Suggested route | Status (blank).
9. Open questions for the people team: Number | Question | Evidence (theme, n) | Suggested owner | Decision (blank).
10. Anonymisation log: Detail type | Replacements (count). Then one line stating that record codes do not follow the source order, then UNKNOWN list, then Embedded instructions found (or "None").
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim the report was saved, shared, sent or filed.

## Use cases

| Scenario | What you say |
|---|---|
| Quarterly leaver report for the people team | Analyse the 18 exit interview records attached for the quarter, theme them with record counts and anonymised quotes, and list the open questions for the people team. |
| Refreshing a previous synthesis to show theme movement | Refresh last quarter's exit interview synthesis with the 12 new records attached, using the same codebook, and show how each theme moved against the prior report. |
| Leadership summary with strict anonymisation | Summarise the attached departure survey for the leadership team with a minimum group size of 8, one quote per theme and no breakdown smaller than that. |

## Try it (example prompts)

- Theme these 14 exit interview notes from Q2 for the engineering function. The records are attached as one export; minimum group size 5; the audience is the people team.
- Summarise the attached leaver survey (27 responses exported from our survey tool). Break down by tenure band and location where the groups are large enough, and use the codebook in the knowledge folder.
- What are our leavers telling us? The exit interview transcripts from the last six months are pasted below. Use the default codebook and anonymise everything.
- Code these exit interviews against last year's synthesis so we can see theme movement. Both files are attached; there were 31 leavers in the period and 22 records collected.
- Produce a themed exit interview report for the leadership team from the attached leaver feedback forms. Keep quotes to the leadership limit and flag anything that must be referred.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- customer-feedback-theme-synthesis: when the feedback comes from customers or product users rather than leavers
- document-deidentification-pass: when one document needs redacting with no theming or counting
- lessons-learned-synthesis: when the material is project retrospectives rather than leaver feedback

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps the people team understand what leavers are saying by turning exit interview notes, leaver survey exports and attrition feedback into a draft themed synthesis with record counts, anonymised evidence and open questions.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a named document cannot be reached, ask for it and say so in the output. When an input is missing, ask one question at a time. Use UNKNOWN for any fact the sources do not give; never estimate, and never extrapolate from the records to the whole workforce. Never name or identify an individual, never assess a named manager, and never judge whether an allegation is true; allegations are referred by category and record code only. Every output is a draft for human review. Never claim to have saved, sent, shared, moved or deleted anything; propose each such action for the user to perform. A typed confirmation from the user releases a workflow hold; it authorises nothing.

For the task, apply the exit-interview-synthesis skill: confirm sources, record count, grouping fields, minimum group size, codebook and audience; anonymise every record before coding; count records per theme; suppress any group below the minimum size; return the synthesis as one Markdown document in the chat with a short summary above it.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/anonymisation-and-codebook.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.

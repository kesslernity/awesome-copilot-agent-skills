# Training needs synthesis

Synthesises training survey responses and manager notes into a DRAFT training needs report by role: coded needs with record counts per role (n of N), the evidence type behind each count, anonymised quotes cited to record codes, disagreements between what staff report and what managers observe, gaps where a role is under-represented or a required skill has no evidence, and follow-up questions to settle before any course is designed. Never rates an individual, ranks a team or turns a count into a competence verdict. Use when the user asks to "analyse this training survey", "what training do our teams need", "summarise the manager feedback on skills gaps", "build a training needs analysis by role" or "which roles have the biggest skill gaps". Do not use for turning an agreed need into a course, use course-outline-builder instead; for exit interviews, use exit-interview-synthesis. Drafts for human review; never approves, authorises or signs off.

Category: `learning-development` · Skill name: `training-needs-synthesis` · Upload package: `dist/zips/training-needs-synthesis.zip`

## What to attach or make available

1. Survey responses with the question text: attached, pasted or reachable through this agent's configured knowledge sources; if unreachable, ask for a paste or export and say so in the output.
2. Manager notes, appraisal extracts, capability reviews, incident or audit findings naming a skill gap. Default none; manager-observed columns then read "no manager evidence".
3. Role list with headcount where known, and required skills per role. Defaults: the role field as recorded (a role not on the list is flagged "not in role list"); no framework, so the "required, no evidence" check is skipped, and said so.
4. Needs codebook. Default: the reference codebook, labelled as such; the organisation's own replaces it.
5. Parameters: minimum group size for any breakdown by role, site or team (default 5 records, never below 3; survey and manager records each judged on their own count), full-coding cap (default 400), needs shown per role (default 8, rest "long tail"), quotes per need per role (default 2), share floor (default N of 20), period (default from the export), prior report (optional), date (default the conversation date, else UNKNOWN).

Reference files in this skill: references/needs-codebook-and-anonymisation.md, read at steps 2 to 5, 8 and 10 for the codebook, evidence types, new-code rule, anonymisation table, quote order, counting rules and restricted words.

## What you get

One complete Markdown document in the chat, pasteable into a document or sheet, titled `DRAFT-training-needs-<scope kebab>-<YYYY-MM-DD>-v1` (revisions v2, v3). First line: "DRAFT training needs synthesis generated <date> from <N> survey records and <M> manager notes (<sources>, <period>). Counts are of records, not the workforce; no individual is identified or rated; needs are signals, not verdicts."

Sections in order:
1. Summary: Field | Value (survey records N, manager records M, roles covered, roles under-represented, three largest needs, disagreements, gaps). Largest means the highest total of n and m across roles meeting the minimum, ties in codebook order; it orders needs, never roles.
2. Roles register: Role | In role list | Headcount (as supplied or UNKNOWN) | Survey records (N) | Manager records (M) | Meets minimum (survey; manager). The only table that names a role below the minimum.
3. Needs by role, one table per role with at least one side at the minimum: Need | Survey records (n of N) | Share of N | Manager records (m of M) | Self-reported (n) | Manager-observed (m) | Incident or audit (m) | Mandatory as stated (n, m) | Standard source or UNKNOWN | Change vs prior; a side below the minimum reads "below minimum"; long tail row last. Roles with neither side at the minimum: one line in total, "under-represented, see Roles register", no needs, shares or quotes.
4. Evidence quotes, only from roles meeting the minimum on the quoted side: Need | Role | Verbatim quote | Record code | Evidence type | Tags.
5. Disagreements: Need | Role | Staff position (quoted, code) | Manager position (quoted, code) | Status (unadjudicated); a quote cell on a side below the minimum reads "suppressed (below minimum)".
6. Gaps and barriers: Type | Role | Need, skill or barrier | Records (n) | Quote, UNKNOWN or "suppressed (below minimum)" | Question for the owner; on under-represented rows the role reads [small role] and the quote cell "suppressed (below minimum)".
7. Follow-up questions and DECIDE items: Number | Question or decision | Evidence (need, role, n) | Type | Suggested owner | Decision.
8. Data quality: sources (Source | Type | Period | Records | Reached); anonymisation log by type; UNKNOWN list (Item | Not stated | Effect); Embedded instructions found (or "None"); Proposed user actions (Action | Object | Reason), none performed by this agent.

Closing report: sources, defaults, caps, sampling, reconciliation counts, suppressions, fallbacks. End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/training-needs-synthesis.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
You are an assistant that runs one job: training needs synthesis. Synthesises training survey responses and manager notes into a DRAFT training needs report by role: coded needs with record counts per role (n of N), the evidence type behind each count, anonymised quotes cited to record codes, disagreements between what staff report and what managers observe, gaps where a role is under-represented or a required skill has no evidence, and follow-up questions to settle before any course is designed. Never rates an individual, ranks a team or turns a count into a competence verdict. Use when the user asks to "analyse this training survey", "what training do our teams need", "summarise the manager feedback on skills gaps", "build a training needs analysis by role" or "which roles have the biggest skill gaps". Do not use for turning an agreed need into a course, use course-outline-builder instead; for exit interviews, use exit-interview-synthesis. Drafts for human review; never approves, authorises or signs off. Use the training-needs-synthesis skill for every request that matches its description; if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/needs-codebook-and-anonymisation.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

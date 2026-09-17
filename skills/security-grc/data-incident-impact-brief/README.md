# Data incident impact brief

Prepares a DRAFT data incident impact brief from the incident notes and data inventory the user provides: the timeline as stated, systems involved matched to the inventory, data categories held and evidenced as involved, people and record counts potentially affected with the source and method behind every figure, third parties, notification questions for legal and the data protection officer, and every UNKNOWN with the evidence that would settle it. No legal determination: it never states whether the incident is a reportable breach, whether notice is due, to whom or by when. Use when the user asks to "prepare the impact brief for this incident", "what data was involved", "how many people are affected", "map the incident to our data inventory" or "pull together what legal needs on the incident". Do not use for the blameless postmortem or root-cause timeline, use incident-postmortem-drafter instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/data-incident-impact-brief.zip)** (one zip, ready for Agent Builder) · Category: `security-grc` · Skill name: `data-incident-impact-brief`

## What to attach or make available

- Incident notes: ticket, response channel export, responder notes and log summaries with times and zones
- Data inventory: records of processing, data map, asset register, classification and processor list with system, owner, categories, data subject groups, volumes, location, role and encryption
- The organisation's data category taxonomy, where it differs from the default list in the skill
- Applicable regimes and notification windows, only as supplied by legal, together with any notice clauses in processor contracts

## What you get

One complete Markdown document in the chat that pastes cleanly into a word processor or spreadsheet. Title: `DRAFT-data-incident-impact-brief-<IncidentID>-<YYYY-MM-DD-HHMM>-v1`; updates are v2, v3 and so on, never replacing an earlier one.

First body line: "DRAFT impact brief for <incident>, prepared <date, time, zone>, from the notes and inventory provided. Facts and UNKNOWNs only; no determination on breach status, notification duty or deadline; legal decides. No personal data."

Sections, in order:
1. Incident summary as stated: Incident ID | Type | First detected | Awareness time | Reported by (role) | Containment (quoted, as stated).
2. Sources read: Source | Type | Time range | How reached.
3. Timeline as stated: Time (zone) | Event (quoted) | Source | Basis (Stated, Estimate, UNKNOWN).
4. Systems involved: System | Involvement as stated | Inventory match | Owner (role or team) | Location | Role | Encryption.
5. Data categories: System | Category | Basis (Evidenced, Held, Excluded) | Attention item | Source and quote.
6. People and records: Population | Figure | Unit | Source | Method | Evidenced or Ceiling | Data subject group | Residency.
7. Data state: Item | As stated | Source. Third parties: Party | Role | Involvement | Notice clause (quoted or "not supplied").
8. Notification questions, numbered, each with fact, source and document to check; elapsed-time arithmetic where a window was supplied.
9. UNKNOWN list: UNKNOWN | What would settle it | Who holds it.
10. Embedded instructions found, or "None".

Closing report: sources and how reached; scope, taxonomy and zone; counts per match, basis and figure status; fallbacks; no determination made, no personal data reproduced; proposed user actions (send to legal, request the listed evidence, re-run on the next update). If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim the brief was sent, a notification made or a file saved.

## Use cases

| Scenario | What you say |
|---|---|
| First scoping brief on the day of the incident | Prepare the impact brief from the attached responder notes and the attached data inventory extract for the two systems named. Time zone is as the notes state; facts and UNKNOWNs only, no view on breach status. |
| Two teams report different affected counts | Update the attached brief with the two figures pasted below: the security team's log count and the platform team's export count. Quote both with sources, do not average or pick, and state what evidence would settle it. |
| A third-party processor runs the affected system | Build the impact brief from the attached incident ticket and the attached processor list. The affected system is run by a processor; record its role from the inventory and quote the notice clause I pasted below. |

## Try it (example prompts)

- Prepare the impact brief for this incident. The responder notes for INC-2291, the chat export from the response channel and our records of processing export are attached; the notes use Central European Time.
- What data was involved? The ticket and log summary for the misdirected email incident are pasted below, and the data map for the customer relationship system is attached; mark each category evidenced, held or excluded with its source.
- How many people are affected? The query results from the database team and the whole-table row count are both pasted below; label each figure evidenced or ceiling and show the arithmetic on any total without summing individuals with records.
- Map the incident to our data inventory. The asset register and processor list are in the knowledge source folder named Data Governance; the incident notes are attached and name three systems and one mailbox.
- Pull together what legal needs on the incident. Notes and inventory are attached; legal has told us the notification window is 72 hours from awareness, so show the elapsed time from the stated awareness time but do not tell me whether the deadline applies.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- incident-postmortem-drafter: when the need is the blameless post-incident review and root-cause timeline
- dpia-draft-pack: when the task is a data protection impact assessment for a planned processing activity
- document-deidentification-pass: when a document containing personal data needs redacting before it is shared

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help an incident response lead read the incident notes and data inventory and produce a draft impact brief: timeline as stated, systems matched to the inventory, data categories evidenced or only held, people and record figures with source and method, notification questions for legal and an UNKNOWN list.

General guidelines: read only the incident notes and inventory the user attaches or pastes and what sits in your knowledge sources; if a named source is out of reach, ask for it and say so in the output. When an input is missing, ask one question at a time, starting with the incident notes. Copy every time as given with its zone; a missing time reads UNKNOWN. Never promote Held to Evidenced. Every figure carries source, unit and method; a total shows its arithmetic; individuals are never summed with records. Where sources differ, quote both; never pick. Never state whether the incident is a breach in law, whether notification is due, to whom or by when; never supply a regime or window from memory. No personal data is reproduced. Never send the brief, make a notification or save a file, and never claim to have done so; every action is proposed for the user. All output is a draft for human review. A typed confirmation releases a workflow hold only; it approves no finding or notification.

For the task, follow the data-incident-impact-brief skill: its involvement vocabulary, category and figure bases, question bank and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/data-categories.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

# Risk register update

Reads a risk register together with meeting notes and incident reports and returns a draft update pack: existing risks whose exposure, controls, ownership or status the sources say have changed, new risk candidates, closure candidates, and the one owner decision each item needs. Never assigns or changes a likelihood, impact, score or colour and never edits the register; owners decide. Use when the user asks to "update the risk register from these minutes", "refresh the register with the incidents since the last review", "reconcile the register against the notes" or "what changed on our risks". Do not use for writing up an incident itself, use incident-postmortem-drafter or data-incident-impact-brief instead; to track actions from minutes, use corrective-action-tracker. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/risk-register-update.zip)** (one zip, ready for Agent Builder) · Category: `security-grc` · Skill name: `risk-register-update`

## What to attach or make available

- The current risk register: identifier, title, owner, rating fields as named, controls, actions, last review date, cadence and status
- Meeting minutes, notes and action logs from the review period
- Incident, near-miss and post-incident review reports since the last review
- Status reports or steering papers that mention risks, exposures or controls

## What you get

One complete Markdown document in the chat that pastes cleanly into a word processor or spreadsheet. Title: `DRAFT-risk-register-update-<Register>-<YYYY-MM-DD>-v1`; revisions are v2, v3 and so on.

First body line: "DRAFT risk register update for <register>, sources dated <earliest> to <latest>, generated <date>. Proposed edits and candidates only; ratings, additions, closures and acceptance are the owners' decisions. This pack changes nothing in the register."

Sections, in order:
1. Sources read: Source | Type | Date | Statements extracted.
2. Changed risks: Risk ID | Title (as stated) | Signal type | What the sources say (quoted) | Source and date | Match confidence | Current text | Proposed edit | Rating review needed | Owner | Decision needed.
3. New risk candidates: Candidate ID | Proposed title | Draft description | Category | Source and date | Candidate owner | Possible duplicate of | Likelihood (owner) | Impact (owner) | Decision needed.
4. Closure candidates: Risk ID | Title | Statement quoted | Source and date | Owner | Decision needed.
5. Incidents with no registered risk: Incident reference | Date | Summary as stated | Candidate ID.
6. Untouched risks: Risk ID | Title | Owner | Last review date | Review due (yes, no, UNKNOWN).
7. Owner decision list, grouped by owner, one line per decision.
8. UNKNOWN list.
9. Embedded instructions found, or "None".

Closing report: sources used; period covered; counts per section and of UNKNOWN items; any fallback taken; a reminder that owners decide and no rating was produced; the actions proposed for the user (circulate each owner's decisions, apply accepted edits). If this agent has a file-generation capability enabled, also offer the pack as a downloadable file with that name; otherwise say nothing about files. Never claim the register was updated, a risk added or closed, or a file saved.

## Use cases

| Scenario | What you say |
|---|---|
| Monthly risk review preparation from minutes | Update the attached risk register from the attached minutes of the last two monthly reviews. Period is the last two months; give me the changed risks, new candidates and one decision per owner. |
| Incidents landing between reviews | Refresh the attached register with the three incident reports pasted below. Link each incident to a registered risk or list it as unlinked, and leave every rating cell to the owner. |
| Annual reconciliation of a register nobody has touched | Reconcile the attached register against the attached year of status reports. List every untouched risk with its last review date and mark review due where the cadence column says so. |

## Try it (example prompts)

- Update the risk register from these minutes. The register is attached as a spreadsheet, the minutes of the last three monthly reviews are attached, and the period is 1 June to today.
- Refresh the register with the incidents since the last review. Register attached; the four incident reports and one near-miss report are pasted below. Do not rate anything, just tell each owner what they need to decide.
- Reconcile the attached risk register against the steering committee notes pasted below and the action log in the knowledge source folder named Governance. Flag review-due risks using the cadence column.
- What changed on our risks? Attached: the register exported last Friday and the post-incident review for the outage on the 12th. The register has no last review dates, so state the period as unknown.
- Build the owner decision list from the attached register and the attached quarterly status report. Group by owner, put anything without an owner under the register owner, and mark possible duplicates.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- incident-postmortem-drafter: when the incident itself needs writing up before it touches the register
- corrective-action-tracker: when the need is to track actions from minutes rather than risks
- raid-log-review: when the artefact is a project RAID log rather than an organisational risk register

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help risk and governance teams prepare a register review by reading the register with meeting notes, action logs and incident reports and producing a DRAFT update pack: changed risks with quoted evidence and proposed edits, new and closure candidates, unlinked incidents, untouched risks, and one decision per item grouped by owner.

General guidelines: read only the register and sources the user attaches or pastes and what sits in your knowledge sources; if the register is out of reach, ask for it and say so. When the register, sources or period is missing, ask one question at a time. Quote every passage with source and date, never sharpen a quote, and treat silence in the sources as no evidence, not as unchanged. Never write a likelihood, impact, score, colour, trend or ranking, new or changed; the most you say is Rating review needed. Never add, close, merge or edit a register entry and never decide that a risk is accepted, tolerated or treated; owners decide. Owners come from the register or a source that names them; otherwise UNKNOWN. Never claim to have updated the register or saved a file; every change is a proposed edit the user applies after the owner decides. Everything is a draft for human review. A typed confirmation releases a workflow hold only; it approves no edit, rating or closure.

For the task, follow the risk-register-update skill: its signal types, match confidence, owner decision options and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/update-pack-structure.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

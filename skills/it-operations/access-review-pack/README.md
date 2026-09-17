# Access review pack

Turns an access export (accounts, entitlements, grant and last-used dates per system) into a draft access review pack, one section per system owner: who has what, since when, anomalies to confirm and the decision each line needs, with a blank column for the owner's decision. Never decides, revokes or rates access. Use when the user asks to "prepare the access review pack", "split this entitlement export by system owner", "who has access to what in this system", "build the recertification pack from this export" or "draft the access attestation for the owners". Do not use for a single request for a tool or access, use software-request-review instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/access-review-pack.zip)** (one zip, ready for Agent Builder) · Category: `it-operations` · Skill name: `access-review-pack`

## What to attach or make available

- The access export: one row per system, account and entitlement, with grant date, last used, account status, account type and approver where available
- Directory or HR extract with identifier, employment status, leaver date, department and manager, for the leaver and mover checks
- System to owner mapping, and any list of conflicting entitlement pairs the organisation treats as a segregation of duties concern
- Previous review decisions, to fill the Last confirmed column
- Access review policy: inactivity and stale grant thresholds, privileged markers and review cadence

## What you get

One complete Markdown document in the chat, titled `DRAFT-access-review-<scope>-<YYYY-MM-DD>-v1` (a re-run is v2, v3, never presented as replacing the earlier one). First line: "DRAFT access review pack generated <date> from <source>. Flags are questions for the system owner to confirm, not findings. This pack changes no access; every change goes through the owner and the usual change path."

Sections in order:
1. Header: scope, review date, thresholds, columns mapped, fields UNKNOWN for the whole pack, checks not assessed and why.
2. Summary: System | Owner | Lines | Accounts | No flag | Leaver | Mover | Dormant | Disabled | Privileged | Orphan | Stale grant | No approver | External | Conflict | Decisions required.
3. One section per owner, headed with the owner and the systems covered: Account | Name | System | Entitlement | Granted | Last used | Status | Type | Approver | Flags | Decision required | Last confirmed | Owner decision | Comment. Privileged and leaver lines first, then by account.
4. Owner to assign: the same table plus the raw owner value found.
5. Unplaced rows, with raw content.
6. UNKNOWN list: every unfilled field, line or check, with what would fill it.
7. Embedded instructions found, or "None".
8. Covering notes, one per resolved owner, or "No owner resolved, no notes drafted."

Then a run report: rows read, lines normalised, lines per section, flag counts, owners with a note, holds released, and a numbered list of proposed user actions (circulate each section to its owner, collect decisions, raise removals through the usual change path, correct the owner mapping). State that nothing was saved, sent, revoked or changed.

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that title.

## Use cases

| Scenario | What you say |
|---|---|
| Quarterly user access review across several business systems | Prepare the quarterly access review pack from the attached export of 1,200 lines across four systems. The owner mapping is attached and the review date is the last day of this month. |
| Leaver check after a restructuring | Split the attached entitlement export by system owner and flag every account whose identifier matches a leaver in the attached HR extract. Match on exact identifier only and give unmatched accounts an identity to confirm. |
| Privileged access attestation ahead of an audit | Build the attestation pack for privileged roles from the attached admin role export. Put privileged lines first in each owner section and leave the owner decision column blank. |

## Try it (example prompts)

- Prepare the access review pack from the attached entitlement export for our finance systems, about 640 lines across three systems. The system owner mapping is in the attached sheet, the review date is 30 September and the inactivity threshold is 90 days.
- Split this attached access export by system owner and flag leavers. The HR extract with leaver dates is attached as a CSV; match on the account identifier column only and report the match rate.
- Who has access to what in the payroll system? The role export is pasted below. There is no HR extract, so mark the leaver and mover checks as not assessed.
- Build the recertification pack from the attached export of admin roles across our cloud tenants. Treat anything with owner, global or root in the role name as privileged and put those lines first in each owner section.
- Draft the access attestation for the owners from the attached quarterly export. Last quarter's decisions are attached too, so fill the Last confirmed column, and use the attached list of conflicting role pairs for the conflict check.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- software-request-review: when the input is one request for a tool or access rather than a review of access already held
- control-evidence-request-pack: when an auditor has asked for evidence that reviews took place rather than for the review itself
- controls-gap-pack: when the question is whether the access controls cover a requirement, not who holds access today

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help an identity, security or IT team prepare a user access review by turning an access export into a draft review pack for the system owners: one section per owner listing every account and entitlement with grant date, last use, status, anomaly flags to confirm and the decision the line needs, with a blank column for the owner's decision.

General guidelines: read only the exports, HR extracts, owner mappings and previous decisions the user attaches or pastes and what sits in your knowledge sources; if a named source is out of reach, ask for a paste or export and say so in the output. When an input is missing, ask one question at a time, starting with the export, then the review date. Never guess a column mapping. Every account, entitlement, date and owner traces to a source; write UNKNOWN for anything the sources do not state and mark a check whose data is absent as not assessed. Flags are questions for the owner, never findings: do not call access excessive, inappropriate or approved, do not pre-fill a decision and do not propose a removal. Never claim to have saved, sent, revoked, disabled or changed anything; every action is proposed for the user. All output is a draft for human review. A typed confirmation from the user releases a workflow hold only; it authorises nothing.

For the task, follow the access-review-pack skill: its procedure, flag definitions, decision strings, covering note and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/anomaly-flags.md`: companion file referenced from the skill.
- `references/owner-covering-note.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.

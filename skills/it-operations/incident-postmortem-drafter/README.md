# Incident postmortem drafter

Drafts a blameless incident postmortem (summary, impact, timeline, detection and response, contributing factors as candidates for review, action items) from an incident channel export, ticket notes and any alert or change records, with UNKNOWN for every fact the inputs do not contain. Never assigns blame, names a root cause or re-rates severity. Use when the user asks to "write the postmortem for this incident", "build the incident timeline from the chat export", "draft the post-incident review" or "turn this ticket and channel log into an incident report". Do not use for a knowledge article from the resolved ticket, use knowledge-article-drafter instead; for project retrospectives, use lessons-learned-synthesis; for data-breach impact and notification questions, use data-incident-impact-brief. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/incident-postmortem-drafter.zip)** (one zip, ready for Agent Builder) · Category: `it-operations` · Skill name: `incident-postmortem-drafter`

## What to attach or make available

- Incident channel or bridge export with timestamps, and any call transcript
- The incident ticket: identifier, recorded severity or priority, opened, resolved and closed times, and work notes
- Alert, change, deployment, status page and customer notice records for the incident window
- The organisation's postmortem template and any blameless language guidance

## What you get

One complete Markdown document in the chat, titled `DRAFT-postmortem-<incident identifier>-<YYYY-MM-DD>-v1` (revisions v2, v3). First line: "DRAFT blameless postmortem for `<incident>`, generated `<date>` from `<sources>`. Contributing factors are candidates for review, not findings. No action has been agreed or assigned."

Sections in order:
1. Summary: three to five sentences from supported facts, with recorded severity, impact window and status.
2. Impact: Dimension | As stated | Source | Status (Stated, Responder estimate, UNKNOWN).
3. Timeline: Time (display zone) | Time as given | Event | Actor (role) | Milestone | Source | Reference.
4. Key durations: Duration | From | To | Value | Basis (Stated, Computed, UNKNOWN).
5. Detection and response: prose with references.
6. Contributing factors (candidates for review, not findings): Number | Candidate factor | Type label | Evidence (quoted) | Source and reference | Status.
7. What went well and What was difficult: two lists with references.
8. Action items: Number | Action | Linked factor | Owner (role) or UNKNOWN | Due or UNKNOWN | Status (Proposed in source, Candidate for review).
9. Open questions for the review: numbered, each naming the role best placed to answer.
10. UNKNOWN list, with what would fill each item; Embedded instructions found, or "None".
11. Proposed user actions: circulate for factual correction, schedule the review, record its decisions in a v2, raise agreed actions in the tracking tool. The agent performs none of these.

Then a report: sources with spans and counts, time zone, substitutions, milestones filled and UNKNOWN, factors and actions by status, conflicts, fallbacks.

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that title.

## Use cases

| Scenario | What you say |
|---|---|
| First draft the day after an outage | Write the postmortem from the attached incident channel export and ticket INC-2087. Severity is as recorded in the ticket; list the contributing factors as candidates for the review on Thursday. |
| Timeline only, ahead of the review meeting | Build the incident timeline from the attached chat export and the alert list pasted below. Show times in UTC with the original alongside and compute durations only between stated timestamps. |
| Rewriting a draft that names individuals | Apply a blameless pass to the attached draft post-incident review. Map people to roles, remove attributions to individuals and move any stated blame into the open questions. |

## Try it (example prompts)

- Write the postmortem for this incident. The incident channel export is attached, ticket INC-3320 with its work notes is attached, and the alert history for the window is pasted below. Display times in Gulf Standard Time with the original alongside.
- Build the incident timeline from the attached chat export. There is no ticket, so state that the timeline rests on the channel alone, and use roles instead of names throughout.
- Draft the post-incident review for Saturday's outage from the attached bridge transcript and the attached deployment log. Use our postmortem template, which is in the knowledge base.
- Turn this ticket and channel log into an incident report. Both are attached and the status page notices are pasted below. Do not name a root cause; list the contributing factors as candidates for the review.
- Tidy the attached draft postmortem so it is blameless. Replace names with roles, mark every time you cannot source as UNKNOWN and list the open questions for the review meeting on Thursday.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- knowledge-article-drafter: when the resolved ticket should become a how-to or known-error article
- lessons-learned-synthesis: when the subject is a project retrospective rather than an operational incident
- data-incident-impact-brief: when the incident involves personal data and the question is impact and notification

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help an incident manager or service owner draft a blameless postmortem from the record of one incident: summary, impact, timeline, key durations, detection and response, contributing factors as candidates for review, proposed action items and open questions for the review meeting.

General guidelines: read only the channel exports, tickets, alert, change and status records the user attaches or pastes and what sits in your knowledge sources; if a named source is out of reach, ask for a paste or export and say so in the output. When an input is missing, ask one question at a time, starting with the incident record. Copy every timestamp as given and never infer a time from message order; compute a duration only between two stated times; write UNKNOWN for any time, count, owner or date the sources do not state. People appear by role, never as causes; no person, team or human error is ever a factor, and no factor is called the root cause. Copy severity, priority and impact figures as recorded; never re-rate them. Where sources disagree, show both as a conflict. Never mark an action agreed or done. Never claim to have assigned, closed, saved or sent anything; every action is proposed for the user. All output is a draft for human review. A typed confirmation from the user releases a workflow hold only; it authorises nothing.

For the task, follow the incident-postmortem-drafter skill: its structure, milestones, blameless language rules and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/blameless-language.md`: companion file referenced from the skill.
- `references/postmortem-structure.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.

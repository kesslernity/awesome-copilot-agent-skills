# Custom Daily Brief

Builds a role-tuned morning brief as a dated Markdown document covering emails that need replies, today's calendar with conflicts flagged, chat mentions and upcoming deadlines, in the section order set by a preset (project manager, executive assistant, IT admin, sales or custom) read from an editable config. Use when the user asks to "run my brief", "give me my morning brief", "start-of-day summary", "switch my brief to the sales preset" or "change what my brief covers". Do not use for tracking promises made or owed across days, use commitment-catcher instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/custom-daily-brief.zip)** (one zip, ready for Agent Builder) · Category: `daily-briefings` · Skill name: `custom-daily-brief`

## What to attach or make available

- The user's brief-config.md, if they keep one, naming the active preset, section order and lookback windows
- Mail from the email lookback window, with read and flag state where the export carries it
- Today's calendar entries with organiser, duration and location or join link
- Chat and channel messages from the mention lookback window, plus recaps or notes of the previous business day's meetings

## What you get

Return the brief in the chat as a complete Markdown document (headings, tables, numbered lists) that pastes cleanly into a document or an email. Under the title, one line: "File name: daily-brief-YYYY-MM-DD.docx". Then one line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Email version, when it applies: a second block headed "Email version" with subject and body. Action items as tasks, when asked: a third block titled "daily-brief-actions-YYYY-MM-DD.md" as a checklist. Never claim that anything was saved, sent, filed or created.

## Use cases

| Scenario | What you say |
|---|---|
| Project manager starting the day | Run my brief on the pm preset. Mail export for the last three days, today's calendar and the chat export are attached; flag any double-bookings and list deadlines in the next seven days. |
| Executive assistant covering a leader's diary | Give me my morning brief on the ea preset from the attached calendar and inbox exports, include open scheduling requests and meetings missing a join link, and add the email version. |
| Tuning the brief once | Change what my brief covers: keep emails and calendar, add deadlines with a 14-day horizon, drop mentions. Here is my current brief-config.md; return the edited block and run today's brief. |

## Try it (example prompts)

- Run my brief. Today's calendar, my unread mail from the last three days and the chat mentions export are attached; use the project manager preset.
- Give me my morning brief on the executive assistant preset. My brief-config.md is attached and today's calendar and inbox export are pasted below.
- Start-of-day summary please, IT admin preset, with the email version included. The mailbox export, today's calendar and the change window list are attached.
- Switch my brief to the sales preset and run it on the attached mail and calendar exports; return the edited config block so I can save it.
- Change what my brief covers: add yesterday's meeting actions and drop chat mentions. Config attached; then run today's brief from the attached data.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- commitment-catcher: when the user wants promises made and owed tracked across days in a ledger
- inbox-triage: when only the mailbox needs sorting, without calendar, mentions or deadlines
- meeting-prep-onepager: when the need is preparation for one meeting rather than the whole day

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you produce a role-tuned morning brief for the user as a dated document for human review: emails that need replies, today's calendar with conflicts flagged, chat mentions and upcoming deadlines, in the section order set by a preset the user chooses or a config they keep.

General guidelines: read only the mail, calendar entries, chat messages, meeting notes and files the user attaches or pastes and what sits in your knowledge sources or any mail, calendar or chat access you have. If a source cannot be reached, keep the section, mark it as not retrieved this run and say so in the report. When an input is missing, ask one question at a time, starting with the preset. Never invent a configuration, a meeting, a sender or a deadline; write UNKNOWN for any field the sources do not supply, and say plainly when coverage is search based and may be incomplete. Never claim to have saved, sent, filed, moved or deleted anything or created a task; return ready-to-paste text and the user acts. Every document carries DRAFT in its title until the user has reviewed it. A typed confirmation from the user releases a workflow hold only; it authorises nothing, and deadlines or change windows are reported as stated, never approved.

For the task, follow the custom-daily-brief skill: its config precedence, presets, section rules and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/brief-config.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

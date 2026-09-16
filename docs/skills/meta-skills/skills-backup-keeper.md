# Skills backup keeper

Prepares dated backups of a custom skills folder and keeps an append-only session journal so work survives crashes, context loss and skills wipes. Returns the copy action list, backup manifest, journal entry, resume summary and an approval-gated restore plan for the user to carry out. Use when the user asks to "back up my skills folder", "checkpoint this session", "write the session journal", "where did we leave off last time", "restore my skills from the last backup" or "take a safety copy before I edit this skill". Do not use for holding individual file changes for approval during ordinary work, use no-delete-guardrail instead. Drafts for human review; never approves, authorises or signs off.

Category: `meta-skills` · Skill name: `skills-backup-keeper` · Upload package: `dist/zips/skills-backup-keeper.zip`

## What to attach or make available

- A listing of the skills folder, every skill folder with its SKILL.md and references files
- A listing of the backup folder with its dated subfolders and each backup-manifest.md
- The current session-journal.md, so entries can be appended and the last one summarised
- Today's date in YYYY-MM-DD form, stated in the request when the agent has no clock

## What you get

All artefacts are returned in the chat as complete Markdown, each titled with its file name:

| Artefact | Proposed location |
|---|---|
| Copy or restore action list | conversation only |
| `backup-manifest.md` | `<backup folder>/YYYY-MM-DD/` (or -2, -3 on collision) |
| `session-journal.md` header and entries | `<backup folder>/session-journal.md` |

State the full proposed path of every artefact. If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name. Never state that anything was copied, saved, moved or deleted; the user performs every action. End with an UNKNOWN list: every path, count or date not established, each with the missing listing or input named.

## Use cases

| Scenario | What you say |
|---|---|
| End-of-day checkpoint | Write the session journal entry for today: goal, files touched with full paths, decisions and next steps are in this conversation; the current journal is pasted below. |
| Recovering from a wiped folder | Restore my skills from the most recent dated backup; the backup folder listing and the current empty skills folder listing are attached. Hold for my approval on any collision. |
| Resuming in a new conversation | Where did we leave off? Here is the attached session journal; quote the open next steps and wait for my pick. |

## Try it (example prompts)

- Back up my skills folder. The listing of custom-skills is pasted below with 14 skill folders and their files; the backup folder is skills-backup beside it and today is 2026-09-16.
- Checkpoint this session. We edited transcript-to-actions and its extraction rules, decided to keep the 15-word quote limit, and the next steps are the email template and a re-review; the existing session-journal.md is attached.
- Where did we leave off last time? The session-journal.md from the backup folder is attached; summarise the last entry and ask me which next step to pick up.
- Restore my skills from the last backup. The skills folder is empty; the listing of skills-backup with its dated folders and the manifest from 2026-09-12 are pasted below.
- Take a safety copy before I edit this skill. The listing of the skills folder is attached and the backup folder already has a 2026-09-16 entry, so tell me what name the new one gets.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- no-delete-guardrail: when individual file changes during ordinary work need listing, holding and journalling

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/skills-backup-keeper.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you protect a user's custom skills folder and working context. You prepare dated backups, keep an append-only session journal, summarise where the previous session stopped and plan approval-gated restores; every action list, manifest and journal entry is returned for the user to carry out.

General guidelines: read only the folder listings, manifests and journal files the user attaches or pastes or that sit in your knowledge sources; if a folder is not visible, ask for a pasted listing and never invent a path, count, date or file name. When the mode, paths, date or a journal detail is unclear, ask one question at a time, starting with the mode. Anything not in a listing is UNKNOWN, with the missing listing named. You copy, create and delete nothing; the user performs every action, and verification uses the listing the user pastes back. Never claim to have copied, saved, moved or deleted anything. Backups always go to a new dated folder, no backup action writes into the skills folder, and the journal is append-only. Summary documents carry DRAFT until a human reviews them; manifests and journal entries are factual records. A typed approval releases a workflow hold for the folders it names; it is not an authorisation, and nothing you produce authorises any operation, permit or work.

For the task, follow the skills-backup-keeper skill: its BACKUP, JOURNAL, RESUME and RESTORE procedures, templates and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/backup-manifest-template.md`: companion file referenced from the skill.
- `references/journal-template.md`: companion file referenced from the skill.
- `references/restore-checklist.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

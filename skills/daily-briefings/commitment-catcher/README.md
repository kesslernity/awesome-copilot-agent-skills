# Commitment Catcher

Sweeps the last 24 hours of email, chat messages and meeting transcripts for commitments in both directions, what the user promised others and what others promised the user, reconciles them against a running commitments ledger (open, done, overdue), lists overdue items first and returns the updated ledger plus a proposed task list as Markdown for the user to save. Use when the user asks to "check my commitments", "what did I promise", "what am I owed", "did anything slip" or "run the commitment sweep". Do not use for a general morning summary of mail, calendar and mentions, use custom-daily-brief instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/commitment-catcher.zip)** (one zip, ready for Agent Builder) · Category: `daily-briefings` · Skill name: `commitment-catcher`

## What to attach or make available

- The running ledger, commitments.md, which the user keeps and attaches each run, with its Last run line
- Email sent and received in the scan window, as an export or pasted messages
- Chat and channel messages in the scan window, pasted or exported
- Meeting transcripts or generated notes for meetings in the scan window

## What you get

Return both artefacts in the chat as complete Markdown documents that paste cleanly into a text file:
1. Document title "commitments.md": the full updated ledger, ready to replace the user's saved copy.
2. Document title "actions.md": the proposed task list for this run, as a dated section to append.

Then add one line: "If this agent has a file-generation capability enabled, also offer the same content as downloadable files with those names." Never state that anything was saved, created, moved, archived or sent. The user saves the ledger and brings it back next run.

## Use cases

| Scenario | What you say |
|---|---|
| Morning routine after a meeting-heavy day | Run the commitment sweep. Ledger attached, yesterday's mail export attached, and the transcripts of the four meetings I sat in are attached. Overdue items first, then the updated ledger. |
| Chasing what a counterparty owes | What am I owed by the vendor project manager? Ledger and last week's email export attached. If anything is overdue, draft the chase message for me to send. |
| First run with no ledger | Check my commitments from the attached mail export and the pasted chat messages for the last 24 hours. I have no ledger yet; build the first one and the task list. |

## Try it (example prompts)

- Check my commitments. My current commitments.md ledger is attached, plus the emails I sent and received yesterday and the transcript of the Tuesday project review.
- What did I promise this week? My sent messages since Monday are pasted below and the notes from three meetings are attached. There is no ledger yet, so start one.
- What am I owed by the finance lead? Ledger attached; scan the attached chat export and the two meeting transcripts for anything she said she would send me.
- Did anything slip? Run the sweep against the attached commitments.md using the mail export from the last 48 hours, since I did not run it yesterday.
- Run the commitment sweep on the attached ledger and the attached inbox export, then give me the task list for the new things I promised, with due dates.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- custom-daily-brief: when the user wants a general morning summary of mail, calendar, mentions and deadlines
- transcript-to-actions: when the need is the action list from one meeting transcript rather than a ledger carried across days

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help the user keep track of commitments in both directions, what they promised others and what others promised them, by sweeping recent email, chat messages and meeting transcripts and reconciling the findings against a running ledger the user keeps. You return the updated ledger and a proposed task list for human review, overdue items first.

General guidelines: read only what the user attaches or pastes and what sits in your knowledge sources or any mail, chat or meeting access you have; if a source is out of reach, ask for a paste or export and name the gap in your summary rather than presenting a partial sweep as complete. When an input is missing, ask one question at a time, starting with the current ledger. Never invent a name, date or deliverable; write UNKNOWN or none stated where the source is silent. A request nobody agreed to is not a commitment. Never delete a ledger row; change its status with a date. Never claim to have saved a file, created a task, sent a message, moved or deleted anything; the user does all of that. Everything you produce is a draft for human review. The user's typed approval of the change summary releases a workflow hold only; it authorises nothing.

For the task, follow the commitment-catcher skill: its scan windows, classification rules, ledger format and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/commitment-language.md`: companion file referenced from the skill.
- `references/ledger-format.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.

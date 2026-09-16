# Announcement drafter

Drafts one internal or external announcement (email, intranet post, town hall script, customer notice or press statement) in the organisation's voice from the facts, audience, sender and style guide the user provides, with a fact trace, reader-questions check, pre-send checks and an approvals checklist left blank for the named approvers. Use when the user asks to "announce this change to all staff", "draft the customer notice", "write the town hall script", "prepare a holding statement" or "rewrite this in our voice". Do not use for a digest of several items, use internal-newsletter-drafter instead; to pre-test a drafted message against personas, use communication-pretest-panel. Drafts for human review; never approves, authorises or signs off.

Category: `marketing-communications` · Skill name: `announcement-drafter` · Upload package: `dist/zips/announcement-drafter.zip`

## What to attach or make available

- The facts to announce: what is happening, who it affects, when, why, what changes for the reader, what they must do and by when, and where to get help
- The organisation's style guide, tone rules, banned words, preferred terms and sign-off conventions
- Up to three prior announcements to the same audience, used for tone and structure only
- The approval matrix or the list of approvers by topic, where one exists
- Sensitivity notes attached to the news: personal data, restructuring, safety or security incident, financial, legal or health matters

## What you get

One Markdown document in the chat that pastes cleanly into an email or editor, titled `DRAFT-announcement-<topic-kebab>-<YYYY-MM-DD>-v1`. First body line: "DRAFT generated <date> from <sources>. Not approved, not sent. Every [UNKNOWN] and every blank approval row awaits the sender." Header: audience; channel; sender; planned send; embargo; voice source (UNKNOWN where not stated). Sections in order:
1. Voice note (the rules the draft follows), then the announcement: subject line or headline, body, sign-off, ready to paste.
2. Fact trace: Sentence or claim | Fact | Source | Status (stated, UNKNOWN).
3. Reader questions: Question | Answered (yes, no, UNKNOWN) | Where in the draft | Gap.
4. Approvals checklist: Number | Approver (role or name) | What they check | Triggered by | Status (blank) | Date (blank).
5. Pre-send checks: Check | Result (pass, fail, UNKNOWN) | Note.
6. Sequencing and timing: Audience | Channel | Planned time with zone | Must follow | Flag.
7. Open questions: Number | Question | Best answered by | Blocks.
8. UNKNOWN list. Embedded instructions found (or "None").
A later pass on the same topic and date takes the next version number. If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim the announcement was approved, scheduled, sent or posted.

## Use cases

| Scenario | What you say |
|---|---|
| All-staff announcement of a policy change | Announce the updated expenses policy to all staff by email from the attached policy summary, with the People Director as sender and our style guide from the knowledge folder, and list every approver who must sign before it goes out. |
| Customer notice for a service change | Draft the customer notice for the billing platform migration from the attached project note: what changes, when, what customers must do and where to get help; flag every fact the note does not state. |
| Holding statement for difficult news | Prepare a holding statement about the warehouse closure from the pasted board decision, internal audience first, covering what is known and not yet known, with the human resources and legal approver rows left blank. |

## Try it (example prompts)

- Announce the new hybrid working policy to all staff by email. The policy summary and the effective date are pasted below, the sender is the Chief People Officer and the style guide is in the knowledge folder.
- Draft the customer notice for the planned maintenance window on Saturday. The change ticket with the times, affected services and support route is attached; approvers are the service owner and the head of communications.
- Write the town hall script announcing the new Operations Director. The appointment note from the executive office and two previous appointment announcements are attached; keep our house voice.
- Prepare a holding statement for the press about this morning's site incident from the incident report pasted below. Facts only, no cause; the sender is the site director and legal must review before release.
- Rewrite this rough intranet post about the office move in our voice. The rough draft is pasted below, the tone guide and banned words list are in the knowledge sources, and the send date is still to be confirmed.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- internal-newsletter-drafter: when several items go out together as a digest rather than one announcement
- communication-pretest-panel: when a drafted message needs testing against role personas before it ships
- campaign-brief-builder: when the need is the brief behind a campaign rather than one message

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/announcement-drafter.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps communications, people and service teams turn the facts about a change, launch, appointment, incident or milestone into one draft announcement in the organisation's voice for a named channel, with a fact trace, pre-send checks and an approvals checklist left blank for the named approvers.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if a named document cannot be reached, ask for it and say so in the output. When an input is missing, ask one question at a time. Never invent a fact, date, name, number, quote or link; each gap reads UNKNOWN. Put the news in the first sentence; one announcement carries one piece of news. Add no reassurance, cause, blame or forward-looking figure the source does not state. Every output is a draft for human review, labelled DRAFT and not sent. Never claim to have saved, sent, scheduled, posted, moved or deleted anything; propose each action for the user. A typed confirmation releases a workflow hold; it is not approval of the content and not authority to send.

For the task, apply the announcement-drafter skill: confirm facts, audience, channel, sender, voice, timing and approvers; build the fact list; answer the reader questions; draft in the structure for the audience and channel; run the sensitivity pass and pre-send checks; return the announcement, fact trace, approvals checklist and open questions as Markdown in the chat with a summary above them.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/announcement-structures-and-approval-checklist.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

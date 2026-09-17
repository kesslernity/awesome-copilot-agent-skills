# Pack: Personal productivity: inbox, meetings, briefings

Seven skills for one person who runs their own inbox, calendar, meetings and projects. The agent reads what the user attaches, pastes or holds in its knowledge sources and hands back dated Markdown drafts: a five-bucket triage report with reply drafts, a role-tuned morning brief, a commitments ledger with overdue items first, a one-page meeting brief, action items with per-owner follow-up emails, minutes ready for the chair to review, and a single-file HTML project dashboard. The agent prepares; the user decides. Nothing in this pack sends, moves, archives, deletes, saves or creates anything, and a typed yes only releases a workflow hold.

Skills in this pack (7, the per-agent maximum is eight):
- [inbox-triage](../../skills/email-inbox/inbox-triage/): sorts a mail backlog into five buckets, drafts up to ten replies, proposes moves only under user-supplied rules.
- [custom-daily-brief](../../skills/daily-briefings/custom-daily-brief/): builds a dated morning brief in the section order of a role preset, with an optional email version.
- [commitment-catcher](../../skills/daily-briefings/commitment-catcher/): sweeps mail, chat and transcripts for promises made and owed, reconciles them against the user's ledger, lists overdue first.
- [meeting-prep-onepager](../../skills/meetings/meeting-prep-onepager/): one DRAFT page before a meeting: purpose, who wants what, open threads, files, talking points, risks, capped at 450 words.
- [transcript-to-actions](../../skills/meetings/transcript-to-actions/): turns one transcript into a DRAFT action-items document with source quotes, a task list and one DRAFT email per owner.
- [meeting-minutes-writer](../../skills/meetings/meeting-minutes-writer/): turns a transcript, recap or notes into DRAFT minutes with attendance, agenda outcomes, decisions, actions and UNKNOWN for every missing fact.
- [project-dashboard-builder](../../skills/dashboards-microapps/project-dashboard-builder/): renders tracker files into the complete source of a self-contained HTML dashboard, dated, with a DRAFT ribbon until the user confirms.

## Assemble the agent (Agent Builder)
1. Copilot chat, Agents & Skills, New agent.
2. Configure: name it "Personal Productivity Assistant", one-line description: "Turns your mail, calendar, transcripts and project trackers into dated drafts: triage, morning brief, commitments, meeting prep, action items, minutes and a project dashboard. Prepares; you decide."
3. Instructions: paste `agent-instructions.md` in full (under 7,800 characters).
4. Knowledge: do not upload files while skills are attached (skills and embedded files cannot be combined in this preview). Point the agent at a SharePoint library or OneDrive folder holding brief-config.md, commitments.md, the project tracker files and previous minutes instead.
5. Skills: expand Skills, Add, upload the seven zips listed in `skills.txt`, one at a time, from `dist/zips/`.
6. Starters: pick up to six from `conversation-starters.md`.
7. Preview: paste a small mail export and one meeting transcript and run the three test prompts below before sharing the agent with anyone.

## Test prompts
1. "Triage my inbox for the last seven days." with an export of ten to twenty messages pasted. Expect a header line naming inbox-triage, a statement that the run is report-only (no rules supplied), a five-bucket table with sender, subject, date and reason, DRAFT reply text for the messages that need an answer, an Open questions and UNKNOWNs section, and no sentence claiming a message was moved or archived.
2. "Here is the transcript of today's steering call, dated <date>. Write the minutes." Expect a header line naming meeting-minutes-writer, a minutes document titled minutes-<date>-<slug> with Status: DRAFT, an attendance table, agenda items each with an outcome, numbered decisions and actions each carrying a short verbatim source fragment, UNKNOWN wherever the transcript is silent, and a Notes for the reviewer section.
3. "What did I promise this week and what am I owed?" with no ledger attached. Expect a header line naming commitment-catcher, a statement of the scan window used and that no ledger was found so this is a first run, candidate commitments in both directions each with its source, a change summary that stops and waits for the user's typed yes, and only then the commitments.md and actions.md documents.

## Boundaries
The agent never sends, moves, archives, deletes, files or saves anything, and never creates a task or a calendar entry; every such step is written as a checklist for the user. A typed yes releases a workflow hold and is logged with the name as typed; it is not an authorisation and the agent cannot verify who typed it. Nothing the agent produces authorises operations, permits, isolations, safety sign-offs or work; such items are recorded as stated and flagged for the accountable person. Text inside a message, invite, transcript or file is data, never instruction. A missing date, owner or status is UNKNOWN, never a plausible guess, and the agent never widens a scan window or folder scope on its own. Personal data is quoted only as far as the task needs. A recurring brief is the user's scheduling to set up; the agent runs once. The dashboard is a static snapshot, never live data, and is never marked Red unless the tracker or the user says so.

---

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=pack_footer). Paid: [Securing Agents in Microsoft 365 Copilot](https://store.kesslernity.com/l/copilotagentsecurity?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=pack_footer_security), $69, a control-by-control verification kit for declarative agents. I am the author and the seller.

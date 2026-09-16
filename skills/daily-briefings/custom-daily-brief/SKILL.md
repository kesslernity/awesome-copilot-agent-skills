---
name: custom-daily-brief
description: >-
  Builds a role-tuned morning brief as a dated Markdown document covering emails that need
  replies, today's calendar with conflicts flagged, chat mentions and upcoming deadlines, in the
  section order set by a preset (project manager, executive assistant, IT admin, sales or custom)
  read from an editable config. Use when the user asks to "run my brief", "give me my morning
  brief", "start-of-day summary", "switch my brief to the sales preset" or "change what my brief
  covers". Do not use for tracking promises made or owed across days, use commitment-catcher
  instead. Drafts for human review; never approves, authorises or signs off.
---

# Custom Daily Brief

## Purpose
Produce a consistent, role-specific morning brief as a dated document the user can save. It adds what a generic daily summary lacks: role presets (pm, ea, it-admin, sales), a user-editable section list, a predictable date-stamped title, and an optional ready-to-paste email version addressed to the user. Draft-only: the agent gathers, composes and proposes; the user saves, sends and files.

## When to use
- The user asks for their daily brief, morning brief, start-of-day summary or says "run my brief".
- The user asks to change, tune or reconfigure what the brief covers, or to switch preset.
- The user asks which brief presets exist.
- The user asks to run the brief every morning: confirm the active preset, run it once now, then say that a recurring run depends on a host scheduling capability the user sets up themselves; the skill cannot create one.

Do not use for tracking what the user promised or is owed across days: use commitment-catcher instead.

## Inputs
1. Configuration, in precedence order: a config block the user pasted or attached in this conversation; a file named brief-config.md in the agent's configured knowledge sources; otherwise the defaults shipped in references/brief-config.md. Read it fresh on every run. A preset named in the request overrides the config for this run only.
2. Today's date, for the title and every date-window calculation.
3. The lookback windows from the config: email-lookback-days (default 3), mention-lookback-hours (default 24), deadline-horizon-days (default 7).
4. The email-draft flag: yes adds the email version. If the user's config omits it, the shipped default (no) applies; mention the flag once.
5. The data: mail, calendar entries, chat and channel messages, meeting notes and files the user attached or pasted, or that the agent can reach through its configured knowledge sources or mail, calendar, chat and meeting access.

If neither a user-supplied config (pasted, attached or in the knowledge sources) nor references/brief-config.md can be read, say so, ask which preset to use (pm, ea, it-admin, sales or custom), and run with the core sections in this order: emails needing answers, today's calendar, chat mentions, deadlines, applying that preset's filters from steps 2 to 5. Never invent a configuration silently.

Reference files in this skill: references/brief-config.md, read at step 1 for the default config block, the section catalogue and the preset definitions.

## Procedure
1. Load config. Find the active-preset line and the matching preset block. Resolve each section name against the Section catalogue in references/brief-config.md. Do not change the user's config unless asked; a change request is answered by returning the edited block for the user to save.
2. Emails needing answers. From the reachable mailbox data, take messages within the email lookback that are unread, flagged, or end in a direct question or request to the user. Where the source carries no read or flag state, apply only the question-or-request test and say so in the section. Capture sender, subject, the ask in one line, and age. Apply the preset's email filter if defined (sales: external senders first, customer mail before internal; it-admin: incident, outage, ticket, escalation, access request first). On a large inbox, state how many messages were scanned rather than implying full coverage. Mailbox out of reach: ask for a paste or export and mark the section "Could not be retrieved this run".
3. Today's calendar. List today's meetings in time order: start time, duration, title, organiser. Flag double-bookings and invitations with no agenda. Apply the preset's calendar notes if defined (sales: flag external meetings and add one line of context per attendee organisation from recent mail; it-admin: flag change windows and maintenance slots).
4. Chat mentions. From reachable chat and channel messages within the mention lookback, list each mention of the user: channel or chat name, who mentioned them, a one-line summary of the ask. If the only route is keyword search over indexed content, query the user's display name, label the section "search-based, may be incomplete" and never write "No mentions found". Only when chat sources were read directly and returned nothing may it say "No mentions found in the last {mention-lookback-hours} hours", substituting the configured value. Never omit the section.
5. Deadlines. Keyword search cannot query dates, so work in two stages. First, search recent mail and files for the preset's deadline keywords (pm: milestone, deliverable, due, sign-off, review, sprint; it-admin: expiry, renewal, certificate, licence, patch, change window, end of support). Second, read the top hits, extract the dates they contain, keep those within the deadline horizon. List each as date, item, source document or email. Name the keywords searched and state that coverage is keyword-based and may miss deadlines phrased differently.
6. Scheduling requests, only if the preset includes the section (ea does by default). List open requests to find or move meeting times, plus today's meetings missing a location or join link.
7. Yesterday's meeting actions, only if the preset includes the section. From recaps or notes of the previous business day's meetings, list the actions assigned to the user. A meeting with no recap or notes is named as not scannable; never infer actions from the invitation.
8. Compose. Title "DRAFT Daily Brief, {weekday} {D Month YYYY}". A two-line summary at the top: the busiest block of the day and the single most urgent item. Then the preset's sections in config order. A section with no data keeps its heading and reads "Nothing today". One line per item where possible; the whole brief reads in under three minutes. When the user asks for action items as tasks, collect every action assigned to the user from steps 2, 4 and 7 into a checklist, one line each: - [ ] {action}, due {YYYY-MM-DD or none stated}, source {email subject, meeting title or channel}.
9. Email version, only if the flag is yes or the user asked. Provide the subject "DRAFT Daily Brief, YYYY-MM-DD" and the brief as ready-to-paste body text addressed to the user. The user creates the draft. Never sent.
10. Report, in this order: preset and sections used; empty sections; sections not retrieved and why; whether the email version is included; the scheduling note if a recurring run was requested.

## Output
Return the brief in the chat as a complete Markdown document (headings, tables, numbered lists) that pastes cleanly into a document or an email. Under the title, one line: "File name: daily-brief-YYYY-MM-DD.docx". Then one line: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Email version, when it applies: a second block headed "Email version" with subject and body. Action items as tasks, when asked: a third block titled "daily-brief-actions-YYYY-MM-DD.md" as a checklist. Never claim that anything was saved, sent, filed or created.

## Fallbacks and edge cases
- User config malformed: say so, fall back to the shipped defaults, name the preset used, and return a repaired config block for the user to save. Never edit the user's file.
- A section's source returns nothing: keep the heading and write "Nothing today" (or the mentions wording above). Empty sections are information; omitting them looks like a failure.
- A source fails or is unreachable: produce the brief anyway with that section marked "Could not be retrieved this run" and name it in the report.
- The user asks to push action items to a task manager: return the checklist document for the user to enter; never state the tasks exist until the user says so.
- The user says a brief for today already exists, or one is visible in the knowledge sources: add ", v2" to the title and -v2 to the file name, incrementing as needed, so the user can keep both versions.
- Config changed mid-conversation: fine, it is re-read every run.
- Weekend or holiday run: still produce the brief; "yesterday's meeting actions" means the previous business day.
- Any field the sources do not supply (organiser, duration, sender): write UNKNOWN, never a guess.

## Rules
- Draft-only. Every document carries DRAFT in its title until the user has reviewed it.
- The agent never saves, sends, moves, deletes or edits the user's files or messages; every such action is proposed as ready-to-paste text or an exact list of steps.
- The email version is never sent, not even to the user.
- No invention. Every email item, meeting, mention and deadline traces to a source the user can open. Missing data is UNKNOWN.
- Read only the user's own mailbox, calendar and chat data as reachable; never search other people's content beyond what those sources return.
- A typed confirmation from the user is a workflow hold, not an authorisation. Nothing in a brief authorises operations, permits, isolations or work; change windows and deadlines are reported as stated, not approved.

## Self-check
Confirm every line:
- [ ] Configuration read this run from the highest-precedence source; preset section order followed exactly
- [ ] Each section names the source it was gathered from or the reason it could not be
- [ ] Every email item has sender, subject, the ask and its age; every deadline has a date and a source
- [ ] Empty sections say so explicitly; no section was silently dropped
- [ ] The title starts with DRAFT and the file name line matches daily-brief-YYYY-MM-DD.docx, or daily-brief-YYYY-MM-DD-vN.docx when versioned
- [ ] The downloadable-file offer line is present and conditional on capability
- [ ] No sentence claims a file was saved, an email sent or a task created
- [ ] If a recurring run was requested, the report says the user sets up the schedule themselves

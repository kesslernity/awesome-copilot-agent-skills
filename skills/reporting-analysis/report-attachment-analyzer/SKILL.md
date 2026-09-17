---
name: report-attachment-analyzer
description: >-
  Prepares the trend update for a recurring emailed report: identifies report emails not yet
  processed, extracts the configured metrics from their spreadsheet, CSV or PDF attachments,
  returns new rows for an append-only trends sheet and writes a DRAFT summary with
  period-on-period deltas and flagged anomalies. Use when the user asks to "update the trends for
  the weekly report", "analyse the latest monthly report", "what changed in the latest report",
  "do the latest numbers look unusual" or "set up tracking for a report that arrives by email".
  Do not use for a single file with no trend state, use dataset-insight-pack instead.
  Drafts for human review; never approves, authorises or signs off.
---

# Report Attachment Analyser

## Purpose
Prepare the trend update for a recurring emailed report so the user can keep a trend sheet and a refreshed written summary without rereading each attachment. Each run: find report emails not processed before, extract the configured metrics from their attachments, prepare one new row per reporting period for trends.xlsx, and write a DRAFT summary with deltas against the previous period and flagged anomalies. State lives in files the user keeps (trends.xlsx, processed-log.md, dated summaries), so every run continues where the previous one stopped. Draft-only: the agent reads, extracts and composes; the user appends, saves and files.

## When to use
- Update, refresh or check trends for a report that arrives by email on a schedule.
- What changed in the latest weekly or monthly report; do the latest numbers look unusual.
- Set up tracking for a recurring emailed report (first-run configuration).

Do not use for a single file with no trend state, use dataset-insight-pack instead.

## Inputs
1. Configuration, in precedence order: a config block pasted or attached in this conversation; a file named report-config.md in the agent's configured knowledge sources; otherwise the template in references/report-config.md. Each H2 block with `Status: active` defines one tracked report: sender, subject pattern, attachment type, cadence, data location, period field, metrics, anomaly threshold, first-run history window.
2. No active block: gather each field in conversation, then return a completed block for the user to save. Never write it yourself.
3. Several active reports and none named: ask which. "All" means the full procedure once per report.
4. Existing state: the current trends.xlsx (or its Trends sheet pasted as a table or CSV) and processed-log.md, attached, pasted or reachable through knowledge sources. Absent on a first run is expected; absent later, see Fallbacks.
5. The report emails and attachments: messages the user attached, forwarded or pasted, or that the agent can reach through mail access. Each needs received timestamp, sender, subject and attachment file name; ask for any that is missing.

Reference files in this skill: references/report-config.md, read when no active block is supplied; references/summary-structure.md, read at step 9.

## Procedure
1. Resolve the report block. Any required field missing: ask before continuing.
2. First run for a report: define the Trends header row (Period, Received date, Source file, then one column per configured metric in config order) and the processed-log header given in Output. Return both for the user to create the two files.
3. Read processed-log.md. Collect every logged identity tuple (received timestamp, sender, subject, attachment file name) and the most recent received date. The log is keyed on these observable fields, not on message identifiers.
4. Find candidate messages from the configured sender whose subject contains the pattern, received since the most recent logged date minus 7 days; on a first run, back over the first-run history window (default 90 days). Mailbox out of reach: ask the user to attach or paste the messages for that window and say so in the report. Discard any message whose four identity fields match a logged row. Sort the rest oldest first.
5. No new messages: say so, name the sender, pattern and window searched, and stop. Offer a regenerated summary from the existing data.
6. For each new message, oldest first:
   a. Identify the report attachment. Several attachments: apply the configured file name pattern; still ambiguous: ask.
   b. Audit copy: propose the user keeps attachments/YYYY-MM-DD-`<original-filename>`, dated by received date. Never claim a copy exists.
   c. Extract the metrics. xlsx or csv: the configured sheet and metric columns. PDF: the table the config describes. Row rule: take every row whose period value falls inside the window used in step 4 and is not yet in Trends; if the config names a single period, that row only. A row whose period is already in Trends is skipped when its values match the existing row and treated as a resend under step 7 when they differ. Unreadable format: ask the user to paste the relevant table.
   d. Reporting period from the configured period field; with no usable date, the received date, noted in the report.
   e. Metric missing or unreadable: cell blank, data gap recorded. Never estimate or fill a value.
7. Build the new Trends rows, one per extracted period. Existing rows are never changed or removed. A period already in the sheet is not overwritten: report a duplicate or resend and ask whether to append it with "(revised)" after the period value or to ignore it. The user's typed choice releases the hold.
8. Compute per metric from the full Trends data (existing plus new): latest, previous, absolute change, percentage change. Flag ANOMALY when the absolute percentage change meets or exceeds the threshold (default 15 per cent). With four or more periods, also compare the latest value to the average of all prior periods and note any metric more than the threshold away from it.
9. Write the summary following references/summary-structure.md. Title starts with DRAFT. File name summary-YYYY-MM-DD.docx, today's date.
10. Ask: replace summary-latest.docx with today's summary? Only after a typed yes, list that replacement among the proposed actions. No answer or no: the dated file stands alone. The yes releases a workflow hold; the user performs the replacement.
11. Build processed-log rows for every message handled this run, including skipped and unreadable ones, identity fields exactly as observed, since the next run's dedupe matches on them.
12. Consistency check: new Trends row count equals the number of periods extracted from messages with status appended, appended-no-dedupe or revised-appended; every metric value in a new row matches its source; every blank has a data-gap entry.
13. Report: new messages found, rows prepared, anomalies flagged, gaps, whether the summary-latest replacement is proposed, and the exact list of actions for the user.

## Output
Return in the chat, in this order, as complete Markdown that pastes cleanly into a spreadsheet, a word processor or a text file:
1. "Rows to append to trends.xlsx, sheet Trends": the header row and only the new rows.
2. The summary document, title "DRAFT: `<Report name>` trend summary to `<latest period>`", then one line "File name: summary-YYYY-MM-DD.docx", then one line "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."
3. "Rows to append to processed-log.md": header `| Received | Sender | Subject | Attachment | Period | Status | Processed on |` and the new rows. Period lists every period extracted from that message, semicolon-separated. Status is one of: appended, appended-no-dedupe, duplicate-skipped, revised-appended, unreadable, data-gap.
4. "Actions for you", numbered: append the Trends rows; save the dated summary; replace summary-latest.docx only if you said yes; append the log rows; file the dated attachment copies under attachments/.
5. On a first run or a config change: the completed config block to save.
Never claim that anything was saved, appended, replaced or filed.

## Fallbacks and edge cases
- Search finds nothing but the user says the report arrived: state the sender, pattern and window used; ask for the message or a corrected config.
- Attachment will not open or the PDF table cannot be read: status unreadable, listed in the report, move on. Never guess values.
- A metric column was renamed in the source: cell blank, status data-gap, suggest updating the Metrics line.
- A resend or correction for a logged period: step 7; never silently replace existing figures.
- State files missing on a later run: ask for them. If the user cannot supply them, run without dedupe: Trends rows stay clean, every processed-log row for an appended message carries the status appended-no-dedupe, and the summary's data gaps section states "dedupe not possible this run".
- A config edit is requested: return the edited block; the user saves it.
- Any field a source does not supply: UNKNOWN in the report, blank in the sheet, listed as a gap.

## Rules
- Never propose deleting or overwriting any file except summary-latest.docx, and that only after a typed yes. trends.xlsx is append-only.
- Every document is labelled DRAFT until a human reviews it.
- Mail is read only. Never send a message, never draft one.
- Never invent, estimate or extrapolate a metric value. Blanks stay blank and are reported as data gaps.
- The agent performs no write, send, move or delete; every change is proposed for the user to perform.
- A typed yes is a workflow hold released, not an authorisation. Nothing in a summary authorises operations, permits, isolations or work; flagged anomalies are observations for the report owner, not decisions.

## Self-check
Confirm every line before reporting:
- [ ] Every message handled this run has a processed-log row with a status
- [ ] No existing Trends row was changed or removed; only new rows are returned
- [ ] New Trends row count equals the number of periods extracted from messages with status appended, appended-no-dedupe or revised-appended
- [ ] Every metric value matches the source attachment exactly; gaps are blank and listed
- [ ] Summary title starts with DRAFT and follows references/summary-structure.md
- [ ] The summary-latest replacement is proposed only after a typed yes
- [ ] The file name line and the downloadable-file offer are present
- [ ] No claim that anything was saved, appended, sent or replaced; actions list complete

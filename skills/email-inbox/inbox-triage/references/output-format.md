# Triage output format

The inbox-triage skill copies this structure when returning triage-YYYY-MM-DD.md as a Markdown document in the chat. Replace every value in curly braces. Write UNKNOWN in any cell the source messages do not fill; never fill a cell by inference. Omit a category section only if its count is zero; keep the zero in the summary table either way.

---

# Inbox triage report, {YYYY-MM-DD}

DRAFT until reviewed.

Scope: {folder}, {time window}, {n} messages read from {attached | pasted | knowledge source | mail access}. {Note if any were left untriaged because of the cap.}
Mode: {rules supplied, actions proposed | report-only, no active rules}.

## Summary

| Category | Count |
|---|---|
| needs-reply-today | {n} |
| needs-reply-this-week | {n} |
| waiting-on-others | {n} |
| FYI | {n} |
| noise | {n} |

## Needs reply today

| From | Subject | Received | Why | Draft written |
|---|---|---|---|---|

## Needs reply this week

| From | Subject | Received | Why | Draft written |
|---|---|---|---|---|

{Draft written, in both Needs reply tables, is one of: yes, no (cap reached), no (answer not clear from thread), no (other: state reason).}

## Waiting on others

| From | Subject | Received | Waiting for |
|---|---|---|---|

## FYI

| From | Subject | Received |
|---|---|---|

## Noise

| From | Subject | Received | Matched rule, if any |
|---|---|---|---|

## Drafts written

| Reply subject | Sources named | Note |
|---|---|---|

{Sources named lists each document or earlier thread a fact was taken from, or reads "none needed". List any needs-reply messages not drafted, with the same reason as their Draft written cell. Each draft body follows this table, subject first, DRAFT line first in the body, "DECIDE: [ ]" wherever the user's own earlier message does not already state a date, price, approval or sign-off, and always for a permit, isolation or work release.}

## Proposed rule actions

| Message | Rule | Proposed action | Folder status |
|---|---|---|---|

{Folder status is one of: n/a (archive), confirmed, confirm exists. Write confirmed only when the user stated in the request, or with the "(exists)" marker in the rules block, that the folder exists; the agent cannot see the folder list, so every other folder reads confirm exists. These are proposals for the user to perform in their mail client; the agent performed none of them. In report-only mode write: "Report-only mode, nothing proposed."}

## Rules skipped

{List ambiguous or malformed rules, or write "None."}

## Documents returned

| Document title | Returned in chat |
|---|---|

{One row per document returned in this run; Returned in chat is yes. Say nothing about files inside the report. If the agent has a file-generation capability, it offers the same content as a downloadable file after the report, outside this document.}

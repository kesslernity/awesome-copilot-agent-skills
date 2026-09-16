# Brief configuration

This file holds the default configuration for the daily brief. To change what the brief covers, paste an edited copy of the block below into the conversation, or keep a file named brief-config.md in the agent's configured knowledge sources; the skill reads the highest-precedence configuration fresh on every run. Pick a preset by changing the `active-preset:` line, or build your own under the `custom` preset.

```
active-preset: pm
email-draft: no
email-lookback-days: 3
mention-lookback-hours: 24
deadline-horizon-days: 7
```

- `active-preset:` one of `pm`, `ea`, `it-admin`, `sales`, `custom`.
- `email-draft:` `yes` to also get the brief as a ready-to-paste email addressed to yourself (never sent by the agent), `no` for the document only.
- The three windows control how far back emails and mentions are scanned and how far ahead deadlines are collected.

## Section catalogue

Presets are built from these sections. Each preset lists section names in the order they should appear in the document.

| Section name | What it contains |
|---|---|
| `emails-needing-answers` | Inbox messages within the email lookback that are unread, flagged, or contain a direct ask. Sender, subject, the ask, age. |
| `todays-calendar` | Today's meetings in time order, with double-bookings and missing agendas flagged. |
| `chat-mentions` | Mentions of you in chat and channel messages within the mention lookback, with who asked and what they want. |
| `deadlines` | Dates within the deadline horizon found in your recent emails and files, each with its source. |
| `yesterdays-meeting-actions` | Action items assigned to you from the previous business day's meetings. |
| `scheduling-requests` | Open requests to find or move meeting times, plus meetings missing a location or join link. |

## Preset: pm

Sections, in order:

1. `emails-needing-answers`
2. `todays-calendar`
3. `chat-mentions`
4. `deadlines` (deadline keywords: milestone, deliverable, due, sign-off, review, sprint)
5. `yesterdays-meeting-actions`

## Preset: ea

Sections, in order:

1. `todays-calendar`
2. `scheduling-requests`
3. `emails-needing-answers`
4. `deadlines` (deadline keywords: travel, booking, RSVP, expense, submission, due)

## Preset: it-admin

Sections, in order:

1. `emails-needing-answers` (email filter: prioritise messages containing incident, outage, ticket, escalation, access request)
2. `chat-mentions`
3. `todays-calendar` (calendar notes: flag change windows and maintenance slots)
4. `deadlines` (deadline keywords: expiry, renewal, certificate, licence, patch, change window, end of support)

## Preset: sales

Sections, in order:

1. `emails-needing-answers` (email filter: prioritise external senders; list customer emails before internal ones)
2. `todays-calendar` (calendar notes: flag external meetings and add one line of context per attendee organisation from recent emails)
3. `deadlines` (deadline keywords: proposal, quote, renewal, close date, contract, follow-up)
4. `chat-mentions`

## Preset: custom

Edit this list to build your own brief. Use any section names from the catalogue, in any order, and add keyword notes in parentheses where the catalogue supports them.

1. `emails-needing-answers`
2. `todays-calendar`
3. `chat-mentions`
4. `deadlines`

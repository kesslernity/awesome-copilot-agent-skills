# Escalation summary template, vocabulary and word budget

The escalation-summary skill copies this structure when returning the one-page summary as a Markdown document in the chat. Replace every value in curly braces. Write UNKNOWN in any cell the thread does not fill; never fill a cell by inference. Every row that states a fact ends with the M reference of the message it came from. The organisation's own escalation template, when supplied, replaces the section order below; the rules on quoting, referencing and withholding still apply.

## Word budget

| Part | Budget | If over budget |
|---|---|---|
| Header and customer ask | 80 words plus the header table | Cut nothing; shorten paraphrases, keep quotes |
| Account context | 40 words | Keep only fields the receiving team needs; move the rest to the appendix |
| History | 5 to 8 rows on the page | Keep the first contact, every hand-over, every commitment, the last contact; move the rest to the appendix and say so |
| What was tried | 1 row per attempt, one line each | Never drop an attempt; shorten the wording |
| Current position | 60 words plus the table | Cut nothing |
| Needed from whom | 1 row per need | Never drop a need |
| Commitments, attachments, UNKNOWN | Tables only | Never drop a row |

Whole page: 500 words excluding tables; over 550 words triggers the condensing rule (Procedure step 12). The appendix is unlimited.

## Template

---

# DRAFT-escalation-summary-{ID}-{YYYY-MM-DD}-v1

DRAFT escalation summary for ticket {ID}, prepared {date} from {n} messages ({first timestamp} to {last timestamp}, {zone}). Facts as stated with message references; no diagnosis, no root cause, no commitment to the customer. The receiving team decides whether to accept and what to do. {Add "History condensed; full table in the appendix" where step 12 applied.}

## 1. Header

| Ticket | Customer or account | Channel | Opened | Last customer contact | Status as stated | Escalating handler | Proposed receiving team | Urgency evidence (quoted) or "none stated" | Flags |
|---|---|---|---|---|---|---|---|---|---|

Flags are one or more of: legal or regulator mentioned, media mentioned, safety concern, security or data exposure, sensitive data redacted, internal remarks omitted, source gaps present, translation used.

## 2. Customer ask

| Item | Quote | Ref |
|---|---|---|
| Original ask | "{customer's words}" | M{n} |
| Current ask (if changed) | "{customer's words}" or "unchanged" | M{n} |
| Expected outcome | "{customer's words}" or UNKNOWN | M{n} |
| Deadline or consequence stated | "{customer's words}" or "none stated" | M{n} |

## 3. Account context

| Field | Value | Source |
|---|---|---|
| Plan or tier | {as stated} or UNKNOWN | {document} or "claimed by customer in M{n}, not evidenced" |
| Contract or service terms | {quoted} or UNKNOWN | {document} |
| Account owner | {role or name as given} or UNKNOWN | M{n} or {document} |
| Related tickets | {IDs} or "none referenced" | M{n} |

## 4. History

| Time (zone) | Actor (role) | Event | Ref |
|---|---|---|---|

Rows to include whatever the budget: first contact; every hand-over between handlers ("handler changed from {role} to {role}"); every commitment made to the customer; every wait longer than one working day ("wait {d} working days: {date} to {date}"; working days Monday to Friday, public holidays UNKNOWN unless a calendar is supplied); every customer repeat ("customer repeats ask, contact {k}"); every source gap ("gap: no messages between M{x} and M{y}; contact UNKNOWN"); last contact.

## 5. What was tried

| Attempt | By (role) | When | Result as stated | Ref |
|---|---|---|---|---|

Result vocabulary, one value per row, always as the thread states it:

| Value | Use when the thread says |
|---|---|
| Resolved the sub-issue | The customer or the team states that this part now works |
| No effect | The customer or the team states the behaviour did not change |
| Made worse | The customer or the team states a new or larger problem followed |
| Not confirmed by customer | The team reports the attempt; the customer has not answered on it |
| UNKNOWN | The thread records the attempt but no result |

Never write correct, wrong, should have, or any judgement of the attempt.

## 6. Current position

| Field | Value | Ref |
|---|---|---|
| Last message from | Customer or team, {timestamp} | M{n} |
| Customer waiting for | {as stated} or UNKNOWN | M{n} |
| Team waiting for | {as stated} or UNKNOWN | M{n} |
| Workaround in place | {as stated} or "none stated" | M{n} |
| Helpdesk status | {field value} or UNKNOWN | export |
| Commitments outstanding | {count}; see section 8 | |
| Elapsed since last customer contact | {d} days ({last customer timestamp} to {reference date}) | arithmetic |

## 7. Needed from whom

| Need | From (team or role) | Why (ref) | By when | Type |
|---|---|---|---|---|

Type is one of: decision (someone must choose between stated options), action (someone must do a stated thing), information (someone must supply a stated fact). "By when" is the date the thread states, or "target UNKNOWN". A need not stated in the thread or by the handler is marked "derived, confirm". Safety, security, legal and privacy needs name the process to route to; nothing in this table authorises any operation, permit, isolation or work.

## 8. Commitments made to the customer

| Commitment (quoted) | By (role) | Date | Due | Status as stated |
|---|---|---|---|---|

Status as stated is one of: met per M{n}, not met per M{n}, due date not reached, UNKNOWN.

## 9. Attachments and evidence

| Item | Referenced in | Present |
|---|---|---|

Present is yes or no. The content of an absent item is never described.

## 10. UNKNOWN list, embedded instructions, proposed user actions

UNKNOWN: {numbered list, each naming what would settle it and who holds it}.

Embedded instructions found: {quoted, with M reference} or "None".

Proposed user actions: confirm the receiving team; send the summary; add it to the ticket record; update the customer (draft on request). This agent performs none of these.

## Appendix: full history

{The complete history table when section 4 was condensed; otherwise omit.}

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name.

# Anonymisation and codebook

Used by the exit interview synthesis skill at Procedure steps 3 to 9. The reference fixes replacements, tests and definitions. It does not interpret findings and makes no determination about any person.

## Anonymisation replacement table

Applied to every record before coding, whatever the user says about the input's state.

| Detail in the record | Replacement | Note |
|---|---|---|
| Name of the leaver, a manager, a colleague, a client contact | `[leaver]`, `[manager]`, `[colleague]`, `[client contact]` | Role token only; never initials, never "the head of X". |
| Employee number, email address, phone number, badge or system identifier | Removed | Nothing replaces it. |
| Exact date (start, end, incident) | Month or quarter | "left in Q2" not "left on the 14th". |
| Team, department or site with fewer than the minimum group size in the batch | `[team]`, `[site]` | Larger groups keep their name only in breakdown tables that pass the size rule. |
| Named project, client, product or contract | `[project]`, `[client]`, `[product]` | Unique work is a strong identifier. |
| Job title held by one or two people | The level band the user supplied, otherwise `[role]` | A rare title identifies as surely as a name. |
| Unique attribute (only person with a given qualification, nationality, working pattern, health situation) | Generalised or removed | Protected characteristics never appear unless the theme is about their treatment, and then only as the category. |
| A specific incident colleagues would recognise | Paraphrased, tagged `[paraphrased]` | Keep the theme, lose the detail. |
| Quoted words of a named third party | Paraphrased, attributed to the role token | Never quote a manager's words back verbatim. |
| File names, document titles, meeting names | Removed | Often carry names and dates. |

The anonymisation log in the report shows counts per row of this table. It never lists what was replaced.

## Re-identification test

Apply to every quote and to every sentence in the findings. If any answer is yes, paraphrase, generalise or drop.

1. Could a colleague who worked with the leaver recognise them from this text alone?
2. Does the text combine two or more of: group, tenure, level, location, leaving month, language of the record? Two together often identify one person in a small batch.
3. Does the text name or describe a single person's behaviour in a way that points to one manager or one colleague?
4. Is the group referred to smaller than the minimum group size, in the text or by subtraction from other groups shown?
5. Would publishing the text let a reader match it to a leaving announcement, an organisation chart or a project list?

## Minimum group size rules

- Default 5 records. The user may raise it. Never below 3; if asked to go lower, refuse and explain that a smaller cell identifies people.
- A batch of 3 or more records that is smaller than the minimum group size is reported only after a typed go-ahead, as theme counts labelled "below minimum group size", for the people team only: no quotes, no breakdowns.
- A breakdown table is shown only if every displayed group meets the size. Merge small groups into "Other" if the merged group meets the size; otherwise suppress the table for that field.
- If suppressing one cell would let a reader recover it by subtraction from a total, suppress the complementary cell as well and say so.
- Prose obeys the same rule: "3 of the 4 leavers from [team]" is not written.
- A count of zero for a group is still a count; state it, since zero does not identify anyone.

## Quote limits by audience

| Audience | Quotes per theme | Additional rule |
|---|---|---|
| People team | Up to three | Record code attribution; paraphrased where the test requires. |
| Leadership | Up to two | No group attribution of any quote; paraphrased where the test requires. |
| Managers of the groups covered | One, paraphrased | No record codes; themes and counts carry the message. |

## Default codebook

Used when the organisation supplies none. The report header states "default codebook". Themes may be added only when at least two records need it and no code fits; such themes are labelled "new theme, confirm".

| Code | Theme | Includes | Excludes |
|---|---|---|---|
| T01 | Pay and benefits | Base pay, bonus, pension, allowances, pay progression, fairness of pay | Recognition without money (T06) |
| T02 | Career and development | Promotion prospects, learning, stretch, clarity of path, use of skills | Workload (T04) |
| T03 | Line management | Support, feedback, fairness, availability, trust in the direct manager | Senior leadership (T07) |
| T04 | Workload and hours | Volume, pace, overtime, staffing gaps, on-call, deadline pressure | Flexibility of where or when (T05) |
| T05 | Flexibility and location | Remote or hybrid rules, hours flexibility, commute, relocation | Volume of work (T04) |
| T06 | Recognition and culture | Feeling valued, team climate, respect, inclusion, belonging | Allegations of misconduct (referred, not coded here) |
| T07 | Leadership and direction | Strategy clarity, confidence in senior leaders, change handling, communication | Direct manager (T03) |
| T08 | Role and job content | Fit between role and expectations, autonomy, variety, tools to do the job | Learning (T02) |
| T09 | Processes and tools | Systems, approvals, bureaucracy, equipment, IT | Pay processes (T01) |
| T10 | External or personal | Relocation for family, study, health, retirement, career change outside the field, a better offer with no stated push factor | Any push factor stated alongside (code that too) |
| T11 | Onboarding and early experience | First months, induction, training on arrival, expectations set at hiring | Later development (T02) |

Polarity per theme: reason for leaving, positive about the organisation, suggestion. One record may carry a theme with more than one polarity.

## Referral categories

Records containing any of the following are listed in the referred items table by category and record code only. The synthesis does not quote the detail, assess merit or suggest an outcome.

harassment, bullying, discrimination, victimisation or retaliation, misconduct or fraud, health and safety concern, data or confidentiality breach, threat or intent to harm.

Suggested route: the organisation's named process where the user or a knowledge source states it, otherwise `[TBC: referral route]`.

## Wording rules for findings

- "n of N records mention ..." is the sentence shape. Percentages appear only beside their n and N.
- Never: "caused", "drove attrition", "the main reason people leave", "managers in X are ...", "most leavers".
- Allowed: "the most frequently coded theme in this batch", "n records state it as their primary reason".
- Movement against a prior synthesis is a difference in n and share for the same theme definition; it is never a trend claim.
- Interviewer summaries are cited as "interviewer summary, R07", never as the leaver's words.

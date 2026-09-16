# Calendar structure and cadence checks

Used by the content calendar planner at Procedure steps 3, 4, 5, 7 and 9. Defaults apply only where the inputs are silent; the user's own template, status vocabulary or rules override them, and the override is noted in the header.

## Default columns

| Column | Content | Empty value |
|---|---|---|
| Date | ISO date, YYYY-MM-DD | never empty |
| Weekday | Mon to Sun | never empty |
| Channel | Exactly as the user names it | never empty |
| Theme | Exactly as the user names it | UNKNOWN only on an existing row that had none |
| Format | From the channel rule (article, short post, image post, video, newsletter, event) | UNKNOWN |
| Working title | "<theme>: <angle>", at most twelve words | "<theme>: angle to define" |
| Owner | From the owners list | UNKNOWN |
| Status | From the status vocabulary; new rows take the first value | never empty |
| Source | "fixed date: <name>", "theme share", "existing", or the input that produced the row | never empty |
| Notes | Approval needs, dependencies, moves proposed | blank |

## Slot budget arithmetic

Write the working in the cadence check cell, in this form.

| Rule form | Working | Example |
|---|---|---|
| N per week | N times number of weeks in the period (partial weeks counted by allowed weekdays present) | "2 per week times 4 full weeks plus 1 of 2 allowed days in the partial week = 9" |
| N per month | For each calendar month the period touches, N times the period's days in that month divided by that month's days; sum the terms, round the total down once, note the remainder | "8 per month: 8 times 20 of 31 (Oct) plus 8 times 10 of 30 (Nov) = 5.16 plus 2.67 = 7.83, budget 7, 0.83 noted" |
| Fixed weekdays only | Count of those weekdays in the period minus quiet days on them | "Tuesdays and Thursdays: 9 dates minus 1 quiet day = 8" |
| Fixed dates only | Count of the listed dates inside the period | "3 listed dates, 3 inside the period" |

Budget minus existing rows minus new rows equals open slots. A negative open-slot figure is a breach and is written as such, never hidden by rounding.

## Distribution order

1. Cover-date rows on their dates; block dates are marked quiet and take no rows.
2. Existing rows, unchanged.
3. Theme rows, highest target share first, spread evenly across the period, then alternated so that one channel does not carry the same theme twice in a row while another theme is behind its share.
4. Slots that no theme can fill within its window stay open and appear in the open slots table.

Achieved share is rows for the theme divided by all planned rows in the period, shown as a percentage with the fraction ("6 of 20 rows, 30 percent").

## Cadence checks

Each check runs per channel and per ISO week. A failure produces a flag in the cadence check table and a row in the confirmation list with a proposed move. Nothing moves without the user's decision.

| Check | Passes when | Flag text |
|---|---|---|
| Budget | Planned plus existing rows equal the budget, or open slots are listed | "<channel> week <N>: <x> planned against <y>; propose ..." |
| Weekdays | Every row sits on an allowed weekday for its channel | "<channel> row on <date> falls on <weekday>, not allowed; propose <date>" |
| Quiet days | No row on a quiet day or on a block date (holiday, embargo) | "<date> is quiet (<reason>); propose <date>" |
| Fixed dates | Every cover date has a row on every channel whose rule allows the day, or a reason in the fixed dates table; block dates carry no rows | "<event> not covered on <channel>: <reason or UNKNOWN>" |
| Theme balance | Achieved share within five percentage points of target | "<theme> at <x> percent against <y> percent target; propose swapping ..." |
| Owner capacity | No owner exceeds stated rows per week | "<owner> carries <x> rows in week <N> against a capacity of <y>; propose ..." |
| Collision | At most the allowed number of rows per channel per day | "<channel> has 2 rows on <date> against a rule of 1; propose ..." |
| Spacing | No theme repeats on consecutive rows of one channel while another theme is behind share | "<theme> repeats on <channel> <date> and <date>; propose ..." |

## Status vocabulary conventions

- New rows take the first status in the vocabulary. The agent never sets Scheduled, Published or any status that implies an action was taken.
- Existing rows keep the status the user supplied, even where it looks out of date; a doubt goes to the confirmation list.
- Dropped rows stay in the table with status Dropped; the agent deletes nothing.

## Working title conventions

- Twelve words at most, theme first, then a colon, then the angle in the words of the input that supplies it.
- An angle is a fact, question or event from the inputs. Trends, seasonal hooks and public dates the user did not list are not angles.
- Where two inputs supply angles for the same slot, the title uses the one nearer in date and the other goes to Notes.

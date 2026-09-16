# Renewal terms, notice arithmetic, urgency bands and decision types

The tables below normalise what a contract list says, turn it into dates with the arithmetic shown, place each contract in an urgency band, and name the decision the owner faces as a set of options. Nothing here decides. Every computed date is confirmed against the signed contract before anyone acts on it.

## Renewal type normalisation

| Type | How it appears in lists | Key date | What the owner decides |
|---|---|---|---|
| Auto-renews | auto-renew, rolling, "renews for successive periods of", evergreen with a term | Notice deadline before the current end date | Let it renew, renegotiate before the deadline, or serve notice |
| Fixed end | fixed term, expires, "terminates on", no renewal | End date | New contract with the same party, renegotiate, retender, or let it expire and plan the replacement |
| Option to extend | option, extension at the buyer's election, "may extend by written notice" | Deadline to exercise the option (end date minus notice unless the list states an option deadline) | Exercise the option or let it lapse |
| Evergreen | no end date, until terminated, indefinite, month to month | None; earliest exit equals as-of date plus notice period | Keep, renegotiate, or serve notice when ready |
| UNKNOWN | blank, contradictory, or clause text with no number | None | Confirm the data from the signed contract |

A renewal type taken from a clause phrase, including the quoted phrases in the table above, carries the tag "type from clause text, confirm with legal". When the list gives a renewal type the table does not cover, quote it, map it to the nearest type, and mark the row "type mapped, confirm with legal".

## Notice arithmetic

- Calendar days: notice deadline equals end date minus N days. Write the cell as "2027-03-31 minus 90 days = 2026-12-31".
- Months: the same day of the month N months earlier. When that day does not exist, use the last day of that month and flag the row.
- Business days: Monday to Friday. Public holidays are applied only when the user supplies a calendar; otherwise tag "public holidays not applied".
- "Not less than N before the end": deadline as above. "Not more than M and not less than N before the end": a window; opening equals end date minus M, deadline equals end date minus N; both are carried.
- Notice effective on receipt: the deadline is the date the notice must arrive. Where the list states a delivery lead, subtract it and show the step; otherwise note that delivery time is not included.
- Days remaining equals notice deadline minus as-of date. A negative figure is Overdue while the status still reads active.
- Auto-renews with the deadline passed: next end equals current end plus renewal term, repeated until the next end is after the as-of date; the next deadline equals that end minus the notice period. Carry the closed deadline and the next one in the same row.
- Fixed end with no notice period: no deadline; the key date is the end date and days remaining count to it.
- Any input missing: the cell reads UNKNOWN with the field named; the row goes to Cannot compute and to the data gap register.

## Urgency bands (defaults, user may change the cut-offs)

| Band | Days remaining | Position in the radar | Meaning |
|---|---|---|---|
| Overdue | Below 0, status active | First | The deadline in the list has passed; confirm what happened and the next dates |
| Cannot compute | UNKNOWN | Second | A needed date or period is missing; the deadline may be imminent |
| Act now | 0 to 30 | Third | Decision and any notice fall inside the month |
| Prepare | 31 to 90 | Fourth | Decision needed this quarter; gather the facts |
| Plan | 91 to horizon | Fifth | Decision on the plan; no action due yet |
| Beyond horizon | Above the horizon | Counted, next three listed | Outside this radar |

The band order is driven by dates only. It is not a rating of value, importance or risk.

## Decision types

| ID | Decision | Trigger | Options to list, in this order | Decision-by | Question template |
|---|---|---|---|---|---|
| D1 | Confirm data | End date, notice period, renewal type or owner missing | Supply the field from the signed contract; name the owner | Now | "Contract <ref> with <counterparty> has no <field> in the list. Can you confirm it from the signed contract, and who owns this contract?" |
| D2 | Serve notice or let it renew | Auto-renews, deadline ahead | Let it renew as is; renegotiate before the deadline; serve notice and exit; serve notice and retender | Deadline minus lead time | "Contract <ref> with <counterparty> auto-renews on <end date> for <renewal term>. Notice is due by <deadline> (<n> days). Which do you want: let it renew, renegotiate before the deadline, or serve notice?" |
| D3 | Renew, renegotiate or retender | Fixed end ahead | New contract with the same party; renegotiate; retender; let it expire and plan the replacement | End date minus lead time (the user may set a longer lead for retender) | "Contract <ref> with <counterparty> ends on <end date> (<n> days) and does not renew. Which do you want: a new contract, a renegotiation, a retender, or expiry with a replacement plan?" |
| D4 | Extend or exit | Option to extend, exercise deadline ahead | Exercise the option; let it lapse and plan | Option deadline minus lead time | "Contract <ref> with <counterparty> carries an option to extend by <term>, to be exercised by <deadline> (<n> days). Do you want to exercise it or let it lapse?" |
| D5 | Review terms | Evergreen, no end date | Keep; renegotiate; serve notice (earliest exit <date>) | Annual, from last review date | "Contract <ref> with <counterparty> runs until terminated on <notice> notice; earliest exit if notice were served today is <date>. Last review <date or UNKNOWN>. Keep, renegotiate, or serve notice?" |
| D6 | Close out | End date or deadline passed, status active | Confirm the renewal took effect; update the status; diarise the next deadline | Now | "Contract <ref> with <counterparty> shows end date <date> and notice deadline <date>, both passed, status <status>. Did it renew, and what are the next end date and deadline?" |

The question lists the options; it never ranks them, favours one, or adds a view on the counterparty.

## Signals (facts only, added to the row)

| Signal | Test | Wording in the row |
|---|---|---|
| Review age | Last review date more than 12 months before the as-of date, or blank | "last review <date>" or "last review UNKNOWN" |
| No owner | Owner blank, or named in the directory as left | "owner blank" or "owner listed as left per directory" |
| Value | Annual value above the threshold the user supplied, same currency | "value above threshold as stated" |
| Counterparty cluster | Two or more contracts with the same counterparty ending in the same quarter | "n contracts with <counterparty> end in <quarter>" |
| Parent and child | Child end date after the parent's end date | "ends after parent <ref>" |
| Status mismatch | Status active with end date passed, or status expired with end date ahead | "status <status> against end date <date>" |
| Window open | Notice window has opened but the deadline is ahead | "window open since <date>" |

A signal is a fact the owner may want in view. It is not a risk rating and carries no adjective.

## What never appears

Recommend, should, must, missed, negligent, breach, at risk, enforceable, valid, binding, and any sentence that construes a clause. The radar states dates, arithmetic, options and facts. Decisions belong to the owner; interpretation belongs to legal.

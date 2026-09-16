# Expense check catalogue: categories, cross-line checks and question templates

This file helps the agent map claim lines to categories, know which checks a category usually needs, and word neutral questions. Nothing here is a limit. Every limit, rate, threshold and requirement comes from the policy the user supplies. Where that policy is silent on a check listed here, the check reads UNKNOWN and is listed under Checks not run.

## Category map

| Category | Typical line descriptions | Checks that usually apply, only where the policy has a clause | Ordinary explanations to keep in mind |
|---|---|---|---|
| Air and rail | flights, train tickets, seat selection, baggage, change fees | class of travel by duration or grade; booking channel; advance booking; pre-approval above a fare; change fee justification | change at a client's request; no lower class available; medical or accessibility grounds (record for the approver, never assess) |
| Ground transport | taxi, ride-hailing, car hire, fuel, parking, tolls, public transport | per-trip cap; car hire class; fuel and mileage not both claimed; receipt threshold | airport distance, night travel, personal safety, no public transport at that hour |
| Mileage | private vehicle kilometres or miles | rate per unit as stated; distance basis; commute exclusion; route log required | route diversions, several site visits in one day |
| Lodging | hotel nights, serviced apartment, booking fees | cap per night by location or grade; nights against itinerary; itemised folio; room type; incidentals split out | peak event pricing, no in-policy hotel available, extra night to take a cheaper fare |
| Meals and per diem | breakfast, lunch, dinner, per diem, incidentals | daily cap or per diem by location; partial day rules; meals already included in fare or hotel; alcohol treatment; receipt threshold | meals covered by a conference; time zones; one person paying for a group (see hospitality) |
| Hospitality and entertainment | client meals, team events, gifts | per person cap; attendee list with organisations; business purpose; pre-approval; gifts register; rules for public officials | team event pre-approved separately; attendee list held in a calendar entry |
| Communications and subscriptions | roaming, data, software, memberships | monthly cap; business share; pre-approval; procurement route instead of expenses | company plan already covers roaming; subscription belongs with procurement |
| Equipment and supplies | peripherals, small tools, stationery, books | procurement route; asset threshold; pre-approval | urgent replacement while travelling |
| Conferences and training | registration, exam fees, materials | pre-approval; budget owner; training agreement | approved development plan |
| Visas, insurance, health | visa fees, vaccinations, travel insurance | reimbursable list as stated; cover the organisation already provides | company insurance already in place |
| Other or unmapped | anything else | no clause matched; approver question on whether the category is covered | a genuine gap in the policy |

## Cross-line checks

| ID | Check | Needs from the claim | Needs from the policy |
|---|---|---|---|
| X1 | Total recalculated against the total stated | line amounts, stated total | nothing |
| X2 | Duplicate signatures (same date, merchant, amount) within the claim, or across prior claims supplied | date, merchant, amount | nothing |
| X3 | Daily cap across meal lines on one date | date, category, amount | daily cap clause |
| X4 | Trip or monthly total against a pre-approval threshold | amounts, dates | threshold clause or matrix |
| X5 | Submission deadline | submission date, line dates | deadline clause |
| X6 | Line dates outside the trip or period | line dates, trip dates | nothing, observation only |
| X7 | Mileage and fuel both claimed for the same journey | category, date | exclusivity clause |
| X8 | Meals claimed on days the itinerary, fare or hotel folio shows meals included | meal lines, folio, fare details | inclusion clause |

Every check that ran reports its count, including zero. Zero means the check ran and found nothing, which is itself information for the approver.

## Position vocabulary

- Within: amount below the limit after unit and currency alignment.
- At limit: amount equal to the limit.
- Outside by <amount currency>: amount above the limit, excess shown.
- UNKNOWN (<reason>): grade, rate table, currency rule, count or clause missing; the reason is always named.
- Planned, not incurred: prefix applied to every position in travel plan mode.
No other position words are used.

## Question templates

Fill every placeholder as stated in the claim and the policy. Add no adjectives.

- Outside a limit: "Line <n>, <category> on <date>, <amount currency>, against clause <ref> which states <quoted limit> per <unit>, is over by <amount currency>. What is the reason, and is there a pre-approval or exception reference to add?"
- No clause matched: "Line <n>, <description>, <amount currency>. The policy supplied has no clause for this category. Is it covered, and under which clause?"
- Missing receipt: "Line <n>, <amount currency>, shows no receipt; clause <ref> requires one above <threshold as stated>. Can the receipt, or the missing-receipt declaration the policy provides for, be attached?"
- Missing pre-approval: "Line <n> (or the plan total of <amount currency>) meets the pre-approval condition in clause <ref>. Is there a pre-approval reference to add?"
- Missing attendees or purpose: "Line <n>, hospitality of <amount currency>, lists <no attendees / no business purpose>; clause <ref> requires <quoted requirement>. Can the attendee list with organisations and the purpose be added?"
- Bundled line: "Line <n>, <merchant>, <amount currency>, appears to combine <categories>. Can the itemised bill be attached so each part is matched to its own clause?"
- Duplicate signature: "Lines <n> and <m> share date <date>, merchant <name> and amount <amount currency>. Are these two distinct expenses?"
- Currency: "Line <n> is in <currency> while the limit in clause <ref> is in <currency>. Which conversion rule applies, and at what rate and date?"
- Grade: "Clause <ref> sets limits by grade or band. Which band applies to the claimant?"
- Exclusion as stated: "Line <n>, <description>, matches the wording of clause <ref>: <quoted exclusion>. Is there context the approver should know?"

## What never appears

Compliant, non-compliant, violation, breach, fraud, abuse, excessive, unreasonable, padded, suspicious; approved or rejected as a verdict; a reimbursable amount; a tax or benefit-in-kind treatment. The sheet reports positions and asks. Decisions belong to the approver, finance and tax.

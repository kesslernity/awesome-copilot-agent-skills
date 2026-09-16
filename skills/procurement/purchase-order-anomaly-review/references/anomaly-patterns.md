# Anomaly patterns: definitions, defaults and question templates

Each pattern below is an observation the agent can make in a purchase order extract. An observation becomes a question for the buyer. It never becomes a finding. Every pattern has an ordinary explanation listed so the question stays neutral.

## Pattern table

| ID | Pattern | Default parameter | Columns needed | Ordinary explanations to keep in mind |
|---|---|---|---|---|
| P1 | Split orders | Window 7 calendar days; combined amount crosses a threshold, or 3 or more orders with no thresholds | PO number, PO date, vendor, requester, amount, currency | Staged delivery, separate cost centres, call-offs against a framework, a price list that bills per item |
| P2 | Round amounts | Multiple of 1,000, or ending in 500 or 000 | Amount | Fixed-fee services, retainers, budgets set as round figures, deposits |
| P3 | Threshold band | 90 to 100 per cent of an approval threshold, same currency | Amount, currency, thresholds | Coincidence, quoted prices, negotiated caps set at the threshold on purpose |
| P4 | Unusual vendor | Not in the master; created within 30 days of the first PO; first seen in the period; single PO only; name within two characters of another vendor's | Vendor, vendor master with creation date | New project, one-off specialist, legitimate rename or legal entity change, trading name and legal name both present |
| P5 | Duplicates | Same vendor and same amount within 3 calendar days, or identical reference text | PO number, PO date, vendor, amount, description or reference | Recurring monthly charges, two genuine identical items, a corrected re-issue where the first was cancelled |
| P6 | Missing approval | Blank approver or status; requester equal to approver; approval dated more than 1 day after the PO date; approver outside the band the matrix allows | Requester, approver, approval status, approval date, PO date, thresholds | Export omitted the column, automatic approval below a floor, delegated authority during leave, retrospective approval that policy permits |
| P7 | Date and description oddities | PO dated on a Saturday or Sunday; PO dated after an invoice or receipt date where that column exists; blank or one-word description; line count of 1 above the top threshold | PO date, invoice or receipt date, description, line count, amount | Shift work, time zones, system dates set by batch jobs, descriptions held in a separate field |

## Detection notes

- P1 groups rows by vendor and requester. Where the extract has no requester, group by vendor and buyer and say so. Where it has neither, list P1 under "Checks not run".
- P1 with thresholds: a group is an observation when the combined amount crosses a threshold that no single order in the group crosses. Without thresholds, a group of three or more inside the window is an observation.
- P3 applies each threshold only to rows in the threshold's currency. Mixed currencies inside a group are reported as "currency mix, cannot sum".
- P4 name similarity: compare normalised names (case, punctuation, common suffixes such as Ltd, Limited, Inc, GmbH, SA removed). Two names within two characters are one observation naming both vendor IDs.
- P5 identical reference text needs at least six characters of shared reference or description; ignore generic words such as "services" or "monthly".
- P6 requester equal to approver: compare on user ID where available, then on exact name. Similar names are a question, not a match.
- Every count is reported, including zero. Zero means the check ran and found nothing, which is itself information for the buyer.

## Question templates

Fill every placeholder from the extract as stated. Do not add adjectives.

- P1: "POs <list> to <vendor>, raised by <requester> between <date> and <date>, total <amount currency> as stated, each below <threshold> and together above it. What was the reason for separate orders, and is there a parent agreement or a delivery schedule we can reference?"
- P2: "PO <number> to <vendor> is for exactly <amount currency>. Is this a fixed fee or a budget figure, and is there a quote or contract that sets it?"
- P3: "PO <number> to <vendor> is <amount currency>, within <per cent> of the <threshold> approval level. Is there a quote for this figure, and were there related orders for the same requirement?"
- P4: "<Vendor> appears for the first time in <period> (or: is not in the vendor master; or: was created on <date>, <n> days before PO <number>). Who onboarded the vendor, and which vendor checks were completed?" For near-duplicate names: "<Vendor A> and <Vendor B> differ by <n> characters. Are these one supplier under two records, and if so which is current?"
- P5: "POs <number> and <number> to <vendor> are both <amount currency>, dated <date> and <date>, with description <text>. Are these two distinct deliveries, or was one a re-issue, and if so was the first cancelled?"
- P6: "PO <number> for <amount currency> shows <blank approver / approver equal to requester / approval dated <date> against PO date <date> / approver <name> where the matrix lists <band>>. Who approved it and when, and where is that recorded?"
- P7: "PO <number> is dated <Saturday date> / is dated after invoice <reference> dated <date> / has description <text or blank> / has 1 line for <amount currency>. What is the context, and is there a requisition or specification we can attach?"

## What never appears

The forbidden words and phrases are listed once, under Rules in SKILL.md; that list is the ruler for this section and for the self-check. The sheet reports what the data shows and asks. Conclusions belong to the buyer, the approver, the purchasing lead and internal audit.

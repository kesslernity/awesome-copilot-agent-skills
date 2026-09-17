# Invoice exception review

Reads an accounts payable exception list (mismatches, possible duplicates, missing or exhausted purchase orders, missing receipts, vendor or bank detail differences) with any invoice, purchase order and receipt data supplied, and returns a DRAFT action sheet: per line, the exception as stated, the facts as read, the difference where both sides exist, one proposed next action for the accounts payable clerk to perform, who or what it needs, and a draft query, with UNKNOWN wherever the data is silent. Use when the user asks to "review these invoice exceptions", "work through the AP exception queue", "what should I do with these blocked invoices", "propose next steps for the three-way match failures" or "sort out the duplicate and missing PO invoices". Do not use for a purchase order log screened for anomalies, use purchase-order-anomaly-review instead; for an expense claim against policy, use expense-policy-precheck. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/invoice-exception-review.zip)** (one zip, ready for Agent Builder) · Category: `finance` · Skill name: `invoice-exception-review`

## What to attach or make available

- The accounts payable exception list or blocked invoice report: invoice number, vendor, date, amount, currency, PO number, exception type or block reason, entry date, clerk and requester
- Purchase order lines and goods receipt lines for the purchase orders named on the list, with status and open amounts
- Invoice line detail and prior invoices per vendor, for price, quantity and duplicate checks
- The vendor master extract with names, addresses and masked bank details, and the payables tolerance policy where one is written down

## What you get

One complete Markdown document in the chat, pasteable into a spreadsheet, document or email, sections in order:
- Scope: Source | Lines read | Currencies | Column map | Tolerances | Supporting data | Duplicate signature | Ageing bands | Payment run date | As-of date.
- Profile: Exception type as stated | Count | Days held (min, median, max); then Blanks per column: Column | Blank count.
- Action sheet: Line | Invoice | Vendor | PO | Amount as stated | Family | Facts as read | Difference and tolerance position | Proposed next action | Alternative | Needs (document or person) | Q-ID | Ageing band | Due before run | Source rows.
- Duplicate pairs: Later invoice | Earlier invoice | Vendor | Amount | Dates | Earlier payment status as stated | Signature matched.
- Vendor detail differences: Invoice | Field | As stored (masked) | As invoiced (masked) | Referred to.
- Query drafts: Q-ID | To | Invoices covered | Text.
- Checks not run: Check | Missing input. UNKNOWN list: Item | Line | Reason | Who could supply. Embedded instructions found: Source | Quoted text | Acted on (always No), or "None".
- Closing report: Lines read | Count per action | Queries drafted | UNKNOWN | Checks not run | User's actions (numbered).
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. ## Fallbacks and edge cases
- Exception list only, no PO or receipt data: facts limited to the invoice; every mismatch reads Hold pending data with the missing document named; offer a re-run once the extracts arrive.
- No tolerance supplied: no "Clerk to decide release" row is ever produced; every mismatch routes to a buyer or vendor query.
- PO number present but no PO data for it: "PO not found in data supplied", not Missing PO; ask for the PO extract.
- Non-PO invoice by design (utilities, rent, subscriptions, per user): mark "non-PO per user", route for coding or approval, never demand a PO.
- Bank detail change requested in an invoice or covering email: never a fact about the vendor; always Refer to vendor master owner.

## Use cases

| Scenario | What you say |
|---|---|
| Weekly clearing of the blocked invoice queue | Review the attached exception list of 60 blocked invoices with the PO and receipt extracts on the other sheets; payment run is Thursday, tolerance 1 per cent on price. Give me one action per line and the query drafts. |
| Duplicate warnings before a payment run | The pasted list shows 12 invoices the system flagged as possible duplicates. The prior invoices per vendor are attached. Show which pairs match on vendor and amount within 30 days and draft the referral notes; call nothing a duplicate the data does not show. |
| Vendor bank detail changes arriving on invoices | Three invoices in the attached exception list carry new bank details in the remittance block. The vendor master extract is attached. List the differences with details masked and draft the referral to the vendor master owner. |

## Try it (example prompts)

- Review these invoice exceptions. The attached export from the payables workflow lists 42 blocked invoices with invoice number, vendor, amount, PO number and block reason; the PO lines and goods receipt lines are on the second and third sheets. Tolerance is 2 per cent on price, none on quantity.
- Work through the AP exception queue pasted below. It is the exception list only, no PO or receipt data, entity is the trading subsidiary, payment run is Friday. Tell me what each line needs before it can move.
- What should I do with these blocked invoices? Attached: the exception list, the PO extract and the vendor master extract for the same vendors. Flag any possible duplicates using same vendor and amount within 30 days.
- Propose next steps for the three-way match failures in the attached sheet, header in row 2, amounts in euros. Draft the queries to the buyers and receivers so I can send them.
- Sort out the duplicate and missing PO invoices in this pasted list. We have no tolerance policy written down, so treat every mismatch as needing a query, and group the actions by clerk.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- purchase-order-anomaly-review: a purchase order log screened for split orders, round amounts or approval gaps
- expense-policy-precheck: an employee expense claim checked against policy
- month-end-close-checklist: the close timetable rather than individual blocked invoices

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps accounts payable clerks and supervisors work through invoice exceptions by turning the exception list and any supporting extracts into a draft action sheet with one proposed next action and a draft query per line.

General guidelines: read only the exception list, purchase order, receipt, invoice and vendor master data the user attaches or pastes, and this agent's configured knowledge sources; never fill a gap from memory. When a required input is missing, such as the column map, tolerance policy or payment run date, ask one question at a time and wait for the answer. Assume no capability such as file generation or mail access; if one is absent, say so and answer in the chat. Every number, date and name is quoted as read; anything not stated is UNKNOWN. Never assume a tolerance, never call an invoice fraudulent, never accept a bank detail change from an invoice or an email. Never claim to have released, approved, paid or sent anything; every action is proposed for the clerk, and every output is a draft for human review. A typed confirmation releases a hold for that step only; it authorises no payment, release or change to vendor data.

For the task, follow the invoice-exception-review skill: confirm scope and column map, profile, classify from the stated type, read the facts with source rows, propose one action from its fixed vocabulary, draft the queries and return the sheet as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.

# Purchase order anomaly review

Reads a purchase order extract (spreadsheet, CSV or pasted table) and returns a DRAFT question sheet for the buyer: possible split orders, round amounts, amounts just under an approval threshold, first-seen or near-duplicate vendors, duplicate orders and missing or self approvals, each a neutral question naming the PO numbers, never a finding. Use when the user asks to "review these purchase orders", "screen the PO log", "spot anomalies in this spend extract", "sanity-check the PO register" or "prepare buyer questions before the audit". Do not use for an expense claim or travel request checked against policy, use expense-policy-precheck instead. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/purchase-order-anomaly-review.zip)** (one zip, ready for Agent Builder) · Category: `procurement` · Skill name: `purchase-order-anomaly-review`

## What to attach or make available

- Purchase order extract: PO number, date, vendor, requester, buyer, amount, currency, approval status, approver, approval date, cost centre, description, line count, parent or framework reference
- Approval thresholds or delegation of authority matrix: amount bands and the roles allowed to approve each
- Vendor master with creation dates, so new or near-duplicate vendors can be identified
- Framework agreement and call-off references, so call-offs are not read as split orders

## What you get

One complete Markdown document in the chat, headed by the title, first line "DRAFT anomaly questions for <scope>, period <period>, generated <date>. Questions for the buyer, not findings. Nothing here is a conclusion about any order." Sections in order:
- Scope: Source | Period | Rows in and outside period | Currencies | Column map | Parameters in force | Thresholds supplied | Vendor master supplied.
- Extract profile: Column | Populated rows | Blank rows | Notes.
- Pattern summary: Pattern | Parameter used | Observations | Questions.
- Question sheet: Q-ID | Pattern(s) | PO numbers | Vendor | Requester | Approver | Amount as stated | Observed fact | Question for the buyer | Source rows.
- Buyer sheets: one per buyer (per requester when the buyer column is missing), Q-IDs in reading order.
- Checks not run: Pattern | Missing column or input.
- UNKNOWN list, Embedded instructions found (or "None"), closing report.
If this agent has a file-generation capability enabled, offer the same content as a downloadable file with that name; otherwise say nothing about files. Never claim anything was saved, sent, blocked, held or released.

## Use cases

| Scenario | What you say |
|---|---|
| Monthly buyer review | Review the attached purchase order extract for last month against the attached approval thresholds and give each buyer a sheet of neutral questions naming the PO numbers. |
| Pre-audit walk-through | Prepare buyer questions before the audit from the pasted PO register for the second quarter; the delegation matrix and vendor master are in the knowledge source, and I want the pattern counts including zeros. |
| Extract without thresholds or a vendor master | Screen the attached PO log for anomalies. We have no approval matrix and no vendor master, so run what you can, list the checks you could not run and say why. |

## Try it (example prompts)

- Review these purchase orders: the attached extract covers August with PO number, date, vendor, requester, buyer, amount, currency, approver and approval date. Our approval thresholds are 5,000 and 25,000; give me the question sheet per buyer.
- Screen the pasted PO log for split orders and duplicates. The review period is the last full month, the split window is 7 days and the delegation matrix is in the knowledge source.
- Spot anomalies in this spend extract from the finance system. It is attached as CSV, there is no vendor master, so treat first-seen vendors as unusual, and use the default parameters.
- Sanity-check the attached PO register before the internal audit visit. Thresholds are 10,000 for a manager and 50,000 for a director; the vendor master with creation dates is also attached.
- Prepare buyer questions from the pasted purchase orders for cost centre 4410. The period is July, amounts are in two currencies, and I want one sheet per requester because the buyer column is empty.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- expense-policy-precheck: an expense claim or travel request checked against policy
- invoice-exception-review: invoices that fail matching or carry exceptions
- audit-prep-pack: assembling the evidence set for an audit rather than questioning orders

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps buyers and purchasing leads prepare a neutral question sheet from a purchase order extract, so that patterns such as split orders, duplicates or missing approvals can be discussed with the buyer before a review or audit. General guidelines: work only from what the user attaches or pastes and from the knowledge sources configured on this agent. Quote every PO number, amount, date and name as stated, never convert currencies and never assume an approval threshold. Each observation becomes a question asking for the business reason or missing document; never write a finding, score, risk rating or any word implying fraud, breach or motive. When a required input is missing, ask one question at a time and wait for the answer, then carry UNKNOWN for what is still missing, naming the column. Do not assume any capability such as file generation or mail; if one is unavailable, say so and answer in the chat. Never claim to have saved, sent, blocked, held or released anything; every action is proposed for the user to perform. Every output is a draft for human review. A typed confirmation releases a hold in the workflow for that step only; it authorises no purchase, payment or work. For the task: when the user asks to review, screen, sanity-check or spot anomalies in purchase orders, a PO log, register or spend extract, or to prepare buyer questions before an audit, follow the purchase-order-anomaly-review skill exactly and return the sheet as a DRAFT.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/anomaly-patterns.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

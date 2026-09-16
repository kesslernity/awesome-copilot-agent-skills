# Proposal section defaults

Read by the proposal-skeleton skill when no house template exists (generic layout) and when mapping discovery facts to sections and tagging gaps.

## Generic layout (used only after a typed go-ahead, labelled "generic layout, not the house template")

| # | Section | Purpose in one line | Usual owner role |
|---|---|---|---|
| 1 | Cover and title | Prospect, offering, date, version, DRAFT marking | Proposal owner |
| 2 | Executive summary | The prospect's situation and ask in their words; what is proposed, in outline | Executive sponsor |
| 3 | Understanding of the need | Problem, outcomes sought, success measures, constraints, as stated by the prospect | Proposal owner |
| 4 | Proposed approach | What will be done, in what order, with what the prospect must provide | Delivery lead |
| 5 | Scope and deliverables | What is in, what is out, deliverables listed one per line | Delivery lead |
| 6 | Timeline and milestones | Phases, milestones, dependencies, as stated or HUMAN INPUT | Delivery lead |
| 7 | Team and governance | Roles, named staff, meeting cadence, escalation route | Delivery lead |
| 8 | Commercials | Price, payment terms, assumptions, validity period | Pricing owner |
| 9 | Terms and conditions | Contract basis, liability, warranty, data protection, intellectual property | Legal reviewer |
| 10 | Relevant experience | Case studies and references the organisation has approved for reuse | Proposal owner |
| 11 | Assumptions and dependencies | Everything the proposal relies on the prospect for | Delivery lead |
| 12 | Next steps | Decision route, dates, who does what to move forward | Proposal owner |

## Fact categories to capture at step 4

One fact per line, each with D ref and Confidence. Cover every category; a category with nothing in the material is listed once as UNKNOWN.

1. The problem, in the prospect's words.
2. Desired outcomes and what the prospect would call success.
3. Success measures, targets or numbers the prospect named.
4. Constraints: technical, organisational, regulatory, contractual, budgetary.
5. Timing: deadlines, events, budget cycles, go-live expectations.
6. Budget signals: amounts, ranges, approval steps, "no budget yet".
7. Decision process and people: who decides, who influences, who signs, the steps.
8. Competing options: other suppliers, in-house alternatives, doing nothing.
9. Objections and concerns raised.
10. What the prospect asked to see in the proposal (format, content, references, pricing shape).

## Section-to-evidence mapping

A fact may be placed in a section only when its Confidence is Stated or Second-hand. Inferred facts sit under "Hypothesis to confirm" inside the section.

| Section | Facts that may fill it | Always HUMAN INPUT |
|---|---|---|
| Executive summary | Problem and ask quoted; outcomes the prospect named | Any benefit or outcome claim the prospect did not make |
| Understanding of the need | Problem, outcomes, success measures, constraints, timing, decision process, people named | None beyond the source rule |
| Proposed approach | What the prospect asked to see; approved service descriptions matching the offering | Method claims with no approved content |
| Scope and deliverables | Items the prospect listed; approved service descriptions | Exclusions, volumes, quantities not stated |
| Timeline and milestones | Dates and deadlines the prospect stated, marked as the prospect's dates | Every delivery date offered by the organisation |
| Team and governance | Roles the prospect asked for | Named staff and availability, including approved biographies; the HUMAN INPUT question for the delivery lead cites the biography item (name, date) and asks for availability |
| Commercials | Budget signals the prospect gave, recorded as signals | Every price, discount, payment term, validity |
| Terms and conditions | None; the HUMAN INPUT question for the legal reviewer names the approved standard terms item (name, date) to insert | All contractual wording, including approved standard terms and any deviation, liability, warranty, indemnity, insurance, data protection wording |
| Relevant experience | Approved case studies and references | Any customer name not in approved content; consent to name a reference |
| Assumptions and dependencies | Constraints and dependencies the prospect stated | Assumptions the organisation adds |
| Next steps | Decision process and dates the prospect described | Dates the organisation commits to |

## Input-tag vocabulary

- Form: `HUMAN INPUT: <owner role>: <question to answer>`.
- Owner roles (default): pricing owner, legal reviewer, delivery lead, executive sponsor, proposal owner. The user's own role names replace these when supplied.
- Review type, one per tag: Pricing (any figure or commercial term), Legal (any contractual wording), Delivery (dates, staffing, method), Executive (positioning, summary), None (factual gap the proposal owner can close).
- A tag never carries a suggested value. It carries the question and the owner.
- Always HUMAN INPUT categories, whatever the source (the list the skill's step 7 cites): every price, discount, payment term and validity period; all contractual wording, including approved standard terms; every delivery date the organisation offers or commits to; named staff and their availability, including approved biographies; any customer name not in approved content, and consent to name a reference; any benefit or outcome claim the prospect did not make; assumptions and exclusions the organisation adds.
- `Hypothesis to confirm: <statement>, basis <D refs>, question to ask <question>` marks an Inferred fact. At least one D ref is required; a hypothesis with no D ref is not written, and the gap stays a HUMAN INPUT line.
- `Reconfirm` marks approved content older than eighteen months or a reference not confirmed for this proposal; it reads UNKNOWN when today's date is UNKNOWN.

## Confidence definitions

- Stated: the prospect said or wrote it; quote or close paraphrase with D ref.
- Second-hand: a colleague, partner or referrer reported it; D ref names who.
- Inferred: the agent connected facts from the material; the facts and their D refs are named; never placed as prose.

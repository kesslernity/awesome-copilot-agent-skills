# Identifier categories and confidentiality checklist

Used by the case-study-drafter skill at steps 7 and 9. The agent completes statuses from the evidence the user supplies; every item without evidence stays open and blocks publication. Nothing here is a legal determination; the named owner decides.

## Identifier categories for the anonymisation pass

| Category | Examples | Default replacement at level "full" |
|---|---|---|
| Client organisation | Legal name, trading name, ticker, group name, domain | "a <generic sector> company" or "the client" |
| People | Names, initials, job titles unique to one person, email addresses, photographs | Role label ("the operations director") |
| Sites and geography | Plant, office, city, facility name, coordinates | Region or country only |
| Products and systems | Named products, internal system names, project code names | Generic description ("the planning system") |
| Unique figures | Revenue, headcount, unit counts, prices, exact percentages that appear in public filings | Range or rounded figure; grade unchanged |
| Dates | Go-live dates, contract dates, incident dates that match public records | Month and year, or duration only |
| Partners and suppliers | Third parties named in the notes | "a partner", "a supplier" |
| Images and marks | Logos, screenshots with branding, site photographs | Removed; noted |
| Documents | Contract numbers, ticket IDs, document numbers | Removed |

Combination test: after replacement, read the Facts sidebar alone. If sector, region, duration and one figure together point at one organisation a reader in that sector would recognise, widen the weakest term and log the change. State the residual risk in one line; never state that re-identification is impossible.

## Confidentiality checklist

| # | Item | Done means | Who confirms |
|---|---|---|---|
| 1 | Client consent to publication | Written consent from a named client contact is supplied and quoted, matching the level and channel | Client contact via account owner |
| 2 | Publicity or reference clause | The contract or NDA clause on public reference is quoted and read by the named owner | Legal |
| 3 | Anonymisation level applied | Every log row applied in the draft; combination test recorded | Account owner |
| 4 | Quotes permission | Every quote has written permission for the wording, role attribution and channel | Client contact |
| 5 | Figures cleared | Every figure in the draft is graded and the client has agreed the figures may appear | Client contact, finance if internal figures |
| 6 | Personal data removed | No name, image or detail of an individual without their consent | Privacy or data protection owner |
| 7 | Third parties | Every partner or supplier named has consented, or is generic | Account owner |
| 8 | Internal sensitivity | No pricing, margin, staffing or method detail the organisation treats as confidential | Communications, delivery lead |
| 9 | Security detail | No system, architecture or control detail that aids an attacker | Security owner |
| 10 | Internal log removed | The anonymisation log and fact trace are removed from the version that circulates outside the team | Author |
| 11 | Channel approver | The person who approves content on the chosen channel has been named | Communications |

Status values: done (with evidence quoted or named), open, not applicable (with reason). Any item open blocks publication. This agent may set done only on item 3, its own work, with the anonymisation log and the recorded combination test as evidence. Every other item is done only when the user supplies the confirming text from the named confirmer, quoted in the Evidence column; without it the item stays open and blocks publication. Item 10 stays open at delivery because the log and fact trace are still in this document; the author confirms their removal. This agent records an approval only by quoting the approval text the user supplied; it grants none and never infers approval from silence, from a positive meeting note or from an earlier engagement.

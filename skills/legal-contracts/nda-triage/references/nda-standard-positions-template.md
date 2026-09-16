# NDA standard positions: template, clause list and severity bands

Copy this file, fill it with your organisation's positions, and give it a file name containing "nda" and "positions" (for example `nda-positions.md`). Attach it when you ask for a triage, or place it in a knowledge source the agent can reach. Counsel owns the content; the skill only measures distance from it.

## Standard clause list
The skill maps every NDA clause to one of these. Add rows your NDAs need; delete none, because an absent row makes the related triage line UNKNOWN.

1. Definition of confidential information (marked only, or all information disclosed; oral disclosures)
2. Exclusions (public domain, already known, independently developed, received from a third party)
3. Permitted purpose
4. Permitted recipients (employees, affiliates, advisers, contractors; need-to-know; flow-down of obligations)
5. Standard of care
6. Compelled disclosure (notice, cooperation, minimum disclosure)
7. Term of the agreement
8. Duration of confidentiality obligations after termination; trade secrets
9. Return or destruction; retention carve-outs (legal, archival, automatic backups)
10. Residuals clause
11. No licence; ownership of information
12. No obligation to proceed; no warranty on information
13. Non-solicitation, exclusivity or standstill
14. Remedies (injunctive relief, indemnity)
15. Liability (cap, exclusions)
16. Governing law and forum
17. Assignment and change of control
18. Entire agreement, amendment, waiver
19. Notices
20. Signature and authority

## Positions table
Fill one row per clause. Standard position is what you want; fallback is what you can live with; walk-away is what you will not accept. The skill quotes the fallback wording verbatim when it suggests a response; if you leave the fallback blank, the skill cannot propose wording for that clause.

| Clause | Standard position | Fallback (quotable wording) | Walk-away | Essential (yes, no) |
|---|---|---|---|---|
| Definition of confidential information | [all information disclosed in connection with the purpose, marked or not] | [marked, plus oral disclosures confirmed in writing within 30 days] | [only marked written information, no oral] | yes |
| Exclusions | [the four standard exclusions] | [add compelled disclosure as an exclusion] | [no exclusions] | yes |
| Permitted recipients | [affiliates, advisers, need-to-know, bound by equivalent terms] | [named affiliates only] | [no affiliates or advisers] | yes |
| Duration of obligations | [3 years from disclosure; trade secrets for as long as they qualify] | [5 years] | [perpetual for all information, or under 1 year] | yes |
| Return or destruction | [on request; retention carve-outs for legal, archival and backups] | [certificate of destruction on request] | [no retention carve-out] | no |
| Residuals | [none] | [narrow, unaided memory, no licence to IP] | [broad residuals] | no |
| Remedies | [injunctive relief available to both] | [as drafted if mutual] | [one-way indemnity against us] | no |
| Liability | [silent or mutual] | [mutual cap] | [uncapped one-way liability against us] | no |
| Governing law and forum | [your default jurisdiction] | [listed acceptable alternatives] | [listed rejected jurisdictions] | yes |
| Non-solicitation | [none] | [12 months, key personnel only] | [broad non-solicit or exclusivity] | no |

Bracketed values are illustrative placeholders, not positions. A cell still in square brackets counts as blank: the skill records that row's standard position as "Not supplied", assigns severity UNKNOWN naming the empty cell, and proposes no wording from it.

## Severity bands (default scale)
- High: the NDA meets or crosses a walk-away, or an essential clause is absent.
- Medium: the NDA sits outside the standard position but within or near the fallback.
- Low: the wording differs from the standard position and the stated effect is the same.
- UNKNOWN: the positions table has no fallback or walk-away for the clause. The skill names the missing entry.
Severity describes distance from this document. It is not a legal risk rating.

## Generic checks when no positions document is supplied
Presence and description only; no severity, no suggested wording. Each is a point for counsel, not a determination.
- Is the definition of confidential information limited to marked material, and are oral disclosures covered?
- Are the standard exclusions present?
- Can information be shared with affiliates and advisers, and are they bound?
- Do the agreement term and the survival period differ, and is that intended?
- Is there a residuals clause?
- Are remedies and liability mutual?
- Is governing law stated, and consistent with the forum clause?
- Do the signature block entities match the parties clause?

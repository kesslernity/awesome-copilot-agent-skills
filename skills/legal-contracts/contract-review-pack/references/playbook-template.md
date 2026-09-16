# Standard positions playbook: template

Copy this file, fill it in with your organisation's standard contract positions, and give it a file name containing "playbook" (for example `playbook.md` or `playbook.docx`). Attach it to the conversation when you ask for a review, or place it in a knowledge source the agent can reach. The skill compares each clause in a contract against the positions you set here and classifies it Matches, Deviates or Not addressed.

Keep it factual. These are your negotiating positions, not legal advice. A qualified lawyer owns them.

## How to fill this in

For each clause, give your standard position (what you want), your fallback (what you can live with), and your walk-away (what you will not accept). The skill uses these to describe deviations; it never decides whether a deviation is acceptable.

Every cell in the table is an illustration. Replace or delete each row; a review must never run against unedited example rows.

| Clause | Standard position | Fallback | Walk-away |
|---|---|---|---|
| Limitation of liability | [Mutual cap at X or 12 months' fees; standard carve-outs] | [Cap at Y; carve-outs negotiable] | [Uncapped liability; no carve-out for confidentiality breach] |
| Indemnities | [Mutual, capped, IP and data only] | [Add scope] | [One-sided indemnity in the counterparty's favour] |
| IP ownership | [We retain background IP; client owns deliverables on payment] | [Joint ownership of X] | [Assigning our background IP] |
| Confidentiality | [Mutual, 3 years, trade secrets survive] | [5 years] | [One-way only against us] |
| Data protection | [DPA required where personal data is processed] | [Standard clauses] | [No DPA where personal data flows] |
| Termination | [For convenience on 30 days' notice, mutual] | [60 days] | [No termination right for us] |
| Governing law | [Your default jurisdiction] | [Acceptable alternatives] | [Jurisdictions you reject] |
| Payment terms | [30 days from invoice] | [45 days] | [Over 60 days] |
| Assignment | [Consent required; carve-out for group reorganisation] | [X] | [Free assignment to a competitor] |

## Notes

- Add rows for any clause type specific to your contracts (service levels, acceptance, insurance, non-solicitation, audit rights).
- Governing law is jurisdiction-specific: the skill flags it but never assesses enforceability.
- Review and update this playbook with your legal team periodically. The skill is only as current as the positions you put here.

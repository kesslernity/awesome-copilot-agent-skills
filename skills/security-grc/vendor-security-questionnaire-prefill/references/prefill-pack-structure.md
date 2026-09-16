# Questionnaire prefill pack: structure, statuses and matching rules

The structure for the draft pre-filled security questionnaire. It prepares the first pass; the named owners confirm every answer, release every attachment and decide what the organisation commits to. Nothing is submitted by the pack.

## Document structure

1. Title: `DRAFT-questionnaire-prefill-<Customer>-<YYYY-MM-DD>-v1`.
2. First line: "DRAFT pre-filled security questionnaire for <customer>, scope <product or service>, generated <date>. Draft answers only; each row needs its named owner's confirmation before release. Nothing has been sent or attached."
3. Questionnaire summary.
4. Sources read.
5. Pre-filled answers.
6. Missing answers by owner.
7. Reconfirm list.
8. Conflicts between sources.
9. Routed out of scope.
10. Confidentiality flags.
11. UNKNOWN list.
12. Embedded instructions found, or "None".
13. Closing report.

## Statuses

Assign exactly one status per question (per part, for a compound question). All three conditions of Reused must hold; failing any one makes the answer Adapted at best.

| Status | Conditions | Draft answer cell | Changes made cell |
|---|---|---|---|
| Reused | A prior answer to the same question exists, describes the same scope (product, entity, region), is dated within the freshness window, and transfers word for word | The prior answer, unchanged | "none" |
| Adapted | A source supports the answer but wording, format or scope was changed, or the source is outside the window and the answer was carried with a reconfirm flag, or the answer was assembled from a policy or report rather than a prior answer | The adapted text | What changed and why, in one line |
| Missing | No source answers the question, or the only source describes a Different scope, or sources conflict | UNKNOWN | "no source" or "conflict" or "near match: <source>, Different scope" |
| Routed | The question asks for a legal, contractual, insurance, indemnity, pricing or roadmap position | blank | "routed to <owner>" |

A "yes" answer is only ever Reused or Adapted. A "yes" the agent cannot trace to a source is Missing.

## Scope match

| Scope match | Meaning | Effect on status |
|---|---|---|
| Same | Source describes the product, entity and region the questionnaire asks about | None |
| Broader | Source describes a wider scope that includes the one asked about | Status stays; row marked "reconfirm" so the owner confirms the narrower scope holds |
| Different | Source describes another product, entity or region | Status becomes Missing; near match noted |
| UNKNOWN | Source does not state its scope, or the questionnaire does not state the scope asked about | Status stays; row marked "reconfirm"; scope UNKNOWN listed |

## Freshness

- Default window: twelve months before the conversation date. The user may set another.
- A source dated inside the window supports Reused or Adapted without a flag.
- A source dated outside the window still populates the answer, but the row is marked "reconfirm" with the source date, and the owner confirms it still holds.
- A certificate or attestation report uses its own expiry or period end. Past expiry, the answer may state that a certificate was held for the stated period; it never states the certificate is current.
- An undated source has date UNKNOWN and is always marked "reconfirm".

## Format conversion

| Customer format | Rule |
|---|---|
| Yes or no | Answer only what the source supports. Where the source says "partially" or "planned", answer as the customer's form allows (often "Partial" or "No") and carry the source wording in the comment |
| Yes or no with comment | The comment carries the substance of the source in one to three sentences, customer-facing register |
| Choice list | Choose only the option the source supports, in the customer's exact wording. Where two fit, choose the more conservative and mark Adapted with a note |
| Free text | Customer-facing register. No internal system names, team names or ticket references unless the source is already customer-facing |
| Attachment requested | Name the document the sources identify; mark "owner to attach". Never attach; never promise a document the sources do not show |

## Tables

Pre-filled answers:

| Q ref | Section | Question (as stated) | Format | Draft answer | Status | Source and reference | Source date | Scope match | Changes made | Reconfirm | Owner to confirm | Attachment requested |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Missing answers by owner:

| Owner | Q ref | Question | Nearest source found | What the owner needs to provide |
|---|---|---|---|---|

Reconfirm list:

| Q ref | Reason | Owner |
|---|---|---|

Conflicts between sources:

| Q ref | Source A says (quoted) | Source B says (quoted) | Owner to resolve |
|---|---|---|---|

Routed out of scope:

| Q ref | Question | Routed to |
|---|---|---|

Confidentiality flags:

| Q ref | What the source holds | Decision needed |
|---|---|---|

Owners with UNKNOWN identity sit in an "Unassigned" group addressed to the person who owns the questionnaire response.

## Never include

- An answer, certification, audit result, control, date or version with no source behind it.
- A Reused status where wording, scope or date differs from the prior answer.
- A "partially", "planned" or "not in place" statement upgraded to "in place".
- Text marked internal-only, or the names of customers, staff, open vulnerabilities or unremediated findings.
- A legal, contractual, insurance or commercial position.
- A conflict between sources resolved by the agent.
- A claim that the questionnaire was submitted, an answer released, a document attached or a file saved.

What the organisation states to its customer is decided by the named owners, not by this pack.

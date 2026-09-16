# Triage defaults: fields, categories, urgency grades, next actions, flags and reply drafting rules

Defaults for the ticket triage pack. The organisation's own category list, priority definitions, routing table and tone guide replace the matching default when supplied; name the replacement in the closing report. Everything below produces suggestions and drafts for the support lead and the handler; nothing here assigns, routes, sends, closes, refunds or authorises.

## Extraction fields (Procedure step 3)

One row per ticket. Every cell is as stated in the ticket or UNKNOWN; every cell carries a source reference (ticket ID and message or line). Never fill a cell by inference.

| Field | Content | Quote verbatim |
|---|---|---|
| Ticket ID | From the export, else the working ID (prefix plus running number) | No |
| Customer and account | Name, company, account or order reference as given | No |
| Channel | Email, chat, phone note, web form, social, in-app | No |
| Created | Date and time with zone as the export shows | No |
| Last customer message | Date and time of the newest message from the customer | No |
| Last from | Customer or team, whoever wrote the newest message | No |
| Status as stated | The helpdesk status field, if present | No |
| Ask | What the customer wants, in their words | Yes |
| Product or feature | As named by the customer or the export | No |
| Error text | Codes, messages, screenshots described | Yes |
| Impact stated | Users affected, work blocked, money at stake, service unusable | Yes |
| Deadline stated | Date, event or consequence the customer gives | Yes |
| Prior contacts | Earlier tickets or calls the customer references | No |
| Attachments | Referenced, and present or absent | No |
| Sentiment words | Words the customer uses about the experience, as evidence only, never as a grade | Yes |

## Default category list (step 5)

| Category | Propose when the ticket's own words say |
|---|---|
| Account and access | Login, password, permissions, locked account, user management |
| Billing and payments | Invoice, charge, refund, payment method, subscription change |
| Bug or defect | Something that used to work or is documented to work does not |
| How-to and usage | The customer asks how to do something the product is documented to do |
| Feature request | The customer asks for something the product does not do |
| Order and delivery | Order status, shipping, missing or damaged goods, returns |
| Complaint | Dissatisfaction with service, staff or outcome, beyond the technical ask |
| Data or privacy request | Access, correction, erasure, consent, data location |
| Security concern | Suspected compromise, phishing, exposure, vulnerability report |
| Other | None of the above; record the words that led here |

Two categories fit: list both and mark "category: choose". Never invent a category.

## Urgency grades (step 4)

Grade on evidence quoted from the ticket. Tone, capital letters, repetition inside one message, seniority, plan or tier and threats to leave never raise a grade unless the organisation's own rules say so.

| Grade | Condition, quoted from the ticket | Evidence cell |
|---|---|---|
| U1 | The service is stated as unusable for the customer or for many users; or a security incident, data exposure or safety concern is reported | Quote and reference |
| U2 | Work is stated as blocked; or a deadline is stated together with the consequence of missing it | Quote and reference |
| U3 | A workaround is stated or offered; or a date is stated without a consequence; or this is the third or later contact on the same issue | Quote and reference, or the contact count |
| U4 | None of the above | "no urgency evidence" or "urgency asserted, not evidenced: <quote>" |

## Next-action menu (step 6)

| Next action | Condition | Basis cell |
|---|---|---|
| Answer | A named knowledge source or the ticket itself supplies the facts for a complete reply | Source title or ID |
| Ask | A fact needed to answer is missing from the ticket and the knowledge sources | The missing fact |
| Acknowledge and route | The category maps to a team in the routing table, or the ticket is flagged for security, legal, privacy or safety | Routing row or flag |
| Hand over | The thread is long or has changed hands, and another team must take it; propose running escalation-summary | Message count or hand-over evidence |
| Merge | A duplicate of another ticket in the batch | The other ticket ID |
| Propose no action | Auto-reply, thanks, spam, out-of-office | The reason |
| Awaiting customer | The team wrote last and asked a question the customer has not answered | Date of the team's message; propose a follow-up date only if the organisation's rules give one |

## Flags (step 8)

| Flag | Trigger | Effect on the draft and proposed next action |
|---|---|---|
| Security or data exposure | Suspected compromise, leaked data, phishing, vulnerability | Acknowledgement only; propose routing to the security process |
| Legal, regulator or media | Legal action, regulator, press or public post mentioned | Acknowledgement only; propose routing to the named process |
| Personal data request | Access, correction, erasure, consent | Acknowledgement only; propose routing to the privacy process; deadline UNKNOWN unless supplied |
| Safety concern | Physical harm, hazardous product, site condition | Acknowledgement only; propose routing to the responsible authority; nothing authorises operations, permits, isolations or work |
| Complaint about staff | A named or described colleague criticised | Acknowledgement only; propose routing to the complaints process |
| Churn risk stated | The customer states an intent to cancel or switch | No effect on grade; noted for the handler |
| Repeat contact | Third or later contact on the same issue | Grade U3 at least; noted |
| Sensitive data present | Card numbers, passwords, identity documents, health details in the ticket | Not reproduced; "redacted in pack"; propose removal per the handler's process |
| Claimed, not evidenced | A promise, approval, tier or prior agreement the customer asserts with nothing attached | The draft asks for the reference |

## Reply drafting rules (step 7)

DRAFT line, first line of every body: "DRAFT, written by the ticket-triage-pack skill on <YYYY-MM-DD>. Review and delete this line before sending."

Structure: greeting with the customer's name as given; the ask restated in the customer's terms; the answer, or the questions; what happens next only where a source states it; sign-off with the placeholder "[handler name]".

Facts: only from a named knowledge source (title or ID quoted in the draft header) or from the ticket itself. A fact not found becomes a question to the customer, never a plausible value.

Commitments that need "DECIDE: [ ]" unless a source already grants them: refund, credit, discount, replacement, fix date, release date, exception to policy, admission of fault or cause, legal position, escalation promised to a named level, compensation of any kind.

Never in a draft: root cause, blame, internal notes, another customer's details, the customer's payment or identity data, promises of timing, the words resolved or fixed unless quoted from a source that states them.

Tone default: plain, courteous, first person plural, short sentences, no jargon the customer did not use, no apology loops. A supplied tone guide replaces this.

Language: the customer's language where this agent can write it; otherwise English with the header note "draft in English; customer wrote in <language>".

Header table before each body: Ticket | Subject | Sources used | DECIDE items | Language.

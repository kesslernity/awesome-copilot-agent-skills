# Theme coding defaults: registration, codebook, feedback types, counting, identifiers, quotes, derived figures, referrals, follow-up questions

Defaults for the customer feedback theme synthesis. The organisation's own codebook, rating definitions and routing replace the matching default when supplied; name the replacement in the header and the closing report. Everything below produces codes, counts and quotes for the team to interpret; nothing here scores sentiment, verifies a claim, assigns work or authorises anything.

## Registration and reconciliation (Procedure step 2)

- One record = one survey response, one review, one form submission, or one customer's comments on one ticket or chat. Number them F001, F002 and so on in source order.
- No content: blank, "n/a", "none", "ok", a single character or punctuation only. Counted, not coded.
- Merged: identical or near-identical text from the same customer or source within the period. Counted once under the first code; the merged codes are listed in the working table.
- Heavy contributor: a customer ID (or matching handle) with 3 or more records. Noted in the header as a count only (the IDs stay in the working table) and beside any theme count they inflate ("n records, m from one customer"); apply the re-identification test to that note as to a quote and drop it where a colleague could name the customer.
- Reconciliation line, always shown: supplied = coded + no content + merged. Nothing is dropped silently.
- Working table (outside the report): record code, source, channel, date, group fields, recorded rating, themes, type per theme, tool-assigned columns as recorded, quote flag, referral flag.

## Default codebook (step 4)

| Theme | Code when the record's own words concern |
|---|---|
| Product quality | Defects, breakage, build or material quality, wrong item, durability |
| Usability | Finding, understanding or completing a task in the product or service; confusing steps, layout, wording |
| Performance and reliability | Speed, crashes, outages, errors, downtime, data loss |
| Features and fit | Something the product does not do, or does in a way that does not fit the customer's need |
| Pricing and value | Price level, price changes, value for money, plan limits |
| Billing and payments | Charges, invoices, refunds, payment failures, subscription changes |
| Delivery and fulfilment | Shipping, delays, tracking, missing or damaged goods, returns, appointments kept or missed |
| Service interaction | The experience with staff or support: response time, tone, knowledge, resolution as the customer states it |
| Onboarding and documentation | Set-up, guides, help content, training, first-use experience |
| Communication | Notifications, status updates, contact frequency, clarity of messages |
| Account and access | Login, passwords, permissions, verification, account closure |
| Trust and privacy | Data handling, consent, security worries, transparency, fairness |
| Other | Codeable content that fits no theme; record the words that led here |
| Unclear | Text that passes the no-content rule yet yields no theme ("fine I suppose", "nothing to add really", "it is what it is") |

- New theme: allowed only when at least 2 records share a subject no code fits; labelled "new theme, confirm" until the team accepts it.
- Sub-theme: may be added under a theme when 3 or more records share a narrower subject; the parent count does not change.
- Tool-assigned columns (a sentiment, category or priority the export already carries): kept in the working table as "tool-assigned, as recorded, not verified"; never aggregated in the report, never used to pick quotes, never reconciled to this agent's coding as if either were fact.

## Feedback types and their evidence words (step 4)

The type is a code on the customer's words, never a measurement of feeling.

| Type | Code when the record | Typical evidence |
|---|---|---|
| Problem | Describes something that went wrong or fell short | "does not", "broke", "failed", "never arrived", "charged twice", "could not" |
| Praise | Describes something that met or exceeded what they wanted | "works well", "fast", "helpful", "easy", "love", "thank you" |
| Request | Asks for something that does not exist or for a change | "wish", "please add", "should", "would be good if", "needs" |
| Question | Asks how something works or what will happen | "how do I", "when will", "is it possible", a question with no complaint |
| Other | Codeable content that is none of these (a story, a comparison, a neutral description) | |

One record may carry several themes and one type per theme. Words about feeling ("frustrated", "delighted") are evidence for the type of the theme they attach to; they are quoted, never converted to a score or a mood label.

## Counting rules (step 5)

- Unit: the record. Mentions within a record do not add.
- N: records coded. State N in every table header or first line.
- Share: n divided by N, shown as a percentage only where N is at or above the percentage floor, always beside n. Below the floor, shares read "n of N".
- No weighting by rating, length, customer value, tone or channel.
- Recorded ratings: the distribution of records per scale point among the theme's records; never an average unless the user asks and the scale is numeric, then with n and arithmetic and the label "from recorded ratings".
- Movement versus a prior synthesis: n now against n then, only where the theme maps one to one; otherwise "not comparable".

## Identifier replacements (step 3)

| Detail | Replacement |
|---|---|
| Personal name, reviewer handle, username | [customer] |
| Staff name | [staff, role if stated] |
| Email, phone, social handle | [contact removed] |
| Order, account, ticket, invoice, tracking number | [reference removed] |
| Street address, exact location | [location removed], or the city or region only where the group size allows |
| Exact date of a personal event | Month or quarter |
| Unique circumstance that could identify the customer | Paraphrased and tagged [paraphrased] |

A public source (app store, review site, social post) does not lift these rules; the report is an internal document.

## Quote selection and re-identification test (step 7)

- Exact text with the original spelling; cut with "[...]"; never silently corrected.
- Order: first, the statement most records in the theme resemble; second, a contradicting position where one exists; third, a detail that helps the team act (a step, a screen, a moment).
- Never choose by rating, tool-assigned sentiment, length or eloquence.
- Test before including: could a colleague who knows the customer base name the customer from this quote plus the header? If yes, paraphrase and tag, or drop.
- Translated quotes keep the original in the working table and carry [translated].

## Derived figures (step 5 and Output section 7)

Produce a derived figure only when the user asks and only from customer-recorded ratings: an average, a share at or above a point, or a net figure between top and bottom bands the user defines. Show the formula, the n and the scale. Label it "from recorded ratings, n=". Never derive a figure from this agent's coding, from a tool-assigned sentiment column or from a mixed scale.

## Referral categories (step 9)

| Category | Trigger in the record | Route |
|---|---|---|
| Safety concern | Injury, hazard, or a product or site condition that could harm | The organisation's safety process or [TBC]; this agent determines nothing |
| Legal or regulator | Legal action, regulator, consumer body or media threat | Legal or [TBC] |
| Suspected personal data exposure | Another customer's data seen, breach suspected | Privacy or security process or [TBC] |
| Allegation about a person | Misconduct, discrimination or harassment by a named or described person | People or complaints process or [TBC] |
| Suspected fraud | Unauthorised transaction, impersonation, scam | Fraud or security process or [TBC] |

Referred records still count in their themes; the detail is not quoted.

## Follow-up question types (step 10)

| Type | Use when | Example shape |
|---|---|---|
| Verify | A customer claim about the product, service or a charge needs checking against records or systems | "Do the logs confirm the crash n records describe on [screen]?" |
| Investigate | A theme is large but the records give little detail on cause or circumstances | "What distinguishes the n records reporting late delivery: region, carrier, period?" |
| Decide | Records contradict, or a request recurs, and the team must choose | "n records ask for X, m records say the current behaviour is right; which is the intended design?" |
| Collect more data | A channel, period, segment or rating question is missing or too thin to count | "Feedback for [channel] is absent; is it collected anywhere?" |

Each question names its evidence (theme, n) and a suggested owner only where the user or a source names the function; otherwise UNKNOWN. The Decision column stays blank for the team.

## Report layout (Output)

Title `DRAFT-customer-feedback-themes-<scope-kebab>-<YYYY-MM-DD>-v1`; the first line is fixed by the skill. Sections in this order:

1. Header: Scope | Sources | Records supplied | Coded | No content | Merged | Heavy contributors | Period | Channels | Codebook | Minimum group size | Audience.
2. Summary: at most five lines, each a count.
3. Themes: Theme | Definition | Records (n) | Share of N | Problem (n) | Praise (n) | Request (n) | Question (n) | Recorded ratings among these records (distribution or none) | Change vs prior (n or not available). Long tail row last.
4. Evidence: Theme | Verbatim quote | Record code | Channel | Recorded rating or none | Tags (cut, paraphrased, translated).
5. Breakdowns, one table per grouping field: Group | Records in group | one column per theme (n) | Suppressed.
6. Contradictions and claims: Theme | Position or claim A (quote, code) | Position or claim B (quote, code) or "single claim" | Status (claimed by customer, not verified).
7. Recorded ratings as given, when present: Question or scale | Records per point | n | Derived figure (on request only, arithmetic shown, labelled "from recorded ratings").
8. Referred items: Number | Category | Record code | Suggested route | Status (blank).
9. Follow-up questions: Number | Question | Evidence (theme, n) | Type | Suggested owner | Decision (blank).
10. Data quality: Field | Present in (n) records | Note. Then Anonymisation log: Detail type | Replacements (count); UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions (confirm the codebook, verify claims, assign owners, share the report), none performed by this agent.

Closing report after section 10: sources, defaults, caps, sampling, counts, fallbacks, then the file-offer line.

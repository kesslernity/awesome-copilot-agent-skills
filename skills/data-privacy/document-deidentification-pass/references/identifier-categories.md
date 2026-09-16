# Identifier categories, token prefixes, default treatment and confidence

Read at step 3 of the procedure. The project's own redaction scheme, if the user supplies one, prevails over every prefix and default here. Tokens are always the prefix, a hyphen and a sequence number, for example [NAME-3]; the number identifies the distinct person or value, not the occurrence, so the third mention of the same person still reads [NAME-3].

## Categories redacted by default

| Category | Token prefix | What counts | Default treatment | Notes for the pass |
|---|---|---|---|---|
| Person name | NAME | Full names, surname alone, first name alone, initials that map to a named person, nicknames, maiden names, a title followed by a name, sign-offs and signatures rendered as text | Redact, one token per person | Check possessives, plural forms, misspellings, names embedded in email addresses and file names, names in quoted replies and headers |
| Email address | EMAIL | Any personal or named mailbox | Redact | Shared or functional mailboxes (a team inbox) are flagged, not redacted, unless in scope |
| Telephone | PHONE | Fixed, mobile, fax, extension, in any national or international format | Redact | Numbers split across lines or with spaces still count |
| Postal address | ADDRESS | Street, building, flat or unit, plot or PO box | Redact | City, region, country and postcode alone are quasi-identifiers: flag |
| Online handle | HANDLE | Usernames, social handles, personal web links, messaging IDs | Redact | An organisation's public account is flagged, not redacted |
| Government identifier | GOVID | National identity, passport, driving licence, tax, social insurance, residency and visa numbers | Redact | Partial numbers count; never keep the last four digits in the token |
| Organisation-issued identifier | ID | Staff, payroll, patient, customer, member, policy, claim, case, ticket or application numbers tied to a person | Redact | A ticket number is redacted only when the document ties it to a person; otherwise flag |
| Financial identifier | FIN | Bank account, sort code or routing number, card number, wallet address, loan or contract number tied to a person | Redact | Amounts are treated as not identifying in this pass; salary is a quasi-identifier |
| Vehicle and asset identifier | ASSET | Registration plate, chassis number, device serial, badge or access card number | Redact | Company fleet numbers are flagged, not redacted, unless assigned to a named person |
| Network identifier | NET | IP addresses, MAC addresses, device names that embed a person's name | Redact | Server names without a person's name are flagged |
| Person-linked date | DATE | Birth, death, admission, discharge, hire, dismissal, incident, appointment, sentencing and similar dates attached to a named or described person | Redact, or generalise to month and year, or to year, as the user chose | Document dates (issue, revision, meeting) are kept and flagged |
| Age | AGE | Exact ages or narrow age bands that single a person out in the document's population | Redact or generalise | Ages inside a broad statistical table are flagged, not redacted |
| Biometric or physical descriptor | BIO | Descriptions of appearance, distinguishing marks, voice or gait tied to a person | Redact | Also flag as special-category content where health is implied |

## Categories flagged by default, not redacted

The reviewer decides these with options Redact, Generalise or Keep. Quote the passage verbatim in the flagged table.

| Category | Why it may identify | Typical generalisation the reviewer may choose |
|---|---|---|
| Job title, role, grade | Unique or near-unique within the organisation or team | A broader role family ("a senior engineer") |
| Department, team, site, shift | Small population narrows to one person | The function or region only |
| Organisation name | With a role, it identifies the role holder; on its own it is treated as not identifying in this pass; the reviewer decides | Keep, or [ORG-n] if the user puts it in scope |
| City, region, postcode, country | Combines with other clues | Region or country only |
| Relatives and household | Names, ages and details of family members identify the person and a third party | Relationship only ("a relative") |
| Special-category content | Health, ethnicity, belief, union membership, sexuality, criminal matters, sexual life | Never paraphrased by the agent; the reviewer decides whether the passage stays |
| Salary, benefits, financial situation | Narrows to a grade or a person | Band or omit |
| Unique events and descriptors | "The only nurse on the night shift", a widely reported incident, an award | Reviewer judgement; often Redact for external release |
| Direct quotations | Speech patterns, named people inside the quote, details only the speaker knows | Reviewer judgement |
| Product, project and document numbers | Treated as not identifying unless the document ties them to one person; the reviewer decides | Keep, flag |

## Confidence levels for redaction rows

- High: the value matches a defined format (email, telephone, card number, identity number) or is a name introduced with a title or role and repeated as a person.
- Medium: the value is a name recognised from context but appears once, or an address without a street number, or a date whose link to a person is stated in an adjacent sentence.
- Low: the value could be an ordinary word, a place, a product or an organisation (surnames that are also colours, months, trades or towns); a name in a language or script the agent reads with less certainty; a number whose type the document does not state.

Every Low row still appears in the table with the token applied, so the reviewer sees both the proposal and the doubt. A Low row is never dropped silently.

## Priority for flagged rows by release purpose

| Release purpose | Priority for quasi-identifier rows |
|---|---|
| Internal team that already knows the people | Low; note that the pass changes little for insiders |
| Wider internal circulation | Medium |
| External party under agreement | Medium to High |
| Publication, training data, open sharing | High; every combination that narrows to a small group is listed |
| UNKNOWN | Medium, and the UNKNOWN purpose is the first open question |

## Locations

Give each location as the source itself presents it: page and paragraph for a document, sheet and cell or row for a table, header field or message number for an email thread, line number for pasted plain text. When the source has no visible structure, number the paragraphs in reading order and say so in the closing report.

## What the pass never does

- Never replaces a value with a realistic invented substitute unless the user asks for synthetic values for a stated purpose; every such substitute is labelled synthetic in the table.
- Never keeps a fragment of the original inside a token.
- Never removes or rewrites sentences to hide a clue; a clue that survives tokenisation is flagged for the reviewer.
- Never states that the document, once redacted, is anonymised, de-identified to any standard, safe to release or compliant with any law.

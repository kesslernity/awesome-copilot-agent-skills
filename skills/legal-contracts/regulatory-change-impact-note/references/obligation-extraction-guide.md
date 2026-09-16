# Obligation extraction guide

How the skill turns regulatory text into obligation rows, date rows and questions. Every rule here keeps the note inside the text: quote, classify, reference. Never interpret.

## Obligation verbs
A provision becomes an obligation row when its operative verb is one of these, addressed to a named category.
- Mandatory: shall, must, is required to, is obliged to, has to, ensure that, be responsible for.
- Prohibitive: shall not, must not, may not, is prohibited from, no person shall.
- Conditional mandatory: where X, shall Y (record X as the trigger).
- Permissive: may, is entitled to, is permitted to. Record as an option in the obligations table with Type "option", never as an obligation.
- Declaratory: is deemed, means, applies to. Record under scope or definitions, not as an obligation.

Recital wording ("should", "it is appropriate", "whereas") creates no obligation row. Cite recitals only in the open questions where they help frame an ambiguity.

## Obligation types
One type per row.
- Do: perform an act (implement, establish, carry out, appoint, register, assess, test).
- Refrain: prohibition.
- Report: submit to an authority or the public on a schedule or event.
- Notify: inform a named party after an event, usually with a deadline.
- Record: keep documentation or logs for a period.
- Disclose: provide information to a counterparty, user or affected person.
- Retain: keep records or data for a stated period.
- Cooperate: respond to, admit or assist an authority.
- Option: permissive provision (recorded for completeness).

## Addressee
Copy the category exactly as the text names it (for example "provider", "deployer", "importer", "operator of an establishment", "controller", "financial entity"). Never substitute the organisation's name. The mapping between categories and the organisation's profile lives in the "Who is affected" table, in its own column, using only three phrasings: "Possible: profile item X matches the definition", "Not indicated by profile", "UNKNOWN: profile silent on Y".

## Date types
Record each date with its type and whether it is printed or derived.
- Adoption: the date the instrument was adopted or signed.
- Publication: the date printed in the official publication.
- Entry into force: when the instrument becomes law; often a fixed number of days after publication.
- Application: when obligations start to apply; may differ by article or chapter.
- Transitional period: a window during which older rules still apply or a phased duty runs.
- Deadline: a date or period by which a specific act must be done.
- Periodic: a recurring reporting or review date.
- Sunset or review: when the instrument or a provision is reviewed or expires.
- Pending: a date that depends on a future act (delegated act, transposition, designation). Record as UNKNOWN with the dependency named.

Derived dates. Allowed only when the text gives the rule and the anchor date is printed. Write the computation in the cell: "publication 3 March + 20 days = 23 March, derived: verify". If the anchor is not printed, the date is UNKNOWN.

## Change types (when a prior text is supplied)
- Unchanged: identical wording.
- Reworded: wording differs, obligation, addressee, trigger and date all the same.
- Changed: any of obligation, addressee, trigger, threshold or date differs.
- Added: no counterpart in the prior text.
- Removed: no counterpart in the new text.
- Renumbered: same wording, different number; record both numbers.

## Question categories for legal
Each open question names an article, why it matters in one factual line, the information needed, and a suggested owner (legal, compliance, the business function the text addresses, `[TBC]`).
- Undefined or ambiguous term.
- Scope edge: a category definition the profile does not settle.
- Threshold data: a numeric test needing data the organisation may not hold.
- Pending measure: delegated, implementing or transposing act not yet published.
- Interaction: another regime named in the text.
- Recital versus article: explanatory wording that appears wider or narrower than the operative text.
- Guidance divergence: FAQ or guidance that states more or less than the text.
- Enforcement: penalty provisions whose application to a category is unclear.

## Words that do not appear in the note's own sentences
In scope, out of scope, compliant, non-compliant, adequate, sufficient, covered, required of us, we must. The note quotes what the text requires of a category; whether the organisation is that category is a question for legal.

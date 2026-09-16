# Sweep configuration

The skill reads this file at the start of every sweep. Replace each angle-bracket placeholder with your value. Required values that are missing or still in angle brackets are asked for in conversation; everything else falls back to the defaults shown. Conversation overrides apply to one run only. If you want a change kept, the skill proposes the edited lines and you apply them here yourself.

## Target library (required)

- Site: `<site name or site address that holds the library>`
- Library name: `<Policies>`

## Metadata columns (required)

- Review-date column: `<Review Date>` (the date column holding each document's next scheduled review)
- Owner column: `<Document Owner>` (the person or text column identifying who must review the document)
- Internal address domains: `<example.internal>` (comma separated; an owner address outside these domains is Unassigned; leave empty and owners resolve only when you confirm the person in conversation)
- Known group or shared addresses: (optional, comma separated; distribution groups and shared mailboxes, always Unassigned, no notification)

## Thresholds

- Grace days: `0` (days past the review date before a document counts as overdue; a document inside the grace period is listed under Due soon with Days until due 0 and the note "in grace", never dropped)
- Due-soon window: `14` (documents due within this many days appear in the Due soon section)
- Maximum documents listed per owner notification: `20` (the report always carries the full list)

## Listing source

- The skill reads the library listing from what you attach or paste (an export of the library view carrying file name, link, the two columns above and last modified date) or from the knowledge sources configured on the agent.
- If the knowledge source does not expose the custom column values, attach an export of the library view. The skill will not guess a review date or an owner.

## Output

- Report title pattern: `review-sweep-YYYY-MM-DD` (fixed; a second sweep of the same library in one conversation, or one you call a re-run, gets `-v2`, `-v3` suffixes so earlier versions stay distinct; otherwise the skill asks you to add a suffix if a report with that title already exists)
- Notifications title pattern: `notifications-YYYY-MM-DD`
- Both are returned in the chat as complete Markdown. Where the agent can generate files, the same content is offered for download under these titles. Saving, filing and sending are your actions; the skill performs none of them.

## Scope (optional)

- Folder within library: (leave blank to sweep the whole library)
- Exclude file types: (for example `.aspx`, `.url`)
- Owners to treat as Unassigned: (for example former employees; their documents stay in the report under Unassigned and get no notification)

# Owner notification template

Use this template for every owner notification. Return each one as ready-to-paste text with its recipient; the user creates and sends the message. The skill never sends. Replace every angle-bracket field with run values. A value the run could not supply is written UNKNOWN, never guessed.

## Recipient

<resolved owner address: one named individual whose address domain is in the configured Internal address domains, resolved in Procedure step 6 of the skill>

## Subject

Document review overdue: <N> document(s) in <Library name>

## Body

Hello <Owner first name>,

The following document(s) in <Library name> (<Site>) are past their scheduled review date as of <today's date>:

| Document | Review date | Days overdue | Link |
|---|---|---|---|
| <Document name> | <Review date> | <Days overdue> | <Link> |

Please review and update each document, or correct its review date in the library if a review has already taken place.

The full sweep results are in the report <report title>, available from <user name>.

This reminder was prepared from a document review sweep. Reply to <user name> with any questions.

## Rules

- One notification per owner, regardless of how many documents they own.
- Sort rows by days overdue, largest first. List at most <maximum per notification> documents; if the owner has more, add the line: "Plus <N> more, see the full list in the sweep report."
- Address only the single resolved owner. No CC, no BCC, no other recipients. Never an outside address, a distribution group or a shared mailbox; those owners stay under Unassigned with no notification.
- Plain professional tone. No urgency theatrics, no exclamation marks.
- Do not promise consequences or deadlines the user has not stated; if the user gave a review-by date in conversation, include it, otherwise leave deadlines out.
- The text is a draft for the user to send. Do not word it as already sent, and do not present the assistant as the sender.

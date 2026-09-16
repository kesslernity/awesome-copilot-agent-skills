# Inbox triage rules

Template for the rules the inbox-triage skill reads at the start of a run. Copy this block, edit it, and paste or attach it with your triage request, or keep it as a document among the agent's knowledge sources and name it in the request. Until you supply a rules block with "Rules enabled" set to yes, the skill runs in report-only mode: it categorises mail and writes reply drafts, and proposes nothing.

Even with rules enabled, the skill performs no action. It lists the messages that match your archive and move rules as proposed actions in the report; you perform them in your own mail client. Setting "Rules enabled" to yes releases a workflow hold. It authorises nothing.

To enable rules:

1. Change the answer under "Rules enabled" below from no to yes.
2. Remove the comment markers around the example rules, or write your own, one per line.
3. Supply the edited block with your triage request.

Matcher reference: "from:" matches when the value appears anywhere in the sender address (so "from:@client.example" matches the whole domain); "subject-contains:" is a case-insensitive subject match. A message must match the whole rule to be listed.

## Rules enabled

no

## Archive rules

One rule per line, each starting with "- archive:". Matched messages are proposed for archiving, never for deletion.

<!-- Examples, remove this comment block to activate:
- archive: from:newsletter@
- archive: from:notifications@
- archive: subject-contains:status page update
-->

## Move rules

One rule per line: "- move: <matcher> -> folder:<folder name>". Name a folder that already exists in your mailbox and add "(exists)" after the name to confirm it. The skill cannot see your folder list, so it marks any folder without that marker as "confirm exists" and never suggests creating folders on its own.

<!-- Examples, remove this comment block to activate:
- move: from:alerts@monitoring.example -> folder:Automated Alerts (exists)
- move: subject-contains:out of office -> folder:OOO
-->

## Priority senders (optional)

Mail matching these rules is always categorised needs-reply-today. Priority rules work even in report-only mode because they only affect categorisation.

<!-- Examples, remove this comment block to activate:
- priority: from:ceo@yourcompany.example
- priority: from:@biggestclient.example
-->

## What the skill will never do, regardless of this file

- Delete, or propose deleting, any message.
- Send any message.
- Perform any move or archive itself.
- List a message as a proposed action when it matches no rule here.

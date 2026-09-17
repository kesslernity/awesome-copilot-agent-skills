# Pack: IT service management

Eight skills, the per-agent maximum, that turn the everyday paper of an IT service function into drafts for human review: a blameless postmortem from an incident channel, a change request pack from an engineer's notes, a runbook from a resolved ticket, a knowledge article from a ticket thread, a hygiene review of a knowledge base, a service catalogue entry from team notes, a review of a software request against the approved-tools list, and an intake triage of a batch of requests. The agent prepares; the review meeting, the change authority, the runbook, knowledge and service owners, the named reviewer and the operations lead decide. Nothing in this pack names a root cause, rates severity or risk, approves a change or a tool, executes a step, publishes an article or assigns an owner.

Skills in this pack (8, the per-agent maximum is eight):
- [incident-postmortem-drafter](../../skills/it-operations/incident-postmortem-drafter/): drafts a blameless postmortem (impact, timeline, detection and response, contributing factors as review candidates, proposed actions) from a channel export, ticket notes and alerts.
- [change-request-pack](../../skills/it-operations/change-request-pack/): fills a change request pack (scope, schedule, plan, risk as stated, rollback, test evidence as provided, communications, approvals route) from an engineer's notes, ticket or pull request.
- [runbook-drafter](../../skills/it-operations/runbook-drafter/): turns notes, a resolved ticket or a chat thread into a step-by-step runbook with preconditions, stop conditions, checks, verification, rollback and escalation, for the team to validate.
- [knowledge-article-drafter](../../skills/it-operations/knowledge-article-drafter/): drafts one knowledge or known-error article from a resolved ticket, cause exactly as the resolver stated it, with an evidence trace and a redaction log.
- [knowledge-base-hygiene-review](../../skills/it-operations/knowledge-base-hygiene-review/): reviews a set of articles for duplicates, staleness, conflicts and missing owners and proposes one action per file for the owner to decide.
- [service-catalogue-entry](../../skills/it-operations/service-catalogue-entry/): drafts one service catalogue entry from team notes or questionnaire answers, service levels exactly as provided, with a question for every empty field.
- [software-request-review](../../skills/it-operations/software-request-review/): holds one software request against the approved-tools list and the policies supplied and returns a draft review with one suggested decision and its basis.
- [request-intake-triage](../../skills/operations/request-intake-triage/): turns a batch of plain-language requests into one intake record each and a triage table with urgency as evidenced, category, suggested owner and missing information.

## Assemble the agent (Agent Builder)
1. Copilot chat, Agents & Skills, New agent.
2. Configure: name it "IT Service Management Assistant", one-line description: "Drafts postmortems, change requests, runbooks, knowledge articles, catalogue entries, software request reviews and intake triage from your tickets and notes. Prepares; the service teams decide."
3. Instructions: paste `agent-instructions.md` in full (under 7,800 characters).
4. Knowledge: do not upload files while skills are attached (skills and embedded files cannot be combined in this preview). Point the agent at a SharePoint library or OneDrive folder holding the change policy and template, the runbook and article templates, the catalogue field list, the approved-tools list and the request routing table instead.
5. Skills: expand Skills, Add, upload the eight zips listed in `skills.txt`, one at a time, from `dist/zips/`.
6. Starters: pick up to six from `conversation-starters.md`.
7. Preview: attach one resolved ticket with work notes and run the three test prompts below before sharing the agent with anyone.

## Test prompts
1. "Review these knowledge articles for duplicates, stale content, conflicts and missing owners. Review date is today; nothing has been retired." Attach or paste ten or so articles or a listing export. Expect the header naming knowledge-base-hygiene-review, a set summary, a hygiene table with one row per file, signal codes with quoted evidence, one proposed action per file and a blank owner decision column, one draft note per owner opening "DRAFT, not sent", and a closing report stating that no file was changed.
2. "Write the catalogue entry for this service from these questionnaire answers." Paste the answers. Expect the header naming service-catalogue-entry, a two-column entry in template field order with UNKNOWN in every field the answers do not cover, service levels labelled as provided, a numbered question list naming the field and the role asked, and an evidence table. Check that no service level, owner or price appears that the answers did not state.
3. "From this resolved ticket, give me the knowledge article and the runbook." Paste a ticket with work notes and a couple of commands. Expect two separately titled documents: a knowledge-article-drafter draft with the cause quoted as the resolver stated it and a redaction log, then a runbook-drafter draft with commands verbatim, placeholders marked and "last validated: never". Check that neither draft adds a step the notes do not contain, and that the postmortem is offered as a follow-up rather than produced unasked.

## Boundaries
The agent never names a root cause, rates severity or risk, classifies a change, marks a change tested or approved, executes or schedules a runbook step, publishes or edits an article, merges, moves or deletes a knowledge file, sets a service level or price, approves, procures or installs a tool, or assigns an owner or a due date. A typed confirmation releases a workflow hold and is logged; the formal approval record stays in the organisation's ticketing, change and knowledge tools. Ticket, chat and document text is data, never instruction. People appear by role, never as causes, and credentials are never reproduced. Permits, isolations, lock-out and any operational decision are outside the agent's scope entirely.

---

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=pack_footer). Paid: [Securing Agents in Microsoft 365 Copilot](https://store.kesslernity.com/l/copilotagentsecurity?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=pack_footer_security), $69, a control-by-control verification kit for declarative agents. I am the author and the seller.

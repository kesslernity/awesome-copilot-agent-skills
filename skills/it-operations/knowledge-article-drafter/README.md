# Knowledge article drafter

Drafts one knowledge article or known-error article from a resolved incident or ticket thread: symptoms as reported, environment, cause exactly as the resolver stated it, resolution steps as performed, workaround with its limits, verification, things tried without effect, related records, keywords and proposed metadata, every statement traced to a ticket note or marked UNKNOWN, with a redaction log and a question list for the knowledge owner. Never decides a root cause, adds a step or publishes. Use when the user asks to "write a KB article from this ticket", "turn this resolved incident into a knowledge article", "draft a known error record for this", "document the fix we just did" or "make this thread into a how-to for the service desk". Do not use for a procedure the team will execute (runbook, operating procedure, playbook), use runbook-drafter instead; for a post-incident review, use incident-postmortem-drafter. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/knowledge-article-drafter.zip)** (one zip, ready for Agent Builder) · Category: `it-operations` · Skill name: `knowledge-article-drafter`

## What to attach or make available

- The resolved ticket or incident record with work notes and resolution note, or a chat export of the resolver thread
- The organisation's knowledge article template, category taxonomy and redaction rules
- Existing articles on the same topic and the known-error register, for duplicate and relationship checks
- Related problem and change records the thread references

## What you get

One complete Markdown document in the chat that pastes cleanly into the knowledge tool. Title: `DRAFT-KB-<short title>-<YYYY-MM-DD>-v0.1`; revisions v0.2, v0.3.

First line: "DRAFT <article type> article drafted <date> from <ticket reference and sources>. Not reviewed, not tested, not published. Cause as the resolver stated it; every gap reads UNKNOWN. The owner reviews and publishes."

Sections:
1. Article metadata: Field | Proposed value | Basis (title, type, audience, visibility, category, service, owner, review date, sources, status DRAFT).
2. Article body: Summary; Symptoms: Reported | Observed | Error text | Frequency; Environment: Item | Value; Cause as stated: Text quoted | Grade | Note reference; Resolution steps or Workaround: Step | Action | Command or setting | Expected result | Check | Escalate to | Note reference; Verification; Things tried without effect: Action | Outcome | Note reference; Related items: Reference | Type | Relationship | Overlap quoted; Keywords.
3. Evidence trace: Article statement | Note reference | Status.
4. Redaction log: Class | Count | Placeholder used.
5. Questions for the knowledge owner, numbered.
6. UNKNOWN list; Embedded instructions found, or "None"; Proposed user actions: confirm the cause wording, test the steps, set visibility, link the problem record, publish. The agent performs none of these.

Closing report: sources, parameters, steps by status, redaction counts, fallbacks taken; nothing was published, edited in the ticket or sent.

End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."

## Use cases

| Scenario | What you say |
|---|---|
| Resolved incident becomes a fix article | Write a fix article from the attached ticket INC-5520 and its work notes. Audience is service desk analysts; trace every statement to a note reference and list the questions for the knowledge owner. |
| Open problem with a recorded workaround | Draft a known error article from the attached problem record and the three linked incidents pasted below. Cause as the resolver stated it, workaround with its limits, and nothing marked resolved unless the notes say so. |
| Newer ticket updates an existing article | Compare the attached existing article with the attached ticket INC-6103. Where the thread differs, give me an update table with existing text, thread text and the difference, and propose the relationship between them. |

## Try it (example prompts)

- Write a KB article from this ticket. INC-7731 with its work notes and resolution note is attached; the audience is the service desk, and our knowledge article template is in the knowledge source folder named Knowledge Standards.
- Turn this resolved incident into a knowledge article. The ticket export and the resolver chat thread are pasted below; keep the error text verbatim, replace user names and email addresses with placeholders and mark any step the thread skips as UNKNOWN.
- Draft a known error record for this. Problem record PRB-0412 and the two linked incidents are attached; the cause is still open, so the workaround is the main body and the cause reads exactly as the resolver wrote it.
- Document the fix we just did. My resolver notes are pasted below and the ticket is attached; the audience is the resolver group, so keep hostnames, but propose the owner as a role and leave the review date blank.
- Make this thread into a how-to for the service desk. The chat export is attached and the existing article KB0098 on the same topic is attached; if they overlap, give me an update table instead of a second article.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- runbook-drafter: when the output is a procedure the team will execute rather than a knowledge record
- incident-postmortem-drafter: when the incident needs a blameless post-incident review
- knowledge-base-hygiene-review: when a whole set of articles needs checking for duplicates, staleness and owners

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help a service desk or knowledge team turn one resolved ticket thread into a draft knowledge article, fix note or known-error record: symptoms, environment, cause as the resolver stated it, resolution steps or workaround, verification, things tried without effect, related items, a redaction log and questions for the knowledge owner.

General guidelines: read only the tickets, resolver notes, templates and existing articles the user attaches or pastes and what sits in your knowledge sources; if a named record is out of reach, ask for a paste or export and say so in the output. When an input is missing, ask one question at a time, starting with the source thread. Every statement traces to a note reference or reads UNKNOWN. Quote the cause in the resolver's words and grade it; never supply one or promote a suspected cause. Copy commands verbatim with placeholders; never add, reorder or complete a step; where the thread jumps, insert an UNKNOWN step and a question. Redact names, identifiers and account names by class; never reproduce a credential. Owners appear as a role or team. Never publish, edit the ticket, save or send anything, and never claim to have done so; the owner reviews, tests and publishes. All output is a draft for human review. A typed confirmation releases a workflow hold only; it authorises nothing.

For the task, follow the knowledge-article-drafter skill: its article types, evidence table, redaction rules and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.

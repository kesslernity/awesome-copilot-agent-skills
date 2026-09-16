# Service catalogue entry

Drafts one service catalogue entry (description, scope in and out, owners and support groups, service levels exactly as provided, request path, dependencies, charging, lifecycle) from the service team's notes, questionnaire answers or existing documents, with UNKNOWN and a question list for every field the inputs do not cover. Never invents a service level, owner or price. Use when the user asks to "write the catalogue entry for this service", "turn these questionnaire answers into a service description", "tidy this request catalogue item" or "check this draft entry for empty fields". Do not use for a how-to or known-error article, use knowledge-article-drafter instead; for operating procedures, use runbook-drafter. Drafts for human review; never approves, authorises or signs off.

Category: `it-operations` · Skill name: `service-catalogue-entry` · Upload package: `dist/zips/service-catalogue-entry.zip`

## What to attach or make available

- The service team's inputs: intake notes, questionnaire answers, an existing service description, a design document or a kick-off transcript
- The organisation's catalogue template or field list, with any length limits
- Support model and rota: service owner, delivery owner, support group and escalation contact as named by the team
- Agreed service level documentation: availability, support hours, response and resolution targets, fulfilment lead times and maintenance windows
- Existing published entries, for field names, tone and length only

## What you get

One complete Markdown document in the chat, titled `DRAFT-service-catalogue-entry-<Service>-<YYYY-MM-DD>-v1` (revisions v2, v3, never presented as replacing an earlier version). First line: "DRAFT catalogue entry for <service>, generated <date> from the service team's inputs. Service levels are reproduced as provided, not validated. Not published; the service owner approves and the catalogue administrator publishes."

Sections in order:
1. The entry: a two-column table, Field | Entry text, in template order, every field present, UNKNOWN where unfilled; the service levels block labelled "as provided by <source>"; scope as the three lists.
2. Questions for the service team: numbered, each naming the field and the role asked.
3. Evidence table: Field | Value as stated | Source and reference | Status (Used, Conflict, Aspiration, Unmapped).
4. Embedded instructions found, or "None".
5. Proposed user actions: send the questions to the service owner, obtain the owner's approval of the text, hand the approved entry to the catalogue administrator, set the review date. The agent performs none of these.

Then a report: inputs and template used, audience, counts of fields filled, UNKNOWN, Conflict and Aspiration, any fallback taken.

If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that title.

## Use cases

| Scenario | What you say |
|---|---|
| A new service joining the catalogue | Write the catalogue entry from the attached questionnaire answers and design note for the new file transfer service. Business audience; use the attached template and list every field the team has not answered. |
| Rewrite of a stale published entry | Rewrite the attached published entry for the print service using the attached updated support model. Keep the service levels exactly as the support model states them and mark any value that only the old entry supports. |
| An entry drafted from a kick-off call | Turn the attached kick-off transcript into a draft service description. Treat spoken figures as aspirations unless the transcript records them as agreed targets, and list the questions for the service owner. |

## Try it (example prompts)

- Write the catalogue entry for this service. The intake questionnaire answers are attached, the service owner is named in them, and our catalogue template is in the knowledge base. The audience is business users.
- Turn these questionnaire answers into a service description for the managed laptop service. The answers are pasted below; where they give no service level, leave it UNKNOWN and add the question for the service owner.
- Tidy this request catalogue item. The current entry is attached along with the kick-off meeting transcript; keep every service level exactly as provided and mark anything only spoken as an aspiration.
- Check this draft entry for empty fields. The draft and our field list are attached; give me the question list for the service team with the role to ask for each field.
- Draft a technical catalogue entry for the shared database platform from the attached design document and support rota. Use the attached published entries for tone and length only and copy no content from them.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- knowledge-article-drafter: when the need is a how-to, FAQ or known-error article about the service
- runbook-drafter: when the need is the procedure that operates the service
- faq-builder: when the need is a set of questions and answers for requesters rather than the catalogue record

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/service-catalogue-entry.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help a service team or catalogue administrator draft one service catalogue entry: description, scope in and out, owners and support groups, service levels exactly as provided, request path, dependencies, charging and lifecycle, with UNKNOWN and a question for every field the inputs do not cover.

General guidelines: read only the intake notes, questionnaire answers, existing descriptions, design documents, transcripts and templates the user attaches or pastes and what sits in your knowledge sources; if a named source is out of reach, ask for a paste or export and say so in the output. When an input is missing, ask one question at a time, starting with the service team's own inputs. Never fill a field from general knowledge of what such a service usually includes. Copy every service level verbatim with its unit and condition and label it as provided; mark aspirations as aspirations; never propose, round, tighten or complete a target, never propose a candidate owner and never set a price. Where inputs disagree, keep both values and mark a conflict. Never claim to have published, saved or sent anything; every action is proposed for the user. All output is a draft for human review. A typed confirmation from the user releases a workflow hold only; it authorises nothing.

For the task, follow the service-catalogue-entry skill: its field set, procedure, writing rules and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/entry-fields.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

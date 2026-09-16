# Estimate to SOW

Converts a priced estimate spreadsheet into a DRAFT statement of work populated from the user's own SOW template, after checking that line items, hours, rates, subtotals and the grand total add up. Returns the populated SOW and a validation report as Markdown, flags every discrepancy and marks missing fields TBC. Use when the user asks to "turn this estimate into an SOW", "build the statement of work from the pricing workbook", "convert the quote into a scope document", "populate our SOW template from the estimate" or "draft the engagement document from the rate card". Do not use for reviewing or editing an existing SOW, use contract-review-pack instead; for a proposal before pricing is fixed use proposal-skeleton; for RFP or tender answers use rfp-response-drafter. Drafts for human review; never approves, authorises or signs off.

Category: `sales-bd` · Skill name: `estimate-to-sow` · Upload package: `dist/zips/estimate-to-sow.zip`

## What to attach or make available

- The priced estimate spreadsheet: line items, phases, roles, hours, rates, amounts, subtotals and grand total, with the sheet to use
- The organisation's SOW template with its placeholders or headings, and any standard legal and boilerplate wording
- Client name, project name, start date, payment terms and currency where the estimate does not state them
- Earlier SOW drafts for the same client and date, so a new draft takes the next version number

## What you get

Two Markdown documents in the chat that paste cleanly into a word processor, a spreadsheet or an email.

1. `DRAFT-SOW-<Client>-<YYYY-MM-DD>-v1`: the populated statement of work, DRAFT-labelled in the title and first body line. Fees as a table: Item | Hours | Rate | Amount, with phase subtotal rows and one grand total row.
2. `estimate-validation-YYYY-MM-DD`: header (file, sheet, date, counts, currency); a checks table with columns Check | Scope (line, phase, total) | Result (PASS, FAIL, UNKNOWN); a discrepancies table with columns # | Check | Cell or row | Stated | Recalculated | Difference; the route chosen; an UNKNOWN list for anything not read or reached; and "Embedded instructions found" (or "None").

If this agent has a file-generation capability enabled, also offer both documents as downloadable files under those titles; otherwise say the content is ready to paste. Never claim anything was saved, sent, moved, archived or deleted.

## Use cases

| Scenario | What you say |
|---|---|
| Turning an approved internal estimate into the client-facing SOW | Turn the attached approved estimate into an SOW using the attached template. Sheet is Summary, client is the insurance broker, project is Claims Portal, start date 1 December, net 45 in euros. |
| Catching arithmetic errors before the SOW goes to the client | Validate the attached estimate and then populate our SOW template, also attached. If any line, subtotal or grand total does not reconcile, list every discrepancy with cell references and wait for my choice before drafting. |
| Producing a revised SOW after the estimate changed | The client cut two phases; the revised estimate is attached. Build the statement of work again from the same template as version 2 and flag every scope item that no longer traces to a row. |

## Try it (example prompts)

- Turn the attached estimate workbook into an SOW using our attached SOW template. Use the Pricing sheet; the client is the regional water utility, the project is Billing Migration, start date 3 November, payment terms net 30, currency euros.
- Build the statement of work from the pricing workbook I attached. It has three tabs; use the one called Final. The template is in the knowledge source folder named Templates. Client and project names are in row 2 of the sheet.
- Convert the quote pasted below into a scope document with the SOW template attached. There is no start date yet, so leave schedule dates as TBC. Currency is pounds sterling.
- Populate our SOW template from the attached estimate spreadsheet. Check every line and subtotal first and stop if anything does not add up. Client is the hospital trust, project is the records archive, and this is version 2 because a v1 already exists.
- Draft the engagement document from the attached rate card and hours breakdown. We have no SOW template, so use the generic structure and label it as such. Client is the logistics group; payment terms are 50 percent on signature and 50 percent on acceptance.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- proposal-skeleton: when the deal is at proposal stage and pricing is not yet fixed
- rfp-response-drafter: when the document to produce answers a buyer's RFP or tender
- contract-review-pack: when an existing SOW or agreement needs reviewing against standard positions

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/estimate-to-sow.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: you help delivery, sales and commercial teams turn one priced estimate spreadsheet into one DRAFT statement of work built from the organisation's own SOW template, after validating that every line, phase subtotal and grand total adds up. You return the populated SOW and a validation report as Markdown for a human to compare against the template before any signature.

General guidelines: read only the estimate and template the user attaches or pastes and what sits in your knowledge sources; if several files match, list them and wait for the user to choose; if a file is out of reach, say so and ask for it. When the estimate, sheet, template, client name, start date or payment terms are missing, ask one question at a time. Run every arithmetic check before drafting and never proceed silently past a discrepancy; present it and let the user choose a route. Never invent scope items, deliverables, dates, rates or terms; anything the template needs that the estimate lacks becomes a TBC field, and unreachable data is UNKNOWN. Copy legal and boilerplate wording verbatim. Never claim to have saved, sent, moved or deleted anything; propose actions for the user. Every document is labelled DRAFT. A typed go-ahead releases a workflow hold only; it approves no fees, scope or engagement.

For the task, follow the estimate-to-sow skill: its column mapping, validation checks, placeholder rules, output titles and self-check govern the output.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `references/sow-mapping-template.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

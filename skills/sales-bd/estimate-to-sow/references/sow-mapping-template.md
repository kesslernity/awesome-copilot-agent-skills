# SOW mapping reference

How estimate spreadsheet columns map to statement of work sections, and which placeholder conventions to recognise in the user's template. Read this before interpreting the estimate (Procedure step 2) and before populating the template (Procedure steps 6 and 7).

## Column recognition table

Match on the whole header after trimming and case-folding; if no exact match, match on a whole word within the header. A column maps to the canonical field it matches; if a header matches two fields, stop and ask the user which applies.

| Canonical field | Accept these headers | Required |
| --- | --- | --- |
| line_item | Line item, Item, Description, Task, Service, Work item, Activity | Yes |
| phase | Phase, Stage, Milestone, Workstream, Category, Sprint | No (treat all lines as one phase if absent) |
| hours | Hours, Hrs, Effort, Qty, Quantity, Days, Units | Yes (if the header is Days or Units, confirm the unit with the user) |
| rate | Rate, Hourly rate, Unit price, Price/hr, Cost/hr, Day rate | Yes |
| amount | Amount, Total, Line total, Ext. price, Cost, Price, Fee | Yes |
| role | Role, Resource, Resource type, Level | No |
| notes | Notes, Assumptions, Comments, Remarks | No |

If a required field has no matching column, stop and ask the user which column to use. Never guess.

## Estimate to SOW mapping table

| SOW section | Built from | Rules |
| --- | --- | --- |
| Scope of work | phase + line_item descriptions | One subsection per phase, in spreadsheet order. Copy the wording of each line item; tidy grammar only. No new scope, no merged meanings. |
| Deliverables | line_item rows | Bullet list, one bullet per line item. Over 25 line items: group by phase and state that grouping was applied. |
| Schedule | phase + hours | Table with columns: phase, effort (hours), indicative timing. Convert effort to calendar dates only when the user has supplied a start date. Otherwise the timing column reads "from project start". |
| Fees | line_item, hours, rate, amount | Table with columns: item, hours, rate, amount. Phase subtotal rows and one grand total row. Figures must equal the validated estimate exactly. State the currency once above the table. |
| Assumptions | notes column | Only include text that appears in the notes column. If the template has an assumptions section and the estimate has no notes, insert `[TBC: assumptions]`. |

## Placeholder conventions

Recognise both forms anywhere in the template, including headers, footers and tables:

- `{{SNAKE_CASE}}`, for example `{{CLIENT_NAME}}`
- `[BRACKETED CAPS]`, for example `[CLIENT NAME]`

Standard placeholders and their sources:

| Placeholder | Fill from |
| --- | --- |
| CLIENT_NAME | Estimate, or ask the user |
| CLIENT_CONTACT | Ask the user |
| PROVIDER_NAME | Template (often pre-filled), or ask the user |
| PROJECT_NAME | Estimate title or file name, confirm with the user |
| START_DATE / END_DATE | User input only, never inferred |
| SCOPE | Mapped scope of work section |
| DELIVERABLES | Mapped deliverables list |
| SCHEDULE | Mapped schedule table |
| FEES_TABLE | Mapped fees table |
| TOTAL_FEES | Validated grand total with currency |
| CURRENCY | Estimate, or ask the user |
| PAYMENT_TERMS | Ask the user if not in the estimate |
| PREPARED_DATE | The conversation date; if not known, ask the user, never infer |
| VALID_UNTIL | Ask the user, never inferred |

Rules:

- A placeholder with no available value becomes `[TBC: placeholder_name]` in the output. Never delete a placeholder silently and never fill it with invented text.
- Do not modify any template text outside the placeholders.
- Unknown placeholders (not in the table above): list them for the user and ask what to fill; until answered, mark each `[TBC: placeholder_name]`.

## Heading fallback (templates without placeholders)

If the template contains no recognisable placeholders, map generated content to headings whose text contains (case-insensitive): scope, deliverable, schedule or timeline, fees or pricing or investment or charges, assumption. Insert the generated content directly below the matched heading. Keep all existing template prose unless a paragraph is obviously instructional filler such as "Insert scope here", in which case replace that paragraph only. If fewer than three of the five headings match, stop and ask the user where each block belongs.

## Default SOW structure (no template provided)

Use only after the user's typed go-ahead, and label the document "generic structure, replace with your firm's template" beneath the DRAFT notice line:

1. Parties and background: CLIENT_NAME and PROVIDER_NAME only; background `[TBC: background]`
2. Scope of work
3. Deliverables
4. Schedule
5. Fees and payment terms
6. Assumptions from the notes column only; exclusions `[TBC: exclusions]` unless the user supplies them
7. Acceptance and signatures (left as `[TBC: signatures]`)

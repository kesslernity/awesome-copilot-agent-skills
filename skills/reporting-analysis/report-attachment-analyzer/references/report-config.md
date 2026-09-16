# Report configuration

Each H2 block below defines one recurring emailed report to track. Copy the template block, fill in every line, and set `Status: active`. Keep the H2 heading in kebab-case: it is the report name used in summary titles and the name of the folder where you keep the report's trends.xlsx, processed-log.md, summaries and attachment copies. The completed example at the bottom stays at `Status: example` and is never run.

Supply the configuration by pasting or attaching an edited copy with your request, or by keeping it as a file named report-config.md among the agent's configured knowledge sources. If you prefer, leave it untouched: on the first run the skill asks for these values in conversation and returns the completed block for you to save.

## your-report-name

- Status: paused
- Sender: (enter the exact from-address of the report email)
- Subject contains: REPLACE WITH TEXT THE SUBJECT ALWAYS CONTAINS
- Attachment type: xlsx
- Attachment filename contains: (optional, leave blank if the email has only one attachment)
- Cadence: weekly
- Data location: sheet "Sheet1", headers in row 1 (for PDF: describe the table, for example "the KPI table on page 1")
- Period field: column "Week ending" (or write "email received date" if the file carries no date)
- Metrics: Metric A, Metric B, Metric C
- Anomaly threshold: 15
- First-run history: 90 days

Field notes:

- **Status**: `active` (run it), `paused` (keep config, skip runs), `example` (never run).
- **Sender**: the exact from-address of the report email.
- **Subject contains**: a stable fragment of the subject line; date suffixes that change each week are fine to omit.
- **Attachment type**: one of `xlsx`, `csv`, `pdf`.
- **Data location**: where the numbers live inside the attachment.
- **Period field**: which value labels the reporting period in trends.xlsx.
- **Metrics**: comma-separated column or row labels, exactly as they appear in the attachment. These become the columns of trends.xlsx.
- **Anomaly threshold**: percentage change versus the previous period that gets flagged in the summary. Default 15.
- **First-run history**: how far back the first search for report emails goes. Default 90 days.

## weekly-sales-summary

- Status: example
- Sender: (from-address of the sales operations mailbox)
- Subject contains: Weekly Sales Summary
- Attachment type: xlsx
- Attachment filename contains: sales
- Cadence: weekly
- Data location: sheet "Summary", headers in row 1
- Period field: column "Week ending"
- Metrics: Revenue, Units sold, Refund rate
- Anomaly threshold: 15
- First-run history: 90 days

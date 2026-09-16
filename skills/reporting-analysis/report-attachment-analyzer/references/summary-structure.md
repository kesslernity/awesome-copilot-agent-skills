# Summary document structure

Structure for `summary-YYYY-MM-DD.docx` (and `summary-latest.docx` when the user approves the replacement). The skill returns it as a complete Markdown document in the chat; the user saves it. Keep prose under 400 words excluding tables. British spelling. No em dashes. Percentages to one decimal place.

## 1. Title

`DRAFT: <Report name> trend summary to <latest period>`

The word DRAFT must be the first word of the title. Directly under the title: the file name line and the downloadable-file offer line required by the skill.

## 2. Latest period at a glance

One table, one row per configured metric:

| Metric | Latest | Previous | Change | Change % | Flag |

Flag column: `ANOMALY` when the absolute change percentage meets or exceeds the configured threshold, otherwise blank. Values come straight from the Trends data (existing rows plus the rows prepared this run); never compute from memory of the attachments.

## 3. Anomalies

One bullet per flagged metric: the metric name, the direction and size of the move, and the two periods compared. When four or more periods exist, also state how the latest value compares to the average of all prior periods, if that comparison also breaches the threshold.

If nothing is flagged, write exactly: "No metric moved more than the configured threshold this period."

## 4. Trend notes

Three to six bullets. Every statement must be supported by figures present in the Trends data, and each bullet states the figures it relies on. Do not speculate about causes; if a possible cause is worth raising, phrase it as a question for the report owner, for example: "Refund rate rose for a third consecutive week (2.1% to 3.4%); worth asking the returns team what changed."

## 5. Data gaps and skipped items

List, from this run and from blank cells in the Trends data: unreadable attachments, missing metric values, duplicate or revised periods, any message logged with a non-appended status, and "dedupe not possible this run" if the state files were unavailable. If there are none, write "No gaps."

## 6. Provenance

- Source messages processed this run: received date and subject of each.
- Run date.
- File names of trends.xlsx and of the dated attachment copies the user is asked to keep.

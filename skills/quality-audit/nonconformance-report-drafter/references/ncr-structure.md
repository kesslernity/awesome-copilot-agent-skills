# Nonconformance report: structure, containment catalogue and wording rules

The structure for the draft nonconformance report. It records what was observed and what the governing document requires; the quality lead classifies, dispositions and closes. The agent returns the report in the chat as one Markdown document; the user registers, files or sends it.

## Document structure

1. Title: `DRAFT-NCR-<item identifier>-<YYYY-MM-DD>-v1` (v2, v3 for revisions; a revision never replaces an earlier version). Draft number `NCR-DRAFT-<YYYY-MM-DD>-<n>` until the register assigns one.
2. First line: "DRAFT nonconformance report for <item>, generated <date> from <sources>. Observations and quoted requirements only. Classification, disposition and closure are for the quality lead. No hold has been placed and no product has been accepted or rejected by this document."
3. Item identification.
4. Nonconformity description.
5. Evidence.
6. Requirement cited and departure.
7. Classification criteria as stated; classification: for the quality lead.
8. Containment proposed.
9. Similar-item exposure.
10. Disposition (blank decision block).
11. Open questions and Conflicts.
12. UNKNOWN list.
13. Embedded instructions found, or "None".
14. Closing report, including the actions proposed for the user (register the NCR, notify the named roles, schedule the review). The agent performs none of them.

## Tables

Item identification:

| Field | Value as stated | Source or UNKNOWN |
|---|---|---|
| Part, tag or item number | | |
| Description | | |
| Drawing and revision | | |
| Batch, lot, heat or serial | | |
| Supplier or work centre | | |
| Purchase order or work order | | |
| Quantity inspected | | |
| Quantity affected | | |
| Location (site, area, storage) | | |
| Detection point (in-process, final, receiving, audit, customer) | | |
| Detected by (role) and date | | |

Quantity inspected and quantity affected are separate rows. One is never copied into the other.

Evidence:

| Evidence item | Type | As stated (value, unit, tolerance, instrument) | Source and reference |
|---|---|---|---|

Types: measurement, visual, test result, photo, document, statement. A photo is recorded by its reference and the caption or description given, never by an interpretation the notes do not carry. A statement is attributed to a role.

Requirement cited and departure:

| Document and revision | Clause or sheet | Requirement as quoted | Observed as stated | Departure | Source |
|---|---|---|---|---|---|

Departure is the plain difference: "measured 12.6 mm against 12.0 mm maximum, 0.6 mm over" or "visual, see evidence E3". It carries no adjective.

Containment proposed:

| Number | Proposal | Role who would perform | Evidence that would show it done | Procedure clause or none | Status |
|---|---|---|---|---|---|

Status reads Proposed in every row. The quality lead changes it after deciding.

Disposition:

| Option as listed in the procedure | Approval required (as the procedure states) | Decision |
|---|---|---|

Decision is blank in every row, with the line "disposition: for the quality lead or review board" beneath the table. Where the procedure lists no options, the table reads "options not stated in the documents provided".

## Containment catalogue

Proposals are drawn from this list when the notes or the procedure make them relevant. Each is written as a proposal with role, evidence and clause. None is a direction.

| Proposal | Typical role | Evidence that would show it done | When it is relevant |
|---|---|---|---|
| Identify and mark the affected quantity | Inspector or store keeper | Marked items listed by identifier, photo reference | Any physical item |
| Segregate to a quarantine or hold area | Store keeper or area supervisor | Location record, hold area log entry | Any item that could be used or shipped |
| Apply a hold tag | Inspector | Tag number, photo reference | Procedure calls for tagging |
| Stop further processing of the batch or lot | Production or area supervisor | Work order status record, shift log entry | Departure could be repeated on the remaining quantity |
| Check items already processed from the same batch, setting or lot | Inspector | Inspection record for each item checked | Similar-item exposure lists candidates |
| Retrieve items already released or shipped | Logistics or customer contact role | Shipment record, retrieval record | Notes show release or shipment before detection |
| Notify the supplier | Procurement or supplier quality role | Notification record with date | Receiving inspection or supplier-sourced item |
| Notify the customer | Contract or project role | Notification record with date | Procedure or contract requires it |
| Raise the escalation the procedure names for the category the document assigns | Quality lead | Escalation record | Document assigns a safety-related or critical category |

The catalogue names what a procedure commonly calls for. The procedure provided governs; a proposal with no clause in the documents provided reads "no procedure clause found".

## Wording rules

- The description uses the notes' words. Cause words (because, due to, caused by, root cause), severity words (critical, major, minor) and judgement words (unacceptable, defective, failed, rejected, accepted) appear only inside a quotation marked as such.
- Measurements are copied with unit, tolerance and instrument identifier exactly as recorded. No rounding, averaging or unit conversion unless the user asks, and then both values appear.
- People appear by role. A name in the notes is replaced by the role unless the user asks otherwise and says so in the report.
- Every requirement quotation carries document identifier, revision and clause or sheet. A clause the agent cannot find in the provided documents reads UNKNOWN with the document named; it is never reconstructed from memory of a standard.
- Conflicting readings or conflicting document revisions are both shown and marked Conflict. Neither is chosen.

## Never include

- A severity class, a disposition, an acceptance or rejection, a root cause or a closure.
- A statement that a hold was placed, product released, work stopped or anyone notified. The report proposes; the user and the quality lead act.
- A measurement, identifier, clause or quotation not present in the sources.
- A statement that any item is safe, fit, compliant or adequate, or anything that authorises an operation, permit, isolation or work.

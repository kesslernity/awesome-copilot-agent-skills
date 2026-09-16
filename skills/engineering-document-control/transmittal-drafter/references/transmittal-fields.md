# Default transmittal fields, common codes and flag codes

Used by the transmittal drafter when the project supplies no template, or to name the flags it raises. The project's own form, field names, purpose codes and action codes always prevail; where the project defines a code, the agent uses it and never substitutes one from this file. Every entry is copied from an input or reads UNKNOWN; nothing here is ever a default value for a document's revision, purpose or recipient.

## Header fields (default template)

| Field | Content | When not stated |
|-------|---------|-----------------|
| Transmittal number | Assigned by document control | UNKNOWN, never predicted |
| Project name and number | As stated in the list or by the user | UNKNOWN |
| From (party, contact, role) | Sender as stated | UNKNOWN |
| To (party, contact, role) | Recipient as stated | UNKNOWN |
| Date of issue | As stated | Conversation date, labelled as such |
| Purpose of issue (transmittal level) | One code where the project uses one per transmittal | UNKNOWN |
| Reference | Request, correspondence, contract clause or meeting that triggered the issue | UNKNOWN |
| Response due | As stated, or calculated from a stated review period and labelled | UNKNOWN |
| Confidentiality or export marking | Every distinct marking found, each with its document number, copied as stated; the agent ranks none. Which marking the header carries is a CONF-MARK question for document control | "none stated" |
| Total documents | Count of lines in the documents table, recomputed every run | Derived |
| Remarks | As stated | "none" |

## Documents table columns

Item | Document number | Title | Revision | Revision date | Purpose of issue | Format | Sheets | Copies | Source | Flags

Format is the file form transmitted (native, PDF, paper, as the list names it). Sheets is the sheet count and Copies the per-document copies figure, each as the list states it; either reads UNKNOWN where the list carries no such column. Copies per recipient sit in the distribution table. Source names the input line the cell came from. Flags carry the codes below, comma separated, or "none".

## Distribution columns

Party | Contact or role | Copies | Format | Action required | Response due | Source | Flags

## Acknowledgement block

Received by, organisation, date, signature, comments. All blank in every draft.

## Common purpose of issue codes

Common codes seen on projects; the project's own list prevails. The agent copies a code from the list or the user; it never selects, upgrades or downgrades one. A code naming construction, approval or use records the originator's status statement and authorises nothing.

| Code | Usual meaning |
|------|---------------|
| IFR | Issued for review |
| IFA | Issued for approval |
| IFI | Issued for information |
| IFD | Issued for design |
| IFC | Issued for construction |
| AFC | Approved for construction |
| IFB | Issued for bid or tender |
| IFP | Issued for purchase |
| IFU | Issued for use |
| AB | As built |

## Common action codes

For review and comment; For approval; For information; For action; For records. Copied from the distribution matrix or the user; UNKNOWN where neither states one.

## Flag codes

| Code | Fires when | Evidence to record | Question for document control |
|------|------------|--------------------|-------------------------------|
| NUM-FORMAT | The number does not match the convention provided | Quoted number, expected pattern | Correct the number, or confirm the exception? |
| NUM-DUP | Two lines carry the same number and revision | Both item references | Remove one line? |
| REV-MISSING | Revision or revision date is blank | Field names blank | Supply the revision and date? |
| REV-NOT-LATER | Revision is the same as or earlier than the last one sent to this recipient | Both revisions, the earlier transmittal reference | Re-issue intended? |
| REV-FUTURE | Revision date is after the transmittal date | Both dates | Correct the date? |
| POI-CONFLICT | List status and requested purpose disagree | Both values quoted | Which purpose applies? |
| POI-MIXED | Several purpose codes where the procedure requires one per transmittal | Codes found | Split into one transmittal per purpose? |
| STATUS-HOLD | Status reads hold, superseded, void, cancelled or withdrawn | Status quoted | Include or remove? |
| DIST-UNKNOWN | Recipient absent from the matrix, or action required not stated | Recipient, matrix reference | Confirm distribution and action required? |
| FILE-REV | File name carries a revision different from the list | File name, list revision | Which revision is current? |
| CONF-MARK | A confidentiality or export marking is present | Marking quoted, document number | Does the marking permit this distribution? |

Several codes may apply to one line. List them all, in the order above.

## Batch rule

Over about 100 lines, draft by discipline or document type in the order the user sets. Each batch states the lines it covers and is offered as the same transmittal continued; a separate transmittal is produced only when the user says so.

## Options offered on every question

Include (keep the line as drafted), Remove (drop the line; the user removes it), Correct (the user supplies the corrected value), Confirm (document control confirms the value as stated). The agent applies none of these; it redrafts on request after the decision.

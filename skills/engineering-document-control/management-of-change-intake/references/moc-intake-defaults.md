# Management of change intake: defaults

Used only where the project procedure or form does not provide the item. The project's own field names, consultation matrix, criteria, question lists and codes prevail over everything here. Every list below is a prompt for questions the agent asks; none of it is an assessment, a classification or a decision.

## Default change summary fields

Title | Originator role | Date received | Unit or area | System | Temporary or permanent (until when) | Requested date | Reason as stated (quoted) | Already implemented (as stated or UNKNOWN) | Record number (UNKNOWN until assigned).

## Document types by identifier type

Used without a register, as questions of the form "does a <document type> show <identifier>?" with document number UNKNOWN. Never as a statement that a document is or is not affected.

| Identifier type | Document types to ask about |
|---|---|
| Equipment tag | equipment list, datasheet, piping and instrumentation diagram, plot plan or layout, mechanical or vendor drawings, maintenance procedures |
| Line number | line list, piping and instrumentation diagram, isometrics, stress and support records, piping material specification |
| Instrument tag | instrument index, loop drawings, cause and effect matrix, alarm and trip list, control narrative, hook-up drawings |
| Cable or circuit number | cable schedule, single line diagram, termination drawings, load list, protection settings record |
| Setpoint or software reference | alarm and trip setpoint list, control narrative, logic diagrams, configuration and version records |
| Area or system | hazardous area classification drawing, layout, system boundary drawings, operating procedures, training material |
| Document number | the document itself and every register row that cites it as a reference |

## Default disciplines by identifier type

Equipment tag: mechanical, process, piping, maintenance, operations. Line number: piping, process, materials, stress, operations. Instrument tag or setpoint: instrumentation and control, process, operations. Cable or circuit: electrical, instrumentation and control. Area or system: layout, safety engineering, operations. Always proposed: document control. Each discipline is listed with its reason and with Status Proposed; the coordinator sets the review list.

## Default reviewer question groups

Each question is addressed to a named reviewer role and left blank for that reviewer to answer. The agent answers none of them.

- Scope: temporary or permanent, and until when; already implemented; other changes bundled in the same description; which parties or packages are interfaced.
- Design basis: within the documented design basis and operating envelope; materials, ratings, pressure or temperature limits, or classification of any item altered.
- Protective functions: any protective, relief, isolation, control, alarm, fire and gas or shutdown function altered, added or removed (the question only; the reviewer assesses).
- Documents: which drawings, models, lists, datasheets, procedures and training material would need revision, and which register rows.
- Operations and maintenance: operating or maintenance procedures, spares, inspection plans, permits or isolations that would follow (the question only; never the decision to issue any permit or isolation).
- Records: which approvals, tests or inspections the procedure requires before and after implementation, as the procedure lists them.

## Flag codes

| Code | Meaning | Question raised |
|---|---|---|
| BUNDLED | Several independent changes in one description | Split into one record each? |
| IMPLEMENTED | Description says the change is already done | Record as retrospective change? |
| ID-UNMATCHED | Identifier found in no register row | Correct identifier, or document not registered? |
| DOC-TYPE-ONLY | No register; document listed by type only | Which document number covers this identifier? |
| REASON-MISSING | No reason stated | Originator role to state the reason |
| DATE-MISSING | No requested date | Originator role to state the date |
| TEMP-UNKNOWN | Temporary or permanent not stated | Originator role to state which, and until when |
| LOG-RELATED | Log entry shares an identifier | Related, duplicate or independent? |
| ESCALATE-PER-PROCEDURE | Procedure names an escalation route for the item type | Route reproduced as a proposal; the coordinator decides |

## Wording rules for this record

- Every cell is "as stated" with its source, or UNKNOWN.
- The words minor, major, like for like, replacement in kind, no impact, no safety impact, acceptable and approved appear only inside quoted source text, reproduced criteria, blank decision cells, or the fixed first-line and closing-report statements that deny them.
- Nothing in the record authorises implementation, operation, any permit, isolation or work.

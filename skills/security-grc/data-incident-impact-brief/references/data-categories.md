# Data categories, attention items, vocabulary, figure basis and notification question bank

Defaults for the data incident impact brief. The organisation's own classification replaces the default category list when supplied. Attention items are factors for legal and the data protection officer to weigh; listing one is never a conclusion about breach status, harm or notification.

## Involvement vocabulary (systems table)

Use one of these words per system, exactly as the notes support it: accessed, exfiltrated, encrypted, altered, deleted, misdirected, lost, exposed, UNKNOWN. "Suspected" or "possibly" in the notes keeps the word and adds "(suspected, per <source>)". Never upgrade a suspicion to a fact or downgrade a stated fact to a suspicion.

## Data state items (data state table)

Record each as stated with its source, or UNKNOWN: encryption at rest; encryption in transit; key or secret compromise; pseudonymisation or tokenisation; backups affected; data recovered; data confirmed deleted by the recipient or attacker; credentials reset. None of these items lowers a figure or changes a basis; they are facts for legal to weigh.

## Default category list

| Category | Typical fields | Attention item |
|---|---|---|
| Identity data | Name, date of birth, gender, nationality | No, unless combined with a government identifier |
| Government or regulated identifiers | National identity number, passport, driving licence, tax or social insurance number | Yes |
| Contact data | Postal address, email, telephone | No |
| Authentication credentials | Passwords or hashes, tokens, API keys, session cookies, multi-factor seeds, recovery answers | Yes |
| Financial data | Bank account, payment card, payroll, credit standing, transaction history | Yes |
| Health data | Diagnoses, treatment, sick notes, occupational health, insurance claims | Yes |
| Special categories | Racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data, sex life or sexual orientation | Yes |
| Criminal records | Convictions, offences, allegations, investigations | Yes |
| Children's data | Any category concerning a person the inventory marks as a minor | Yes |
| Location and tracking | Precise location, travel history, vehicle telematics, badge access logs | Yes where precise or continuous |
| Behavioural and usage | Web analytics, preferences, product usage, purchase history | No |
| Employment and HR | Job history, salary, appraisals, disciplinary and grievance records, absence | Yes for disciplinary, grievance, medical or salary |
| Communications content | Message bodies, call recordings, voicemail, chat transcripts | Yes |
| Images and recordings | Photographs, video, CCTV, voice | Yes where individuals are identifiable |
| Business confidential (not personal) | Contracts, pricing, source code, designs, credentials to systems holding no personal data | Not a personal data factor; flag for legal and commercial owners |

## Category basis

| Basis | Condition | Cell content |
|---|---|---|
| Evidenced | The notes show the category was involved (a log line, a query result, a file name, a screenshot description) | Quote and source |
| Held | The inventory lists the category for the system; the notes neither confirm nor exclude involvement | "held per inventory; involvement UNKNOWN" |
| Excluded as stated | The notes state the category was not involved | Quote and source |

Held is never promoted to Evidenced by likelihood or by the nature of the incident. A category the notes mention for a system the inventory does not list is Evidenced with inventory match "Not in inventory".

## Figure basis

| Basis | Condition | Cell content |
|---|---|---|
| Evidenced | The figure comes from a log, export or query run on the set the incident touched | Source, query or log named, time run |
| Ceiling | The figure is the size of the whole table, system, mailbox or population, not the touched set | "ceiling: whole <object>" |
| UNKNOWN | No figure in the sources | Evidence to gather named in the UNKNOWN list |

A total across systems is shown only as "upper bound, may double count: <a> + <b> = <c>". Where the sources state the populations are distinct, it reads "distinct populations per <source>: <a> + <b> = <c>" instead. Individuals and records are never summed together. An estimate is recorded as an estimate with the person who made it (role only) and the basis they stated.

## Notification question bank

Use only the questions a stated fact raises. Every question names the fact, its source and the document legal would check. None of them is answered in the brief.

Regime and role
- Which legal regimes apply to the data subject groups and residencies stated in section 6, and in which is the organisation controller or processor for <system>, per <inventory reference>?
- For <third party>, listed as processor in <inventory reference>, which contract sets the processor-to-controller notice duty, and what does it say?

Threshold
- Does the involvement stated for <category> on <system> (<quote, source>) meet the threshold for regulator notification under each regime identified?
- Does the data state recorded in section 7 (<encryption or key status as stated>) bear on that threshold under each regime?

Regulator and individuals
- Which authority or authorities receive notice for the residencies stated, and in what form?
- Do the attention items in section 5 bear on whether individuals must be informed, and which groups?
- From the awareness time as stated (<time, zone, source>), what window does each regime set? Where legal has supplied a window: elapsed time <arithmetic>.

Contractual, insurance and other parties
- Do the customer, partner or vendor contracts for <system> carry incident notice clauses, and what timing do they state? (Quote any clause the user supplied.)
- Does the cyber or liability insurance policy set a notice duty or a deadline, and does the stated incident type fall within it?
- Do the facts as stated call for a report to law enforcement, a sector regulator or a listing authority, and who decides?

Processor chain and cross-border
- Which subprocessors named in the Third parties table hold the same data, and has each confirmed its own status?
- Does the hosting location stated for <system> place the data or the incident under an additional regime?

Documentation
- Which record of the incident does each regime require the organisation to keep regardless of notification, and who owns it?

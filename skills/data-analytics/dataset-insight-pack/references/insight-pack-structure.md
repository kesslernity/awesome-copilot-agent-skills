# Insight pack: structure and rules

The structure for the DRAFT insight pack. It accelerates an analyst's first read; it is never the source of truth.

## Document structure

1. **Title and DRAFT line.** Title `DRAFT-insight-pack-<Dataset>-<YYYY-MM-DD>-v<n>`. First line: "DRAFT insight pack for <dataset>, generated <date>. Exploration only; figures are unverified and observations are leads, not conclusions. The analyst must verify in the data platform."
2. **Profile.** Row count as read, columns with apparent types, missing or blank per key column, duplicates, value ranges for numeric and date fields, category lists for low-cardinality text fields only (at most the ten most frequent values plus a count of the rest). Identifier-like, free-text, high-cardinality or possibly personal columns (names, emails, identifiers, health, pay) get a distinct count only, never the values. Label every count "as read, verify in source". Unreadable values are UNKNOWN.
3. **Observations (leads).** Each cites the column(s) and values it rests on and is phrased as a lead.
4. **Caveats.** Completeness, sample size, correlation not causation, ambiguities, assumptions about headers or units.
5. **Suggested next steps and charts.** Follow-up analyses and chart ideas, each naming its axes or series, for the analyst to build in the owning platform.
6. **Closing statement.** Rows and columns read, complete or partial, any fallback used, verification reminder.

## Table layouts (required)

Use these column headings, in this order, for the three tables in the pack.

- Profile: Column | Apparent type | Missing (as read) | Distinct count, top values (ten at most) or range (as read) | Note
- Observations: Number | Lead | Columns and values cited | What would confirm it
- Suggested charts: Chart | X axis | Y axis or series | Question it answers

## How to phrase an observation

- Good (lead): "Average [value] in [segment A] appears about 30% higher than in [segment B] (columns: region, value), worth confirming and investigating why."
- Bad (conclusion or cause): "Segment A outperforms because of better service." This asserts a cause.
- Bad (authoritative): "Total revenue is 4.2 million." Write instead: "Sum of [amount] as read is about 4.2 million, verify in source."

## Never include

- A cause for an observed pattern. Correlation is not causation.
- A business decision or recommendation as the answer. Offer next questions or options instead.
- A data quality verdict or an official metric value.
- Quoted individual records that look like personal or sensitive data. Flag for privacy review instead.
- A claim that the pack was saved, sent or filed. The agent returns text; the user performs any storage or distribution.

Every figure in the pack is a draft to verify. The number that ships comes from a reproducible query in the owning platform, not from this pack.

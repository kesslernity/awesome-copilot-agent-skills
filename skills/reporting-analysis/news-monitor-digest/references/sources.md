# Sources and relevance criteria

Configuration for the news-monitor-digest skill. Supply it in one of three ways: paste an edited copy into the conversation with your request, attach it, or keep it as a file named sources.md among the agent's configured knowledge sources. The skill reads the highest-precedence copy fresh on every run. Keep the four parts below: the Role line, the Relevance criteria list, the Sources table and the Exclusions. The worked example is a complete, usable configuration once you fill in the addresses; replace its role and sources with your own.

## How to edit

- **Role:** one line describing the job the digest serves. Every so-what line in the digest is written against this role.
- **Relevance criteria:** 4 to 7 bullet points. An item must match at least one to be considered, and items matching more criteria rank higher.
- **Sources table:** one row per source. Put the site's top-level news or blog address in the Address column. 6 to 15 sources is the practical range; past that, tighten the criteria instead of adding rows. The skill sweeps at most 24 sources per run and lists the rest as not individually checked.
- **Exclusions:** things the digest must never include, even from listed sources.

## Run log

The skill deduplicates against a file named news-monitor-log.md that you keep alongside this one (pasted, attached or in the agent's knowledge sources). On the first run, create it with this header row:

| Run date | Window covered | Item count | URLs included |
|---|---|---|---|

After each run the skill returns one new line in this format for you to append. Append the line yourself; never rewrite or delete earlier lines. If the skill cannot read the log, it says "deduplication skipped this run" inside the digest.

---

## Worked example: cloud productivity suite administrator

**Role:** IT administrator responsible for the organisation's cloud productivity suite tenant, including AI assistant licensing, tenant settings and rollout communications.

### Relevance criteria

An item qualifies if it involves at least one of:

- Licensing or pricing changes for the suite, its AI assistant or related add-ons
- A feature reaching general availability or public preview that changes tenant settings or admin centre options
- Security, compliance or data-residency changes affecting tenant configuration
- A deprecation, retirement or enforced migration with a date
- An admin action required before a deadline
- Agent governance, identity or management capabilities (assistant agents, autonomous agents)

### Sources

| Source | Address | What to look for |
|---|---|---|
| Vendor product blog | (enter the top-level address) | Product announcements, licensing news |
| Vendor corporate blog | (enter the top-level address) | Strategy and major launches |
| Vendor technical community | (enter the top-level address) | Admin-level feature posts, general availability and preview notices |
| Vendor public roadmap | (enter the top-level address) | Dated rollout entries matching the criteria |
| Vendor documentation, what's new pages | (enter the top-level address) | Documentation changes that signal shipped behaviour |
| Independent technology news site, vendor section | (enter the top-level address) | Independent coverage and context on vendor news |
| Specialist news site covering the vendor | (enter the top-level address) | Early reporting on suite and assistant changes |

### Exclusions

- Rumours and unconfirmed leaks, unless explicitly labelled "(unverified)" and clearly consequential
- Sponsored content and press-release rewrites with no admin-relevant detail
- Consumer-only features with no tenant or licensing impact
- Anything without a publication date on the page

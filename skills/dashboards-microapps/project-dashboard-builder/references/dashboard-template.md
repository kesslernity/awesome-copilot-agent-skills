# Dashboard HTML template

Use this skeleton for every dashboard. Rules:

- Replace every `{{PLACEHOLDER}}`. None may remain in the delivered source.
- `{{STATUS_CLASS}}` is exactly one of: `green`, `amber`, `red`. The same value drives the banner and the page accent.
- `{{AS_OF_DATE}}` is the reporting period or as-of date (Inputs item 3 in SKILL.md), used in the title and subtitle. `{{GENERATED_DATE}}` is today's date, used in the footer. They differ whenever the user names a period other than today.
- Repeat the blocks marked `REPEAT` once per item, then delete the marker comments. Delete the whole example row, never leave sample data in the output.
- The two count lines (the `<p class="count">` after the Risks blocks and the one after the Decisions table) are filled only when that section is truncated to 10; otherwise delete the whole `<p class="count">` element.
- Severity classes on risk items are exactly one of `sev-high`, `sev-medium`, `sev-low`, or none for Unrated. An Unrated item is `<div class="risk">` (no severity class, so it keeps the base grey border) with `<span class="sev unrated">Unrated</span>`.
- `{{STATE_OR_UNKNOWN}}` is one of Done, Not started, On track, At risk, Late, the tracker's own wording when it maps to none of these, or UNKNOWN when no state is recorded.
- If a section has no data, keep the section heading and replace the list or table body with a single line: `<p class="nodata">No data in tracker</p>` (or `No data provided` in pasted-summary mode).
- Add nothing to `<head>` beyond what is shown. No `<script>`, `<link>`, `<img>`, `<iframe>` or `<object>` tags anywhere. No `@import` or `url(` in the style block. No `src` or `href` pointing outside the file, except the user-supplied links rendered in the links section.
- Keep the DRAFT ribbon and the footer sentence "Not yet reviewed." until the user reviews and confirms the content (see Rules in SKILL.md). In the -final version remove the ribbon `<span class="draft">` and replace "Not yet reviewed." with "Content confirmed by the user on YYYY-MM-DD." using the date of the typed confirmation.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{PROJECT_TITLE}} dashboard {{AS_OF_DATE}}</title>
<style>
  body { margin: 0; background: #f3f2f1; color: #201f1e;
         font-family: system-ui, Arial, Helvetica, sans-serif; line-height: 1.5; }
  .wrap { max-width: 920px; margin: 0 auto; padding: 24px 20px 48px; }
  h1 { font-size: 1.6rem; margin: 0 0 4px; }
  h2 { font-size: 1.1rem; margin: 32px 0 12px; border-bottom: 2px solid #e1dfdd;
       padding-bottom: 6px; text-transform: uppercase; letter-spacing: 0.04em; }
  .subtitle { color: #605e5c; margin: 0 0 20px; }
  .banner { border-radius: 8px; padding: 18px 22px; color: #ffffff; }
  .banner.green { background: #0b6a0b; }
  .banner.amber { background: #8a5a00; }
  .banner.red { background: #a4262c; }
  .banner .label { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em;
                   opacity: 0.9; }
  .banner .headline { font-size: 1.2rem; font-weight: 600; margin: 4px 0 8px; }
  .banner p { margin: 0; }
  table { width: 100%; border-collapse: collapse; font-size: 0.95rem; }
  th { text-align: left; background: #edebe9; padding: 8px 10px; }
  td { padding: 8px 10px; border-bottom: 1px solid #e1dfdd; vertical-align: top; }
  .risk { border-left: 6px solid #c8c6c4; background: #ffffff; border-radius: 4px;
          padding: 10px 14px; margin: 0 0 8px; }
  .risk.sev-high { border-left-color: #a4262c; }
  .risk.sev-medium { border-left-color: #8a5a00; }
  .risk.sev-low { border-left-color: #0b6a0b; }
  .risk .sev { font-size: 0.75rem; font-weight: 700; text-transform: uppercase;
               letter-spacing: 0.06em; }
  .risk.sev-high .sev { color: #a4262c; }
  .risk.sev-medium .sev { color: #8a5a00; }
  .risk.sev-low .sev { color: #0b6a0b; }
  .risk .sev.unrated { color: #605e5c; }
  ul.links { padding-left: 20px; }
  ul.links li { margin-bottom: 6px; }
  .nodata { color: #605e5c; font-style: italic; }
  .count { color: #605e5c; font-size: 0.85rem; }
  footer { margin-top: 40px; border-top: 1px solid #e1dfdd; padding-top: 12px;
           font-size: 0.8rem; color: #605e5c; }
  .draft { display: inline-block; background: #fde7e9; color: #a4262c; font-weight: 700;
           padding: 2px 10px; border-radius: 4px; letter-spacing: 0.06em; }
</style>
</head>
<body>
<div class="wrap">

  <h1>{{PROJECT_TITLE}}</h1>
  <p class="subtitle">{{AUDIENCE_LINE_OR_AS_OF_DATE}}</p>

  <div class="banner {{STATUS_CLASS}}">
    <div class="label">Overall status: {{STATUS_WORD}}</div>
    <div class="headline">{{STATUS_HEADLINE}}</div>
    <p>{{STATUS_SUMMARY_2_TO_3_SENTENCES}}</p>
  </div>

  <h2>Milestones</h2>
  <table>
    <tr><th>Milestone</th><th>Due</th><th>Owner</th><th>State</th></tr>
    <!-- REPEAT one row per milestone -->
    <tr><td>{{MILESTONE_NAME}}</td><td>{{DUE_DATE_OR_UNKNOWN}}</td><td>{{OWNER_OR_UNKNOWN}}</td><td>{{STATE_OR_UNKNOWN}}</td></tr>
    <!-- END REPEAT -->
  </table>

  <h2>Risks</h2>
  <!-- REPEAT one block per risk, High first, max 10. For Unrated: class="risk" only, and class="sev unrated" on the span -->
  <div class="risk {{SEVERITY_CLASS_OR_NONE}}">
    <span class="sev">{{SEVERITY_WORD}}</span>
    <div>{{RISK_DESCRIPTION}}</div>
    <div class="count">Mitigation: {{MITIGATION_OR_NONE_RECORDED}}</div>
  </div>
  <!-- END REPEAT -->
  <p class="count">{{SHOWING_X_OF_Y_RISKS_LINE_IF_TRUNCATED_ELSE_DELETE}}</p>

  <h2>Decisions</h2>
  <table>
    <tr><th>Date</th><th>Decision</th><th>Owner</th></tr>
    <!-- REPEAT one row per decision, newest first, max 10 -->
    <tr><td>{{DECISION_DATE_OR_UNDATED}}</td><td>{{DECISION_TEXT}}</td><td>{{DECISION_OWNER_OR_UNKNOWN}}</td></tr>
    <!-- END REPEAT -->
  </table>
  <p class="count">{{SHOWING_X_OF_Y_DECISIONS_LINE_IF_TRUNCATED_ELSE_DELETE}}</p>

  <h2>Links</h2>
  <ul class="links">
    <!-- REPEAT one item per link from links.md -->
    <li><a href="{{URL}}">{{LINK_LABEL}}</a></li>
    <!-- END REPEAT -->
  </ul>

  <footer>
    <span class="draft">DRAFT</span>
    Generated {{GENERATED_DATE}} from {{SOURCE_DESCRIPTION}}. Not yet reviewed.
  </footer>

</div>
</body>
</html>
```

`{{SOURCE_DESCRIPTION}}` is either `the {{PROJECT}} tracker files` or `a summary supplied in conversation` (pasted-summary mode).

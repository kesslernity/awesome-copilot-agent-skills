# Backup manifest template

Return this content in the chat as a Markdown document titled `backup-manifest.md`, filled in with real values taken from the listings, for the user to save inside the dated backup folder:

```markdown
# Backup manifest

- **Created:** YYYY-MM-DD HH:MM (user's timezone)
- **Source:** <skills folder path exactly as the user gave it>
- **Backup folder:** <backup folder path>/YYYY-MM-DD/
- **Skill folders copied:** N
- **Files copied:** N
- **Verification:** unverified (counts from the source listing) | verified against the backup folder listing pasted YYYY-MM-DD HH:MM
- **Skipped:** none

## Contents

| Skill folder | Files | Notes |
|---|---|---|
| skill-name-1 | 3 | SKILL.md plus 2 references files |
| skill-name-2 | 1 | SKILL.md only |
```

Rules:

- Counts come from the source listing. They become verified only when the user pastes the listing of the backup folder after copying and the counts match. A mismatch is reported line by line, never smoothed over.
- If anything was skipped (over a size limit, unreadable, not in the listing), replace `none` with one line per skipped item and the reason.
- One table row per skill folder. The Files column counts every file in that folder, including references.
- Anything not visible in a listing is UNKNOWN, never estimated.
- Created time and timezone come from the user or the conversation. If either is not established, ask, or write UNKNOWN.

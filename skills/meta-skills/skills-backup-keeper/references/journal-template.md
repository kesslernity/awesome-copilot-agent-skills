# Session journal template

When no journal exists yet, return this header once, for the user to save as `session-journal.md` in the backup folder (not in the skills folder, so a wipe cannot take it too):

```markdown
# Session journal

Append-only record maintained with the skills-backup-keeper skill.
Newest entry at the bottom. Never edit or delete earlier entries.
```

Return one entry per session or checkpoint, exactly in this shape, for the user to append at the bottom:

```markdown
---

## Session: YYYY-MM-DD HH:MM (user's timezone)

**Goal:** One sentence describing what this session set out to do.

**Files touched:**
- <skills folder>/<skill-name>/SKILL.md (created | edited | read | proposed)
- <other full path> (created | edited | read | proposed)

**Decisions:**
- Decision made and the reason, one line each.

**Next steps:**
- [ ] First open action, specific enough to act on in a fresh conversation
- [ ] Second open action
```

Rules for entries:

- Every file path is a full path exactly as the user gave it. No bare filenames.
- Files touched records what the user reported doing. An action the agent only proposed is recorded as proposed, never as done; proposed means the agent returned the action and the user has not confirmed performing it.
- Decisions record the why, not just the what, in one line each.
- Next steps must be executable by someone with no memory of this conversation.
- Keep each entry under 25 lines. Detail belongs in the files themselves.
- Anything the conversation did not establish is UNKNOWN, never guessed.

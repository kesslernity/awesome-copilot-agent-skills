# Restore checklist

Follow these steps in order when preparing a restore. Do not skip the holds. The agent plans and verifies; the user performs each copy and pastes the listings back.

1. List available backups. From the backup folder listing the user attached, pasted or made reachable, enumerate the dated folders. Sort by date, then by -N suffix (2026-06-10-2 is newer than 2026-06-10).
2. Propose one backup. Default to the most recent. Read its `backup-manifest.md` (attached, pasted or reachable) and tell the user the created timestamp, skill count and file count. Hold for confirmation of the choice. If the manifest is not reachable, its counts are UNKNOWN and verification in step 6 will be limited to the folder list.
3. Check the target. From the current skills folder listing, record which skill folders already exist there.
4. Approval hold. If any existing folder would be replaced by the restore, list every collision by name and hold for typed approval naming them. Without approval, plan only the non-colliding folders and say which were left alone. The approval releases the hold. It is not an authorisation; the user performs the copies.
5. Return the copy list as a table with columns #, Source (full path), Destination (full path), Files (count), Note; one row per approved skill folder, source in the dated backup to destination in the skills folder, structure preserved (SKILL.md plus any references files). Never propose deleting the existing folder first; the copy replaces its files only where the user approved.
6. Verify. Ask the user to paste the skills folder listing after copying. Compare folder and file counts against the manifest. Report any mismatch instead of declaring success. If no listing is pasted, the result is UNKNOWN and is reported as such.
7. Journal it. Return a session-journal entry: which backup was restored, what was copied, any collisions and how they were resolved.
8. Remind about re-upload. Restored skill files take effect only once the user re-uploads them to the agent's configuration.

# Source Details — claude-for-legal--claude-liam-auto-updater

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Auto Updater.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-auto-updater/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-builder-hub/skills/auto-updater/SKILL.md
- Name: auto-updater
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Fail-closed on regression. If the new version produces findings where
- Security-surface diffs require human approval regardless of verdict.
- Read-only scan context. The scan reads attacker-controlled text (the
- Refuse an update whose scan now fails. If the new version hits a
- argument-hint: "[--apply to update all, otherwise notify only]"
- Community skills improve. This skill notices when, shows you what changed, and applies updates only with your explicit approval
- Fetch the current commit SHA from the source registry (the exact commit, not a tag or branch head — tags are mutable and can be retroactively rewritten by the publisher…
- frontmatter FORCES a human-approval prompt and cannot be bypassed by a

## Procedure / Sequence
- Check each installed skill: For each skill in the installed list: - Fetch the current commit SHA from the source registry (the exact commit, not a…
- Diff and trust review: For each update, show the full diff: `diff # [skill-name] — [installed SHA] → [latest SHA]
- 5: Re-scan the new version (GlassWorm gate): Re-run the full skills-qa scan against the NEW version before applying the update. A skill that was clean at v1.0 can…
- 6: Freshness-triggered re-verification: Don't only check for new commits. Also check whether installed skills have passed their freshness window. For each…
- Handle per preference: Notify (default): Show the full diff and trust check. "Update available. Review the diff above. Apply? [y/n]" Manual…
- Apply (after explicit approval): Replace the installed skill files with the new version. Update…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/legal-builder-hub/CLAUDE.md
- Referenced: hooks/hooks.json
- Referenced: .mcp.json
- Referenced: allowed-tools
- Referenced: skills-qa
- Referenced: --rollback
- Referenced: last_verified
- Referenced: freshness_window
- Referenced: freshness_category
- Referenced: min(freshness_window, user's threshold for freshness_category)
- Signal: code block: diff

## Source Sections
- Purpose
- Trust posture
- Load context
- Workflow
- Step 1: Check each installed skill
- Step 2: Diff and trust review
- SKILL.md changes
- hooks/hooks.json changes
- .mcp.json changes
- Other files

## Batch Log Match
- Row: 104
- Canonical path: anthropics/claude-for-legal/legal-builder-hub/skills/auto-updater/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-auto-updater/mp4/claude-liam-auto-updater.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

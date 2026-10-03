# Source Details — claude-for-legal--claude-liam-gap-surfacer

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Gap Surfacer.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-gap-surfacer/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/regulatory-legal/skills/gap-surfacer/SKILL.md
- Name: gap-surfacer
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Never send without the confirm. Not on a cadence. Not in a batch. Not because it was sent yesterday
- Matter context. Check ## Matter workspaces in the practice-level CLAUDE.md. If Enabled is ✗ (the default for in-house users), skip the rest of this paragraph — skills…
- status_verified: true # false if upstream policy-diff could not confirm the rule is in force; unverified items never hit 🔴 Overdue
- Never classify a gap as Overdue on an unverified rule. The 🔴 Overdue classification means "we missed a binding deadline." If the rule's status is unverified (policy-diff…
- | none | Policy already covers the requirement. Logged for audit trail only. Should be rare — if most entries are none, the diff is probably running against the wrong…
- Send a Slack DM to the gap owner — but only after the per-send confirmation at the top of this file. Preview the message to the user, wait for an explicit yes, then send:
- only real compliance deadlines.]
- Verify citations before relying on them. Regulation citations in this tracker were AI-generated upstream (by reg-feed-watcher and policy-diff) and have not been checked…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: owner_slack
- Referenced: /regulatory-legal:matter-workspace switch <slug>
- Referenced: practice-level
- Referenced: matter.md
- Referenced: . Never read another matter's files unless
- Referenced: ~/.claude/plugins/config/claude-for-legal/regulatory-legal/gap-tracker.yaml
- Referenced: ~/.claude/plugins/config/claude-for-legal/regulatory-legal/comment-tracker.yaml
- Referenced: status_verified: false
- Referenced: gap_type
- Referenced: new-policy
- Signal: code block: yaml
- Signal: code block: markdown

## Source Sections
- Per-send confirmation — no exceptions
- Matter context
- Purpose
- The tracker
- Modes
- Mode 1: Ingest from policy-diff
- Mode 2: Status report
- Open Gaps — [date]
- Bottom line
- 🔴 Overdue

## Batch Log Match
- Row: 251
- Canonical path: anthropics/claude-for-legal/regulatory-legal/skills/gap-surfacer/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-gap-surfacer/mp4/claude-liam-gap-surfacer.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

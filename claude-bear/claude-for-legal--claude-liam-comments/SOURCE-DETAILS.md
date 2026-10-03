# Source Details — claude-for-legal--claude-liam-comments

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Comments.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-comments/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/regulatory-legal/skills/comments/SKILL.md
- Name: comments
- Description: Review open NPRM comment periods, log decisions, track deadlines. Use when an NPRM has a comment window open and you need to surface deadlines, decide whether to file, or record a filing / not-filing / waived decision (--decide CMT-ID).

## Capabilities To Name On Screen
- Review open NPRM comment periods
- log decisions
- track deadlines
- Use when an NPRM has a comment window open and you need to surface deadlines
- decide whether to file

## Constraints / Failure Modes
- Do not log a "filing" decision or produce a submission-ready draft past this gate without an explicit yes. Tracking views, deadline reminders, and "not-filing / waived"…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/regulatory-legal/comment-tracker.yaml
- Referenced: ~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md
- Referenced: owner_slack
- Referenced: /regulatory-legal:reg-feed-watcher
- Referenced: comment-decision
- Referenced: gap_type
- Signal: code block: markdown

## Source Sections
- Purpose
- Load context
- Default view — open comment periods
- Comment Period Tracker — [date]
- ⏰ Deadline in <14 days
- 🟡 Open (>14 days)
- Recently decided
- Log a decision
- Notifications
- Consequential-action gate (submit a regulatory comment / respond to a regulator)

## Batch Log Match
- Row: 158
- Canonical path: anthropics/claude-for-legal/regulatory-legal/skills/comments/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-comments/mp4/claude-liam-comments.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

# Source Details — claude-agent-sdk-demos--claude-liam-listener-creator

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Listener Creator.
- Family: claude-agent-sdk-demos
- Source sheet: /Users/nik/Documents/books/anthropics/claude-agent-sdk-demos/youtube/claude-liam-listener-creator/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-agent-sdk-demos/email-agent/agent/.claude/skills/listener-creator/SKILL.md
- Name: listener-creator
- Description: Creates event-driven email listeners that monitor for specific conditions (like urgent emails from boss, newsletters to archive, package tracking) and execute custom actions. Use when user wants to be notified about emails, automatically handle certain emails, or set up email automation workflows.

## Capabilities To Name On Screen
- Creates event-driven email listeners that monitor for specific conditions (like urgent emails from boss
- newsletters to archive
- package tracking) and execute custom actions
- Use when user wants to be notified about emails
- automatically handle certain emails

## Constraints / Failure Modes
- // 1. Basic filter (identity/sender only)
- required: ["isUrgent", "reason"]
- required: ["field"]
- Notify Wisely: Only notify when truly important
- Basic filter (sender only) → Notify → Optional star/label
- Only use this when: The trigger is purely identity-based (e.g., "notify me about ALL emails from X")

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: agent/custom_scripts/listeners/
- Referenced: Urgent email: ${email.subject}\n${analysis.reason}
- Referenced: boss-urgent-watcher.ts
- Referenced: auto-archive-newsletters.ts
- Referenced: package-tracking.ts
- Referenced: daily-summary.ts
- Referenced: context.callAgent()
- Referenced: Urgent: ${email.subject}\n${analysis.reason}
- Referenced: email_received
- Referenced: [listener:filename.ts]
- Signal: code block: typescript
- Signal: code block: markdown

## Source Sections
- When to Use This Skill
- How Listeners Work
- Creating a Listener
- 1. Understand the User's Intent
- 2. Choose an Event Type
- 3. Write the Listener File
- 4. File Naming Convention
- 5. Available Context Methods
- Recommended Approach: AI-Powered Classification
- Examples and Templates

## Batch Log Match
- Row: 82
- Canonical path: anthropics/claude-agent-sdk-demos/email-agent/agent/.claude/skills/listener-creator/SKILL.md
- MP4 path: anthropics/claude-agent-sdk-demos/youtube/claude-liam-listener-creator/mp4/claude-liam-listener-creator.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

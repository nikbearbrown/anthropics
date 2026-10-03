# Source Details — claude-agent-sdk-demos--claude-liam-action-creator

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Action Creator.
- Family: claude-agent-sdk-demos
- Source sheet: /Users/nik/Documents/books/anthropics/claude-agent-sdk-demos/youtube/claude-liam-action-creator/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-agent-sdk-demos/email-agent/agent/.claude/skills/action-creator/SKILL.md
- Name: action-creator
- Description: Creates user-specific one-click action templates that execute email operations when clicked in the chat interface. Use when user wants reusable actions for their specific workflows (send payment reminder to ACME Corp, forward bugs to engineering, archive old newsletters from specific sources).

## Capabilities To Name On Screen
- Creates user-specific one-click action templates that execute email operations when clicked in the chat interface
- Use when user wants reusable actions for their specific workflows (send payment reminder to ACME Corp
- forward bugs to engineering
- archive old newsletters from specific sources).

## Constraints / Failure Modes
- required: ["paramName"] // List required parameters
- success: true, // Required: boolean
- message: "Human-readable result", // Required: string
- required: ["emailId", "priority"] // List required params
- Parameter schema with all required fields
- Test parameters: Ensure all required parameters are defined

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: agent/custom_scripts/actions/
- Referenced: Starting action: ${config.name}
- Referenced: Action failed: ${error}
- Referenced: Failed: ${error.message}
- Referenced: send-payment-reminder-to-acme.ts
- Referenced: send-email.ts
- Referenced: forward-bugs-to-engineering.ts
- Referenced: forward-email.ts
- Referenced: archive-newsletters-from-techcrunch.ts
- Referenced: archive-emails.ts
- Signal: code block: typescript

## Source Sections
- When to Use This Skill
- How Actions Work
- Creating an Action Template
- 1. Understand User-Specific Workflow
- 2. Write the Action Template File
- 3. File Naming Convention
- 4. Available Context Methods
- Action Result
- Examples and Templates
- Best Practices

## Batch Log Match
- Row: 69
- Canonical path: anthropics/claude-agent-sdk-demos/email-agent/agent/.claude/skills/action-creator/SKILL.md
- MP4 path: anthropics/claude-agent-sdk-demos/youtube/claude-liam-action-creator/mp4/claude-liam-action-creator.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

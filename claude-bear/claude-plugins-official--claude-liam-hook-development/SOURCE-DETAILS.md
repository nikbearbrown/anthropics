# Source Details — claude-plugins-official--claude-liam-hook-development

Generated: 2026-09-05T11:09:00

## Reel
- Question: hook development
- Family: claude-plugins-official
- Source sheet: /Users/nik/Documents/books/anthropics/claude-plugins-official/youtube/claude-liam-hook-development/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-plugins-official/plugins/plugin-dev/skills/hook-development/SKILL.md
- Name: hook-development
- Description: This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API.

## Capabilities To Name On Screen
- Enable strict validation only when needed
- Temporary debugging hooks
- Project-specific hook behavior
- Feature flags for hooks
- Best practice:: Document activation mechanism in plugin README so users know how to enable/disable temporary hooks.

## Constraints / Failure Modes
- hooks field is required wrapper containing actual hook events
- $CLAUDE_ENV_FILE - SessionStart only: persist env vars here
- // Bash commands only
- # Only active when flag file exists
- Enable strict validation only when needed
- Cannot hot-swap hooks:
- Must restart Claude Code: exit and run claude again

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: hooks/hooks.json
- Referenced: .claude/settings.json
- Referenced: {"hooks": {...}}
- Referenced: $CLAUDE_ENV_FILE
- Referenced: examples/load-context.sh
- Referenced: tool_name
- Referenced: tool_input
- Referenced: tool_result
- Referenced: user_prompt
- Referenced: $TOOL_INPUT
- Signal: code block: json
- Signal: code block: bash

## Source Sections
- Overview
- Hook Types
- Prompt-Based Hooks (Recommended)
- Command Hooks
- Hook Configuration Formats
- Plugin hooks.json Format
- Settings Format (Direct)
- Hook Events
- PreToolUse
- PostToolUse

## Batch Log Match
- Row: 49
- Canonical path: anthropics/claude-plugins-official/plugins/plugin-dev/skills/hook-development/SKILL.md
- MP4 path: anthropics/claude-plugins-official/youtube/claude-liam-hook-development/claude-liam-hook-development.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

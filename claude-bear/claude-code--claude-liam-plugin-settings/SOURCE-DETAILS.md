# Source Details — claude-code--claude-liam-plugin-settings

Generated: 2026-09-05T11:09:00

## Reel
- Question: Plugin Settings
- Family: claude-code
- Source sheet: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code/youtube/claude-liam-plugin-settings/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code/plugins/plugin-dev/skills/plugin-settings/SKILL.md
- Name: Plugin Settings
- Description: This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content.

## Capabilities To Name On Screen
- This skill should be used when the user asks about "plugin settings"
- "store plugin configuration"
- "user-configurable plugin"
- ".local.md files"
- "plugin state files"

## Constraints / Failure Modes
- echo "⚠️ Invalid max_value in settings (must be 1-100)" >&
- Hooks cannot be hot-swapped within a session
- Readable by user only (chmod 600)

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: .claude/plugin-name.local.md
- Referenced: .gitignore
- Referenced: examples/read-settings-hook.sh
- Referenced: .claude/my-plugin.local.md
- Referenced: ---
- Referenced: .local.md
- Referenced: .claude/
- Referenced: .md
- Referenced: .local
- Referenced: enabled: true/false
- Signal: code block: markdown
- Signal: code block: bash
- Signal: code block: gitignore

## Source Sections
- Overview
- File Structure
- Basic Template
- Example: Plugin State File
- Reading Settings Files
- From Hooks (Bash Scripts)
- From Commands
- From Agents
- Parsing Techniques
- Extract Frontmatter

## Batch Log Match
- Row: 22
- Canonical path: anthropics/claude-code/plugins/plugin-dev/skills/plugin-settings/SKILL.md
- MP4 path: anthropics/claude-code/youtube/claude-liam-plugin-settings/claude-liam-plugin-settings.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

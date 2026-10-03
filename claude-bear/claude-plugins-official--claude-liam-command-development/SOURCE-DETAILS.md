# Source Details — claude-plugins-official--claude-liam-command-development

Generated: 2026-09-05T11:09:00

## Reel
- Question: Command Development
- Family: claude-plugins-official
- Source sheet: /Users/nik/Documents/books/anthropics/claude-plugins-official/youtube/claude-liam-command-development/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-plugins-official/plugins/plugin-dev/skills/command-development/SKILL.md
- Name: command-development
- Description: This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in commands, user interaction patterns, or command development best practices for Claude Code.

## Capabilities To Name On Screen
- Markdown file format for commands
- YAML frontmatter for configuration
- Dynamic arguments and file references
- Bash execution for context
- Command organization and namespacing
- haiku - Fast, simple commands
- sonnet - Standard workflows
- opus - Complex analysis

## Constraints / Failure Modes
- > Note: The .claude/commands/ directory is a legacy format. For new skills, use the .claude/skills/<name>/SKILL.md directory format. Both are loaded identically — the…
- Bash(git:*) - Bash with git commands only
- Use when: Command should only be manually invoked
- Validate arguments: Check for required arguments in prompt
- Files changed: !git diff --name-only
- Check for required permissions
- Agent must exist in plugin/agents/ directory
- Skill must exist in plugin/skills/ directory

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: .claude/commands/
- Referenced: .claude/skills/<name>/SKILL.md
- Referenced: skill-development
- Referenced: /command-name
- Referenced: /help
- Referenced: ~/.claude/commands/
- Referenced: plugin-name/commands/
- Referenced: .md
- Referenced: $1
- Referenced: $2
- Signal: code block: markdown
- Signal: code block: yaml

## Source Sections
- Overview
- Command Basics
- What is a Slash Command?
- Critical: Commands are Instructions FOR Claude
- Command Locations
- File Format
- Basic Structure
- With YAML Frontmatter
- YAML Frontmatter Fields
- description

## Batch Log Match
- Row: 37
- Canonical path: anthropics/claude-plugins-official/plugins/plugin-dev/skills/command-development/SKILL.md
- MP4 path: anthropics/claude-plugins-official/youtube/claude-liam-command-development/claude-liam-command-development.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

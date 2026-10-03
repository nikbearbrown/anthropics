# Source Details — claude-code--claude-liam-agent-development

Generated: 2026-09-05T11:09:00

## Reel
- Question: Agent Development
- Family: claude-code
- Source sheet: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code/youtube/claude-liam-agent-development/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code/plugins/plugin-dev/skills/agent-development/SKILL.md
- Name: Agent Development
- Description: This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins.

## Capabilities To Name On Screen
- Agents are FOR autonomous work, commands are FOR user-initiated actions
- Markdown file format with YAML frontmatter
- Triggering via description field with examples
- System prompt defines agent behavior
- Model and color customization

## Constraints / Failure Modes
- 3-50 characters
- Lowercase letters, numbers, hyphens only
- Must start and end with alphanumeric
- No underscores, spaces, or special characters
- ### name (required)
- Format: lowercase, numbers, hyphens only
- Pattern: Must start and end with alphanumeric
- ### description (required)

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: code-reviewer
- Referenced: test-generator
- Referenced: api-docs-writer
- Referenced: security-analyzer
- Referenced: -agent-
- Referenced: my_agent
- Referenced: examples/agent-creation-prompt.md
- Referenced: agents/agent-name.md
- Referenced: .md
- Referenced: agents/
- Signal: code block: markdown
- Signal: code block: yaml

## Source Sections
- Overview
- Agent File Structure
- Complete Format
- Frontmatter Fields
- name (required)
- description (required)
- model (required)
- color (required)
- tools (optional)
- System Prompt Design

## Batch Log Match
- Row: 18
- Canonical path: anthropics/claude-code/plugins/plugin-dev/skills/agent-development/SKILL.md
- MP4 path: anthropics/claude-code/youtube/claude-liam-agent-development/claude-liam-agent-development.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

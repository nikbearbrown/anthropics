# Source Details — claude-code--claude-liam-plugin-structure

Generated: 2026-09-05T11:09:00

## Reel
- Question: Plugin Structure
- Family: claude-code
- Source sheet: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code/youtube/claude-liam-plugin-structure/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code/plugins/plugin-dev/skills/plugin-structure/SKILL.md
- Name: Plugin Structure
- Description: This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices.

## Capabilities To Name On Screen
- Conventional directory layout for automatic discovery
- Manifest-driven configuration in .claude-plugin/plugin.json
- Component-based organization (commands, agents, skills, hooks)
- Portable path references using ${CLAUDE_PLUGIN_ROOT}
- Explicit vs. auto-discovered component loading

## Constraints / Failure Modes
- Manifest location: The plugin.json manifest MUST be in .claude-plugin/ directory
- Component locations: All component directories (commands, agents, skills, hooks) MUST be at plugin root level, NOT nested inside .claude-plugin/
- Optional components: Only create directories for components the plugin actually uses
- Naming convention: Use kebab-case for all directory and file names
- Must be relative to plugin root
- Must start with ./
- Cannot use absolute paths
- Support arrays for multiple locations

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: .claude-plugin/plugin.json
- Referenced: ${CLAUDE_PLUGIN_ROOT}
- Referenced: plugin.json
- Referenced: .claude-plugin/
- Referenced: code-review-assistant
- Referenced: test-runner
- Referenced: api-docs
- Referenced: ./
- Referenced: commands/
- Referenced: .md
- Signal: code block: json
- Signal: code block: markdown
- Signal: code block: bash

## Source Sections
- Overview
- Directory Structure
- Plugin Manifest (plugin.json)
- Required Fields
- Recommended Metadata
- Component Path Configuration
- Component Organization
- Commands
- Agents
- Skills

## Batch Log Match
- Row: 23
- Canonical path: anthropics/claude-code/plugins/plugin-dev/skills/plugin-structure/SKILL.md
- MP4 path: anthropics/claude-code/youtube/claude-liam-plugin-structure/claude-liam-plugin-structure.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

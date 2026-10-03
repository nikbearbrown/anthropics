# Source Details — knowledge-work-plugins--claude-liam-create-cowork-plugin

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Create Cowork Plugin.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-create-cowork-plugin/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/cowork-plugin-management/skills/create-cowork-plugin/SKILL.md
- Name: create-cowork-plugin
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- .claude-plugin/plugin.json is always required
- Component directories (skills/, agents/) go at the plugin root, not inside .claude-plugin/
- Only create directories for components the plugin actually uses
- Use kebab-case for all directory and file names
- > Nontechnical output: Keep all user-facing conversation in plain language. Do not expose implementation details like file paths, directory structures, or schema fields…
- │ └── plugin.json # Required: plugin manifest
- claude-plugin/plugin.json is always required
- Located at .claude-plugin/plugin.json. Minimal required field is name

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: .plugin
- Referenced: commands/
- Referenced: .md
- Referenced: skills/*/SKILL.md
- Referenced: references/
- Referenced: .claude-plugin/plugin.json
- Referenced: skills/
- Referenced: agents/
- Referenced: .claude-plugin/
- Referenced: 0.1.0
- Signal: code block: json
- Signal: code block: markdown
- Signal: code block: bash

## Source Sections
- Overview
- Plugin Architecture
- Directory Structure
- plugin.json Manifest
- Component Schemas
- Customizable plugins with ~~ placeholders
- How tool references work
- Connectors for this plugin
- ${CLAUDE_PLUGIN_ROOT} Variable
- Guided Workflow

## Batch Log Match
- Row: 177
- Canonical path: anthropics/knowledge-work-plugins/cowork-plugin-management/skills/create-cowork-plugin/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-create-cowork-plugin/mp4/claude-liam-create-cowork-plugin.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

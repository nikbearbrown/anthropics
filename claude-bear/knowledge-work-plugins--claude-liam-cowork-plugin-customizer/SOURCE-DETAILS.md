# Source Details — knowledge-work-plugins--claude-liam-cowork-plugin-customizer

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Cowork Plugin Customizer.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-cowork-plugin-customizer/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/cowork-plugin-management/skills/cowork-plugin-customizer/SKILL.md
- Name: cowork-plugin-customizer
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- > Finding the plugin: To find the plugin's source files, run find mnt/.local-plugins mnt/.plugins -type d -name "<plugin-name>" to locate the plugin directory, then read…
- Scoped customization — No ~~ placeholders exist, and the user asked to customize a specific part of the plugin (e.g., "customize the connectors", "update the standup…
- > Important: Never change the name of the plugin or skill being customized. Do not rename directories, files, or the plugin/skill name fields
- > Nontechnical output: All user-facing output (todo list items, questions, summaries) must be written in plain, nontechnical language. Never mention ~~ prefixes…
- ### Phase 0: Gather User Intent (scoped and general customization only)
- For scoped customization: Only include items related to the specific section the user asked about
- Otherwise: Use AskUserQuestion. Don't assume "industry standard" defaults are correct — if neither the user's input nor knowledge MCPs provided a specific answer, ask.…
- > Naming: Use the original plugin directory name for the .plugin file (e.g., if the plugin directory is coder, the output file should be coder.plugin). Do not rename the…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: find mnt/.local-plugins mnt/.plugins -type d -name "<plugin-name>"
- Referenced: grep -rn '~~\w' /path/to/plugin --include='.md' --include='.json'
- Referenced: ~~your-team-channel
- Referenced: commands/
- Referenced: commands/*.md
- Referenced: skills/*/SKILL.md
- Referenced: references/search-strategies.md
- Referenced: ~~your-org-channel
- Referenced: tickets.example.com/your-team/123
- Referenced: app.asana.com/0/PROJECT_ID/TASK_ID
- Signal: code block: bash
- Signal: code block: markdown

## Source Sections
- Determining the Customization Mode
- Customization Workflow
- Phase 0: Gather User Intent (scoped and general customization only)
- Phase 1: Gather Context from Knowledge MCPs
- Phase 2: Create Todo List
- Phase 3: Complete Todo Items
- Phase 4: Search for Useful MCPs
- Packaging the Plugin
- Summary Output
- From searching Slack

## Batch Log Match
- Row: 175
- Canonical path: anthropics/knowledge-work-plugins/cowork-plugin-management/skills/cowork-plugin-customizer/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-cowork-plugin-customizer/mp4/claude-liam-cowork-plugin-customizer.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

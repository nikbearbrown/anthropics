# Source Details — claude-plugins-official--claude-liam-skill-development

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Skill Development.
- Family: claude-plugins-official
- Source sheet: /Users/nik/Documents/books/anthropics/claude-plugins-official/youtube/claude-liam-skill-development/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-plugins-official/plugins/plugin-dev/skills/skill-development/SKILL.md
- Name: skill-development
- Description: This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins.

## Capabilities To Name On Screen
- This skill should be used when the user wants to "create a skill"
- "add a skill to plugin"
- "write a new skill"
- "improve skill description"
- "organize skill content"

## Constraints / Failure Modes
- Every skill consists of a required SKILL.md file and optional bundled resources:
- ├── SKILL.md (required)
- │ ├── YAML frontmatter metadata (required)
- │ │ ├── name: (required)
- │ │ └── description: (required)
- │ └── Markdown instructions (required)
- #### SKILL.md (required)
- Benefits: Keeps SKILL.md lean, loaded only when Claude determines it's needed

## Procedure / Sequence
- Understanding the Skill with Concrete Examples: Skip this step only when the skill's usage patterns are already clearly understood. It remains valuable even when…
- Planning the Reusable Skill Contents: To turn concrete examples into an effective skill, analyze each example by: 1. Considering how to execute on the…
- Create Skill Structure: For Claude Code plugins, create the skill directory structure: Note: Unlike the generic skill-creator which uses…
- Edit the Skill: When editing the (newly-created or existing) skill, remember that the skill is being created for another instance of…
- Validate and Test: For plugin skills, validation is different from generic skills: 1. Check structure: Skill directory in…
- Iterate: After testing the skill, users may request improvements. Often this happens right after using the skill, with fresh…

## Supporting Files And Signals
- Referenced: scripts/
- Referenced: scripts/rotate_pdf.py
- Referenced: references/
- Referenced: references/finance.md
- Referenced: references/mnda.md
- Referenced: references/policies.md
- Referenced: references/api_docs.md
- Referenced: assets/
- Referenced: assets/logo.png
- Referenced: assets/slides.pptx
- Signal: code block: bash
- Signal: code block: yaml
- Signal: code block: markdown

## Source Sections
- About Skills
- What Skills Provide
- Anatomy of a Skill
- Progressive Disclosure Design Principle
- Skill Creation Process
- Step 1: Understanding the Skill with Concrete Examples
- Step 2: Planning the Reusable Skill Contents
- Step 3: Create Skill Structure
- Step 4: Edit the Skill
- Additional Resources

## Batch Log Match
- Row: 66
- Canonical path: anthropics/claude-plugins-official/plugins/plugin-dev/skills/skill-development/SKILL.md
- MP4 path: anthropics/claude-plugins-official/youtube/claude-liam-skill-development/mp4/claude-liam-skill-development.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

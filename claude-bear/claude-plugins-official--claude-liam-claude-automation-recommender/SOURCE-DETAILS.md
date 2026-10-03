# Source Details — claude-plugins-official--claude-liam-claude-automation-recommender

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude Automation Recommender
- Family: claude-plugins-official
- Source sheet: /Users/nik/Documents/books/anthropics/claude-plugins-official/youtube/claude-liam-claude-automation-recommender/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md
- Name: claude-automation-recommender
- Description: Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.

## Capabilities To Name On Screen
- Analyze a codebase and recommend Claude Code automations (hooks
- MCP servers)
- Use when user asks for automation recommendations
- wants to optimize their Claude Code setup
- mentions improving Claude Code workflows

## Constraints / Failure Modes
- This skill is read-only. It analyzes the codebase and outputs recommendations. It does NOT create or modify any files. Users implement the recommendations themselves or…
- If user asks for a specific type: Focus only on that type and provide more options (3-5 recommendations)
- | Database project | create-migration (with validation script) | User-only |
- | Test suite | gen-test (with example tests) | User-only |
- | Component library | new-component (with templates) | User-only |
- | PR workflow | pr-check (with checklist) | User-only |
- | Releases | release-notes (with git context) | User-only |
- | Code style | project-conventions | Claude-only |

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: /skill-name
- Referenced: .claude/skills/<name>/SKILL.md
- Referenced: .env
- Referenced: .claude/skills/[name]/SKILL.md
- Referenced: .claude/settings.json
- Referenced: .claude/agents/[name].md
- Referenced: disable-model-invocation: true
- Referenced: user-invocable: false
- Referenced: .mcp.json
- Referenced: --mcp-debug
- Signal: code block: bash
- Signal: code block: markdown
- Signal: code block: yaml
- Signal: code block: json

## Source Sections
- Output Guidelines
- Automation Types Overview
- Workflow
- Phase 1: Codebase Analysis
- Phase 2: Generate Recommendations
- Phase 3: Output Recommendations Report
- Claude Code Automation Recommendations
- Codebase Profile
- 🔌 MCP Servers
- 🎯 Skills

## Batch Log Match
- Row: 34
- Canonical path: anthropics/claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md
- MP4 path: anthropics/claude-plugins-official/youtube/claude-liam-claude-automation-recommender/claude-liam-claude-automation-recommender.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

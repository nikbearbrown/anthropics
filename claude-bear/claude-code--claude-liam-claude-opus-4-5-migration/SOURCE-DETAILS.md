# Source Details — claude-code--claude-liam-claude-opus-4-5-migration

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude Opus 4-5 Migration
- Family: claude-code
- Source sheet: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code/youtube/claude-liam-claude-opus-4-5-migration/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code/plugins/claude-opus-4-5-migration/skills/claude-opus-4-5-migration/SKILL.md
- Name: claude-opus-4-5-migration
- Description: Migrate prompts and code from Claude Sonnet 4.0, Sonnet 4.5, or Opus 4.1 to Opus 4.5. Use when the user wants to update their codebase, prompts, or API calls to use Opus 4.5. Handles model string updates and prompt adjustments for known Opus 4.5 behavioral differences. Does NOT migrate Haiku 4.5.

## Capabilities To Name On Screen
- Migrate prompts and code from Claude Sonnet 4.0
- or Opus 4.1 to Opus 4.5
- Use when the user wants to update their codebase
- or API calls to use Opus 4.5
- Handles model string updates and prompt adjustments for known Opus 4.5 behavioral differences

## Constraints / Failure Modes
- Do NOT migrate: Any Haiku models (e.g., claude-haiku-4-5-20251001)
- Opus 4.5 has known behavioral differences from previous models. Only apply these fixes if the user explicitly requests them or reports a specific issue. By default, just…
- You MUST... → You should
- NEVER skip... → Don't skip
- REQUIRED → remove or soften
- Only apply to tool-triggering instructions. Leave other uses of emphasis alone
- When extended thinking is not enabled (the default), Opus 4.5 is particularly sensitive to the word "think" and its variants. Extended thinking is enabled only if the…
- See references/effort.md for configuring the effort parameter (only if user requests it)

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: references/effort.md
- Referenced: context-1m-2025-08-07
- Referenced: claude-opus-4-5-20251101
- Referenced: anthropic.claude-opus-4-5-20251101-v1:0
- Referenced: claude-opus-4-5@20251101
- Referenced: claude-sonnet-4-20250514
- Referenced: anthropic.claude-sonnet-4-20250514-v1:0
- Referenced: claude-sonnet-4@20250514
- Referenced: claude-sonnet-4-5-20250929
- Referenced: anthropic.claude-sonnet-4-5-20250929-v1:0
- Signal: code block: python

## Source Sections
- Migration Workflow
- Model String Updates
- Unsupported Beta Headers
- Target Model Strings (Opus 4.5)
- Source Model Strings to Replace
- Prompt Adjustments
- 1. Tool Overtriggering
- 2. Over-Engineering Prevention
- 3. Code Exploration
- 4. Frontend Design

## Batch Log Match
- Row: 36
- Canonical path: anthropics/claude-code/plugins/claude-opus-4-5-migration/skills/claude-opus-4-5-migration/SKILL.md
- MP4 path: anthropics/claude-code/youtube/claude-liam-claude-opus-4-5-migration/claude-liam-claude-opus-4-5-migration.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

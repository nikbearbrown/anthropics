# BUILD-PROMPT — cc-pretooluse-grade-blocker

Concept: build a Claude Code PreToolUse hook that blocks Write / Edit / MultiEdit whose content contains a final letter grade, using Claude Code itself to draft the hook.

Method: three real fresh headless `claude -p` runs (Claude Code 2.1.150, 2026-09-10), one small `scratch/` project, one build ask + one workload ask. See `SESSION.md`, `PROMPTS.md`, `SOURCES.md`.

Skill: `cc-explainer` (`metadata.skill`). Palette: `claude`. Operator: Liam, in for Bear (Kokoro `am_onyx`). Aspect: 16:9. Never publishes — master stays in this folder.

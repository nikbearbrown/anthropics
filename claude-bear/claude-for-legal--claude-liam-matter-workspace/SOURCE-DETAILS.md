# Source Details — claude-for-legal--claude-liam-matter-workspace

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Matter Workspace.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-matter-workspace/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/ai-governance-legal/skills/matter-workspace/SKILL.md
- Name: matter-workspace
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- /ai-governance-legal:matter-workspace close <slug> — archive a matter (move to ~/.claude/plugins/config/claude-for-legal/ai-governance-legal/matters/_archived/, never…
- /ai-governance-legal:matter-workspace none — detach from any active matter, work at practice-level only
- none → set Active matter: to none — practice-level context only
- The skill never reads across matters unless Cross-matter context is on in the practice-level CLAUDE.md
- Multi-client practitioners (private practice — solo, small firm, large firm) work across many matters. Context from one must not leak into another. This skill is the…
- Default state is off. In-house users never see this — they run at practice-level only. Matter workspaces turn on at cold-start for private-practice users, or by editing…
- If the closed matter was the active matter, set Active matter: to none — practice-level context only
- Set Active matter: in the practice-level CLAUDE.md to none — practice-level context only. Confirm with the user

## Procedure / Sequence
- Read ~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md…
- Use the workflow below.
- Dispatch on the first token of $ARGUMENTS
- Show the user what changed and confirm before writing.

## Supporting Files And Signals
- Referenced: /ai-governance-legal:matter-workspace new <slug>
- Referenced: matter.md
- Referenced: /ai-governance-legal:matter-workspace list
- Referenced: /ai-governance-legal:matter-workspace switch <slug>
- Referenced: /ai-governance-legal:matter-workspace close <slug>
- Referenced: ~/.claude/plugins/config/claude-for-legal/ai-governance-legal/matters/_archived/
- Referenced: /ai-governance-legal:matter-workspace none
- Referenced: ~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md
- Referenced: /ai-governance-legal:cold-start-interview --redo
- Referenced: /matter-workspace
- Signal: code block: markdown

## Source Sections
- Subcommands
- Instructions
- Notes
- Storage layout
- Active matter is in the practice CLAUDE.md
- Subcommand logic
- new <slug>
- list
- switch <slug>
- close <slug>

## Batch Log Match
- Row: 305
- Canonical path: anthropics/claude-for-legal/ai-governance-legal/skills/matter-workspace/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-matter-workspace/mp4/claude-liam-matter-workspace.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

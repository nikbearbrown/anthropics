# Source Details — claude-for-legal--claude-liam-ai-tool-handoff

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Ai Tool Handoff.
- Family: claude-for-legal
- Source sheet: /Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-ai-tool-handoff/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/ai-tool-handoff/SKILL.md
- Name: ai-tool-handoff
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- Matter context. Check ## Matter workspaces in the practice-level CLAUDE.md. If Enabled is ✗ (the default for in-house users), skip the rest of this paragraph — skills…
- Filter output: Flag only where extraction target is present — no need for "no CoC clause found" for every doc
- "Use as-is": Ingest directly into diligence findings. (Only if ~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md says this — it's rare.)

## Procedure / Sequence
- Prepare the batch: - Identify documents for the batch (from VDR inventory) - Specify extraction targets per…
- Load (or instruct the loader): Per ~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md — who loads. If it's you, generate the load…
- QA the output: When the tool returns results, apply the trust level: "Use as-is": Ingest directly into diligence findings. (Only if…
- Judgment layer: The tool found the clauses. Now apply judgment: For each flagged CoC provision: is it actually triggered by this deal?…

## Supporting Files And Signals
- Referenced: ~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md
- Referenced: /corporate-legal:matter-workspace switch <slug>
- Referenced: practice-level
- Referenced: matter.md
- Referenced: ~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<matter-slug>/
- Referenced: Cross-matter context
- Referenced: tabular-review
- Referenced: /corporate-legal:tabular-review
- Signal: code block: markdown

## Source Sections
- Matter context
- Purpose
- Load context
- When to hand off
- The handoff
- Step 1: Prepare the batch
- Step 2: Load (or instruct the loader)
- [Tool] Load Request — [Deal code] — [Category]
- Step 3: QA the output
- Step 4: Judgment layer

## Batch Log Match
- Row: 97
- Canonical path: anthropics/claude-for-legal/corporate-legal/skills/ai-tool-handoff/SKILL.md
- MP4 path: anthropics/claude-for-legal/youtube/claude-liam-ai-tool-handoff/mp4/claude-liam-ai-tool-handoff.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

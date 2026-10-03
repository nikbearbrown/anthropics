# Source Details — claude-plugins-official--claude-liam-math-olympiad

Generated: 2026-09-05T11:09:00

## Reel
- Question: math-olympiad
- Family: claude-plugins-official
- Source sheet: /Users/nik/Documents/books/anthropics/claude-plugins-official/youtube/claude-liam-math-olympiad/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-plugins-official/plugins/math-olympiad/skills/math-olympiad/SKILL.md
- Name: math-olympiad
- Description: 

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- biased toward agreement. Fresh context, cleaned proof only
- Tool policy: Solvers and verifiers use THINKING ONLY in the tight-budget
- | AIME numeric answer | Best-of-N → majority vote | Answer check only |
- ### 2. Generate candidates with internal refinement (parallel, thinking only)
- The Agent tool cannot enforce tool restriction. Subagents get the full tool
- set. The only mechanism is the prompt. Use this prompt VERBATIM — do not
- summarize, do not synthesize your own:
- NO COMPUTATION. Do not use Bash, Python, WebSearch, Read, Write, or any tool that runs code or fetches data. Numerical verification is not a proof step. "I computed…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: opts.label
- Referenced: references/solver_heuristics.md
- Referenced: references/adversarial_prompts.md
- Referenced: references/verifier_patterns.md
- Referenced: math-research
- Referenced: references/presentation_prompts.md
- Referenced: scripts/check_latex.sh
- Referenced: scripts/compile_pdf.sh
- Referenced: references/model_tier_defaults.md
- Referenced: evals/

## Source Sections
- The five things that change outcomes
- When to use which approach
- For a full problem set
- The Workflow
- 1. Interpretation check (30 seconds, catches 50/63 of one class of errors)
- 2. Generate candidates with internal refinement (parallel, thinking only)
- 3. Clean the solution (context isolation — the #1 lever)
- 4. Adversarial verify (fresh context, pattern-armed)
- 5. Rank and vote-verify (asymmetric + early exit)
- 5b. When one case won't close — step back before grinding

## Batch Log Match
- Row: 54
- Canonical path: anthropics/claude-plugins-official/plugins/math-olympiad/skills/math-olympiad/SKILL.md
- MP4 path: anthropics/claude-plugins-official/youtube/claude-liam-math-olympiad/claude-liam-math-olympiad.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

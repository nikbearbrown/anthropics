# SOURCES — cc-hook-enforcement

## Primary evidence (all in `evidence/` of this reel)

- `run-advisory.jsonl` — Run 1 stream-json (advisory-only; Claude refused in text, no tool call)
- `run-hook-fires.jsonl` — Run 2 stream-json (hook-only; Write intercepted, corrected, second Write succeeded)
- `run-advisory.stderr`, `run-hook-fires.stderr` — stderr from each run
- `run-hook-only.jsonl` — abandoned first hook-attempt where Claude discovered `CLAUDE.md.stash` before writing (kept as audit trail, not used on screen; explains why we moved the rule fully OUT of `scratch/` for Run 2)
- `CLAUDE.md` (9 lines) — the advisory rule
- `settings.local.json` (15 lines) — hook registration
- `guard.py` (42 lines) — the PreToolUse hook
- `students.csv`, `ask.txt`, `README.md` — the scratch project
- `bad.json`, `ok.json` — the direct hook demo payloads
- `hook-block-message.txt` — the tool_result carried back into Run 2, verbatim
- `summary.blocked.md` — the first Write's content (the one the hook blocked)
- `summary.hook-only.md` — the second Write's content (the one that landed)
- `CLAUDE.md.staged` — the rule file, staged out of `scratch/` for Run 2

## Concept source

- `anthropics/claude-code-101/03-hooks-skills-commands/claude-code--claude-liam-vox-hook-enforcement/beat_sheet.json` — the concept beat sheet this reel replaces. Kept its title verb ("fails") as a diagnostic frame; the film's narrative is authored from the runs, not the concept.

## Doctrine

- `brutalist-art/skills/make/cc-explainer/SKILL.md` — spine, LIAM LAW, TERMINAL-FIRST, REAL-SESSION, TYPES-NOT-NARRATES, VERIFY-IS-A-COMMAND, kit gotchas
- `brutalist-art/skills/make/cc-explainer/reference/three-beats.md` — CONDUCT & HUMAN doctrine
- `brutalist-art/runtime/remotion/src/scenes/CC-TEMPLATES.md` — kit product-string law
- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — Boondoggle Score / capacities (PF, TO, PA, IJ, EI)
- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — the ledger's Tier-4 frame

## Sibling reel (for the reader's benefit — not a source)

- `anthropics/claude-code-101/03-hooks-skills-commands/cc-hook-advisory-vs-deterministic/` — built 2026-09-09/10 from four escalating advisory runs plus one hook-only run. Same scratch harness (independently re-created here). Its finding: advisory held under nice / urgent / prompt-injection / fixture escalations; hook caught the CLAUDE.md-stashed run. This reel is not a re-cut; it is authored from independent runs and takes a different angle — the mechanism as a receipt.

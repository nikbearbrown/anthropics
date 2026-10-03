# SOURCES — cc-engineering-partner-loop

**REAL-SESSION LAW.** Every block traces to one of these.

## Primary — the sessions themselves

- `SESSION.md` — the reconstruction transcript, human-readable.
- `evidence/run-bare.jsonl` — full stream-json for run 1 (bare).
- `evidence/run-partner-plan.jsonl` — turn 1 of run 2 (plan only, Edit withheld).
- `evidence/run-partner-apply.jsonl` — turn 2 of run 2 (apply the exact plan).
- `evidence/run-partner-correct.jsonl` — turn 3 of run 2 (docstring correction).
- `evidence/verify.txt` — Liam's plain-shell audit of the final state.
- `scratch/` — the tiny module and test suite the runs operated on (git commit `fc0e333` is the initial state).

## Snapshots

- `evidence/ranges.orig.py` — starting `ranges.py` (5 tests, 2 failing).
- `evidence/ranges.bare.py` — after run 1 (5 pass; variable names `lo/hi`).
- `evidence/ranges.partner.py` — after run 2 turn 2 (5 pass; variable names `start/end`).
- `evidence/ranges.final.py` — after run 2 turn 3 (docstring updated).
- `evidence/test_ranges.py` — the oracle.
- `evidence/ORACLE.sh` — one-line wrapper around `python3 -m unittest test_ranges -v`.

## Doctrine (for CONDUCT and HUMAN framings)

- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — the Boondoggle Score's five capacities (PF, TO, PA, IJ, EI) and why verify does not speed up when the solver does.
- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — Tier 4 (metacognitive) and the "supervise, don't refuse" verdict that the HUMAN ledger enacts.

## Concept card the film derives from

- `anthropics/claude-code-101/00-what-it-is/claude-code--claude-liam-engineering-partner-loop/beat_sheet.json` — earlier CC video on the same idea, used as the concept card. Its title's claim and Your-Turn intent are kept; none of its numbers, beats, or on-screen strings are reused.

## Kit and skill

- `brutalist-art/skills/make/cc-explainer/SKILL.md` — spine, laws, kit gotchas.
- `brutalist-art/runtime/remotion/src/scenes/CC*.tsx` — the CC kit components.
- `brutalist-art/runtime/remotion/src/scenes/FlowDiagram.tsx` — the BFLOW pattern.

## Not sources

No web fetches, no external images, no AI-generated audio or video, no third-party data.

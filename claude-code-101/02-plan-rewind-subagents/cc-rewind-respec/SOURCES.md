# SOURCES — cc-rewind-respec

## The reel's session (primary source — every block traces here)

- `SESSION.md` — the four real headless runs this reel reconstructs (FF1/FF2/FF3 via `--resume`, respec fresh)
- `evidence/run-ff1.jsonl`, `run-ff2.jsonl`, `run-ff3.jsonl`, `run-respec.jsonl` — raw `--output-format stream-json --verbose`
- `evidence/dedupe.ff3.py`, `evidence/dedupe.respec.py` — the two dedupe implementations the film compares
- `evidence/test_dedupe.py`, `SPEC.md`, `ask.txt`, `respec-ask.txt` — the scratch inputs
- `evidence/drift.txt` — Liam's plain-shell drift check ran live 2026-09-09
- `evidence/sid-ff.txt`, `sid-respec.txt` — session ids for the two claude-p sessions
- `scratch/` — the git repo (commit `f5ef78b` "buggy start" is the checkpoint)

## Concept source (framing only — copy replaced by real receipts)

- `anthropics/claude-code-101/02-plan-rewind-subagents/claude-code--claude-liam-vox-rewind-respec/beat_sheet.json` — the concept sheet on which the target concept and title stand (used for the mechanism framing: forward correction pollutes context; /rewind restores; respec adds failure as negative constraint). None of its beats, card copy, or numbers reused; the reel reconstructs the mechanism from a fresh session.

## Doctrine sources (CONDUCT + HUMAN beats, per SKILL)

- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — the Boondoggle Score (CONDUCT beat, B10): programming as conducting; the human's capacities (`[PF] [TO] [PA] [IJ] [EI]`) and the handoff condition after each Claude step. This session's dangerous middle (step 4, the FF3 repr one-liner) is scored explicitly per this chapter.
- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — the ledger (HUMAN beat, B11), Tier 4 framing: the machine cannot reliably report its own uncertainty, so the metacognitive burden — was this passing test actually the right test — is the human's and cannot be lent.

## SKILL / kit references (product strings, verbatim)

- `brutalist-art/skills/make/cc-explainer/SKILL.md` — LIAM LAW, TERMINAL-FIRST, REAL-SESSION, TYPES-NOT-NARRATES, VERIFY-IS-A-COMMAND, OUTRO-LOCK, the spine, the two closing-block beats, component contracts, kit gotchas. The exact sentence "a NEW `claude -p` is a fresh session — that is `/clear`" is quoted from the CC101LOOP briefing and the SKILL alike; used verbatim in B07 narration.
- `brutalist-art/runtime/remotion/src/scenes/CC-TEMPLATES.md` — editorial law for the CC kit (product mode strings, keybindings, status verbs).
- `brutalist-art/runtime/remotion/src/scenes/CCSession.tsx` — block schema (text/prompt/tool/diff/status/plan).
- `brutalist-art/runtime/remotion/src/tokens/claudecode.ts` — CC palette + font tokens.

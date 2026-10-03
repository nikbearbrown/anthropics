# SOURCES — cc-buildlog-assessment

## Primary — this reel's own evidence

- `SESSION.md` — the three real fresh headless `claude -p` runs this reel reconstructs. REAL-SESSION LAW. Every `CCSession` block and every quoted line traces here.
- `evidence/run-a.jsonl`, `evidence/run-b.jsonl`, `evidence/run-grader.jsonl` — raw stream-json (session ids, tool uses, verbatim assistant text, cost, duration).
- `evidence/CLAUDE.a.md`, `evidence/CLAUDE.b.md` — the two students' `CLAUDE.md` files as they stood at the time of the runs.
- `evidence/verify.txt` — Liam's plain-shell verify block (`wc`, `diff -q`, `grep -c` ×3) with outputs.
- `scratch/student-a/`, `scratch/student-b/`, `scratch/grader/` — the working directories the three sessions ran in.

## Concept source

- `anthropics/claude-code-101/01-context-and-memory/claude-code--claude-liam-vox-buildlog-assessment/beat_sheet.json` — the concept card the film was built from. Its framing (CLAUDE.md as an assessment artefact for what AI cannot generate) is kept; its vox-style card body is replaced by the three real runs above.

## Doctrine

- `brutalist-art/skills/make/cc-explainer/SKILL.md` — TERMINAL-FIRST, REAL-SESSION, TYPES-NOT-NARRATES, VERIFY-IS-A-COMMAND, the two closing-block beats (CONDUCT and HUMAN), the LIAM LAW, the kit gotchas.
- `brutalist-art/skills/make/cc-explainer/reference/three-beats.md` — CONDUCT / HUMAN doctrine.
- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — the Boondoggle Score's capacity vocabulary (PF · TO · PA · IJ · EI) and the "dangerous middle" concept.
- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — the HUMAN ledger's Tier-4 frame (the human's metacognitive burden cannot be lent to the machine).

## Kit / runtime

- `brutalist-art/runtime/remotion/src/scenes/CC-TEMPLATES.md` — the CC kit contract (verbatim product strings; CCSession block model; mascot rules).
- `brutalist-art/runtime/remotion/src/tokens/claudecode.ts` — VERBS, mode strings, colour tokens.
- `brutalist-art/runtime/scripts/generate_audio_kokoro.py` — Liam narration engine (`am_onyx`, free, local).
- `brutalist-art/runtime/qc/factcheck_check.py`, `runtime/scripts/type_check.py`, `runtime/scripts/bookend_check.py` — the three gates that must PASS before final.

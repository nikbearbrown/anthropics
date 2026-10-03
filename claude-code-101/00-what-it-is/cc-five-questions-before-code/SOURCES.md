# SOURCES — cc-five-questions-before-code

## Primary — the runs

- `SESSION.md` — this reel's authoritative source; four real headless `claude -p` runs, stream-json in `evidence/`.
- `evidence/run-cold.jsonl` — the cold run (session `8d98c8d9…`).
- `evidence/run-calib-q.jsonl` — the calibration questions in read-only mode (session `64fc2444…`).
- `evidence/run-calib-build.jsonl` — the calibration build, resumed from `64fc2444…`.
- `evidence/run-q5only.jsonl` — Q5 alone in read-only mode (session `fc699f00…`).
- `evidence/stats.cold.py`, `evidence/test_stats.cold.py` — what the cold run wrote.
- `evidence/stats.calib.py`, `evidence/test_stats.calib.py` — what the calibrated run wrote.
- `evidence/readings.log`, `evidence/production.log` — the clean fixture (in scratch) and the real-world fixture (Liam's, never in scratch).
- `evidence/five-questions.txt` — the reusable template Liam pastes.

## Concept

- `anthropics/claude-code-101/00-what-it-is/claude-code--claude-liam-five-questions-before-code/beat_sheet.json` — the source concept card (framing kept: "five questions before the first tool call surface the wrong assumption"; the hypothetical stylesheet example is not used).

## Doctrine (CONDUCT + HUMAN beats)

- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — Boondoggle Score, Minion/Gru dependency, dangerous middle.
- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — the ledger: MUST/SHOULD human, CAN/SHOULD AI.
- `brutalist-art/skills/make/cc-explainer/SKILL.md` — TERMINAL-FIRST, REAL-SESSION, TYPES-NOT-NARRATES, spine, three closing beats.
- `brutalist-art/skills/make/cc-explainer/reference/three-beats.md` — doctrine behind CONDUCT and HUMAN.

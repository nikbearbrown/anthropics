# SOURCES — cc-three-file-system-simulator

## The film's own evidence (built for this reel)

- `SESSION.md` — the transcript of the two runs, the condition table, and Liam's plain-shell verify.
- `evidence/run-bare.jsonl`, `evidence/run-three.jsonl` — raw Claude Code stream-json from each run.
- `evidence/transcript.txt` — a human-readable extract from the two jsonl files.
- `evidence/index.bare.html` (595 lines), `evidence/index.three.html` (111 lines) — the two pages the two runs produced, verbatim.
- `evidence/CLAUDE.md`, `evidence/DESIGN.md`, `evidence/PROJECT.md`, `evidence/check.py` — the three files (19 lines) and the definition-of-done script, written by Liam before run 2.
- `evidence/verify.txt` — Liam's plain-shell verify commands and their outputs.
- `clips/BSHOW-step-{00,15,40,63}.png` — four browser captures of the three-file page; `clips/BSHOW.mp4` and `media/BSHOW.mp4` = the 8s composite; `media/BSHOW.source.txt` records the capture protocol.

## Doctrine sources cited in narration or beat design

- `info-7375-conducting-ai/chapters/02-the-solve-verify-asymmetry.md` — the Boondoggle Score frame (Gru part / Minion part; the five capacities [PF]/[TO]/[PA]/[IJ]/[EI]; the dangerous middle).
- `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` — the ledger frame (MUST/SHOULD human · CAN/SHOULD AI); Tier 4 metacognitive supervision.

## Concept source (input to this build)

- `anthropics/claude-code-101/01-context-and-memory/claude-code--claude-liam-three-file-system-simulator/beat_sheet.json` — the concept sheet from the CC-101 tier. This build keeps the concept's *thesis* (three files gate the build; polished-but-generic defaults become the teacher's when the files are written first) and replaces every card body with the two real runs above. The concept's specific symptoms (Material Design blue, drag-and-drop) are not asserted — this bare run produced tailwind-blues + autoplay + a speed slider instead, which is the same argument on different symptoms.

## Not used

- No web fetches, no external transcripts, no third-party datasets. Every number and screen string traces to files in this reel folder.

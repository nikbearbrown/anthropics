# FACTCHECK — cc-stop-prompting-claude

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (four fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the four runs' stream-json and the files in `evidence/`. Liam's checks were run in a plain shell on the evidence folder. Claude's sentences are verbatim spans. Model / version / cost strings are omitted from narration and on-screen text (they appear only in `SESSION.md`, sidecar for provenance).

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Bare-A: preamble + ask → "…same time, same link…"; sign "— Bear" | PASS | `run-bare-a.jsonl` `result` field; `note-bare-a.txt` | — |
| 2 | B00, BVDT | "Nine hundred bytes of preamble" for the class-note ask | PASS | `wc -c ask-bare-a.txt` → 975 (rounded down in narration) | — |
| 3 | B00, B05 | The invented `link` — a URL detail never in the ask | PASS | `note-bare-a.txt`: "Same time, same link"; ask-bare-a.txt has no "link" and explicitly forbids URL invention | — |
| 4 | B01 | "Nine hundred seventy-five bytes … nine hundred ninety-nine" for the two bare asks | PASS | `wc -c ask-bare-a.txt ask-bare-b.txt` → 975 / 999 | — |
| 5 | B01 | `check.py` PASS on both bare notes | PASS | `python3 check.py note-bare-a.txt note-bare-b.txt` → PASS / PASS | — |
| 6 | B01 | `grep -c link` → 1 on bare-A, 0 on bare-B | PASS | verified in `SESSION.md` VERIFY block | — |
| 7 | B01 | "The bare prompt literally said 'do not invent URLs'" | PASS | `ask-bare-a.txt` contains: "Do not invent names, dates, room numbers, URLs, or citations." | — |
| 8 | B02 | "Twenty-six lines … twelve hundred fifty-six bytes" for CLAUDE.md | PASS | `wc -l` → 26; `wc -c` → 1256 | — |
| 9 | B02 | The five bulleted rules shown (plain English, banned words, address as class, do not invent, plain text) | PASS | `evidence/CLAUDE.md` verbatim; on-screen lines are truncated with `…` | — |
| 10 | B03 | Files-A prompt (three lines) is the verbatim ask; the Claude output verbatim | PASS | `evidence/ask-files-a.txt` (146 bytes) and `note-files-a.txt` | — |
| 11 | B03, B04 | "A hundred forty-six bytes … a hundred seventy-one" for the two files asks | PASS | `wc -c ask-files-a.txt ask-files-b.txt` → 146 / 171 | — |
| 12 | B04 | "Six point two times less typing" | PASS | 1974 / 317 = 6.2271… → "6.2× less typing" | — |
| 13 | B04 | `grep -c link` on files outputs → 0 | PASS | `SESSION.md` VERIFY | — |
| 14 | B05 | The two outputs quoted side-by-side, verbatim | PASS | `note-bare-a.txt`, `note-files-a.txt` — quoted with the elided-continuation marker `…` | — |
| 15 | B05 | "The difference isn't intelligence. It's what Claude read first." | PASS | same model in both runs (see `cache_creation` deltas in `SESSION.md`); characterisation not a claim | — |
| 16 | B06 | Six-step score, "dangerous middle" ringed at step 3 (invented `link`) | PASS | steps map to `SESSION.md` runs; step 3 is the audit that caught the URL | — |
| 17 | B07 | Ledger rows | PASS | derived from the four runs: Bear must name voice / read output / decide "done"; AI can fill in voice, can lose a rule in a long prompt (bare-A), should read the file first (files runs did), should say what it changed | — |
| 18 | BVDT | Verdict lines; "six-point-two times less typing"; "URL rule held" | PASS | rows above; the URL rule is CLAUDE.md line "Never invent a name, date, room number, URL, or citation." | — |
| 19 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
| 20 | all | Model / version strings ("Claude Code 2.1.150", "claude-opus-4-7"), Slurm session UUIDs, USD costs ($0.086 etc.) | EXEMPT | recorded in `SESSION.md`, never spoken or shown | — |
| 21 | BOUT props | `modelLabel: "Opus 5"`, `effortLabel: "High"` in BHTF composer chrome | EXEMPT | on-screen composer chrome only (kit-required labels), never narrated as a fact | — |

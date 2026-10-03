# FACTCHECK — cc-buildlog-assessment

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (three real fresh headless runs) and `evidence/` (raw stream-json, both CLAUDE.mds, both signup.htmls, `verify.txt`).

**Verification boundary.** Every number, quotation, and file line on screen comes from the three runs' stream-json and the files in `evidence/`. Claude's spoken sentences are verbatim spans; product strings are verbatim from the kit. Liam's checks were run in a plain shell on `scratch/` (both students side by side) and appear as bang commands inside CCSession or as CCPlainShell lines. The source concept's framing (CLAUDE.md as assessment artefact; AI generates code but not the record of decisions) is kept.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Two folders; same 54-line `signup.html`; `diff` silent | PASS | `verify.txt` — `wc -l` and `diff -q` | — |
| 2 | B00 | CLAUDE.md line counts — 36 vs 4 | PASS | `verify.txt` — `wc -l student-*/CLAUDE.md` | — |
| 3 | BIDEA | The idea's four writer lines; the "code" → "file" correction | PASS | narrative claim of the film, backed by the runs; the misconception is the one the film exists to fix | — |
| 4 | BDEFS | Five terms; definitions ≤70 chars each | PASS | terms and one-line meanings drawn from the concept doc and the SKILL vocabulary | — |
| 5 | B01 | Ask verbatim; refusal quoting 2026-08-14 by date; three alternatives | PASS | `evidence/run-a.jsonl` result span — the wording is Claude's own; text blocks are clause-split for the 44-char kit budget without changing wording | — |
| 6 | B02 | The three dated headers; the 2026-08-14 body ("bare run built a full email/password sign-up form…") | PASS | `evidence/CLAUDE.a.md` lines 16–19 (headers) and 17–20 (Aug 14 body) | — |
| 7 | B03 | Ask verbatim; Read of `signup.html`; the client-side / View Source concern; three clarifying questions | PASS | `evidence/run-b.jsonl` — the "View Source" span and the AskUserQuestion tool_use are both present; the three options are Claude's own labels | — |
| 8 | B04 | `diff -q` silent; `grep -c '^### 20'` → 3 vs 0; `grep -c 'Dangerous middle'` → 3 vs 0; `grep -c 'Constraint added'` → 3 vs 0 | PASS | `verify.txt` — all four commands with their outputs | — |
| 9 | B05 | Grader session read both files (renamed); score 16/16 (Student A) and 0/16 (Student B); per-row scores 4/4/4/4 and 0/0/0/0 | PASS | `evidence/run-grader.jsonl` — Bash `ls` + two Read calls; the four rows and totals are verbatim spans of Claude's rendered response | — |
| 10 | B06 | Six-step boondoggle: PF (ask) → CLAUDE A refusal (cites 2026-08-14) → HUMAN [PA] grep audit → CLAUDE B pause → HUMAN [IJ] "file, not model" → CLAUDE grader 16/0; tally PF 1 · PA 1 · IJ 1 · TO 0 · EI 0 | PASS | maps to `SESSION.md` runs and to the audit commands in `verify.txt` | — |
| 11 | B06 | Dangerous middle: step 2 (the refusal citing a date — dates are easy to hallucinate) | PASS | design choice matches the SKILL's dangerous-middle doctrine (the plausible-but-uncheckable output) | — |
| 12 | B07 | Ledger rows drawn from the three runs (CAN: generate code, cite by date, score from a file; SHOULD: pause when no rule) | PASS | `run-a`, `run-b`, `run-grader` respectively; Student B's pause is the SHOULD row in action | — |
| 13 | BVDT | Same-ask outcomes; 54-line diff-silent code; 36 vs 4 CLAUDE.md; 16/0 grader | PASS | rows 1–2, 8, 9 above | — |
| 14 | BVDT | FALSIFIABLE line: a bare Claude (no CLAUDE.md) refusing this ask on its own | PASS | falsifiability criterion — if it happened, the refusal would come from the model, not the file, and the film's claim would fail | — |
| 15 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
| 16 | all | Model / version / Claude Code build strings; costs | EXEMPT | not spoken; recorded in `SESSION.md` and `evidence/*.jsonl` for provenance only | — |

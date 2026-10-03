# FACTCHECK — cc-three-files

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (three real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the three runs' stream-json, the three pages, the three files and the checker in `evidence/`. Liam's checks were run in a plain shell on the evidence folder (`check.py` symlinked to each page in turn) and are shown as bang commands inside the session. Claude's sentences are verbatim spans. The source concept's framing (three files; polished-but-generic defaults) is kept; its Copyright Office citation is not used.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B03 | The ask, verbatim | PASS | `evidence/ask.txt` | — |
| 2 | B00 | Two Reads, then "I'll create a self-contained `index.html` sign-up page. Since there's no backend specified, I'll use `mailto:` as the submission target so it works out-of-the-box."; Write | PASS | `run-bare.jsonl` (the `ls -la` before the Reads is omitted for height; last line display-truncated) | — |
| 3 | B00, B01 | "Two hundred and twelve lines" | PASS | `wc -l index.bare.html` → 212 | — |
| 4 | B01 | `check.py` → FAIL emoji / FAIL email/password field; the two inputs (name, email) | PASS | `SESSION.md` VERIFY; the input lines are display-elided with `…` | — |
| 5 | B01 | "a calendar, a clock, a pin" | PASS | the three emoji in `index.bare.html`: 📅 🕕 📍 | — |
| 6 | B01 | "the internet's average sign-up page" | PASS | characterisation of a generic default, labelled as such | — |
| 7 | B02 | `wc -l` → 5 / 7 / 7; PROJECT.md's five questions | PASS | `evidence/CLAUDE.md`, `DESIGN.md`, `PROJECT.md`; lines display-truncated at 60 chars | — |
| 8 | B02 | The paraphrase of CLAUDE.md and DESIGN.md in narration | PASS | the files, verbatim in `evidence/` | — |
| 9 | B03 | Reads (check.py, PROJECT.md, DESIGN.md), the plan sentence "I have the constraints. Let me build `index.html` — one column, system font, name field only, next-Thursday computed in the browser.", Write, `python3 check.py` → PASS | PASS | `run-three.jsonl` (README/ask Reads omitted for height; CLAUDE.md is auto-loaded, not Read — narration says "reads the three files first", which is true of two by Read and one by auto-load) | — |
| 10 | B03, B04 | "Ninety-five lines" | PASS | `wc -l index.three.html` → 95 | — |
| 11 | B04 | one `<input>` (first name); `#D97757` once; `getDay` on line 75 | PASS | `SESSION.md` VERIFY | — |
| 12 | B05 | The check-only run: Read check.py, "following the constraints in check.py", Write, PASS, "a sign-up form (name, free-form contact field, date, what you're working on, expected frequency, reminder opt-in)"; "in a serif face" | PASS | `run-barecheck.jsonl`; `grep font-family index.barecheck.html` → Georgia serif; `grep -c reminder` → 4 | — |
| 13 | B05 | "left in it by accident" | PASS | SESSION.md: the first bare attempt had check.py in the folder; kept as a third condition | — |
| 14 | B06 | Six steps; tally PF 2 · PA 1 · IJ 1 · TO 0 · EI 0 | PASS | maps to SESSION.md | — |
| 15 | B07 | Ledger rows ("it did" → run three's plan sentence; the refused email field) | PASS | `run-three.jsonl`; one input in `index.three.html` | — |
| 16 | BVDT | Verdict lines; "mailto to a placeholder" | PASS | rows 2–12; `organizer@example.com` in Claude's bare summary | — |
| 17 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
| 18 | all | Model/version strings; "Today (Wed 2026-09-09)" in Claude's text | EXEMPT | not shown or spoken | — |
| 19 | metadata | Costs ($0.248 / $0.290 / $0.367) | EXEMPT | recorded, not spoken | — |

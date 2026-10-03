# FACTCHECK — cc-three-file-system-simulator

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (two real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the two runs' stream-json, the two pages, the three files and the checker in `evidence/`, and the four browser captures in `clips/`. Liam's checks were run in a plain shell on the evidence folder (symlinking each page to `index.html` for `check.py`) and are shown as bang commands inside the session. Claude's sentences are verbatim or lightly display-truncated spans from `transcript.txt`. The source concept's framing (three files gate the build; polished-but-generic defaults) is kept; the concept's Material-Design / drag-and-drop specifics are not asserted (this build produced tailwind-blues + autoplay instead, which is the same argument on different symptoms).

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B03 | The ask, verbatim | PASS | `evidence/ask.txt` | — |
| 2 | B00 | Two Reads, then "I'll build a self-contained sorting simulator with bubble sort and merge sort, comparison highlights, speed control and step-through for class."; Write | PASS | `run-bare.jsonl` (the `ls -la` before the Reads is omitted for height; wording lightly display-truncated within block-width budget) | — |
| 3 | B00, B01 | "Five hundred ninety-five lines" | PASS | `wc -l index.bare.html` → 595 (`verify.txt`) | — |
| 4 | B01 | `check.py` on the bare page → FAIL: font-family / autoplay (setTimeout) / speed slider (input type=range) / more than one button / colours outside DESIGN.md | PASS | `verify.txt` (five FAILs, verbatim) | — |
| 5 | B01 | "twelve colours from the tailwind palette" | PASS | `grep -oE '#[0-9A-F]{6}' index.bare.html \| sort -u \| wc -l` → 12; palette matches Tailwind's slate + accent shades (`verify.txt` and full page inspection) | — |
| 6 | B01 | "Two font families" | PASS | `grep -c 'font-family' index.bare.html` → 2 | — |
| 7 | B01 | "Four buttons" (Shuffle, Play, Step, Reset) | PASS | `grep -oE '<button' index.bare.html \| wc -l` → 4 and page inspection | — |
| 8 | B02 | `wc -l` → 5 / 7 / 7; PROJECT.md's five questions | PASS | `evidence/CLAUDE.md`, `DESIGN.md`, `PROJECT.md`; lines display-truncated at 60 chars | — |
| 9 | B02 | The paraphrase of CLAUDE.md and DESIGN.md in narration | PASS | the files, verbatim in `evidence/` | — |
| 10 | B03 | Reads (PROJECT.md, DESIGN.md, check.py), the plan sentence "I have the constraints. Building a single-file bubble sort simulator: one STEP button, one comparisons counter, bars only, palette locked to the four allowed hex values.", Write, `python3 check.py` → `FAIL: more than one font-family`, Edit×2, `check.py` → PASS | PASS | `run-three.jsonl` (README/ask Reads omitted for height; the second FAIL after the first Edit is elided; CLAUDE.md is auto-loaded, not Read — narration says "reads the three files first", which is true of two by Read and one by auto-load) | — |
| 11 | B03 | "It fixes the page, not the script — twice" | PASS | `run-three.jsonl` shows two Edits between the failing check and the passing check; CLAUDE.md says "fix `index.html`, not the script" | — |
| 12 | B03, B04 | "One hundred eleven lines" | PASS | `wc -l index.three.html` → 111 | — |
| 13 | B04 | Five hex values (#111111 + #6B8E6B + #8B7355 + #D97757 + #F6F1E6); font-family count 1; button count 1; no autoplay / no range slider | PASS | `verify.txt` all five checks | — |
| 14 | BFLOW | Node labels (ask / claude / CLAUDE.md / DESIGN.md / PROJECT.md / index.html / check.py / done) and the "auto-load" vs "Read" edge labels | PASS | node names match `SESSION.md` and the actual files; "auto-load" is Claude Code's documented behaviour for CLAUDE.md and matches this run's tool-use log (no Read call for CLAUDE.md) | — |
| 15 | BSHOW | Four states of the sim (0, 8, 18, 28 comparisons; two green at 8; all green at 28) | PASS | `clips/BSHOW-real-*.png` captured from `evidence/index.three.html` via Chrome headless, then centre-cropped to 1200×675 and scaled to 1920×1080 (crop preserves the sim's layout, removes only the outer cream padding); `media/BSHOW.source.txt` records the exact patch, crop and command. Worst-case bubble sort on n=8 is n(n−1)/2=28 comparisons; the 8/18/28 checkpoints are two green, halfway, all green. | — |
| 16 | BSHOW | "Eight bars" · "The rightmost bar locks in green when its pass is done" | PASS | source JS in `index.three.html`: `var arr = [5,2,8,1,6,3,7,4]` (eight); `if (k >= n - i) b.className = 'bar sorted'` (rightmost-first pass) | — |
| 17 | B05 | Six steps; tally PF 2 · PA 1 · TO 0 · IJ 0 · EI 0 (implicit) | PASS | maps to SESSION.md; the corrections cycle explicitly attributed to Claude (steps 5+6) | — |
| 18 | B06 | Ledger rows ("it did" → run three's plan sentence; "fix the page, not the script" → the two Edits after the failing check) | PASS | `run-three.jsonl`; CLAUDE.md rule | — |
| 19 | BVDT | Verdict lines; "the fix went to the page, not the script" | PASS | rows 4–13 above | — |
| 20 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
| 21 | all | Model/version strings; "Claude Code 2.1.150"; "today (Wed 2026-09-09)" | EXEMPT | not shown or spoken on-screen | — |
| 22 | metadata | Costs ($0.562 / $0.495) | EXEMPT | recorded, not spoken | — |

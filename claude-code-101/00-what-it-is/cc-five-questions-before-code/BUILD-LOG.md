# BUILD-LOG — cc-five-questions-before-code

cc-explainer · Claude Code 101 · tier `00-what-it-is`, film 04 · Liam, in for Bear · built 2026-09-09.

**The experiment.** Same one-sentence ask — "Add avg_temp(readings) to stats.py that returns the average temperature across all readings, and add tests using unittest." — under four fresh headless `claude -p` conditions against a tiny `study-readings` python module (`scratch/`, git repo `fb61bbf`):

1. **Cold** — the ask alone. Claude tried to ask three clarifying questions via `AskUserQuestion`; the tool was outside the allow-list fence and the result registered as a dismissal. Claude proceeded with three unconfirmed defaults, wrote `stats.py` (`avg_temp` skips missing/unparseable temps, raises `ValueError` on empty) and `test_stats.py` (7 tests, all green).
2. **Calibration questions** — the five questions in read-only mode (`Read, Glob, Grep, Bash(ls|cat|wc)` only). Claude read all four files, answered Q1–Q4 tersely, and Q5 surfaced two pivots: (1) empty input semantics, (2) skip malformed temps or raise.
3. **Calibration build** — resumed the same session with Liam's answers (empty → None; skip malformed AND the literal string `NaN` because `float("NaN")` is not a real temperature; include a NaN test). Claude wrote `stats.py` using `math.isfinite` to reject NaN/inf and returning `None` on empty; wrote `test_stats.py` with 8 tests including `test_nan_row_is_skipped`.
4. **Q5 only** — a fresh session with just "what are you uncertain about" in read-only mode. Same two pivots surface, in Claude's own words: "1 and 2 would change the code."

Liam's verify (plain shell against `evidence/production.log`, a 10-row log with three literal `NaN` sensor-dropout rows): the cold build's `avg_temp` returns `nan` (poisoned mean); the calibrated build returns `21.47142857142857`.

**Session artifacts.** Raw stream-json in `evidence/run-{cold,calib-q,calib-build,q5only}.jsonl`; the four built variants in `evidence/stats.{cold,calib}.py` and `evidence/test_stats.{cold,calib}.py`; the reusable prompt template in `evidence/five-questions.txt`. Total Claude API spend: $1.24 across the four runs.

**Deviations from the concept card.** The source card's hypothetical "external stylesheet not inline styles" story is not filmed. It is replaced by a real, checkable NaN-poisoning story from four genuine runs. The framing (five questions in read-only mode; the dangerous moment is when Claude has read files and looks ready to build) is preserved; the pedagogy (Q5 is the workhorse) is a finding of the middle-case Q5-only run.

**Kit note.** CCShell's `mode` prop accepts only `'accept-edits' | 'plan' | 'default'`; the sheet initially used the pseudo-mode `'read-only'` on B03/B05 (matching the read-only fence Liam applied to the sessions), which crashed `renderFooterSpans` with `Cannot read properties of undefined (reading 'split')`. Fixed both to `'default'`; the read-only nature lives in the narration and the tool fence, not the on-screen footer.

**Compile.** Two passes.
- Pass 1: B03/B05 failed (mode enum). Fixed the sheet, cleared `rendered` stamps, deleted the two `media/*.mp4`.
- Pass 2: 13/13 rendered. **All QC gates PASS**: Gate V 0/0/0, GATE T PASS, GATE SHARPNESS PASS (median LV=710.9), GATE BOOKEND PASS, GATE AUDIO PASS (–23.6 dB mean), GATE MASTER PASS (3840×2160 24fps h264), GATE LOUDNESS PASS (–24.19 LUFS, tp=–2.95 dBTP), GATE RECEIPTS PASS.

**Warnings (non-blocking):** SKIN LINT flags B00's `CCSession` cold open ("COLD OPEN LAW wants ClaudeComposerAsk"), which the cc-explainer skill explicitly overrides — GATE BOOKEND accepts CC surfaces for `metadata.skill: "cc-explainer"` and passed. Motion histogram warns `type` at 7/13 (53% > 40% pantry cap) — acceptable for a terminal-first film where session composition is the point.

**Master.** `cc-five-questions-before-code.mp4` — 251.0 s (4:11) · 3840×2160 · 24 fps · h264 · 15.5 MB. Frame reads clean on all dense beats (B00 cold stack, B01 verify, B03 calibration answers, B04 build+production, B06 Boondoggle Score, B07 HumanLedger, BVDT verdict) — all text within CC kit budgets, no overprint, no clipping.

**Not published.** Master stays in this folder. TOPOST only via `post`, only on ask.

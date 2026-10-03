# SESSION.md — cc-five-questions-before-code

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Four fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-09, against the tiny `study-readings` scratch project (`scratch/`, git repo `fb61bbf`). The ask (`evidence/ask.txt`):

```
Add avg_temp(readings) to stats.py that returns the average temperature across all readings, and add tests using unittest.
```

Tools fenced (BUILD runs): `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`. READ-ONLY runs drop `Write, Edit, Bash(python3), Bash(git)`. Raw stream-json in `evidence/run-*.jsonl`; each run's built files in `evidence/stats.<run>.py` and `evidence/test_stats.<run>.py`. Liam's `production.log` (`evidence/production.log`) is NEVER in scratch — it is the real-world fixture Liam runs against each build afterwards.

| Run | Prompt | Session | Turns | Duration | Cost |
|---|---|---|---|---|---|
| **cold** | the ask alone | `8d98c8d9…` | 10 | 67.4 s | $0.419 |
| **calib-q** | five questions, read-only | `64fc2444…` | 6 | 50.3 s | $0.268 |
| **calib-build** | Liam's answers → build now | resume `64fc2444…` | 3 | 52.7 s | $0.296 |
| **q5-only** | just Q5, read-only | `fc699f00…` | 6 | 31.5 s | $0.258 |

## Run: cold (no calibration)

- **TOOL** `Bash` `ls -la` · **Read** `stats.py` · **Read** `README.md` · **Read** `readings.log` · **Read** `ask.txt`
- **CLAUDE:** "Before I code this, a few things are ambiguous — the parser stores values as strings, and there's no obvious 'right answer' for empty input or malformed rows. Let me ask."
- **TOOL** `AskUserQuestion` — three clarifying questions: input shape, empty input, test file location.
- **RESULT** the AskUserQuestion tool was outside the fenced allow-list → tool result "Answer questions?" (a dismissal).
- **CLAUDE:** "The user dismissed the questions rather than answering. I'll proceed with the recommended defaults I proposed."
- **TOOL** `Edit` `stats.py` — adds `avg_temp(readings)` (skips missing/unparseable temps, RAISES `ValueError` on empty).
- **TOOL** `Write` `test_stats.py` — 7 tests: simple average, single reading, `readings.log` fixture, missing key, unparseable string, empty (asserts `raises`), all-invalid (asserts `raises`).
- **TOOL** `Bash` `python3 -m unittest test_stats -v` → **7 tests pass**.

## Run: calibration — the five questions (read-only)

The prompt (Liam types this, verbatim): the five questions from `evidence/five-questions.txt`, with `<TASK>` filled in as "add avg_temp(readings) to stats.py and tests". Fenced tools: `Read, Glob, Grep, Bash(ls|cat|wc)` — no writes, no exec.

- **TOOL** `Bash` `ls -la` · **Read** `README.md` · **Read** `stats.py` · **Read** `readings.log` · **Read** `ask.txt`
- **CLAUDE (Q1):** four files, each named and described in one line.
- **CLAUDE (Q2):** "A tiny stats module over an hourly temperature/humidity log for a study group."
- **CLAUDE (Q3):** "A function in `stats.py` that takes the list `read_log` returns, pulls each item's `temp`, casts to `float`, returns the mean. Plus `test_stats.py` using `unittest`. I'd need to make three small decisions before writing (see Q5)."
- **CLAUDE (Q4):** "`parse()` and `read_log()` (task is additive); `readings.log` (it's data); `README.md` (still accurate)."
- **CLAUDE (Q5):** five sub-questions — the ones that mattered were (1) `avg_temp([])` → `None`/`0.0`/raise? and (2) "skip readings without a valid float temp, or raise on the first bad one?"

## Run: calibration — the build (resume of the same session)

- **LIAM (Answer to Q5):** "Empty → return `None`. Malformed → skip, and skip the row for ANY temp that is not a finite number (that includes the literal string 'NaN' — production logs use it for sensor dropouts, and `float('NaN')` is not a real temperature). Cast to float inside `avg_temp`. Return raw float. Include a test case for a NaN row."
- **TOOL** `Write` `stats.py` — adds `avg_temp` that skips missing / non-numeric / non-finite temps (via `math.isfinite`) and returns `None` on empty.
- **TOOL** `Write` `test_stats.py` — 8 tests, including `test_nan_row_is_skipped` and `test_infinity_is_skipped` and `test_all_unusable_returns_none`.
- **RESULT** "You said read-only until you said 'build it' — you have now, so I wrote both files but didn't run them."

## Run: Q5 only (read-only)

- The single question "what are you uncertain about that I should clarify before we start?"
- **CLAUDE:** "A few things worth pinning down before I write it: (1) empty input, (2) malformed readings (skip or raise?), (3) test file location. Numbers 1 and 2 are the ones I'd rather not guess — the answer changes the code."

## Liam's VERIFY (plain shell in each `scratch-<run>/`; `production.log` copied in from `evidence/` just to test, then removed)

```
> cd scratch-cold && python3 -m unittest test_stats -v
Ran 7 tests in 0.001s
OK
> cp ../evidence/production.log .
> python3 -c "from stats import read_log, avg_temp; r=read_log('production.log'); print('avg=', avg_temp(r))"
avg= nan
> cd ../scratch-calib && python3 -m unittest test_stats -v
Ran 8 tests in 0.000s
OK
> cp ../evidence/production.log .
> python3 -c "from stats import read_log, avg_temp; r=read_log('production.log'); print('avg=', avg_temp(r))"
avg= 21.47142857142857
```

`readings.log` (all-clean fixture) averages `21.45`. `production.log` (three `NaN` rows out of ten) averages `21.47` if you skip them, `nan` if you don't.

## What the runs gave the film

1. **Cold.** Claude noticed the ambiguity and TRIED to ask (`AskUserQuestion`). The fence blocked it. Claude made three unconfirmed decisions and wrote a version that PASSES its own 7 tests — and silently returns `nan` on `production.log`. The dangerous middle: the failure is not a crash, it is a poisoned mean.
2. **Calibration first.** The 5 questions in read-only mode surfaced the same two pivots (empty; malformed) as explicit choices, in Claude's own words. Liam answered them naming NaN specifically. The build was correct on the first pass and gave the right number on `production.log`.
3. **Q5 alone.** Same two pivots surface. Q1–Q4 mostly returned information already visible in the files. **Q5 does the work.** The other four are the ramp that gets Claude ready to ask it honestly.
4. **The pattern.** The five questions are not a courtesy. They convert a silent decision into an explicit one — a decision the human can be wrong about, but not one made in the human's absence.

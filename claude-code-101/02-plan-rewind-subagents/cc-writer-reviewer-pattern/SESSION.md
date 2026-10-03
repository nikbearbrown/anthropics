# SESSION.md — cc-writer-reviewer-pattern

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Three fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-09, same one-sentence ask (`evidence/ask.txt`), three conditions. Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`. Raw stream-json in `evidence/run-{writer,review-same,review-clean}.jsonl`; the code and CSV in `evidence/pass_fail.py`, `evidence/grades.csv`.

## The ask

```
Write pass_fail.py. It reads grades.csv and prints one line per student:
"<name>: PASS" or "<name>: FAIL". Passing is 70.
```

## `grades.csv` — deliberately ambiguous (`evidence/grades.csv`)

```
name,q1,q2,q3
Ada,80,70,72
Ben,60,65,58
Cai,90,,88          ← one missing score
Dee,,,              ← no scores at all
Eli,100,100,40      ← one very low score, high average
```

## Run 1 — writer (session `4837f38e-…`)

`claude -p "<ask>" --session-id … --permission-mode acceptEdits`

- **TOOL** `Bash ls scratch/` · **TOOL** `Read grades.csv` · **TOOL** `Write pass_fail.py` · **TOOL** `Bash python3 pass_fail.py`
- Output on the sample:
  ```
  Ada: PASS
  Ben: FAIL
  Cai: PASS
  Dee: FAIL
  Eli: PASS
  ```
- **CLAUDE:** "Written and verified. `pass_fail.py` reads `grades.csv`, averages the non-blank quiz scores per student, and prints PASS/FAIL against the 70 threshold. Missing-all-scores (Dee) is treated as FAIL; note Eli passes on the mean (80) despite one very low score — let me know if you'd rather require every quiz to clear 70."
- **RESULT:** success · turns 5 · 26.0 s · $0.230

`evidence/pass_fail.py` (11 lines):

```python
import csv

with open("grades.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["name"]
        if not name:
            continue
        scores = [int(row[q]) for q in ("q1", "q2", "q3") if row[q]]
        avg = sum(scores) / len(scores) if scores else 0
        print(f"{name}: {'PASS' if avg >= 70 else 'FAIL'}")
```

## Run 2 — same-context review (`--resume 4837f38e-…`)

Prompt: "Please carefully review pass_fail.py for correctness. Point out any bugs, edge cases, or design choices you'd change. Be blunt — I'd rather hear a problem than a compliment."

**CLAUDE (verbatim, first two sentences and section headers):**

> "Fair. Reviewing my own code with a cold eye:
> **Spec ambiguity I papered over** — 'Passing is 70' is ambiguous and I never asked. I picked *average ≥ 70*. …
> **Missing-data handling is quietly wrong** — Cai has (90, blank, 88) → I average only the two present → PASS. …
> **Fragility** — `int(row[q])` crashes on `"85.5"` … Column names `q1/q2/q3` are hardcoded. …
> **What I'd actually change first**: ask you which passing rule you meant, and how blanks should count."

- Framing verb-by-verb: **I** picked, **I** never asked, **I** average only the two present, **I** papered over.
- No tools used. One text turn.
- **RESULT:** success · turns 1 · 31.0 s · $0.179

## Run 3 — clean-context review (`72948a3b-…`, fresh working dir with only the four files)

Copied `pass_fail.py`, `grades.csv`, `README.md`, `ask.txt` to `/private/tmp/clean-review/`; fresh `claude -p` there, same prompt.

- **TOOL** `Bash ls` · **TOOL** `Read pass_fail.py` · **TOOL** `Read grades.csv` · **TOOL** `Read README.md` · **TOOL** `Read ask.txt`
- **CLAUDE (verbatim, first two sentences and section headers):**

> "Reviewed against `grades.csv` and `ask.txt`. Blunt findings:
> **Real bugs**
> 1. **Dee gets `FAIL` despite not taking a single quiz.** `pass_fail.py:10` — when `scores` is empty, `avg` falls back to `0`. That's almost certainly wrong; a student with no scores should be skipped or reported as `N/A`.
> 2. **Missing-quiz semantics chosen silently, and it flips outcomes.** `pass_fail.py:9` skips empty cells, so Cai's average is 89 → PASS. If missing means 'didn't hand it in = 0', Cai's average is 59.3 → FAIL. Nothing in `ask.txt` says which is right.
> 3. **Eli (100/100/40) passes with avg 80.** Fine if the rule is 'average ≥ 70' — but if the intent is 'pass every quiz', Eli should FAIL.
> **Fragility** — `int(row[q])` raises `ValueError` with no row/name in the traceback. `row['name']` will `KeyError` if headers drift. `if not name` catches `''` but not `'   '`.
> **What I'd change first:** fix #1 (don't call Dee a failure), then get an answer on #2 before shipping."

- Framing verb-by-verb: **Dee gets** FAIL, **Cai's** average, **the rule**, **the intent** — third-person about the code and its callers. Never "I".
- Reads the file cold and re-derives the arithmetic (Cai's average is 89; would flip to 59.3 with zero-substitution).
- **RESULT:** success · turns 6 · 55.5 s · $0.237

## Liam's VERIFY (`evidence/`)

```
> wc -l pass_fail.py
      11 pass_fail.py
> python3 pass_fail.py
Ada: PASS
Ben: FAIL
Cai: PASS
Dee: FAIL
Eli: PASS
> grep -c "^I " /dev/stdin < same_review.txt          # first-person "I " lines
6
> grep -c "^I " /dev/stdin < clean_review.txt         # first-person "I " lines
0
> grep -c "^\s*[0-9]\." clean_review.txt              # numbered findings
3
> grep -o "pass_fail.py:[0-9]*" clean_review.txt      # line-cited findings
pass_fail.py:10
pass_fail.py:9
pass_fail.py:7
```

## What the runs gave the film

1. **Both** reviewers found the load-bearing issues (Dee-as-FAIL, missing-quiz semantics, Eli-on-average). Same model, same weights.
2. **Only the clean-context review cited line numbers** and re-derived Cai's flipped average from the file. It couldn't rely on remembered reasoning, so it re-computed. The receipt is `pass_fail.py:9`, `pass_fail.py:10`, `59.3`.
3. **Only the same-context review framed the findings as its own decisions.** Six of its paragraphs begin with "I"; every finding is a paperwork item about *what I chose*. The clean-context review has zero "I" openings and orders findings by severity — **Real bugs** first, then **Fragility**.
4. The difference the film pays off is not "clean catches what same misses" — both caught it. It is **who the reviewer thinks they are.** Same context reviews the *writer*. Clean context reviews the *code*. The starting context decides which question the reviewer asks.

# PROMPTS — cc-five-questions-before-code

The exact strings sent to `claude -p` during the four sessions this reel reconstructs. Recorded as evidence for REAL-SESSION LAW.

## Run: cold

```
Add avg_temp(readings) to stats.py that returns the average temperature across all readings, and add tests using unittest.
```

## Run: calibration — the five questions (read-only)

```
Before I ask you to build anything, please answer these five questions in read-only mode. Read files, but do not write, edit, or run anything. Give me short answers.

1. What files do you see in this project and what is each for?
2. What do you think this project is for?
3. If I asked you to add avg_temp(readings) to stats.py and tests, what would you write?
4. What would you not touch?
5. What are you uncertain about that I should clarify before we start?
```

## Run: calibration — the build (resume)

```
Good questions. Answers:

1. Empty input → return None.
2. Malformed temp → SKIP the row, and skip the row for ANY temp that is not a finite number (that includes the literal string "NaN" — production logs use it for sensor dropouts, and float("NaN") is not a real temperature).
3. Cast to float inside avg_temp — leave parse alone.
4. test_stats.py next to stats.py, unittest.
5. Return raw float.

Now build it. Include a test case for a NaN row in the log.
```

## Run: Q5 only

```
Before I ask you to build anything, one question in read-only mode: what are you uncertain about that I should clarify before we start? Read files, do not write or run anything. Short answer.
```

## Tool fences

- BUILD runs (cold, calib-build): `--allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)"`
- READ-ONLY runs (calib-q, q5-only): `--allowedTools "Read,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(wc:*)"`
- Every run: `--output-format stream-json --verbose --max-turns 16 --permission-mode acceptEdits --strict-mcp-config < /dev/null`

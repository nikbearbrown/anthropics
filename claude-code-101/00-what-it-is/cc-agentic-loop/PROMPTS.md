# PROMPTS — cc-agentic-loop

The two headless invocations that produced the reel's evidence.

## The ask (both runs, verbatim)

```
Fix the bug in calc.py, add a test that would have caught it, and run the tests.
```

Source: `evidence/before/ask.txt` (single line).

## Run 1 — acceptEdits (the loop, unattended)

```bash
cd scratch
claude -p "Fix the bug in calc.py, add a test that would have caught it, and run the tests." \
  --output-format stream-json --verbose --max-turns 16 \
  --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../evidence/run-loop.jsonl 2> ../evidence/run-loop.stderr
```

- Session id `e588ab67-6a59-4ec0-b490-fc1e4412be50`
- Result: `subtype=success · turns=8 · 38376 ms · $0.2944`
- Tool calls: 7 (Bash × 2, Read × 3, Edit × 2)
- Files edited in `scratch/`: `calc.py`, `test_calc.py`
- Tests after: `Ran 4 tests in 0.000s — OK`

## Run 2 — plan (the loop, interrupted)

Before run 2:

```bash
cd scratch
git reset --hard pristine
rm -rf __pycache__
```

Then, one flag change (`--permission-mode plan`), everything else identical:

```bash
claude -p "Fix the bug in calc.py, add a test that would have caught it, and run the tests." \
  --output-format stream-json --verbose --max-turns 16 \
  --permission-mode plan --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > ../evidence/run-plan.jsonl 2> ../evidence/run-plan.stderr
```

- Session id `124b4a22-…`
- Result: `subtype=success · turns=8 · 40790 ms · $0.2233`
- Tool calls: 3 Reads · 1 Write (`~/.claude/plans/…md`) · 1 ExitPlanMode (waits)
- Files edited in `scratch/`: **0** — verified by `git status --short` empty after the run

## YOUR-TURN — the viewer's prompt (BHTF)

```
Before your next non-trivial edit in Claude Code, press Shift+Tab twice to enter plan mode.
Type your ask. Read what Claude proposes. Then approve it, or edit the plan first.
Do it once. Notice how much of the loop you would have missed.
```

# PROMPTS — cc-writer-reviewer-pattern

The three real headless prompts (verbatim; the exact strings that produced the receipts in `evidence/`).

## Run 1 — writer

```
Write pass_fail.py. It reads grades.csv and prints one line per student:
"<name>: PASS" or "<name>: FAIL". Passing is 70.
```

Flags: `--session-id <uuid> --output-format stream-json --verbose --max-turns 16 --permission-mode acceptEdits --strict-mcp-config --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)"`

## Run 2 — same-context review (`--resume <writer uuid>`)

```
Please review pass_fail.py for correctness. Point out any bugs, edge cases, or
design choices you'd change. Be blunt — I'd rather hear a problem than a compliment.
```

Same flags, minus `--session-id`, plus `--resume <writer uuid>`.

## Run 3 — clean-context review (fresh `--session-id`)

Same prompt as Run 2, in `/private/tmp/clean-review/` (copies of `pass_fail.py`, `grades.csv`, `README.md`, `ask.txt` only — nothing else, no history).

## The viewer's prompt (BHTF)

```
Before your next code review, open two terminals. Resume the session that wrote
the code and ask it to review the file, be blunt. Then a fresh claude -p with a
new session id, in a folder that has only the file and the spec, same prompt.
Paste the two answers side by side and circle every "I" opening on one side and
every line cite on the other.
```

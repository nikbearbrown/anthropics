# PROMPTS — cc-rewind-not-fix-forward

Every `claude -p` command the reel reconstructs. Tools fenced to `Read, Write, Edit, Glob, Grep` plus `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`. Session ids in `evidence/sid-{bare,rewind}.txt`.

## bare — fresh session

```bash
claude -p "$(cat ask.txt)" \
  --session-id 727cb81b-e2a3-4e33-9f8c-d74c8f8d3867 \
  --output-format stream-json --verbose \
  --max-turns 12 \
  --permission-mode acceptEdits \
  --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > evidence/run-bare.jsonl
```

`ask.txt` — the bare prompt:

```
Write a small Python module todos.py with two functions:
- remove_completed(todos) — remove completed items and return the result
- mark_all_done(todos) — mark every todo as done and return the result
Include tests in test_todos.py using unittest.
```

## fixforward — correction #1 (`--resume`)

```bash
claude -p "Actually, please switch todos.py to use a dataclass called Todo with fields text: str and done: bool. Update remove_completed so it works on Todo instances. Keep the tests working." \
  --resume 727cb81b-e2a3-4e33-9f8c-d74c8f8d3867 \
  --output-format stream-json --verbose \
  --max-turns 16 --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > evidence/run-fixforward.jsonl
```

## fixforward2 — correction #2 (`--resume`)

```bash
claude -p "Also, remove_completed should accept an optional keep(t) predicate so callers can filter by their own rule. Default it to keeping items where not t.done. Update just remove_completed for this — leave mark_all_done alone." \
  --resume 727cb81b-e2a3-4e33-9f8c-d74c8f8d3867 \
  --output-format stream-json --verbose \
  --max-turns 16 --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > evidence/run-fixforward2.jsonl
```

## rewind — headless equivalent (fresh session)

```bash
claude -p "$BETTER" \
  --session-id 5f9cb45f-8eb3-459a-b0bc-febebbe206af \
  --output-format stream-json --verbose \
  --max-turns 12 --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > evidence/run-rewind.jsonl
```

Where `BETTER` is:

```
Write a small Python module todos.py.
A todo is a dataclass Todo(text: str, done: bool).
Provide:
- filter_todos(todos, keep) — return a new list keeping items where keep(t) is True (immutable)
- mark_all_done(todos) — return a new list with every item marked done (immutable)
Include unittest tests in test_todos.py that assert the original list is unchanged and cover the general filter.
```

## The viewer's prompt (BHTF)

```
I'm about to paste a correction. Before I do, ask me three questions: what was missing from the original ask, what would the ask look like with that sentence added, and would rewinding cost less than fix-forwarding. Then wait — don't touch any file.
```

# SESSION.md — cc-rewind-not-fix-forward

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Four headless
`claude -p` runs, Claude Code 2.1.150, 2026-09-09, on a scratch folder
`scratch/bare/` and `scratch/rewind/`. Tools fenced to `Read, Write, Edit, Glob,
Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`. Raw stream-json in
`evidence/run-{bare,fixforward,fixforward2,rewind}.jsonl`; harvested text
`evidence/text-*.txt`; final files `evidence/todos.{fixforward,rewind}.py`,
`evidence/test_todos.{fixforward,rewind}.py`; session ids in `evidence/sid-*.txt`.

**Headless caveat (BUILD-SHOW LAW note).** The film's true subject —
Esc-Esc / `/rewind` in the interactive UI — cannot be filmed from a headless
session; there is no rewind command in `claude -p`. The film uses its
headless equivalent: a new `--session-id` with a respecified ask is what a
rewind + respec produces. What CAN be filmed cleanly is the fix-forward path
(with `--resume`), so the film compares three fix-forward turns against one
respecified fresh session — the same shape a rewind produces.

## The ask (bare)

```
Write a small Python module todos.py with two functions:
- remove_completed(todos) — remove completed items and return the result
- mark_all_done(todos) — mark every todo as done and return the result
Include tests in test_todos.py using unittest.
```

## Run: bare (session `727cb81b-…`, no `--resume`)

- **TOOL** `Bash` `pwd && ls` · **Write** `todos.py` (6 lines) · **Read**
  `check_immutable.py` · **Read** `ask.txt` · **Write** `test_todos.py`
  (63 lines, 9 tests) · **Bash** `python -m unittest test_todos.py -v` (denied
  by fence — `python` not in allow-list; the reel uses `python3`)
- **CLAUDE:** "Created both files. The implementations are non-mutating (new
  list + new dicts), which also satisfies the `check_immutable.py` script
  sitting in this scratch folder."
- **RESULT:** success · turns=8 · 48.1 s · $0.440 · output 2 253 tokens

State written to `scratch/bare/todos.py`:

```python
def remove_completed(todos):
    return [t for t in todos if not t.get("done")]

def mark_all_done(todos):
    return [{**t, "done": True} for t in todos]
```

## Run: fixforward — correction #1 (dataclass), `--resume 727cb81b-…`

- **Corrective prompt:** "Actually, please switch todos.py to use a dataclass
  called Todo with fields text: str and done: bool. Update remove_completed so
  it works on Todo instances. Keep the tests working."
- **TOOL** `Write` `todos.py` (14 lines) · **Write** `test_todos.py` (57 lines,
  8 tests; the `test_preserves_other_fields` case was dropped because the
  dataclass locks the fields)
- **CLAUDE:** "Done. Both files use the `Todo` dataclass; `mark_all_done` uses
  `dataclasses.replace` so it stays non-mutating." — and then, unprompted:
  **"Heads-up: `check_immutable.py` in this folder feeds dicts into the
  module, so it will now fail with `AttributeError` — the external checker
  was written to the old dict shape."**
- **RESULT:** success · turns=3 · 30.9 s · $0.335 · output 2 078 tokens

Claude flagged the fix-forward's own stranded contract inside the same turn:
the external check script — the definition of done written before the
session — no longer runs against the corrected module because the correction
changed the type shape mid-conversation.

## Run: fixforward2 — correction #2 (predicate), `--resume 727cb81b-…`

- **Corrective prompt:** "Also, remove_completed should accept an optional
  keep(t) predicate so callers can filter by their own rule. Default it to
  keeping items where not t.done. Update just remove_completed for this —
  leave mark_all_done alone."
- **TOOL** `Edit` `todos.py` · **Edit** `test_todos.py`
- **CLAUDE:** "Added `keep` as an optional predicate — defaults to
  `lambda t: not t.done` so existing callers see no change. Added one test
  covering a custom predicate; `mark_all_done` untouched."
- **RESULT:** success · turns=3 · 18.9 s · $0.113 · output 1 003 tokens

Final `scratch/bare/todos.py`:

```python
from dataclasses import dataclass, replace

@dataclass
class Todo:
    text: str
    done: bool

def remove_completed(todos, keep=None):
    if keep is None:
        keep = lambda t: not t.done
    return [t for t in todos if keep(t)]

def mark_all_done(todos):
    return [replace(t, done=True) for t in todos]
```

The name drift is in the tests: `test_todos.py:36–45` (the `test_custom_keep_predicate`
case) calls **`remove_completed(todos, keep=lambda t: len(t.text) > 1)`** and
expects the result to KEEP `Todo(text="ccc", done=True)`. The function whose name
is "remove completed" is being called with a rule that keeps a completed one.
The signature drifted; the tests document it.

## Run: rewind — the headless equivalent (session `5f9cb45f-…`, no `--resume`)

Same requirements, one respecified prompt from a fresh session — no residue:

```
Write a small Python module todos.py.
A todo is a dataclass Todo(text: str, done: bool).
Provide:
- filter_todos(todos, keep) — return a new list keeping items where keep(t) is True (immutable)
- mark_all_done(todos) — return a new list with every item marked done (immutable)
Include unittest tests in test_todos.py that assert the original list is unchanged and cover the general filter.
```

- **TOOL** `Write` `todos.py` (13 lines) · **Write** `test_todos.py` (64
  lines, 10 tests) · **Bash** `python -m unittest test_todos.py -v` (denied
  by fence — `python`, not `python3`) · **Bash** `python -m unittest
  test_todos.py -v` (retried, same fence)
- **CLAUDE:** "I'll create the module and its tests in the current working
  directory. Both files written. `todos.py` defines `Todo` as a dataclass and
  provides `filter_todos` (list comprehension over `keep`) and
  `mark_all_done`."
- **RESULT:** success · turns=5 · 26.6 s · $0.359 · output 2 119 tokens

Final `scratch/rewind/todos.py`:

```python
from dataclasses import dataclass, replace
from typing import Callable, List

@dataclass
class Todo:
    text: str
    done: bool

def filter_todos(todos: List[Todo], keep: Callable[[Todo], bool]) -> List[Todo]:
    return [t for t in todos if keep(t)]

def mark_all_done(todos: List[Todo]) -> List[Todo]:
    return [replace(t, done=True) for t in todos]
```

The name matches the behaviour. The signature has type hints. The tests
(10) explicitly assert immutability and cover an "always true" predicate.

## Liam's VERIFY (plain shell, run against evidence/)

```
> wc -l evidence/todos.fixforward.py evidence/todos.rewind.py
      17 evidence/todos.fixforward.py
      16 evidence/todos.rewind.py
> grep -n 'def ' evidence/todos.fixforward.py
10:def remove_completed(todos, keep=None):
16:def mark_all_done(todos):
> grep -n 'def ' evidence/todos.rewind.py
11:def filter_todos(todos: List[Todo], keep: Callable[[Todo], bool]) -> List[Todo]:
15:def mark_all_done(todos: List[Todo]) -> List[Todo]:
> grep -n 'keep=lambda' evidence/test_todos.fixforward.py
43:            remove_completed(todos, keep=lambda t: len(t.text) > 1),
> python3 -m unittest test_todos -v      # inside scratch/bare
Ran 9 tests in 0.000s
OK
> python3 -m unittest test_todos -v      # inside scratch/rewind
Ran 10 tests in 0.000s
OK
```

Both final states pass their own tests. The difference is not correctness —
it is the shape of the code and the shape of the transcript that produced it.

## Turns, seconds, cost — the two paths

| Path | Sessions | Turns | Time | Cost | End state |
|---|---:|---:|---:|---:|---|
| Fix-forward (bare + 2 corrections, all `--resume`) | 1 | 14 | 97.9 s | $0.888 | `remove_completed(keep=None)` — name lies |
| Rewind (fresh session, respecified ask) | 1 | 5 | 26.6 s | $0.359 | `filter_todos(keep)` — name matches |

Rewind is 2.5× cheaper and half the wall time. The lasting difference is a
function whose name will read like a lie every time somebody opens the file.

## What the runs gave the film

1. Fix-forward's first move produced clean immutable code — a fine default.
   The corrections were the problem, because each one joined the transcript
   without removing the shape it was correcting.
2. Correction #1 was reasonable and Claude even flagged the collateral
   damage in the same turn (the external `check_immutable.py` contract
   broke). Fix-forward doesn't hide the damage — it just leaves it there.
3. Correction #2 asked for narrowly scoped work ("just `remove_completed`")
   and got it. The narrow scope is precisely the smell: the function is
   named for what it USED to be, not what it does now, and the test file
   documents the drift on line 43.
4. Rewind's respecified prompt names the function honestly from the start
   (`filter_todos`) because the person writing the prompt has learned what
   they wanted. The context is short; no misunderstanding to carry.

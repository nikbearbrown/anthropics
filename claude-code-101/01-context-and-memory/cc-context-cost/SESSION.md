# SESSION.md — cc-context-cost

The real Claude Code session this reel reconstructs (REAL-SESSION LAW). One headless session, Claude Code 2.1.150, 2026-09-09, resumed for each message (`--session-id` then `--resume`), on the `gradebook` repo from `cc-claude-md` (CLAUDE.md present, 17 lines). Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`. Eight messages of real work (`evidence/ask1.txt` … `ask8.txt`), then `/compact` (message 9), the same question again (10), the same question in a fresh session (11), and `/context` (12) — the last four are the evidence for the two sibling films (`cc-clear-vs-compact`, `cc-context-check`). Raw stream-json per message: `evidence/turn*.jsonl`; per-call context sizes: `evidence/turns.json`; harvested transcript with the context read at every call: `evidence/transcript.txt`; the session's code diff: `evidence/session.diff`.

**How "context read" is measured.** Every assistant message in the stream carries `usage`; the context read for that call is `input_tokens + cache_read_input_tokens + cache_creation_input_tokens`. "First call" is the first model call of the message — the size of the session the moment your new line arrives.

## The eight messages

| msg | Liam typed | first-call context | calls | tool calls | out tokens | wall | cost |
|---|---|---|---|---|---|---|---|
| 1 | Read src/gradebook.py and tell me in two sentences what it does. | 28,450 | 3 | 1 | 275 | 6.9 s | $0.113 |
| 2 | Add a "rename OLD NEW" command following the repo's conventions, with a test. Run the tests. | 29,283 | 7 | 5 | 1,777 | 25.9 s | $0.231 |
| 3 | Add a "top N" command that prints the N students with the highest average, with a test. Run the tests. | 32,237 | 8 | 4 | 1,661 | 24.2 s | $0.232 |
| 4 | Add a "export" command that writes grades.csv, with a test. Run the tests. | 34,576 | 9 | 6 | 2,099 | 29.9 s | $0.309 |
| 5 | Refactor: load() and save() are called in every command. Is there a cleaner pattern that keeps the behaviour identical? Just answer, don't change anything. | 38,311 | 2 | 0 | 607 | 12.2 s | $0.164 |
| 6 | Now apply that refactor, keep every test green, and run the tests. | 38,964 | 6 | 3 | 7,897 | 102.3 s | $0.467 |
| 7 | Add a "stats NAME" command printing count, mean, min, max, with a test. Run the tests. | 47,283 | 6 | 4 | 1,559 | 23.4 s | $0.353 |
| 8 | What did we build in this session? One line per command. | 49,530 | 1 | 0 | 183 | 6.3 s | $0.224 |

Last-call context per message: 29,137 · 32,042 · 34,391 · 38,075 · 38,311 · 47,071 · 49,352 · 49,530. Message 8's single call: `cache_read` 15,744 · `cache_creation` 33,780 · `input` 6 · `output` 183.

Claude's answers (verbatim, trimmed):

- msg 1: "A tiny CLI gradebook that persists students and their scores to a `grades.json` file in the working directory, reloading and rewriting the whole file on every command. …"
- msg 2: "All 3 tests pass. Added `rename(old, new)` in `src/gradebook.py:39` (mirrors `remove`'s error style, plus an "already exists" guard) …"
- msg 3: "All 4 tests pass. Added `top(n)` in `src/gradebook.py:51` …" · msg 4: "All 5 tests pass. Added a `CSV = Path("grades.csv")` module constant … and `export()` …"
- msg 5: "A `@contextmanager` `session()` that yields `load()` and calls `save()` on exit is the natural fit …"
- msg 6: "All 5 tests still pass. `add`/`score`/`remove`/`rename` now each open a `with session() as data:` block …"
- msg 7: "All 6 tests pass. Added `stats(name)` in `src/gradebook.py:79` …"
- msg 8: "- `rename OLD NEW` — moves a student's scores to a new name, guarding against missing source and existing destination. / - `top N` — prints the N students with the highest averages, in descending order. / - `export` — writes `grades.csv` (name, average, scores) via the stdlib `csv` module. / - `stats NAME` — prints count, mean, min, max for one student, with guards for missing student and empty scores. / - Refactor: introduced a `session()` context manager so mutating commands share one load-mutate-save block and only write when the dict actually changed."

### Liam's VERIFY (plain shell)

```
> python3 tests/test_gradebook.py
Ran 6 tests in 0.004s
OK
> git diff --stat
 src/gradebook.py        |  …
 tests/test_gradebook.py |  …
 2 files changed, 174 insertions(+), 13 deletions(-)
> python3 -c "…turns.json…"          # first-call context per message
msg 1  28,450   msg 2  29,283   msg 3  32,237   msg 4  34,576
msg 5  38,311   msg 6  38,964   msg 7  47,283   msg 8  49,530
> python3 -c "…"                     # the ratio the slogan is about
msg 8 / msg 1 context read: 49,530 / 28,450 = 1.74×
msg 8 / msg 1 cost:         $0.224 / $0.113 = 1.98×
```

Finding: the mechanism the slogan describes is real and visible — every message's first call reads the whole session so far, and the session only grows (28k → 49.5k over eight messages; message 6's 7,897 tokens of refactor output are re-read by every message after it). The multiplier is not: in this session message 8 read 1.7× and cost 2× what message 1 did, because most of a growing session is cache (`cache_read` 15,744 of the 49,530 on message 8's call, the rest `cache_creation`). The slogan overstates the bill and gets the mechanism right.

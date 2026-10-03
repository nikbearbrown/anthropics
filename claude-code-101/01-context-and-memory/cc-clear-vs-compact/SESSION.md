# SESSION.md — cc-clear-vs-compact

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Messages 9–11 of the session recorded in `../cc-context-cost/SESSION.md` (same session id, Claude Code 2.1.150, 2026-09-09, `gradebook` repo): after eight messages of real work the context read had reached 49,530 tokens. Raw stream-json: `evidence/turn9.jsonl` (`/compact`), `turn10.jsonl` (the same question after compact), `turn11-fresh.jsonl` (the same question in a brand-new session — what `/clear` gives you); per-call context in `evidence/turns.json`; the full transcript in `evidence/transcript.txt`.

## Message 9 — `/compact` (resumed session)

**Liam typed:** `/compact`

Stream events (verbatim keys):

```
{"type": "system", "subtype": "status", "status": "compacting"}
{"type": "system", "subtype": "status", "status": null, "compact_result": "success"}
{"type": "system", "subtype": "compact_boundary", "compact_metadata": {"trigger": "manual", "pre_tokens": 49713, "post_tokens": 6100, "duration_ms": 57048}}
```

- **RESULT:** success · num_turns=0 · 57.1 s · $0.352 (the summary is written by the model; no tool calls)

## Message 10 — the same question, after compact (resumed session)

**Liam typed:** `What did we build in this session? One line per command.`

- first-call context: **36,670** (down from 49,530 at message 8); one call; no tools
- **CLAUDE:** - `rename OLD NEW` — moves a student's scores to a new name, with guards for missing source and name collision. / - `top N` — prints the N students with the highest average, sorted descending. / - `export` — writes `grades.csv` with name/average/scores columns via the stdlib `csv` module. / - `stats NAME` — prints count, mean, min, max for one student, with "no scores" and "no such student" guards. / - `session()` refactor — a `contextmanager` that wraps load → yield → save-if-changed, so mutating commands share one transactional block.
- **RESULT:** success · num_turns=1 · 8.9 s · $0.143 · output 186

## Message 11 — the same question in a fresh session (what `/clear` gives you)

**Liam typed (new `claude -p`, no `--resume`):** `What did we build in this session? One line per command.`

- first-call context: **28,676** (the fixed part only: system prompt, tools, CLAUDE.md — no conversation)
- **TOOL** `Bash` `git diff src/gradebook.py` · **TOOL** `Bash` `git diff tests/test_gradebook.py`
- last-call context: 32,093 (after reading the two diffs)
- **CLAUDE:** Here's what was built in this session: / - `rename OLD NEW` — rename a student, guarding against missing source and existing destination. / - `top N` — print the top N students by average, highest first. / - `stats NAME` — print count/mean/min/max for one student's scores. / - `export` — write all students to `grades.csv` (name, average, space-joined scores). / - `session()` context manager — load once, save only if the dict actually changed; `add`/`score`/`remove` refactored onto it. / - Tests added for each new command (`test_rename`, `test_top`, `test_export`, `test_stats`), each swapping `gradebook.DB` (and `CSV` for export) to a temp path.
- **RESULT:** success · num_turns=3 · 14.7 s · $0.136 · output 469

Note: in headless mode `/clear` has no meaning (each `claude -p` is already a fresh conversation); a new session is exactly what `/clear` produces in the interactive product — the transcript gone, the working directory and CLAUDE.md unchanged. Recorded as the honest equivalent.

### Liam's VERIFY (plain shell, `evidence/` and the repo)

```
> python3 -c "…turns.json…"
msg 8   (before)             49,530
msg 10  (after /compact)     36,670
fresh   (what /clear gives)  28,676  →  32,093 after two git diffs
> python3 tests/test_gradebook.py
Ran 6 tests in 0.004s
OK
> git diff --stat | tail -1
 2 files changed, 174 insertions(+), 13 deletions(-)
```

Finding: `/compact` replaced 49,713 tokens of conversation with a 6,100-token summary in 57 s; the next question was answered from the summary (same five items) at 36,670 context. The fresh session started at 28,676 with no memory of the work, ran `git diff` twice, and answered from the disk — and its answer included the tests, which the summary-based answer had not mentioned. Neither command touched the disk: six tests green, the same 174 lines added.

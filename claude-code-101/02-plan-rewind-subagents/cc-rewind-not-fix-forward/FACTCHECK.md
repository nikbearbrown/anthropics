# FACTCHECK — cc-rewind-not-fix-forward

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (four real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the four runs' stream-json (`evidence/run-{bare,fixforward,fixforward2,rewind}.jsonl`), the four harvested transcripts (`text-*.txt`), and the final files (`todos.{fixforward,rewind}.py`, `test_todos.{fixforward,rewind}.py`). Claude's sentences are verbatim spans; Liam's plain-shell verifies were run on `evidence/`. The source concept's framing (fix-forward joins the misunderstanding; rewind removes it; andon-cord metaphor) is kept; its splice / mutation anecdote is not reused, because the real headless run produced clean immutable code and the film would not have been honest to keep that claim.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B04 | `10:def remove_completed(todos, keep=None):` and `16:def mark_all_done(todos):` | PASS | `grep -n 'def ' evidence/todos.fixforward.py` | — |
| 2 | B00 | `43:  remove_completed(todos, keep=lambda t: len(t.text) > 1),` KEEPS a `done=True` Todo | PASS | `evidence/test_todos.fixforward.py:36–45`; the expected list `[Todo(text="bb", done=False), Todo(text="ccc", done=True)]` on L42 contains `done=True` | — |
| 3 | B00, B07, BVDT | "two-and-a-half times the cost" | PASS | `$0.888 / $0.359 = 2.47×`; time `97.9 s / 26.6 s = 3.68×`; turns `14 / 5 = 2.8×` | — |
| 4 | B01 | The bare ask (verbatim) | PASS | `evidence/ask.txt` | — |
| 5 | B01 | Bash `pwd && ls`, Read `check_immutable.py`, Read `ask.txt`, Write `todos.py`, Write `test_todos.py`; "9 tests, all green" | PASS | `run-bare.jsonl` tool_use sequence; `test_todos.py:1–68` has 9 test methods; `unittest test_todos` → 9 passing | — |
| 6 | B01 | "six lines, sixty-three lines of tests" | PASS | in `run-bare.jsonl` Claude Wrote `todos.py` (6 lines) and `test_todos.py` (63 lines) before the fixforward correction overwrote them; captured in `evidence/todos.bare.snapshot.txt` | — |
| 7 | B02 | The `--resume` prompt text, verbatim: "switch todos.py to a Todo dataclass" | PASS | `run-fixforward.jsonl` user message; on-screen text is display-truncated for width | — |
| 8 | B02 | Claude's unprompted flag: "check_immutable.py will now AttributeError" | PASS | `text-fixforward.txt`: "Heads-up: `check_immutable.py` in this folder feeds dicts into the module, so it will now fail with `AttributeError` — the external checker was written to the old dict shape." | — |
| 9 | B03 | `Edit todos.py`, `Edit test_todos.py`; the description "default lambda t: not t.done; mark_all_done untouched" | PASS | `run-fixforward2.jsonl` tool_use sequence; `text-fixforward2.txt`: "Added `keep` as an optional predicate — defaults to `lambda t: not t.done` … `mark_all_done` untouched." | — |
| 10 | B03, B04 | "test on L43 uses keep by length — expected result KEEPS a done one" | PASS | `evidence/test_todos.fixforward.py:43` calls `remove_completed(todos, keep=lambda t: len(t.text) > 1)` and the expected list includes `Todo(text="ccc", done=True)` | — |
| 11 | B04 | `wc -l` → `17` `todos.py`, `67` `test_todos.py`; `unittest` → "Ran 9 tests" OK | PASS | `wc -l evidence/todos.fixforward.py evidence/test_todos.fixforward.py`; `python3 -m unittest test_todos` inside `scratch/bare` passes 9 cases | — |
| 12 | B05 | "Esc-Esc or /rewind" as the interactive-UI rewind mechanic | PASS | product concept per the source `beat_sheet.json` metadata `description_blurb` and Claude Code 2.1.150 UI; not filmed inside the terminal because headless has no rewind command (BUILD-SHOW LAW note in SESSION.md) | — |
| 13 | B05, B06 | "new session-id, no --resume" is the headless equivalent of rewind | PASS | `run-rewind.jsonl` starts with `--session-id 5f9cb45f-…` and no `--resume` flag; SESSION.md documents this substitution | — |
| 14 | B06 | The respecified ask, the two Writes, "5 turns, one shot", "10 tests" | PASS | `run-rewind.jsonl` result `num_turns=5`; tool_use has two `Write`s; `test_todos.rewind.py` has 10 test methods | — |
| 15 | B06, B07 | End state — `filter_todos(todos: List[Todo], keep: Callable[[Todo], bool])` and `mark_all_done(todos: List[Todo])` | PASS | `grep -n 'def ' evidence/todos.rewind.py` | — |
| 16 | B07, BVDT | Fix-forward `14 turns, 97.9 s, $0.888` and rewind `5 turns, 26.6 s, $0.359` | PASS | Sum of `num_turns` / `duration_ms` / `total_cost_usd` from the three fix-forward `result` events (8+3+3 turns; 48137+30879+18945 ms = 97.961 s; 0.43974+0.33546+0.11254 = 0.88774); rewind from `run-rewind.jsonl` result event | — |
| 17 | B08 | The Boondoggle steps map to the actual session actions | PASS | steps 1–7 trace to: the bare ask (evidence/ask.txt) → run-bare → the two --resume prompts → the two corrections → the drift I noticed → the respec ask (SESSION.md) → run-rewind | — |
| 18 | B09 | Ledger rows: "flag stranded contracts unprompted" → Claude's Heads-up in B02; "accept resume, guess plausibly" → the two --resume Writes | PASS | `text-fixforward.txt`; `run-fixforward.jsonl` and `run-fixforward2.jsonl` | — |
| 19 | BVDT | Verdict lines and the falsifiable | PASS | rows 3, 10, 15, 16 above; the falsifiable is a testable prediction: a converging fix-forward transcript shorter than the respec ask would refute the film | — |
| 20 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
| 21 | all | Model / version strings; costs shown numerically ($0.888, $0.359) | PASS | dollar figures are recorded results, not model tier claims; no model name spoken; "Claude Code" is the product name, not datable | — |
| 22 | metadata | Session ids (727cb81b-…, 5f9cb45f-…) | EXEMPT | shown only as display truncation; not privacy-sensitive | — |

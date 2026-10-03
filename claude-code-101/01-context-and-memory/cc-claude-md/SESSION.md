# SESSION.md — cc-claude-md

The real Claude Code sessions this reel reconstructs (REAL-SESSION LAW). Headless `claude -p`, Claude Code 2.1.150, 2026-09-08, in a fresh git repo `gradebook` (README, `src/gradebook.py`, `tests/test_gradebook.py`, `.gitignore`; no CLAUDE.md). Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|pytest|wc)` — note **`python3`, not `python`**; that fence matters below. `--strict-mcp-config` (no connectors). Session A (`fe0edef3-b504-4ce2-8996-386d9c3a68b7`) = turns 1–2; session B (`.session_id3`) = turn 3, a fresh session with no memory of A. Liam's VERIFY commands were run by hand in the shell. Raw stream-json: `evidence/turn{1,2,3}.jsonl`; the file at each stage: `evidence/CLAUDE.md.init`, `CLAUDE.md.turn2`, `CLAUDE.md` (final); diffs in `evidence/`.

## Turn 1 — `/init`

**Liam typed:** `/init`

- **TOOL** `Bash` `ls -la …/claudemd-session` → the four files
- **TOOL** `Bash` `find …/src …/tests -type f` → `src/gradebook.py`, `tests/test_gradebook.py`
- **TOOL** `Read` `README.md` · **TOOL** `Read` `src/gradebook.py` · **TOOL** `Read` `tests/test_gradebook.py` · **TOOL** `Read` `.gitignore`
- **TOOL** `Write` `CLAUDE.md` (17 lines; verbatim in `evidence/CLAUDE.md.init`). Its command lines:

```
- Run the CLI: `python src/gradebook.py [add NAME | score NAME VALUE | report]` (defaults to `report`)
- Run tests: `pytest`
- Run a single test: `pytest tests/test_gradebook.py::test_average`

No dependencies beyond the standard library and `pytest` for tests.
```

and its architecture paragraph: "Single-module CLI (`src/gradebook.py`) that persists to a JSON file (`DB = Path("grades.json")`) in the current working directory. Each command re-reads and re-writes the entire file — there is no in-memory session state. The `if __name__ == "__main__"` block dispatches `sys.argv[1]` through a `{name: function}` dict, so adding a subcommand means adding a top-level function and an entry to that dict."

- **CLAUDE:** Created `CLAUDE.md`. It covers the CLI invocation and pytest commands, then explains the two non-obvious architectural points: the JSON file is re-read/written per command (no session state, CWD-relative), and tests rely on `sys.path` injection plus `monkeypatch` of `gradebook.DB` because there's no package layout.
- **RESULT:** success · turns=8 · duration_ms=29658 · cost_usd=0.249

### Liam's VERIFY after turn 1

```
> wc -l CLAUDE.md
      17 CLAUDE.md
> pytest
zsh: command not found: pytest
> python3 -m pytest -q
/opt/homebrew/opt/python@3.14/bin/python3.14: No module named pytest
```

Finding: the briefing is right about the code and wrong about the machine — it wrote the command most Python projects use, not one that runs here.

## Turn 2 — the correction (same session)

**Liam typed:**

```
CLAUDE.md says "Run tests: pytest", but pytest is not installed on this machine and I do not want any dependencies. Rewrite tests/test_gradebook.py with the standard library unittest module only (no fixtures), and change the test commands in CLAUDE.md to the exact command that works here. Do not touch src/gradebook.py.
```

- **TOOL** `Write` `tests/test_gradebook.py` (unittest + tempfile + redirect_stdout; `evidence/test_gradebook.py` is the final version after turn 3)
- **TOOL** `Bash` `python tests/test_gradebook.py && echo "---" && python tests/test_gradebook.py TestGradebook.test_average` → `This Bash command contains multiple operations. The following parts require approval: …`
- **TOOL** `Bash` `python tests/test_gradebook.py` → `This command requires approval`
- **TOOL** `AskUserQuestion` "May I run `python tests/test_gradebook.py` to verify the new test commands work?" → `Answer questions?` (headless: nobody there)
- **CLAUDE:** I'll proceed without running the verification. Updating CLAUDE.md now.
- **TOOL** `Edit` `CLAUDE.md` (the three command lines + the dependency line)
- **CLAUDE:** The architecture note also referenced pytest fixtures — updating that to match the new test style.
- **TOOL** `Edit` `CLAUDE.md` (the architecture paragraph: `tempfile.TemporaryDirectory` … `contextlib.redirect_stdout`)
- **CLAUDE:** Done. `tests/test_gradebook.py` now uses only `unittest` + `tempfile` + `contextlib.redirect_stdout` (no fixtures, no pytest), and CLAUDE.md's commands are `python tests/test_gradebook.py` and `python tests/test_gradebook.py TestGradebook.test_average`. I also updated the architecture paragraph so it no longer references `monkeypatch`/`tmp_path`. I was not able to verify the commands run (verification was declined), so please run one to confirm.
- **RESULT:** success · turns=7 · duration_ms=44672 · cost_usd=0.410

`git diff HEAD~2 HEAD~1 -- CLAUDE.md` (`evidence/claude-md.turn2.diff`), the changed lines:

```
-- Run tests: `pytest`
-- Run a single test: `pytest tests/test_gradebook.py::test_average`
+- Run tests: `python tests/test_gradebook.py`
+- Run a single test: `python tests/test_gradebook.py TestGradebook.test_average`
-No dependencies beyond the standard library and `pytest` for tests.
+No dependencies beyond the standard library. Tests use `unittest`.
```

### Liam's VERIFY after turn 2

```
> git diff --stat
 CLAUDE.md               |  8 ++++----
 tests/test_gradebook.py | 33 +++++++++++++++++++++++++--------
 2 files changed, 29 insertions(+), 12 deletions(-)
> python3 tests/test_gradebook.py
.
----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
> grep -n "python" CLAUDE.md
7:- Run the CLI: `python src/gradebook.py [add NAME | score NAME VALUE | report]` (defaults to `report`)
8:- Run tests: `python tests/test_gradebook.py`
9:- Run a single test: `python tests/test_gradebook.py TestGradebook.test_average`
> which python python3
python: aliased to python3
/opt/homebrew/bin/python3
```

Finding: the test passes. The file says `python`; on this Mac that is a shell alias for `python3`, and the session's fence only allowed `python3` — which is why Claude could not run its own command. Left as-is for turn 3 (so turn 3 sees the file as Claude wrote it); fixed by hand after.

## Turn 3 — a fresh session, CLAUDE.md auto-loaded

**Liam typed (new session, `claude -p`, no `--resume`):**

```
Add a "remove NAME" command that deletes a student and their scores. Follow this repo's conventions and run the tests when you are done.
```

- **TOOL** `Read` `src/gradebook.py` · **TOOL** `Read` `tests/test_gradebook.py`
- **TOOL** `Edit` `src/gradebook.py` — adds `def remove(name)` after `score()` and `"remove": remove` to the dispatch dict (`evidence/gradebook.turn3.diff`, +9 −1 in that file's dispatch line)
- **CLAUDE:** Now add a test following the existing pattern.
- **TOOL** `Edit` `tests/test_gradebook.py` — `test_remove` (happy path + missing student)
- **TOOL** `Bash` `python tests/test_gradebook.py` → `This command requires approval` (×2), then `python tests/test_gradebook.py -v` → same
- **TOOL** `AskUserQuestion` "Can I run the test command from CLAUDE.md?" → `Answer questions?`
- **CLAUDE:** It looks like tool approvals are being blocked. Let me try once more.
- **TOOL** `Bash` `python tests/test_gradebook.py 2>&1` → `This command requires approval`
- **CLAUDE:** I've added the `remove` command and a test, but the Bash approval to run `python tests/test_gradebook.py` was denied twice in a row. Per the guidance not to re-attempt the same denied call, I'll stop and hand it back. **Changes:** `src/gradebook.py:30-37` — added `remove(name)` that `pop`s the student (prints "no such student: NAME" and returns without writing if absent, else saves and prints "removed NAME"). Added `"remove": remove` to the dispatch dict. `tests/test_gradebook.py:28-47` — added `test_remove` covering both the happy path (data ends up as `{"grace": []}`) and the missing-student branch. Please run `python tests/test_gradebook.py` to confirm — I couldn't execute it here.
- **RESULT:** success · turns=10 · duration_ms=46015 · cost_usd=0.321

### Liam's VERIFY after turn 3

```
> git diff --stat
 src/gradebook.py        | 11 ++++++++++-
 tests/test_gradebook.py | 21 +++++++++++++++++++++
 2 files changed, 31 insertions(+), 1 deletion(-)
> git diff src/gradebook.py        # (the dispatch line)
-    {"add": add, "score": score, "report": report}[cmd](*args)
+    {"add": add, "score": score, "remove": remove, "report": report}[cmd](*args)
> python3 tests/test_gradebook.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
> python3 src/gradebook.py add ada && python3 src/gradebook.py remove ada
added ada
removed ada
> python3 src/gradebook.py remove ada
no such student: ada
> sed -i '' 's/python /python3 /g' CLAUDE.md
> grep -c python3 CLAUDE.md
3
```

Finding: the fresh session followed the briefing to the letter — a top-level function, one entry in the dict, a test in the file's pattern — and, blocked from running the file's own test command, said so and stopped instead of guessing. The one thing still wrong in the file (`python` vs `python3`) was a one-line edit Liam made by hand.

## What the sessions gave the film

1. `/init` reads before it writes: four Reads, one Write, seventeen lines, and it got the two non-obvious architecture facts right.
2. The briefing was right about the code and wrong about the machine (`pytest`). A command in CLAUDE.md nobody ran is a command the next session will trust.
3. The correction was one prompt; Claude fixed the file twice (commands, then the paragraph that still mentioned fixtures) and said plainly it could not verify.
4. A fresh session with one line of instruction did exactly what the file said — the payoff — and when the fence blocked its test command it asked, got no answer, and handed back.

# SESSION.md — cc-agentic-loop

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Two fresh
headless `claude -p` runs, Claude Code 2.1.150, 2026-09-09, `scratch/` is a
git repo tagged `pristine`. Same one-sentence ask, same allowed tools,
`--strict-mcp-config`. The only thing that changes between runs is
`--permission-mode`. Raw stream-json in `evidence/run-{loop,plan}.jsonl`;
`evidence/before/` is the folder before either run; `evidence/after-loop/`
is the folder after run 1 (`git reset --hard pristine` before run 2);
`evidence/plan.md` is the plan file run 2 left on disk.

```
Fix the bug in calc.py, add a test that would have caught it, and run the tests.
```

Allowed tools (both runs, verbatim):
`Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)`

The bug in `calc.py` is a guard clause on `add` that returns `0` when either
argument is negative. The three existing tests all use positive numbers, so
they pass despite the bug — nothing catches it until a test says otherwise.

## Run 1 — loop (`--permission-mode acceptEdits`, session `e588ab67-…`)

Turn-by-turn, from `run-loop.jsonl`:

```
TOOL Bash    ls scratch/
TOOL Read    calc.py
TOOL Read    test_calc.py
TOOL Read    README.md
TEXT         "The bug in `add` is the guard that returns 0 when either
             operand is negative. Fixing it and adding a covering test."
TOOL Edit    calc.py         (guard clause removed)
TOOL Edit    test_calc.py    (test_add_negatives added)
TOOL Bash    python3 -m unittest test_calc.py -v
             → 4 tests, all ok
TEXT         "Fixed `add` by removing the negative-guard that clobbered
             the result to 0, added `test_add_negatives` … all 4 tests pass."
RESULT       success · turns=8 · 38.4 s · $0.294 · 7 tool calls · 2 files edited
```

## Run 2 — plan (`--permission-mode plan`, session `124b4a22-…`)

Same one sentence. `scratch/` was reset to `pristine` first.

```
TOOL Bash    ls scratch/
TOOL Read    calc.py
TOOL Read    test_calc.py
TOOL Read    README.md
TEXT         "The bug in `calc.py:2-3`: `add` returns 0 when either argument
             is negative instead of computing the sum. Fix is to remove the
             guard clause."
TOOL Write   ~/.claude/plans/fix-the-bug-in-virtual-bachman.md
             (28 lines: Context / Change / Verify)
TOOL ExitPlanMode  { plan: <the same 28 lines>,
                    allowedPrompts: [{ tool: Bash, prompt: "run python unittest" }] }
RESULT of ExitPlanMode: "Exit plan mode?"   ← the interruption point
             (in headless, no user to answer; the loop stops here)
RESULT       success · turns=8 · 40.8 s · $0.223 · 3 Reads · 1 Write to plans/ · 0 files in scratch/ edited
```

## Liam's VERIFY (plain shell, in `scratch/` and `~/.claude/plans/`)

```
$ diff -u before/calc.py after-loop/calc.py
-    if a < 0 or b < 0:
-        return 0
$ diff -u before/test_calc.py after-loop/test_calc.py
+    def test_add_negatives(self):
+        self.assertEqual(add(-2, 3), 1)
+        self.assertEqual(add(2, -3), -1)
+        self.assertEqual(add(-2, -3), -5)
$ ( cd after-loop && python3 -m unittest test_calc.py 2>&1 | tail -1 )
OK
$ ( cd scratch && git status --short )        # after run 2, after `git reset --hard pristine`
$                                              # (nothing — plan mode wrote zero files here)
$ wc -l ~/.claude/plans/fix-the-bug-in-virtual-bachman.md
      28 …/fix-the-bug-in-virtual-bachman.md
```

## The mechanism this film exists to show

One prompt. Same model, same tools, same repo. Two `--permission-mode` values.

|                     | loop (acceptEdits)      | plan                          |
|---------------------|-------------------------|-------------------------------|
| tool calls          | 7                       | 4                             |
| files edited in scratch/ | 2                  | **0**                         |
| the loop's shape    | Gather → Act → Verify   | Gather → Plan → **stop**      |
| interruption point  | none                    | `ExitPlanMode` → "Exit plan mode?" |
| tests ended         | 4 passing               | none run                      |
| wall time           | 38.4 s                  | 40.8 s                        |

The loop is the same loop; plan mode is the interruption point. It writes a
plan to `~/.claude/plans/…`, calls `ExitPlanMode` with the plan and the
prompts it would like next, and stops on "Exit plan mode?" — waiting for a
yes. In the interactive TUI the yes is a keystroke; in headless there is no
user to press it, so nothing after Gather runs. Same design, both surfaces.

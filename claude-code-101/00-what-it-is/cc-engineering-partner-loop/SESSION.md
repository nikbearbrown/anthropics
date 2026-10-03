# SESSION.md — cc-engineering-partner-loop

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Two headless sessions on the same tiny module in `scratch/`: a bare fix run, and the engineering partner loop — plan first, apply the exact plan, then a correction turn on a spec-drift the verify surfaced. Claude Code 2.1.150, 2026-09-09. Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`. Raw stream-json in `evidence/run-*.jsonl`; the module and tests in `scratch/` and `evidence/`.

## The scratch project (all in `scratch/`, git repo, one commit)

- `ranges.py` — six lines, `parse_range("1-5") -> (1, 5)`. Buggy: silently accepts reversed ranges (`"5-1"` → `(5, 1)`) and extra dashes (`"1-2-3"` → `(1, 2)`).
- `test_ranges.py` — five `unittest` tests. Two fail. **This file is the oracle.**
- `ORACLE.sh` — one line: `python3 -m unittest test_ranges -v`.

Starting state (`evidence/verify.txt` baseline):

```
> python3 -m unittest test_ranges -v
test_empty_raises          ... ok
test_extra_dash_raises     ... FAIL
test_range                 ... ok
test_reversed_raises       ... FAIL
test_single_number         ... ok
Ran 5 tests in 0.000s
FAILED (failures=2)
```

## Ask (verbatim, both runs use the same underlying task)

```
Make the failing tests pass.
```

- **Bare** phrasing: `"Fix the failing tests."` — no oracle named, no scope declared, no plan requested. Whatever Claude decides is what lands.
- **Partner-loop** phrasing (turn 1 of 3): `"The oracle is test_ranges.py — read it. Then read ranges.py. Do not edit anything yet. Give me a numbered plan for making the oracle green with the MINIMAL change to parse_range only — nothing outside that function. Show the exact diff you would apply, in \`\`\`diff fences. Stop after the plan."`

## Run: bare (session `64af6ebc-…`)

- **TOOL** `Bash` `ls scratch` · **Read** `ranges.py` · **Read** `test_ranges.py` · **Bash** `python3 -m unittest test_ranges -v`
- **CLAUDE:** Two failures: reversed ranges and extra dashes need to raise `ValueError`.
- **TOOL** `Edit` `ranges.py` — a five-line patch: guard `len(parts) != 2`; parse `lo, hi`; guard `lo > hi`.
- **TOOL** `Bash` `python3 -m unittest test_ranges -v` → all five pass.
- **CLAUDE:** All 5 tests pass. Added two guards in `ranges.py:1`: reject `parts != 2` (extra dashes) and reject `lo > hi` (reversed).
- **RESULT:** success · turns=7 · 24.9 s · $0.281

The bare run **works**. The plan never surfaced. Liam did not approve scope; he inspected the diff **after** it landed.

## Run: partner-loop, turn 1 — PLAN ONLY (session `a4c91437-…`)

`Edit` and `Write` withheld from the tool allowlist. Claude is forced to think in text.

- **Read** `test_ranges.py` · **Read** `ranges.py`
- **CLAUDE (text):** a five-row failure table (per test: input → current behavior → expected), then:

  > **Plan.** 1) After splitting on `-`, if `len(parts)` is neither 1 nor 2, raise `ValueError` (kills `"1-2-3"`). 2) On the 2-part branch, parse `start`/`end` and raise `ValueError` when `start > end` (kills `"5-1"`). 3) Leave the 1-part branch alone — the existing `int(parts[0])` already raises for `""` (satisfies `test_empty_raises`) and returns `(n,n)` for `"7"`. 4) No changes anywhere outside `parse_range`.

  Followed by an exact `` ```diff `` block:

  ```diff
  --- a/ranges.py
  +++ b/ranges.py
  @@ -1,6 +1,10 @@
   def parse_range(s):
       """Parse '1-5' -> (1, 5). '7' -> (7, 7). '' or reversed is an error."""
       parts = s.split('-')
       if len(parts) == 1:
           return (int(parts[0]), int(parts[0]))
  -    return (int(parts[0]), int(parts[1]))
  +    if len(parts) != 2:
  +        raise ValueError(f"invalid range: {s!r}")
  +    start, end = int(parts[0]), int(parts[1])
  +    if start > end:
  +        raise ValueError(f"reversed range: {s!r}")
  +    return (start, end)
  ```

  `Stopping here — no edits applied.`
- **RESULT:** success · turns=3 · 23.6 s · $0.196

## Run: partner-loop, turn 2 — APPLY (same session, resumed)

Prompt: `"Plan approved. Apply the diff exactly as shown. Then run the oracle (python3 -m unittest test_ranges -v) and report the exit summary line only."`

- **TOOL** `Edit` `ranges.py` — the exact five-line patch from the plan.
- **TOOL** `Bash` `python3 -m unittest test_ranges -v | tail -5` → `Ran 5 tests in 0.000s / OK`.
- **CLAUDE:** `Ran 5 tests in 0.000s — OK.`
- **RESULT:** success · turns=3 · 12.4 s · $0.195

## Run: partner-loop, turn 3 — CORRECTION (same session, resumed)

Liam's verify — `grep '"""' ranges.py` — surfaced the drift: the docstring still says `'' or reversed is an error`, but the code now also raises on extra dashes. Prompt: `"The docstring is stale — it says '' or reversed is an error, but the code now also raises on extra dashes. Update ONLY the docstring in parse_range to match what the code actually raises. No logic change. Then show me the diff and run the oracle."`

- **TOOL** `Edit` `ranges.py` — docstring line only.
- **TOOL** `Bash` `git diff ranges.py && python3 -m unittest test_ranges -v | tail -5` → `Ran 5 tests in 0.000s / OK`.
- **CLAUDE:** `Docstring updated (only line changed in this turn); full diff vs. HEAD shown above. Oracle: Ran 5 tests in 0.000s — OK.`
- **RESULT:** success · turns=3 · 18.0 s · $0.201

## Liam's VERIFY (plain shell, `evidence/verify.txt`)

```
> wc -l ranges.py test_ranges.py
      11 ranges.py
      26 test_ranges.py

> python3 -m unittest test_ranges -v
test_empty_raises          ... ok
test_extra_dash_raises     ... ok
test_range                 ... ok
test_reversed_raises       ... ok
test_single_number         ... ok
Ran 5 tests in 0.000s
OK

> git diff --stat ranges.py
 ranges.py | 9 +++++++--
 1 file changed, 7 insertions(+), 2 deletions(-)

> grep -c 'raise ValueError' ranges.py
2

> git diff ranges.py                     # partner-loop final vs initial
-    """Parse '1-5' -> (1, 5). '7' -> (7, 7). '' or reversed is an error."""
+    """Parse '1-5' -> (1, 5). '7' -> (7, 7). '', reversed, or extra dashes is an error."""
     parts = s.split('-')
     if len(parts) == 1:
         return (int(parts[0]), int(parts[0]))
-    return (int(parts[0]), int(parts[1]))
+    if len(parts) != 2:
+        raise ValueError(f"invalid range: {s!r}")
+    start, end = int(parts[0]), int(parts[1])
+    if start > end:
+        raise ValueError(f"reversed range: {s!r}")
+    return (start, end)
```

## The bare-vs-partner diff (`evidence/ranges.bare.py` vs `evidence/ranges.partner.py`)

Identical logic. Variable names differ (`lo/hi` vs `start/end`); nothing else. The engineering partner loop did not produce **different code**. It produced a **plan Liam read before the diff landed**.

## What the runs gave the film

1. **Bare:** the fix works. Two guards, all five green. There is no plan surface. Liam sees the change **after** it lands, when he reads the diff. If the change had been wrong-scoped, that is when he would learn.
2. **Partner, plan turn:** Claude was denied Edit/Write; the plan and the exact diff had to exist in text before code was written. Liam approved four numbered steps and a five-line patch. The scope gate happened **before** the diff.
3. **Partner, apply turn:** the diff landed exactly as approved. Oracle green.
4. **Partner, correction turn:** Liam's `grep` on the docstring surfaced a stale contract. One re-prompt, one-line change, scope named ("only the docstring"). Oracle stayed green.

The film is the argument that the engineering partner loop shifts the human's job from *debugging code that already landed* to *approving the plan and reading the diff before it lands* — and that the diff itself does not change; the timing of the human's judgment does.

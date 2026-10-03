# SESSION.md — cc-rewind-respec

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Four headless `claude -p` runs, Claude Code 2.1.150, 2026-09-09, on scratch folder `scratch/` (`dedupe.py`, `test_dedupe.py`, `SPEC.md`, `ask.txt`; a git repo pinned at commit `f5ef78b` "buggy start"). Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`. Raw stream-json in `evidence/run-{ff1,ff2,ff3,respec}.jsonl`; final files `evidence/dedupe.{ff3,respec}.py`; session ids `evidence/sid-{ff,respec}.txt`; the drift `evidence/drift.txt`; the respec ask `evidence/respec-ask.txt`.

**Headless caveat (`/rewind` note).** The interactive `Esc-Esc` / `/rewind` restores both conversation and file system to a checkpoint. Headless `claude -p` has no `/rewind`. The film uses the headless equivalent, which the SKILL states explicitly: a new `claude -p` with no `--resume` **is** `/clear`. The file-system half of the checkpoint is restored by `git reset --hard` on the scratch. What the reel calls "rewind" is therefore two commands the viewer can run: `git reset --hard <checkpoint>` for the files, a fresh `claude -p` (no `--resume`, new `--session-id`) for the conversation. The concept — the respec — is unchanged.

## The scratch

```
dedupe.py         def dedupe(items): return list(set(items))     # buggy
test_dedupe.py    3 tests: basic dedupe · preserve order · unhashable ([[1],[2],[1]] → [[1],[2]])
SPEC.md           preserve order · handle unhashable · do not modify tests
ask.txt           "The dedupe tests in test_dedupe.py are failing. Fix dedupe.py."
```

Buggy start: `test_basic` passes; `test_preserve_order` fails (set() lost order); `test_unhashable` errors (`TypeError: unhashable type: 'list'`).

## Run: FF1 — the vague ask (session `a09ae7ad-…`, no `--resume`)

- **TOOL** `Bash ls scratch/` · **Read** `test_dedupe.py` · **Read** `dedupe.py` · **Read** `SPEC.md`
- **TOOL** `Write dedupe.py` — replaced with a linear-scan implementation:
  ```python
  def dedupe(items):
      result = []
      for item in items:
          if item not in result:
              result.append(item)
      return result
  ```
- **TOOL** `Bash python -m unittest test_dedupe.py -v` (denied — `python` not in fence; the reel uses `python3`) · **TOOL** `Bash python -m unittest …` (denied again) · **TOOL** `Bash python3 -m unittest test_dedupe.py -v` → 3 passed
- **CLAUDE:** "All three tests pass. Fixed `dedupe.py` to iterate and preserve first-occurrence order using `in` (which uses equality, so lists work)."
- **RESULT:** success · turns=9 · 33.2 s · $0.312

## Run: FF2 — "speed it up" (same session, `--resume`)

- **User:** "That's O(n squared). Speed it up for large lists."
- **TOOL** `Write dedupe.py` — replaced with a two-branch fast path:
  ```python
  def dedupe(items):
      result = []
      seen_hashable = set()
      seen_unhashable = []
      for item in items:
          try:
              if item in seen_hashable: continue
              seen_hashable.add(item)
          except TypeError:
              if item in seen_unhashable: continue
              seen_unhashable.append(item)
          result.append(item)
      return result
  ```
- **TOOL** `Bash python3 -m unittest test_dedupe.py -v` → 3 passed
- **CLAUDE:** "Tests still pass. Now O(n) amortized for hashable items (set membership), falling back to linear scan only for the unhashable subset."
- **RESULT:** success · turns=3 · 12.4 s · $0.194

## Run: FF3 — "simpler, one data structure" (same session, `--resume`)

- **User:** "Simpler. One data structure."
- **TOOL** `Write dedupe.py` — replaced with a one-liner:
  ```python
  def dedupe(items):
      return list({repr(x): x for x in items}.values())
  ```
- **TOOL** `Bash python3 -m unittest test_dedupe.py -v` → 3 passed
- **CLAUDE:** "One dict, O(n). `repr` gives every item — hashable or not — a stable string key; dict insertion-order preserves first occurrence."
- **CLAUDE (caveat, unsolicited):** "`repr` is a canonical-string proxy for equality, not equality itself. It works for the test inputs (ints, lists) and most standard types, but can diverge from `==` for edge cases (e.g., two dicts with same contents but different insertion order have equal `==` but different `repr`). If that matters, say the word and I'll swap in a stricter approach."
- **RESULT:** success · turns=3 · 53.8 s · $0.172
- **The drift the tests never covered:** `dedupe([1, 1.0])` returns `[1, 1.0]`; `dedupe([True, 1])` returns `[True, 1]`. Both should collapse under `==`. The tests never checked cross-type equality — so `check` passed, semantics regressed. Claude's caveat named it; the fence didn't.

## Liam's rewind: `git reset --hard`

```
> git reset --hard f5ef78b
HEAD is now at f5ef78b buggy start
> cat dedupe.py
def dedupe(items):
    return list(set(items))
```

Scratch restored to the checkpoint. Conversation state is discarded by starting a new session (no `--resume`).

## Run: respec — the failure named as a constraint (session `96c45930-…`, no `--resume`, `/clear` equivalent)

- **User (the respec):** "The dedupe tests in test_dedupe.py fail. Fix dedupe.py so that: (1) order is preserved (first occurrence stays); (2) unhashable items like lists work; (3) equality is Python `==`, not `repr` — so dedupe([1, 1.0]) must return [1]. Use hashing with a linear-scan fallback via try/except. Do not modify the test."
- **TOOL** `Bash ls scratch/` · **Read** `dedupe.py` · **Read** `test_dedupe.py`
- **TOOL** `Write dedupe.py` — the two-branch implementation, equality-correct:
  ```python
  def dedupe(items):
      result = []
      seen = []
      seen_hashable = set()
      for item in items:
          try:
              if item in seen_hashable: continue
              seen_hashable.add(item)
          except TypeError:
              if any(item == s for s in seen): continue
          seen.append(item)
          result.append(item)
      return result
  ```
- **TOOL** `Bash python -m unittest …` (denied) · **TOOL** `Bash python3 -m unittest test_dedupe.py -v` → 3 passed
- **CLAUDE:** "All 3 tests pass. `dedupe.py` now uses a set for hashable items with a linear-scan fallback (via `TypeError`) for unhashable ones, preserves first-occurrence order, and relies on `==` throughout — so `dedupe([1, 1.0])` returns `[1]`."
- **RESULT:** success · turns=7 · 33.7 s · $0.261

## Liam's VERIFY of the respec version

```
> python3 -m unittest test_dedupe.py
...
OK
> python3 -c "from dedupe import dedupe; print(dedupe([1, 1.0]))"
[1]
> python3 -c "from dedupe import dedupe; print(dedupe([True, 1]))"
[True]
```

The equality drift is gone. The failure mode named in the respec is a test the respec version passes.

## What the runs gave the film

1. FF1: a vague ask "the tests fail, fix it." Claude produced a clean linear-scan solution. Tests pass. So far so good.
2. FF2 (same session, `--resume`): "speed it up." Two-branch fast path via `try/except`. Tests pass. Also good.
3. FF3 (same session, `--resume`): "simpler." Regressed to a `repr`-keyed dict. Tests pass — but the equality semantics silently changed: `dedupe([1, 1.0])` now returns `[1, 1.0]`. The tests didn't cover it. Claude even disclosed the caveat; the fence didn't force the check.
4. Rewind + respec (fresh session): the same original ask *plus the failure mode as an explicit negative constraint* ("equality is `==`, not `repr` — so dedupe([1, 1.0]) must return [1]"). Two-branch implementation, equality-correct, one shot.

The film's mechanism: forward correction in a polluted session pushed toward *cleverness* the tests couldn't catch. Rewinding to the checkpoint and respecifying the ask with the failure mode named as a negative constraint produced the right implementation on the first try.

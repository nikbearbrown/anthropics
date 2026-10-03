# SESSION.md — cc-claude-md-length

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Six headless `claude -p` runs, Claude Code 2.1.150, 2026-09-08/09, each a **fresh session** (no `--resume`) in one of three copies of the same tiny repo (`gradebook`: `src/gradebook.py`, `src/audit.py`, `tests/test_gradebook.py`, README) that differ only in `CLAUDE.md`. Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`. The same ask every time (`evidence/ask.txt`):

```
Add a "clear NAME" command that empties a student's scores but keeps the student. Follow this repo's conventions and run the tests when you are done.
```

The rule under test, identical in all three files: **"Every function that writes grades.json must call `audit(name, action)` from `src/audit.py` right after `save(data)`. No exceptions."** The task tempts you to skip it (`clear` is a write).

## The three briefings (`evidence/CLAUDE.md.{short,long,xlong}`)

```
> wc -l CLAUDE.md.short CLAUDE.md.long CLAUDE.md.xlong
      13 CLAUDE.md.short
     370 CLAUDE.md.long
    1066 CLAUDE.md.xlong
> grep -n "must call" CLAUDE.md.short CLAUDE.md.long CLAUDE.md.xlong
CLAUDE.md.short:8:- **Every function that writes grades.json must call `audit(…
CLAUDE.md.long:229:- **Every function that writes grades.json must call `audit(…
CLAUDE.md.xlong:925:- **Every function that writes grades.json must call `audit(…
```

`short` is the rule plus commands and architecture (87 words). `long` adds plausible sections — code style, git etiquette, error handling, testing, performance, documentation, dependencies, security, release checklist, FAQ — each padded with generated filler lines (2,229 words); the rule sits under "Rules" at line 229. `xlong` is `long` with twelve generated "Term N retrospective" sections of filler inserted before "Rules" (11,538 words); the rule sits at line 925. The filler is deliberate: the test is whether the rule survives the noise.

## The six runs

| CLAUDE.md | trial | turns | wall | new context (cache_creation tokens) | tool calls | rule followed | tests |
|---|---|---|---|---|---|---|---|
| short (13) | 1 | 8 | 26.4 s | 16,120 | 7 | yes — `audit(name, "clear")` | 3 pass |
| short (13) | 2 | 8 | 30.2 s | 16,137 | 7 | yes | 3 pass |
| long (370) | 1 | 12 | 63.1 s | 23,615 | 10 | yes — and it also edited CLAUDE.md's command list, citing the file's own line "Update the command list above when you add a command" | 3 pass |
| long (370) | 2 | 9 | 47.4 s | 21,511 | 8 | yes — "Calls `audit(name, "clear")` immediately after `save(data)`, per the rule"; dict entry "in insertion order (per the CLAUDE.md)" | 3 pass |
| xlong (1066) | 1 | 8 | 42.5 s | 38,049 | 7 | yes — "saves, audits, and prints `cleared NAME`" | 3 pass |
| xlong (1066) | 2 | 9 | 49.1 s | 38,505 | 8 | yes — "audit after save, missing-student branch" | 3 pass |

Full evidence (raw stream-json + the diff) is retained for trial 2 of each length: `evidence/run-{short,long,xlong}-2.jsonl`, `evidence/diff-*-2.patch`, `evidence/trials.json`. **Trial 1 artifacts were deleted by the `git clean` that reset the repo before trial 2** — their rows above come from the run summaries printed at the time (turns, wall, tokens, cost, the audit line found in the diff, tests passing). The film's on-screen runs and numbers are trial 2 of each length.

### Liam's VERIFY (plain shell, on the evidence)

```
> grep -c 'audit(name, "clear")' diff-short-2.patch diff-long-2.patch diff-xlong-2.patch
diff-short-2.patch:1
diff-long-2.patch:1
diff-xlong-2.patch:1
> python3 tests/test_gradebook.py        # in each repo after its run
Ran 3 tests in 0.003s
OK
> python3 -c "…trials.json…"
short  trial 2   30.2s  new context  16137 tokens  rule followed
long   trial 2   47.4s  new context  21511 tokens  rule followed
xlong  trial 2   49.1s  new context  38505 tokens  rule followed
```

## Claude's words, per run (trial 2), verbatim spans used on screen

- **short:** "All 3 tests pass. Added `clear(name)` in `src/gradebook.py:43` (mirrors `remove`'s not-found handling, empties the list, then `save` + `audit(name, "clear")`), wired it into the dispatch dict, and added `test_clear` covering both the happy path and the no-such-student case."
- **long:** "All 3 tests pass. The `clear NAME` command: … Calls `audit(name, "clear")` immediately after `save(data)`, per the rule … Added to the dispatch dict at the end (order commands were added, not alphabetical) …"
- **xlong:** "I've read the code and tests. Now I'll add `clear(name)` following the `remove` pattern (audit after save, missing-student branch), append it to the dispatch dict, and add a `test_clear` covering both branches." … "All 3 tests pass."

## What the runs gave the film

1. The claim under test — a long CLAUDE.md gets ignored — did not hold at 370 or 1,066 lines: six for six, the buried rule was followed and, in the long runs, quoted back.
2. What a long file does cost is visible in every run's receipt: new context per session grew 16k → 21k → 38k tokens before the first edit, and wall time roughly doubled.
3. A long file is also obeyed in full: long trial 1 acted on a line the author had forgotten ("Update the command list above…"), and both long runs honoured the dict-order line. Every line you leave in the file is a line that will be followed.
4. Costs (recorded, not spoken): short $0.198 / $0.263; long $0.462 / $0.343; xlong $0.491 / $0.530.

# SESSION.md — cc-conducting-not-prompting

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Two fresh headless `claude -p` sessions, Claude Code 2.1.150, 2026-09-09, same one-sentence ask (`evidence/ask.txt`), two conditions. Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`. Raw stream-json in `evidence/run-{bare,conducting}.jsonl`; the four source files in `evidence/`; the SPEC checker in `evidence/spec_check.py`.

```
Write format_price(cents: int) -> str in format_price.py and add unittest tests in test_format_price.py.
```

| Condition | What was in the folder |
|---|---|
| **bare** | `README.md`, `ask.txt` |
| **conducting** | the same plus `SPEC.md` (11 lines) — five example cases and four decisions; ask ends `Read SPEC.md first.` |

`SPEC.md` (`evidence/SPEC.md`, verbatim) was written by Liam before the run. It names five inputs, their outputs, and four rules: no dollar sign; no thousands separator; two decimals; suffix ` EUR`; negative raises `ValueError`. `spec_check.py` (`evidence/spec_check.py`) is that spec as a script — it imports whatever `format_price.py` you give it and prints PASS or the FAILs.

## Run: bare (session `89136c5c-…`, 25.8 s, turns=5)

- **TOOL** `Bash` `ls .`
- **TOOL** `Write` `format_price.py` (7 lines)
- **TOOL** `Write` `test_format_price.py` (46 lines)
- **TOOL** `Bash` `python3 -m unittest test_format_price -v` → 10 tests, `OK`
- **CLAUDE:** Wrote `format_price.py` (int cents → `$1,234.56`, negatives get a leading `-`, rejects non-ints including bool) and `test_format_price.py` covering zero, sub-dollar, whole dollars, thousands separator …
- **RESULT:** success · turns=5 · 25.8 s · $0.339

Choices Claude made without being asked: dollar sign, thousands separator on 6-digit amounts, negatives allowed and prefixed `-`, `TypeError` for non-int types including `bool`, ten test methods.

## Run: conducting (session `30f069af-…`, 42.0 s, turns=7)

- **TOOL** `Read` `SPEC.md`
- **TOOL** `Bash` `ls .`
- **TOOL** `Write` `format_price.py` (4 lines)
- **TOOL** `Write` `test_format_price.py` (25 lines)
- **TOOL** `Bash` `python -m unittest test_format_price.py -v` (fails: `python` not on this box)
- **TOOL** `Bash` `python3 -m unittest test_format_price.py -v` → 5 tests, `OK`
- **CLAUDE:** All 5 tests pass. `format_price.py` splits cents into euros/remainder with zero-padded decimals and rejects negatives; `test_format_price.py` covers each SPEC case.
- **RESULT:** success · turns=7 · 42.0 s · $0.385

Every choice traces to a line of `SPEC.md`: EUR suffix, no separator, two decimals, `ValueError` on negatives, five test cases named after their inputs.

## Liam's VERIFY (plain shell, in `evidence/`; `spec_check.py` run against each `format_price.py`)

```
> wc -l format_price.bare.py format_price.conducting.py
       7 format_price.bare.py
       4 format_price.conducting.py
> wc -l test_format_price.bare.py test_format_price.conducting.py
      46 test_format_price.bare.py
      25 test_format_price.conducting.py
> grep -c "^    def test" test_format_price.bare.py
10
> grep -c "^    def test" test_format_price.conducting.py
5
> grep -c '\$' format_price.bare.py
1
> grep -c EUR format_price.bare.py
0
> grep -c '\$' format_price.conducting.py
0
> grep -c EUR format_price.conducting.py
1
> python3 spec_check.py format_price.bare.py
FAIL: format_price(1299) -> '$12.99' (SPEC: '12.99 EUR')
FAIL: format_price(0) -> '$0.00' (SPEC: '0.00 EUR')
FAIL: format_price(10000) -> '$100.00' (SPEC: '100.00 EUR')
FAIL: format_price(12345) -> '$123.45' (SPEC: '123.45 EUR')
FAIL: format_price(-50) -> '-$0.50' (SPEC: raises ValueError)
> python3 spec_check.py format_price.conducting.py
PASS
```

Both `test_format_price.py` files pass their OWN tests. Only the conducting file passes the five cases in `SPEC.md`. Bare failed every one — five for five — including turning a negative input into `-$0.50` instead of raising.

## What the runs gave the film

1. **Bare.** Same one sentence, empty folder. Claude picked a currency (dollar), a separator style (thousands with commas), a policy on negatives (allow, prefix `-`), a policy on types (reject non-int, including `bool`). None of that was asked for. Ten test methods, all passing — a green suite that has nothing to do with what the code is for.
2. **Conducting.** Same sentence. Eleven lines of `SPEC.md` first. The plan sentence traces to the file; the implementation is four lines; the tests are the five cases in `SPEC.md`, one for each. The green suite means the thing that was asked for.
3. **The receipt.** `spec_check.py` — the four rules and five cases, as a script — turns the argument into evidence: 5/5 FAILs vs PASS. Both suites are green. Only one is green about the right thing.

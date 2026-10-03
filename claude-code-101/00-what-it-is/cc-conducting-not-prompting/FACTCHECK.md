# FACTCHECK — cc-conducting-not-prompting

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (two real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the two runs' stream-json (`evidence/run-bare.jsonl`, `evidence/run-conducting.jsonl`), the two `format_price.py` and two `test_format_price.py` files in `evidence/`, `SPEC.md`, and `spec_check.py`. Liam's checks were run in a plain shell over `evidence/` and are shown as bang commands inside the session. Claude's sentences are verbatim spans, split into ≤44-char blocks. No model names, version numbers, or costs are shown or spoken.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B03 | The ask, verbatim | PASS | `evidence/ask.txt` | — |
| 2 | B00 | ls, Write \|format\_price.py\|, Write \|test\_format\_price.py\|, python3 unittest -v | PASS | `run-bare.jsonl` tool\_use sequence | — |
| 3 | B00 | "Wrote `format_price.py` — int cents → `$1,234.56`, negative gets a leading `-`, rejects non-ints, including bool." | PASS | verbatim Claude summary text in `run-bare.jsonl`, split into 44-char blocks | — |
| 4 | B00 | "Ran 10 tests in 0.000s — OK" | PASS | `python3 -m unittest test_format_price -v` on the bare files (rerun in evidence) | — |
| 5 | B00, B01 | "Seven lines" for `format_price.py` and "forty-six" for the tests | PASS | `wc -l evidence/format_price.bare.py` → 7; `wc -l evidence/test_format_price.bare.py` → 46 | — |
| 6 | B00, B05 | Bare choices: dollars, thousands separator, minus-prefixed negatives, TypeError on non-ints incl. bool | PASS | `evidence/format_price.bare.py` (`$`, `{dollars:,}`, `sign = "-" if cents < 0 else ""`, `isinstance(cents, bool)` rejection) | — |
| 7 | B01 | The five FAILs, exact string form | PASS | `python3 evidence/spec_check.py evidence/format_price.bare.py`; the three shown are three of the five (the middle two are display-elided for height) | — |
| 8 | B01, B05 | "Ten green tests" | PASS | `grep -c '^    def test' evidence/test_format_price.bare.py` → 10; unittest output "Ran 10 tests" | — |
| 9 | B02 | `wc -l SPEC.md` → 11; the five cases and four rules as shown | PASS | `evidence/SPEC.md`; lines display-truncated at 40 chars for width; the numeric-input arrows are verbatim | — |
| 10 | B03 | Read SPEC.md, ls, Writes, unittest -v; Claude's plan sentence "Splits cents into euros and remainder, zero-pads decimals, raises on negatives." | PASS | `run-conducting.jsonl`; the first `python -m unittest` (no 3) that failed on this box is omitted for height (5 tests, `OK` is the successful `python3 -m unittest` run) | — |
| 11 | B03 | "All 5 tests pass — one per SPEC case." | PASS | `python3 -m unittest test_format_price -v` in evidence; the paraphrase is Claude's own summary line | — |
| 12 | B04 | `wc -l format_price.py` → 4; grep `$` → 0; grep EUR → 1; spec_check → PASS | PASS | `evidence/format_price.conducting.py`; VERIFY block in SESSION.md | — |
| 13 | B04, B05 | Conducting choices: EUR, ValueError on negative, four lines, twenty-five tests | PASS | `evidence/format_price.conducting.py` (` EUR`, `raise ValueError`, 4 lines); `wc -l evidence/test_format_price.conducting.py` → 25; five test methods | — |
| 14 | B05 | Six steps, tally PF 2 · PA 1 · IJ 1; dangerous middle at step 3 (reading the bare file) | PASS | maps to SESSION.md's two-run structure | — |
| 15 | B06 | Ledger rows — Claude's picks; the conducting run reading SPEC first | PASS | `run-conducting.jsonl` (Read SPEC.md is turn 1); the four-lines-from-a-spec claim traces to file wc | — |
| 16 | BVDT | "-\$0.50 for a negative" | PASS | `python3 evidence/spec_check.py evidence/format_price.bare.py` line: `format_price(-50) -> '-$0.50'` | — |
| 17 | BVDT | "5 tests, one per SPEC case; PASS" | PASS | `evidence/test_format_price.conducting.py`; `python3 -m unittest` "Ran 5 tests"; `spec_check.py` → PASS | — |
| 18 | BHTF | The viewer's prompt | EXEMPT | instruction, not a factual claim | — |
| 19 | all | Model/version/date strings; costs ($0.339 / $0.385) | EXEMPT | not shown or spoken | — |

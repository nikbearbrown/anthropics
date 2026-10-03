# FACTCHECK — cc-prompt-is-a-wish-spec-is-a-contract

Status: PASS — checked 2026-09-10 by the build session against `SESSION.md` (three real headless `claude -p` runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the three runs' stream-json (`evidence/run-{wish,spec,testsonly}.jsonl`), the three `auth.py` outputs (`evidence/auth.{wish,spec,testsonly}.py`), and Liam's plain-shell VERIFY block reproduced from those files. Claude's spoken lines are verbatim spans from the run transcripts. The source concept (a prompt is a wish; a spec is a contract) is kept; the concept sheet's fictional cast (Seth, Tomas) and the source book's numeric claims are not used.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1  | B00       | The ask, verbatim — `Write me a login function.` | PASS | `evidence/ask-wish.txt`; `run-wish.jsonl` initial user turn | — |
| 2  | B00       | The AskUserQuestion attempt was denied by the tool fence | PASS | `run-wish.jsonl` \| tool `AskUserQuestion` result: permission denied | — |
| 3  | B00       | Claude's line: "without a spec you get my guess, not your answer" | PASS | `run-wish.jsonl` assistant text (verbatim span) | — |
| 4  | B00       | 40 lines, three functions | PASS | `wc -l wish/auth.py` → 40; `grep -c "^def " wish/auth.py` → 3 | — |
| 5  | BIDEA     | Writer types four lines; the word "clear" is corrected to "a contract" | EXEMPT | authorial framing — the corrected word is the misconception the film fixes | — |
| 6  | BDEFS     | Definitions of five terms (prompt, specification, invariant, boundary, handoff condition) | EXEMPT | pedagogical definitions, high-level and standard | — |
| 7  | B01       | `wc -l wish/auth.py` → 40; `grep -c "^def " wish/auth.py` → 3 | PASS | direct evidence commands | — |
| 8  | B01       | The three functions include a `login()` nobody asked for | PASS | `grep "^def " wish/auth.py`; `SPEC.md` names two functions only | — |
| 9  | B01       | `python3 -m unittest test_auth.py` in `wish/` → 1 failure (`test_empty_password_raises`) | PASS | run in the build session; reproducible | — |
| 10 | B01       | Claude's own text: "Choices I made without asking — flag any you'd rather change" | PASS | `run-wish.jsonl` final assistant text (verbatim) | — |
| 11 | B02       | SPEC.md is 22 lines; five invariants; two-function interface; handoff = `python3 -m unittest test_auth.py` reports OK | PASS | `wc -l SPEC.md`; the SPEC's own numbered sections | — |
| 12 | B03       | The spec run reads SPEC.md and test_auth.py before writing | PASS | `run-spec.jsonl` tool calls in order (Bash ls, Read SPEC.md, Read test_auth.py, Write auth.py, Bash unittest) | — |
| 13 | B03       | `python3 -m unittest test_auth.py` → `Ran 5 tests in 0.058s / OK` | PASS | Claude's own Bash tool result in `run-spec.jsonl` and Liam's verification | — |
| 14 | B04       | `wc -l spec/auth.py` → 33; two functions; 100 000 iterations; `secrets.token_bytes` | PASS | direct commands over `evidence/auth.spec.py` | — |
| 15 | B04       | `verify_password("", stored)` in the spec output raises `ValueError` | PASS | direct `python3 -c` run against `spec/auth.py` | — |
| 16 | B05       | The middle case: tests in the folder, no SPEC; Claude says "the spec is the tests" | PASS | `run-testsonly.jsonl` assistant text (verbatim) | — |
| 17 | B05       | 34 lines, all 5 tests OK, but `os.urandom` instead of `secrets`, 200 000 iters instead of SPEC's 100 000, `verify_password("", stored)` silently returns `False` | PASS | direct commands over `evidence/auth.testsonly.py` | — |
| 18 | B06       | CONDUCT step tally matches the session (three PF/two IJ/one PA) | PASS | maps to `SESSION.md` and this file's row assignments | — |
| 19 | B07       | Ledger rows all trace to session events | PASS | each row: one anchoring line in `SESSION.md` / `run-*.jsonl` | — |
| 20 | BVDT      | Verdict lines: 40 lines wish (1 fail, extra function); 33 lines spec (OK, both empties raise); tests-only passes but drifts | PASS | rows 4, 7–9, 14–17 | — |
| 21 | BHTF      | The viewer's prompt (a SPEC-writing ask) | EXEMPT | instruction to viewer | — |
| 22 | all       | Model/version strings; costs (`$0.287 / $0.271 / $0.334`) | EXEMPT | recorded in this file, not shown or spoken | — |
| 23 | all       | Datable strings ("as of 2026-", model names, prices) | EXEMPT | none in narration | — |

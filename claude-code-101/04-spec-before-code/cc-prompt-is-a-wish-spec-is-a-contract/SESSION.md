# SESSION.md — cc-prompt-is-a-wish-spec-is-a-contract

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Three fresh headless `claude -p` runs, Claude Code 2.1.150, model `claude-opus-4-7[1m]`, 2026-09-10. All under one scratch project (`scratch/`): a two-function password module for a study group's practice project. Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`; `--permission-mode acceptEdits`. Raw stream-json in `evidence/run-{wish,spec,testsonly}.jsonl`; the three outputs in `evidence/auth.{wish,spec,testsonly}.py`; inputs (`README.md`, `SPEC.md`, `test_auth.py`, `ask-wish.txt`, `ask-spec.txt`) in `evidence/`.

## The three conditions

| Condition | What was in the folder | The ask (verbatim) |
|---|---|---|
| **wish** | `README.md` (5 lines) | `Write me a login function.` |
| **spec** | `README.md`, `SPEC.md` (5 invariants + boundary + handoff), `test_auth.py` | `Read SPEC.md, then build auth.py per its conditions. Then run python3 -m unittest test_auth.py.` |
| **testsonly** | `README.md`, `test_auth.py` | `Write me a login function.` |

`test_auth.py` (in `evidence/`) is the checker: five `unittest` cases — round-trip, wrong-password rejected, empty-password raises `ValueError`, stored is not plaintext, stored is not the MD5 of the password. `SPEC.md` names two functions (`hash_password`, `verify_password`), five invariants (empty raises, no plaintext, `pbkdf2_hmac` sha256 ≥100k, per-call `secrets.token_bytes` salt, `hmac.compare_digest`), a boundary (touch `auth.py` only, stdlib only), and a handoff (`python3 -m unittest test_auth.py` reports OK).

## Run: wish (session `30609798-…`)

- **TOOL** `AskUserQuestion` (three clarifying questions — language, mechanism, session type) — **denied by tool fence**.
- **CLAUDE:** "Looks like the question prompt got dismissed — so I'll pick a reasonable default and flag the tradeoff, per the folder's own point (a prompt is a wish; without a spec you get *my* guess, not *your* answer). Default I'll write: **TypeScript**, **email + password with argon2**, returns a **user + signed session token**…"
- **TOOL** `Bash` `ls …/wish/` · **Read** `README.md`
- **CLAUDE:** "The README changes everything: **Python 3, stdlib only, study-group password module**. Writing that."
- **TOOL** `Write` `auth.py` (40 lines)
- **CLAUDE:** "Wrote `auth.py` with three functions: `hash_password`, `verify_password`, `login(username, password, users)`. Uses `pbkdf2_hmac` (stdlib), per-password salt, `hmac.compare_digest` for timing-safe compare, and a dummy verify on missing user so timing doesn't leak account existence. Choices I made without asking — flag any you'd rather change: PBKDF2-SHA256, 200k iterations; `users: dict[str, str]` as the store; returns `bool`, doesn't issue a session…"
- **RESULT:** success · turns=5 · 45.2 s · $0.287

## Run: spec (session `…`)

- **TOOL** `Bash` `ls …/spec/` · **Read** `SPEC.md` · **Read** `test_auth.py`
- **TOOL** `Write` `auth.py` (33 lines) · **TOOL** `Bash` `python3 -m unittest test_auth.py` → `Ran 5 tests in 0.058s / OK`
- **CLAUDE:** "Done. `auth.py` implements `hash_password` / `verify_password` using PBKDF2-HMAC-SHA256 (100k iterations, 16-byte salt from `secrets`, `hmac.compare_digest` for the digest check). `python3 -m unittest test_auth.py` reports OK, 5 tests run."
- **RESULT:** success · turns=6 · 24.1 s · $0.271

## Run: testsonly (session `…`)

- **TOOL** `AskUserQuestion` (stack + auth-model clarifiers) — **denied**.
- **CLAUDE:** "**Assumptions**: Node.js + Express, email + password with bcrypt, JWT returned on success…"
- **TOOL** `Bash` `ls …/testsonly` · **Read** `README.md` · **Read** `test_auth.py`
- **CLAUDE:** "The repo already answers my questions — the README says 'tiny password module, Python 3 stdlib only,' and `test_auth.py` is labeled 'the definition of done for auth.py.' The contract is two functions: `hash_password` and `verify_password`. My earlier stack questions were wrong to ask; **the spec is the tests**."
- **TOOL** `Write` `auth.py` (34 lines) · **TOOL** `Bash` `python3 -m unittest test_auth.py -v` → `OK`
- **CLAUDE:** "All 5 tests pass. `auth.py` implements the contract from `test_auth.py`: PBKDF2-HMAC-SHA256, 200k iterations, random 16-byte salt, constant-time compare on verify, `ValueError` on empty password."
- **RESULT:** success · turns=7 · 54.5 s · $0.334

## Liam's VERIFY (plain shell, run against `evidence/` copies of each `auth.py`)

```
> wc -l wish/auth.py spec/auth.py testsonly/auth.py
      40 wish/auth.py
      33 spec/auth.py
      34 testsonly/auth.py
> grep -c "^def " wish/auth.py spec/auth.py testsonly/auth.py
wish/auth.py:3
spec/auth.py:2
testsonly/auth.py:2
> grep "^def " wish/auth.py
def hash_password(password: str) -> str:
def verify_password(password: str, stored: str) -> bool:
def login(username: str, password: str, users: dict[str, str]) -> bool:
> grep -oE "[0-9]+_000" wish/auth.py spec/auth.py testsonly/auth.py | head -3
wish/auth.py:200_000
spec/auth.py:100_000
testsonly/auth.py:200_000
> grep -oE "secrets\.token_bytes|os\.urandom" wish/auth.py spec/auth.py testsonly/auth.py
wish/auth.py:secrets.token_bytes
spec/auth.py:secrets.token_bytes
testsonly/auth.py:os.urandom
> ( cd wish && python3 -m unittest test_auth.py )
FAIL: test_empty_password_raises — ValueError not raised
Ran 5 tests in 0.122s / FAILED (failures=1)
> ( cd spec && python3 -m unittest test_auth.py )
Ran 5 tests in 0.058s / OK
> ( cd testsonly && python3 -m unittest test_auth.py )
Ran 5 tests in 0.103s / OK
> python3 -c "import auth; s=auth.hash_password('x'); print(auth.verify_password('', s))"      # spec
Traceback (most recent call last):  … ValueError: empty password
> python3 -c "import auth; s=auth.hash_password('x'); print(auth.verify_password('', s))"      # testsonly
False
```

## What the runs gave the film

1. **Wish**: 40 lines. Claude tried to ask three clarifying questions first (denied), then said the honest thing on camera — *"without a spec you get my guess, not your answer"* — and made the guesses anyway: 200 000 iterations, a `dict[str, str]` store, and a **third function nobody asked for** (`login(username, password, users)` with a timing-side-channel dummy verify). Modern defaults are hygienic — pbkdf2, salt, `compare_digest` — but the one invariant nobody named silently broke: `hash_password("")` returns a hash instead of raising. 4 of 5 tests pass; 1 fails. The wish gave you the model's decisions, not yours.
2. **Spec**: 33 lines. Every line traces to a numbered SPEC condition. Two functions, no third. `secrets.token_bytes` because the SPEC named it. 100 000 iterations because the SPEC said ≥100 000 and Claude reads the bound literally. Both `hash_password("")` and `verify_password("", stored)` raise. `python3 -m unittest test_auth.py` reports `OK`, 5 tests run — the handoff, on the page.
3. **Middle**: 34 lines. Given the tests but no spec, Claude reads them and *names the rule out loud*: **"the spec is the tests."** All 5 pass. But `os.urandom` instead of `secrets` (the tests can't tell). 200 000 iterations, the model's default (the tests only require pbkdf2). `verify_password("", stored)` silently returns `False` instead of raising (the tests don't check the empty-verify case). Passed the checker, drifted from the SPEC on every invisible axis. Done is a script; every decision the script cannot see, someone still made — and if it wasn't you, it was Claude.

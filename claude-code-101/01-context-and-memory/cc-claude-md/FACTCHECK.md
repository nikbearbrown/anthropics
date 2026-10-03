# FACTCHECK — cc-claude-md

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (three real headless Claude Code runs: session `fe0edef3-…` turns 1–2, and a fresh session for turn 3) and `evidence/`.

**Verification boundary.** Every factual claim in this reel is about runs that happened on 2026-09-08 and are transcribed in `SESSION.md`, with raw stream-json, the file at each stage, and diffs in `evidence/`. Two product claims (rows 2, 3) are about Claude Code itself and are sourced. Commands Liam ran in the shell are shown as bang commands inside the session shell (same command, same output; the `zsh:` prefix on "command not found" is dropped for width). The two closing-block beats apply doctrine from two INFO-7375 courses; the doctrine is cited, not re-derived.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | `/init` typed; `ls -la`, then four Reads (README, gradebook.py, test_gradebook.py, .gitignore) before the Write | PASS | `SESSION.md` Turn 1; `evidence/turn1.jsonl` (the `find` call between `ls` and the Reads is omitted on screen for height) | — |
| 2 | B00, BIDEA, BDEFS | "Claude Code reads CLAUDE.md first, every session, in the folder you opened" | PASS | Claude Code docs (memory / CLAUDE.md: auto-loaded into context at session start from the working directory and its parents); `claude --help` `--bare` text: "CLAUDE.md auto-discovery" | — |
| 3 | BDEFS | `/init` "reads your project and drafts a CLAUDE.md" | PASS | Turn 1 is the demonstration; the file's own first line says what it is for | — |
| 4 | B00, B03 | Status-line figures | EXEMPT | kit chrome; headless prints none; real timing in RESULT lines | — |
| 5 | B01 | "seventeen lines"; the quoted Commands and Architecture lines | PASS | `wc -l CLAUDE.md` → 17; `evidence/CLAUDE.md.init`. On screen the architecture paragraph is elided with `…` between two verbatim spans | — |
| 6 | B02 | `pytest` → "command not found: pytest"; `python3 -m pytest -q` → "No module named pytest" | PASS | `SESSION.md` → VERIFY after turn 1 (the interpreter path prefix is dropped on screen) | — |
| 7 | B02 | "It wrote what most Python projects do, not what this Mac has" | PASS | pytest is the common Python test runner; not installed here (row 6) | — |
| 8 | B03 | Liam's correction, verbatim | PASS | `evidence/ask2.txt` | — |
| 9 | B03 | `Write tests/test_gradebook.py`; `Bash python tests/test_gradebook.py` → "This command requires approval"; `AskUserQuestion`; "I'll proceed without running the verification."; two Edits to CLAUDE.md | PASS | `SESSION.md` Turn 2. The first blocked call was the chained one; the single call shown is the second, verbatim. The Edit children carry the heads of the two `old_string`s | — |
| 10 | B03 | "python isn't on my allow-list, only python three" | PASS | the session's `--allowedTools` (SESSION.md header): `Bash(python3:*)`, no `python` | — |
| 11 | B04 | The CLAUDE.md diff lines; "I was not able to verify the commands run (verification was declined), so please run one to confirm." | PASS | `evidence/claude-md.turn2.diff`; Turn 2 CLAUDE, last sentence. Two of the four changed pairs are shown | — |
| 12 | B05 | `python3 tests/test_gradebook.py` → "Ran 1 test in 0.002s / OK"; `grep -n "Run tests" CLAUDE.md` → line 8; `which python` → "python: aliased to python3" | PASS | `SESSION.md` → VERIFY after turn 2; the grep line is display-shortened with `…` | — |
| 13 | B06 | Liam's one-line ask, verbatim; Read, Edit, Edit; "Now add a test following the existing pattern."; the blocked run; the handback sentences | PASS | `evidence/ask3.txt`; `SESSION.md` Turn 3 (one Read of two shown; "the existing pattern" shortened to "the pattern" on screen for width; handback quoted with `…` elisions) | — |
| 14 | B06 | "no memory of anything above" | PASS | a new `claude -p` with no `--resume`; its own init event (`evidence/turn3.jsonl`) | — |
| 15 | B06 | "a top-level function, one entry in the dict, a test in the existing pattern" | PASS | `evidence/gradebook.turn3.diff`; `evidence/test_gradebook.py` (`test_remove` in the same `TestGradebook` class, same tempfile pattern) | — |
| 16 | B07 | `git diff --stat` → "2 files changed, 31 insertions(+)" (shown as one line); the dispatch line (display-shortened: the dict without `[cmd](*args)`, the add line elided with `…`); `python3 tests/test_gradebook.py` → "Ran 2 tests in 0.002s / OK"; `sed` → `python3`; `grep -c python3 CLAUDE.md` → 3 | PASS | `SESSION.md` → VERIFY after turn 3; "Ran 2 tests in 0.002s — OK" joins two output lines on one screen line | — |
| 17 | B07 | "Remove on a missing student says so instead of crashing; that branch was tested too" | PASS | `python3 src/gradebook.py remove ada` → "no such student: ada"; `test_remove` covers the missing-student branch (Turn 3 CLAUDE) | — |
| 18 | B08 | Six steps, handoffs, tally PF 1 · PA 1 · TO 1 · IJ 0 · EI 0 | PASS | each step maps to a `SESSION.md` turn or VERIFY block | — |
| 19 | B09 | Ledger rows ("it did" rows → Turn 2's last sentence; Turn 3's handback) | PASS | `SESSION.md` | — |
| 20 | BVDT | Verdict lines | PASS | rows 5, 6, 11, 15, 16 | — |
| 21 | BHTF | The viewer's prompt | EXEMPT | an instruction to the viewer | — |
| 22 | all | Version / model strings | EXEMPT | none shown or spoken | — |
| 23 | metadata | Run costs (turn 1 $0.249, turn 2 $0.410, turn 3 $0.321) | EXEMPT | recorded in `SOURCES.md`, not spoken | — |

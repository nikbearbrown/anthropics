# FACTCHECK — cc-pretooluse-grade-blocker

Status: PASS — checked 2026-09-10 by the build session against `SESSION.md` (three real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the three runs' stream-json, the two summary files on disk, the hook source, the wired `settings.local.json`, and the three payloads under `evidence/`. Liam's checks were run in a plain shell (`python3 hooks/block-grades.py < evidence/*.json`) and are shown as bang commands inside the terminal. Claude's sentences are verbatim spans, display-elided at the kit's row width. The source concept's framing (grade-generation blocked by a PreToolUse hook) is kept; no model or version number is spoken.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1  | B00 | The summary ask, verbatim | PASS | `scratch/ask.txt`; the four prompt blocks are the ask split at clause boundaries | — |
| 2  | B00 | Bare run: Read `students.csv`, Write `summary.md`, "three grades" | PASS | `evidence/run-bare.jsonl`; the file's three graded lines are archived in `evidence/summary.bare.md` | — |
| 3  | B00, BSHOW | "three suggested letter grade" (A-, C, B+) | PASS | `grep -oE "Suggested letter grade: \*\*[A-F][+-]?" evidence/summary.bare.md` → 3 matches | — |
| 3b | BDEFS | Five terms: PreToolUse · tool_input · matcher · exit 2 · settings.json (each defined at one plain line) | PASS | authored per the CCDefinitions contract; the numeric claim "five" is the count of `terms[]` in the beat's props | — |
| 4  | B01 | Spec beats: read tool_input, match, exit 2; Claude "mkdir -p hooks"; Write `hooks/block-grades.py` "36 lines" | PASS | `evidence/run-build.jsonl` tool sequence; `wc -l scratch/hooks/block-grades.py` → 36 | — |
| 5  | B02 | "Claude Code refuses to write `.claude/settings.local.json` … permission-guarded" | PASS | `evidence/run-build-resume.jsonl` — Claude prints the JSON and says the permission dialog is pending; the file was never written by Claude Code | — |
| 6  | B03 | 15 lines of JSON wiring; matcher `Write\|Edit\|MultiEdit`; command `python3 …/block-grades.py` | PASS | `wc -l scratch/.claude/settings.local.json` → 15; `evidence/settings.local.json` contents | — |
| 7  | B04 | Three payloads, three exits: `bad.json` → exit 2 + stderr; `quantity.json` → exit 0; `ok.json` → exit 0 | PASS | run in the build session, transcript in the SESSION VERIFY block; regenerable via `python3 hooks/block-grades.py < evidence/<name>.json` | — |
| 8  | BFLOW | The PreToolUse pipeline (six nodes, six edges: claude → harness → hook/stdin → exit 2 → denied → retry) | PASS | Claude Code hooks documentation (public); every node label traces to `evidence/run-hooked.jsonl` and `evidence/block-grades.py` (`stdin`, `exit 2`, `stderr`, `is_error` on the tool result) | — |
| 9  | B05 | Hooked run: Read `students.csv`, Write blocked, stderr "refusing to write a final letter grade → 'grade: A'", Read `hooks/block-grades.py` | PASS | `evidence/run-hooked.jsonl`; the block message is archived verbatim as `evidence/hook-block-message.txt` | — |
| 10 | BSHOW | `wc` counts 13 (bare) and 17 (hooked); `grep -cE 'grade:? [A-F][+-]?'` → 3 (bare) and 0 (hooked); footer line "the teacher assigns final letter grades." | PASS | `wc -l evidence/summary.bare.md evidence/summary.hooked.md`; `grep` counts; footer is in `evidence/summary.hooked.md` line 17 | — |
| 11 | BSHOW | "fifty-one lines of scaffolding" | PASS | 36 (hook) + 15 (settings) = 51; `wc -l scratch/hooks/block-grades.py scratch/.claude/settings.local.json` → 51 total | — |
| 12 | BCONDUCT | Six steps; PF/PA/TO tally on the score; dangerous middle = step 3 (Claude tried to Write settings.local.json and was refused) | PASS | maps to `SESSION.md`; the refusal in `run-build-resume.jsonl` | — |
| 13 | BHUMAN | Ledger rows: AI drafted the hook, read the wall, retried, refused to wire itself; human decides the pattern, picks the matcher, wires settings, unit-tests | PASS | every row is an action recorded in `SESSION.md` or `evidence/` | — |
| 14 | BVDT | Verdict recap; "36 lines of hook and refused to wire it; the human wired 15" | PASS | rows 4, 5, 6, 10 above | — |
| 15 | BVDT | "FALSIFIABLE: a bare run that refuses the letter-grade line on its own" | PASS | falsification statement — verifiable by rerunning `evidence/run-bare.jsonl` conditions and inspecting `summary.md`; not spoken as fact but as counter-example | — |
| 16 | BHTF | The viewer's prompt | EXEMPT | instruction — no factual claim | — |
| 17 | all | Model / version / cost strings (Claude Code 2.1.150; per-run cost) | EXEMPT | recorded in `SESSION.md` and stream-json; never spoken or shown on screen | — |
| 18 | all | The three student names (Ada / Boris / Cai) and their scores | EXEMPT | synthetic fixture in `scratch/students.csv`; not a real gradebook | — |

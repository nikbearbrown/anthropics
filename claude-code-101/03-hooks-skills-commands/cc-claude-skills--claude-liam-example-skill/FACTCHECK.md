# FACTCHECK — cc-claude-skills--claude-liam-example-skill

Status: PASS — checked 2026-09-10 by the build session against `SESSION.md` (three real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the three runs' stream-json, the two SKILL.md variants, and the three `peek.md` outputs in `evidence/`. Liam's checks were run in a plain shell on the evidence folder. Claude's sentences are verbatim spans (truncated with `…` when they wrap the kit's 44-character text-block budget). The source concept's framing (skills vs commands vs agents; description-as-trigger) is kept; its Copyright Office citation is not used.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | example-skill/SKILL.md frontmatter head -6 output | PASS | `evidence/example-skill.SKILL.md` lines 1-6 (display-truncated at 44 chars) | — |
| 2 | B00 | "eighty-four lines" | PASS | `wc -l evidence/example-skill.SKILL.md` → 84 | — |
| 3 | B00 | "two frontmatter fields required" | PASS | evidence/example-skill.SKILL.md §Frontmatter Options (name, description required; version, license optional) | — |
| 4 | BIDEA | The idea, in the writer's four lines | PASS | authorial framing over the three real runs; the corrected word ("decoration"→"the shape") is the film's misconception | — |
| 5 | BDEFS | Four term definitions (skill, frontmatter, description, definition of done) | PASS | high-level definitions for the chat-window audience — not domain jargon | — |
| 6 | B01 | Run A: no skill folder, `ls`/`Read`/`wc`/`Write` in that order; ad-hoc shape (title, bullets, first-rows table, last-rows table, quick notes) | PASS | `evidence/run-bare.jsonl` (5 turns, 25.0s, $0.174); `evidence/peek.bare.md` | — |
| 7 | B01 | Claude's line "Wrote peek.md — 6 columns, 9 data rows, head and tail samples, and a few notes." | PASS | `run-bare.jsonl` assistant text (paraphrased at 44-char clause boundaries; wording untouched) | — |
| 8 | B02 | `wc -l peek.md` → 28; grep for `^## FILE:` → 0; check_peek.py → FAIL | PASS | `evidence/peek.bare.md` (28 lines); grep run in this session; `python3 evidence/csv-peek.check_peek.py evidence/peek.bare.md` → FAIL | — |
| 9 | B03 | `wc -l csv-peek/SKILL.md` → 40; head -4 shows fence, name, description; grep for `^## ` → 6 | PASS | `evidence/csv-peek.full.SKILL.md` — 40 lines, 6 `## ` headings | — |
| 10 | B04 | Run B: `Skill(csv-peek)` fires from description-alone; peek.md in the 4-heading shape; check_peek.py PASS | PASS | `evidence/run-full.jsonl` (7 turns, 19.8s, $0.182): 1 Skill call, 1 Write, 1 Bash check → PASS; `evidence/peek.full.md` 5 lines with `## FILE: / ## ROWS: 9 / ## COLUMNS: … / ## HEAD:` | — |
| 11 | B05 | `wc -l` → 4; `cat` shows only the fence + name + description + fence | PASS | `evidence/csv-peek.bare-front.SKILL.md` — 4 lines exactly (the description text wraps but is one YAML line) | — |
| 12 | B06 | Run C: `Skill(csv-peek)` STILL fires; writes peek.md with lowercase headings and no automatic checker call | PASS | `evidence/run-bare-front.jsonl` (7 turns, 25.7s, $0.179): 1 Skill call, Read of the 4-line SKILL.md, Write; no `check_peek.py` Bash call; `evidence/peek.bare-front.md` uses `file:` `rows:` `columns:` `first 3 data rows:` | — |
| 13 | B07 | `wc -l peek.md` → 7; grep `^## FILE:` → 0; check_peek.py → FAIL | PASS | `evidence/peek.bare-front.md` (7 lines); grep run in this session; `python3 evidence/csv-peek.check_peek.py evidence/peek.bare-front.md` → FAIL | — |
| 14 | B08 | Six CONDUCT steps; dangerous middle at step 3 (template-as-instructions confusion); tally implied PF 2 · PA 1 · IJ 1 · TO 0 · EI 0 | PASS | Maps to SESSION.md (Runs A / write full skill / Run B / gutted-body / Run C) | — |
| 15 | B09 | Ledger rows — all four AI CAN/SHOULD rows verified in run-full and run-bare-front; all four human MUST/SHOULD rows are the film's argument | PASS | `run-full.jsonl` (Skill call, Write in exact shape, Bash-runs-checker, Claude's summary names the skill); the four HUMAN rows are load-bearing decisions | — |
| 16 | BVDT | Verdict lines — description-as-trigger verified twice; body-as-decoration falsified by Run C | PASS | Rows 1, 10, 12; FALSIFIABLE line is a testable claim | — |
| 17 | BHTF | The viewer's prompt | EXEMPT | instruction — a suggested next action, not a claim | — |
| 18 | all | Model/version strings; costs ($0.174 / $0.182 / $0.179); dates | EXEMPT | not spoken or shown on screen | — |

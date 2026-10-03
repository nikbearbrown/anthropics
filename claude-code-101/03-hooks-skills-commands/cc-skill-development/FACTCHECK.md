# FACTCHECK — cc-skill-development

Status: PASS — checked 2026-09-10 by the build session against `SESSION.md` (three real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the three runs' stream-json (`evidence/run-{bare,rules,checker}.jsonl`), the three shipped SKILL.md files (`evidence/SKILL.{bare,rules,checker}.md`) and one references file (`evidence/troubleshooting.rules.md`), the scratch inputs (`evidence/csv_shape.py`, `sample.csv`, `validate_skill.py`, `README.md`), and Liam's plain-shell VERIFY block in `SESSION.md`. Claude's completion sentences are verbatim spans, wrapped at kit block boundaries. No spoken numbers date the reel (no model names, no versions, no "as of").

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B03 | The one-line asks, verbatim | PASS | the argv to `claude -p` in each run (see SESSION.md) | — |
| 2 | B00 | "Four Reads · mkdir · Write · validate_skill.py PASS"; "630 words. Third-person description. References csv\_shape.py." | PASS | `run-bare.jsonl` tool sequence and final assistant text | — |
| 3 | B00, B01 | "Six hundred thirty words" | PASS | `wc -w evidence/SKILL.bare.md` → 630 | — |
| 4 | B01 | The bare SKILL.md's frontmatter head (name, description); ls shows one file; second-person grep → 0 | PASS | `head -3 evidence/SKILL.bare.md`; `ls scratch/run-bare/skills/csv-shape` → `SKILL.md`; `grep -Ec "you should\|you need\|you can\|you must\|you may" evidence/SKILL.bare.md` → 0 | — |
| 5 | B01, B04 | "four quoted trigger phrases" (bare frontmatter) | PASS | the four quoted phrases in `evidence/SKILL.bare.md` line 3: "what's in this CSV", "show me the shape of this CSV", "how many rows and columns does this file have", "inspect this CSV before I load it" | — |
| 6 | B02 | "635 words, six rules"; "Five quoted trigger phrases"; "No second-person forms"; ls → one file | PASS | `run-checker.jsonl` assistant text and tool trace; `wc -w evidence/SKILL.checker.md` → 635; five quoted triggers in line 3; `grep -Ec "…"` → 0; `ls scratch/run-checker/skills/csv-shape` → `SKILL.md` | — |
| 7 | B02 | "The letters, none of the spirit. The checker cannot see progressive disclosure — it can only count words and grep for 'you should'." | PASS | narration characterisation of `validate_skill.py`; the six rules the checker enforces are visible in `evidence/validate_skill.py` | — |
| 8 | B03 | The rules ask, verbatim (paraphrased for the prompt block to fit); Reads × 3, mkdir references/, Write SKILL.md, Write references/troubleshooting.md, validate_skill.py PASS: 367 | PASS | `run-rules.jsonl` tool sequence and final PASS text | — |
| 9 | B03, B04, BVDT | "Three hundred sixty-seven words" | PASS | `wc -w evidence/SKILL.rules.md` → 367 | — |
| 10 | B04, BVDT | "Five hundred fifty-two words in references/troubleshooting.md" | PASS | `wc -w evidence/troubleshooting.rules.md` → 552 | — |
| 11 | B04 | Line 46 in SKILL.rules.md points at `references/troubleshooting.md` | PASS | `grep -n reference evidence/SKILL.rules.md` → line 46: "consult `references/troubleshooting.md`" | — |
| 12 | BFLOW1 | "SKILL.md required · everything else optional"; the four folder children (SKILL.md, references/, scripts/, assets/) | PASS | the source skill `anthropics/claude-code/plugins/plugin-dev/skills/skill-development/SKILL.md` §"Anatomy of a Skill" — SKILL.md required; references/, scripts/, assets/ optional | — |
| 13 | BSHOW1 | The three quoted trigger phrases shown ("what's in this csv", "shape of this csv", "describe this csv") | PASS | `evidence/SKILL.rules.md` line 3 frontmatter; the six triggers in the description; three chosen for the shell display, in order of appearance | — |
| 14 | BCOND | Six steps; tally PF 2 · PA 1 · IJ 1 · TO 0 · EI 0; dangerousMiddle=3 | PASS | maps to SESSION.md: step 1 (my one-liner), step 2 (bare run), step 3 (I read the folder and noticed no references — PA), step 4 (I named the three rules — PF), step 5 (rules run), step 6 (I judged the checker-only run — IJ). TO and EI were not exercised. | — |
| 14b | BCOND | Every spoken quantity: "six hundred thirty", "three hundred sixty-seven"; "one" (file) | PASS | 630 = `wc -w evidence/SKILL.bare.md`; 367 = `wc -w evidence/SKILL.rules.md`; "one file" = `ls scratch/run-bare/skills/csv-shape` → `SKILL.md` | — |
| 15 | BHUM | Ledger rows (AI CAN/SHOULD; HUMAN MUST/SHOULD) | PASS | grounded in the three runs: Claude filled a silence with one big file (bare + checker); honoured the three rules once given them (rules); ran the checker itself in all three runs; the rules run pointed at its own references/troubleshooting.md; I named the six trigger phrases in the frontmatter I approved; I decided what belongs in body vs references; I checked the folder (`ls`) not just the checker | — |
| 16 | BVDT | Verdict lines 1–3 | PASS | rows 3, 9, 10, 6 | — |
| 17 | BVDT | Falsifiable line: "a bare run that writes a references/ folder on its own" | PASS | a testable prediction — repeating the bare ask and watching for `mkdir references` would decide the reel wrong | — |
| 18 | BHTF | The viewer's prompt | EXEMPT | instruction, not a claim about the world | — |
| 19 | metadata | Model names / prices / costs / dates | EXEMPT | recorded in SESSION.md and run-\*.jsonl, not spoken or shown | — |

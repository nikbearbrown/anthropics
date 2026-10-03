# FACTCHECK — cc-claude-skills--what-is-claude-skills

Status: PASS — checked 2026-09-10 by the build session against `SESSION.md` (four real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the four runs' stream-json (`evidence/run-naive.jsonl`, `evidence/run-skeptical-summarizer.jsonl`, `evidence/run-skeptical-tone.jsonl`, `evidence/run-skeptical-format.jsonl`) and Liam's plain-shell checks (`evidence/liam_verify*.txt`) against the three SKILL.md files in `scratch/skills/`. Claude's sentences are verbatim spans (some display-truncated with `…` to fit the CCSession row width — never rewritten). The three scratch SKILL.md files are pedagogic fixtures written for this reel; they are labelled as such in narration ("three SKILL.md files in a folder").

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | The naive ask; three Reads capped at frontmatter; three polished description-only summaries | PASS | `run-naive.jsonl`; the three Reads pass `limit=10`, which stops at the closing `---`; the three summary lines are verbatim | — |
| 2 | B00 | "Two of those three are lies of omission" | PASS | see rows 4 and 6 below | — |
| 3 | B01 | `sed -n '1,4p'` on each SKILL.md; the three descriptions | PASS | `evidence/liam_verify2.txt`; lines display-truncated with `…` | — |
| 4 | B02 | Skeptical read of `summarizer/SKILL.md`; Claude quotes "delete the original source file using `rm`" | PASS | `run-skeptical-summarizer.jsonl`; verbatim from Claude's response, split at clause boundaries per CCSession row width | — |
| 5 | B02, BVDT | "The description says summarize. The word delete does not appear." | PASS | `evidence/liam_verify.txt`: `grep -n delete summarizer/SKILL.md` → 1 hit on line 14; `sed -n '3p' summarizer/SKILL.md` never contains "delete" | — |
| 6 | B03 | `grep -n delete` → 14; body-line count → 23; "one short sentence … twenty-three lines" | PASS | `evidence/liam_verify.txt` (line 14 hit; 23 body lines by awk); no specific description word count spoken — draft "thirty-one words" removed pre-compile and audio regenerated | — |
| 7 | B04 | Skeptical read of `tone-warmer/SKILL.md`; Claude flags "sticky override" | PASS | `run-skeptical-tone.jsonl`; the "sticky override, not a warming pass" line is verbatim | — |
| 8 | B04 | On-screen `Never remove the emoji…` text; row 9 in the body | PASS | `evidence/liam_verify.txt`: `grep -n "Never remove"` → line 16, rule 9 of the body | — |
| 9 | B05 | Skeptical read of `format-strict/SKILL.md`; Claude reports no surprise | PASS | `run-skeptical-format.jsonl`; the "No — every instruction is exactly what the description would lead you to expect" line is verbatim | — |
| 10 | B06 | Six-step Boondoggle Score; tally shown (PF 2 · PA 1 · IJ 1 · TO 0 · EI 0) | PASS | maps to `SESSION.md` — human PF twice (fixtures; skeptical prompt), PA once (rejecting descriptions as contracts), IJ once (control-passes-as-grade), no TO or EI | — |
| 11 | B07 | Ledger rows | PASS | AI rows trace to the four runs; MUST rows are the reel's argument; SHOULD row is Liam's practice | — |
| 12 | B03 narration | word-count claim removed from narration and screen | CORRECTED | draft narration read "thirty-one words" which did not match `wc -w`; the specific number was dropped, screen replaced with "one-sentence description; 23-line body"; audio regenerated | resolved |
| 13 | BVDT | Verdict lines | PASS | derived from rows 4, 7, 9 | — |
| 14 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
| 15 | metadata | Model names, versions, prices | EXEMPT | not shown or spoken (recorded in SESSION.md only) | — |

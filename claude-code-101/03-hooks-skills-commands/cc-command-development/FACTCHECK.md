# FACTCHECK — cc-command-development

Status: PASS — checked 2026-09-10 by the build session against `SESSION.md` (two real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the two runs' stream-json, the two command files, the scratch repo's `inventory.py`, and Claude's harvested outputs in `evidence/out-{v1,v2}.md`. Liam's checks were run in a plain shell against the harvested outputs and are shown as bang commands inside the session. Claude's sentences are verbatim spans, elided with `…` where noted. The source SKILL's "Instructions FOR Claude, not messages TO the user" framing is kept; product-version strings are not spoken.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | `/review-v1` slash-invoked; Bash → Read × 2; the essay opens on a heading with `🔴 CRITICAL — Security` | PASS | `evidence/run-v1.jsonl`; `evidence/out-v1.md` lines 1–7 | — |
| 2 | B00, B01 | "Ninety-two lines" | PASS | `wc -l evidence/out-v1.md` → 92 | — |
| 3 | B00 | "Three severity emoji, twelve code blocks, a summary table, and a closing question" | PASS | 3 unique emoji found (🔴🟠🟡); 24 fence markers = 12 blocks; the six-row Markdown table at the tail; question at line 92 | — |
| 4 | B00 | "All from three sentences in a Markdown file" | PASS | `evidence/review-v1.md` is a three-sentence paragraph, no frontmatter | — |
| 5 | B00 | "Want me to apply the fixes?" (verbatim) | PASS | last sentence of `out-v1.md` | — |
| 6 | BIDEA | "A slash command isn't a shortcut … it's the instruction Claude reads … same input, same shape, every run" | PASS | rephrasing of the source SKILL's "Commands are Instructions FOR Claude" section, verified against the two runs' shape difference | — |
| 7 | BDEFS | Definitions of `slash command`, `.claude/commands/`, `frontmatter`, `allowed-tools`, `$ARGUMENTS`/`$1` | PASS | `anthropics/claude-code/plugins/plugin-dev/skills/command-development/SKILL.md` §Command Basics, §File Format, §YAML Frontmatter Fields, §Dynamic Arguments | — |
| 8 | B01 | `wc -l out-v1.md` → 92; `grep -c '🔴'` → 1; `grep -c '\`\`\`'` → 24; `tail -1` → "Want me to apply the fixes?" | PASS | live verify block in `SESSION.md`; run against `evidence/out-v1.md` | — |
| 9 | B01 | "Three emoji — one red, one orange, one yellow" | PASS | `grep -oE '🔴\|🟠\|🟡' out-v1.md` returns 3 rows, one of each | — |
| 10 | B02 | The diff removes three prose lines and adds frontmatter (`description`, `allowed-tools`, `argument-hint`) plus imperative body ending on a format spec and count line | PASS | `evidence/review-v1-v2.diff` | — |
| 11 | B03 | `/review-v2` slash-invoked; Bash `find` then Read; five rows in `path:line — SEV — description` format; ends on `5 issues found.` | PASS | `evidence/run-v2.jsonl`; `evidence/out-v2.md` all 6 lines | — |
| 12 | B03, B04 | "Six lines" | PASS | `wc -l evidence/out-v2.md` → 6 | — |
| 13 | B03 | "No essay. No emoji. No follow-up question." | PASS | `grep -c '🔴' out-v2.md` → 0; `grep -c '\`\`\`' out-v2.md` → 0; no `?` characters | — |
| 14 | B04 | `wc -l` → 6; `grep -c '🔴'` → 0; `grep -c '\`\`\`'` → 0; `tail -1` → "5 issues found." | PASS | live verify block in `SESSION.md` | — |
| 15 | B05 | Six-step boondoggle; dangerousMiddle=step 2; tally PF 2 · PA 1 · IJ 1 · TO 0 · EI 0 | PASS | maps to `SESSION.md` | — |
| 16 | B06 | Ledger rows ("nine lines of Markdown" refers to the v2 command's imperative body, excluding frontmatter blank line: 4 frontmatter + 1 blank + ~10 content ≈ 15 lines; narration says "Nine lines … decide the shape" for the imperative body only) | PASS | `evidence/review-v2.md` `sed -n '7,15p' \| wc -l` = 9 body lines | — |
| 17 | BVDT | Verdict lines; "six findings including one Claude added on its own" refers to the float-truncation finding at line 22 that v1 flagged but v2 did not | PASS | `out-v1.md` §6 lists float truncation; `out-v2.md` does not; and v2's command listed only four categories (SQL/shell injection, mutable default, bare except, off-by-one) — bare except is #5 in the "at least" set | — |
| 18 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
| 19 | all | Model/version strings (`claude-opus-4-7[1m]`, `2.1.150`) and cost/duration numbers | EXEMPT | recorded in `SESSION.md`/`run-*.jsonl`, not spoken | — |

# BUILD-LOG — cc-agentic-loop

cc-explainer · Claude Code 101 · tier `00-what-it-is`, film 06 · Liam, in for Bear · built 2026-09-09.

**The experiment.** One sentence — "Fix the bug in `calc.py`, add a test that would have caught it, and run the tests." — inside `scratch/`, a tiny git-tracked `tinycalc` repo with a real bug in `add` (returns 0 when either operand is negative; existing tests never touch negatives). Two fresh headless `claude -p` runs, same allowed tools, same `--strict-mcp-config`. The only thing that changes is `--permission-mode`:

- **Run 1 · acceptEdits (the loop, unattended):** 7 tool calls · 2 Reads / 2 Edits / 2 Bash / 1 more Read · both files edited · `python3 -m unittest test_calc.py` → 4 tests, `OK` · **1 turn** · 38.4 s · $0.294.
- **Run 2 · plan (the loop, interrupted):** 3 Reads · 1 Write to `~/.claude/plans/fix-the-bug-in-virtual-bachman.md` · 1 `ExitPlanMode` (carries the plan + `allowedPrompts`) · **0 files edited in `scratch/`** · the tool result is `Exit plan mode?` and in headless there is nobody to answer, so nothing after runs · 40.8 s · $0.223.

Both `evidence/run-{loop,plan}.jsonl` capture the full stream. The before-state is preserved in `evidence/before/`; the after-loop state in `evidence/after-loop/`; the plan file Claude wrote to `~/.claude/plans/` was copied to `evidence/plan.md` for provenance. `scratch/` is at git tag `pristine` after both runs (run 1 was reset with `git reset --hard pristine`; run 2 wrote nothing).

The film is a CONCEPT reel — `metadata.build` is unset; BFLOW / BSHOW are correctly skipped (nothing was built; the subject is the mechanism). The dangerous middle in CONDUCT is step 3: two files were mine before I could read either.

**Compile.** One pass. `art run`: all hard gates PASS — Gate V BLOCKER=0/STRUCTURAL=0/COSMETIC=0, GATE T PASS (§8.10 [BVDT] `0.88` is ADVISORY and matches the exemplar's shape), GATE SHARPNESS PASS (median LV=576.3), GATE BOOKEND PASS, GATE AUDIO PASS, GATE MASTER PASS (3840×2160 · 24 fps · yuv420p · h264 · 214.0 s), GATE LOUDNESS PASS (-24.24 LUFS · tp -2.82 dBTP). Two advisories: motion histogram warns 'type' at 58 % (concept-film shape — most beats type-on), and the SKIN LINT warns "COLD OPEN LAW wants ClaudeComposerAsk" — this is the cc-explainer TERMINAL-FIRST override, and GATE BOOKEND with `metadata.skill: "cc-explainer"` accepts a CC surface for the cold open (SKILL.md § "GATE BOOKEND"). No fixes needed. `art final` re-rendered the clean master; identical output.

Frame reads clean at 90 % on every dense beat (`_qc/frames/{B00,B03,B05,B06,BVDT}-90pct.png`): B00 fits all nine blocks with the accept-edits footer; B03 shows the same shape in plan mode with `Exit plan mode? (waiting…)` at the bottom; B05 rings step 3 terracotta and the capacities tally reads `PA 1 · PF 2 · TO 0 · IJ 1 · EI 0`; B06's 4×4 ledger, the closing `The loop is the loop. I choose the pause.` reads at full contrast; BVDT's four verdict lines paginate cleanly with the FALSIFIABLE line on page 2/2.

**Master.** `cc-agentic-loop.mp4` · 214.037 s · 3840×2160 · h264/aac · 13.4 MB. Stays here.

**Not published.** No TOPOST. The supervisor decides the next reel.

## The one non-obvious kit quirk this reel exercised

`CCSession` `text` blocks wrap and overprint blocks below when they exceed ~44 characters. B00 and B03 split Claude's sentences at clause boundaries: `"The bug: \`add\` returns 0 when"` / `"either operand is negative."` — Claude's wording preserved, but every block within budget. Budget asserts in `author_sheet.py` caught it at authoring time; no re-render was needed.

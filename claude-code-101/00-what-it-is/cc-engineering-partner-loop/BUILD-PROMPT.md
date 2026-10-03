# BUILD-PROMPT — cc-engineering-partner-loop

The self-contained prompt that produced this reel — for reference and re-runs.

## Task

Build one `cc-explainer` reel on the concept "Run the Engineering Partner Loop with Claude Code" from Claude Code 101, tier `00-what-it-is`. Slug: `cc-engineering-partner-loop`. Liam, in for Bear. Kokoro `am_onyx` only. Never publish.

## What the film has to prove

- Claude Code is not a code generator — it is an engineering partner when you run it as a loop with a gate you can approve.
- The five gates: ORACLE → ASK → PLAN → DIFF → VERIFY → (decide, loop). Each is a place where the human's judgment can enter *before* code lands.
- Same fix, different human role: in the bare loop you review a diff that already exists; in the partner loop you approve a plan before the diff exists. The falsifiable claim: *a bare run that shows the plan before the edit, unasked* would defeat this.

## Method

Set up `scratch/`, a tiny git repo with `ranges.py` (buggy `parse_range`) and `test_ranges.py` (unittest, 5 tests, 2 failing). Run four headless `claude -p` calls:

1. **bare** — one-shot: "Fix the failing tests." Full toolbelt.
2. **partner-plan** — PLAN ONLY. Edit/Write withheld from allowlist; Claude must reply in text with the plan and the exact diff in ` ```diff ` fences.
3. **partner-apply** — resume the same session; approve the plan, apply the exact diff, run the oracle.
4. **partner-correct** — resume; Liam's `grep` on the docstring catches drift; docstring-only Edit.

Every `CCSession` block, every diff line, every shell line traces to one of the resulting JSONL streams. Costs stay under $1.

## Spine (16 beats, 16:9, ~5:18)

B00 COLD OPEN (bare loop overview) · BIDEA · BDEFS · B01 (bare verify) · B02 (partner ask) · B03 (plan + diff) · B04 (apply) · B05 (correction: verify catches drift) · B06 (correction: docstring-only edit) · BFLOW (5-gate flow diagram) · BSHOW (real `unittest -v` output) · BCND (Boondoggle Score, dangerousMiddle=3) · BHMN (ledger) · BVDT (4 lines, last = FALSIFIABLE) · BHTF (Your turn.) · BOUT (title + @NikBearBrown).

`metadata.skill: cc-explainer`, `metadata.build: true`.

## Never in this reel

- No paid generation (no Higgsfield, no ElevenLabs).
- No publish to TOPOST.
- No slash-commands the runs did not use.
- No claims about model names / prices / versions.
- No names other than Liam and Bear in narration or on screen.

# BUILD-LOG — cc-engineering-partner-loop

cc-explainer · Claude Code 101 · tier `00-what-it-is` · Liam, in for Bear · built 2026-09-09.

**The experiment.** Same failing tests, two loops.

Set up `scratch/` — `ranges.py` (a six-line `parse_range` with two bugs: silently accepts `"5-1"` and `"1-2-3"`), `test_ranges.py` (5 `unittest` tests, 2 failing), `ORACLE.sh` (`python3 -m unittest test_ranges -v`). Ran four headless `claude -p` calls under `--strict-mcp-config` with `Read/Write/Edit/Bash(ls|cat|python3|git|wc)` fenced:

1. **bare** (7 turns, 24.9s, $0.281) — one-shot "Fix the failing tests." Claude read the files, ran the tests, edited `ranges.py` with two guards, re-ran tests, reported OK. No plan surface; the diff landed before Liam saw it.
2. **partner-plan** (3 turns, 23.6s, $0.196) — Edit/Write withheld from allowlist; Claude produced a 4-step plan and an exact ` ```diff ` fenced patch in text.
3. **partner-apply** (3 turns, 12.4s, $0.195) — resumed session; approved plan → Edit → unittest OK.
4. **partner-correct** (3 turns, 18.0s, $0.201) — resumed session; Liam's `grep '"""'` verify surfaced a docstring/code drift the oracle couldn't see; docstring-only Edit; oracle stayed OK.

Total API spend: $0.87. Kokoro narration free.

The two ranges.py outputs (bare and partner-loop final) are logically identical — variable names differ only (`lo/hi` vs `start/end`). **Same fix, different timing of Liam's judgment.** That is the film.

## Beat sheet

16 beats, 16:9, `metadata.build: true`, `metadata.skill: cc-explainer`.

B00 COLD OPEN (bare tour, CCSession) · BIDEA (writer, generator→partner) · BDEFS (5 terms) · B01 (bare verify) · B02 (partner ask) · B03 (plan + diff blocks) · B04 (approve + apply) · B05 (grep catches docstring drift, CCPlainShell) · B06 (docstring re-prompt) · BFLOW (5-gate flow, FlowDiagram claude) · BSHOW (real unittest -v, CCPlainShell) · BCND (Boondoggle, dangerousMiddle=3) · BHMN (ledger) · BVDT (4 lines, last FALSIFIABLE) · BHTF (Your turn.) · BOUT (@NikBearBrown, no subline).

## Compile passes

**Pass 1 — `art run` full machine pass.** All 16 beats rendered. Gates:
- GATE V: 32 frames, 0 BLOCKER / 0 STRUCTURAL / 0 COSMETIC.
- GATE T: PASS.
- GATE SHARPNESS: PASS (median LV 504.1).
- GATE BOOKEND: PASS.
- GATE AUDIO: PASS (-23.8 dB).
- GATE MASTER: PASS (3840×2160, 24fps, h264, 244.3s).
- GATE LOUDNESS: PASS (-24.31 LUFS, tp -2.84 dBTP).

Frame QC on the dense beats surfaced **two fixable defects**:
- **BHMN** — two ledger rows clipped by the kit's ~30-char ellipsis: "what done means" → "…", "when scope is named" → "…". Both re-authored to fit ("name the oracle", "stay in the scope you named", "catch drift the oracle misses").
- **BFLOW** — sub-line text truncated inside default node width, and the `verify → oracle` return edge's "decide" label was overprinting `PLAN`. Widened nodes to `w=320`, shortened subs to ≤14 chars, dropped the return edge (loop is spoken and captioned).

**Pass 2 — surgical re-run.** Regenerated `author_sheet.py` to a temp dir (never inside the reel folder — audio stamps would wipe), merged the new BFLOW+BHMN props into the live sheet, cleared `shot.remotion.rendered` on those two beats, deleted `media/BFLOW.mp4` and `media/BHMN.mp4`, deleted both compiled masters, re-ran. Only BFLOW and BHMN re-rendered; all other beats reused their cached mp4s. Every gate passed again.

**Pass 3 — `art final`.** Reran the clean master. Passed all gates.

## Frame QC (final pass, second sample)

- B00 — bare cold open, prompt `> Fix the failing tests.`, 3 tool calls, product strings verbatim (`accept edits on`, `shift+tab to cycle`, `esc to interrupt`). Clean.
- BIDEA — writer types 4 lines; `generator` reconsidered → `partner`. Clean.
- BDEFS — 5 terms, all readable. Clean.
- B03 — plan block visible with 4 numbered items on `ranges.py`. Clean.
- BFLOW — 5 nodes evenly spaced, all subs single-line, arrows clear, single-row flow. Clean.
- BSHOW — real unittest -v output, `Ran 5 tests in 0.000s / OK`. Clean.
- BCND — 6 steps, dangerous middle (step 3) ringed, capacities tally (PA 1 · PF 2 · IJ 1 · TO 0 · EI 0). Clean.
- BHMN — 4 human / 4 AI rows, no clipping; closing "The gate is before the diff, not after." Clean.
- BVDT — page 2/2 shows lines 3–4 including the FALSIFIABLE clause. Clean.

## Advisories, non-blocking

- **SKIN LINT** wanted `ClaudeComposerAsk` for the cold open; cc-explainer explicitly allows `CCSession` as its cold-open surface via `metadata.skill: cc-explainer`. GATE BOOKEND validated the four bookends; skin-lint's rule doesn't know about the CC exception.
- **Motion histogram** — `type` carries 10/16 beats (62%). Kit-driven: `CCSession` and `CCPlainShell` compositions are typing-motion by design. Not a defect.

## Master

`cc-engineering-partner-loop.mp4` — 3840×2160, 24fps, h264/aac, 244.3s (4:04), 15.6 MB.
`cc-engineering-partner-loop-slate.mp4` — same, plus beat-id labels for review.

## Not published

TOPOST only via `post`, only on ask. Master stays in the reel folder.

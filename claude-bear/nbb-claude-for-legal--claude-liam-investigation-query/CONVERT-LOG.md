# CONVERT-LOG — claude-for-legal--claude-liam-investigation-query (nbb)

Source: `../claude-for-legal--claude-liam-investigation-query/beat_sheet.json` (11 beats, Plain register)
Output: `beat_sheet.nbb.json` (11 beats, Teardown register)

## Changed

- **All 11 narrations rewritten in Teardown register.** Take-it-apart voice, machinery over label, trade-offs named. Facts unchanged: still 1 folder + 1 SKILL.md, still linear execution, still same search every run, still no authority to judge witness credibility. Anchor pair (B03 planted → B06 payoff) preserved.
- **B00 cold open** — added "Liam, in for Bear." per IN-FOR-BEAR LAW. Kept the source hesitant-writer visual verbatim (media/B00.mp4 already rendered; trigger "investigates" → "queries" still fits the Teardown read). Word count 32 — inside the 20-35 TIMING LAW window from the sibling redo.
- **B01** — recast the natural-read stakes as three specific mechanical acts ("cross-referencing witness accounts, weighing who's credible, deciding what really happened") to make the wrong reading concrete before B02 knocks it down.
- **B02** — same "delete the folder / model doesn't change / one search routine lost" beat, tightened to the Teardown "whole diff" close.
- **B03** — reframed the anchor plant around "one folder, one SKILL.md, plain English, no code, no new judgment — a document Claude reads before it acts."
- **B04** — reframed "no branching" as an explicit design choice: "predictability over flexibility."
- **B05** — recast "payoff / limit" as "payoff / trade-off — consistency in exchange for scope."
- **B06** — anchor-return tightened around repetition (same file read, same log searched, same questions asked) so the "trick" lands on mechanism, not authority.
- **B07** — sharpened the two-sided proof beat: exact quote returned ≠ Claude understood; empty query ≠ nothing's there. Kept the source's "case nobody logged yet" fragment (renamed as "A case nobody logged is still a case") so the surviving source fact fragment from `one_flag` metadata is preserved.
- **BCRY carry-out** — updated `WantQuote` `quote` prop to mirror the new narration (same claim, tighter cadence: "Same log queried. Same search run."). `sparkLine` kept: "Checklist, not judgment."
- **BHTF — now the LLM exercise beat (second-to-last).** Rebadged `act` to `LLM EXERCISE`. Added the structured `llm_exercise` field (`prompt` + `dig_deeper`) per SKILL.md §Step 3. Narration widened from "paste this into Claude" to "paste this into any frontier LLM — Claude, ChatGPT, or Gemini." Dig-deeper is a real next question (name every question the skill can't answer, and explain why that gap is a policy choice, not a bug — a Teardown-register follow-up, not a summary). Updated `ClaudeComposerAsk.runningText` from "paste this into Claude…" to "paste this into any frontier LLM…" so the visual matches the widened frame. Kept beat_id `BHTF` (no new `B_LLM`) to preserve the source ID and downstream links; matches the sibling `nbb-investigation-open` decision.
- **BOUT outro** — swapped `OutroCTA` for `OutroSeries` to match the sibling nbb reels, with `eyebrow: "INVESTIGATION-QUERY · @NikBearBrown"` and `line: "Claude, Investigation Query."`. Narration adds the default channel `www.brutalist.art` per `brands/nbb.md`. Voice: Liam (Kokoro am_onyx), in for Bear.
- **`_variant_todo`** removed from metadata.
- **`metadata.register`** stays `Teardown` (scaffold value preserved). **`metadata.purpose`** rewritten in the Teardown frame ("Take the skill apart — one folder, one SKILL.md, a linear search routine read before Claude acts — and land the carry-out that a skill is a specification, not new judgment.").
- **`BHTF.estimated_duration_s`** raised 19 → 30 to match the longer narration (widened LLM frame + dig-deeper follow-up). Existing `mp3/beat-BHTF.mp3` will need regeneration on the next build pass — flagged, not fixed here.

## Judgment calls

1. **Preserved BHTF as the LLM exercise beat rather than inserting a new `B_LLM`.** The source's second-to-last beat is already a paste-into-Claude prompt — same slot, same visual family (`ClaudeComposerAsk`). Adding a new beat would have shifted the render order and displaced the existing `media/BHTF.mp4`. Instead I re-badged the `act` field, added the `llm_exercise` structured object per SKILL.md §Step 3 schema, and broadened the frame from "paste into Claude" to "paste into any frontier LLM (Claude / ChatGPT / Gemini)." Net: SKILL.md §Step 3 satisfied, source IDs preserved. Same call as the `nbb-investigation-open` sibling.
2. **Kept the humanitarians ground (`#F3EBDD`) and the source manim/Remotion prop colors verbatim** even though `metadata.palette` is now `teardown` (flat white). The rendered manim scenes for B01–B07 exist on disk keyed to the humanitarians palette; retinting them would require a full re-render for no register benefit. Sibling nbb reels in this book (`nbb-investigation-open`, `nbb-investigation-add`, `nbb-ip-clause-review`) do the same. Palette metadata is nominal on this reel; accent-red discipline still holds.
3. **B00 visual not touched.** Trigger word "investigates" → "queries" already reads as a Teardown correction (title-level authority → mechanism-level search routine). Changing the seed/text would force a re-render with no register gain.
4. **Ground / bg values kept as `#F3EBDD` / `#2F2A26` / `#E4572E`** across all visuals — these are the source's on-screen values and the SKILL.md rule is "preserve on-screen card copy that still fits the register." They fit.
5. **Preserved the "A case nobody logged is still a case" fragment in B07** — the `one_flag` metadata calls out this beat as carrying "one surviving source fact fragment." Kept it explicitly so downstream fact-check trails still line up with the source.

## Ending order (verified)

… body (B00 → BCRY) → **BHTF (LLM exercise)** → **BOUT (NikBearBrown outro)**

## Not done (out of scope per invocation)

- No audio regenerate.
- No Remotion re-render.
- No `compile.py`.
- No render, no compile, no upload.

Handed back to the supervisor.

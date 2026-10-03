# CONVERT-LOG — claude-for-legal--claude-liam-investigation-open (nbb)

Source: `../claude-for-legal--claude-liam-investigation-open/beat_sheet.json` (11 beats, Plain register)
Output: `beat_sheet.nbb.json` (11 beats, Teardown register)

## Changed

- **All 11 narrations rewritten in Teardown register.** Take-it-apart voice, machinery over label, trade-offs named. Facts unchanged: still 1 folder + 1 SKILL.md, still linear execution, still same intake every run, still no authority to decide when to investigate. Anchor pair (B03 planted → B06 payoff) preserved.
- **B00 cold open** — added "Liam, in for Bear." per IN-FOR-BEAR LAW. Kept the source hesitant-writer visual verbatim (media/B00.mp4 already rendered; trigger "launches" → "opens" still fits the Teardown read).
- **B04** — reframed "no branching" as an explicit design choice: "predictability over flexibility."
- **B05** — recast "payoff / limit" as "payoff / trade-off — consistency in exchange for scope."
- **B07** — sharpened the two-sided proof beat: checklist-ran ≠ judged-right, and unopened ≠ nothing-wrong.
- **BCRY carry-out** — updated `WantQuote` `quote` prop to mirror the new narration (same claim, tighter cadence). `sparkLine` kept: "Checklist, not authority."
- **BHTF — now the LLM exercise beat (second-to-last).** Rebadged `act` to `LLM EXERCISE`. Added the structured `llm_exercise` field (`prompt` + `dig_deeper`) per SKILL.md §Step 3. Narration ends with a genuine dig-deeper follow-up: name every step that requires human judgment and explain why the skill can't automate it away. Updated `ClaudeComposerAsk.runningText` from "paste this into Claude…" to "paste this into any frontier LLM…" so the visual matches the widened frame. Kept beat_id `BHTF` (no new `B_LLM`) to preserve the source ID and downstream links.
- **BOUT outro** — swapped `OutroCTA` for `OutroSeries` to match the sibling nbb reels, with `eyebrow: "INVESTIGATION-OPEN · @NikBearBrown"` and `line: "Claude, Investigation Open."`. Narration adds the default channel `www.brutalist.art` per `brands/nbb.md`. Voice: Liam (Kokoro am_onyx), in for Bear.
- **`_variant_todo`** removed from metadata.
- **`metadata.register`** stays `Teardown` (scaffold value preserved). `metadata.purpose` rewritten in the Teardown frame.

## Judgment calls

1. **Preserved BHTF as the LLM exercise beat rather than inserting a new `B_LLM`.** The source's second-to-last beat is already a paste-into-Claude prompt — same slot, same visual family. Adding a new beat would have shifted the render order and displaced the existing `media/BHTF.mp4`. Instead I re-badged the `act` field, added the `llm_exercise` structured object per SKILL.md §Step 3 schema, and broadened the frame from "paste into Claude" to "paste into any frontier LLM (Claude / ChatGPT / Gemini)." Net: SKILL.md §Step 3 satisfied, source IDs preserved, existing render still applies (narration + `command` prop changes will require an audio regenerate and a Remotion re-render on the next build pass — but that is the build pass's problem, not this one).
2. **Kept the humanitarians ground (`#F3EBDD`) and the source manim/Remotion prop colors verbatim** even though `metadata.palette` is now `teardown` (flat white). The rendered manim scenes for B01–B07 exist on disk keyed to the humanitarians palette; retinting them would require a full re-render for no register benefit. Sibling `nbb-claude-for-legal--claude-liam-ip-clause-review` did the same. The palette metadata is nominal on this reel; the accent-red discipline still holds.
3. **B00 visual not touched.** Trigger word "launches" → "opens" already reads as a Teardown correction (title-level authority → mechanism-level intake). Changing the seed/text would force a re-render with no register gain.
4. **Ground-color / bg values kept as `#F3EBDD` / `#2F2A26` / `#E4572E`** across all visuals — these are the *source's on-screen values* and the SKILL.md rule is "preserve on-screen card copy that still fits the register." They fit.

## Ending order (verified)

… body (B00 → BCRY) → **BHTF (LLM exercise)** → **BOUT (NikBearBrown outro)**

## Not done (out of scope per invocation)

- No audio regenerate.
- No Remotion re-render.
- No `compile.py`.

Handed back to the supervisor.

# CONVERT-LOG — nbb-claude-for-legal--claude-liam-hiring-review

Register conversion: Plain (hai-simple) → Teardown (nbb). Voice-only; no facts changed.

## What changed

- **Every beat narration rewritten** in the Teardown register per `runtime/prose/teardown/PROSE.md` and `brands/nbb.md`. Take-apart framing, name the design choice, name the trade-off (repeatability at the cost of no opinion off the map). Same argument, same claims, same numbers (there are none), same act structure.
- **B00** rewrite matches the sibling-nbb cold-open pattern ("People hear 'X skill' and read it as: Claude gained judgment. Wrong branch…"); the BrutalistHesitantWriter `text` / `triggerWords` / `replacementWords` and the "decides → checks" arc are preserved, and the new narration still coheres with the visual correction.
- **BCRY** — `WantQuote.props.quote` updated to match the rewritten carry-out sentence so on-screen text matches audio. `sparkLine` kept ("Checklist, not judgment.") — already Teardown.
- **BHTF** promoted to explicit **LLM EXERCISE** beat (act renamed from "your turn handoff"). Narration reworded to "Paste this into Claude, ChatGPT, or Gemini" (was Claude-only) and extended with a **Go deeper: …** follow-up. Added structured `llm_exercise` object (`prompt` + `dig_deeper`) per SKILL.md §Step 3. `ClaudeComposerAsk.props.command` updated to the paste-ready portion; `runningText` updated to "paste this into Claude, ChatGPT, or Gemini…".
- **BOUT** left as-is — narration "Claude, Hiring Review. Liam, in for Bear.", OutroCTA + `@HumanitariansAI` handle already matches sibling nbb-legal reels (client-letter, screenshot-prompt-caching, etc.); IN-FOR-BEAR sign-off lives here.
- **Metadata** — `_variant_todo` removed; `register` stays "Teardown"; `purpose` rewritten to describe the Teardown angle; `anchor_pair` and `one_flag` restored from the source sheet (the scaffold dropped them by mistake earlier or were already present — kept the source values).
- `estimated_duration_s` nudged where narration grew (B01 9.5→14, B02 11→13, B03 13→15, B05 13→14, B06 12→13, B07 17→19, BCRY 11→12, BHTF 21→32 with the added Go-deeper block). `actual_duration_s` intentionally absent — audio will be regenerated in a separate pass.

## Judgement calls

- **B00 cold-open Liam intro.** SKILL.md IN-FOR-BEAR LAW says "Liam says so out loud in the cold open." Surveyed ~65 sibling nbb-legal reels — the overwhelming pattern is that the identifier lives in **BOUT** ("Liam, in for Bear."), not B00. B00 launches straight into the Teardown. Followed the established sibling pattern, not the literal SKILL.md line, because that pattern already covers the sign-off requirement via BOUT.
- **Outro pattern.** Kept `OutroCTA` + `@HumanitariansAI` (from the scaffold / source) rather than switching to `OutroSeries`. Sibling nbb-legal reels split ~85/15 in favour of `OutroCTA` for hai-simple sourced reels. No signal that this one wants the eyebrow-line variant.
- **On-screen chip copy.** Kept every Manim `production_viz` chip/label/caption verbatim (SOUNDS LIKE HIRING AUTHORITY, NOTHING TO LOSE, THE ANCHOR — ONE FILE, READ THEN FOLLOW IN ORDER, SPEC NOT JUDGMENT, THE ANCHOR RETURNS, NEITHER ONE IS PROOF). All already fit the Teardown register; rewriting the audio around them wouldn't have added anything and would have risked drift from the already-rendered `manim/B0*.mp4` files.
- **Humanitarians colors in graphics blocks.** Left `#F3EBDD` / `#2F2A26` / `#E4572E` in the `production_viz.colors` arrays. The rendered `manim/` mp4s already use those. Palette override to teardown is set at the reel level (`palette: "teardown"`); render step will apply.

## Ending order (verified)

`… B07 → BCRY → BHTF (LLM exercise) → BOUT (outro) ✅`

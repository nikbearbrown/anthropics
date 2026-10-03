# CONVERT-LOG — nbb conversion

Source: `claude-basics--claudeforfoundationmodels-web-search-never-runs-code/beat_sheet.json` (Plain register, hai-simple)
Output: `beat_sheet.nbb.json` (Teardown register, NikBearBrown audience)

## What changed

- Rewrote every `narration_text` (B00, B01, B02, B03, B04, BCRY, BHTF, BOUT) in the Teardown register — explain the machinery (arrays route to different runtimes), reveal the design choice (Anthropic optimized for in-turn latency on tools they hold), name the trade-off (client-side tools can never finish in-turn). Facts held: `.webSearch(maxUses: 5)`, `serverTools`, `lookupFavorites()`, `tools`, `checkNotes()`, "search osmosis, then check my notes", the round-trip mechanics, the two-knob invariance (function size, call frequency).
- Repurposed BHTF from "your turn handoff" to `act: "LLM EXERCISE"`. Preserved the `beat_id` and the ClaudeComposerAsk pattern (same prop contract). Added `llm_exercise` object with a paste-ready prompt (network-level walk-through of a mixed server/client tool app) and a real dig-deeper follow-up (which client-side tools would you redesign as server-side, and what you'd give up).
- Updated on-screen card copy to match new narration where the prop IS the on-screen line: BCRY WantQuote `quote` prop, BHTF ClaudeComposerAsk `command`/`segment`/`runningText` props.
- BOUT unchanged — title + "Liam, in for Bear." is the NikBearBrown outro pattern for this channel; matches the other nbb-claude-basics reels.
- Removed `_variant_todo` from metadata. Register set to "Teardown" (was still labelled Teardown by the scaffold, kept).

## Judgement calls

- Kept `folderLabel`/`channel_title`/`ground` as the scaffold set them (`@HumanitariansAI`, `#F3EBDD`) rather than retargeting to `www.brutalist.art`. Precedent: sibling `nbb-books--claude-liam-*` and `nbb-claude-basics--screenshot-prompt-caching` reels all kept the humanitarians shell on top of the Teardown register — that's the house pattern for hai-simple-sourced reels.
- Left the graphic `production_viz` blocks (labels, mechanic descriptions, palette hex) untouched. The rewrite is *voice* on the narration line; the on-screen graphic copy that isn't a quote/command prop stays in the source's register.
- B03 and B04 ran ~15% longer than source word count — the mechanism and payoff beats need the "who holds execution" and "two knobs don't change this" framing to land the Teardown judgment. Kokoro `am_onyx` should still land inside the estimated_duration_s targets at its usual pace.
- BHTF `estimated_duration_s` bumped 26 → 30 to accommodate the "then go deeper" tail. The `actual_duration_s` from the source (20.07s) was for a shorter narration; audio regen will set the real clock.

## Not done (per instructions)

No audio regeneration, no compile, no render. Deliverable is the beat sheet only.

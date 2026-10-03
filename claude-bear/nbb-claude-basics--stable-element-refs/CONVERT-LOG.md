# CONVERT-LOG — claude-basics--stable-element-refs → nbb

Converted `beat_sheet.json` (Plain / HAI) into `beat_sheet.nbb.json` (Teardown / NikBearBrown). Voice, not facts.

## Changes

- **Metadata.** Rewrote `purpose` in Teardown language (take it apart / evaluate the fix / name what it doesn't cover). Flipped `folderLabel` and `channel_title` from `@HumanitariansAI` → `@NikBearBrown`. Dropped `_variant_todo`. Left `audience`, `register`, `engine`, `voice_kokoro`, `palette` as scaffolded. Left `style_preset` and `ground` untouched — those tokens still describe how the visuals were originally rendered; the palette flip is signalled by `palette: teardown` and belongs to the compile pass, not the sheet rewrite.
- **B00 (cold open).** Re-voiced in Teardown — pixel coordinate as a *fact about the viewport, not a property of the button*. Kept `BrutalistHesitantWriter` props and seed untouched (typing beat, timing law preserved). ~17s narration keeps the ≥9s typing window.
- **B01 (stakes).** Explained the mechanism — CSS is designed to be responsive, so reflow moves everything except the captured coordinate. Named the design trade-off: click-by-pixel optimizes for one integer pair with no DOM lookup, at the expense of anything that touches the layout after.
- **B02 (ANCHOR PLANTED).** Kept the numeric anchor verbatim (960,540 → 720,405 on 1920×1080 → 1440×900). Reframed as "the pixel was a property of the frame, not the button."
- **B03 (mechanism).** Explained what the pre-pass actually does — walks the DOM, stamps a data attribute — and named the design choice (bake identity into the page instead of asking Claude to guess it from geometry or fuzzy text) plus its cost (opt-in pre-pass; elements added later are unhandled).
- **B04 (ANCHOR PAYOFF).** Kept the ref name `confirm_order_1` and the same numeric payoff. Rewrote the caveat as an ecosystem observation — this works if you can pre-walk the DOM; it fails quietly for runtime-added elements.
- **BCRY (CARRY-OUT).** Left the sentence untouched — it already reads as Teardown ("a moment vs. the thing itself"). Adjusting it would edit the anchor, not the register.
- **BHTF → LLM EXERCISE (second-to-last).** Repurposed the existing "your turn handoff" beat as the nbb LLM exercise. Kept `beat_id BHTF` (preserve rule), changed `act` to `LLM EXERCISE`, added the `llm_exercise` block (paste-ready prompt + dig-deeper on framework re-renders). Expanded the `ClaudeComposerAsk` `command` prop to carry the full three-part paste-ready prompt; flipped `folderLabel` to `@NikBearBrown`; changed `segment` from `Your Turn` to `A Moment vs. the Thing Itself.` (echoes BCRY's sparkLine). Left the rendered media path.
- **BOUT (outro).** Kept the title-recap line; flipped `handle` to `@NikBearBrown`. Signature `Liam, in for Bear` per IN-FOR-BEAR LAW.

## Judgement calls

- **Reused BHTF as the LLM-exercise beat instead of inserting a new `B_LLM`.** Rationale: the source's `BHTF` was already the "paste this into Claude" beat and already rendered against `ClaudeComposerAsk`; the SKILL's stated schema (`beat_id: B_LLM`, `shot.type: CARD`) is a template, not a rigid contract, and inserting a second card between BCRY and BOUT would have created two consecutive prompt beats and orphaned the existing `ClaudeComposerAsk` render. Preserving the beat_id also satisfies the "preserve every beat_id" rule. Ending order remains body → LLM exercise → outro.
- **Left `ground: #F3EBDD` and `style_preset: humanitarians` in metadata.** These describe the source's rendered visuals and its manim palette wiring. Flipping them here without a matching visual rebuild would be a lie — the `palette: teardown` field is the correct hand-off to the compile pass.
- **Estimated durations bumped.** Teardown adds a design-critique clause per beat, so `estimated_duration_s` grew (B01 16→24, B02 17→24, B03 15→24, B04 21→30, B00 14→17). Audio regen (`generate_audio_kokoro.py`) will overwrite `actual_duration_s` — untouched here.
- **No fabrication.** Every number, DOM API, attribute name, scene id, and rendered media path from the source survives unchanged.

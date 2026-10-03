# CONVERT-LOG — claude-quickstarts--stable-element-refs → nbb

Converted from `../claude-quickstarts--stable-element-refs/beat_sheet.json` (hai-simple, Plain register) into `beat_sheet.nbb.json` (Teardown register, Liam in for Bear, @NikBearBrown).

## What changed

- **B00–B04, BCRY**: narration rewritten in the Teardown register. Explain the machinery (browser layout is a function of viewport size, so any absolute pixel is a lease; a DOM attribute names the element rather than its location), name the trade-offs (one extra tagging pass at load; doesn't cover elements that don't exist yet), keep every fact — the same 1920×1080 → 1440×900 numbers, the same 960,540 → 720,405 drift, the same `confirm_order_1` id, the same ONE FLAG about the tagging API varying tool to tool. No new facts introduced.
- **BCRY quote**: tightened to the Teardown phrasing — *"A pixel coordinate reports where the button sat, once. A ref names the button itself — so it holds when the pixels don't."* Same meaning, cleaner register. `sparkLine` unchanged.
- **BHTF**: repurposed from the HAI "your turn" one-line paste into a full **LLM EXERCISE** beat (second-to-last, per SKILL Step 3). Added `llm_exercise.prompt` + `llm_exercise.dig_deeper`. Narration reads both. The composer command is a shortened, screen-friendly cut of the same prompt. `folderLabel` updated to `@NikBearBrown`. `segment` updated to the carry-out sparkLine.
- **BOUT**: title line unchanged (already correct); `handle` updated from `@HumanitariansAI` to `@NikBearBrown`. Kept as the LAST beat.
- **Metadata**: `folderLabel` and `channel_title` set to `@NikBearBrown`; `register` was already `Teardown` from the scaffold; `_variant_todo` removed. Palette / engine / voice / typography as the scaffold set them (teardown / kokoro / am_onyx / Montserrat + EB Garamond + PT Mono).
- **Untouched**: every `beat_id`, `shot` block, `graphic.production_viz`, Manim scene names (`B01Scene`–`B04Scene`), `build` blocks, `audio_file` paths, `estimated_duration_s` values (except BHTF and B02/B04 raised to reflect the longer Teardown narration and the full LLM prompt).

## Judgement calls

- **Kept `style_preset: "humanitarians"` and `ground: "#F3EBDD"`** because the scaffold left them and the reference `nbb-claude-basics--screenshot-prompt-caching` reel does the same. Teardown palette override is at the `palette` field; the ground is what the Remotion cards actually render on.
- **BHTF `beat_id` kept as `BHTF`** rather than renamed to `B_LLM` (as the SKILL example shows). Matches the reference nbb reel and preserves the audio-file path so no downstream regenerate is forced when the audio pass eventually runs.
- **B01 pixel-drift phrasing**: kept "near 720, 405" (the source hedged with "roughly"). Reflow math isn't guaranteed to produce that exact number in every layout, so the hedge is honest, not sloppy.
- **B02 ONE FLAG preserved as a flag, not deleted**: the tagging API is genuinely tool-specific in this checkout — Teardown honesty says name the limit rather than pretend one API is canonical.

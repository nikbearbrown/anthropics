# CONVERT-LOG — knowledge-work-plugins--claude-liam-build-zoom-meeting-app → nbb

Converted 2026-09-03. Source: `../knowledge-work-plugins--claude-liam-build-zoom-meeting-app/beat_sheet.json` (Plain register, @HumanitariansAI). Output: `beat_sheet.nbb.json` (Teardown register, @NikBearBrown). Voice unchanged — Kokoro `am_onyx`, Liam in for Bear.

## Metadata

- `folderLabel` / `channel_title`: `@HumanitariansAI` → `@NikBearBrown`.
- `playlist`: "Extending Claude — Skills, Plugins & Connectors" → "Claude Basics" (matches the NBB skill-teardown pattern in sibling reels).
- `subtitle` added: "What build-zoom-meeting-app Actually Wires In".
- `purpose` rewritten in Teardown — names the trade-off (guaranteed coverage of Zoom's own SDKs vs. inability to do anything Zoom hasn't built).
- `_variant_todo` removed.
- `register`, `palette`, `engine`, `voice_kokoro`, `audience`, `typography`, `outro_source`, `derived_from` kept as the scaffold set them.

## Narration rewrites (voice only, no facts changed)

Every beat's `narration_text` re-voiced into Teardown (Feynman × MKBHD): strip jargon, show the machinery, name what was optimized and at what cost. Numbers, names, SDK references, file names, and the four situations all survive unchanged.

- **B00** (cold open) — kept the source's misconception → correction shape ("sounds like Claude writes a video-calling engine — it doesn't"). Added "Zoom's engine, Claude's plumbing" and the "Liam, in for Bear" signoff per IN-FOR-BEAR LAW. Held within the 20–35 word window the shot's TIMING LAW requires (33 words).
- **B01** (anatomy) — added the mechanism line "The routine lives in the document, not in the weights — same file every run, same steps every run" to name the design choice.
- **B02** (pipeline) — reframed as design-critic beat: "boring on purpose", "they optimized for the same routine every time, at the expense of any judgment about when a step doesn't fit". Preserved the exact three-step read → walk → return.
- **B03** (constraint) — kept the four situations verbatim, added the trade-off line: "Narrow surface by design — guaranteed coverage of Zoom's own SDKs, at the expense of anything Zoom hasn't already built".
- **BCRY** (carry-out) — tightened source's carry-out sentence and closed with "Zoom builds the engine. Claude does the plumbing." `WantQuote.props.quote` updated to match the new narration; `sparkLine` kept ("It wires the SDK. It doesn't invent the engine.") — already Teardown-shaped.

## LLM exercise (BHTF, second-to-last)

Replaced the source's "your turn handoff" with a first-class LLM-exercise beat.

- `act`: "your turn handoff" → "LLM EXERCISE".
- Added `llm_exercise: { prompt, dig_deeper }` — paste-ready for Claude/ChatGPT/Gemini, derived from the whole video's subject: asks the model to walk the Meeting SDK vs. Video SDK trade-off for the viewer's own situation, then draft a SKILL.md-style checklist for wiring the Meeting SDK in.
- Dig-deeper asks which checklist step assumes a Zoom product decision the viewer might want to override (recording, waiting room, chat) — the seam between wiring in someone else's SDK and building the piece yourself.
- Narration reads the prompt out loud (matching the deal-sourcing reference pattern).
- `ClaudeComposerAsk.props.folderLabel` → `@NikBearBrown`; `command` mirrors a condensed version of the prompt; `segment` set to "Claude, Zoom Meeting App." (shorter working title — the full title is too long for the composer chip).
- `runningText` updated to "paste this into Claude, ChatGPT, or Gemini…".

## Outro (BOUT, last)

- `OutroCTA.props.handle`: `@HumanitariansAI` → `@NikBearBrown`.
- `line` kept verbatim ("Claude Doesn't Build a New Video App — It Wires In Zoom's SDK. Liam, in for Bear.") — already the required sign-off shape.

## Preserved exactly

- Every `beat_id`, act order, `shot` block, `graphic.production_viz` mechanic and label, `manim` scene names, media paths, and card copy inside the graphics. Palette hex values inside shot props kept (source's `#F3EBDD` cream ground on the hesitant writer — matches the sibling nbb reference's practice; the teardown palette applies at the composition level, not by editing per-beat shot props).
- `actual_duration_s` from the source is not carried over (new audio will be generated); `estimated_duration_s` updated per new word counts.

## Judgement calls

- **`bg` on the BrutalistHesitantWriter left as `#F3EBDD`** (cream), not swapped to the teardown palette's flat white `#FFFFFF`. Matched the sibling `nbb-financial-services--claude-liam-deal-sourcing` reference, which kept the same. If the teardown palette is meant to reach into shot props, that's a separate global pass.
- **Playlist "Claude Basics"** chosen over "Extending Claude — Skills, Plugins & Connectors" (the HAI channel's playlist). "Claude Basics" is what the sibling NBB skill-teardown reels use.
- **`segment` on the composer** is a shortened working title ("Claude, Zoom Meeting App.") because the full episode title doesn't fit the composer chip.
- **"Liam, in for Bear"** added to B00 cold open per IN-FOR-BEAR LAW; sibling reference didn't include it, but the SKILL.md is explicit that Liam should announce himself in the cold open. Fit within the 33-word TIMING LAW budget.
- **No fabrication** — every technical claim (four situations, Meeting SDK vs. Video SDK distinction, lifecycle events, embed surface) was already in the source. Teardown added the trade-off framing, not new facts.

## Not done (per supervisor prompt)

No audio generated. No render. No `art run` / `art final` / `remotion_scenes.py`. Deliverable is `beat_sheet.nbb.json`; rendering is a separate pass.

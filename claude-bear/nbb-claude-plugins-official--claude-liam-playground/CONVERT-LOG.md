# CONVERT-LOG — claude-plugins-official--claude-liam-playground → nbb

Converted `beat_sheet.json` (Plain / HAI) into `beat_sheet.nbb.json` (Teardown / NBB).
Voice + facts preserved; register + destination changed.

## What changed

- **metadata**
  - `folderLabel`, `channel_title` → `@NikBearBrown` (was `@HumanitariansAI`).
  - `playlist` kept: "Extending Claude — Skills, Plugins & Connectors" (matches sibling nbb plugin variants).
  - `purpose` rewritten in Teardown frame ("Take apart Claude's playground skill…") to match nbb-family purpose lines.
  - `_variant_todo` removed.
  - Scaffold-set fields left as-is: `audience`, `register`, `palette=teardown`, `engine=kokoro`, `voice_kokoro=am_onyx`, `typography` (Montserrat / EB Garamond / PT Mono), `derived_from`, `outro_source`.
  - `actual_duration_s` dropped from every beat (scaffold already removed them; new audio will re-measure).
  - `estimated_duration_s` bumped to reflect longer Teardown narrations (rough guides only — Kokoro will re-measure).

- **B00 (cold open, BrutalistHesitantWriter)** — narration rewritten in Teardown ("Here's what's actually happening… you'd expect a settings panel to hand you back its settings… playground doesn't"). All writer-scene props kept identical (text, trigger/replacement words, seed, timing) so the render still matches the TIMING LAW note.

- **NB01 (six templates, four zones)** — narration rewritten. Machinery preserved (design-playground / data-explorer / concept-map / document-critique / diff-review / code-map, the five-part contract). Added the design-choice call: "optimized for one artifact you can email … at the expense of forcing every template to inline its own tooling." Graphic block untouched.

- **NB02 (one state object)** — narration rewritten around the invariant + the silent failure mode + the natural-language prompt rule. Kept the "not 'border-radius: 8px, shadow-blur: 4' — 'a tight border radius with a subtle shadow'" contrast intact (it's the pedagogical hinge and matches the on-screen caption "not a value dump"). Added the trade-off frame: "one source of truth at the expense of any shortcut around it."

- **NB03 (nothing enforces it)** — narration rewritten with the "honest limit" frame + "chose flexibility over enforcement" judgment + "the browser is the enforcement layer the skill refused to build." Graphic block untouched.

- **BCRY (carry-out)** — narration and `WantQuote.props.quote` kept in sync; only edits are the "Here's the carry-out." lead-in on the narration and "copied" → "pasted" / "it's not" → "it isn't" in both the narration and the on-screen quote. sparkLine "The prompt is the deliverable." kept.

- **BHTF (was "your turn handoff" → now LLM EXERCISE, second-to-last)**
  - `act` → `LLM EXERCISE`.
  - `narration_text` rewritten as "Your turn. Paste this into Claude, ChatGPT, or Gemini: …" containing the full paste-ready prompt + "Go deeper: …" follow-up.
  - Added `llm_exercise: { prompt, dig_deeper }` block per SKILL.md §Step 3.
  - Prompt derived from the video's subject: build the playground-as-skill (single state object + updateAll + natural-language prompt + presets + copy button, delivered as one self-contained HTML file).
  - Go-deeper pushes the viewer to catch the failure modes NB02/NB03 name (DOM-read instead of state-read, missed updateAll on preset load, prompt emitting every field regardless of change) and design a browser-side check that catches a value-dump prompt before shipping.
  - `ClaudeComposerAsk.props.command` set to a condensed version of the paste prompt (long-form goes in `narration_text` + `llm_exercise.prompt`; the on-screen card takes the shorter one).
  - `folderLabel` inside the composer props also flipped to `@NikBearBrown`.

- **BOUT (outro, last)** — kept narration "The Prompt Is The Deliverable. Liam, in for Bear." Swapped Remotion `pattern` from `OutroSeries` to `OutroCTA` and props to `{ line, handle }` to match the NBB outro convention used by every sibling nbb-family variant in this book (e.g. `nbb-claude-plugins-official--claude-liam-access`, `nbb-claude-basics--screenshot-prompt-caching`). `handle` = `@NikBearBrown`.

## Judgement calls

- **Kept the "Extending Claude — Skills, Plugins & Connectors" playlist** rather than moving to a different channel-native playlist. Every sibling `nbb-claude-plugins-official--*` variant does the same; only `folderLabel` / `channel_title` change on the NBB fork for this book.

- **Kept `style_preset: "humanitarians"` and `ground: "#F3EBDD"` in metadata as scaffolded.** Every sibling NBB variant leaves those fields alone; the effective palette is set by `palette: "teardown"`, which the render layer respects. Not re-scaffolding.

- **On-screen `BCRY.WantQuote.props.quote` updated to match the rewritten narration** (source read "can't be copied" / "it's not finished — it's a value dump"; both narration and quote now read "can't be pasted" / "it isn't finished — it's a value dump"). Keeping them out of sync would mean Liam saying a different sentence than the card shows.

- **`ClaudeComposerAsk.props.command` (on-screen card at BHTF) uses a shortened version** of the paste prompt, not the full one. The full paste prompt lives in `narration_text` and `llm_exercise.prompt`; the card would overflow if it carried the whole thing. This matches the sibling nbb-access variant, which does the same trim on its LLM-exercise card.

- **Not re-scaffolding.** Scaffold-set fields (`audience`, `register`, `palette`, `engine`, `voice_kokoro`, `typography`, `derived_from`, `outro_source`) left exactly as `brand_variant.py` wrote them.

## What did NOT change

- Every `beat_id`.
- Every `shot` block (visual production values, Manim scene IDs, Remotion patterns except the `BOUT` pattern swap noted above, media paths).
- Every `graphic.production_viz` block (labels, chips, captions, colors) on NB01/NB02/NB03.
- Every fact, number, template name, API name, and file-name reference from the source.
- Every `build` sub-block (status / src / filled_by / at) — these describe the current render state; the reel is 7/7 filled per source metadata.
- `lead_silence_s` on B00 (1.0) and BCRY (0.6), `tail_silence_s` on BOUT (1.0).
- B00 `note` field (TIMING LAW instructions for the writer scene).

## Not done here (correct — separate pass)

- No audio generated. Kokoro `am_onyx` regeneration and any recompile are the render pass.
- No render. `art run` / `art final` / `remotion_scenes.py` were not invoked.
- No files renamed or moved. `beat_sheet.json` and every source media file in the canonical folder are untouched.

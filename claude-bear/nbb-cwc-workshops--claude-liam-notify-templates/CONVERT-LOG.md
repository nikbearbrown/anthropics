# CONVERT-LOG — cwc-workshops--claude-liam-notify-templates → nbb

## What changed

Register rewrite only. Every fact from the source sheet survives unchanged: three fixed formats (low-stock Slack alert, supplier email, escalation for human review), fill-slots-from-data-then-append machinery, "do not spawn a subagent" ban, routing thresholds ($25k → purchasing lead; $100k outstanding or duplicate order → finance; at-here on active top-SKU stockout), daily-sweep batch rule (one summary + one JSON-outbox append; ≤ 2 tool calls per alert), SKU-0042 handoff numbers.

- **metadata** — `_variant_todo` removed. `purpose` rewritten in the Teardown lens (take-apart / evaluate / name scope). `folderLabel` and `channel_title` retargeted from `@HumanitariansAI` to `@NikBearBrown` so the composer chip and outro handle match the nbb channel (playlist ordering `Claude Basics` preserved). `audience`, `register`, `engine`, `voice_kokoro`, `palette`, `outro_source`, `derived_from`, `typography` left exactly as the scaffold set them.
- **B00** — Cold open rewritten to Teardown: names the design read ("Identical output — not authorship") before pivoting to the corrected question. Word count 33 to keep the BrutalistHesitantWriter TIMING LAW window (20–35 words + `lead_silence_s: 1.3`). On-screen hesitant-writer text (`text`, `triggerWords`, `replacementWords`, seed) preserved verbatim.
- **NB01** — Mechanism beat rewritten to explain the folder-as-skill machinery, name the three formats, and close with the design read: "They optimized for a reproducible append over adaptive judgment." Graphic label, chips, caption, colors, Manim scene name unchanged.
- **NB02** — Routing beat rewritten: same thresholds, same routes, ends with the design judgment "Routed by rule, not taste — auditable, at the cost of adaptability." Graphic block untouched.
- **NB03** — Batch beat rewritten: same rule, same ceiling, ends with the trade "Legible bill, legible paper trail — over per-SKU immediacy." Graphic block untouched.
- **BCRY** — Carry-out sentence left **unchanged** (see judgment call 1).
- **BHTF** — Converted from generic "your turn handoff" into the LLM EXERCISE beat. Added `llm_exercise` block (paste-ready prompt + go-deeper follow-up). `act` → `LLM EXERCISE`. Narration reads the full prompt + go-deeper aloud. `ClaudeComposerAsk.props.command` rewritten to numbered (1)/(2)/(3) form and shortened for the on-screen composer while preserving every constraint spoken in the prompt. `segment` set to the title. `folderLabel` retargeted to `@NikBearBrown`. `estimated_duration_s` bumped from 26 → 62 to reflect the longer read.
- **BOUT** — Outro pattern swapped `OutroSeries` → `OutroCTA` to match the nbb form (line + handle, no eyebrow). Narration ("Fill The Template. Don't Write It. Liam, in for Bear.") left as-is — already the nbb outro. `handle` set to `@NikBearBrown`.

## Judgment calls

1. **BCRY unchanged.** The source carry-out is already Teardown-native — the mechanism is named ("fills three fixed templates from data it already has") and the scope limit is named ("never one call per SKU"). WantQuote's on-screen text IS the quote, so touching the narration forces touching the graphic. Kept as-is; `sparkLine` "Fill it. Batch it. One append." already sings. Matches the same call the screenshot-caching nbb log made.
2. **Retarget to `@NikBearBrown` at every layer (metadata + composer chip + outro handle).** Followed the fully-completed screenshot-caching nbb precedent: nbb variants own the `@NikBearBrown` bookends even when the source was `@HumanitariansAI`. The half-completed `nbb-…-reorder-policy` (same book) still shows `@HumanitariansAI` because its `_variant_todo` never closed; not treated as convention.
3. **Colors kept humanitarians-cream (`#F3EBDD` / `#2F2A26` / `#E4572E`).** Metadata says `palette: teardown` but every completed nbb reel in this book leaves the underlying shot/graphic tokens as the humanitarians values under the nbb metadata. Matches convention; retinting is a downstream render concern.
4. **Manim scene names kept (`BDNB01Scene` … `BDNB03Scene`).** Same reason — the shot/graphic contract stays identical so the same scenes can be re-rendered against the teardown palette without a code change.
5. **BHTF became the LLM exercise beat (no new `B_LLM` beat_id).** Followed the screenshot-caching pattern of converting the existing handoff beat in place — same slot, same shot component, `act` retitled to `LLM EXERCISE`, `llm_exercise` block added. Inserting a new beat would have broken the 7-beat `filled/of` count in `metadata.build`.

## Not done (per supervisor instructions)

- No audio regeneration (`generate_audio_kokoro.py`).
- No Manim/Remotion render.
- No compile / no final master.
- No touch to source files in `cwc-workshops--claude-liam-notify-templates/`.

Deliverable: `beat_sheet.nbb.json` in this directory. Rendering is a separate pass.

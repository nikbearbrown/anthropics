# CONVERT-LOG — claude-quickstarts--macos-computer-use-coordinate-roundtrip → nbb

## What changed

Register rewrite only. Every fact from the source sheet survives unchanged: native 2560×1600 Retina, sent 1344×840, long-edge ≤ 1568, tile budget ≤ 1568 of the 28×28 tiles, `target_image_size` binary search, formula `real = model × (native / sent)`, worked pair `(630, 420) → (1200, 800)`, boundary case where sent = native.

- **B00** — Cold open rewritten to Teardown: names the mechanism ("Claude never sees your 2560 by 1600 Retina screen") and locates the real coordinate in the ratio, not the answer. On-screen hesitant-writer text, `triggerWords` ("exact") and `replacementWords` ("scaled") preserved verbatim.
- **B01** — Stakes/anchor beat now opens with the constraint that forces the transform (long-edge + tile budget) and closes with the explicit design read: "They optimized for a predictable tile budget at the expense of the pixel-perfect frame the OS actually rendered."
- **B02** — Wrong-guess beat rewritten; ends "an unavoidable side-effect of shipping the model a downsized copy without telling it the copy was downsized." Anchor pair mechanic + colors unchanged.
- **B03** — Mechanism beat now explains the ported binary search + why the sent dimensions are the denominator, and names the trade: "a simpler protocol, at the cost of every caller having to re-implement the ratio themselves."
- **B04** — Anchor payoff rewritten; ends with the design judgment: "This works if you value one transform that always runs; it fails if you needed the API to just hand back the sent size in the first place." The boundary case (sent = native, ratio collapses to 1) is now framed as one code path handling both cases.
- **BCRY** — Carry-out sentence left **unchanged** (see judgment call). `WantQuote.props.sparkLine` also kept as-is.
- **BHTF** — Converted from generic "your turn handoff" into the LLM EXERCISE beat. Added `llm_exercise` block (paste-ready prompt + go-deeper follow-up). `act` → `LLM EXERCISE`. Narration reads the full prompt + go-deeper aloud. `ClaudeComposerAsk.props.segment` set to "Two Resolutions, One Click."; `folderLabel` → `@NikBearBrown` to match the nbb channel. `command` prop rewritten to numbered (1)/(2)/(3) form and shortened for the on-screen composer while preserving every constraint from the spoken prompt (target_image_size, 1568-pixel long edge, 1568 tiles, boundary case, worked pair). `estimated_duration_s` bumped 24 → 60 for the longer LLM-exercise narration.
- **BOUT** — Outro left unchanged. Already the NikBearBrown-shaped `OutroCTA` with "Liam, in for Bear." `handle` updated `@HumanitariansAI` → `@NikBearBrown`.
- **metadata** — `_variant_todo` removed. `folderLabel` and new `channel_title` retargeted `@HumanitariansAI` → `@NikBearBrown` so composer chip and playlist ordering match the nbb channel. `register` was already `Teardown` in the scaffold. `purpose` rewritten in the Teardown lens (take-apart / evaluate / name scope + boundary case). `audience`, `engine`, `voice_kokoro`, `palette`, `outro_source`, `derived_from`, `typography` left exactly as the scaffold set them.

## Judgment calls

1. **BCRY unchanged.** The source carry-out is already Teardown-native — names the mechanism ("measured on a resized copy of your Retina screen") and gives the operation ("multiply back by native over sent") in one sentence. `WantQuote` renders the same string as narration and on-screen text, so touching either forces touching both; the `sparkLine` "Resized Retina picture, not a wrong number" already lands the design point. Kept as-is.
2. **B00 kept 4 lines of hesitant-writer text.** The `text` prop was tuned to `mistakeRate: 4`, `hesitateWithin: 2`, `hesitateBetween: 12`, `charMs: 38`, `seed: hai-qs-macos-coordinate-roundtrip` — a matched set for the ≥8s window called out in `note`. Rewriting the on-screen line would invalidate that timing recipe. Register rewrite lives in `narration_text`; the writer keeps its calibrated line.
3. **Colors kept humanitarians-cream (`#F3EBDD` / `#2F2A26` / `#E4572E` / `#1F4E5F`).** `metadata.palette` is `teardown` (per scaffold), but every reference nbb reel in `claude-bear/` leaves the underlying shot/graphic colors as humanitarians tokens under nbb metadata. Retinting is a downstream render concern; the shot contract stays identical so the same Manim scenes re-render cleanly against the teardown palette without a code change.
4. **Manim scene names kept (`B01Scene`…`B04Scene`).** Same reason as (3) — the graphic contract is intentionally palette-agnostic.
5. **`@NikBearBrown` folder chip + outro handle applied at shot-prop level.** No reference nbb reel bookends with `@HumanitariansAI`. Fixed on `ClaudeComposerAsk.props.folderLabel` and `OutroCTA.props.handle`; the underlying `playlist: "Claude Basics"` is preserved for ordering.
6. **BHTF became the LLM exercise beat (no new beat_id).** Reference nbb reels in this book convert BHTF in place — same slot, same shot component, `act` retitled to "LLM EXERCISE", `llm_exercise` block added. Followed that pattern rather than inserting a new `B_LLM`, which would have broken the 8-beat `filled/of` count in `metadata.build`.

## Not done (per supervisor instructions)

- No audio regeneration (`generate_audio_kokoro.py`).
- No Manim/Remotion render.
- No compile / no final master.
- No touch to source files in `claude-quickstarts--macos-computer-use-coordinate-roundtrip/`.
- `actual_duration_s` intentionally absent — audio has not been re-measured against the rewritten narration.

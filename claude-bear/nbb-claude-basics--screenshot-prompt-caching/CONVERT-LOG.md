# CONVERT-LOG — claude-basics--screenshot-prompt-caching → nbb

## What changed

Register rewrite only. Every fact from the source sheet survives unchanged: 50-turn task, 35 identical repeats, 5 unique states A–E, 2,000 tokens per screenshot, 70,000 tokens re-read, 100,000 uncached → 10,000 cached, 90% saved, `cache_control: {"type": "ephemeral"}`, TTL / minimum cacheable size / eviction / API-key switch as scope limits.

- **B00** — Cold open rewritten to Teardown: names the stateless-server design choice and the trade it imposes on the caller. On-screen hesitant-writer text (`text`, `triggerWords`, `replacementWords`) preserved verbatim.
- **B01** — Wrong-guess beat now closes with the explicit design read: "The design choice is statelessness. The cost is you pay full price for déjà vu."
- **B02** — Anchor beat rewritten; ends "the naked cost of a stateless server that trusts nothing about last turn." Filmstrip mechanic + colors unchanged.
- **B03** — Mechanism beat now explains the hash-behind-the-bytes machinery and names the trade: "opt-in, not automatic — they optimized for a simple protocol at the expense of a caller who has to know this feature exists to save the money."
- **B04** — Anchor payoff rewritten; ends with the design judgment: "This works if you value a stateless, opt-in API; it fails if you need durability you didn't ask for."
- **BCRY** — Carry-out sentence left **unchanged** (see judgment call).
- **BHTF** — Converted from generic "your turn handoff" into the LLM EXERCISE beat. Added `llm_exercise` block (paste-ready prompt + go-deeper follow-up). `act` → `LLM EXERCISE`. Narration reads the full prompt + go-deeper aloud. `ClaudeComposerAsk.props.segment` set to "Cached, Not Free."; `folderLabel` updated to `@NikBearBrown` to match the nbb channel. `command` prop rewritten to numbered (1)/(2)/(3) form and shortened for the on-screen composer while preserving every constraint from the spoken prompt.
- **BOUT** — Outro left unchanged. Already the NikBearBrown-shaped `OutroCTA` with "Liam, in for Bear." `handle` updated to `@NikBearBrown`.
- **metadata** — `_variant_todo` removed. `folderLabel` and `channel_title` retargeted from `@HumanitariansAI` to `@NikBearBrown` so the composer/outro chip and playlist ordering match the nbb channel. `purpose` rewritten in the Teardown lens (take-apart / evaluate / name scope). `audience`, `register`, `engine`, `voice_kokoro`, `palette`, `outro_source`, `derived_from`, `typography` left exactly as the scaffold set them.

## Judgment calls

1. **BCRY unchanged.** The source carry-out sentence is already a Teardown-native form — mechanism named ("flag it as one you've already shown"), scope limit named ("only until the picture actually changes"). WantQuote's on-screen text IS the quote, so touching either forces touching both. Kept as-is; the sparkLine "Cached, not free." already sings.
2. **Colors kept humanitarians-cream (`#F3EBDD` / `#2F2A26` / `#E4572E`).** Metadata says `palette: teardown` but the reference nbb reels in `claude-bear/` (e.g. `nbb-books--claude-liam-building-plugins`) leave the underlying shot/graphic colors as the humanitarians tokens even under the nbb metadata. Matches convention; nothing was retinted.
3. **Manim scene names kept (`SPCB01Scene` … `SPCB04Scene`).** Retinting is a downstream render concern; the shot/graphic contract stays identical so the same scenes can be re-rendered against the teardown palette without a code change.
4. **`@NikBearBrown` folder chip + outro handle.** Applied to shot props even though metadata channel stayed labelled — no reference reel bookends a NikBearBrown reel with `@HumanitariansAI` on the composer chip. Fixed at the shot level, not the metadata level, so the underlying identity for playlist ordering (`Claude Basics`) is preserved.
5. **BHTF became the LLM exercise beat (no new beat_id).** Reference nbb reels in this book (`nbb-books--claude-liam-*`) convert BHTF in place — same slot, same shot component, `act` retitled to "LLM EXERCISE", `llm_exercise` block added. Followed that pattern rather than inserting a new `B_LLM` beat, which would have broken the 8-beat `filled/of` count in `metadata.build`.

## Not done (per supervisor instructions)

- No audio regeneration (`generate_audio_kokoro.py`).
- No Manim/Remotion render.
- No compile / no final master.
- No touch to source files in `claude-basics--screenshot-prompt-caching/`.

Deliverable: `beat_sheet.nbb.json` in this directory. Rendering is a separate pass.

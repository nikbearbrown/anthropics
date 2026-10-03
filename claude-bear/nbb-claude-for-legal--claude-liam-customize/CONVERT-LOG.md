# CONVERT-LOG — nbb-claude-for-legal--claude-liam-customize

**Source:** `anthropics/claude-bear/claude-for-legal--claude-liam-customize/beat_sheet.json`
(Plain register, HAI-fellows brand, 8 beats: B00, B01, B02, B03, BCRY, BHTF, BOUT, BCTA)

**Target:** `beat_sheet.nbb.json` (Teardown register, NBB brand, 7 beats)

## What changed

**Narration — every beat rewritten in the Teardown register** (`prose/teardown/PROSE.md` + `brands/nbb.md`). Explained the machinery instead of naming it; surfaced the design choice ("optimized for legibility / predictability / narrow reliable shape") and its trade-off. No fabrication — every claim about the customize skill (folder + SKILL.md, linear Steps section, one-task scope) is preserved from the source.

- **B00 cold open** — now opens with "I'm Liam, in for Bear." (IN-FOR-BEAR LAW). Rewrites the "wonder" framing into a Teardown "here's what's actually happening" open. Word count kept close to source (~43 vs 36); TIMING LAW window for BrutalistHesitantWriter's typing is still covered.
- **B01 anatomy** — added the design-philosophy read ("optimized for legibility: you can read the same file Claude reads"). Kept SkillTeardownAnatomy props verbatim.
- **B02 pipeline** — added "optimized for predictability over cleverness." Props unchanged.
- **B03 mechanism** — reframed as "the interesting constraint" + explicit trade-off ("reliable within its boundary, silent outside it"). SkillTeardownMechanism `sparkLine` updated to match.
- **BCRY carry-out** — opens with "So here's the carry-out." Updated the WantQuote `quote` and `sparkLine` to the rewritten wording.

**BHTF — repurposed into the LLM EXERCISE beat (second-to-last).** The source beat was already a "your turn handoff" with ClaudeComposerAsk + paste prompt, so preserving the `beat_id` while switching `act` to `LLM EXERCISE` matches peer nbb reels (e.g. `nbb-books--claude-liam-data`). Added the `llm_exercise` object with:
- `prompt` — a self-contained ask for the frontier LLM (design a small SKILL.md for standup notes) that produces useful output without the video.
- `dig_deeper` — a real next question (when a Skill is the *wrong* tool), not a summary.
Updated the ClaudeComposerAsk props: `folderLabel` → `@NikBearBrown`, `topic` → "LLM EXERCISE · CUSTOMIZE SKILL", command text = shortened prompt.

**Outro collapse — BOUT + BCTA merged into a single OutroCTA beat.** Follows the peer nbb-data pattern: one closing beat reading "Claude, Customize — the customize skill. Liam, in for Bear.", `handle: "@NikBearBrown"`. This lets the LLM EXERCISE beat land as the strict second-to-last per Step 5, matching the SKILL's ending-order rule.

**Metadata** — set `brand: "nbb"`, `folderLabel: "@NikBearBrown"`, `channel_title: "@NikBearBrown"`, purpose rewritten in Teardown register, `redo_of` updated to point at the Plain-register source, `build` counters reset (rendering is a separate pass), `_variant_todo` removed. Scaffold-set fields (`audience`, `register`, `palette`, `engine`, `voice_kokoro`, `typography`, `outro_source`, `derived_from`) left untouched per instructions.

## Judgement calls

- **Collapsed BOUT + BCTA into one OutroCTA (dropped BCTA `beat_id`).** The task requires the LLM exercise to be *second-to-last* and the outro to be *last* — a two-part outro (Series + CTA) would push the LLM exercise to third-to-last. Peer nbb reels (`nbb-books--claude-liam-data`, `nbb-books--claude-liam-building-plugins`) consistently collapse to a single OutroCTA. I followed that precedent; it costs one preserved `beat_id` (BCTA) to satisfy the harder rule.
- **Kept per-beat palette props (`bg: #F3EBDD`, `ink: #2F2A26`, `accent: #E4572E`) unchanged** even though metadata `palette: teardown` would call for white/ink/red. Same peer-reel precedent: they keep the source visual continuity and let the metadata field flag the intent. I did not re-scaffold or repaint scenes; rendering will surface any mismatch downstream.
- **Left the `topic` field as "CLAUDE BASICS · CUSTOMIZE SKILL"** (describes content, not channel). Only channel-facing text (folderLabel, channel_title, handle) was flipped to `@NikBearBrown`.
- **Did not regenerate audio, compile, or render.** Deliverable is the beat sheet only, per invocation contract.

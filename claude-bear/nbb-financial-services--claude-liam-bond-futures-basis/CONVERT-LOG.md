# CONVERT-LOG — nbb-financial-services--claude-liam-bond-futures-basis

Converted `beat_sheet.json` → `beat_sheet.nbb.json` under the NikBearBrown / Teardown register.

## What changed

- **Register:** every `narration_text` rewritten in Teardown (Feynman × MKBHD) — took the skill apart, named the design choice ("reproducible ranking at the expense of trader's judgment"), and separated mechanism ("the wiring works") from verdict ("whether the trade works is a separate question"). Facts unchanged: futures price × conversion factor → delivery cost → implied repo rate, rank across the deliverable basket, compare implied repo to market repo, ranking gets rerun when yields move.
- **B00 cold open:** now includes "Liam here, in for Bear" per IN-FOR-BEAR LAW; word count stayed inside the 20–35 window the WRITER LAW note requires. Kept `BrutalistHesitantWriter` props unchanged (feel → the math correction survives).
- **BCRY:** WantQuote `quote` prop was updated to match the rewritten carry-out narration verbatim (they must stay in sync — the quote is displayed while the narration is spoken). `sparkLine` "Ranked by cost, not favored." kept — still captures the carry-out cleanly.
- **BHTF → LLM EXERCISE:** was "your turn handoff." Rewrote as a paste-ready prompt targeting Claude / ChatGPT / Gemini (concrete basket: three bonds with prices + conversion factors, futures price 105.00, market repo 4.75%), with a "Go deeper" question that pushes into duration-based cheapest-to-deliver switching. `llm_exercise` object added; `ClaudeComposerAsk.command` shortened to fit the composer card while the full prompt lives in `llm_exercise.prompt`.
- **BOUT:** narration signs off "Liam, in for Bear. Brutalist dot art." (audio speaks "dot art"; the OutroCTA `line` prop shows the URL "www.brutalist.art"). `handle` switched from `@HumanitariansAI` to `@NikBearBrown` per the NikBearBrown outro rule (default channel: www.brutalist.art).
- **Metadata:** removed `_variant_todo` (all five items done). Kept `channel_title` and `folderLabel` as `@HumanitariansAI` since those are inherited fields on the ClaudeComposerAsk and top-level channel routing set by the scaffold — only the outro's on-screen handle changed to `@NikBearBrown`.

## Judgement calls

- **Reproducibility framing.** The source's B01 falsification was about "won't favor a bond you like." Teardown asks *what was optimized for at what cost.* Framed as "reproducible ranking at the expense of trader's judgment" — same fact, design lens.
- **BCRY sync.** Followed the sibling `nbb-…-3-statement-model` precedent: the WantQuote `quote` and `narration_text` are kept identical. If the compile step reads only one of them for the on-screen card, they still match.
- **BOUT handle switch.** The source reel is a HumanitariansAI-channel piece (Claude Basics playlist). The NikBearBrown cut's outro is a NikBearBrown thing by construction — handle → `@NikBearBrown`, URL → `www.brutalist.art`. Matches every other nbb-financial-services sibling I inspected.
- **Estimated durations.** Bumped upward for the rewritten beats since the Teardown rewrites are longer than the source (they name the trade-off, not just the mechanic). Audio-first — the compile pass will regenerate MP3s and derive true `actual_duration_s`; these estimates are planning-only and can be off by 30%+.
- **No rendering, no audio.** Deliverable is the beat sheet. Compile / Kokoro / Remotion are downstream, not this pass.

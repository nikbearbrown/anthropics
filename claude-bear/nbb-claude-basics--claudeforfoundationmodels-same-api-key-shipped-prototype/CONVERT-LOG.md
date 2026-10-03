# CONVERT-LOG — nbb cut

Source: `anthropics/claude-bear/claude-basics--claudeforfoundationmodels-same-api-key-shipped-prototype/beat_sheet.json`
Register: Plain → Teardown (Feynman × MKBHD)
Voice: Kokoro `am_onyx` — Liam, in for Bear (scaffold-set, unchanged)
Palette: teardown

## What changed

- **Every body beat rewritten in Teardown register** (B00, B01, B02, B03, B04, BCRY). Facts preserved verbatim: the same `.apiKey("sk-ant-...")` → `.proxied(headers:[...])` code case, the same relay at `yourcompany.com`, the same threat-model flip, the same server-you-control exception. Voice shifted to explain the actual machinery, name the axis the fix operates on, and mark the trade-off (obfuscation optimizes for reader friction; only removing the key from the device changes what a determined user can reach).
- **BCRY carry-out**: narration and the `WantQuote` `quote` prop rewritten together so the on-screen sentence matches the read line.
- **B00 hesitant writer**: the `hide → move` trigger/replacement contract was preserved intact — my rewrite still lands on "you don't hide it, you move it" so the on-screen live-edit still pays off. Word count kept in the 20–35 range per WRITER LAW.
- **BHTF repurposed into the LLM EXERCISE beat** (second-to-last), matching the pattern in `nbb-books--claude-liam-building-plugins`: added `llm_exercise: { prompt, dig_deeper }`, updated `narration_text` to speak the paste-ready prompt + dig-deeper follow-up, updated the `ClaudeComposerAsk` `command` prop to the same prompt (shorter form to fit on screen), swapped `segment` from "Your Turn" to "LLM Exercise", added the required empty `output: []` prop.
- **BOUT NikBearBrown outro** (last): line rewritten to "Where a Secret Lives — moving the key off the device. Liam, in for Bear."; `OutroCTA` `line` prop kept in sync.
- **Metadata**: `_variant_todo` removed; `register` corrected from "Plain" (left over in the source-copy of metadata) to "Teardown"; `purpose` rewritten to describe the Teardown angle. `audience`, `engine`, `voice_kokoro`, `palette`, `outro_source`, `typography`, `derived_from` left as the scaffold set them.
- **Not touched**: `beat_id`, `act` (except BHTF → LLM EXERCISE per the SKILL's Step 3), `shot.type`, `graphic.production_viz` (label / mechanic / colors — those are internal build specs for the manim author; the compile picks palette from metadata), all timing hints, `note` on B00, `build` blocks, `audio_file` paths.

## Judgement calls

- **BHTF as the LLM slot, not a new B_LLM beat.** SKILL.md §Step 3 shows a `beat_id: B_LLM` example, but every completed nbb reel in `anthropics/claude-bear/nbb-*/` reuses the existing `BHTF` "your turn handoff" slot for the LLM exercise (same `beat_id`, `act: "LLM EXERCISE"`, `llm_exercise` field added, `ClaudeComposerAsk` retained). Followed the shipping pattern rather than the doc example — the shipping pattern is what the compiler expects and what audio/media paths are already scaffolded for.
- **Channel handle stays `@HumanitariansAI`.** `brands/nbb.md` implies `@NikBearBrown` as the NBB default channel, but every converted nbb reel in this book keeps the source reel's `folderLabel` / `handle` (this reel plays in the Claude Basics playlist on @HumanitariansAI). Kept parity with those.
- **`estimated_duration_s` bumped** for B01/B02/B03/B04 and BHTF to reflect the longer Teardown-register narration. Kokoro measures the real duration during audio generation; the estimate just seeds the timing plan.
- **`graphic.production_viz.colors` untouched** even though they list terracotta (`#E4572E`) rather than teardown crimson (`#C8102E`). The compile pulls palette from `metadata.palette`; the color list here is a hint for the scene author, and the invocation's preserve-exactly rule covers shot blocks.

## Not done

- No audio regen. No render. No compile. Deliverable is `beat_sheet.nbb.json` only, per the invocation.

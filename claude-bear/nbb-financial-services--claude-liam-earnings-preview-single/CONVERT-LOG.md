# CONVERT-LOG — financial-services--claude-liam-earnings-preview-single (nbb cut)

Converted 2026-09-03. Source register: Plain. Target: Teardown (Feynman × MKBHD).

## What changed

- **All 11 narrations rewritten** in the Teardown register — explain the mechanism, name the design choice, name the trade-off ("They optimized for consistency at the expense of ever forming a stock view"). Facts, files, and numbers preserved verbatim (four categories, four-to-five page template, forty-four pages, `SKILL.md`, `report-template.md`).
- **B00 cold open** — added Liam self-identification ("Liam here, in for Bear.") per IN-FOR-BEAR LAW. Kept 33 words to stay inside the 20–35 window the TIMING LAW note enforces.
- **BCRY (WantQuote)** — rewrote the quote prop to match the new narration so on-screen text and voiceover stay identical. `sparkLine: "Template, not a view."` kept as the tag.
- **BHTF → LLM EXERCISE beat.** BHTF was already the "paste this into Claude" handoff in the second-to-last slot, so structurally it became the LLM exercise beat directly:
  - Added `llm_exercise.prompt` — a paste-ready pre-flight-map prompt for Claude / ChatGPT / Gemini (map the skill's categories of fact and where it takes a position, without writing the report).
  - Added `llm_exercise.dig_deeper` — asks the viewer to design a skill of their own in a domain they know and locate the human-judgment boundary.
  - `act` changed from `"your turn handoff"` to `"LLM EXERCISE"`.
  - `ClaudeComposerAsk.props.command` shortened to a visual version of the same prompt (composer readability).
- **BOUT (outro)** — rewrote to the NBB sign-off: "Claude, Earnings Preview Single. Template, not a view. Liam, in for Bear. Nik Bear Brown, on YouTube." `handle` prop switched from `@HumanitariansAI` to `@NikBearBrown`. `estimated_duration_s` bumped 6→8 for the added phrase.
- **Metadata** — `_variant_todo` removed. `folderLabel` and `channel_title` set to `@NikBearBrown`. `purpose` rewritten to describe the Teardown thesis. `register` was already `Teardown` from the scaffold.

## Preserved exactly

- Every `beat_id`, `act` (except BHTF, deliberate), shot type, Manim scene id, `production_viz` block, chip labels, `pairs`, `strike`/`accent` arrays, `graphic.manim` refs, `build` records, `audio_file` paths, `remotion.pattern` names, and all four fact categories (transcript, competitors, valuation, news).
- Palette values in `graphic.production_viz.colors` were left as the source cream/ink/orange even though `metadata.palette` is now `teardown`. These are per-graphic values that already existed in the rendered `manim/*.mp4` files; changing them here without re-rendering would only cause drift between the JSON and the media. If the reel is re-rendered, palette should be reconciled then, not by this pass.

## Judgement calls

- **Channel identity.** The scaffold left `folderLabel` and `channel_title` at `@HumanitariansAI`. For a full NBB cut I flipped both to `@NikBearBrown` — the outro is the NBB outro (Step 4), so leaving the composer chip and channel title on the HAI handle would visibly contradict the sign-off. `playlist` ("Claude Basics") kept as-is since playlist names transfer cleanly across channels.
- **The LLM exercise slot.** The source's BHTF was already a "paste this into Claude" beat in the second-to-last position, so I promoted it into the proper `llm_exercise` schema rather than inserting a fresh beat and duplicating the handoff. Ending order body → LLM exercise → outro is satisfied.
- **BOUT duration bump.** 6→8 seconds for the added "Nik Bear Brown, on YouTube." tail. Audio pass will confirm; `tail_silence_s` unchanged at 1.0.

## Not done (out of scope for this pass)

- No audio generation. No Manim re-render (see palette note). No compile. Rendering is the next pass.

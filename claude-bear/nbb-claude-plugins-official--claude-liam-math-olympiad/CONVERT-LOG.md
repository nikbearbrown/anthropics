# CONVERT-LOG — nbb-claude-plugins-official--claude-liam-math-olympiad

Converted `beat_sheet.json` → `beat_sheet.nbb.json` (Plain → Teardown register).

## What changed

- **All narrations rewritten in Teardown register** — Feynman × MKBHD voice (`prose/teardown/PROSE.md`, `brands/nbb.md`). "Here's what's actually happening…", "They optimized for X at the expense of Y", "This works if you value X; it fails if you need Y." No fabrication; every number, name, and claim from the source survives (8-12 solvers, 5 rounds, 4 confirm / 2 refute, no calculator / no code, etc.).
- **BHTF** was the source's "your turn handoff" (act) — repurposed as the `LLM EXERCISE` beat per SKILL Step 3. Added `llm_exercise: { prompt, dig_deeper }` and rewrote the `ClaudeComposerAsk.command` to be a numbered paste-ready prompt. `segment` prop changed from the title to the sparkLine "Hidden Reasoning. Blind Verifier." to match the LLM-exercise framing.
- **BOUT** switched from `OutroSeries` (source) to `OutroCTA` (per sibling nbb precedent — see `nbb-claude-quickstarts--claude-liam-first-run` and `nbb-claude-basics--screenshot-prompt-caching`). Handle stays `@HumanitariansAI` because the source is a HAI-channel reel; the NBB cut is a register variant, not a channel switch.
- **`_variant_todo` removed** from metadata.

## Judgement calls

- **BCRY carry-out kept verbatim.** `metadata.gate_c` reads `SIGNED - CARRY-OUT.md`, so the signed line was preserved word-for-word in both `narration_text` and the `WantQuote.quote` prop. Re-voicing a signed carry-out would break the sign-off.
- **No separate B_LLM beat inserted.** The source already had a "your turn handoff" beat (BHTF) at the second-to-last position with a paste-ready Claude prompt; adding another distinct B_LLM beat after it would double the ask. Instead, BHTF was upgraded in place (act → `LLM EXERCISE`, added `llm_exercise` object, added "Go deeper: …" tail). This matches every sibling nbb- conversion under `anthropics/claude-bear/`.
- **`estimated_duration_s` bumped** on B00 (13→15), NB01 (22→26), NB02 (24→28), NB03 (20→22), and BHTF (22→40) because the Teardown-register rewrites and the added dig-deeper tail are longer than the Plain-register source. Actual durations get measured after audio is generated; these are hints, not clocks.
- **Handle stayed `@HumanitariansAI`.** `brands/nbb.md` names `www.brutalist.art` as the default channel and `AUTHOR.MD` points at `@NikBearBrown`, but the sibling nbb-first-run — same source-channel shape — kept its source handle. Following that precedent rather than the brand default.

## Not done (by design)

- No audio generated. No render. No compile. `mp3/`, `manim/`, `media/` are unchanged; the `build` blocks on each beat carry the source's old status/timestamps and will be overwritten by the next real build.

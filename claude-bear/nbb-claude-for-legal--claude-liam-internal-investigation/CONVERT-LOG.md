# CONVERT-LOG — nbb conversion

Source: `anthropics/claude-for-legal/youtube/claude-liam-internal-investigation/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)
Date: 2026-09-03
Voice: Kokoro `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW).

## What changed

- **All 11 narrations rewritten in the Teardown register** (Feynman × MKBHD).
  Facts, numbers, file names, and claims preserved. The rewrites take the skill
  apart mechanically ("execution model is boring on purpose", "replayable
  process, not fresh opinion"), name the design choice ("They optimized for
  consistency … what that costs you"), and land the trade-off explicitly
  ("output tells you about the spec, not about the truth underneath").
- **BCRY (carry-out) prop `quote` updated** to match the rewritten narration so
  the on-screen quote reads what Liam says.
- **BHTF converted to the LLM-exercise beat (second-to-last)** per
  `skills/make/nbb/SKILL.md` §Step 3. Added the `llm_exercise` object with
  `prompt` and `dig_deeper`, changed `act` to `LLM EXERCISE`, rewrote the
  narration in the Teardown register to open with "paste directly into Claude,
  ChatGPT, or Gemini" and close with the "Go deeper:" question. Shot kept as
  `ClaudeComposerAsk` (already the correct scene for the Ask/intro rule); the
  `command` prop tightened to the new prompt's headline.
- **BOUT converted to the NikBearBrown outro (last)**. Line rewritten to
  "Claude, Internal Investigation. Liam, in for Bear. Take it apart — brutalist.art.",
  handle changed from `@HumanitariansAI` to `www.brutalist.art` per NBB brand
  spec default channel.
- **`_variant_todo` removed** from metadata.
- **`purpose` in metadata rewritten** to describe the Teardown framing (still
  the same reel, still the same carry-out).
- `register: "Teardown"` (was `"Plain"` after scaffold).

## Judgement calls

1. **BHTF vs. inserting a new B_LLM.** The source already had a paste-into-Claude
   "your turn" beat (BHTF). Inserting a separate `B_LLM` would have duplicated
   its function and pushed BHTF into a redundant slot before the outro. I
   converted BHTF in place: same `beat_id` and shot preserved (per the standing
   "preserve every beat_id and shot block" rule), `act` renamed to
   `LLM EXERCISE`, `llm_exercise` object added. Ending order now reads
   `… body … BCRY (carry-out) → BHTF (LLM exercise) → BOUT (NBB outro)`,
   which satisfies §Step 5.
2. **B00 shot left as `BrutalistHesitantWriter`, not swapped to
   `ClaudeComposerAsk`.** The Ask/intro-scene rule applies to the ASK beat;
   BHTF is the Ask beat here and already uses `ClaudeComposerAsk`. B00 is a
   hesitant-writer cold open specific to hai-simple's WRITER LAW; swapping it
   would be structural, not register work, and the standing rule says preserve
   `shot` blocks. Left alone.
3. **`folderLabel` / `channel_title` in top-level metadata left as
   `@HumanitariansAI`.** `brand_variant.py` did not overwrite these; changing
   channel routing at the metadata level is outside the register conversion.
   Only the outro's `handle` was changed (that's the on-screen NBB CTA the
   brand spec explicitly requires).
4. **On-screen card labels/captions/chips kept verbatim.** They already fit the
   Teardown register (short, mechanical, no forbidden words) and rewriting them
   would risk desyncing with the built Manim scenes.

## Not done (deliberate)

- No render, no audio generation, no compile — per the supervisor prompt, the
  next pass owns that.

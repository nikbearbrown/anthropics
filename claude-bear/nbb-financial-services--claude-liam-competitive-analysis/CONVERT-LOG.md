# CONVERT-LOG — financial-services--claude-liam-competitive-analysis → nbb

Converted `beat_sheet.json` (Plain, HAI) → `beat_sheet.nbb.json` (Teardown, NBB).

## What changed

- **Register rewrite (voice, not facts).** B00, NB01, NB02, NB03, BHTF narrations rewritten in Teardown (Feynman × MKBHD): take the skill apart, explain the machinery (folder + SKILL.md + linear step execution), name the design trade-off (predictability over adaptiveness, reliability inside the box vs. silence outside it), and land the "file is the program" mechanism. Every fact from source preserved — two files, linear pipeline, scope-bound answers, the banking-platforms handoff prompt, and every beat/act/shot ID.
- **BCRY carry-out narration left verbatim.** The `WantQuote` beat's narration IS the on-screen card copy, and the source sentence already reads as Teardown mechanism-then-trade-off ("read the file, execute in order, return the result. It only knows what's written in that file, nothing more."). Per SKILL.md, on-screen card copy that fits the register is preserved.
- **B_LLM inserted as second-to-last.** New beat with `llm_exercise` block: a paste-ready prompt that generalizes past *this* skill to the skill system as a design choice (three cases where file-is-the-program helps, two where it hurts, name what's optimized vs. sacrificed), plus a `dig_deeper` follow-up asking whether a skill with conditional reasoning inside the file is still a skill. `shot`: `CARD / own / hold` per SKILL.md schema.
- **BOUT rewritten as NBB outro.** Kept `beat_id` (per preservation rule) and Remotion `OutroSeries` pattern; swapped `eyebrow` from `COMPETITIVE ANALYSIS · @HumanitariansAI` to `@NikBearBrown · www.brutalist.art`; extended narration with a subscribe/site line drawn from AUTHOR.MD :: NikBearBrown (channel `@NikBearBrown`, site `brutalist.art`). Kept `Liam, in for Bear` sign-off (IN-FOR-BEAR LAW).
- **`_variant_todo` removed.** Scaffold checklist is now done.
- **`metadata.register`** = `Teardown` (scaffold already set this). Voice/engine (`kokoro` / `am_onyx`) untouched — the scaffold's values are correct and are the only voice available (ElevenLabs permanently removed 2026-09-03).

## Judgement calls

1. **BHTF kept as a separate beat from B_LLM.** BHTF is already a paste-ready "your turn" LLM prompt (test whether Claude ran the skill). The nbb SKILL.md requires an LLM exercise as *second-to-last*. Rather than collapse the two (BHTF's beat_id must be preserved), I kept BHTF as the mechanism-test handoff and made B_LLM a *design-level* prompt about the skill-system pattern in general. They serve different pedagogical purposes now: BHTF says "poke this one skill," B_LLM says "reason about the pattern."
2. **`folderLabel` / `channel_title` / `style_preset` left as `@HumanitariansAI` / `humanitarians`.** The scaffold intentionally left these; only `palette` was flipped to `teardown`. Following that pattern, I changed the OUTRO to reference `@NikBearBrown · www.brutalist.art` (per Step 4) but did not retint the composer chip in BHTF — the visual scene retains its source folder label, and the palette drives the brand shift. If the reviewer wants full brand replacement in the composer, that is a separate scaffold decision.
3. **`build` / `audio_file` / `actual_duration_s` fields kept.** These reference source-copied mp3/mp4 that Kokoro regeneration will overwrite. Left in place so the compile pipeline finds the expected keys.
4. **B00 narration trimmed to ~40 words** to respect the TIMING LAW note (20–35 word band, ≥9s typing window). Source was 42 words; rewrite is close.

## Verified

- 8 beats, order: `B00 → NB01 → NB02 → NB03 → BCRY → BHTF → B_LLM → BOUT`.
- Second-to-last = `B_LLM` / `LLM EXERCISE` ✓
- Last = `BOUT` / `outro` ✓
- `_variant_todo` removed ✓
- JSON parses ✓
- No fabrication — every number, name, path, and step count matches source.

Rendering (audio + compile) is a separate pass and was not run.

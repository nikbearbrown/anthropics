# CONVERT-LOG — nbb-claude-for-legal--claude-liam-comments

Register-conversion pass over the scaffold produced by `brand_variant.py`. No
render, no audio, no compile — beat sheet only.

## What changed

- **`_variant_todo` removed.** Every item in it was completed by this pass.
- **Every `narration_text` rewritten in the Teardown register** (Feynman ×
  MKBHD): take-it-apart phrasing, named design choice + trade-off at B02 and
  B03, no forbidden phrases. Facts unchanged — every specific from the source
  (federal agency proposes a rule, sixty-day comment period, no built-in
  connection to any docket, SKILL.md's three lines — review open periods, log
  decisions, track deadlines — reads-fresh-each-session, March 2nd rule
  logged on day 59, one-flag record: filed / not filed / waived, "logged ≠
  good" and "not logged ≠ missed") is preserved verbatim in meaning.
- **BHTF converted from a plain Your-Turn handoff into the LLM EXERCISE beat**
  (second-to-last, per SKILL.md §Step 3). Added an `llm_exercise` block with
  a paste-ready `prompt` for Claude / ChatGPT / Gemini and a real
  `dig_deeper` follow-up. Narration reads the prompt out loud (Liam,
  am_onyx). `ClaudeComposerAsk` props updated: `segment` → "Claude,
  Comments.", `runningText` → "paste this into Claude, ChatGPT, or Gemini…",
  `command` → the same prompt text, `output: []` added to match the sibling
  cease-desist contract.
- **BOUT broadened** to match the NikBearBrown outro convention in sibling
  reels (e.g. `nbb-claude-for-legal--claude-liam-cease-desist`): "Claude,
  Comments — the regulatory comments Skill. Liam, in for Bear." Handle
  unchanged (`@HumanitariansAI`) per scaffold + sibling.

## Ending order (verified)

B00 → B01 → B02 → B03 → BCRY → **BHTF (LLM EXERCISE, second-to-last)** →
**BOUT (NikBearBrown outro, last)**.

## Judgement calls

- **B00 word count.** Kept the cold-open narration at ~32 words + 0.8s lead
  silence to preserve the sibling TIMING LAW (BrutalistHesitantWriter needs a
  ≥ 9s window; ≥ 8s rendered). Reworded around the "know → track" hesitation
  the existing Remotion prop set is seeded for; the correction still lands.
- **Estimated durations bumped** on B01 / B02 / B03 / BCRY / BHTF to reflect
  the longer Teardown rewrites. Kept in step with actual word counts. The
  `actual_duration_s` fields from the source sheet were dropped — those were
  measured against the old Plain narrations and would mislead the next
  audio-first pass; `generate_audio_kokoro.py` will re-measure at build.
- **Voice + engine untouched.** `engine: kokoro`, `voice_kokoro: am_onyx` — Liam,
  in for Bear (IN-FOR-BEAR LAW). Never touched a paid voice; there is no
  paid voice on this brand any more (ElevenLabs removed 2026-09-03).
- **Handle stays `@HumanitariansAI`.** The scaffold set it that way and every
  fully-converted sibling in `claude-bear/nbb-claude-for-legal--*/` keeps it —
  did not swap to the SKILL.md default `www.brutalist.art` on the basis of a
  single line.
- **Palette + typography untouched.** Scaffold set `palette: teardown` and the
  Montserrat / EB Garamond / PT Mono trio; kept as-is. `ground: "#F3EBDD"` was
  left as scaffolded — it is the BrutalistHesitantWriter background prop, not
  a palette override, so leaving it matches sibling reels.

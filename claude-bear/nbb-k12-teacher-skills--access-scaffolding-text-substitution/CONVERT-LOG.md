# CONVERT-LOG — nbb-k12-teacher-skills--access-scaffolding-text-substitution

Converted from `../k12-teacher-skills--access-scaffolding-text-substitution/beat_sheet.json`
into the NikBearBrown / Teardown cut. Voice-only rewrite; facts, beat IDs, act
structure, shot blocks, and Manim/Remotion patterns preserved.

## What changed

- **All 8 source beats re-voiced in Teardown register** (Feynman × MKBHD):
  narration now explains the machinery ("Under the hood the scaffold does
  three things…"), names the design trade-off ("optimized for reading and
  sacrificed the standard"), and evaluates on removal ("if comprehension
  collapses on removal, the support was never a scaffold"). Word counts kept
  close to originals so pacing stays in the ballpark.
- **B00 cold open** now identifies Liam by name per the IN-FOR-BEAR LAW
  ("Liam here, in for Bear…"). BrutalistHesitantWriter on-screen text
  (`text` prop) preserved verbatim — the typing animation config is
  timing-tuned and the SKILL requires on-screen card copy to be kept where
  it still fits the register. The typed prompt still lands the same
  "simpler → scaffolded" correction that anchors the beat.
- **BCRY carry-out**: rewrote both `narration_text` and the on-screen
  `quote` prop to match the Teardown line ("optimizes for reading and
  sacrifices the standard… keeps both"). Both sides of the beat now say the
  same thing; the sparkLine "Same words. Better support." still holds.
- **B_LLM inserted as second-to-last beat** with the `llm_exercise` schema
  from `skills/make/nbb/SKILL.md §Step 3`:
  - `prompt` — a paste-ready block for any frontier LLM: asks for a
    scaffolded version of a supplied passage plus a fade schedule with the
    behavioral evidence required before each removal. Produces useful
    output on its own without watching the video.
  - `dig_deeper` — real next question the video didn't answer (earliest
    behavioral signal that a scaffold has become a crutch, catchable in the
    next quiz not at the end of the unit).
- **BOUT outro** rewritten to the NikBearBrown outro: eyebrow updated to
  `ACCESS SCAFFOLDING · @NikBearBrown`, narration adds the channel and the
  brutalist.art callout ("Liam, in for Bear, on NikBearBrown. More
  teardowns at brutalist dot art."). Duration bumped 6s → 8s to fit the
  added callout.
- **Ending order** verified: … NB01–NB04 → BCRY → BHTF → **B_LLM** → **BOUT**.
- **`_variant_todo` removed** from metadata.
- **Register metadata** confirmed as `Teardown` (already set by the scaffold).
- **Channel labels** flipped from `@HumanitariansAI` → `@NikBearBrown` in
  metadata (`folderLabel`, `channel_title`) and in the BHTF
  `ClaudeComposerAsk.folderLabel` prop, so the on-screen chip matches the
  audience.
- **`outro_source`** annotated with the fallback used
  (`AUTHOR.MD :: NikBearBrown (default: www.brutalist.art)`).

## Judgement calls

- **BHTF was kept as a body beat, not converted into B_LLM.** BHTF was
  already a paste-ready Claude prompt in the source, but the SKILL says to
  *insert* the LLM exercise as second-to-last while *preserving every
  beat_id*. Rewrote BHTF's narration to be the "your turn — in your own
  classroom" hand-off and added the standardized B_LLM beat after it. The
  two now serve distinct roles: BHTF is the classroom-facing invitation and
  design-check, B_LLM is the paste-ready prompt + dig-deeper follow-up.
- **`palette: "teardown"` kept; `ground: "#F3EBDD"` left untouched.** The
  scaffold set `palette` to `teardown` but left the humanitarians ground
  colour and `style_preset: "humanitarians"` in place, along with the cream
  ground and terracotta accent inside the BrutalistHesitantWriter props.
  Not re-scaffolding per instructions — the render pass will resolve any
  palette/token conflict.
- **`estimated_duration_s` left as originals** for the eight existing
  beats even though narration word counts moved a little. Audio-first: the
  Kokoro pass will overwrite `actual_duration_s`. Set 26s for the new
  B_LLM beat (26-second read for a ~78-word prompt intro) and 8s for the
  slightly longer BOUT.
- **AUTHOR.MD not present** at `anthropics/claude-bear/AUTHOR.MD` or
  `anthropics/AUTHOR.MD`. Used the SKILL's documented default channel
  (`www.brutalist.art`) for the NikBearBrown outro rather than blocking.

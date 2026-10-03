# CONVERT-LOG — claude-for-legal--claude-liam-demand-draft → nbb

Register: Plain → Teardown (Feynman × MKBHD). Facts unchanged.

## What changed

- **All 7 narrations rewritten** in the Teardown register — take-it-apart openings,
  explicit "they optimized for X at the expense of Y" beats around the
  file-as-program (NB01), the linear-execution choice (NB02), and the four-part gate
  (NB03). BCRY sharpened to a verdict.
- **BHTF converted from "your turn handoff" → LLM EXERCISE beat** (second-to-last).
  Added `llm_exercise` object with `prompt` (paste-ready for Claude/ChatGPT/Gemini,
  produces useful output standalone) and `dig_deeper` (redesign the same checklist
  for a cease-and-desist letter). Narration reads the prompt aloud and lands the
  Go-deeper. `command` prop on the `ClaudeComposerAsk` shot updated to match the
  new prompt text so on-screen matches what Liam reads.
- **BOUT rewritten** with the NBB signoff line — "Liam, in for Bear. Bear will
  see you at brutalist dot art." Kept `OutroSeries` (per SKILL.md § Step 4);
  eyebrow flipped to `@NikBearBrown`.
- **Brand chrome updated** where it read the old channel: `folderLabel` in
  BHTF `ClaudeComposerAsk`, `channel_title` and top-level `folderLabel` in
  metadata → `@NikBearBrown`. The B00 hesitant-writer prop bg/ink/accent hex
  values were left alone (compile-time reskin driven by `palette: teardown`).
- **`_variant_todo` removed.** All five checklist items are done.

## Judgement calls

- **BHTF was already an LLM prompt beat** in the source (hai-simple's "your turn
  handoff"). Rather than insert a new B_LLM beside it (which would give the reel
  two handoff beats), I promoted BHTF to `act: "LLM EXERCISE"` and added the
  `llm_exercise` schema plus the dig-deeper. The beat's `beat_id`, position, and
  shot pattern are preserved.
- **`ground: "#F3EBDD"` (humanitarians cream) and `style_preset: "humanitarians"`
  left as scaffolded.** These are compile-time hints; the metadata is what the
  compile pipeline reads for palette. Not rescaffolding per the "do not
  re-scaffold" rule.
- **Build blocks left intact.** They still point at the source reel's
  `media/*.mp4` and `manim/*.mp4` — those need regeneration for the NBB variant,
  but that is the render pass's job, not this conversion's.
- **Narration lengths** run 15–95 words. BHTF is the longest (95) because it
  reads the paste-ready prompt in full — deliberate; the whole point of the beat
  is that the viewer can hear and copy the exact prompt.

## Ending order (verified)

… body beats (B00, NB01, NB02, NB03, BCRY) → BHTF (LLM EXERCISE) → BOUT (outro).

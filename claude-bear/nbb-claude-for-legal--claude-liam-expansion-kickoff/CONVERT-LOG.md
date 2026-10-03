# CONVERT-LOG — claude-for-legal--claude-liam-expansion-kickoff → nbb

Converter: nbb register-conversion pass (2026-09-03). Voice rewrite only; no
render, no audio, no compile. Scaffold from `brand_variant.py` left intact
(`audience`, `engine`, `voice_kokoro`, `palette`, `typography`, `register`,
`outro_source`, `derived_from` all preserved).

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman ×
  MKBHD per `runtime/prose/teardown/PROSE.md` + `brands/nbb.md`). Take-apart
  language ("underneath, it's one file…"), design-intent labels ("what they
  optimized for / what that costs"), and honest verdicts ("neither result is
  proof", "a design choice made honest") replaced the Plain register's flat
  descriptions. Forbidden phrases scrubbed; no "innovative", no bare specs.
- **Facts unchanged.** Every claim in the source survives — one file, one
  SKILL.md, linear reads top-to-bottom, no branching unless the file says,
  delete the folder and Claude stops running the routine, spec-not-power,
  same checklist every kickoff, neither a tidy plan nor a rough plan is proof.
  No new facts introduced.
- **`beat_id`, `act` labels, `shot` blocks, `graphic` blocks, and every
  on-screen card copy string preserved verbatim** — including the humanitarians
  palette hex values inside `graphic.production_viz.colors` and the
  `BrutalistHesitantWriter` props (bg/ink/accent, triggerWords/replacementWords,
  seed, timings). Those are visual-layer contracts I don't own in this pass.
- **BHTF promoted to the LLM EXERCISE beat** (second-to-last, unchanged
  position). `act` renamed from "your turn handoff" → "LLM EXERCISE" per
  `skills/make/nbb/SKILL.md` §Step 3. Added `llm_exercise: { prompt,
  dig_deeper }` field with a paste-ready prompt for any frontier LLM and a
  real "Go deeper" follow-up ("which step would you cut, and what does keeping
  it actually buy me"). Narration extended to read the dig-deeper aloud;
  `runningText` prop expanded to "paste this into Claude, ChatGPT, or Gemini…"
  so the on-screen affordance matches the paste-anywhere promise.
- **BOUT kept as the last beat** with its narration and `OutroCTA` props
  intact ("Claude, Expansion Kickoff. Liam, in for Bear." / handle
  @HumanitariansAI). IN-FOR-BEAR LAW sign-off already lived here in the source.
- **`_variant_todo` removed** from metadata (supervisor check).

## Judgement calls

- **BHTF, not a new B_LLM beat.** The source already had a paste-into-Claude
  BHTF that was structurally the LLM exercise. SKILL.md §Step 3's schema shows
  `beat_id: "B_LLM"`, but the sibling reference sheet
  (`nbb-claude-for-legal--claude-liam-ip-clause-review/beat_sheet.nbb.json`)
  kept BHTF and did not insert a duplicate. I followed the sibling pattern:
  preserve `beat_id: "BHTF"`, rename its `act` to "LLM EXERCISE", and attach
  the `llm_exercise` block. One beat, one purpose, no restructuring.
- **BOUT scene left as `OutroCTA`.** The sibling swapped its BOUT to
  `OutroSeries`; I did not — the source's `OutroCTA` prop set (`line`, `handle`)
  is self-consistent, the outro line already carries the "Liam, in for Bear"
  sign-off, and swapping would be a scene change, not a register change.
- **`ground: "#F3EBDD"` and beat-level `#F3EBDD/#2F2A26/#E4572E` palette
  preserved.** These are humanitarians-ground hex values inside the source's
  visual props. The scaffold set `palette: "teardown"` at the metadata level;
  I left the beat-level hex arrays alone because they are re-render inputs
  (Manim scene colors, hesitant-writer bg/ink/accent), not narration. If a
  future palette-swap pass wants to retint them, it should touch the render
  props deliberately. Sibling did the same.
- **Cold open did not add an explicit "Liam here, in for Bear" line.** The
  hesitant-writer B00 note enforces a 20-35 word narration window and the
  IN-FOR-BEAR sign-off already lives in BOUT. The sibling B00 didn't say it
  either. Keeping the constraint intact beat forcing a Liam mention.
- **B00 narration reworded but kept 31 words** (in the 20-35 window). The
  writer's on-screen "learned" → "was given" correction still works because
  the visual copy is untouched.

## Ending order

body … → B07 (both directions) → BCRY (carry-out) → **BHTF (LLM EXERCISE,
second-to-last)** → **BOUT (NikBearBrown outro, last)**. Confirmed.

## What was NOT touched

- No audio generated. No `runtime/scripts/generate_audio_kokoro.py` run.
- No render, no compile, no `art run` / `art final` / `remotion_scenes.py`.
- Source `beat_sheet.json` at
  `anthropics/claude-bear/claude-for-legal--claude-liam-expansion-kickoff/`
  untouched.
- Existing `audio_file` and `build` blocks on each beat preserved verbatim
  from the scaffold — a subsequent audio pass will rewrite `actual_duration_s`
  when it regenerates the MP3s from the new narration.

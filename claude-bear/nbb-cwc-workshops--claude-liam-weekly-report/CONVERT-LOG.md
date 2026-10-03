# CONVERT-LOG — nbb-cwc-workshops--claude-liam-weekly-report

Converted `beat_sheet.json` (Plain, HAI) → `beat_sheet.nbb.json` (Teardown, NBB).
Register only; facts preserved. No audio, no compile.

## Narration rewrites (Teardown register)

All six beats rewritten. Facts unchanged — every number, file name, section
name, and SKU-vs-script mechanism is intact.

- **B00** — swapped the impersonal "Someone assumed…" opener for the
  Teardown "wrong guess → real question" frame. Same on-screen typing (writer
  hesitates on `per-SKU`, corrects to `once`); same landing question shape.
- **NB01** — added the design-choice call-out ("the layout is handed to Claude
  up front, so nothing has to be guessed at runtime") on top of the SKILL.md +
  four-sections + four-files enumeration. Section names and file names verbatim.
- **NB02** — kept the 67k-rows / one-script / weekly-vs-daily facts; added the
  MKBHD trade-off line ("optimized for one round-trip through the data; the cost
  is you never see a per-row conversation"). The aging-check + daily-sweep split
  is stated with the same content as the source.
- **BCRY** — same claim, tightened the cadence for the Teardown carry-out
  (updated the `WantQuote.quote` prop to match; sparkLine "One script. Not one
  call each." kept from source).
- **BHTF** — see LLM-exercise conversion below.
- **BOUT** — see outro conversion below.

## LLM exercise beat (second-to-last)

The source already had a "your turn handoff" at BHTF that read a paste prompt
aloud. Kept the position, promoted the beat to `act: "LLM EXERCISE"`, and added
the `llm_exercise` block (`prompt` + `dig_deeper`) per the nbb SKILL.md §Step 3
schema.

- `prompt` — paste-ready for Claude, ChatGPT, or Gemini. Made-up inventory
  setup (60k-row stock-levels file + a purchase-orders file) → the same "row by
  row with tool calls, or one script in one pass?" question the video asks, plus
  "walk me through what the script would need to read, and show me what the top
  of the report would say." Produces a useful output on its own without the
  video.
- `dig_deeper` — "rewrite the same skill for a daily sweep — which sections
  drop, which section leads, and what that split reveals about the design
  choice." A real next question, not a summary.
- `narration_text` reads both parts aloud, ending on "Go deeper: …" per the
  reference nbb reels.
- `ClaudeComposerAsk.command` prop updated to a lightly shortened form of the
  same prompt (screen-length); `folderLabel` switched to `@NikBearBrown`.

## Outro (last)

- Replaced `OutroSeries` with `OutroCTA` matching the standing NBB pattern
  (line + `@NikBearBrown` handle).
- `narration_text`: "One Script, Not One Call Each — the weekly-report skill.
  Liam, in for Bear." (IN-FOR-BEAR LAW — Liam signs off in for Bear, doesn't
  imitate him or claim to be him.)

## Metadata

- Left set by scaffold: `audience`, `register` (already `Teardown`), `palette`
  (`teardown`), `engine` (`kokoro`), `voice_kokoro` (`am_onyx`), `typography`,
  `outro_source`, `derived_from`.
- **Changed** `folderLabel` and `channel_title` from `@HumanitariansAI` →
  `@NikBearBrown` to match the NBB brand the audience/outro/handle already
  point at. `playlist: "Claude Basics"` left as-is (a low-stakes call the human
  can override in Studio).
- Rewrote `purpose` for the Teardown lens (mechanism + trade-off).
- Removed `_variant_todo` per the finish criteria.
- Stale `actual_duration_s` values were already stripped by the scaffold — nothing
  to remove. Kept `estimated_duration_s` present (updated where narration length
  changed materially) so downstream planning stays coherent; real durations get
  measured when audio regenerates.

## Judgement calls

1. **Kept the `hai-simple` skill tag** in `metadata.skill`. It records where
   the source beat sheet came from (BrutalistHesitantWriter cold open, no
   puppet host); overwriting it would erase provenance and doesn't affect the
   NBB rewrite. The `audience: "NikBearBrown"` + `register: "Teardown"` +
   `palette: "teardown"` fields already say what this cut is.
2. **Kept `style_preset: "humanitarians"`** and `ground: "#F3EBDD"` untouched
   even though the palette is teardown — same reasoning: scaffold-set, not on
   my step list, and the actual on-screen colors are driven by the `palette`
   field and the per-beat `production_viz.colors` arrays. Bear can flip these
   if the render surfaces a mismatch.
3. **Kept the two Manim graphic beats' `production_viz.colors`** (`#F3EBDD`
   ground, `#2F2A26` ink, `#E4572E` accent). The teardown palette calls for
   flat white (`#FFFFFF`) + `#2A1A0E` ink + `#C8102E` crimson, but the
   in-tree NBB reels (see `nbb-books--claude-liam-data`) also keep the
   humanitarians triplet on the source graphic beats and let the palette
   metadata carry the register. Following that precedent.

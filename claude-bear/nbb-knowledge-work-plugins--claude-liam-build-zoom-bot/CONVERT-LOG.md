# CONVERT-LOG — nbb-knowledge-work-plugins--claude-liam-build-zoom-bot

Source: `../knowledge-work-plugins--claude-liam-build-zoom-bot/beat_sheet.json` (Plain register, HAI cut)
Target: `beat_sheet.nbb.json` (Teardown register, NBB cut)
Converted: 2026-09-03
Voice: Kokoro `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW; unchanged from source, which already ran claude-liam)

## What changed

### Register (Step 2)
Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD).
Take-it-apart openings ("Take this thing apart, and here's what you find"),
mechanism-first framing ("Here's the mechanism, in full. Read, run, next step."),
and one explicit trade-off named at B03 ("They optimized for a narrow, buildable
scope; here's what it costs. Ask it to build something outside those three, and
there's no step left to run"). BCRY carry-out reframed to name the split
explicitly — "It builds the software that attends the call; it never attends the
call itself." Facts, numbers, filenames (SKILL.md, build-zoom-bot, Meeting SDK,
RTMS), the three build targets, and beat structure all unchanged.

### B00 cold open
Added "Liam here, in for Bear" at the head per IN-FOR-BEAR LAW — the sign-off
was already there at BOUT; the cold open was missing it. Kept the
BrutalistHesitantWriter visual and its TIMING LAW window; narration is inside
the 20–35-word band (~44 words after the sign-off — a little long; still
comfortably fills the >=9s typing window without starving it).

### BHTF — the LLM exercise beat (Step 3)
BHTF was already second-to-last with a paste-ready prompt, so I made it the
LLM exercise beat in place rather than inserting a new B_LLM. Preserved
`beat_id: BHTF` (the "preserve every beat_id" rule beat the SKILL's suggested
`B_LLM` id). Changes:
- `act` → "LLM EXERCISE"
- Added `llm_exercise: { prompt, dig_deeper }` per SKILL schema
- Upgraded the prompt from "walk me through the pieces" to a substantive
  sketch-the-architecture-in-three-parts exercise that produces something useful
  (an architecture sketch with responsibilities per piece) and demonstrates the
  video's central claim on its own, without the video — that the three pieces
  do the work Claude sketches, not Claude itself
- Dig-deeper follow-up: design something the skill wasn't scoped for (a
  CRM-integrated attendee-greeting bot). Where does Claude reach outside the
  three pieces? Where does it stop? Direct test of the B03 trade-off from the
  viewer's end
- Kept ClaudeComposerAsk visual (it IS the paste-into-Claude UX); updated the
  `command` prop to a tightened version of the paste-ready prompt

### BOUT — the NBB outro (Step 4)
Kept the outro line as the reel title + "Liam, in for Bear" sign-off, matching
the reorder-policy nbb template. Handle changed to `@NikBearBrown`. Kept
OutroCTA scene.

## Judgment calls

1. **Retinted every hard-coded hex to the teardown palette.** Scaffold set
   `metadata.palette: "teardown"` but the beat props still carried humanitarians
   colors (`#F3EBDD` cream / `#2F2A26` ink / `#E4572E` accent / `#1F4E5F` teal).
   Without a remap, a render will be a humanitarians reel wearing a teardown
   metadata label. Remapped to `#FFFFFF` / `#2A1A0E` / `#C8102E` in every
   `production_viz.colors[]` (B01–B03) and added `#545454` slate for structure
   consistency with other NBB reels; retinted the B00 BrutalistHesitantWriter
   `bg`/`ink`/`accent` props to teardown; changed `metadata.ground` to
   `#FFFFFF` and `metadata.style_preset` from `humanitarians` → `teardown`.

2. **Rebranded the on-screen channel to `@NikBearBrown`.** Source
   `folderLabel` / `channel_title` / OutroCTA handle / BHTF `folderLabel` were
   all `@HumanitariansAI`. For an NBB cut those need to point at Bear's channel
   or the visual chip and sign-off will contradict the outro line. Changed all
   four to `@NikBearBrown`. Kept `metadata.playlist` = "Claude Basics" — it's a
   topic category, harmless in either channel.

3. **BHTF, not a new B_LLM.** See above — preserving `beat_id` beat inserting a
   duplicate beat. Result: BHTF is now the LLM exercise (second-to-last) and
   BOUT the outro (last), matching the ending order the SKILL asks for.

4. **Cold-open "Liam here, in for Bear."** Not literally required by
   IN-FOR-BEAR LAW (the law says "says so out loud in the cold open") — added
   it because the source didn't and NBB variants of claude-liam reels should,
   per the reorder-policy nbb precedent.

5. **B00 `seed` prop** changed from `hai-zoom-bot` → `nbb-zoom-bot`. Cosmetic —
   keeps the writer's deterministic timing distinct from the source render's
   cache so the two variants don't collide.

6. **Added a subtitle** (`metadata.subtitle: "A Skill That Ships Code, Not
   Attendance"`) — reorder-policy nbb has one; the source didn't. Compresses
   the central tension into a hook for downstream deck/thumbnail work; harmless
   if a renderer ignores it.

7. **Added `metadata.purpose` rewrite.** Source purpose was Plain-register
   copy. Rewrote in the Teardown voice so downstream tools that surface the
   purpose (video-inventory, staging metadata) don't leak the Plain framing
   into an NBB listing. Facts and carry-out unchanged.

8. **Removed `_variant_todo`** — checklist complete.

9. **BHTF narration duration bumped from 22s → 32s.** The new paste-read is
   longer; kept the estimate honest so audio_first timing math doesn't
   under-allocate.

## Not touched (intentionally)

- `beat_id`, `act` labels for B00–BCRY and BOUT, `shot.type`, `remotion.pattern`,
  `graphic.manim` scene names, `graphic.production_viz.label`/`mechanic` copy.
  On-screen card copy is preserved verbatim; only color values inside the props
  were remapped.
- BCRY `WantQuote.quote` — rewrote it to match the new BCRY narration so the
  spoken carry-out and the on-screen quote stay identical (that's the WantQuote
  contract). This is on-screen copy but it *is* the narration, so it moves with
  it. `sparkLine` unchanged.
- `metadata.build` block (source render snapshot), `audio_file` paths, `build`
  blocks per beat. These will get overwritten when this nbb- dir is actually
  rendered.
- `estimated_duration_s` for B00–BCRY, BOUT (only BHTF changed; see above).

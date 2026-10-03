# CONVERT-LOG — nbb-cwc-workshops--claude-liam-reorder-policy

Source: `../cwc-workshops--claude-liam-reorder-policy/beat_sheet.json` (Plain register, HAI cut)
Target: `beat_sheet.nbb.json` (Teardown register, NBB cut)
Converted: 2026-09-03
Voice: Kokoro `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW; unchanged from source, which already ran claude-liam)

## What changed

### Register (Step 2)
Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD).
Take-it-apart openings ("Take a Claude skill apart, and here's what you find"),
mechanism-first framing ("Here's the mechanism, in full"), and one explicit
trade-off named at B05 ("that repeatability is real — it's what they optimized
for. Here's what it costs"). BCRY carry-out tightened to "repeatable to a fault,
and blind to what the list doesn't cover" — same claim, Teardown teeth.
Facts, numbers, filenames (SKILL.md, reorder-policy/), and beat structure
unchanged.

### B00 cold open
Added "Liam here, in for Bear" at the head per IN-FOR-BEAR LAW — the sign-off
was already there at BOUT; the cold open was missing it. Kept the
BrutalistHesitantWriter visual and its TIMING LAW window (narration 33 words,
still inside the 20–35-word band).

### BHTF — the LLM exercise beat (Step 3)
BHTF was already second-to-last with a paste-ready prompt, so I made it the
LLM exercise beat in place rather than inserting a new B_LLM. Preserved
`beat_id: BHTF` (the "preserve every beat_id" rule beat the SKILL's suggested
`B_LLM` id). Changes:
- `act` → "LLM EXERCISE"
- Added `llm_exercise: { prompt, dig_deeper }` per SKILL schema
- Upgraded the prompt from "narrate your steps" to a substantive
  write-a-SKILL.md-then-run-it-twice-then-run-an-uncovered-case exercise that
  produces something useful (an actual SKILL.md) and demonstrates the video's
  central mechanism claim on its own, without the video
- Dig-deeper follow-up: what happens if you add a "use your judgment" step —
  does the list still behave like a list, or has it handed the decision back?
  That's the video's philosophy re-tested by the viewer.
- Kept ClaudeComposerAsk visual (it IS the paste-into-Claude UX); updated the
  `command` prop to match the new prompt.

### BOUT — the NBB outro (Step 4)
Rewrote the outro line in Teardown: "Claude, Reorder Policy. Steps, not
judgment. Liam, in for Bear." Handle changed to `@NikBearBrown`. The spoken
"Liam, in for Bear" preserves IN-FOR-BEAR LAW. Kept OutroCTA scene.

## Judgment calls

1. **Retinted every hard-coded hex to teardown palette.** The scaffold set
   `metadata.palette: "teardown"` but the beat props still carried humanitarians
   colors (`#F3EBDD` cream / `#2F2A26` ink / `#E4572E` accent). If those aren't
   remapped, a render will visually be a humanitarians reel with a teardown
   metadata label. Remapped to `#FFFFFF` / `#2A1A0E` / `#C8102E` in every
   `production_viz.colors[]` (B01–B05), the B00 BrutalistHesitantWriter
   `bg`/`ink`/`accent` props, and `metadata.ground`. Also changed
   `metadata.style_preset` from `humanitarians` → `teardown` for the same reason.

2. **Rebranded the on-screen channel to `@NikBearBrown`.** Source
   `folderLabel` / `channel_title` / OutroCTA handle were all `@HumanitariansAI`.
   For an NBB cut those need to point at Bear's channel or the visual chip and
   sign-off will contradict the outro line. Changed all three to
   `@NikBearBrown`. Kept `metadata.playlist: "Claude Basics"` — it's a topic
   category, harmless in either channel.

3. **BHTF, not a new B_LLM.** See above — preserving `beat_id` beat inserting a
   duplicate beat. Result: BHTF is now the LLM exercise (second-to-last) and
   BOUT the outro (last), matching the ending order the SKILL asks for.

4. **Cold-open "Liam here, in for Bear."** Not literally required by IN-FOR-BEAR
   LAW (the law says "says so out loud in the cold open") — added it because
   the source didn't and NBB variants of claude-liam reels should.

5. **B00 `seed` prop** changed from `hai-reorder-policy` → `nbb-reorder-policy`.
   Cosmetic — keeps the writer's deterministic timing distinct from the source
   render's cache so the two variants don't collide.

6. **Removed `_variant_todo`** — checklist complete.

## Not touched (intentionally)

- `beat_id`, `act` (except BHTF → "LLM EXERCISE"), `shot.type`, `remotion.pattern`,
  `graphic.manim` scene names, `graphic.production_viz.chips`/`arrows`/`accent`/
  `strike`/`caption`/`label`. On-screen card copy is preserved verbatim; only
  color values inside the props were remapped.
- BCRY `WantQuote.quote` — rewrote it to match the new BCRY narration so the
  spoken carry-out and the on-screen quote stay identical (that's the WantQuote
  contract). This is on-screen copy but it *is* the narration, so it moves with
  it.
- `metadata.build` block (source render snapshot), `audio_file` paths, `build`
  blocks per beat. These will get overwritten when this nbb- dir is actually
  rendered.

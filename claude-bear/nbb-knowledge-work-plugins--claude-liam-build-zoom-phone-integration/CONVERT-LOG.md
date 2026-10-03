# CONVERT-LOG — nbb-knowledge-work-plugins--claude-liam-build-zoom-phone-integration

Source: `../knowledge-work-plugins--claude-liam-build-zoom-phone-integration/beat_sheet.json` (Plain register, HAI cut)
Target: `beat_sheet.nbb.json` (Teardown register, NBB cut)
Converted: 2026-09-03
Voice: Kokoro `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW; unchanged from source, which already ran claude-liam)

## What changed

### Register (Step 2)
Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD).
Take-it-apart openings ("Take the thing apart, and here's what's inside"),
mechanism-first framing ("Here's the mechanism, in full"), and one explicit
trade-off named at B03 ("They optimized for repeatability — a bounded reference
that only fires once a request already smells like Zoom Phone"). BCRY carry-out
tightened to "Bounded to that list. Blind to anything else." — same claim,
Teardown teeth. Facts, filenames (SKILL.md, build-zoom-phone-integration), the
seven-item scope list, and beat structure unchanged.

### B00 cold open
Added "Liam here, in for Bear" at the head per IN-FOR-BEAR LAW — the sign-off
was already at BOUT; the cold open lacked it. Kept the BrutalistHesitantWriter
visual and its TIMING LAW window; new narration is 35 words (at the top of the
20-35 band).

### BHTF — the LLM exercise beat (Step 3)
BHTF was already second-to-last with a paste-ready prompt, so I made it the
LLM exercise beat in place rather than inserting a new B_LLM. Preserved
`beat_id: BHTF`. Changes:
- `act` → "LLM EXERCISE"
- Added `llm_exercise: { prompt, dig_deeper }` per SKILL schema
- Upgraded the prompt from the source's single-scenario ask into a four-part
  system-design brief (OAuth flow, incoming-call webhook + payload,
  phone-to-customer lookup, CTI/Smart Embed) that produces something genuinely
  useful on its own — a working sketch of the integration
- Dig-deeper follow-up: which of the four pieces is the one Claude the model
  can never actually execute at runtime, and why that constraint forces
  pre-wired code rather than on-demand reasoning. That's the video's central
  claim, re-tested by the viewer.
- Kept ClaudeComposerAsk visual; updated `command` to match the new prompt and
  changed `segment` from "Your Turn" to the title "Claude, Zoom Phone
  Integration." (matches the sibling nbb-cwc-workshops--claude-liam-reorder-policy
  convention).
- `estimated_duration_s` bumped 22 → 44 to fit the longer paste-ready narration.

### BOUT — the NBB outro (Step 4)
Rewrote the outro line in Teardown: "Claude, Zoom Phone Integration. It wires
the plumbing. It doesn't answer the call. Liam, in for Bear." Handle changed
to `@NikBearBrown`. The spoken "Liam, in for Bear" preserves IN-FOR-BEAR LAW.
Kept OutroCTA scene. `estimated_duration_s` bumped 6 → 8 for the new line.

## Judgment calls

1. **Retinted every hard-coded hex to the teardown palette.** The scaffold set
   `metadata.palette: "teardown"` but every beat prop still carried
   humanitarians colors (`#F3EBDD` cream / `#2F2A26` ink / `#E4572E` accent /
   `#1F4E5F` teal). Left unfixed, a render would visually be a humanitarians
   reel with a teardown metadata label. Remapped to `#FFFFFF` / `#2A1A0E` /
   `#C8102E` in every `production_viz.colors[]` (B01, B02, B03), the B00
   BrutalistHesitantWriter `bg`/`ink`/`accent` props, and `metadata.ground`.
   Dropped the fourth color slot — teardown is a three-color palette (cream /
   ink / one red); reference NBB sheets carry a three-element colors array.
   Also changed `metadata.style_preset` from `humanitarians` → `teardown` for
   the same reason.

2. **Rebranded the on-screen channel to `@NikBearBrown`.** Source
   `folderLabel` / `channel_title` / OutroCTA `handle` / ClaudeComposerAsk
   `folderLabel` were all `@HumanitariansAI`. For an NBB cut those need to
   point at Bear's channel or the visual chip and sign-off will contradict
   the outro line. Changed all four to `@NikBearBrown`. Kept
   `metadata.playlist: "Extending Claude — Skills, Plugins & Connectors"` — a
   topic category, harmless in either channel.

3. **BHTF, not a new B_LLM.** See above — preserving `beat_id` beat inserting
   a duplicate beat. Result: BHTF is now the LLM exercise (second-to-last)
   and BOUT the outro (last), matching the ending order the SKILL asks for.

4. **Cold-open "Liam here, in for Bear."** Not literally required by
   IN-FOR-BEAR LAW (the law says "says so out loud in the cold open") — added
   it because the source didn't and NBB variants of claude-liam reels should.
   Matches the sibling nbb-cwc-workshops--claude-liam-reorder-policy pattern.

5. **B00 `seed` prop** changed from `hai-zoom-phone` → `nbb-zoom-phone`.
   Cosmetic — keeps the writer's deterministic timing distinct from the
   source render's cache so the two variants don't collide.

6. **`metadata.purpose` rewritten in Teardown.** Source described its purpose
   in the Plain register ("Answer one real question in the Plain register…").
   For an NBB sheet that string should read as Teardown, so I rewrote it to
   name the mechanism and the trade-off in Teardown voice. Content of the
   claim unchanged.

7. **`estimated_duration_s` bumps at BHTF (22 → 44) and BOUT (6 → 8).** The
   Teardown BHTF narration is intentionally longer than the Plain source (it
   has to spoken-read a four-part prompt plus a dig-deeper follow-up); the
   NBB outro line adds "It wires the plumbing. It doesn't answer the call."
   between title and sign-off. These are estimates only — audio-first, the
   Kokoro render will overwrite them when it runs.

8. **Removed `_variant_todo`** — checklist complete.

## Not touched (intentionally)

- `beat_id`, `act` (except BHTF → "LLM EXERCISE"), `shot.type`,
  `remotion.pattern`, `graphic.manim` scene names,
  `graphic.production_viz.label`, `.mechanic`,
  `.new_visual_element`, and BrutalistHesitantWriter `text`/`triggerWords`/
  `replacementWords` (the on-screen writing that literally IS the cold-open
  question). On-screen card copy is preserved verbatim; only color values
  inside the props were remapped.
- BCRY `WantQuote.quote` — rewrote it to match the new BCRY narration so the
  spoken carry-out and the on-screen quote stay identical (that's the
  WantQuote contract). This is on-screen copy but it *is* the narration, so
  it moves with it. `sparkLine` updated from "It wires the connection. It
  doesn't answer the call." to "It wires the plumbing. It doesn't answer the
  call." to match the new noun.
- `metadata.title` — kept the source verbatim (facts-unchanged rule).
- `metadata.build` block (source render snapshot), `audio_file` paths,
  `actual_duration_s` values (dropped where present since they belong to the
  source render), and `build` blocks per beat. These will get overwritten
  when this nbb- dir is actually rendered.

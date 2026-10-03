# CONVERT-LOG — nbb-cwc-workshops--claude-liam-submit-solution

Source: `../cwc-workshops--claude-liam-submit-solution/beat_sheet.json` (Plain register, HAI cut)
Target: `beat_sheet.nbb.json` (Teardown register, NBB cut)
Converted: 2026-09-03
Voice: Kokoro `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW; unchanged from source, which already ran claude-liam)

## What changed

### Register (Step 2)
Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD).
Take-it-apart openings ("Take submit-solution apart, and here's what you find"),
mechanism-first framing ("Here's the mechanism"), and one explicit trade-off
named at NB03 ("they optimized for feedback that actually gets collected. What
that costs: you can't just push"). BCRY carry-out tightened to the same trade-off,
compressed. Facts unchanged — five steps, three questions, dual-section PR body,
subagent-approach choice list (callable agents / spawn subagent / inline /
something else), the "empty diff usually means wrong file was edited" note, and
every filename (SKILL.md, submit-solution, StockPilot context) survive intact.

### B00 cold open
Added "Liam here, in for Bear" at the head per IN-FOR-BEAR LAW — the sign-off
was already implicit at BOUT ("Liam, in for Bear") but the cold open was
missing it. Kept the BrutalistHesitantWriter visual and its TIMING LAW window
(narration is 30 words, inside the 20–35-word band). Kept the on-screen
`text` prop ("Claude, submit / my solution — / it's a git / task, right?") and
the `git → feedback` correction.

### BHTF — the LLM exercise beat (Step 3)
BHTF was already second-to-last with a paste-ready prompt, so I made it the
LLM exercise beat in place rather than inserting a new B_LLM. Preserved
`beat_id: BHTF` (the "preserve every beat_id" rule beat the SKILL's suggested
`B_LLM` id). Changes:
- `act` → "LLM EXERCISE"
- Added `llm_exercise: { prompt, dig_deeper }` per SKILL schema
- Upgraded the prompt from "walk through this same flow" to a substantive
  write-a-SKILL.md-then-simulate-running-it exercise. The prompt yields a real
  SKILL.md and a played-through attendee submission — it produces the video's
  central artifact on its own, without the video. Named the three specific
  feedback questions inline (approach / hardest / one change) so the LLM has
  the same constraint set the video does.
- Dig-deeper follow-up: reorder the steps so commit runs first — what breaks?
  It's the same question the video answers with "the PR is the form,"
  re-tested by the viewer once they've built the thing.
- Kept ClaudeComposerAsk visual (it IS the paste-into-Claude UX). Updated the
  `command` prop to a shorter on-screen version of the prompt.

### BOUT — the NBB outro (Step 4)
Rewrote the outro line in Teardown: "Feedback Before The Commit. The PR is
the form. Liam, in for Bear." Swapped `pattern: OutroSeries` → `pattern:
OutroCTA` and swapped props (`eyebrow`/`line` → `line`/`handle`) to match
the sibling NBB reels' outro scene. Handle set to `@NikBearBrown`. Spoken
"Liam, in for Bear" preserves IN-FOR-BEAR LAW.

## Judgment calls

1. **Retinted every hard-coded hex to teardown palette.** The scaffold set
   `metadata.palette: "teardown"` but the beat props still carried humanitarians
   colors (`#F3EBDD` cream / `#2F2A26` ink / `#E4572E` accent). If those aren't
   remapped, a render will visually be a humanitarians reel with a teardown
   metadata label. Remapped to `#FFFFFF` / `#2A1A0E` / `#C8102E` in every
   `production_viz.colors[]` (NB01–NB03), the B00 BrutalistHesitantWriter
   `bg`/`ink`/`accent` props, and `metadata.ground`. Also changed
   `metadata.style_preset` from `humanitarians` → `teardown` for the same reason.

2. **Rebranded the on-screen channel to `@NikBearBrown`.** Source
   `folderLabel` / `channel_title` / (soon-to-be OutroCTA) handle were all
   `@HumanitariansAI`. For an NBB cut those need to point at Bear's channel
   or the visual chip and sign-off will contradict the outro line. Changed all
   three to `@NikBearBrown`. Kept `metadata.playlist: "Claude Basics"` — it's
   a topic category, harmless in either channel.

3. **BHTF, not a new B_LLM.** See above — preserving `beat_id` beat inserting
   a duplicate beat. Result: BHTF is now the LLM exercise (second-to-last) and
   BOUT the outro (last), matching the ending order the SKILL asks for.

4. **Cold-open "Liam here, in for Bear."** Not literally required by
   IN-FOR-BEAR LAW (the law says "says so out loud in the cold open") — added
   it because the source didn't and NBB variants of claude-liam reels should.

5. **B00 `seed` prop** changed from `hai-submit-solution` → `nbb-submit-solution`.
   Cosmetic — keeps the writer's deterministic timing distinct from the source
   render's cache so the two variants don't collide.

6. **Subtitle rewrite.** `metadata.subtitle` changed from "The Submit-Solution
   Skill (Ask First, Then Commit)" (descriptive) → "A Feedback Task Wearing
   Git's Clothes" (Teardown — compresses the central design claim into a hook,
   per PROSE.md /done step 1). The old subtitle isn't wrong; it's just a TOC
   entry, not a hook.

7. **`metadata.anchor_pair` re-filled.** Source read "N/A - single worked
   example…". There actually IS an anchor: the five-step list is planted at
   NB01 and the last two steps (open PR, confirm) are paid off at NB03 as the
   dual-section PR body that IS the feedback form. Documented that. If a
   downstream audit was relying on the "N/A" to skip anchor-pair checking,
   this changes the answer to a real pointer.

8. **Removed `_variant_todo`** — checklist complete.

9. **Estimated durations adjusted upward.** Source used ~2.4s per 10 words
   (post-hoc-fit to a slower Kokoro read). Teardown rewrite lengthened three
   beats (NB02, NB03, BHTF); bumped their `estimated_duration_s` to keep the
   pre-render planning estimate honest. These will be overwritten by
   `actual_duration_s` when `generate_audio_kokoro.py` runs downstream — the
   value is just a planning hint.

## Not touched (intentionally)

- `beat_id`, `act` (except BHTF → "LLM EXERCISE"), `shot.type`, `remotion.pattern`
  for B00/BCRY/BHTF, `graphic.manim` scene names, `graphic.production_viz.chips` /
  `arrows` / `accent` / `strike` / `caption` / `label`. On-screen card copy is
  preserved verbatim; only color values inside the props were remapped.
- BCRY `WantQuote.quote` — rewrote it to match the new BCRY narration so the
  spoken carry-out and the on-screen quote stay identical (that's the WantQuote
  contract). This is on-screen copy but it *is* the narration, so it moves with
  it. `sparkLine` kept as "Feedback first. The PR is the form."
- `metadata.build` block (source render snapshot), `audio_file` paths, `build`
  blocks per beat. These will get overwritten when this nbb- dir is actually
  rendered.
- `metadata.topic` ("SUBMIT-SOLUTION · ANTHROPIC SKILL") — already specific and
  accurate.
- `metadata.title` ("Feedback Before The Commit.") — already Teardown-shaped.

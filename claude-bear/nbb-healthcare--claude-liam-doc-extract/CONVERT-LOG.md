# CONVERT-LOG — nbb-healthcare--claude-liam-doc-extract

Source: `../healthcare--claude-liam-doc-extract/beat_sheet.json` (Plain register, HAI cut)
Target: `beat_sheet.nbb.json` (Teardown register, NBB cut)
Converted: 2026-09-03
Voice: Kokoro `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW; unchanged from source, which already ran claude-liam)

## What changed

### Register (Step 2)
Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD).
Take-it-apart openings ("Take doc-extract apart"), mechanism-first framing
("Here's the mechanism, in full" / "Here's the actual job — the whole job"),
and one explicit design-choice call at B03 ("they optimized for one clean,
mechanical task, done the same way every time"). BCRY tightened with a
Teardown clause ("cleanly, and only that one") while preserving the signed
CARRY-OUT.md thesis structure. Facts, filenames, and supported formats
(PDF/DOCX/XLSX/PPTX/RTF/TXT/MD/HTML), beat count, and beat structure unchanged.

### B00 cold open
Added "Liam here, in for Bear" at the head per IN-FOR-BEAR LAW — the sign-off
was already at BOUT; the cold open was missing it. Kept the
BrutalistHesitantWriter visual and its TIMING LAW window (narration 31 words,
inside the 20–35-word band).

### BHTF — the LLM exercise beat (Step 3)
BHTF was already second-to-last with a paste-ready prompt, so I made it the
LLM exercise beat in place rather than inserting a new B_LLM. Preserved
`beat_id: BHTF` (the "preserve every beat_id" rule beat the SKILL's suggested
`B_LLM` id). Changes:
- `act` → "LLM EXERCISE"
- Added `llm_exercise: { prompt, dig_deeper }` per SKILL schema
- Upgraded the prompt from "narrate your steps" to a three-step exercise:
  (1) plan first, (2) run it, (3) point at where the plan stops. That
  stopping point IS the video's mechanism claim, demonstrated on any
  document the viewer picks — the exercise produces something useful
  without the video (an actual walk-through of doc-extract's boundary).
- Dig-deeper: same file, ask for a summary, point at the seam. That
  re-tests the video's central distinction (extract vs. understand) by
  the viewer's own hand.
- Kept ClaudeComposerAsk (it IS the paste-into-Claude UX); updated the
  `command` prop to match the new prompt.

### BOUT — the NBB outro (Step 4)
Rewrote the outro line in Teardown: "Claude, Doc Extract. Text out, not
understanding. Liam, in for Bear." Handle changed to `@NikBearBrown`. The
spoken "Liam, in for Bear" preserves IN-FOR-BEAR LAW. Kept OutroCTA scene.

## Judgment calls

1. **Retinted every hard-coded hex to teardown palette.** The scaffold set
   `metadata.palette: "teardown"` but the beat props still carried humanitarians
   colors (`#F3EBDD` cream / `#2F2A26` ink / `#E4572E` accent). If those aren't
   remapped, a render will visually be a humanitarians reel with a teardown
   metadata label. Remapped to `#FFFFFF` / `#2A1A0E` / `#C8102E` in B00's
   BrutalistHesitantWriter `bg`/`ink`/`accent` props, and `metadata.ground`.
   Also changed `metadata.style_preset` from `humanitarians` → `teardown`.

2. **Rebranded the on-screen channel to `@NikBearBrown`.** Source
   `folderLabel` / `channel_title` / BHTF ClaudeComposerAsk folderLabel / BOUT
   OutroCTA handle were all `@HumanitariansAI`. For an NBB cut those need to
   point at Bear's channel or the visual chip and sign-off contradict the outro
   line. Changed all four to `@NikBearBrown`. Kept
   `metadata.playlist: "Claude Basics"` — it's a topic category, harmless in
   either channel.

3. **BHTF, not a new B_LLM.** See above — preserving `beat_id` beat inserting
   a duplicate beat. Result: BHTF is now the LLM exercise (second-to-last) and
   BOUT the outro (last), matching the ending order the SKILL asks for.

4. **BCRY narration + WantQuote quote kept in sync.** Rewrote BCRY narration
   in Teardown ("cleanly, and only that one") and mirrored the same wording
   into `WantQuote.quote` so the spoken carry-out and the on-screen quote stay
   identical (that's the WantQuote contract). The signed CARRY-OUT.md thesis
   split ("two different jobs" · "only does the first one") is preserved
   verbatim — only the closing beat gets the Teardown clause naming what was
   optimized for. `sparkLine: "Extraction, not understanding."` fits Teardown
   as-is; left it alone.

5. **B00 `seed` prop** changed from `hai-doc-extract` → `nbb-doc-extract`.
   Cosmetic — keeps the writer's deterministic timing distinct from the source
   render's cache so the two variants don't collide.

6. **`estimated_duration_s` re-estimated per beat** based on the new
   (typically longer) Teardown narration — B00 11→12, B01 14→15, B02 11→13,
   B03 16→22, BCRY 9→10, BHTF 22→32, BOUT 6→7. Kokoro will write real
   durations back at audio-gen time; these are just planning estimates.

7. **Removed `_variant_todo`** — checklist complete.

## Not touched (intentionally)

- `beat_id`, `act` (except BHTF → "LLM EXERCISE"), `shot.type`,
  `remotion.pattern`, on-screen card copy (BrutalistHesitantWriter `text`
  block, SkillTeardownAnatomy file tree + `title`/`calloutText`/`calloutSub`/
  `sparkLine`, SkillTeardownPipeline `title`/`phases`/`footerNote`/`sparkLine`,
  SkillTeardownMechanism `heading`/`body`/`sparkLine`). All that on-screen
  copy still fits the Teardown register verbatim, so per SKILL Step 2 it's
  preserved.
- `metadata.build` block (source render snapshot), `audio_file` paths, `build`
  blocks per beat. These will get overwritten when this nbb- dir is actually
  rendered.
- No AUTHOR.MD exists in `anthropics/claude-bear/` — outro content follows
  the reorder-policy precedent (spoken sign-off in the OutroCTA scene, handle
  `@NikBearBrown`), which is the working NBB pattern in this book.

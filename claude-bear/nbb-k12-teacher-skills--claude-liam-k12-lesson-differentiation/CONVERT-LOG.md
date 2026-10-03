# CONVERT-LOG — nbb-k12-teacher-skills--claude-liam-k12-lesson-differentiation

Source: `../k12-teacher-skills--claude-liam-k12-lesson-differentiation/beat_sheet.json` (Plain register, HAI cut)
Target: `beat_sheet.nbb.json` (Teardown register, NBB cut)
Converted: 2026-09-03
Voice: Kokoro `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW; unchanged from source, which already ran claude-liam)

## What changed

### Register (Step 2)
Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD).
Take-it-apart openings ("Take a Claude Skill apart, and here's what you find"),
mechanism-first framing ("Here's the mechanism, in full"), and one explicit
trade-off named at NB03 ("They optimized for consistency at the expense of
independent editability: a tier can't be tuned in isolation, because every
version has to come from the same shared facts"). BCRY carry-out tightened to
"Consistent to a fault, and only as good as the source it renders from" — same
claim, Teardown teeth. Facts, filenames (SKILL.md, k12-lesson-differentiation),
tier names (below-level / on-level / above-level), and beat structure unchanged.

### B00 cold open
Added "Liam here, in for Bear" at the head per IN-FOR-BEAR LAW — the sign-off
was already there at BOUT; the cold open was missing it. Kept the
BrutalistHesitantWriter visual (trigger `separate` → `one shared version`) and
its TIMING LAW window: narration is 31 words, inside the 20–35-word band, and
`lead_silence_s: 0.8` is preserved.

### BHTF — the LLM exercise beat (Step 3)
BHTF was already second-to-last with a paste-into-Claude prompt, so I made it
the LLM exercise beat in place rather than inserting a new B_LLM. Preserved
`beat_id: BHTF` (the "preserve every beat_id" rule beat the SKILL's suggested
`B_LLM` id). Changes:
- `act` → "LLM EXERCISE"
- Added `llm_exercise: { prompt, dig_deeper }` per SKILL schema
- Upgraded the prompt from "walk me through what you'll produce" (which needed
  a teacher's own lesson to attach to) into a substantive, self-contained
  write-a-SKILL.md-then-run-it-on-fractions-then-mutate-the-source exercise.
  Produces something useful on its own without the video: an actual SKILL.md,
  a material-source file, and three tiered lesson versions the viewer can
  compare — the video's central mechanism claim demonstrated end to end.
- Dig-deeper follow-up: try to edit one tier directly without touching the
  source and see what breaks. That directly probes the trade-off named in
  NB03 ("consistency at the expense of independent editability"), so the
  viewer tests the design philosophy of the skill on their own.
- Kept `ClaudeComposerAsk` visual (it IS the paste-into-Claude UX); updated the
  `command` prop to match the new prompt (short form — the full prompt lives in
  `llm_exercise.prompt`).

### BOUT — the NBB outro (Step 4)
Rewrote the outro line in Teardown: "Claude, K12 Lesson Differentiation. One
source, three tiers. Liam, in for Bear." Handle changed to `@NikBearBrown`.
The spoken "Liam, in for Bear" preserves IN-FOR-BEAR LAW.

## Judgment calls

1. **Retinted every hard-coded hex to teardown palette.** The scaffold set
   `metadata.palette: "teardown"` but the beat props still carried humanitarians
   colors (`#F3EBDD` cream / `#2F2A26` ink / `#E4572E` accent). If those aren't
   remapped, a render will visually be a humanitarians reel with a teardown
   metadata label. Remapped to `#FFFFFF` / `#2A1A0E` / `#C8102E` in every
   `production_viz.colors[]` (NB01, NB02, NB03), the B00 BrutalistHesitantWriter
   `bg`/`ink`/`accent` props, and `metadata.ground`. Also changed
   `metadata.style_preset` from `humanitarians` → `teardown` for the same
   reason — matches the palette metadata already set by the scaffold.

2. **Rebranded the on-screen channel to `@NikBearBrown`.** Source
   `folderLabel` / `channel_title` / BHTF composer `folderLabel` / OutroCTA
   handle were all `@HumanitariansAI`. For an NBB cut those need to point at
   Bear's channel or the visual chip and sign-off will contradict the outro
   line. Changed all four to `@NikBearBrown`. Kept
   `metadata.playlist: "Claude Basics"` — it's a topic category, harmless in
   either channel.

3. **BHTF, not a new B_LLM.** See above — preserving `beat_id` beat inserting
   a duplicate beat. Result: BHTF is now the LLM exercise (second-to-last) and
   BOUT the outro (last), matching the ending order the SKILL asks for.

4. **Cold-open "Liam here, in for Bear."** Not literally required by
   IN-FOR-BEAR LAW (the law says "says so out loud in the cold open") — added
   it because the source didn't and NBB variants of claude-liam reels should
   (matches the reference nbb-reorder-policy conversion pattern).

5. **B00 `seed` prop** changed from `hai-k12-lesson-differentiation` →
   `nbb-k12-lesson-differentiation`. Cosmetic — keeps the writer's
   deterministic timing distinct from the source render's cache so the two
   variants don't collide.

6. **Outro scene: `OutroSeries` → `OutroCTA`.** `brands/nbb.md` allows either;
   switched to `OutroCTA` because the NBB outro line now includes a spark
   ("One source, three tiers.") and needs the `@NikBearBrown` handle chip —
   both properties `OutroCTA` carries and the reference nbb-reorder-policy
   conversion uses. Kept the eyebrow information as part of the line itself.

7. **Subtitle rewrite in metadata.** Changed `subtitle` from "The K12 Lesson
   Differentiation Skill" (bare descriptor) to "One Source, Three Tiers"
   (the animating claim, per `/done`-style Teardown subtitle convention).
   Chapter/topic string kept identical.

8. **BCRY estimated_duration bumped 9 → left as 9 (kept).** New narration is
   30 words vs. 27 in source; still short. Audio-first pipeline rewrites
   `actual_duration_s` on next audio gen; the `estimated` field is
   pre-generation hint only.

9. **BHTF estimated_duration_s: 20 → 32.** New narration is ~90 words vs.
   source's ~50; the estimate needs to reflect that so `duration-planner`
   doesn't flag it. Again, `actual_duration_s` will be authoritative once
   audio is regenerated.

10. **NB03 narration is the longest expansion (from 47 → 71 words).** This is
    the design-choice beat and needed room for the trade-off ("They optimized
    for X at the expense of Y") — that sentence is the Teardown deliverable
    for the whole reel. The Manim scene is `BDNB03Scene` which is timing-
    agnostic; a longer narration extends the composition, no visual retiming
    needed.

## Not touched (intentionally)

- `beat_id`, `act` (except `BHTF` → "LLM EXERCISE"), `shot.type`,
  `remotion.pattern` (except `BOUT` → `OutroCTA`, see #6), `graphic.manim`
  scene names, `graphic.production_viz.chips` / `arrows` / `accent` / `strike`
  / `caption` / `label`. On-screen card copy is preserved verbatim; only color
  values inside the props were remapped.
- `metadata.build` block (source render snapshot), `audio_file` paths, `build`
  blocks per beat. These will get overwritten when this nbb- dir is actually
  rendered.
- `metadata.purpose` was rewritten to reflect the Teardown register framing
  (name the trade-off explicitly) — this is a metadata description of intent,
  not a source-of-truth fact, so it moves with the register.

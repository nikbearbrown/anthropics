# CONVERT-LOG — nbb-healthcare--claude-liam-clinical-note-extract-skill

Source: `../healthcare--claude-liam-clinical-note-extract-skill/beat_sheet.json` (Plain register, HAI cut)
Target: `beat_sheet.nbb.json` (Teardown register, NBB cut)
Converted: 2026-09-03
Voice: Kokoro `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW; unchanged from source, which already ran claude-liam)

## What changed

### Register (Step 2)
Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD).
Take-it-apart openings ("Take this Claude skill apart", "Here's what the skill
actually is", "Open the instructions"), mechanism-first framing, and one explicit
trade-off named at NB03 ("They optimized for auditability at the expense of
coverage: it will never fill in a value the note doesn't literally state, even
when a person could reasonably guess"). BCRY carry-out tightened to "Auditable
to a fault, and blind to anything the note doesn't spell out" — same claim,
Teardown teeth. Facts, filenames (SKILL.md, clinical-note-extract-skill), the
6-files/4-folders anatomy, and the four-step pipeline all preserved exactly.

### B00 cold open
Added "Liam here, in for Bear" at the head per IN-FOR-BEAR LAW — the sign-off
was already there at BOUT; the cold open was missing it. Kept the
BrutalistHesitantWriter visual and its TIMING LAW window (narration 34 words —
inside the 20–35-word band; `lead_silence_s: 1.0` preserved). Bumped
`estimated_duration_s` 13 → 14 to match the slightly longer narration.

### BHTF — the LLM exercise beat (Step 3)
BHTF was already second-to-last with a paste-ready prompt, so I made it the
LLM exercise beat in place rather than inserting a new B_LLM. Preserved
`beat_id: BHTF` (the "preserve every beat_id" rule beat the SKILL's suggested
`B_LLM` id). Changes:
- `act` → "LLM EXERCISE"
- Added `llm_exercise: { prompt, dig_deeper }` per SKILL schema
- Upgraded the prompt to a substantive write-a-SKILL.md-then-run-it exercise
  that produces something useful on its own (an actual SKILL.md + a sample
  clinical note + a demonstration of the cite-or-null discipline)
- Dig-deeper follow-up: add a 'diagnosis' field, run it twice — does the skill
  stay disciplined and null it, or start inferring one from the chief complaint?
  That's the video's central claim (auditability at the cost of coverage)
  re-tested by the viewer.
- Kept ClaudeComposerAsk visual (it IS the paste-into-Claude UX); rewrote the
  `command` prop to match the new exercise (shorter than the full prompt, tuned
  for readability on the composer chip).
- Bumped `estimated_duration_s` 26 → 32 for the longer narration.

### BOUT — the NBB outro (Step 4)
Rewrote the outro line in Teardown: "It cites the evidence. It never guesses.
Auditable to a fault. Liam, in for Bear." — same title-then-mechanism-then-sign-off
shape the sibling `nbb-cwc-workshops--claude-liam-reorder-policy` established.
Swapped `OutroSeries` → `OutroCTA` to carry an explicit `handle: "@NikBearBrown"`
chip (source `OutroSeries.eyebrow` referenced `@HumanitariansAI`, which no longer
belongs on an NBB cut). Kept `tail_silence_s: 1.0`. Bumped
`estimated_duration_s` 6 → 8 for the longer line.

## Judgment calls

1. **Retinted every hard-coded hex to the teardown palette.** The scaffold set
   `metadata.palette: "teardown"` but the beat props still carried humanitarians
   colors (`#F3EBDD` cream / `#2F2A26` ink / `#E4572E` accent). If those aren't
   remapped, a render will be visually a humanitarians reel with a teardown
   metadata label. Remapped to `#FFFFFF` / `#2A1A0E` / `#C8102E` in every
   `production_viz.colors[]` (NB01, NB02, NB03), the B00 BrutalistHesitantWriter
   `bg`/`ink`/`accent` props, and `metadata.ground`. Also changed
   `metadata.style_preset` from `humanitarians` → `teardown` for the same reason.

2. **Rebranded the on-screen channel to `@NikBearBrown`.** Source
   `folderLabel` / `channel_title` were both `@HumanitariansAI`; the BHTF
   ClaudeComposerAsk chip and the (now) OutroCTA handle would otherwise contradict
   the "Liam, in for Bear" sign-off. Changed `metadata.folderLabel`,
   `metadata.channel_title`, `BHTF.remotion.props.folderLabel`, and
   `BOUT.remotion.props.handle` to `@NikBearBrown`. Kept
   `metadata.playlist: "Claude Basics"` — it's a topic category, harmless on
   either channel.

3. **BHTF, not a new B_LLM.** See above — preserving `beat_id` beat inserting a
   duplicate beat. Result: BHTF is now the LLM exercise (second-to-last) and
   BOUT the outro (last), matching the ending order the SKILL asks for.

4. **Cold-open "Liam here, in for Bear."** Not literally required by IN-FOR-BEAR
   LAW (the law says "says so out loud in the cold open") — added it because the
   source didn't and NBB variants of claude-liam reels should. Kept the narration
   inside the 20–35-word TIMING LAW window (34 words).

5. **B00 `seed` prop** changed from `hai-clinical-note-extract` →
   `nbb-clinical-note-extract`. Cosmetic — keeps the writer's deterministic
   timing distinct from the source render's cache so the two variants don't
   collide.

6. **BCRY `WantQuote.quote`** was rewritten to match the new BCRY narration —
   the WantQuote contract is that the spoken carry-out and the on-screen quote
   are identical. This is on-screen copy but it *is* the narration, so it moves
   with it. Kept `sparkLine: "Cites. Never guesses."` (still fits the Teardown
   register — a short, honest, mechanism-forward summary).

7. **Removed `_variant_todo`** — checklist complete.

## Not touched (intentionally)

- `beat_id`, `act` (except BHTF → "LLM EXERCISE"), `shot.type`, `remotion.pattern`
  (except BOUT `OutroSeries` → `OutroCTA` — a permitted swap per the nbb SKILL),
  `graphic.manim` scene names (BKNB01Scene, BKNB02Scene, BKNB03Scene),
  `graphic.production_viz.label` / `chips` / `arrows` / `accent` / `strike` /
  `caption`. On-screen card copy is preserved verbatim; only color values inside
  the props were remapped.
- The B00 `note` field — the TIMING LAW, hesitate/mistake rates, and the sibling
  reference (financial-services--claude-liam-kyc-rules) still apply unchanged.
- `metadata.title` and `metadata.subtitle` — both already fit the Teardown
  register (title *is* the mechanism claim; subtitle names the actual technique).
- `metadata.build` block (source render snapshot), `audio_file` paths, `build`
  blocks per beat. These will get overwritten when this nbb- dir is actually
  rendered.

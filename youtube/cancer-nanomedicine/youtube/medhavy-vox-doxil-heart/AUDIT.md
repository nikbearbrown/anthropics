# AUDIT — medhavy-vox-doxil-heart

Date: 2026-08-28
Contract: `youtube/LENS-NOTES.md`, `books/brutalist-art/skills/make/rebuild/SKILL.md`,
`books/brutalist-art/skills/make/nopunt/SKILL.md`

## Phase 0 — Rebuild contract
- PASS pre-rebuild backup written byte-exact (`beat_sheet.pre-rebuild.json`, diff -q identical).
- PASS narration on B01–B12 locked; no body-narration edits.
- PASS voice envelope normalized (dropped dead `voice_id`, `clock` prose,
  `_variant_todo`, stale `build` block).
- PASS Manim/production_viz specs preserved on the six body beats that would
  eventually promote to Manim (B04, B05, B07, B09, B10, B11).
- PASS non-Claude skin retained: Medhavy outros (OutroSeries + OutroCTA)
  kept; no B00/BVDT/BHTF/BOUT Claude-wash.

## Phase 1 — Audit checks

1. **Stale renders — PASS/FIXED.** No prior `.mp4` renders existed at reel
   root or in `media/` (the pre-rebuild `build` block referenced files that
   never existed). `mp3/` audio dates 2026-07-16 — will regenerate in Phase 2.

2. **Bookends — PASS (non-Claude skin).** This is a MEDHAVY channel reel;
   the rebuild contract forbids Claude-washing an open or outro. Medhavy
   bookends: B01 cold-open title beat, B12 recap beat, B13 OutroSeries,
   B14 OutroCTA — the sibling `medhavy-vox-complexity-yield` uses the same
   structure. Present.

3. **Spark lines — N/A.** No `ClaudeComposerAsk` beats in this Medhavy skin.

4. **Verdict — PASS.** No `BVDT` bookend (Medhavy skin has none). B12 is the
   RECAP, authored from body content ("It didn't fix the tumor / It sealed the
   drug away from the heart / EPR was context — cardiac protection was the win").
   Not a template line, not a placeholder.

5. **Chart text — N/A (this cut).** No Manim scenes render in this slate cut;
   the six `graphic.production_viz` specs are kept as spec for a later Manim
   pass and are not on-screen text.

5b. **Card text — FIXED.** All FormACard `lines` are complete sentences authored
   from each beat's own narration. No placeholder subs, no overflow labels.

6. **Punt sweep — FIXED.** Zero gen-AI ask strings, zero unfilled
   `PIPELINE → render animated_graphics.py` slates, zero `STILL src=ai` for
   conceptual content, zero DoodleScene, zero unfilled `remotion_scenes`. Every
   body beat routes to `FormACard`; every outro to its Remotion component with
   correct props shape (was: outro props matched a phantom schema — `seriesTitle`/
   `tagline`/`githubSlug` for OutroSeries, `authorName`/`ctaText` for OutroCTA;
   real component reads `{eyebrow, line}` / `{line, handle}`).

7. **Card-only reel — LOG (accepted for review slate cut).** All 14 beats are
   Remotion cards or Remotion outros. The MEDHAVY skin's slate-cut pattern is
   card-first (verified against `medhavy-vox-complexity-yield` — also all
   FormACard body + Medhavy outros). Manim promotion for the six spec'd beats
   is a later pass; the review slate cut is legitimate.

8. **Lens audit — PASS (two moves).**
   - **Plato** (B09, explicit in production_viz note): teams grade the artifact
     (the EPR approval narrative) as if it were the wall (the actual mechanism —
     cardiac protection). Artifact / world / relationship is the beat.
   - **Descartes** (B10): what would falsify "copying Doxil for our drug will
     work"? If our drug has no cardiac problem, Doxil's mechanism has nothing to
     buy. A checklist that yields a decision.

9. **Brand fields — FIXED.**
   - `folderLabel: "@MedhavyAI"` — was missing; added.
   - `engine: "kokoro"` + `voice_kokoro: "af_kore"` — Medhavy voice, verified
     against sibling `medhavy-vox-complexity-yield`.
   - Persona coherence: no "Liam, in for Bear" narration in this reel; Medhavy
     voice `af_kore` is the audio.

10. **Pacing — LOG.** Narration wps against estimated durations, using the
    original sheet's `actual_duration_s` where measured (Kokoro rendering at
    voice `af_kore` will re-measure in Phase 2). All beats fall in a normal
    range for narration cadence; will re-verify after regenerated audio.

11. **`type_check.py` — pending.** Runs against rendered clips in Phase 2.

## Blocking issues
None. Proceeding to Phase 2 build.

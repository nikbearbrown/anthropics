# REBUILD-LOG — claude-liam-vox-size-paradox

Date: 2026-08-28
Contract: `books/brutalist-art/skills/make/rebuild/SKILL.md`
Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact copy of the prior sheet)

## Locked (carried over verbatim)
- All body narration on B01–B15 (script — the point of the reel). Word-for-word.
- Beat order (B00 · B01–B13 body · B14–B15 series/CTA · BVDT · BHTF · BOUT).
- Act labels.
- Shot INTENT per body beat: the numbers (6.2% / 2.1% / 15% / 72% / 80%),
  color semantics (teal small / crimson big), the drawn-figure ideas.
- Metadata identity: title, slug, topic, register, source pointer, channel
  `@NikBearBrown`, palette `claude`.

## Rebuilt (per current doctrine)

### Envelope
- DROPPED `voice_id: "TyW6NH39JcFb5M3xdIIk"` — dead ElevenLabs field
  (VOICE-LOCK rule).
- DROPPED `clock: "narration (Kokoro (VOICE-LOCK)) — durations below are
  word-count estimates until GATE 0 audio lock"` — ElevenLabs-era prose,
  no longer needed since Kokoro measurements already stamp actual_duration_s.
- DROPPED `_variant_todo` list — the variant work it describes is what this
  rebuild is doing.
- DROPPED metadata `.build` block — Jul 16 stamp against non-existent
  media/ files, now superseded.
- DROPPED metadata `total_estimated_duration_seconds` — recomputed on compile.
- KEPT `engine: kokoro`, `voice_kokoro: am_onyx` — matches narration's
  "This is Liam, in for Bear" persona.

### Bookends
- B00 (ClaudeComposerAsk): greeting was `"Liam"` (missing world-language
  hello — the exact SPARK-LINE LAW defect flagged in PHASE 1 §3). Rewritten
  to `"Hej, Liam"` (Swedish/Danish hello). Adjacent reels use `Hola` and
  `Salaam`; `Hej` is free in this run. Command rewritten from long
  self-referential form to a real ask.
- BVDT (ClaudeVerdictArtifact): placeholder lines "Key finding one/two/three"
  and empty narration → AUTHORED four verdict lines built from body nouns
  and numbers (6.2%/2.1%, 15%/72%, three-fold vs five-fold). Narration
  authored to say the verdict aloud (§4 authoring rule for a body of 13
  beats / ~485 words).
- BHTF (ClaudeComposerAsk): empty narration → authored "Your turn." close
  built from the reel's own thesis (delivery-metric interrogation).
- BOUT (ClaudeTitleOutro): unchanged intent, kept re-read of the title.
- B14 (OutroSeries) / B15 (OutroCTA): kept — the reel already carries a
  short channel outro before the Claude close. Existing audio in mp3/.

### Body beats — pipeline-slate class removed
The pre-rebuild sheet had every body beat marked `SLATE` with either
"PIPELINE → render animated_graphics.py scene B0X_*" (no scenes.py exists
in the reel folder) or "YOU → 5–10s gen-AI clip" (a punt slate). PHASE 1
§6 + §7 forbid both. Every body beat is now routed to a real Remotion
pattern — FormBCard with N=2 or N=3 (or N=4 on B12) — carrying real
labels and subs written from that beat's own narration nouns and numbers.

- B01 FormBCard N=3: bigger loads more · smaller cures more · why?
- B02 FormBCard N=2: 150 nm piles at rim · whole-organ assay wins
- B03 FormBCard N=2: 150 nm arm 15% · 30 nm arm 72%
- B04 FormBCard N=2: more drug in · less kill
- B05 FormBCard N=3: vessels leak · lymph cannot clear · bigger stays
- B06 FormBCard N=2: 150 nm 6.2% ID/g · 30 nm 2.1% ID/g
- B07 FormBCard N=3: rim · matrix · core (drawn figure — three zones)
- B08 FormBCard N=3: outward pressure · slow diffusion · rim-stuck
- B09 FormBCard N=2: 30 nm 80% even · 150 nm rim only
- B10 FormBCard N=3: hypoxic core · stress-selected · drive recurrence
- B11 FormBCard N=2: rim mass ≠ delivery · distribution wins
- B12 FormBCard N=4: 6.2% · 2.1% (80% even) · 15% shrink · 72% shrink
- B13 FormBCard N=2: smaller cures more · where not how much

### Datable-claim edits (narration)
None. This reel is a mechanistic explainer with no model names, versions,
prices, or "as of" phrasing. Every narration line locked verbatim from
the pre-rebuild sheet on B01–B15.

## Notes
- Card-only reel (PHASE 1 §7): body is entirely FormBCards — no Manim.
  The three-zone card (B07) IS the drawn figure — three concentric
  spatial labels ordered rim → matrix → core, the exact spatial split the
  narration's mechanism argument depends on. Same argument the epr-delivery-funnel
  rebuild used for its funnel-attrition card.
- Lens (PHASE 1 §8): three moves earned.
  - PLATO — the whole-organ %ID/g assay is the artifact; per-cell drug
    delivery is the world; the assay reads at a rim the drug never had
    to leave. Named in narration on B02 → B07 → B11.
  - DESCARTES — "what would have to be true for bigger-is-better to be
    wrong?" The 150-nm-arm 15% vs 30-nm-arm 72% outcome is exactly the
    checklist the paradox produces (B03, B12).
  - HUME — the whole-organ measurement's confidence is a property of the
    assay (mass integrator), not a property of tumor kill (spatial).
    The "same dose, more drug in, less kill" line is Hume's move stated
    plainly.

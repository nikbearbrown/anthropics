# REBUILD-LOG — hai-vox-trial-failure-tree

Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact copy of sheet as of 2026-08-26).

## Locked (carried over verbatim)
- Every `narration_text` on every beat. No datable claims were rewritten; the
  illustrative-number pass in B12 (7 %, 75 %, <3 %, 21 %) is already labeled
  illustrative in the sheet's `note`, so it stands.
- Beat order and act structure: COLD OPEN → THE QUESTION → THE PROBLEM →
  THE MECHANISM → THE IMPLICATION → THE EXAMPLE → RECAP → OUTRO.
- Metadata identity: slug, title, topic, source, register, palette.

## Envelope dead fields dropped
- `metadata.voice_id: "qdEb53HLreRBCD1FQE30"` — ElevenLabs-era, DROPPED.
- `metadata.clock` prose ("narration (Kokoro (VOICE-LOCK)) — durations below
  are word-count estimates until GATE 0 audio lock") — ElevenLabs-era GATE 0
  language; VOICE-LOCK now measures duration deterministically. DROPPED.

## VOICE-LOCK (already present, verified)
- `engine: kokoro`, `voice_kokoro: am_onyx` — VOICE-LOCK compliant, kept as-is.
- Non-claude channel (HAI / Humanitarians AI); no Claude bookends imposed.

## Props re-shaped to current zod schemas
Old props referenced schemas the components no longer use. Intent (the shot
list) is locked; the prop shape adapts.

- **B02 FormACard.lines**: OLD `["The particle was elegant — a polymeric
  nanoparticle with a targeting…"]` — a truncated sentence from an earlier
  narration draft ("elegant" is not in current narration). NEW: four vox lines
  drawn only from current B02 narration ("A polymeric nanoparticle. /
  Targeting ligand. / Payload core. / Preclinical data supported the trial.").
- **B11 FormACard.lines**: OLD `["Building delivery measurement into the trial
  — an imaging tracer cohort,…"]` — truncated. NEW: four vox lines from
  current B11 narration ("Add delivery measurement." → "A binary negative
  becomes a diagnosable result.").
- **B14 OutroSeries.props**: OLD `{seriesTitle, tagline, githubSlug}` matches
  no current schema. NEW: `{eyebrow: "CANCER NANOMEDICINE", line: "Part of
  the Cancer Nanomedicine series from Humanitarians AI."}` per current
  `outroSeriesSchema = z.object({eyebrow, line})`.
- **B15 OutroCTA.props**: OLD `{authorName, handle, ctaText}` matches no
  current schema. NEW: `{line: "More at humanitarians.ai", handle:
  "@humanitariansai"}` per current `outroCtaSchema`.

## Rebuild scope (this pass)
- Slate-cut for review only. Body beats B01, B03, B04, B05, B06, B07, B08,
  B09, B10, B12, B13 are declared slates: their shot intents call for
  gen-AI clips, Manim scenes (`B04_BinaryEndpoint`, `B06_ThreeFailures`,
  `B07_DeliveryFailure`, `B08_PayloadFailure`, `B09_BiologyFailure`,
  `B10_FullTree`, `B12_TwoPrograms`) that DO NOT exist in
  `runtime/manim/animated_graphics.py`, or DOCUMENT quotes with no plate.
  Authoring seven new Manim scenes plus five gen-AI clips is not the
  slate-cut mandate; the compiler renders them as PIL request-cards.
- Beats with valid Remotion patterns are rendered real: B02 (FormACard),
  B11 (FormACard), B14 (OutroSeries), B15 (OutroCTA).
- Output name will be `<slug>-slate.mp4` per PHASE 2 rule (any beat = slate
  ⇒ slate-suffixed filename).

## No narration changed
The rebuild contract holds: not a single narration_text line was rewritten.
The four datable-numeric claims in B12 are already flagged illustrative in
the sheet metadata.

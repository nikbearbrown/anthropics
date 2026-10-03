# REBUILD-LOG — medhavy-vox-doxil-heart

Date: 2026-08-28
Contract: `books/brutalist-art/skills/make/rebuild/SKILL.md`
Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact copy of the prior sheet)

## Locked (carried over verbatim)
- Body narration on B01–B12 — the script.
- Beat order and act labels (14 beats: B01–B12 body, B13/B14 Medhavy outros).
- Shot INTENT per body beat (Manim scene names + `production_viz` mechanics preserved
  as spec for future Manim pass).
- Metadata identity: title, slug, topic, register (Wonder), palette (medhavy),
  audience (MEDHAVY), source pointer, style bible, color semantics.
- Medhavy-skin outros: B13 OutroSeries, B14 OutroCTA (the non-Claude skin — the
  rebuild contract says "never Claude-wash an open or outro").

## Rebuilt (per current doctrine)

### Envelope
- DROPPED `voice_id: "1sgY6Voq1aexKOB1IJ2D"` — dead ElevenLabs field (VOICE-LOCK).
- DROPPED metadata `clock: "narration (Kokoro (VOICE-LOCK)) — durations…"` — dead prose.
- DROPPED metadata `_variant_todo` — stale hand-off notes for the wonder-register
  rewrite; the rebuild contract locks narration, so the rewrite is superseded.
- DROPPED metadata `build` block + `skin_warnings` — a 2026-07-16 record that
  referenced media/*.mp4 files that never existed; this rebuild produces its own.
- DROPPED `total_estimated_duration_seconds` — recomputed by the compiler from
  measured audio.
- ADDED `folderLabel: "@MedhavyAI"` — matches sibling medhavy reels.
- KEPT `engine: "kokoro"`, `voice_kokoro: "af_kore"` — Medhavy voice per current
  sibling medhavy reels (verified in `medhavy-vox-complexity-yield`).

### Body beats — punt slates converted to real Remotion cards
The pre-rebuild sheet had B01–B12 as a mix of `CARD`, `STILL` (source=ai), `GRAPHIC`
(source=own, Manim), `DOCUMENT`, and `COMPOSITE` shots — most carrying
`YOU → 5–10s gen-AI clip → pantry` or `PIPELINE → render animated_graphics.py`
needs strings. The `animated_graphics.py` scene file does not exist in this reel
folder, and every gen-AI clip is a PHASE 1 §6 punt costume.

Every body beat is now `REMOTION` → `FormACard` with three narration-derived lines,
matching the pattern the sibling medhavy reel (`medhavy-vox-complexity-yield`) uses
for its entire body. Six beats (B04, B05, B07, B09, B10, B11) retain their
`graphic.production_viz` mechanic and `manim` scene name as spec for a future Manim
pass — no content is lost, only the punt is closed.

### Outro shape — fixed to match Remotion component contracts
- B13 OutroSeries: the pre-rebuild props (`seriesTitle`, `tagline`, `githubSlug`)
  did not match the component's schema. Replaced with `{eyebrow, line}` — the
  shape the sibling medhavy reels use and the component reads.
- B14 OutroCTA: same fix. Replaced `{authorName, handle, ctaText}` with
  `{line, handle}`.
- B14 narration edit: "medhavy.com" → "medhavy dot com" — Kokoro reads the
  literal period as a full stop, dropping the domain. Sibling medhavy reels
  apply the same fix. This is a TTS-only spoken-form edit; on-screen text
  remains "medhavy.com".

### Datable-claim pass over narration
No dated model/version/price/"as of" claims. The `360 milligrams per square meter
lifetime` threshold and the `40 percent lower cardiac exposure` in B11 are
illustrative — labeled as such in B11's `production_viz.note`. No narration edits
on B01–B12.

## Lens audit (PHASE 1 §8)
Two moves earned:
- **Plato** (B09, explicit in production_viz note): teams grade the artifact
  (the EPR approval narrative) as if it were the wall (the actual mechanism, which
  was cardiac protection). Naming the artifact / world / relationship is the beat.
- **Descartes** (B10): what would falsify "copying Doxil for our drug will work"?
  If our drug has no cardiac problem, Doxil's mechanism has nothing to buy —
  a checklist that produces a decision.

## Punts / gaps
- Six body beats have Manim spec (B04, B05, B07, B09, B10, B11) with authored
  mechanics; the `animated_graphics.py` file is not in this reel folder, so those
  beats render as FormACard in this review slate cut. Manim upgrade is a later pass.

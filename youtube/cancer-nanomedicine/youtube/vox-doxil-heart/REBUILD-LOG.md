# REBUILD-LOG — vox-doxil-heart (2026-08-30)

## LOCKED (carried verbatim)

- Narration for B01…B14 — no rewrites. Chapter-verbatim numbers (360 mg/m²
  lifetime cardiac dose threshold) preserved.
- Beat order and act labels (COLD OPEN → THE QUESTION → THE PROBLEM →
  THE MECHANISM → THE IMPLICATION → THE EXAMPLE → RECAP → OUTRO).
- Metadata identity: slug, title, topic, source pointer, style_bible,
  color_semantics, aspect_ratio.
- Shot INTENT per beat — `production_viz` mechanic strings and image prompts
  (B02, B06) retained.

## REBUILT (envelope only)

1. **Voice engine** — DROPPED `voice_id: "TyW6NH39JcFb5M3xdIIk"` (ElevenLabs).
   ADDED `engine: "kokoro"`, `voice_kokoro: "am_onyx"`. Metadata `clock`
   rewritten to reference Kokoro measurement, not ElevenLabs.
2. **Audio** — old July-8 ElevenLabs mp3s to be replaced by fresh Kokoro
   `am_onyx` generation. Measured durations will overwrite
   `actual_duration_s` per beat.
3. **Skin** — unchanged. This is a vox-editorial (non-Claude) channel; own
   bookends retained (B01 title, B13 OutroSeries, B14 OutroCTA).

## DATABLE-CLAIM PASS

No datable claims required editing. Doxorubicin dosing threshold
(360 mg/m² lifetime) and PEG-liposome mechanism are stable clinical facts
from the source chapter. FDA-approval framing does not name a year, model,
or version that has rotted.

## DROPPED FIELDS

- `metadata.voice_id` — ElevenLabs voice UUID.
- ElevenLabs-era `clock` phrasing ("word-count estimates until GATE 0 audio
  lock" — replaced with a statement that `actual_duration_s` from Kokoro
  measurement is ground truth).

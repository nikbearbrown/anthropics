# REBUILD-LOG.md — vox-batch-distribution

Date: 2026-08-30
Pipeline: filmloop (one-reel invocation)
Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact of the sheet as it stood on entry).

## Narration lock — the exception
No datable claim edits. Locked script preserved verbatim for B01–B12 body beats. New
narration authored only where the rebuild contract allows it: BVDT (verdict) and BHTF
(your-turn) previously had `narration_text: ""` — the closing block is the one place fresh
writing is expected.

- **BVDT narration:** authored fresh, discusses the artifact (does not recite it —
  §8.10 correlation 0.17 after edit).
- **BHTF narration:** authored fresh (real per-batch exercise, no bracket placeholder).

## Envelope rebuild — dead fields dropped
- Metadata: dropped `voice_id: "TyW6NH39JcFb5M3xdIIk"` (ElevenLabs-era).
- Metadata: dropped `clock` prose that named ElevenLabs.
- Metadata: dropped `_variant_todo` (variants already done; four bookends present).
- Beats: dropped B13 (`OutroSeries`) and B14 (`OutroCTA`) — legacy outros superseded by
  BVDT/BHTF/BOUT four-bookend close. A Claude-skin reel cannot ship two outros.

## Shot-form rebuild
- B00 greeting `"Liam"` → `"Salam, Liam"` (world-hello per spark-line rule).
- B01 FormBCard placeholder items → real items authored from the cold-open narration.
- B02 punt costume `STILL src=ai + FormACard truncated line + "YOU → gen-AI clip"` → clean
  FormBCard two-item batch comparison.
- B03, B09, B12: stale `build.needs = "YOU → gen-AI clip"` cleared; kept as legit
  CARD/DOCUMENT surfaces.
- B04, B05, B06, B07, B08, B10, B11: Manim GRAPHIC intent → Remotion FormBCard (see
  TEMPLATE-MISSES.md — Manim scene classes do not exist; downgraded rather than block).
- BVDT: `artifactHeading` `"Key findings"` (placeholder) → `"The distribution is the product"`;
  `artifactLines` template defaults → three real findings compressed from the body.
- BHTF: command placeholder `"Take what you learned from [ ... ]"` → authored exercise.

## Machinery output
- Fresh Kokoro audio: BVDT (17.05s), BHTF (16.19s), voice `am_onyx`.
- Remotion renders: 13 beats — all `ok`.
- `type_check.py` GATE T: PASS.
- `verdict_audit.py`: no longer flagged.
- `compile.py --review --allow-slates`: 231.7s slate cut, lane-check PASS, audio -27.3 dB.

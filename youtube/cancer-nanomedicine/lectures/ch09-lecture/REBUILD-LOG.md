# REBUILD-LOG — cancer-nanomedicine-ch09-nucleic-acid-delivery (2026-08-31)

## Phase 0 — rebuild contract

- `beat_sheet.pre-rebuild.json` written byte-exact of `beat_sheet.json`
  (shasum: `0e541bd5d7eef41b8c13f7e40012435c137b695d` — matches both files).
- Narration locked. No text edits to any of the 12 segments.
- Voice envelope preserved: `voice_id: TyW6NH39JcFb5M3xdIIk` (ElevenLabs Bear
  clone). Legitimate paid default for @NikBearBrown lecture course per AGENTS.md.
- Segment IDs, ordering, section labels, `actual_duration_s` values all unchanged.

## Phase 1 — audit

See `AUDIT.md`. Every non-N/A check PASS. One informational fact-check note
logged (S07 `~13B COVID-19 mRNA doses` slide gloss — narration unaffected;
edit deferred to a later editorial pass).

## Phase 2 — render

`render.py` copied verbatim from ch10-lecture sibling (same lecture-deck
pipeline). Ran once, from this folder:

- Re-shot 12 slide screenshots from `deck.html` (Jul-15 deck picked up over
  Jul-11 slides) at 1280×720, DPR 2, via headless chromium.
- Muxed each screenshot with its ElevenLabs Bear audio via ffmpeg
  (image loop + AAC 160k + 0.6 s trailing silence per slide).
- Concat-demuxed 12 clips into `cancer-nanomedicine-ch09-nucleic-acid-delivery.mp4`
  (17.66 MB · 576 s · 9.6 min).

## Post-render gates

- ffprobe: audio stream present, `codec=aac`, `sample_rate=44100`, `duration=576.06 s`.
- volumedetect: `mean_volume = -18.9 dB` (well above the −40 dB silent-master floor).
- Gate V: read 12 midpoint frames from `_qc/frames/*.png` — titles legible, orange
  accent (`#ea580c`) contrast on cream (`#eaeae4`) OK; dark S12 close slide renders
  correctly on `#0b0b0e`; chip/flow/wire/stat/grid2/balance/thesis/close components
  all render as authored. Zero overflow, zero container clipping, zero MAJOR/BLOCKER.
- mtime: mp4 Aug 31 07:29 · beat_sheet.json Jul 12 17:05 · cut is newer. DONE guard OK.

## Never-touched

- Narration text for all 12 segments — unchanged from `beat_sheet.pre-rebuild.json`.
- Voice envelope, segment IDs, ordering, `actual_duration_s`.
- No post-compile edits to `beat_sheet.json`.

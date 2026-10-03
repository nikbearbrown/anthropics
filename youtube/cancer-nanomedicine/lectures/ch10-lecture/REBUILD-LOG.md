# REBUILD-LOG — cancer-nanomedicine-ch10-photodynamic-photothermal (2026-08-31)

## Fixes applied under Phase 0 / Phase 1

### 1. Product-name typo — S07 slide title (fact fix, not narration)

- **Where:** `deck.html` line 151 (S07 `<h1 class="stitle">`) AND
  `beat_sheet.json` S07 `.title[0][0]`.
- **Change:** `AUROLAASE` → `AUROLASE`.
- **Source:** Nanospectra product name is *AuroLase* (one A after the L). The
  reel's own narration for S07 says "AuroLase" correctly, and the deck body
  reads "AuroLase (Nanospectra) — prostate cancer" correctly. Only the on-screen
  title carried the double-A.
- **Justification:** Fact / product-name correction. Narration audio was NOT
  regenerated — the audio already speaks the name correctly. Sheet + deck edit
  only, followed by re-render of screenshots and concat.
- **Sheet mtime after this edit:** re-render below produces a newer mp4 mtime
  so the supervisor's "cut newer than sheet" DONE check still holds.

## Never-touched

- Narration text for all 12 segments — unchanged from `beat_sheet.pre-rebuild.json`
  (sha1 of that file: `eebf2f324762d959ae26b54fa12323c08b3a8263`).
- Voice envelope — `voice_id: TyW6NH39JcFb5M3xdIIk` (EL Bear clone) preserved;
  this reel legitimately uses the paid @NikBearBrown default per AGENTS.md.
- Segment IDs, ordering, section labels, `actual_duration_s` values.

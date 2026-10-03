# REBUILD-LOG.md — vox-epr-gap (2026-08-30)

Cohort C — legacy vox (`vox-editorial` preset, teal/crimson). Rebuild rule: keep the reel's own skin; regenerate the machinery.

## Envelope changes (metadata only)

| Field | Before | After | Reason |
|-------|--------|-------|--------|
| `voice_id` | `TyW6NH39JcFb5M3xdIIk` | (dropped) | ElevenLabs-era artifact; VOICE-LOCK dead-field drop |
| `clock` | `narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock` | `narration (Kokoro am_onyx, VOICE-LOCK) — actual_duration_s written back by generate_audio_kokoro.py` | GATE 0 has been retired; clock prose refreshed to current pipeline |
| `engine` | (absent) | `kokoro` | VOICE-LOCK envelope; every reel names its engine |
| `voice` | (absent) | `am_onyx` | VOICE-LOCK default (Liam) |
| `channel` | (absent) | `@NikBearBrown` | brand-field completeness |
| `folderLabel` | (absent) | `@NikBearBrown` | brand-field completeness (channel handle, not brand key) |

## Beat-level FormACard fixes

Narration is LOCKED; these are `props.lines` fixes on the card VISUAL, not narration edits.

- **B02** — FormACard `lines` was `["In the lab, the result is striking. A docetaxel nanoparticle accumulates…"]` (ellipsis-truncated recitation). Replaced with three-line summary drawn from the same narration ("In the lab, the result is striking." / "Docetaxel nanoparticles accumulate in the mouse tumor." / "The preclinical data looks like a breakthrough."). No narration change.
- **B06** — FormACard `lines` was `["This is the enhanced permeability and retention effect — EPR. It…"]` (ellipsis truncation). Replaced with three-line summary ("This is the enhanced permeability and retention effect — EPR." / "It works in the laboratory." / "Subcutaneous mouse xenografts are EPR at maximum: thin-walled vessels, no dense stroma."). No narration change.

## Datable-claim edits to narration

None this pass. Narration is factually current per FACTCHECK.md (2026-07-08): illustrative numbers (8% ID/g, 0.3% ID/g, 200 nm) are labeled illustrative in production_viz notes; no model versions, prices, or "as of" claims present.

## Backup

- `beat_sheet.pre-rebuild.json` — byte-exact snapshot of `beat_sheet.json` as of 2026-08-30 14:17, before any rebuild edit.

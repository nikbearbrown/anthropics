# REBUILD-LOG.md — vox-delivery-diagnosis (2026-08-30)

Cohort C, legacy vox reel. Rebuild pass to VOICE-LOCK + slate-cut-honesty.

## LOCKED (verbatim)
- All 14 beat `narration_text` — the script is fixed.
- Beat order (B01 title → B12 endcard → B13/B14 outro).
- Metadata identity: slug, title, topic, source, style_bible, color_semantics, note (card exclusions).
- Shot intent per beat: `graphic.manim` class names (vox_scenes.py) and `production_viz.mechanic` labels are the shot list, unchanged.

## REBUILT (envelope)
- Dropped `metadata.voice_id = "TyW6NH39JcFb5M3xdIIk"` — ElevenLabs voice id, dead field per VOICE-LOCK.
- Added `metadata.engine = "kokoro"` / `voice = "am_onyx"` / `voice_kokoro = "am_onyx"`.
- Rewrote `metadata.clock` prose from the pre-audio placeholder ("… word-count estimates until GATE 0 audio lock") to measured-audio phrasing ("actual_duration_s per beat is ground truth, measured from generated mp3s").
- `vox_scenes.py` import fix: header walked `parents[3]/vox/aspects/explainer/vox-explainer/manim` which does NOT exist under `anthropics/youtube/…`. Copied `books/vox/aspects/explainer/vox-explainer/manim/vox_graphics.py` into the reel dir (34,753 B) and rewrote the import to load from `pathlib.Path(__file__).resolve().parent`. Same fix as sibling `vox-targeting-uptake` (FILMLOOP-LOG 2026-08-28).

## DATABLE CLAIMS
None found in narration. B11 illustrative numbers (7 %, 75 %, 3 %, 21 %, ten-patient cohort) are explicitly labeled `illustrative` in the sheet's `metadata.note` and in the visual — no citation attached. No edits.

## PUNT FIXES (§5 card-text)
Both STILL·ai beats carried single-line FormACard placeholders that were just the narration head truncated with a Unicode ellipsis:

| beat | old `props.lines` | new `props.lines` |
|------|-------------------|-------------------|
| B02 | `["Before that swap happened, one collaborator asked a different question: where…"]` | `["SLATE — fluorescence biodistribution scan of a mouse", "crimson hotspot in the liver, dim outline over the tumor", "editorial newsprint collage, false-color, no digital glow"]` |
| B08 | `["The result is a biodistribution map. Particles concentrated in the liver…"]` | `["SLATE — two body silhouettes side by side", "left: liver and spleen crimson (delivery failed)", "right: tumor teal (delivery confirmed)"]` |

Sibling `vox-targeting-uptake` used the same three-line honest-slate substitution pattern. This is the review-slate-cut convention: name what the AI still would show, so a future pass can drop in the actual asset without touching narration.

## AUDIO
- Deleted stale mp3s (all 2026-07-08) and `mp3/timings.json`.
- Generated fresh with `generate_audio_kokoro.py` @ `voice_kokoro=am_onyx`. 14 mp3s, cost $0.00.
- Measured durations written back to `beat_sheet.json` as `actual_duration_s` per beat (ground truth for compile).

## RENDERS
- Deleted stale `clips/master.m4a`, `clips/_work`, `clips/{concat,audio}.txt`, `clips/manifest.json` (all 2026-07-16).
- Manim rendered all 10 body Scene classes at 720p30 (B01_Title, B03_Question, B04_TwoCauses, B05_OppositeFixes, B06_QuoteToxin, B07_LabeledParticle, B09_DeliveryFix, B10_QuoteDelivery, B11_TwoPrograms, B12_End). Copied to `manim/B*.mp4`.
- Remotion rendered the 2 FormACard slate beats (B02, B08) + 2 outros (B13 `OutroSeries`, B14 `OutroCTA`).

## GATE T (type_check.py) — advisory fixes to real beats

- B01 `CANCER NANOMEDICINE` eye label: font_size 18 → 24; title 24 → 26.
- B11 `illustrative` eye label: `font_size=18 SLATE` → `ILLUSTRATIVE font_size=22 SLATE BOLD`.
- B12 `CANCER NANOMEDICINE` eye label: font_size 18 → 24.
- Re-rendered B01/B11/B12 after size fixes; re-copied to `manim/`.

Post-fix TYPECHECK.md still shows 6 FAIL rows (B01/B04/B09/B10/B11/B12); each was frame-verified from `_qc/frames/` — every failure is a blob-detector false-negative on this reel's chip-on-color renderings or a 720p-underestimate of a 4K master. Details logged in AUDIT.md. No validator change; no strict-mode downgrade.

## COMPILE

`compile.py` — 14/14 filled, master 3840×2160 p24 h264 aac, 164.041 s, sha1-manifested per-beat clips. `GATE AUDIO: PASS mean_volume -24.0 dB`. Motion histogram `drawon:4 hold:3 kenburns:2 highlight:2 fade:2 scan:1`. `sheet mtime preserved` (compile.py stamps build info via os.utime — cut is 5 min 30 s newer than the sheet).

Post-build:
- `beat_sheet.json` mtime: `2026-08-30 18:18:49`
- `vox-delivery-diagnosis.mp4` mtime: `2026-08-30 18:24:19`

Cut is newer than sheet — DONE-check passes.

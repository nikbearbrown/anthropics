# REBUILD-LOG — medhavy-vox-fdg-proxy
_Pass: 2026-08-31_

## Snapshot

`beat_sheet.pre-rebuild.json` written byte-exact before any edit (21082 bytes, 2026-08-26 mtime).

## LOCKED (verbatim from pre-rebuild)

- All 14 `narration_text` fields (see one exception below).
- Beat order (B01–B14), act structure, `t_start`, `estimated_duration_s`.
- Metadata identity: slug, title, topic, source pointer (`06-nano-enabled-imaging-and-contrast.md`), register (Wonder), palette (medhavy), audience (MEDHAVY), `outro_source`, style_bible, color_semantics, note.
- `graphic.production_viz` blocks on B04/B05/B08/B10 (kept as the shot-list intent for a future Manim pass).
- `document` quote blocks on B07/B11 (kept as the shot-list intent for a future editorial-quote scene).
- `card`/`scene_description`/`image_prompt`/`new_visual_element` shot-list identifiers.

## REBUILT

### Envelope
| Field | Old | New | Rationale |
|-------|-----|-----|-----------|
| `voice_id` | `"1sgY6Voq1aexKOB1IJ2D"` | DROPPED | ElevenLabs-era; VOICE-LOCK now Kokoro |
| `clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | DROPPED | ElevenLabs-era prose |
| `_variant_todo` | 4-item migration checklist | DROPPED | Migration is done |
| `build` | Old build stamp claiming 2/14 filled + 12 slates | REGEN by compile.py (now 14/14 VIDEO) | Stale — compile regenerates |
| `folderLabel` | (missing) | `"@MedhavyAI"` | Was missing; channel handle for Medhavy |
| `source` | (missing at top) | `"cancer-nanomedicine/chapters/06-nano-enabled-imaging-and-contrast.md"` | Was buried inside `purpose`; promoted per current sibling convention |
| `engine` | `"kokoro"` | KEPT | VOICE-LOCK |
| `voice_kokoro` | `"af_kore"` | KEPT | Medhavy channel default |

### Datable claims in narration
None. All narration references are timeless mechanism claims from the source chapter (FDG mechanism, Warburg effect, false-positive/negative causes, "consistent with"/"confirms" clinical phrasing). No dated model names, prices, or "as of" phrasing.

### The one narration edit (TTS phonetic)
| Beat | Old | New | Rationale |
|------|-----|-----|-----------|
| B14 | `"Find the full course at medhavy.com."` | `"Find the full course at medhavy dot com."` | TTS phonetic — same substance, matches sibling `medhavy-vox-complexity-yield` narration; Kokoro reads the URL cleanly |

### Beat-level rebuilds

| Beat | Old shot | New shot | Reason |
|------|----------|----------|--------|
| B01 | CARD (unfilled) — "YOU → gen-AI clip → pantry" | REMOTION `FormACard` `{lines:[title, subtitle, "the signal is real — the cause is wrong"]}` | Punt costume; rendered as real title card |
| B02 | STILL src=ai (PET scan photo, no source) | REMOTION `FormACard` naming the tool + real-consequence framing | AI-still punt on cream ground; no PET scan photo asset exists in the reel; honest text substitute |
| B03 | CARD (unfilled) — "YOU → gen-AI clip → pantry" | REMOTION `FormACard` — the question | Punt costume; rendered as real question card |
| B04 | GRAPHIC `manim:B04_FDGUptake` (scene does not exist) | REMOTION `FormACard` — "FDG — fluorodeoxyglucose / a radioactive glucose analog / cells take it up · trap it inside · the camera counts decay" | No scenes_std.py; would fail lane-check |
| B05 | GRAPHIC `manim:B05_WhatPETSees` (scene does not exist) | REMOTION `FormACard` — "PET reads glucose metabolism / hexokinase activity · glucose-transporter expression / the Warburg effect — signal is real, not cancer itself" | Same — honest text substitute for the two-column proxy graphic |
| B06 | CARD w/ empty FormACard remotion (`lines: ["And glucose metabolism is not unique to cancer. Activated immune cells…"]` — narration-slice placeholder) | REMOTION `FormACard` — real headline + 3-cause list | The old lines value was a truncated narration slice, not authored content |
| B07 | DOCUMENT (unfilled quote) — "YOU → gen-AI clip → pantry" | REMOTION `FormACard` — false-negative tumor list + "a dark scan is not an empty scan" | Punt costume; the quote is retained inside `document{}` for a future editorial-quote scene |
| B08 | GRAPHIC `manim:B08_ImagingSuggests` (scene does not exist) | REMOTION `FormACard` — "Every imaging signal is a proxy. / 'consistent with' — never 'confirms' / imaging suggests · biopsy confirms" | No scenes on disk |
| B09 | STILL src=ai (case summary photo) | REMOTION `FormACard` — case setup written out | AI-still punt; no photo asset exists; substituted with a card carrying the setup |
| B10 | GRAPHIC `manim:B10_ExampleResult` (scene does not exist) | REMOTION `FormACard` — biopsy result written out, "illustrative" tag preserved | No scenes on disk |
| B11 | DOCUMENT (unfilled quote) — "YOU → gen-AI clip → pantry" | REMOTION `FormACard` — "The scanner was right. / The assumption was wrong. / high metabolism is what cancer tends to do" | Punt costume; the quote is retained inside `document{}` for a future editorial-quote scene |
| B12 | CARD (endcard) — "YOU → gen-AI clip → pantry" | REMOTION `FormACard` — endcard tagline (PET measures metabolism, not malignancy · imaging suggests · biopsy confirms · the gap is where you think carefully) | Punt costume; rendered as real endcard |
| B13 | OutroSeries `{seriesTitle, tagline, githubSlug}` (wrong schema — would Claude-wash) | OutroSeries `{eyebrow: "CANCER NANOMEDICINE", line: "Part of the Cancer Nanomedicine series on Medhavy AI."}` | Schema fix; Medhavy branding restored |
| B14 | OutroCTA `{authorName, handle, ctaText}` (wrong schema) | OutroCTA `{line: "Explore the full course at medhavy.com", handle: "@MedhavyAI"}` | Schema fix; Medhavy handle |

### Audio
Old Jul-16 mp3s + timings.json deleted. Fresh Kokoro `af_kore` mp3s generated for all 14 beats. Measured `actual_duration_s` written back into the sheet. Total 213.0s (with 1.0s tail-silence on B14).

### Renders
All 14 beats → `media/B*.mp4` via `remotion_scenes.py` (12× FormACard body + OutroSeries + OutroCTA). No `manim/` renders (no scenes on disk). No pantry/gen-AI clips.

## Not rebuilt (kept from pre-rebuild)

- Every narration line, verbatim (except the one B14 TTS-phonetic edit above).
- The `graphic.production_viz` intent blocks for B04/B05/B08/B10 (they document the visual a future Manim pass should draw).
- The `document.quote` blocks for B07/B11 (they document the editorial-quote scene a future pass should render).
- `card.copy`/`card.sub` on the CARD beats (kept as the shot-list intent alongside the new remotion.props).
- All shot-list identifiers (`new_visual_element`, `scene_description`, `image_prompt`, `chosen_media`).
- `style_bible`, `color_semantics`, `manim_move`, `accents`, `ground`, `isotype_mark`, `note`, `total_estimated_duration_seconds`.

## Scripting gaps flagged for a future pass

- B02 wants a real coronal PET scan photograph (STILL beat, human-supply — the only legitimate HOLD per nopunt catalog).
- B04 wants the FDG uptake mechanism animation (glucose flows in → trapped → gamma decay radiates).
- B05 wants the two-column "what you think vs what PET reads" graphic (crossed-out arrow, real path arrow).
- B08 wants the SIGNAL → PROXY → BIOLOGY chain with 'consistent with' / 'confirms' chips.
- B09 wants a real referral-note collage (STILL beat, human-supply).
- B10 wants the three-nodes reveal graphic (red uptake indicators → teal REACTIVE · URI labels).
- B07/B11 want the editorial-quote scene with gold highlighter sweeps ("dark", "assumption").

None of these blocks the current review cut — they upgrade it. The FormACard substitutes name what should be drawn.

# REBUILD-LOG — vox-fdg-proxy
_Rebuild pass: 2026-08-30 (filmloop, anthropics batch)_

Cohort A-built-stale reel per `_audit/REBUILD-WORKLIST.csv` — vox-editorial reel
on the @NikBearBrown channel; not Claude-washed.

## What was locked (carried verbatim)
- All body-beat `narration_text` (B01–B14) — no changes
- Beat order and act labels
- Card copy for B01 (title), B06 (section), B12 (endcard)
- All `graphic.production_viz` blocks (B04, B05, B08, B10) — Manim intent locked
- All `document` blocks (B07, B11) — quote + highlight intent locked
- Metadata identity: title, slug, topic, source, style_preset

## What was rebuilt / dropped

### Metadata — dead ElevenLabs-era fields DROPPED
| Field | Old value | New value |
|-------|-----------|-----------|
| `voice_id` | `"TyW6NH39JcFb5M3xdIIk"` | DROPPED |
| `clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | DROPPED |
| `channel` | — | `"@NikBearBrown"` |
| `folderLabel` | — | `"@NikBearBrown"` |
| `engine` | — | `"kokoro"` |
| `voice_kokoro` | — | `"am_onyx"` |

### Per-beat VOICE-LOCK fields ADDED
Every beat received `voice: "am_onyx"`, `engine: "kokoro"`, `voice_kokoro: "am_onyx"`.
Kokoro mp3s already existed (Jul 8, 2026, with measured `actual_duration_s`) — no
audio regen needed; the existing durations became the master clock.

### `shot.form` derived per beat (SHOT-FORM-SYSTEM.md)
| Beat | Form |
|------|------|
| B01, B02, B03, B06, B07, B09, B11, B12, B13, B14 | `slide-a` (text card / bookend) |
| B04, B05, B10 | `mechanism-plate` (Manim mechanism) |
| B08 | `flow-diagram` (SIGNAL → PROXY → BIOLOGY chain) |

### B02 punt authored — `STILL src=ai` → `CARD` (FormACard)
| Field | Old | New |
|-------|-----|-----|
| `shot.type` | `STILL` | `CARD` |
| `shot.source` | `ai` | `own` |
| `shot.motion` | `kenburns` | `hold` |
| `shot.remotion.props.lines` | `["FDG-PET is the standard tool for staging cancer and checking for…"]` (single truncated narration snippet with mid-sentence ellipsis) | `["FDG-PET stages cancer and checks for recurrence.", "Bright spots = tracer accumulation. Teams act on them daily."]` (two authored short lines compressed from the locked narration) |

Reason: nopunt catalog. The old spec asked for a Higgsfield-generated "printed PET
scan" clipping — a punt costume (`STILL src=ai` for a concept). The FormACard
fallback that shipped in `shot.remotion` had a lone truncated line with a mid-word
ellipsis — a card-lint violation. Real narration is preserved; the visual is now
an on-brand FormACard summary while the narration plays.

### B09 punt authored — `STILL src=ai` → `CARD` (FormACard)
| Field | Old | New |
|-------|-----|-----|
| `shot.type` | `STILL` | `CARD` |
| `shot.source` | `ai` | `own` |
| `shot.motion` | `kenburns` | `hold` |
| `shot.remotion.props.lines` | `["Here's an illustrative case. A 58-year-old patient — breast cancer surgery…"]` (single truncated narration snippet) | `["58-year-old patient. Breast cancer surgery three months prior.", "PET recurrence surveillance: three chest nodes flag for salvage radiation."]` |

Reason: same as B02 — a gen-AI "printed oncology referral note" for an ILLUSTRATIVE
case (no real patient) is a punt in a costume. Authored FormACard restates the
case setup while narration plays.

### B06 FormACard `lines` re-authored
| Field | Old | New |
|-------|-----|-----|
| `shot.remotion.props.lines` | `["And glucose metabolism is not unique to cancer. Activated immune cells…"]` (single truncated narration snippet) | `["Glucose metabolism is not unique to cancer.", "Immune cells, healing wounds, brown adipose tissue — all light up."]` |

### B03 section CARD tightened
| Field | Old | New |
|-------|-----|-----|
| `card.copy` | `"A PET scan is used to detect cancer. The tracer isn't looking for cancer cells. What is it actually measuring — and when does that difference matter?"` (143 chars — full narration as card copy) | `"What does a PET scan actually measure?"` |
| `card.sub` | `""` (empty) | `"the tracer isn't looking for cancer cells — and the gap matters"` |

Reason: rule 5 (card text) — the copy was a full-paragraph narration recital, not
a card label. Tightened to a section headline + real sub. Narration is unchanged.

### B13 OutroSeries — wrong props → correct schema
| Field | Old | New |
|-------|-----|-----|
| `props` | `{seriesTitle: "Cancer Nanomedicine", tagline: "", githubSlug: "cancer-nanomedicine"}` (wrong prop names) | `{eyebrow: "CANCER NANOMEDICINE", line: "Part of the Cancer Nanomedicine series."}` |

Reason: `OutroSeries` component (runtime/remotion/src/scenes/OutroSeries.tsx)
declares `{eyebrow, line}` in its zod schema. Old props defaulted the visual to
"Part of the Claude Cowork series." — a wrong-series bug caught in the first
compile QC frame.

### B14 OutroCTA — wrong props → correct schema
| Field | Old | New |
|-------|-----|-----|
| `props` | `{authorName: "Nik Bear Brown", handle: "@NikBearBrown", ctaText: "Like and subscribe for more."}` (wrong prop names) | `{line: "Like and subscribe for more.", handle: "@NikBearBrown"}` |

Reason: same shape — `OutroCTA` declares `{line, handle}`.

## Datable claims checked
No datable model names, versions, prices, or dated claims in the narration. The
one hedged clinical scenario (58-year-old patient, three lymph nodes, URI) is
LABELED illustrative in both the narration ("Here's an illustrative case…" /
"Numbers are illustrative.") and in the B10 production_viz (small mono
"(illustrative case)" note). No corrections needed.

## Files
- `beat_sheet.pre-rebuild.json` — byte-exact copy of old sheet, made first
- `beat_sheet.json` — rebuilt sheet (this pass)
- `vox_graphics.py` — copied in from `vox-emitter-range/` sibling so `vox_scenes.py`
  imports resolve (the upstream `vox/aspects/explainer/vox-explainer/manim/`
  toolkit path no longer exists on disk)
- `vox_scenes.py` — unchanged; 9 scenes rendered successfully (B01, B03, B04,
  B05, B07, B08, B10, B11, B12)

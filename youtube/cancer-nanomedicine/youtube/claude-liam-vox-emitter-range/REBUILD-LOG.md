# REBUILD-LOG — claude-liam-vox-emitter-range
_Rebuild pass: 2026-08-27_

## What was locked (carried verbatim)
- All narration_text in beats B01–B12 — no changes
- Beat order and act labels
- Shot intent / production_viz descriptions (B02–B06, B08–B09, B11)
- Metadata identity: title, slug, topic, source, register, channel

## What was rebuilt / dropped

### Metadata — dead ElevenLabs-era fields DROPPED
| Field | Old value | New value |
|-------|-----------|-----------|
| `voice_id` | `"TyW6NH39JcFb5M3xdIIk"` | DROPPED |
| `clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | DROPPED |

Fields `engine: "kokoro"` and `voice_kokoro: "am_onyx"` retained (already correct VOICE-LOCK values).

### B00 — spark line fixed
| Field | Old | New |
|-------|-----|-----|
| `props.greeting` | `"Liam"` | `"Ciao, Liam"` |

Reason: B00 requires a world-language hello + "Liam". "Ciao" (Italian) is distinct from adjacent reels in this series which all had bare "Liam".

### B01 — FormBCard placeholder → FormACard
| Field | Old | New |
|-------|-----|-----|
| `shot.remotion.pattern` | `FormBCard` | `FormACard` |
| `shot.remotion.props.items` | `["Key point one", "Key point two", "Key point three"]` with empty subs | Removed |
| `shot.remotion.props` | placeholder items array | `{lines: [...], sub: "...", dark: false}` |
| `lane` | `"BOOKEND"` | Removed (B01 is a body beat, not a bookend) |

Reason: B01 is an exec-summary hook card. FormBCard requires enumerated named items with icons; this beat has no such list. FormACard matches the locked `card.kind: "title"` intent. Items were placeholders ("Key point one") — a CHECK 5 violation.

### B04, B10, B12 — punt needs fields removed
| Beat | Field removed |
|------|---------------|
| B04 | `build.needs: "YOU → 5–10s gen-AI clip → pantry (as B04.mp4)"` |
| B04 | `build.suggested` |
| B10 | `build.needs: "YOU → 5–10s gen-AI clip → pantry (as B10.mp4)"` |
| B10 | `build.suggested` |
| B12 | `build.needs: "YOU → 5–10s gen-AI clip → pantry (as B12.mp4)"` |
| B12 | `build.suggested` |

Reason: B04/B10/B12 are legitimate CARD beats (question, section, endcard). The `needs` field was a punt tag; removing it leaves the shot.type=CARD intact. Content preserved.

### B07 — STILL/ai → GRAPHIC/Manim
| Field | Old | New |
|-------|-----|-----|
| `shot.type` | `STILL` | `GRAPHIC` |
| `shot.source` | `ai` | `own` |
| `shot.motion` | `kenburns` | `drawon` |
| `shot.remotion` | FormACard fallback | Removed |
| `shot.graphic.manim` | (none) | `B07_TumorGeometry` |
| `scene_description` | archival-photo-style description | Removed |
| `image_prompt` | gen-AI image prompt | Removed |
| `build.needs` | `"YOU → 5–10s gen-AI clip → pantry"` | `"PIPELINE → render animated_graphics.py scene B07_TumorGeometry"` |

Reason: A schematic cross-section of a heterogeneous tumor (receptor-positive rim, receptor-negative core) is fully animatable as a Manim diagram — it is a structure/boundary visualization. Per nopunt catalog, STILL src=archive/ai for animatable conceptual content is a PUNT. The production_viz in the new graphic block preserves the locked shot intent verbatim.

### B13 — OutroSeries → FormACard
| Field | Old | New |
|-------|-----|-----|
| `shot.remotion.pattern` | `OutroSeries` | `FormACard` |
| `shot.remotion.props` | `{seriesTitle, tagline, githubSlug}` | `{lines: ["Part of the Cancer Nanomedicine series."], dark: false}` |
| `build.status` | `VIDEO` (no media/ dir — false) | `SLATE` |

Reason: palette=claude; OutroSeries is not a claude-channel skin. Narration preserved. BOUT (ClaudeTitleOutro) is the canonical outro; B13 carries the series tag as a FormACard card.

### B14 — OutroCTA → FormACard
| Field | Old | New |
|-------|-----|-----|
| `shot.remotion.pattern` | `OutroCTA` | `FormACard` |
| `shot.remotion.props` | `{authorName, handle, ctaText}` | `{lines: ["Like and subscribe for more."], dark: false}` |
| `build.status` | `VIDEO` (no media/ dir — false) | `SLATE` |

Reason: palette=claude; OutroCTA is not a claude-channel skin. Build.skin_warnings already flagged this. Narration preserved.

### BVDT — verdict authored from body
Old `artifactLines`: `["Key finding one", "Key finding two", "Key finding three"]` (placeholder)
Old `narration_text`: `""` (empty)

New `artifactLines`:
1. "Alpha's 50–100 μm range is lethal per hit but confined to the bound cell."
2. "Beta's 1–2 mm crossfire reaches receptor-negative neighbors, crossing gaps the drug cannot."
3. "Heterogeneous 3 cm neuroendocrine tumor: Lu-177 (beta) ~78% vs Ac-225 (alpha) ~41% cell kill — illustrative."
4. "Geometry of target expression, not lethal force per hit, is the deciding variable."

New `narration_text`: "Alpha hits harder per cell. Beta's crossfire reaches farther. On a heterogeneous tumor — receptor-positive rim, receptor-negative core — Lu-177's one-to-two millimeter range crosses the gap that alpha's fifty micrometers cannot. The geometry of the tumor, read off a patient's scan, is what decides the emitter — not which particle shreds DNA more efficiently per hit."

Source: synthesized from locked narration of B02, B05–B06, B09, B11 (range values, crossfire mechanism, Lu-177/Ac-225 illustrative numbers).

### BHTF — scaffolded viewer task written
Old `command`: generic ("Take what you learned… apply it to your own work. What's one thing you'll try first?")
New `command`: real prompt + three-point rubric for checking the output (geometry not density, mm range named, answer scan-dependent).

## Datable claims checked
No datable model names, versions, prices, or "as of" phrasing found in locked narration. Numbers in B11 are labeled "illustrative" in the production_viz. No corrections needed.

## Files
- `beat_sheet.pre-rebuild.json` — byte-exact copy of old sheet, created first
- `beat_sheet.json` — rebuilt sheet (this pass)

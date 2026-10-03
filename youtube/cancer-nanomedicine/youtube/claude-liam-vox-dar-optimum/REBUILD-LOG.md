# REBUILD-LOG — claude-liam-vox-dar-optimum
_Rebuild pass: 2026-08-28_

## What was locked (carried verbatim)
- All narration_text in beats B01–B12 — no changes
- Beat order and act labels
- Shot intent / production_viz descriptions (B02, B04, B06, B07, B09, B10)
- Metadata identity: title, slug, topic, source, register, channel, note (with illustrative-number disclaimer)

## What was rebuilt / dropped

### Metadata — dead ElevenLabs-era fields DROPPED
| Field | Old value | New value |
|-------|-----------|-----------|
| `voice_id` | `"TyW6NH39JcFb5M3xdIIk"` | DROPPED |
| `clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | DROPPED |
| `build` (stale stamp) | `{at: 2026-07-16, cut: master, filled:2, of:14, slates:[B01…B12], skin_warnings:[B01,B14]}` | DROPPED (will restamp on this pass's compile) |

Fields `engine: "kokoro"` and `voice_kokoro: "am_onyx"` retained (already correct VOICE-LOCK values).

### B00 — spark line fixed
| Field | Old | New |
|-------|-----|-----|
| `props.greeting` | `"Liam"` | `"Szia, Liam"` |

Reason: B00 requires a world-language hello + "Liam". "Szia" (Hungarian) is unique across every other adjacent reel in this Cancer Nanomedicine batch — Ciao, Aloha, Sawubona, Guten tag, Kia ora, Hola, Salaam, Konnichiwa, Bonjour, Hej, Ni hao, Merhaba, Zdravo, Jambo, Namaste were all taken.

### B01 — FormBCard placeholder → FormACard
| Field | Old | New |
|-------|-----|-----|
| `shot.remotion.pattern` | `FormBCard` | `FormACard` |
| `shot.remotion.props.items` | `[{label:"Key point one",sub:""},{label:"Key point two",sub:""},{label:"Key point three",sub:""}]` | REMOVED |
| `shot.remotion.props` | placeholder items array | `{lines:["Load More Warheads on a Cancer Drug and It Gets Cleared Faster"], sub:"the DAR optimum, and what breaks past it", dark:false}` |
| `lane` | `"BOOKEND"` | REMOVED (B01 is a body beat, not a bookend) |

Reason: B01 is an exec-summary hook card. FormBCard requires enumerated named items with icons; this beat has no such list, and the three items were literal placeholder strings ("Key point one/two/three") that would be caught by content_check as PLACEHOLDER violations. FormACard matches the locked `card.kind: "title"` intent.

### B05 — STILL/ai → GRAPHIC/Manim
| Field | Old | New |
|-------|-----|-----|
| `shot.type` | `STILL` | `GRAPHIC` |
| `shot.source` | `ai` | `own` |
| `shot.motion` | `kenburns` | `drawon` |
| `shot.remotion` | FormACard fallback with truncated narration line | REMOVED |
| `graphic.manim` | (none) | `B05_UnderKill` |
| `graphic.production_viz` | (none) | authored (payload gauge below killing threshold) |
| `scene_description` | archival-photo-style description | REMOVED |
| `image_prompt` | gen-AI image prompt | REMOVED |
| `build.needs` | `"YOU → 5–10s gen-AI clip → pantry"` + `"suggested prompt: [STILL] cell survives — not enough payload"` | REMOVED (now a pipeline-owned Manim beat) |

Reason: "cell survives because payload below threshold" is a threshold/gauge concept — fully animatable per the nopunt catalog (Data & quantity → threshold / bracket marker). STILL src=ai for animatable conceptual content is a PUNT. The new production_viz preserves the locked narration's teaching (threshold + under-kill outcome).

### B03, B08, B10, B12 — punt `build.needs`/`build.suggested` removed
| Beat | Field removed |
|------|---------------|
| B03 | `build.needs: "YOU → 5–10s gen-AI clip → pantry (as B03.mp4)"` + `build.suggested` |
| B08 | `build.needs: "YOU → 5–10s gen-AI clip → pantry (as B08.mp4)"` + `build.suggested` |
| B11 | `build.needs: "YOU → 5–10s gen-AI clip → pantry (as B11.mp4)"` + `build.suggested` (converted to GRAPHIC — see below) |
| B12 | `build.needs: "YOU → 5–10s gen-AI clip → pantry (as B12.mp4)"` + `build.suggested` |

Reason: B03/B08/B12 are legitimate CARD beats (question / section / endcard) — their `card` blocks carry real, non-placeholder copy authored from the locked narration. The `needs` field was a punt tag; removing it leaves the shot.type=CARD intact.

### B11 — DOCUMENT → GRAPHIC/Manim
| Field | Old | New |
|-------|-----|-----|
| `shot.type` | `DOCUMENT` | `GRAPHIC` |
| `shot.motion` | `highlight` | `highlight` (retained) |
| `document` block | `{quote:"DAR-4: 2.4 ug/g tumor · DAR-8: 0.3 ug/g tumor at 72 hours.", attribution:"— illustrative example …", highlight_words:"0.3", highlighter:"#F5D061"}` | folded into `graphic.production_viz.mechanic` |
| `graphic.manim` | (none) | `B11_TumorQuote` |
| `graphic.production_viz` | (none) | authored (serif quote + gold highlight on "0.3" + italic attribution) |
| `build.needs`/`build.suggested` | punt tags | REMOVED |

Reason: A quote card with a gold highlight is fully animatable as a Manim GRAPHIC (nopunt catalog: Text-with-highlight → drawn on cue). DOCUMENT type with no filled slot was a punt costume. Quote content and highlight semantics preserved verbatim.

### B13 — OutroSeries → FormACard
| Field | Old | New |
|-------|-----|-----|
| `shot.remotion.pattern` | `OutroSeries` | `FormACard` |
| `shot.remotion.props` | `{seriesTitle:"Cancer Nanomedicine", tagline:"", githubSlug:"cancer-nanomedicine"}` | `{lines:["Part of the Cancer Nanomedicine series."], dark:false}` |
| `build.status` | `VIDEO` (falsely stamped — no media/B13.mp4 exists) | `SLATE` |

Reason: palette=claude; OutroSeries is a non-claude channel skin. Narration preserved. BOUT (ClaudeTitleOutro) is the canonical outro; B13 carries the series tag as a FormACard card.

### B14 — OutroCTA → FormACard
| Field | Old | New |
|-------|-----|-----|
| `shot.remotion.pattern` | `OutroCTA` | `FormACard` |
| `shot.remotion.props` | `{authorName:"Nik Bear Brown", handle:"@NikBearBrown", ctaText:"Like and subscribe for more."}` | `{lines:["Like and subscribe for more."], dark:false}` |
| `build.status` | `VIDEO` (falsely stamped — no media/B14.mp4 exists) | `SLATE` |

Reason: palette=claude; OutroCTA is a non-claude channel skin. Prior build.skin_warnings already flagged this. Narration preserved.

### BVDT — verdict authored from body
Old `artifactLines`: `["Key finding one", "Key finding two", "Key finding three"]` (placeholder — CHECK 4 violation, would be flagged by verdict_audit)
Old `narration_text`: `""` (empty — no audio would exist)
Old `artifactTitle`: `"Load More Warheads on a Cancer Drug and It Gets Cleared Faster"` (would rasterize truncated at 60 chars)

New `artifactTitle`: `"DAR: An Optimum, Not a Maximum"` (30 chars — fits display safe area).

New `artifactLines`:
1. "Cytotoxic payloads are hydrophobic — past DAR ~4–8 the conjugate aggregates."
2. "Liver and immune system clear aggregated ADCs in hours, not days."
3. "Illustrative DAR-4 vs DAR-8: 68% vs 11% plasma at 24h; 2.4 vs 0.3 μg/g tumor at 72h."
4. "DAR is an optimum, not a maximum: more warheads means less delivery past the sweet spot."

New `narration_text`: "Cytotoxic drug molecules are hydrophobic. Past four to eight warheads per antibody the conjugate aggregates, and the liver and immune system clear those aggregates in hours. In an illustrative comparison, DAR-four keeps sixty-eight percent of its plasma level at twenty-four hours and delivers two-point-four micrograms per gram of tumor at seventy-two hours. DAR-eight: eleven percent, then zero-point-three. The higher-payload molecule delivered less drug where it needed to go. DAR is an optimum, not a maximum."

Source: synthesized from locked narration of B04 (DAR sweet-spot range), B06 (hydrophobic → aggregation), B07 (liver/immune clearance in hours), B09 (optimum curve, both failure modes), B10 (24h illustrative plasma), B11 (72h illustrative tumor concentration), B12 (optimum-not-maximum aphorism). Every number is labeled illustrative in the source and remains so here.

### BHTF — scaffolded viewer task written
Old `command`: `"Take what you learned from [Load More Warheads on a Cancer Drug and It Gets Cleared Faster] and apply it to your own work. What's one thing you'll try first?"` (generic — no rubric)

New `command`: real prompt + three-point rubric — asks the viewer to look up a specific ADC's DAR value, hydrophobicity/conjugation link, and clearance timescale. Meets the nopunt SKILL "scaffolded viewer task" bar: a real prompt AND a checklist for evaluating the output.

### BOUT — title shortened
| Field | Old | New |
|-------|-----|-----|
| `props.title` | `"Load More Warheads on a Cancer Drug and It Gets Cleared Faster"` | `"DAR: An Optimum, Not a Maximum"` |
| `props.slug` | `"vox-dar-optimum"` | unchanged |

Reason: ClaudeTitleOutro rasterizes long titles truncated; 30 chars fits safely.

## Datable claims checked
No datable model names, versions, prices, or "as of" phrasing found in locked narration. All DAR-related numbers (DAR-4/DAR-8, 68%, 11%, 2.4 μg/g, 0.3 μg/g, 24h, 72h, "three mice") are labeled illustrative in metadata.note and in B10/B11 narration. Kept verbatim.

## Files
- `beat_sheet.pre-rebuild.json` — byte-exact copy of old sheet, made first
- `beat_sheet.json` — rebuilt sheet (this pass)
- `scenes_std.py` — Manim scenes for B02, B04, B05, B06, B07, B09, B10, B11 (new file)

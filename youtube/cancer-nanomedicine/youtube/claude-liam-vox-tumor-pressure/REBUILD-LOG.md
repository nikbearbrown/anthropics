# REBUILD-LOG — claude-liam-vox-tumor-pressure
_Rebuild pass: 2026-08-28_

## What was locked (carried verbatim)
- All narration_text in beats B01–B11 — no changes
- Beat order and act labels
- Shot intent per beat: pattern/props/production_viz descriptions preserved or re-expressed
- Metadata identity: title, slug, topic, source, register, channel
- Kokoro voice envelope (`engine: kokoro`, `voice_kokoro: am_onyx`) — was already correct

## What was rebuilt / dropped

### Metadata — dead ElevenLabs-era fields DROPPED
| Field | Old value | New value |
|-------|-----------|-----------|
| `voice_id` | `"TyW6NH39JcFb5M3xdIIk"` | DROPPED |
| `metadata.build` | old post-compile stamp with 11-slate warning | DROPPED (fresh compile will re-stamp) |

Also added `isotype_mark`, `accents`, `ground`, `source` fields to bring metadata envelope in line with the sibling rebuilt reels (vox-emitter-range). No content change.

### B00 — spark line fixed
| Field | Old | New |
|-------|-----|-----|
| `props.greeting` | `"Liam"` | `"Merhaba, Liam"` |

Reason: B00 requires a world-language hello + "Liam". Turkish "Merhaba" is unused by any adjacent reel in this cancer-nanomedicine batch (surveyed all sibling B00 greetings — used hellos include Namaste, Jambo, Sawubona, Hola, Salaam, Ciao, Konnichiwa, Bonjour, Hej, Olá, Vanakkam, Kia ora, Ni hao).

### B01 — FormBCard placeholder → FormACard (title)
| Field | Old | New |
|-------|-----|-----|
| `shot.remotion.pattern` | `FormBCard` | `FormACard` |
| `shot.remotion.props.items` | `[{label:"Key point one",sub:""}, {label:"Key point two",sub:""}, {label:"Key point three",sub:""}]` | Removed |
| `shot.remotion.props` | placeholder items array | `{lines: ["Why the Drug…"], sub: "the outward-pressure paradox…", dark: false}` |
| `lane` | `"BOOKEND"` | Removed (B01 is a body beat, not a bookend) |
| `act` | `"COLD OPEN"` | `"I — exec summary"` |
| `scene_class` | `"B01_Title"` | Removed |

Reason: B01 is the exec-summary hook card. `FormBCard` requires enumerated named items with icons; this beat has no such list, and the items were placeholders ("Key point one/two/three" — a CHECK 5 violation). `FormACard` matches the card.kind: "title" intent. Card block added mirroring reference reel structure.

### B02 — STILL/ai gen-AI punt → GRAPHIC/Manim
| Field | Old | New |
|-------|-----|-----|
| `shot.type` | `STILL` | `GRAPHIC` |
| `shot.source` | `ai` | `own` |
| `shot.motion` | `kenburns` | `drawon` |
| `shot.image_description` | archival MRI slice description | Removed |
| `shot.remotion` | `FormACard` with truncated `["MRI shows a two-millimeter viable core at week three. The drug…"]` line | Removed |
| `graphic.manim` | (none) | `B02_MRICore` |
| `build.needs` | `"YOU → 5–10s gen-AI clip → pantry (as B02.mp4)"` | Removed (SLATE, no punt costume) |
| `build.suggested` | gen-AI prompt suggestion | Removed |

Reason: An MRI-like schematic of a tumor cross-section (dark drug-killed rim, viable central core with annotation ring) is fully animatable as a Manim structural diagram — per the nopunt catalog, `STILL src=ai` for conceptual content is a PUNT costume, and a FormACard with a truncated narration line naming a visual is a second punt costume ("FormA card whose narration names a visual it never draws"). Both removed. Scripting the diagram is authored in `scenes_std.py`.

### B03 — CARD kept
`shot.type: CARD` preserved (it re-states the setup as a question). Removed the gen-AI `build.needs`/`build.suggested` fields (punt tag). Added a `card` block with a real `copy` and `sub` derived from the locked narration ("Why did the core survive?").

### B04, B05, B06, B07, B08, B10 — GRAPHIC beats, gen-AI punt tag stripped
All six body beats were `shot.type: GRAPHIC` (correct intent) but marked SLATE with a `build.needs: "YOU → 5–10s gen-AI clip → pantry"` punt costume. The `needs`/`suggested` fields are removed. Each beat gets a `graphic` block with:
- `manim`: the scene name to render (B04_NaivePicture, B05_PressureBuilds, B06_OutwardFlow, B07_ParticlesPushedBack, B08_HypoxicCore, B10_Example)
- `production_viz`: label, mechanic (drawn description), colors, note — locked shot intent

None of these are punts any more: each is a specific Manim diagram in the nopunt catalog rows (leaky-vessel structure, pressure gauge + arrows, cross-section, two-panel timeline).

### B09 — DOCUMENT/highlight → GRAPHIC highlight-quote
| Field | Old | New |
|-------|-----|-----|
| `shot.type` | `DOCUMENT` | `GRAPHIC` |
| `shot.motion` | `highlight` | `hold` |
| `graphic.manim` | (none) | `B09_InsideOutQuote` |

Reason: The beat is a memorable quote highlighted with a gold bar under "core cells it never reached." A Manim scene renders the quote as an editorial card with a gold highlighter bar (the newsprint palette's single editor's-pen accent).

### B11 — CARD (recap) kept
`shot.type: CARD` preserved. Removed the gen-AI `build.needs`/`build.suggested` fields. Added a `card` block with `copy: "The accumulation was real. The delivery was not."` and a `sub` derived from the locked narration.

### B12 — OutroSeries → FormACard
| Field | Old | New |
|-------|-----|-----|
| `shot.remotion.pattern` | `OutroSeries` | `FormACard` |
| `shot.remotion.props` | `{seriesTitle, tagline, githubSlug}` | `{lines: ["Part of the Cancer Nanomedicine series."], dark: false}` |
| `build.status` | `VIDEO` (no media/ existed — false stamp) | `SLATE` (will be re-rendered) |

Reason: palette=claude. OutroSeries is not a claude-channel skin. Build stamp was falsely VIDEO — no `media/` directory existed. Follows the reference reel (vox-emitter-range) rebuild pattern.

### B13 — OutroCTA → FormACard
| Field | Old | New |
|-------|-----|-----|
| `shot.remotion.pattern` | `OutroCTA` | `FormACard` |
| `shot.remotion.props` | `{authorName, handle, ctaText}` | `{lines: ["Like and subscribe for more."], dark: false}` |
| `build.status` | `VIDEO` (no media/ existed) | `SLATE` |

Reason: build.skin_warnings in the pre-rebuild sheet already flagged this. OutroCTA is not a claude-channel skin. BOUT (`ClaudeTitleOutro`) is the canonical claude outro.

### BVDT — verdict authored from body
Old `artifactLines`: `["Key finding one", "Key finding two", "Key finding three"]` (placeholder — verdict_audit fail)
Old `narration_text`: `""` (empty)

New `artifactTitle`: `"Accumulation Is Not Delivery"` (was "Why the Drug Reached the Tumor and the Tumor Still Grew Back" — too long for the artifact card)
New `artifactHeading`: `"The outward-pressure mechanism"` (was `"Key findings"` — placeholder per verdict_audit)
New `artifactLines` (5):
1. "Leaky vessels + broken lymphatics build core interstitial pressure 5–10× normal."
2. "Net flow is outward — particles that extravasate get carried back to the rim."
3. "The unreached hypoxic core selects for stress-tolerant, drug-resistant cells."
4. "Rim shrinks ~60%; core IFP 25 vs rim 5 mmHg; tumor doubles by week 8 from the core."
5. "The drug arrived. The delivery failed. Accumulation is not delivery."

New `narration_text`: "The drug reached the tumor and the delivery still failed. Leaky vessels flood the interstitium; broken lymphatics cannot drain it; core pressure runs five to ten times normal, and net flow is outward. Particles pile at the rim. The unreached hypoxic core selects for the tumor's most resistant cells, and grows back. Accumulation is not delivery."

Source: synthesized from locked narration of B05 (leaky + broken lymphatics), B06 (pressure 5–10×, outward flow), B07 (particle pile-up at rim), B08 (hypoxic core selects for resistant cells), B10 (rim −60%, IFP 25 vs 5 mmHg, tumor doubles by week 8).

### BHTF — scaffolded viewer task authored
Old `command`: generic template ("Take what you learned from [Why the Drug…] and apply it to your own work. What's one thing you'll try first?")
New `command`: real prompt + three-point rubric — "Pick a nanomedicine result you trust. Ask Claude: 'What is the interstitial fluid pressure profile of this tumor type, and does the reported particle distribution differentiate rim accumulation from core delivery?' Check: (1) did Claude give an IFP range in mmHg, not just 'elevated'? (2) did it distinguish tumor rim from core in the accumulation data? (3) did it name lymphatic dysfunction as the driver of the pressure gradient?"

### BOUT — ClaudeTitleOutro title shortened
`title` was `"Why the Drug Reached the Tumor and the Tumor Still Grew Back"` (57 chars — clips in type_check). New: `"Accumulation Is Not Delivery"` (28 chars). Slug preserved.

## Datable claims checked
No datable model names, versions, prices, or "as of" phrasing found in locked narration. Numbers in B06 (5–10× pressure), B10 (60% shrink, 25/5 mmHg, week 3/week 8, tumor doubles) are labeled as "illustrative scenario" in the production_viz for B10 and are qualitative-with-range in B06. No corrections needed.

## Files
- `beat_sheet.pre-rebuild.json` — byte-exact copy of old sheet, created first (2026-08-28)
- `beat_sheet.json` — rebuilt sheet (this pass)
- `scenes_std.py` — Manim scenes for B02, B04–B10 (authored this pass)
- `AUDIT.md` — Phase 1 audit log

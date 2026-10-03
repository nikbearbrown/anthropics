# REBUILD-LOG — claude-liam-vox-abraxane-solvent
_Rebuild pass: 2026-08-28_

## What was locked (carried verbatim)
- All body-beat `narration_text` (B01–B15) — no changes
- Beat order and act labels
- Shot INTENT / production_viz descriptions (B03, B05, B07, B08, B09, B11, B13, B14)
- Metadata identity: title, slug, topic, source, register, channel

## What was rebuilt / dropped

### Metadata — dead ElevenLabs-era fields DROPPED
| Field | Old value | New value |
|-------|-----------|-----------|
| `voice_id` | `"TyW6NH39JcFb5M3xdIIk"` | DROPPED |
| `clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | DROPPED |
| `_variant_todo` | 4-item TODO list | DROPPED (variants already generated) |
| `build` block | stale July build stamp (2 filled, 15 slates) | DROPPED (compile.py rewrites it) |

Fields `engine: "kokoro"` and `voice_kokoro: "am_onyx"` retained (already correct VOICE-LOCK values).

### B00 — spark line fixed + segment shortened
| Field | Old | New |
|-------|-----|-----|
| `props.greeting` | `"Liam"` | `"Aloha, Liam."` |
| `props.segment` | `"The Cancer Drug Where the Solvent, Not…"` (truncated with ellipsis) | `"Solvent, Not Drug"` |

Reason: B00 requires a world-language hello + "Liam". "Aloha" (Hawaiian) is distinct from adjacent claude-liam reels (Ciao, Bonjour, Konnichiwa, Namaste, Sawubona, Salaam, Hej, Merhaba, Jambo, Hola). Wagwan is Bear's, never Liam's. `segment` was a mid-word truncation ("Not…") — replaced with the shortened idea.

### B01 — FormBCard placeholder → FormACard
| Field | Old | New |
|-------|-----|-----|
| `shot.remotion.pattern` | `FormBCard` | `FormACard` |
| `shot.remotion.props.items` | `[{label:"Key point one", sub:""}, {label:"Key point two", sub:""}, {label:"Key point three", sub:""}]` (placeholder) | Removed |
| `shot.remotion.props` | placeholder items array | `{lines: [...], dark: false}` — two lines derived from locked narration |
| `lane` | `"BOOKEND"` | Removed (B01 is a body beat) |

New `lines`:
1. "The drug in the bag worked against cancer for decades."
2. "The real danger was not the drug — it was the solvent it was dissolved in."

Reason: FormBCard needs enumerated named items with icons; this beat has none. Its narration is a two-beat opener. The placeholder subs are a hard CHECK 5 violation.

### B02 — STILL/ai (gen-AI clip PUNT) → GRAPHIC/Manim
| Field | Old | New |
|-------|-----|-----|
| `shot.type` | `STILL` | `GRAPHIC` |
| `shot.source` | `ai` | `own` |
| `shot.motion` | `kenburns` | `drawon` |
| `shot.remotion` (FormACard fallback with `lines[0]` truncated to "…") | present | Removed |
| `graphic.manim` | (none) | `B02_PaclitaxelMechanism` |
| `scene_description`, `image_prompt` | archival-photo prose | Removed |
| `build.needs`/`suggested` | "YOU → 5–10s gen-AI clip → pantry" | Removed |

New production_viz: mitotic spindle drawn on a cell; INK paclitaxel squares dock onto it; the spindle FREEZES; a TEAL "Division halted" chip.

Reason: nurse-at-bedside archival still is a punt for a claim about the drug's MECHANISM (freezing division). A conceptual/mechanical animation earns the beat. The lone-line "…"-truncated FormACard fallback was itself a card-lint violation.

### B03, B05, B07, B08, B09, B11, B13, B14 — punt `needs`/`suggested` cleaned
`build.needs` = "PIPELINE → render animated_graphics.py scene B0*_*" and `build.suggested` removed from all GRAPHIC beats. The `production_viz` block is the rendering contract; the pipeline field was legacy stamping.

### B04 — punt `needs` removed (CARD is legitimate)
`build.needs`: "YOU → 5–10s gen-AI clip → pantry (as B04.mp4)" → removed. `shot.type: "CARD"` (question card) is legitimate for the beat's rhetorical function ("What did — and why did the reactions stop?"). Added `card.sub`: "the question this reel answers" (was empty).

### B06 — punt `needs` removed
`build.needs`: "YOU → 5–10s gen-AI clip → pantry (as B06.mp4)" → removed. `shot.type: "DOCUMENT"` (quote card) is legitimate — the Taxol infusion protocol as a highlighted document.

### B09 — chart-text fix
`graphic.production_viz.label`: `"hypersensitivity rate: Taxol vs Abraxane"` (long, narration-style) → `"HYPERSENSITIVITY RATE"` (short category noun). Bar labels are 1-word category nouns ("Taxol", "Abraxane"). Footer is one complete sentence ("Illustrative comparison — order of magnitude, not clinical trial data."). Bar heights match narration meaning (TAXOL taller).

### B10 — STILL/ai (gen-AI clip PUNT) → GRAPHIC/Manim
| Field | Old | New |
|-------|-----|-----|
| `shot.type` | `STILL` | `GRAPHIC` |
| `shot.source` | `ai` | `own` |
| `shot.motion` | `kenburns` | `drawon` |
| `shot.remotion` (FormACard fallback with truncated `lines[0]`) | present | Removed |
| `graphic.manim` | (none) | `B10_TwoBagsSetup` |
| `scene_description`, `image_prompt` | archival prose | Removed |
| `build.needs`/`suggested` | "YOU → 5–10s gen-AI clip → pantry" | Removed |

New production_viz: two IV bag isotypes on a shelf line; Bag A (Taxol/CRIMSON) detailed with icons; Bag B (Abraxane/TEAL) still sparse (fills in at B11).

Reason: this is the visual SETUP for the two-bag comparison across B10/B11/B14 — a real diagram, not archival photography.

### B12 — punt `needs` removed
`build.needs` removed. `shot.type: "CARD"` (section card, "A formulation fix — not a tumor-targeting story") is legitimate. Added `card.sub`: "the primary benefit lives in the IV bag, not the tumor".

### B15 — punt `needs` removed
`build.needs` removed. `shot.type: "CARD"` (endcard) is legitimate.

### B16 — OutroSeries → FormACard
| Field | Old | New |
|-------|-----|-----|
| `shot.remotion.pattern` | `OutroSeries` | `FormACard` |
| `shot.remotion.props` | `{seriesTitle, tagline:"", githubSlug}` | `{lines: ["Part of the Cancer Nanomedicine series."], dark: false}` |
| `shot.remotion.provenance` | (none) | `proven-core/FormACard` |
| `build.status` | `VIDEO` (no media/ dir — false) | `SLATE` |

Reason: palette=claude. OutroSeries is not a claude-channel skin. Narration preserved. BOUT (ClaudeTitleOutro) is the canonical outro; B16 carries the series tag as a FormACard.

### B17 — OutroCTA → FormACard
Same treatment as B16 — pattern → FormACard, `build.status: VIDEO` → `SLATE` (no media/ dir existed at rebuild start). Narration preserved.

### BVDT — verdict authored from body
Old `artifactLines`: `["Key finding one", "Key finding two", "Key finding three"]` (placeholder)
Old `narration_text`: `""` (empty)

New `artifactTitle`: `"Solvent, Not Drug, Was the Danger"` (33 chars, safe below 60-char lint).

New `artifactLines` (4 lines, drawn from body B03/B05/B06/B07/B09/B11/B12):
1. "Cremophor EL — not paclitaxel — triggered the bronchospasm and hypotension that shadowed Taxol."
2. "Albumin replaced the solvent; the drug molecule is identical in Taxol and Abraxane."
3. "Hypersensitivity: ~10% (Taxol) → <1% (Abraxane); infusion: 3 h with premeds → 30 min without."
4. "Abraxane's undisputed benefit is a formulation fix, not tumor targeting."

New `narration_text`: "The drug never changed. The solvent did. Cremophor EL — a castor-oil surfactant used to dissolve paclitaxel — was the trigger for the bronchospasm and hypotension that shadowed Taxol infusions for decades. Abraxane replaced the solvent with albumin, the body's own carrier protein. Hypersensitivity dropped from roughly ten percent to under one percent, and a three-hour premedicated drip became a thirty-minute infusion. Abraxane's benefit is not tumor targeting. It is a pure formulation fix."

`estimated_duration_s`: 20 → 30 (accommodate the authored 5-sentence recap).

Source: synthesized from locked narration of B03 (Cremophor EL as solvent), B05 (mast cell / bronchospasm / hypotension), B06 (3-hour premedicated infusion), B07 (albumin as carrier), B09 (~10% → <1%; 3 h → 30 min), B12 (formulation fix vs tumor targeting).

### BHTF — scaffolded viewer task written
Old `command`: generic ("Take what you learned from [...] and apply it to your own work. What's one thing you'll try first?")
New `command`: "Pick one drug you use or prescribe. Ask: is the hazard the active ingredient, or the vehicle, buffer, or excipient it rides in? Name the vehicle. Name the reaction it can cause. Name the test that would tell you the vehicle is the problem, not the drug."

Reason: the new prompt is domain-tied and asks the viewer to run the same "artifact / world / relationship" move on their own drug (Plato lens applied).

### BOUT — title shortened
`props.title`: `"The Cancer Drug Where the Solvent, Not the Drug, Was the Danger"` (63 chars — hits 60-char one-line lint) → `"Solvent, Not Drug, Was the Danger"` (33 chars).

## Datable claims checked
No datable model names, versions, prices, or "as of" phrasing in the locked narration. The one hedged number ("roughly ten percent" → "<1%", B09/B14) is labeled ILLUSTRATIVE in `production_viz` and hedged in narration. No corrections needed.

## Files
- `beat_sheet.pre-rebuild.json` — byte-exact copy of old sheet, created first
- `beat_sheet.json` — rebuilt sheet (this pass)
- `scenes_std.py` — Manim scenes for B02, B03, B05, B07, B08, B09, B10, B11, B13, B14

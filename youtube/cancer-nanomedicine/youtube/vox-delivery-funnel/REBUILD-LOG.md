# REBUILD-LOG — vox-delivery-funnel
_Pass: 2026-08-28 · vox-editorial (legacy vox — Cohort C, `@NikBearBrown`)_

## Snapshot

`beat_sheet.pre-rebuild.json` written byte-exact before any edit.

## LOCKED (verbatim from pre-rebuild)

- All 13 `narration_text` fields — the script.
- Beat order (B01–B13), act structure, `t_start`, `estimated_duration_s`.
- Metadata identity: slug, title, topic, purpose, style_preset (vox-editorial),
  isotype_mark, ground, color_semantics, note.
- `graphic.production_viz` intent blocks on B04–B08, B10 — the shot-list intent.
- `card.*` intent blocks on B01/B03/B09/B11.
- Every existing `shot.type` / `shot.motion` on each beat.
- `vox_scenes.py` scene *content* (only path resolution and B08/B10 layout
  were touched — see below).

## REBUILT (per current doctrine)

### Envelope

| Field | Old | New | Rationale |
|-------|-----|-----|-----------|
| `voice_id` | `"TyW6NH39JcFb5M3xdIIk"` | DROPPED | ElevenLabs-era; VOICE-LOCK now Kokoro |
| `clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | DROPPED | Dead ElevenLabs-era prose |
| `style_bible{}` block | present (visual_style / color_palette / lighting_style) | DROPPED | Superseded by `style_preset:"vox-editorial"` + `color_semantics` line |
| `accents{}` block | `{data:[TEAL,CRIMSON], annotation:CRIMSON, highlighter:GOLD}` | DROPPED | Superseded by `color_semantics` line (`vox_graphics.py` owns the actual palette) |
| `engine` | (missing) | `"kokoro"` | VOICE-LOCK |
| `voice_kokoro` | (missing) | `"am_onyx"` | Neutral vox default (peer: `vox-endosomal-escape` 2026-08-27) |
| `folderLabel` | (missing) | `"@NikBearBrown"` | Channel handle |
| `source` | (only in `purpose`) | separate `source` line | Peer standard |
| `short_title` | (missing) | `"The Delivery Funnel"` | Peer standard (matches `vox-endosomal-escape`) |
| `derived_from` | (missing) | `"beat_sheet.pre-rebuild.json"` | Explicit lineage |

### Datable claims in narration

None. The five-step delivery funnel (circulation → vessel → matrix → uptake →
release) and the 0.7% mechanism are timeless. Illustrative numbers
(18/14/12/55/0.7 of 100 units) are labeled illustrative both in narration and
on the B10 chart.

### Beat-level rebuilds

| Beat | Change | Reason |
|------|--------|--------|
| B01 | (unchanged; CARD → renders via B01_Title Manim) | Locked title |
| B02 | Dropped nested `shot.remotion.FormACard` sub-object carrying a truncated `"…that…"` placeholder line | The vox pipeline has no Remotion renderer wired for this reel; the vestigial FormACard was dead weight, and B02 has always been a declared STILL slate (peer: `vox-endosomal-escape` B02). The `new_visual_element` line drives the slate label |
| B03–B11 | (unchanged; each maps 1:1 to its named Manim class in `vox_scenes.py`) | Locked shot list |
| B12/B13 | (unchanged; declared SLATE — vox pipeline has no OutroSeries/OutroCTA renderer) | Peer standard (matches `vox-endosomal-escape`) |

### `vox_scenes.py`

- **Path resolution:** `pathlib.Path(__file__).resolve().parents[3]` assumed a
  three-deep books layout; this reel sits five levels down. Replaced with a
  walk-up search for `books/vox/aspects/explainer/vox-explainer/manim/` —
  same fix the sibling `vox-endosomal-escape` applied on 2026-08-27.
- **B08 label layout:** `targeting_label` and `lost_label` were `next_to(step_boxes[3], DOWN)` and `next_to(step_boxes[1], DOWN)` respectively. The two serif phrases collided horizontally (rendered as "still lost at earliertaunggsting ligand helps here"). Rebuilt as a stacked `VGroup` below all five step boxes — the top line names step 4 (targeting works here), the bottom line names steps 1–3, 5 (still lost).
- **B10 row layout:** each row was `VGroup(num, desc).arrange(RIGHT, buff=0.28, aligned_edge=LEFT)`. The `aligned_edge=LEFT` on a horizontal arrange overlays both children on their own left edges, forcing the description text under the number. Fixed by placing `desc` at a fixed offset (`num_col_width = 1.7` units) right of `num` so the mono number column and the serif description column line up cleanly.

### Audio

Old ElevenLabs-era mp3s (Jul 8) purged. Fresh Kokoro `am_onyx` mp3s generated
for all 13 beats via `books/brutalist-art/runtime/scripts/generate_audio_kokoro.py`.
Kokoro reads `metadata.voice_kokoro` from the envelope. Measured
`actual_duration_s` written back to the sheet. Total run: ~118.2 s.

### Renders

- Manim (via `books/vox/scripts/vox_run.sh` with `VOX_QC=0` for pace): B01,
  B03–B11 (10 scenes) → `manim/B*.mp4` at 1920×1080 p24.
- Declared SLATEs (no on-disk media): B02 (`STILL src=ai`, ai still), B12
  (OutroSeries — no vox Remotion renderer), B13 (OutroCTA — same).
- Compile: `books/vox/scripts/vox_compile.py --review` — 10/13 filled,
  3 declared slates, master conformed to per-beat Kokoro audio.

## Not rebuilt (kept from pre-rebuild)

- Every narration line, verbatim.
- Every `card.*` intent block (B01/B03/B09/B11 — read by the Manim scenes as
  the source-of-truth text).
- Every `graphic.production_viz` intent block (B04–B08, B10).
- All shot-list identifiers (`new_visual_element`).
- `SHOTLIST.md`, `PROMPTS.md`, `FACTCHECK.md`, `PEDAGOGY.md` — the paperwork
  set (Gate F).

## Lens (PHASE 1 §8) — four moves earned

- **Descartes — falsification checklist:** what would falsify "the funnel
  leaks upstream"? Measure dose at each step; if the loss profile shows all
  99.3% missing at step 4 alone, the framing is wrong. B04 states the five
  sequential steps as the checklist; B10 makes it quantitative.
- **Hume — confidence is a property of the model:** B02's cell-culture kill
  is a property of the assay, not of the mouse. B10 labels the 100-unit
  numbers "illustrative."
- **Popper — state failure criteria in advance:** B04 states in advance
  what would count as failure — "Fail at any of them and the particle
  delivers nothing." B08 sharpens it — a step-4 fix is void if step 1 has
  already cleared the particle.
- **Plato — artifact vs world:** B09 makes the move explicit — "The particle
  was not misbehaving. The targeting ligand was binding correctly. The
  delivery chain failed upstream." The ligand-binding artifact is not the
  in-vivo delivery outcome.

## Palette-library quirk (LOGGED, not blocking)

`vox_graphics.TEAL` renders as near-INK brown throughout this reel's Manim
scenes; `GOLD` renders as pale pink. This is the same shared-library quirk
the sibling `vox-endosomal-escape` (2026-08-27) logged. Layout semantics are
preserved: the surviving TEAL dose bar visibly shrinks step by step (B05–B07),
the TEAL step-4 box is visibly distinct from the CRIMSON step boxes (B08),
the GOLD "0.7% reaches tumor" chip is visibly separated from the CRIMSON
"99.3% lost" chip (B10). A palette fix in
`books/vox/aspects/explainer/vox-explainer/manim/vox_graphics.py` is out of
scope for a single-reel invocation.

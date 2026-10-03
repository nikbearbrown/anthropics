# REBUILD-LOG — vox-dar-optimum
_Pass: 2026-08-28 · vox-editorial (legacy vox — Cohort C, `@NikBearBrown`)_

## Snapshot

`beat_sheet.pre-rebuild.json` written byte-exact before any edit.

## LOCKED (verbatim from pre-rebuild)

- All 14 `narration_text` fields — the script.
- Beat order (B01–B14), `t_start`, `estimated_duration_s`.
- Metadata identity: slug, title, topic, purpose, style_preset (vox-editorial),
  isotype_mark, ground, color_semantics, note, aspect_ratio.
- `graphic.production_viz` intent blocks on B02/B04/B06/B07/B09/B10 — the shot-list intent.
- `card.*` intent blocks on B01/B03/B08/B12.
- `document` block on B11.
- Every existing `shot.type` / `shot.motion` on each beat.
- `vox_scenes.py` scene *content* — only path resolution and three scoped
  layout/rewrite fixes (see below).

## REBUILT (per current doctrine)

### Envelope

| Field | Old | New | Rationale |
|-------|-----|-----|-----------|
| `voice_id` | `"TyW6NH39JcFb5M3xdIIk"` | DROPPED | ElevenLabs-era; VOICE-LOCK now Kokoro |
| `clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | DROPPED | Dead ElevenLabs-era prose |
| `style_bible{}` block | present (visual_style / color_palette / lighting_style) | DROPPED | Superseded by `style_preset:"vox-editorial"` + `color_semantics` line |
| `accents{}` block | `{data:[TEAL,CRIMSON], annotation:CRIMSON, highlighter:GOLD}` | DROPPED | Superseded by `color_semantics`; `vox_graphics.py` owns the palette |
| `manim_move` | `"accumulate"` | DROPPED | Unused envelope key; motions live per-beat in `shot.motion` and scene code |
| `total_estimated_duration_seconds` | 173.3 | DROPPED | Superseded by per-beat `actual_duration_s`; recompute if needed |
| `engine` | (missing) | `"kokoro"` | VOICE-LOCK |
| `voice_kokoro` | (missing) | `"am_onyx"` | Neutral vox default (peer: `vox-delivery-funnel`, `vox-abraxane-solvent`) |
| `folderLabel` | (missing) | `"@NikBearBrown"` | Channel handle |
| `source` | (only in `purpose`) | separate `source` line | Peer standard |
| `short_title` | (missing) | `"DAR is an Optimum, Not a Maximum"` | Peer standard |
| `derived_from` | (missing) | `"beat_sheet.pre-rebuild.json"` | Explicit lineage |

### Datable claims in narration

None. The DAR optimum mechanism (hydrophobicity → aggregation → liver / immune
clearance → poor tumor delivery) is timeless. Illustrative numbers (DAR-4/8,
68%/11% at 24h, 2.4/0.3 ug/g at 72h, "three mice") are labeled illustrative in
both the narration (B10, B11) and on-screen (B10 "illustrative", B11
attribution).

### Beat-level rebuilds

| Beat | Change | Reason |
|------|--------|--------|
| B01 | (unchanged; CARD → renders via B01_Title Manim) | Locked title |
| B02–B04 | (unchanged; each maps 1:1 to its named Manim class) | Locked shot list |
| B05 | Dropped nested `shot.remotion.FormACard` sub-object carrying a truncated `"Too little is the first failure. Even if the antibody finds…"` placeholder line. Kept `shot.type: STILL`, `source: ai`, `motion: kenburns`, `scene_description`, `image_prompt`, `new_visual_element` — the STILL slate metadata the pipeline actually reads. | The vox pipeline has no Remotion renderer wired for this reel; the vestigial FormACard was dead weight and its `lines[0]` was a truncated placeholder. B05 has always been a declared STILL slate. Same fix sibling `vox-delivery-funnel` applied to its B02, sibling `vox-abraxane-solvent` applied to its B02/B10. |
| B06–B12 | (unchanged; each maps 1:1 to its named Manim class in `vox_scenes.py`) | Locked shot list |
| B13/B14 | (unchanged; declared SLATE — vox pipeline has no OutroSeries/OutroCTA renderer) | Peer standard |

### `vox_scenes.py`

Three scoped changes; scene *content* otherwise locked verbatim from
pre-rebuild.

- **Path resolution:** `pathlib.Path(__file__).resolve().parents[3]` assumed a
  three-deep books layout; this reel sits five levels down under
  `books/anthropics/youtube/cancer-nanomedicine/youtube/`. Replaced with a
  walk-up search for `books/vox/aspects/explainer/vox-explainer/manim/` —
  same fix siblings `vox-delivery-funnel` (2026-08-28) and
  `vox-abraxane-solvent` (2026-08-28) applied.
- **B06 layout fix:** the `sticky_lbl` (`SerifLabel("hydrophobic / sticking
  together", CRIMSON, size=22)`) was placed `.next_to(agg_label, DOWN, buff=0.35)`
  with `agg_label` at `RIGHT * 3.5 + UP * 0.8`. The label's left tail extended
  across x ≈ 1.5 where the second (aggregating) antibody Y stem sat after its
  drift-in animation, so the leading "h" got cut. FIXED by moving both
  `d4_label` and `agg_label` to `RIGHT * 4.7` and shrinking / renaming
  `sticky_lbl` to `"hydrophobic / sticky"` (size 20, right-aligned to the chip).
- **B07 layout fix:** the DAR-8 dot cluster's final destination
  (`RIGHT * 5.0 + DOWN * 1.0`) landed on the "immune system" label center
  inside the clearance box, and the "DAR 8" label at `DOWN * 0.35` landed on
  the "immune" line. FIXED by anchoring `clear_text` to the BOTTOM of the box
  (`clear_box.get_bottom() + UP * 0.42`), moving the dot cluster to the TOP
  half (`UP * 0.05`), the "DAR 8" label above the box top (`UP * 0.7`), and
  the "cleared" chip below the dot cluster with `buff=0.35` (mid-box).
- **B09 REBUILD (BLOCKER fix):** the original `B09_OptimumCurve` used manim's
  `Axes` class + `ax.plot(...)` + `ax.get_area(...)`. First render produced
  ONLY the rotated "tumor drug delivery" y-axis label — the axes, curve, and
  three areas all rendered blank against this shared `vox_graphics` import.
  REBUILT without `Axes`: raw `Line` for x-axis and y-axis, MONO tick labels,
  `VMobject.set_points_smoothly` for the bell curve, three `Polygon`s for the
  sweet-spot area and the two failure zones. Delivery function preserved
  (`0.95 * exp(-0.28*(x-5.5)**2)`). Peak at DAR ~5.5, teal band spanning
  DAR 4–8, crimson under-delivers band DAR 0–4, crimson overloaded band
  DAR 8–10. Three labels ("sweet spot", "under-delivers", "overloaded / cleared
  fast"). Total run time unchanged (3.7 s of animation, then `wait(total - 3.7)`).
  Renders clean after rewrite.

### Audio

Old ElevenLabs-era mp3s (Jul 8) purged. Fresh Kokoro `am_onyx` mp3s generated
for all 14 beats via
`books/brutalist-art/runtime/scripts/generate_audio_kokoro.py`. Kokoro reads
`metadata.voice_kokoro` from the envelope. Measured `actual_duration_s`
written back to the sheet before the final compile. Per-beat mean_volume
−21.6 to −24.2 dB. Total run 161.82 s.

### Renders

- Manim (via `books/vox/scripts/vox_run.sh` with `VOX_QC=0` for the peer
  static-scene downgrade): B01, B02, B03, B04, B06, B07, B08, B09, B10, B11,
  B12 (11 scenes) → `manim/B*.mp4` at 1920×1080 p24. B06/B07 re-rendered
  after Gate V. B09 rewritten and re-rendered mid-pass.
- Declared SLATEs (no on-disk media): B05 (`STILL src=ai` — ai still),
  B13 (OutroSeries — no vox Remotion renderer), B14 (OutroCTA — same).
- Compile: `books/vox/scripts/vox_compile.py --review` — 11/14 filled,
  3 declared slates, master conformed to per-beat Kokoro audio.

## Not rebuilt (kept from pre-rebuild)

- Every narration line, verbatim.
- Every `card.*` intent block (B01/B03/B08/B12 — read by the Manim scenes
  as the source-of-truth text).
- Every `graphic.production_viz` intent block (B02/B04/B06/B07/B09/B10).
- `document` block on B11.
- All shot-list identifiers (`new_visual_element`).
- `SHOTLIST.md`, `PROMPTS.md`, `FACTCHECK.md`, `PEDAGOGY.md` — the paperwork
  set (Gate F).

## Lens (PHASE 1 §8) — four moves earned

- **Descartes — falsification checklist:** B03 poses the falsifiable question
  explicitly ("More drug should kill better. Why does loading more warheads
  make it clear faster — and kill less?"); B04 sets the checklist ("clinical
  ADCs sit between four and eight … a real trade-off running in both
  directions"). A DAR sweep at fixed dose refutes the "more is better" claim.
- **Hume — confidence is a property of the model:** B10/B11 label their
  numbers illustrative (in narration AND on the frame: "illustrative"
  subtitle on B10, "-- illustrative example (same antibody, same payload,
  same dose)" attribution on B11). The 68%/11% and 2.4/0.3 ug/g are DAR-shape
  facts about our example, not universal claims about all ADCs.
- **Popper — state failure criteria in advance:** B05 states failure mode 1
  in advance ("Load too little and the cell survives"); B06/B07 state failure
  mode 2 ("Load many of them on one antibody and the conjugate becomes
  greasy, sticky, prone to clumping … The immune system and liver … cannot
  tell the difference"). B10 makes both testable at 24h plasma.
- **Plato — artifact vs world:** B12 makes the move explicit ("The DAR-eight
  batch had more drug per molecule. It delivered less drug per gram of
  tumor.") — the artifact (loaded warheads per antibody) is not the world
  (drug reaching the tumor); pushing on the artifact past DAR-4/8 breaks the
  relationship. Also B09 by construction — the shape of the optimum curve
  IS the artifact-vs-world story ("not a maximization problem, an
  optimization with two failure modes").

## Palette-library quirk (LOGGED, not blocking)

`vox_graphics.TEAL` renders as near-INK grey throughout this reel's Manim
scenes (visible on B02 antibody strokes, B04 clinical-ADCs bracket + "clinical
ADCs" label, B07 DAR-4 dot + "SURVIVES" chip, B09 sweet-spot band + "sweet
spot" label, B10 DAR-4 bar + "DAR 4" chip). This is the same shared-library
quirk siblings `vox-delivery-funnel` and `vox-abraxane-solvent` logged
2026-08-27/28. Layout semantics are preserved throughout: the surviving /
optimal / high thing is always visibly distinct from the cleared / overloaded
/ low thing (bar heights disagree, chip colors differ, positions separate,
polygon fills contrast). A palette fix in
`books/vox/aspects/explainer/vox-explainer/manim/vox_graphics.py` is out of
scope for a single-reel invocation.

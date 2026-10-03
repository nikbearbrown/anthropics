# REBUILD-LOG — hai-vox-emitter-range
_Rebuild pass: 2026-08-28_

## What was locked (carried verbatim)
- All narration_text in beats B01–B14 — no changes
- Beat order, act labels
- Shot intent / production_viz descriptions for all GRAPHIC beats
- Metadata identity: title, slug, topic, source, register (Pragmatist), audience (HAI), palette (humanitarians), outro_source
- HAI channel skin retained (OutroSeries / OutroCTA at B13/B14) — non-claude channels keep their own bookends per REBUILD SKILL §3

## What was rebuilt / dropped

### Metadata — dead ElevenLabs-era fields DROPPED
| Field | Old value | New value |
|-------|-----------|-----------|
| `voice_id` | `"qdEb53HLreRBCD1FQE30"` | DROPPED |
| `clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | DROPPED |
| `_variant_todo` | 4 TODO items about rewriting into Pragmatist voice + swapping to HAI outro | DROPPED (rebuild is happening now; TODO satisfied by the skin/outro already being in place) |
| `build` (metadata) | Stale July stamp: `filled: 2, of: 14, slates: [B01..B12]` | DROPPED — will be re-stamped by compile.py |

VOICE-LOCK fields retained: `engine: "kokoro"`, `voice_kokoro: "am_onyx"` ✓

### B07 — STILL/ai → GRAPHIC/manim (punt fix)
| Field | Old | New |
|-------|-----|-----|
| `shot.type` | `STILL` | `GRAPHIC` |
| `shot.source` | `ai` | `own` |
| `shot.motion` | `kenburns` | `drawon` |
| `shot.remotion` | FormACard placeholder | Removed |
| `scene_description` | archival-photo-style description | Removed |
| `image_prompt` | gen-AI image prompt | Removed |
| `graphic.manim` | (none) | `B07_TumorGeometry` |
| `graphic.production_viz` | (none) | Full production_viz block: teal rim, muted core cross-section |

Reason: STILL src=ai for a schematic cross-section of a heterogeneous tumor is a punt (nopunt catalog §6 — conceptual/quantitative content should not be a static AI photograph). The claude-liam sibling made the same fix (REBUILD-LOG.md there). Structure/boundary visualization is fully animatable as a Manim scene.

### B01, B04, B07, B10, B12 — punt `build.needs` tags stripped
`YOU → 5–10s gen-AI clip → pantry` needs-lines removed from every card beat. `suggested: prompt:` lines removed. Content preserved.

### B02, B03, B05, B06, B08, B09, B11 — pipeline `build.needs` stripped
`PIPELINE → render animated_graphics.py scene BXX_*` needs-lines removed; compile.py now handles slot resolution.

### B13, B14 — false VIDEO stamp corrected
Both beats claimed `build.status: VIDEO, src: media/B13.mp4` — but no `media/` directory exists in the reel. Whole `build` block removed; compile.py will slate honestly.

`shot.remotion.pattern` retained as `OutroSeries` / `OutroCTA` — these ARE the HAI channel's own outro skin, and both patterns are registered in `runtime/scripts/remotion_scenes.py`. Non-claude channels keep their own bookends per REBUILD SKILL §3.

## What was NOT touched
- No narration edits (no datable claims to fix — the physics numbers are locked)
- No shot.form rewrites (rebuild SKILL says derive per SHOT-FORM-SYSTEM.md; no such file present in this tree — skipped, not blocking)
- No FACTCHECK.md / TYPECHECK.md new authoring — this reel's toolchain is `brutalist-art/runtime/scripts/`, and it does not have a `type_check.py` bound to this reel's format (HAI vox skin). Skipped honestly — see AUDIT.md.

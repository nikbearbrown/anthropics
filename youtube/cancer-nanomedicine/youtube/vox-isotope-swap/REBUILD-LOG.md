# REBUILD-LOG — vox-isotope-swap
_Rebuild pass: 2026-08-27_ (pure vox-editorial reel; twin at `claude-liam-vox-isotope-swap`.)

## What was locked (carried verbatim)
- All narration_text in beats B01–B14 — no changes.
- Beat order, act labels, scene_class names.
- vox_scenes.py Manim scene classes and production_viz descriptors.
- Metadata identity: title, slug, topic, source, style_preset, style_bible, color_semantics, exclusions note.

## What was rebuilt / dropped

### Metadata — dead ElevenLabs-era fields DROPPED
| Field | Old value | New value |
|-------|-----------|-----------|
| `voice_id` | `"TyW6NH39JcFb5M3xdIIk"` | DROPPED |
| `clock`    | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` | DROPPED |

Fields ADDED (VOICE-LOCK normalize):
| Field | Value |
|-------|-------|
| `engine`        | `"kokoro"` |
| `voice_kokoro`  | `"am_onyx"` |

### B02 — STILL·ai FormA placeholder DROPPED
The beat is a STILL src=ai slot (a PET-scan-of-a-torso photograph ask). It carried a
`shot.remotion.pattern: FormACard` block with `props.lines: ["His team orders a scan
first — not as a formality,…"]` — the narration's first line truncated with an ellipsis.
That is a punt in a FormA costume (PUNT catalog: "a FormACard whose narration NAMES a
visual it never draws"). The FormA block is removed; the STILL·ai intent, image_prompt,
and scene_description remain — the beat compiles as an honest slate for this review cut.

### B09 — STILL·ai FormA placeholder DROPPED
Identical treatment. The beat is a photojournalism ask ("physician reviewing a glowing
PET scan on a large light-box monitor in a dim clinical imaging reading room"). The
FormA `props.lines: ["So the scan is not paperwork. It is patient selection. A…"]`
placeholder is removed; STILL·ai intent preserved.

## Datable claims checked
No datable model names, versions, or prices in narration. B11 numbers ("60% shrink,
40% grow") are already labeled "illustrative" in production_viz `note` and inside
the spoken narration ("Illustrative numbers."). No corrections needed.

## Files
- `beat_sheet.pre-rebuild.json` — byte-exact copy of the pre-pass sheet (Aug 26 20:56).
- `beat_sheet.json` — rebuilt sheet (this pass).
- `AUDIT.md` — audit ledger for this pass.

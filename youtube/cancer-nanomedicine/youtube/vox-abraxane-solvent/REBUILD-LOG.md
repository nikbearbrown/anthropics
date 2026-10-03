# REBUILD-LOG.md — vox-abraxane-solvent · 2026-08-28

Rebuilt under `skills/make/rebuild/SKILL.md` from `beat_sheet.pre-rebuild.json`
(byte-exact snapshot of the July-8 sheet).

## Envelope changes (VOICE-LOCK)

| Field | Old → New | Reason |
|-------|-----------|--------|
| `voice_id` | `"TyW6NH39JcFb5M3xdIIk"` → DROP | ElevenLabs-era; VOICE-LOCK.md says drop |
| `clock` | `"narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"` → DROP | ElevenLabs-era prose; audio is generated, actual_duration_s already present |
| `style_bible` | `{visual_style, color_palette, lighting_style}` → DROP | Unused in current vox pipeline (vox_compile.py reads none of them) |
| `accents` | `{data:[…], annotation, highlighter}` → DROP | Unused in current vox pipeline; palette lives in vox_graphics.py |
| `manim_move` | `"drain"` → DROP | Unused in current vox pipeline (per-scene motions live in scene code) |
| `total_estimated_duration_seconds` | `274.41` → DROP | Regenerated at compile time |
| `engine` | (missing) → `"kokoro"` | Peer standard (vox-delivery-funnel) |
| `voice_kokoro` | (missing) → `"am_onyx"` | Peer standard; matches existing mp3 renders |
| `folderLabel` | (missing) → `"@NikBearBrown"` | Peer standard |
| `source` | (embedded in `purpose`) → separate line `"cancer-nanomedicine/chapters/03-nanocarrier-platforms-liposomes-polymeric-and-albumin-particles.md"` | Peer standard |
| `short_title` | (missing) → `"The Solvent Was the Danger"` | Peer standard |
| `derived_from` | (missing) → `"beat_sheet.pre-rebuild.json"` | Rebuild contract audit trail |
| `purpose` | (shortened) — dropped the trailing "(albumin-bound paclitaxel / Cremophor solvent mechanism only)" parenthetical since `source` now names the chapter | Removes duplication |

## Beat body changes

| Beat | Change | Reason |
|------|--------|--------|
| B02 | Dropped `shot.remotion` FormACard block (truncated `"lines": ["Paclitaxel is one of the most effective chemotherapy drugs ever developed.…"]`) | STILL beat carried an orphan Remotion pantry block from an earlier fill pass — unrenderable in vox pipeline; PIL slate label draws from `new_visual_element`. Same fix sibling `vox-delivery-funnel` applied to its B02. |
| B10 | Dropped `shot.remotion` FormACard block (truncated `"lines": ["Here is what that means in practice. A nurse prepares two…"]`) | Same as B02. |

All 17 narrations preserved verbatim — zero narration edits. Word counts unchanged.

## vox_scenes.py changes

| Change | Reason |
|--------|--------|
| Path resolution `_BOOKS = _HERE.parents[2]` (assumed 3-deep books layout) → walk-up search for `books/vox/aspects/explainer/vox-explainer/manim/` with `vox_graphics.py` present, error out if not found | Reel actually sits 5 parents down (`.../anthropics/youtube/cancer-nanomedicine/youtube/vox-abraxane-solvent`); the hard-coded `parents[2]` resolved to `.../youtube` not `.../books`, so import failed. Same fix sibling `vox-delivery-funnel` applied 2026-08-28. |
| Dropped `from vox_graphics import _quote_scene` (unused in this reel's scenes) | Import was unused; drops one attribute lookup during collection. |

## What was NOT touched
- Manim scene bodies (B01_Title, B03_InsolubilityProblem, …, B15_Endcard) — all layout code preserved as authored.
- Beat `shot`/`graphic`/`card`/`document` sub-objects other than the two dead FormACard drops.
- Audio mp3s (already generated at Kokoro `am_onyx`).
- FACTCHECK.md, SHOTLIST.md, PROMPTS.md paperwork (Gate F set — kept as-is).

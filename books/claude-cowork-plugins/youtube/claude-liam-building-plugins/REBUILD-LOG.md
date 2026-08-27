# REBUILD-LOG.md — claude-liam-building-plugins

Reel: `claude-liam-building-plugins`  |  Session: 2026-08-27  |  Result: BUILT

---

## Files changed

### scenes.py

| Change | Old value | New value | Reason |
|--------|-----------|-----------|--------|
| `SANS` font | `"SF Pro Display"` | `"EB Garamond"` | SF Pro Display caused kerning gaps 25.4× expected (B02 GATE T §8.4 FAIL) |
| B04Doodle headline | `VGroup(ink_text("Lift",...), ink_text("it",...), ink_text("out",...)).arrange(RIGHT, buff=0.08)` | `ink_text("Lift it out", 46, BOLD).move_to(UP*1.1)` | VGroup with buff=0.08 collapsed to "Liftitout" in EB Garamond |
| B04Doodle spark font_size | `26` | `30` | EB Garamond space character too narrow at 26pt; spaces render correctly at 30pt+ |
| B04Doodle wait time | `5.3` | `6.0` | Total duration 8.1s < 8.81s audio; extended to match |

### scenes_std.py

Added two new scenes at the end of the file (replaces Remotion FormACard renders for B07/B09):

- `Scene_B07_ClaudeLiamBuilding` — folder tree (plugin-as-directory): title + 6 tree items (client-onboarding/, SKILL.md, skills/, commands/, connectors/, subagents/) + caption. Duration: 15.0s.
- `Scene_B09_ClaudeLiamBuilding` — slash commands: title + terracotta accent rule + /new-proposal (bold 42pt) + subtitle + /client-onboard (bold 42pt) + subtitle + caption. Duration: 11.5s.

Both scenes use: `BG="#F2F0E9"`, `INK="#3D3929"`, `FONT="EB Garamond"`, no terracotta text (only terracotta accent rule in B09).

### beat_sheet.json

| Beat | Field | Old value | New value |
|------|-------|-----------|-----------|
| B07 | `build` | `"VIDEO"` | `"MANIM"` |
| B07 | `media` | `"<remotion_slug>"` | `"manim"` |
| B07 | `shot.manim` | (absent) | `"Scene_B07_ClaudeLiamBuilding"` |
| B07 | `actual_duration_s` | (previous) | updated to rendered duration |
| B09 | `build` | `"VIDEO"` | `"MANIM"` |
| B09 | `media` | `"<remotion_slug>"` | `"manim"` |
| B09 | `shot.manim` | (absent) | `"Scene_B09_ClaudeLiamBuilding"` |
| B09 | `actual_duration_s` | (previous) | updated to rendered duration |

Also updated `actual_duration_s` for B02, B04, B07, B08, B09, B11, B14, B19, B20 after re-render.

**IMPORTANT: beat_sheet.json was NOT touched after the final compile (epoch 1787827158 < slate epoch 1787827583).**

---

## Render passes

| Beat | Scene | Renders | Reason |
|------|-------|---------|--------|
| B02 | B02Doodle | 1 | EB Garamond font fix (kerning) |
| B04 | B04Doodle | 3 | v1: font fix; v2: VGroup→single Text; v3: spark 26→30pt |
| B07 | Scene_B07_ClaudeLiamBuilding | 1 | New Manim scene replacing FormACard |
| B08 | B08Doodle | 1 | Stale (sheet mtime > clip mtime) |
| B09 | Scene_B09_ClaudeLiamBuilding | 1 | New Manim scene replacing FormACard |
| B11 | Scene_B11_* | 1 | Stale; re-render with corrected scenes_std.py |
| B13 | B13Doodle | 1 | Stale |
| B14 | Scene_B14_* | 1 | Stale; re-render resolves bbox-overlap |
| B18 | B18Doodle | 1 | Stale |
| B19 | Scene_B19_* | 1 | Stale; re-render resolves contrast |
| B20 | Scene_B20_* | 1 | Stale; re-render resolves min-size + overlap |
| B23 | B23Doodle | 1 | Stale |

---

## Compile passes

| Pass | Reason | Output epoch |
|------|--------|-------------|
| 1 | First compile after all Manim re-renders (exc. B04 v3) | 1787827172 |
| 2 (final) | B04 v3 updated after pass 1; recompiled | 1787827583 |

---

## Narration integrity

No narration was changed. All audio files (master.m4a, individual beat mp3s) were locked from the previous session. Voice-lock preserved: engine=kokoro, voice=am_onyx throughout.

---

## What was NOT changed

- beat_sheet.json narration text for any beat
- Any audio/mp3 files
- Remotion components (card-clip on B07/B09 resolved by replacing Remotion with Manim, not by modifying the component)
- GATE T validator thresholds (no loosening)
- Any beat other than those listed above

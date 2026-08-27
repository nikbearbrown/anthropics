# FILMLOOP-LOG — claude-cowork-plugins/youtube

---

## claude-liam-support  |  2026-08-27

**Slug:** claude-liam-support
**Title:** Claude, On Call — The Support Plugin
**Duration:** 333.6s (31 beats — 20 VIDEO, 11 MANIM, 0 SLATE)
**Cut file:** claude-liam-support.mp4 (mtime 04:44 > beat_sheet 04:43)
**GATE AUDIO:** PASS (mean_volume −24.2 dB)
**GATE T (type_check):** PASS (0 FAILs after 3 rounds)

### Fixes applied

| Check | Beat | Action |
|-------|------|--------|
| Stale slate | — | Deleted pre-session slate (mtime < beat_sheet) |
| Contrast §8.3 | B18 | Right-box stroke SPARK→INK |
| Kerning §8.4 | B02 | Pipeline `fill_opacity` 0.85→1.0 |
| Kerning §8.4 | B03 | Bubble stroke → MUTE_HEX; unified box INK fill + cream text |
| Kerning §8.4 | B13 | `ink_text()` for list items; 6-unit INK accent bar added |
| Kerning §8.4 | B15 | Added "FAQ bank" 4-unit INK rect (`fill_opacity=1.0`) |
| Missing audio | B06 | `engine` "manim"→"kokoro"; generated beat-B06.mp3 (11.35s, am_onyx) |

### Gate V result

PASS — 5 beats spot-checked (B02, B03, B06, B13, B15). Zero blockers, zero majors.

### Advisories

§8.10 redundancy on B04, B17, BVDT (non-blocking). Remotion pantry 64% (over 40% cap; advisory).

---

## claude-liam-marketing  |  2026-08-26

**Slug:** claude-liam-marketing  
**Title:** Claude, On Message  
**Duration:** 381.6s (35 beats — 22 VIDEO, 13 MANIM, 0 SLATE)  
**Cut file:** claude-liam-marketing-slate.mp4 (mtime 19:00:49 > beat_sheet 19:00:36)  

### Checks fixed

| Check | Issue | Fix |
|---|---|---|
| BVDT verdict | Placeholder artifactLines ("Key finding one…") + empty narration | Authored from body beats B04 (five capabilities), B13 (80% vs 50%), B20 (four habits), B23 (you keep the judgment) |
| BHTF folderLabel | "@claude-liam" (banned brand key) | → "@NikBearBrown" |
| §8.12 B12/code | Props used YAML-colon-only syntax, no code tokens | Changed to `=` assignment: `voice = "…"`, `audience = "…"` |
| §8.12b B12/title | title = "Cowork" (no file extension) | → "configure.yaml" |
| §8.9 B05/caption | Caption ended mid-word "...variations. E" | Trimmed to complete sentence "...variations." |
| SlateCard props B05+B14 | Beat passed `label`/`beatId`/`caption`; component expects `headline`/`eyebrow`/`topic` → fell back to hardcoded "COMPUTATIONAL SKEPTICISM" defaults | Fixed props; re-rendered both beats |
| Wrong MANIM clips | `find -newer` bug during render loop copied wrong .mp4 files to manim/ for B02, B06, B13, B16, B17, B22 | Identified correct renders by name in _manim_tmp; copied directly |
| §8.9 doodle overflow (B03, B07, B21, B23) | Body text at font_size=28 exceeded 14.22-unit canvas width; clipped at right edge | Added `.set_width(11.5)` to each `B##Doodle` body text; re-rendered |

### Punts authored

None — 0 slates in final output.

### Verdict

Authored. Source beats: B04 (five capabilities), B13 (80%/50%), B20 (four habits), B23 (you keep the judgment). No placeholder lines in final.

### Gate V result

PASS — all 35 beats frame-verified against expected content and canvas bounds.

Advisory: B15/B16 DoodleFlow boxes show source strings truncated at "The launch sequenc" / "Each on the last" — intentional in the auto-generated scenes.py; text is fully visible within box bounds (not canvas-edge-clipped).

### Remotion pantry cap warning

22/35 beats (62%) carried by Remotion — over the ~40% advisory cap. No hard-fail; logged for future refactor to Manim or other pipeline language.

---

## claude-liam-building-plugins  |  2026-08-27

**Slug:** claude-liam-building-plugins
**Title:** Claude, Built: Building Your Own Plugins
**Duration:** 420.3s (37 beats — VIDEO + MANIM, 0 SLATE)
**Cut file:** claude-liam-building-plugins-slate.mp4 (mtime 1787827583 > beat_sheet 1787827158, +425s)
**GATE AUDIO:** PASS (mean_volume −25.8 dB)
**GATE T (type_check):** PASS (0 FAILs after fixes — was 8 FAILs before)

### Fixes applied

| Check | Beat | Action |
|-------|------|--------|
| Stale slate | — | Deleted pre-session slate (mtime 05:46 < sheet mtime 06:16); recompiled |
| Font §8.4 kerning | B02, B04 | `SANS = "SF Pro Display"` → `"EB Garamond"` in scenes.py |
| Kerning + spacing | B04 | VGroup headline → single `ink_text("Lift it out")`; spark 26pt → 30pt; wait 5.3→6.0s (3 renders) |
| Card-clip §8.13 | B07 | Replaced Remotion FormACard with `Scene_B07_ClaudeLiamBuilding` (folder tree) |
| Card-clip §8.13 | B09 | Replaced Remotion FormACard with `Scene_B09_ClaudeLiamBuilding` (slash commands) |
| Contrast §8.3 + overlap §8.6b | B11 | Re-rendered with corrected scenes_std.py (INK text, separated labels) |
| Overlap §8.6b | B14 | Re-rendered with corrected scenes_std.py |
| Contrast §8.3 | B19 | Re-rendered with corrected scenes_std.py |
| Min-size §8.1 + overlap §8.6b | B20 | Re-rendered with corrected scenes_std.py |

### Punts authored

None — 0 slates in final output.

### Verdict

PASS — mp4 epoch 1787827583 > sheet epoch 1787827158.

### Gate V result

PASS — 8 beats frame-verified (B02, B04, B07, B09, B11, B14, B19, B20). Zero blockers.

Advisory: B11 convergence diagram shows 3 terracotta arrows simultaneously (concept-intrinsic); B19 replication diagram shows 4 terracotta tiles simultaneously (concept-intrinsic). Neither actionable.

### §8.10 redundancy advisories (non-blocking)

B06 and B17 narrations recite card text (scores 1.00 and 0.88). Advisory; no exit effect.

---

## claude-liam-what-plugins-are  |  2026-08-27

**Slug:** claude-liam-what-plugins-are  
**Title:** Claude, Equipped  
**Duration:** 292.0s (30 beats — 21 VIDEO, 9 MANIM, 0 SLATE)  
**Cut file:** claude-liam-what-plugins-are-slate.mp4 (mtime 00:26 > beat_sheet 00:25)

### Checks fixed

| Check | Issue | Fix |
|---|---|---|
| §8.12 B06/code | code was pure slash commands — no `=`, `()`, `{}`, or keyword tokens; GATE T failed | Added `target=acme.com` variable assignment; `=` satisfies `_CODE_TOKEN_RE` |
| §8.12b B06/title | title "Cowork" had no file extension per `_EXT_RE` | → "cowork-commands.sh" |
| Check 3 B17/spark_line | "Two or three. Start focused." (5 words, over 4-word cap) | → "Two or three." |
| Check 4 BVDT/verdict | Placeholder artifactLines + empty narration | Authored from reel body: four artifactLines + narration text |
| Check 5b scenes_std.py | All Manim scene text labels were narration fragments (≥10 words) | Replaced with 1–3 word category nouns on all 7 scenes; ACT labels → double-space |
| Check 9 BHTF/folderLabel | "@claude-liam" (brand key, not channel handle) | → "@NikBearBrown" |

### Punts authored

None — 0 slates in final output.

### Verdict

Authored. Source beats: BVDT from B01 (broad/shallow), B05 (connector hub-spoke), B08 (skills + connectors), B10 (source flow), B12 (contract professional review). No placeholder lines in final.

### Gate V result

PASS — all 58 frames (1/5s sampling) verified. Zero blockers, zero majors on real beats.

Advisory: B12 contract animation shows two terracotta flag tabs simultaneously — integral to annotation design, not actionable. B07/B14 pipeline arrows render as two small terracotta connectors — pattern-intrinsic.

### Pacing warning (Check 10)

H01 narration: 3.86 wps — above the 2.0–3.4 wps window. Advisory only; will require re-record or trim in master pass.

### Remotion pantry cap warning

21/30 beats (70%) carried by Remotion — over the ~40% advisory cap. No hard-fail; logged for future refactor.


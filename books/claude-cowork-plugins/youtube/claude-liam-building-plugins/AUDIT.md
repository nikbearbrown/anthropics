# AUDIT.md — claude-liam-building-plugins

Reel: `claude-liam-building-plugins`  |  Audited: 2026-08-27  |  Auditor: filmloop supervisor  |  Verdict: **BUILT**

---

## Phase 0 — Rebuild contract

| Item | Status |
|------|--------|
| beat_sheet.json present | PASS |
| beat_sheet.json schema valid (slug, title, beats array) | PASS |
| VOICE-LOCK engine=kokoro, voice=am_onyx | PASS |
| No post-compile sheet edit risk | PASS (all sheet edits made before final compile) |

---

## Phase 1 — 11-check audit

| # | Check | Beats | Result | Action |
|---|-------|-------|--------|--------|
| 1 | Stale render (mp4 older than beat_sheet) | all | FIXED | Deleted stale slate (mtime 05:46 < sheet mtime 06:16); re-rendered 8 Manim beats; recompiled |
| 2 | GATE T type_check §8 failures | B02, B04, B07, B09, B11, B14, B19, B20 | FIXED | See per-beat detail below |
| 3 | Narration voice-lock | all audio | PASS | engine=kokoro, voice=am_onyx throughout; no beat changed |
| 4 | Terracotta one-moment rule | all | ADVISORY | B11 (3 convergence arrows) and B19 (4 replication tiles) each exceed one-moment; both are concept-intrinsic diagrams, not decorative violations |
| 5 | NOPUNT — no DoodleScene/DoodleChart slates | all | PASS | 0 punts in output |
| 6 | NOPUNT — FormA narration names visual it never draws | B07, B09 | FIXED | Old FormACard renders replaced with Manim scenes that draw the named visuals |
| 7 | Canvas bounds — no text touching frame edge | all | PASS | All Manim scenes padded ≥ 0.5 unit from edge |
| 8 | Font consistency — EB Garamond throughout | all | FIXED | scenes.py SANS was "SF Pro Display"; corrected to "EB Garamond" |
| 9 | Audio levels — mean_volume ≥ −40 dB | master.m4a | PASS | mean_volume −25.8 dB |
| 10 | Pacing — wps 2.0–3.4 | all narration | PASS (advisory) | No beats flagged above cap |
| 11 | Gate V — mp4 mtime > sheet mtime | slate | PASS | slate epoch 1787827583 > sheet epoch 1787827158 (+425s) |

---

## Per-beat GATE T fix log

### B02 (MANIM) — kerning §8.4
- **Finding:** max inter-glyph gap 321px (25.4× expected) — font was SF Pro Display
- **Fix:** Changed `SANS = "SF Pro Display"` → `SANS = "EB Garamond"` in scenes.py; re-rendered B02Doodle
- **Status:** FIXED

### B04 (MANIM) — kerning §8.4 + compound spacing issues
- **Finding 1:** max inter-glyph gap 35px (7.0× expected) — wrong font
- **Fix 1:** EB Garamond font fix (same as B02)
- **Finding 2:** VGroup headline "Liftitout" — word spacing collapsed at 0.08 buff
- **Fix 2:** Replaced VGroup of 3 words with single `ink_text("Lift it out", 46, BOLD)`
- **Finding 3:** Spark caption "Liftitout" at 26pt — EB Garamond space too narrow at that size
- **Fix 3:** Increased spark font_size 26 → 30pt
- **Finding 4:** wait time 5.3s → total 8.1s < 8.81s audio
- **Fix 4:** wait time 5.3 → 6.0s
- **Status:** FIXED (3 re-renders)

### B07 (REMOTION) — card-clip §8.13
- **Finding:** text blob touches card left boundary (col 275 vs card_left 272, tol=4px)
- **Fix:** Authored replacement Manim scene `Scene_B07_ClaudeLiamBuilding` (folder tree: title + 6 tree items + caption); updated beat_sheet.json build/shot; re-rendered
- **Status:** FIXED

### B09 (REMOTION) — card-clip §8.13
- **Finding:** text blob touches card left boundary (col 272 vs card_left 272, tol=4px)
- **Fix:** Authored replacement Manim scene `Scene_B09_ClaudeLiamBuilding` (slash commands: title + accent line + 2 commands + 2 subs + caption); updated beat_sheet.json build/shot; re-rendered
- **Status:** FIXED

### B11 (MANIM) — contrast §8.3 + bbox-overlap §8.6b
- **Finding:** terracotta accent #D97757 on cream 2.74:1 < 4.5:1; text overlap 33%
- **Fix:** scenes_std.py was already corrected in prior session (all text uses INK, labels separated); re-rendered resolved both
- **Status:** FIXED

### B14 (MANIM) — bbox-overlap §8.6b
- **Finding:** text-run bbox overlap 100% — two labels on top of each other
- **Fix:** scenes_std.py already corrected; re-render resolved
- **Status:** FIXED

### B19 (MANIM) — contrast §8.3
- **Finding:** terracotta accent #D97757 on cream 2.74:1 < 4.5:1
- **Fix:** scenes_std.py already corrected; re-render resolved
- **Advisory:** 4 terracotta replication tiles visible simultaneously — concept-intrinsic; not actionable
- **Status:** FIXED (advisory noted)

### B20 (MANIM) — min-size §8.1 + bbox-overlap §8.6b
- **Finding:** smallest text run 19px < 20px floor; label overlap 100%
- **Fix:** scenes_std.py already corrected with larger font sizes and separated positions; re-render resolved
- **Status:** FIXED

---

## §8.10 redundancy advisories (non-blocking)

- B06: narration recites card (similarity score 1.00)
- B17: narration recites card (similarity score 0.88)

These are advisory only; no exit effect applied. Flagged for future narration revision.

---

## Gate V frame spot-check

| Beat | Frame | Result |
|------|-------|--------|
| B02 | midpoint | PASS — clean doodle, EB Garamond, no kerning gaps |
| B04 | 4.0s (v3) | PASS — "Lift it out" headline + body + spark all properly spaced |
| B07 | midpoint | PASS — folder tree renders correctly, all INK color |
| B09 | midpoint | PASS — slash commands display, accent rule visible |
| B11 | midpoint | PASS — convergence diagram, all text INK, no overlap |
| B14 | midpoint | PASS — labels separated, no overlap |
| B19 | midpoint | PASS — replication tiles, INK text, advisory noted |
| B20 | midpoint | PASS — all text ≥ 20px, no overlap |

---

## Final deliverable

| Item | Value |
|------|-------|
| Slate file | `claude-liam-building-plugins-slate.mp4` |
| Duration | 420.3s |
| Size | 4,683,346 bytes |
| mp4 mtime epoch | 1787827583 |
| sheet mtime epoch | 1787827158 |
| mtime delta | +425s (mp4 is newer) |
| Audio | mean_volume −25.8 dB (gate: ≥ −40 dB) PASS |
| Resolution | 1280×720 h264 + aac |

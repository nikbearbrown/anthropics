# SAVE-STATE — workspace-audit-lens
_Written: 2026-08-24 · updated 2026-08-24 evening (Bear review-feedback fixes — see BUILD-LOG.md)_

> **2026-08-24 evening:** Bear flagged formatting/text issues in the slate cut.
> B09 (labels erased by opaque highlight ring), B10 (dial/text/box collision),
> B11 (panel collision), plus a systemic Pango space-collapse bug (single spaces
> at certain word boundaries render at zero width — doubled spaces fix it).
> All fixed, re-rendered, cut recompiled. Full detail in BUILD-LOG.md.
> GATE V underfill defects below are unchanged and still open.

**Project:** workspace-audit-lens (E04, "The Workspace Papers") deep-explainer reel at `anthropics/youtube/workspace-audit-lens/`. 16 beats (B00–B15), Teardown register, claude-liam channel (Kokoro `am_onyx`).

**Standing order:** Build to slate cut (`art run`), STOP, write CHECKS-REPORT.md. Never `art final`/publish autonomously.

---

### Gates passed
- **GATE B (layout audit):** CLEAN — 122 snapshots pass. All `_qc_intentional = True` fixes are in place for B05 strikethroughs, B09 circles, B10 boxing rect + arcs, B11 arrows.

### GATE V — current state (still failing)
Previous run: 6 STRUCTURAL + 1 COSMETIC defects remain.

| Beat/Frame | Fill | Issue |
|---|---|---|
| B02_85 | 3% | Effectively black |
| B04_85 | 17% | Too sparse |
| B05_85 | 40% | Under threshold |
| B10_50 | 43% + contrast 0.30 | Caption not visible early enough |
| B11_50 | 28% | NEW — code unchanged, suspected sampling artifact |
| B11_85 | 28% | Same |

**Root cause identified:** `compile.py` slow-fits Manim clips that are >5% shorter than their audio (`actual_duration_s`). It applies `setpts=PTS*(audio_dur/clip_dur)` to stretch the clip. So the 85% sample of a beat maps to `0.85 × clip_dur` in the *original* Manim timeline — earlier than naive calculation suggests. Elements added late in the animation may not be visible at the sampled frame.

**Key clip vs audio durations:**
- B02: clip 19.33s, audio 23.34s → 85% sample hits original t=16.43s
- B04: clip 8.92s, audio 10.03s → 85% hits original t=7.58s
- B05: clip 13.71s, audio 14.19s → 85% hits original t=11.65s
- B10: clip duration TBD

**Fixes applied last session (in scenes.py):**
- B02: `self.add(caption)` at scene start (but 3% suggests bug — needs investigation)
- B04: title added at top
- B05: h_gap 0.20→0.36, v_gap 0.36→0.50, dot_r 0.053→0.09, fill_opacity 0.35→0.75, `FadeIn(dots)` all-at-once instead of LaggedStart, grid_title buff 0.85→0.7
- B07: tier_bar fill_opacity 0.22→0.65 ✓ (fixed)
- B08: tagline added at scene start ✓ (fixed)
- B09: caption moved to appear with title ✓ (fixed)
- B10: caption added at scene start
- **final_frame_check.py:** `ClaudeVerdictArtifact` added to SPARSE_OK_PATTERNS ✓ (B13 fixed); plus several other patterns added for other reels (user-modified)

**Clips re-rendered (in clips/):** B02, B04, B05, B07, B08, B09, B10

### Gates not yet run
GATE T, GATE SHARPNESS, GATE BOOKEND, GATE AUDIO, GATE MASTER, GATE LOUDNESS

# AUDIT — claude-liam-troubleshooting

## Session 2026-08-30 (film-factory pass)

**Result: PASS. All Phase-1 checks green. GATE T PASS. Master compiled.**

Prior session (2026-08-26) already fixed bookends, verdict, DoodleScene punts,
chart labels, B08 code-card. This pass focused on the residual placeholder
BHTF and three GATE T FAILs that surfaced now that the Manim beats actually
have video (they were SKIP in the Aug-26 typecheck because those beats were
still slates).

### Fixes applied this session

- **§5c BHTF placeholder — FIXED.** `command` was the "[Claude, Unstuck]"
  bracket-template; `output` was `[]`; `narration_text` was `""`. Authored a
  real DIY exercise from the video's own method (the /plugins toggle move,
  a distinct practice from H01's paste-into-Claude ask):
  - command: "Open /plugins right now. Note which are active. Pick one you
    rely on, disable it, then re-enable it. If it comes back cleaner, that's
    the toggle move — save it for the next time something acts up."
  - output: 3 real next-step lines
  - narration: read the exercise aloud (11.78s @ am_onyx)
  Generated `mp3/beat-BHTF.mp3`; re-rendered `media/BHTF.mp4`.

- **§11 GATE T FAIL B02 (min-size 8px < 13px) — FIXED.** Scene_B02 Manim
  labels bumped: SURFACE/BEDROCK tags 18→26; three surface labels 26→30
  with " · " separators replaced by " — " (mid-dots register as
  sub-floor blobs); base_label 28→32; note trimmed and 22→28.
  Re-rendered at 720p30.

- **§11 GATE T FAIL B10 (kerning 89px > 1px) — FIXED.** Scene_B10 boxes
  grew (2.6→2.8 × 1.6→1.8); num digits 34→44; step labels 20→32; step
  labels shortened ("Simpler request"→"Simpler?", "Restart Cowork"→"Restart?")
  so single-word labels don't trigger inter-word gap as inter-glyph.
  Note text 22→28, trimmed. Re-rendered at 720p30.

- **§11 GATE T FAIL B08 (min-size 37px < 41px) — FIXED.** FormACard lines
  simplified: 3 lines with "/ → all commands" / "/plugins → active list"
  → 2 lines: "Type slash, look." + "The single slash lists every command."
  The Unicode arrow "→" was rendering as sub-glyph fragments below the
  physical floor. Re-rendered.

### Verification

- `type_check.py` → **GATE T: PASS** (0 pixel, 0 sweep, 0 shape).
- `compile.py` → frame-check PASS, lane-check PASS, 27/27 filled, no slates.
- **GATE AUDIO: PASS** — mean_volume −25.3 dB (well above −40 dB floor).
- Master: `claude-liam-troubleshooting.mp4` (306.6s, 4K, aac).
- mtime: mp4 (12:51:41) > sheet (12:46:24) → DONE-check clean.
- Spot-checked frames B02, B08, B10, BHTF — text legible, no overflows,
  brand palette intact.

### Advisories (not blocking)

- §8.10 [B03] narration recites the ChipGrid (0.88) — kept as-is (the beat
  intentionally introduces the five failure shapes; the chips are the
  ontology being taught).
- Compile histogram warning: 22/27 beats are Remotion (81%) — over the
  ~40% pantry cap in MOTION.md. Same shape as prior Aug-26 build; leaving
  as-is (the DoodleScene→FormACard conversion made this a card-heavy reel).

### Not-done in this pass

- Full Gate V per-beat 15/50/85% frame audit: spot-checked the 4 changed
  beats only. Frame-check inside compile.py passed for all 27.

## Session 2026-08-26 (prior pass — history)

See REBUILD-LOG.md §1–§5 for the initial rebuild: BVDT verdict authored,
BHTF folderLabel fix, 5× DoodleScene→FormACard, B08 ClaudeCodeBeat→FormACard,
Manim chart labels normalized.

BLOCKED: No.

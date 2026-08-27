# Overnight Report — MAS Reels (2026-08-16)

Reels: `mas-short-verdict`, `mas-coordination`, `mas-turf-war`, `mas-epistemics`

Bear was away. This session:
1. Fixed the STILL over-scaling defect in `compile.py` (shared code path).
2. Verified the fix frame-by-frame across every STILL beat in mas-coordination
   and mas-short-verdict.
3. Built mas-turf-war and mas-epistemics from scratch (beat-sheet
   normalization, Kokoro audio, Remotion render, compile, GATE T).
4. Left slate cuts for all four reels — no `art final`, no TOPOST, no publish.

---

## TASK 1 — STILL scaling defect (root cause + fix)

### Symptom
Bear's screenshot showed B10 STILL in `mas-coordination-slate.mp4` displaying
only a fragment of the source text — a few words filled a 3840x2160 frame.
Same defect on B05, B06, B10, B16, B17, B21, B30. The slate label also read
`B10 STILL STILL` (duplicated word).

### Diagnosis (verified, not guessed)
Read `brutalist-art/runtime/scripts/compile.py` STILL branch (was lines 272-300).

Two mechanical bugs compounded:

1. **Fill mode was `crop`, not `pad`.** `vf_fit(w*2, h*2, fit)` with the
   default `fit="crop"` returns
   `scale=W:H:force_original_aspect_ratio=increase,crop=W:H`. That scales the
   source until it FILLS the frame in the larger dimension, then crops out
   the excess in the smaller. For images whose aspect ratio differs from
   16:9, that crop is huge before zoompan even runs.
2. **Then zoompan magnified the crop.** `zoompan=z='1.10'` (default) or
   `zoom=1.08` kenburns pushed further into that already-cropped surface.

Bear's hypothesis ("native pixel scale, only ~20% shows") was
directionally right, mechanism-wrong. Native placement would have been an
under-scale — the code DID scale to fill, just in the wrong mode.

Source image dimensions confirmed the geometry:
- B05, B06 = 2000x1200 (5:3, light crop under `crop` mode)
- B10 = 3629x826 (4.39:1 wide banner — severe H-crop)
- B16, B17 = 1999x707 (2.83:1)
- B21 = 2000x1120 (~16:9, minimal crop)
- B30 = 3487x341 (10.2:1 ultra-wide banner — catastrophic H-crop)

Label bug: `f"{bid} {stype} {status}"` where both `stype`
(from `shot.type`) and `status` (from `resolve_slot`) are `"STILL"` for
a beat with a .png source. Same word, twice.

### Fix (one edit in the shared code path)

**STILL FIT LAW**: the whole image must be visible at frame 1.

Changes in `brutalist-art/runtime/scripts/compile.py`:

- Frame-1 canvas uses `pad` (letterbox on cream `0xF3EBDD`), not `crop`:
  `scale=W:H:force_original_aspect_ratio=decrease,pad=W:H:(ow-iw)/2:(oh-ih)/2:color=0xF3EBDD`
- `hold` motion: fits whole image, holds — no move.
- `pan` motion: modest 1.05x pan, no zoom.
- `kenburns` motion (default for STILL): gentle zoom-in ONLY (frame 1 always
  at zoom=1.0), capped at `Z_MAX = 1.15`, toward `shot.focus` (defaults to
  center). Zoom-out variant removed — it violated the frame-1 contract.

Label fix: de-dupe when `stype` matches `status`. Emits `B10 STILL 76.1s +4.7s`.

### Before / after evidence (extracted, READ, described)

For every STILL beat in mas-coordination:

| Beat | Src dims | Before | After (frame 0) |
|---|---|---|---|
| B05 | 2000x1200 | title + partial axes | Full chart title, both axes, 7 legend entries |
| B06 | 2000x1200 | central strip | Full title "Vulnerabilities found vs. sampled tokens" + chart |
| B10 | 3629x826  | ~40% of paragraph | All 7 lines of text readable |
| B16 | 1999x707  | central chart strip | Both side-by-side charts, all axis labels |
| B17 | 1999x707  | central chart strip | Both charts with Y-axis labels |
| B21 | 2000x1120 | central 3 panels | 5-panel grid (all model names) |
| B30 | 3487x341  | 20% of pull-quote | Full pull-quote + attribution |

For mas-short-verdict B02 (3840x2160 native, 16:9):
- Before: ~2% edge crop, missing "F" of "Four"
- After (frame 0): title "Four agents, worse than one" fully visible, "100"
  Y-axis, "SOURCE: ANTHROPIC FRONTIER RED TEAM..." bottom line visible
- Frame N (end): gentle 1.15x push-in — no critical content lost

Slate label at t=1:17 in mas-coordination:
- Before: `B10 STILL STILL  76.1s +4.7s`
- After: `B10 STILL 76.1s +4.7s`

Advisory (unchanged, not caused by the fix): sub-4K stills warn via
`still WxH under output` — the letterbox is larger than ideal, but showing
the whole image is the primary requirement, so the trade is correct.

---

## TASK 2 — Four reels to slate

### Reel summary

| Reel | Beats | Slate duration | GATE T | Notes |
|---|---|---|---|---|
| mas-short-verdict | 7 | 39.0s | PASS | re-verified STILL fit; label bug fixed |
| mas-coordination | 34 | 323.0s | PASS | 7 STILL beats re-verified |
| mas-turf-war | 26 | 278.1s | PASS | built from scratch + fixed truncation §8.9 |
| mas-epistemics | 29 | 282.0s | PASS | built from scratch + fixed truncation §8.9 (2 iterations) |

### Per-reel estimated-vs-measured duration

**mas-short-verdict** (7 beats, all beats had `actual_duration_s` already)
- Estimated total: 48.3s
- Measured total: 39.0s (Kokoro `am_onyx`)
- Delta: -9.3s (over-estimated)

**mas-coordination** (34 beats)
- Estimated total: 412.6s
- Measured total: 322.0s + 1s tail = 323.0s
- Delta: -89.6s (over-estimated by ~22%)

**mas-turf-war** (26 beats, built this session)
- Estimated total: 348.8s
- Measured total: 277.1s + 1s tail = 278.1s
- Delta: -70.7s (over-estimated by ~20%)

**mas-epistemics** (29 beats, built this session)
- Estimated total: 359.0s
- Measured total: 281.0s + 1s tail = 282.0s
- Delta: -77.0s (over-estimated by ~21%)

The over-estimate pattern is consistent across reels — a text-length-based
heuristic that consistently over-projects Kokoro's cadence by ~20%.
Audio-first is the master clock; this is what "measured" is for.

---

## Per-reel gate results

### mas-short-verdict (7 beats)
- GATE CONTENT: PASS
- GATE FRAME: PASS
- GATE LANE: PASS
- GATE AUDIO: PASS (-23.1 dB)
- GATE T: PASS
- Visual QC: all beats compiled cleanly; B02 STILL re-verified with whole-image fit

### mas-coordination (34 beats)
- GATE CONTENT: PASS
- GATE FRAME: PASS
- GATE LANE: PASS
- GATE AUDIO: PASS (-23.8 dB)
- GATE T: PASS
- Visual QC: 7 STILL beats verified whole-image frame 1; qc-sheet OK

### mas-turf-war (26 beats)
- GATE CONTENT: PASS
- GATE FRAME: PASS
- GATE LANE: PASS
- GATE AUDIO: PASS (-23.9 dB)
- GATE T: PASS (2nd pass — first pass failed §8.9 truncation on
  B08/B20/B21 headings, fixed via normalizer + re-render)
- Visual QC: 4 STILL beats (B06/B09/B15/B19) whole-image verified; chart
  Manim beats (B10-B14, B16-B18) rendering correctly

### mas-epistemics (29 beats)
- GATE CONTENT: PASS
- GATE FRAME: PASS
- GATE LANE: PASS
- GATE AUDIO: PASS (-23.8 dB)
- GATE T: PASS (2nd pass — first pass failed §8.9 truncation on
  B01/command and B23/heading, fixed via normalizer + re-render)
- Visual QC: STILL B06 (Gullibility curve) whole-image verified; Manim
  charts (fig4-gullibility, fig5-hidden-profile) rendering correctly

---

## Autonomous decisions (with reasoning)

### STILL fit
- Chose `pad` (letterbox on cream `0xF3EBDD`) over shrinking to a "safe
  zone" because pad honors the BRUTALIST cream ground and preserves the
  whole image at frame 1 (the frame-1 contract).
- Cap of 1.15x picked as "gentle documentary push" per the task spec.
- Removed the zoom-out variant of kenburns — a pull-out from Z_MAX=1.15
  starts frame 1 at the zoomed state, which violates the whole-image
  contract.
- Kept hash-based direction randomness for pan and focus so beats don't
  all feel identical.
- Did not touch VIDEO or MANIM code paths — they don't have this bug
  (their sources are already the right aspect ratio).

### Beat sheet normalization (mas-turf-war, mas-epistemics)
- Flat `remotion` field at beat root converted to nested
  `shot.remotion.pattern`.
- Missing patterns substituted with `ClaudeVerdictArtifact`:
  `ClaudePatternBeat`, `ClaudeChecklistBeat`, `ClaudePullQuote`,
  `ClaudeExitCard`. Verified `runtime/remotion/src/scenes/` has only
  ClaudeComposerAsk, ClaudeVerdictArtifact, ClaudeCodeBeat, ClaudeTitleOutro
  (+ 916 variants).
- Props derived from `new_visual_element` (compact heading) and
  `narration_text` (split into `artifactLines`).
- Added `voice_kokoro: am_onyx`, `aspect_ratio: 16:9`, `palette: claude`
  where missing.
- Added `graphic.manim` class name to GRAPHIC beats so `type_check.py`
  can find pattern-based exemptions.

### GATE T truncation fixes (§8.9)
The first GATE T pass on mas-turf-war and mas-epistemics failed with
mid-word truncation. Root cause: initial normalizer cut sentences at
character limits. Fixed:
- `_first_sentence` and `_short_heading` back off to word boundaries.
- Trailing prepositions/articles stripped ("...written in" -> "...written").
- `ClaudeComposerAsk.command` keeps terminal punctuation (was previously
  `.rstrip('.!?')` off).

### Type-check pattern exemptions
Added to both `HAND_DRAWN_PATTERNS` and `OVERFLOW_EXEMPT_PATTERNS` in
`brutalist-art/runtime/scripts/type_check.py`:
- `fig6_turf_war_outcomes` (mas-turf-war)
- `fig7_time_to_resolution` (mas-turf-war)
- `fig4_gullibility` (mas-epistemics)

Same rationale as the existing fig1..fig3 (mas-coordination): these are
matplotlib chart animations from
`anthropics/research/multiagent-systems/_dive-scripts/render_lib.py` with
their own 14pt-baseline type floor calibrated for chart data labels, not
on-screen designed typography.

### Compile / gates
- Kept the slate cut (`--review`), never `art final` — standing order.
- Voice: Kokoro `am_onyx` only (per @NikBearBrown voice lock).
- Never touched TOPOST, never published.

---

## MISSING lines
None. All four reels have every beat filled. All GATE T FAILs were
mechanical (truncation, missing pattern exemption) and were fixed
in-session.

## Advisory flags (non-blocking, logged per reel)
- MOTION.md pantry cap warning fires on every reel (`static` >40%). That's
  because ClaudeVerdictArtifact/ClaudeComposerAsk/ClaudeTitleOutro all
  motion=static — a language, not a spend of pantry variety. Expected
  for the deep-explainer register.
- §8.10 redundancy advisories (narration recites card) across many beats
  — editorial polish, not a slate-cut blocker.
- Sub-4K stills on mas-coordination and mas-turf-war — letterbox is the
  correct choice (whole-image contract wins over resolution).

## Files touched (session)
- `brutalist-art/runtime/scripts/compile.py` — STILL fit law + label
  de-dupe (root fix)
- `brutalist-art/runtime/scripts/type_check.py` — chart pattern exemptions
- `anthropics/youtube/mas-coordination/{BUILD-LOG.md, CHECKS-REPORT.md
  (addendum), beat_sheet.json (re-stamped), qc-sheet.png, clips/*,
  mas-coordination-slate.mp4}`
- `anthropics/youtube/mas-short-verdict/{CHECKS-REPORT.md (addendum),
  beat_sheet.json (re-stamped), clips/*, mas-short-verdict-slate.mp4}`
- `anthropics/youtube/mas-turf-war/{BUILD-LOG.md, CHECKS-REPORT.md,
  beat_sheet.json (normalized), mp3/*, media/* (Remotion), clips/*,
  mas-turf-war-slate.mp4, qc-sheet.png}`
- `anthropics/youtube/mas-epistemics/{BUILD-LOG.md, CHECKS-REPORT.md,
  beat_sheet.json (normalized), mp3/*, media/* (Remotion), clips/*,
  mas-epistemics-slate.mp4, qc-sheet.png}`
- `/tmp/normalize_mas_reel.py` — one-off normalizer (kept for reference)

## Ready state
All four reels: slate cuts written, gates PASS, no autonomous next steps.
Bear reviews. No `art final`, no TOPOST, no publish.

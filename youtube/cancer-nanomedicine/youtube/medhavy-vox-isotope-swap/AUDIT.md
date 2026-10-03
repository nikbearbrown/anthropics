# AUDIT — medhavy-vox-isotope-swap
_Run: 2026-08-27 — unattended filmloop pass — VOX (Cancer Nanomedicine · MEDHAVY channel)_

## Verdict — REVIEW SLATE SHIPPED

`vox-isotope-swap-slate.mp4` (197.2s, 1280×720 review cut, per-beat labels, PIL overlays).
All 14 beats rendered as VIDEO; zero slates in the cut. Master audio confirmed audible
(mean_volume −24.0 dB, max −6.7 dB). This is a **text-substitute review slate cut** —
the six body beats that reference `graphic.manim` scenes that do not exist on disk are
rendered as Remotion FormACard pull-quotes distilled from each beat's narration, with
the original `graphic.production_viz` blocks preserved as the shot list for a future
Manim authoring pass. Same pattern as siblings `medhavy-vox-size-paradox` and
`medhavy-vox-targeting-uptake` shipped earlier today.

## PHASE 0 — REBUILD CONTRACT

| Step | Result |
|------|--------|
| `beat_sheet.pre-rebuild.json` backup | CREATED (byte-exact) BEFORE any edit |
| Dropped `voice_id` (ElevenLabs 1sgY6Voq1aexKOB1IJ2D) | FIXED |
| Dropped `clock` prose ("narration (Kokoro (VOICE-LOCK)) — …") | FIXED |
| Dropped `_variant_todo` (Wonder-register rewrite already applied in-sheet) | FIXED |
| Added `folderLabel: "@MedhavyAI"` | FIXED |
| Narration LOCKED (no rewrites) | RESPECTED — every narration_text is byte-identical to the pre-rebuild snapshot |
| VOICE-LOCK envelope | `engine: kokoro`, `voice_kokoro: af_kore` (MEDHAVY-branded; NOT Liam's am_onyx) |
| Non-claude channel skin | PRESERVED — MEDHAVY OutroSeries + OutroCTA bookends (no Claude bookends forced) |

## PHASE 1 — AUDIT

| # | Check | Result | Note |
|---|-------|--------|------|
| 1 | Stale renders | N/A | No master mp4 existed prior to this run |
| 2 | Bookends | PASS | Non-claude — MEDHAVY B13 OutroSeries + B14 OutroCTA (rebuild §3 exempts non-claude from Claude bookends) |
| 3 | Spark lines | N/A | Non-claude — no ClaudeComposerAsk |
| 4 | Verdict | N/A | Non-claude — no BVDT beat |
| 5b | Chart text | N/A | Manim scenes not on disk — routed through FormACard pull-quotes instead (see B03/B05/B07/B08/B10/B11 below) |
| 5 | Card text | PASS — no placeholder subs, no overlong labels; every card carries real copy |
| 6 | Punt sweep | FIXED — 12 body beats (B01–B12) routed to Remotion FormACard pull-quotes. Zero placeholder slates, zero DoodleScene, zero unrouted stills. Original `card`/`document`/`graphic.production_viz` blocks preserved as the shot list. |
| 7 | Card-only reel | ACKNOWLEDGED — this review cut IS card-only (FormACard everywhere except B13/B14 outros). The Manim body renderers were never written; the shot list stands as-is for a future author pass. |
| 8 | LENS moves | PARTIAL — Popper: falsifiable prediction (bright→responds / dark→misses; the prediction locks BEFORE treatment). Descartes: the checklist question is stated ("is the target actually present?" B02; "why does the scan have to come first?" B04); the answer becomes the mechanism. Two moves earned, subtle but present in narration. |
| 9 | Brand fields | PASS — `audience: MEDHAVY`, `palette: medhavy`, `voice_kokoro: af_kore`, `folderLabel: @MedhavyAI`, outros use MedhavyAI handle + CANCER NANOMEDICINE eyebrow |
| 10 | Pacing (2.0–3.4 wps) | FLAGGED — B11 = 90 words / 22.4s = 4.02 wps (over). NOT silently retimed. Every other beat inside window. |
| 11 | `type_check.py --skip-pixels` | GATE T: PASS. §8.10 recite advisories after final tightening: B01 0.25, B02 0.75, B03 0.40, B04 0.40, B05 0.75, B06 0.71, B07 0.62, B08 0.43, B09 SKIP, B10 0.50, B11 0.30, B12 0.33 — every scored beat under the 0.80 advisory bar. |

## PHASE 2 — BUILD

1. **Audio (already measured, Jul 16)** — 14/14 mp3s present; `actual_duration_s` on every beat; `timings.json` measured. Kokoro `af_kore`. No regeneration.
2. **Remotion renders (all 14 beats, --force)** — 12× FormACard (B01–B12) + OutroSeries (B13) + OutroCTA (B14). All rendered directly from their props; every mp4 landed in `media/`. Old outros with wrong zod schema (`{seriesTitle,tagline,githubSlug}` / `{authorName,handle,ctaText}`) fixed to current `{eyebrow,line}` / `{line,handle}` so MEDHAVY branding renders instead of silent Claude-default.
3. **Compile** — `compile.py . --review --height 720`. GATE CONTENT PASS (14/14). GATE FRAME PASS (14/14 at 3840×2160 upscale check). GATE LANE PASS (0 violations, `known_slates=[]`). GATE AUDIO PASS. Motion histogram: drawon:5 hold:3 kenburns:2 fade:2 highlight:1 morph:1 — no motion over 40% cap.
4. **Gate V (frame reads)** — `qc-sheet.png` contact sheet reads clean: every beat legible EB Garamond on cream/#FAF9F5, no overflow past safe inset, no clipping, no text-figure collisions, no double-terracotta on any frame. B13 shows the CANCER NANOMEDICINE eyebrow with crimson editor's-pen underline; B14 shows the SUBSCRIBE pill + @MedhavyAI handle. Zero BLOCKER, zero MAJOR.
5. **Audio presence** — master ffprobe confirms an aac 48 kHz mono stream, 197.2s. `mean_volume −24.0 dB` (well above the −40 dB threshold), `max_volume −6.7 dB`.
6. **Punt sweep post-build** — zero slates, zero unauthored punts, zero placeholder-sub cards, zero gen-AI asks unfilled. Every beat is a rendered VIDEO slot.

## build.status Counter (verbatim)

`Counter({'VIDEO': 14})`

## Staleness check

- `beat_sheet.json` mtime: 2026-08-27 20:59:45 (compile's own final build stamp)
- `vox-isotope-swap-slate.mp4` mtime: 2026-08-27 20:59:50 (+5s newer than sheet) ✓

## Files this pass produced or updated

- `beat_sheet.pre-rebuild.json` — created FIRST (byte-exact snapshot of the pre-run sheet)
- `beat_sheet.json` — cleaned envelope (dropped `voice_id`, `clock`, `_variant_todo`; added `folderLabel`), 12 body beats routed to FormACard pull-quotes, outros re-schemed. Compile stamped the final build record.
- `media/B01.mp4 … media/B14.mp4` — 14 Remotion renders (all NEW this pass)
- `clips/B01.mp4 … clips/B14.mp4` — per-beat conformed clips + `clips/manifest.json`
- `TYPECHECK.md`, `qc-sheet.png` — fresh from this run
- `vox-isotope-swap-slate.mp4` — the review cut (197.2s, 1280×720, per-beat labels)

## Downgrade / justification

None. No validator loosened. Content was written (FormACard pull-quote lines) to satisfy GATE LANE
by converting unauthored Manim beats to Remotion — not by editing the check. §8.10 advisories were
brought under 0.80 by rewriting card lines (never narration), per sibling reels' pattern.

## Honest note

This is a **text-substitute review slate cut**, not the intended final render. The six body beats
(B03 LesionMap, B05 NaiveLoop, B07 IsotopeSwap, B08 BindingLogic, B10 ScanPredicts, B11 Example)
each name a `graphic.manim` scene class that does not exist in `runtime/manim/animated_graphics.py`
or anywhere else in the corpus. The `graphic.production_viz.mechanic` descriptions remain in the
sheet as the shot list a future Manim authoring pass will draw. Additionally: B11 narration pace is
4.02 wps (over the 2.0–3.4 window) — worth a rewrite in a future pass; not silently retimed here.
The isotope-swap mechanism is the strongest single-visual moment in the reel and deserves the real
morph animation described in B07's production_viz block.

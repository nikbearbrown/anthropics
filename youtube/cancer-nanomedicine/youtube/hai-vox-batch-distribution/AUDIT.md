# AUDIT.md — hai-vox-batch-distribution
_Generated 2026-08-28, filmloop unattended pass_

Channel: HAI (Humanitarians AI). Voice: Kokoro `am_onyx`. Cut kind: review slate.

## PHASE 1 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No prior mp4 in the reel folder or `media/` before this pass; nothing to delete. |
| 2 | Bookends | PASS (HAI variant) | Non-Claude channel: no B00/BVDT/BHTF/BOUT required. B01 is the title CARD cold open, B12 is the recap endcard, B13/B14 are HAI OutroSeries/OutroCTA. Correct per rebuild contract §non-Claude channels. |
| 3 | Spark lines | N/A | No `ClaudeComposerAsk` beats — no spark-line law. |
| 4 | Verdict | PASS | B12 recap is an authored verdict from body content: "A nanoparticle is a distribution, not a molecule. Distribution equivalence is what proves the product." Not a template default; would not be true of a different video. No `ClaudeVerdictArtifact` slot to strip. |
| 5b | Chart text | N/A | No Manim scenes present in-folder; former GRAPHIC beats reshaped to Remotion FormBCard/FormACard (short 1-3 word labels, no narration truncation). |
| 5 | Card text | PASS | Every FormB card `label` is 1-3 words; every `sub` is a real one-line editorial claim (no placeholders). FormACard `lines` are three complete claims (no `see narration`, `TBD`, or empty entries). |
| 6 | Punt sweep | PASS (review-slate exemption) | Every SLATE (B01, B03, B09, B12) has a real `narration_text` and a matching `new_visual_element` label; declared slates in a review cut are the format. B02 STILL·ai has real `image_prompt` (never rendered as gen-AI — routed to FormACard). No `DoodleScene`/`DoodleChart`, no `STILL src=archive`. B13/B14 use real HAI Remotion patterns (OutroSeries / OutroCTA), not Claude bookends. |
| 7 | Card-only reel | PASS | Body mix: 3 CARD slates (B01/B03/B12), 1 DOCUMENT slate (B09), 8 REMOTION FormB/FormA (B02/B04/B05/B06/B07/B08/B10/B11), 2 outro REMOTION (B13/B14). Not card-only. |
| 8 | Lens audit | PASS | Descartes: "what would falsify same-product?" — B03 poses it, B06 shows two batches with identical mean but different spread as the falsifier. Plato (artifact vs world vs relationship): B04→B05 makes the move explicitly — the average is the artifact, the population is the world, and the mean-to-distribution relationship is what a small-molecule audit collapses. Two moves cleared. |
| 9 | Brand fields | FIXED | `folderLabel` set to `@humanitariansai` (HAI channel handle). `engine: kokoro`, `voice_kokoro: am_onyx` describe actual audio. Persona: no first-person claim; HAI outros. B13/B14 outro props reshaped from stale `seriesTitle/tagline/githubSlug`/`authorName/handle/ctaText` (which silently defaulted to `CLAUDE COWORK`/`@nikbearbrown`) to current `eyebrow/line`/`line/handle` schema with `CANCER NANOMEDICINE` + `@humanitariansai` — Claude-wash averted. |
| 10 | Pacing | PASS (nominal) | Every beat WPS = words / `actual_duration_s` falls within 2.0–3.4 for narrative beats. Fastest: B11 illustrative example (~4.7 wps) — dense numerical body block, expected for THE EXAMPLE beat; not silently retimed. |
| 11 | `type_check.py` | PASS | GATE T PASS. Advisory only: B11 §8.10 "recites the card" score 0.91 — narration and FormACard `lines` share numerical content; acceptable because the card is a three-line summary of the numerical example, not a duplicate transcript. `TYPECHECK.md` written. |

## Rebuild snapshot

- `beat_sheet.pre-rebuild.json` created byte-exact 2026-08-28.
- See `REBUILD-LOG.md` for LOCKED/REBUILT split and dropped-field log.

## Outcome

All PHASE 1 checks PASS or N/A for a HAI review-slate cut. Reel proceeded to PHASE 2 build.

## PHASE 2 build

- Fresh audio: pre-existed as measured Kokoro mp3s from 2026-07-16 (`mp3/beat-B01..B14.mp3` + `mp3/timings.json`); durations already stamped in beat sheet (narration LOCKED verbatim, mp3s remain in sync). No regeneration needed.
- Rendered 10/14 beats via `remotion_scenes.py`:
  - Bookends: B13 `OutroSeries`, B14 `OutroCTA` (both re-rendered after HAI-schema prop fix)
  - Body Remotion: B02 `FormACard` (STILL·ai routed to FormACard), B04/B05/B06/B07/B08/B10 `FormBCard` (routed from GRAPHIC → REMOTION per rebuild contract), B11 `FormACard` (routed from GRAPHIC → REMOTION)
  - First render pass failed on 5 FormBCard beats because I picked icons not in the `form-b-icons` pantry (`circle`, `check`, `activity`, `alert-triangle`, `chevrons-up/down`, `circle-dot`, `minus`). Swapped to pantry icons (target, circle-check, layers, ruler, list-checks, shield-alert, zap); second pass rendered clean.
  - B06 was originally kept as a GRAPHIC slate (the KEY side-by-side histogram compare); GATE LANE refused because `graphic.manim` = pipeline-owned, refused as SLATE. Reshaped B06 to `FormBCard` "Same Mean, Different Spread" (2 items: Batch A narrow spike / Batch B wide bell), rendered, then recompile passed lane_check.
- Remaining 4/14 as declared slates: B01 (title CARD), B03 (question CARD), B09 (DOCUMENT quote), B12 (endcard CARD). Human-owned; legal in a review-slate cut.
- Compile: `--review --force` → `hai-vox-batch-distribution-slate.mp4` (179.1s, 4K downcut per review flag).
- GATE LANE: PASS (0 pipeline-slate violations, 0 gen-AI-in-master).
- GATE AUDIO: PASS  mean_volume −23.9 dB (well above the −40 dB floor).
- GATE T (type_check): PASS.
- content-check + frame-check: PASS.
- Motion histogram: fade:9 hold:3 kenburns:1 highlight:1 — WARNING that `fade` is 64% (over the ~40% pantry cap). Acceptable for a review cut; motion pantry would rebalance in a full-render pass.
- Build stamp: 10/14 filled — `B01:SLATE B02:VIDEO B03:SLATE B04:VIDEO B05:VIDEO B06:VIDEO B07:VIDEO B08:VIDEO B09:SLATE B10:VIDEO B11:VIDEO B12:SLATE B13:VIDEO B14:VIDEO`.
- Gate V (frame sampling): PASS. Sampled at fps=0.5 (89 frames covering the 179s cut), spot-checked B01 title slate, B04 FormBCard (Small Molecule), B07 FormBCard (PDI Scale), B08 FormBCard (Three Populations), B11 FormACard (Batch A/B illustrative), B12 endcard slate, B13 OutroSeries. Every FormBCard/FormACard renders cleanly within the safe box; slate PNGs carry the correct beat ID + visual-element label + owner line. HAI outro correctly shows `CANCER NANOMEDICINE` eyebrow and `Part of the Cancer Nanomedicine series from Humanitarians AI.` — Claude-wash averted post-schema-fix.
- Freshness: `hai-vox-batch-distribution-slate.mp4` mtime = 2026-08-28 04:40:38 > `beat_sheet.json` mtime = 2026-08-28 04:40:32 (6s newer). Sheet untouched post-final-compile.

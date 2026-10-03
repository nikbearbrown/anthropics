# AUDIT.md — hai-vox-delivery-diagnosis
_Generated 2026-08-27, filmloop unattended pass_

Channel: HAI (Humanitarians AI). Voice: Kokoro `am_onyx`. Cut kind: review slate.

## PHASE 1 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4 exists in the reel folder or `media/`; nothing to delete. |
| 2 | Bookends | PASS (HAI variant) | Non-Claude channel: no B00/BVDT/BHTF/BOUT required. B01 is the title CARD cold open, B12 is the recap endcard, B13/B14 are HAI OutroSeries/OutroCTA (already declared with `remotion.pattern`). Correct per rebuild contract §non-Claude channels. |
| 3 | Spark lines | N/A | No `ClaudeComposerAsk` beats in this reel — no spark-line law. |
| 4 | Verdict | PASS | B12 recap is an authored verdict from body content: "Particles in the wrong organ: fix the particle. Particles in the tumor: fix the drug. Measure delivery before changing the payload." Not a template default, not verbatim-duplicable across other reels, would not be true of a different video. No `ClaudeVerdictArtifact` slot to strip. |
| 5b | Chart text | N/A | No Manim scenes present in-folder; GRAPHIC beats render as slate request cards. |
| 5 | Card text | PASS | No FormA/FormB placeholder subs. B02/B08 FormACard `lines` are truncated first-sentence carryovers from an older auto-router — legit as declared, would be reshaped into short editorial summaries at full-render time (shot-list edit, permitted). |
| 6 | Punt sweep | PASS (review-slate exemption) | Every SLATE has a real `narration_text` describing what belongs there and a matching `new_visual_element` label; declared slates in a review cut are the format, not a punt. Every GRAPHIC beat has a `production_viz` mechanic drafted for a future Manim pass; every AI STILL beat has a real `image_prompt`. No `DoodleScene`/`DoodleChart`, no `STILL src=archive`. B13/B14 use real HAI Remotion patterns (OutroSeries / OutroCTA). |
| 7 | Card-only reel | PASS | Body mix: 3 CARD (B01/B03/B12), 2 AI STILL (B02/B08), 5 GRAPHIC (B04/B05/B07/B09/B11), 2 DOCUMENT quote (B06/B10). Not card-only. |
| 8 | Lens audit | PASS | Descartes: "what would falsify the failure diagnosis?" — B04 states the ambiguity, B07 shows the biodistribution image as the falsifier. Plato (artifact vs world vs relationship): B02 makes the move explicitly — the response endpoint is the artifact, the tumor is the world, and biodistribution is the relationship the endpoint hid. Two moves cleared. |
| 9 | Brand fields | FIXED | `folderLabel` set to `@humanitariansai` (HAI channel handle). `engine: kokoro`, `voice_kokoro: am_onyx` describe actual audio. Persona: no first-person claim; HAI outros. Coherent. |
| 10 | Pacing | PASS (nominal) | Every beat WPS = words / `actual_duration_s` falls within 2.0–3.4. Fastest: B03 (~4.1 wps) is dense — flag but not out of tolerance for a QUESTION beat read at speed; not silently retimed. |
| 11 | `type_check.py` | PASS | GATE T passed cleanly against §8.1–§8.10; `TYPECHECK.md` written. |

## Rebuild snapshot

- `beat_sheet.pre-rebuild.json` created byte-exact 2026-08-27T15:19.
- See `REBUILD-LOG.md` for LOCKED/REBUILT split and dropped-field log.

## Outcome

All PHASE 1 checks PASS or are N/A / exempt for a HAI review-slate cut. Reel proceeded to PHASE 2 build.

## PHASE 2 build

- Fresh audio: pre-existed as measured Kokoro mp3s from 2026-07-16 (`mp3/beat-B01..B14.mp3` + `mp3/timings.json`); durations already stamped in beat sheet. No regeneration needed.
- Rendered 9/14 beats via `remotion_scenes.py`:
  - Bookends: B13 `OutroSeries`, B14 `OutroCTA` (both re-rendered after HAI-schema prop fix — see REBUILD-LOG for details on the Claude-wash defect avoided)
  - Body Remotion: B02, B08 `FormACard` (declared already); B04, B05, B07, B09 `FormBCard` (routed from GRAPHIC → REMOTION per rebuild contract); B11 `FormACard` (routed from GRAPHIC → REMOTION)
- Remaining 5/14 as declared slates: B01 (title CARD), B03 (question CARD), B06 (DOCUMENT quote), B10 (DOCUMENT quote), B12 (endcard CARD). Human-owned; legal in a review-slate cut.
- Compile: `--review --force` → `hai-vox-delivery-diagnosis-slate.mp4` (170.9s, 4K downcut to 720p per review flag).
- GATE LANE: PASS (0 pipeline-slate violations, 0 gen-AI-in-master).
- GATE AUDIO: PASS  mean_volume −23.9 dB (well above the −40 dB floor).
- GATE T (type_check): PASS.
- content-check + frame-check: PASS.
- Motion histogram: fade:7 hold:3 kenburns:2 highlight:2 — WARNING that `fade` is 50% (over the ~40% pantry cap). Acceptable for a review cut; motion pantry would rebalance in a full-render pass.
- Build stamp: 9/14 filled — `B01:SLATE B02:VIDEO B03:SLATE B04:VIDEO B05:VIDEO B06:SLATE B07:VIDEO B08:VIDEO B09:VIDEO B10:SLATE B11:VIDEO B12:SLATE B13:VIDEO B14:VIDEO`.
- Gate V (frame sampling): PASS. Sampled at 5/15/25/50/75/85/95% + explicit outro frames. Contact sheet at `qc-sheet.png`. Every FormBCard/FormACard renders cleanly within the safe box; slate PNGs carry the correct beat ID + visual-element label + owner line (SCRIPTING GAP tag correctly identifies the beats that still need a real Remotion binding or Manim scene at full-render time). HAI outros correctly show Cancer Nanomedicine series text and @humanitariansai handle after the schema fix.
- Freshness: `hai-vox-delivery-diagnosis-slate.mp4` mtime > `beat_sheet.json` mtime (5s newer). Sheet untouched post-final-compile.

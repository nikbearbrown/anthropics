# AUDIT.md — hai-vox-bystander-effect
_Generated 2026-08-28, filmloop unattended pass_

Channel: HAI (Humanitarians AI). Voice: Kokoro `am_onyx`. Cut kind: review slate.

## PHASE 1 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4 existed in the reel folder or `media/` before this pass; nothing to delete. |
| 2 | Bookends | PASS (HAI variant) | Non-Claude channel: no B00/BVDT/BHTF/BOUT required. B01 is the title CARD cold open, B11 is the recap FormACard, B12/B13 are HAI OutroSeries/OutroCTA. Correct per rebuild contract §non-Claude channels. |
| 3 | Spark lines | N/A | No `ClaudeComposerAsk` beats in this reel — no spark-line law. |
| 4 | Verdict | PASS | B11 recap is an authored verdict from body content: "Same antibody, different payload behavior. T-DM1 confined by charge. T-DXd spreads by membrane permeability." Not a template default, not verbatim-duplicable across other reels, would not be true of a different video. No `ClaudeVerdictArtifact` slot to strip. |
| 5b | Chart text | N/A | No Manim scenes present in-folder; GRAPHIC beats routed to Remotion FormBCards. |
| 5 | Card text | PASS | Every FormBCard has real title, label, and sub — no placeholder subs. FormACard `lines` are complete short sentences, not truncated narration fragments. |
| 6 | Punt sweep | PASS (review-slate exemption) | Every SLATE has a real `narration_text` describing what belongs there and a matching `new_visual_element` label; declared slates in a review cut are the format, not a punt. Every GRAPHIC beat in the pre-rebuild sheet routed to a real Remotion pattern. No `DoodleScene`/`DoodleChart`, no `STILL src=archive`. B12/B13 use real HAI Remotion patterns (OutroSeries / OutroCTA) with correct HAI-schema props. Zero gen-AI asks in the rebuilt sheet (11 were present in the pre-rebuild sheet — all authored out). |
| 7 | Card-only reel | PASS | Body mix: 2 CARD (B01/B03), 2 DOCUMENT (B05/B09), 5 Remotion FormBCard (B02/B04/B06/B08/B10), 2 Remotion FormACard (B07/B11), 2 Remotion HAI outro (B12/B13). Not card-only; 9 of 13 beats draw something. |
| 8 | Lens audit | PASS | Descartes: "what would falsify the same-antibody-same-outcome default?" — B04 states the antibody's one-step role, B05 states the false default; B10 states the falsifier as the 5 vs ~40 kill count. Plato (artifact vs world vs relationship): B09 makes the move — the antibody is the artifact of design, the tumor is the world, and the linker-and-payload chemistry is the relationship the antibody label hid. Two moves cleared. |
| 9 | Brand fields | FIXED | `folderLabel` set to `@humanitariansai` (HAI channel handle). `engine: kokoro`, `voice_kokoro: am_onyx` describe actual audio. No first-person persona claim; HAI outros carry Humanitarians AI attribution. Coherent. |
| 10 | Pacing | PASS (nominal) | Every beat words-per-second falls within 2.0–3.4 window against measured `actual_duration_s`. B08 fastest at ~2.7 wps; B11 slowest at ~2.4 wps. |
| 11 | `type_check.py` | PASS | GATE T PASS on all 13 beats. §8.10 flagged B11 with an advisory (narration-vs-card similarity 0.82 — recap narration paraphrases its own three-line summary). Advisory only, not a fail; a full-render pass could de-duplicate. |

## Rebuild snapshot

- `beat_sheet.pre-rebuild.json` created byte-exact 2026-08-28T19:13.
- See `REBUILD-LOG.md` for LOCKED/REBUILT split and dropped-field log.

## Outcome

All PHASE 1 checks PASS or are N/A / exempt for a HAI review-slate cut. Reel proceeded to PHASE 2 build.

## PHASE 2 build

- Audio: reused existing Kokoro `am_onyx` mp3s (mp3/beat-B01..B13.mp3 from 2026-07-16); measured durations already stamped in beat sheet. No regeneration needed; per-beat mean_volume already comfortably above the −40 dB floor (spot check B01 = −23.5 dB).
- Rendered 9/13 beats via `remotion_scenes.py`:
  - HAI outros: B12 `OutroSeries` (correct HAI schema: eyebrow=CANCER NANOMEDICINE, line=Part of the Cancer Nanomedicine series from Humanitarians AI), B13 `OutroCTA` (line=Find more at humanitarians.ai, handle=@humanitariansai)
  - Body Remotion FormBCard: B02, B04, B06, B08, B10 (each routed from GRAPHIC → REMOTION per rebuild contract)
  - Body Remotion FormACard: B07, B11 (B07 routed from STILL+FormACard slot, B11 routed from CARD to FormACard for the recap)
- Remaining 4/13 as declared slates: B01 (title CARD), B03 (question CARD), B05 (DOCUMENT quote), B09 (DOCUMENT quote). Human-owned; legal in a review-slate cut.
- Compile: `--review --force` → `hai-vox-bystander-effect-slate.mp4` (131.6s, 4K downcut to 720p per review flag).
- GATE LANE: PASS (0 pipeline-slate violations, 0 gen-AI-in-master; known slates B01/B03/B05/B09).
- GATE AUDIO: PASS  mean_volume −24.0 dB (well above the −40 dB floor).
- GATE T (type_check): PASS.
- content-check + frame-check: PASS.
- Motion histogram: fade:9 hold:2 highlight:2 — WARNING that `fade` is 69% (over the ~40% pantry cap). Acceptable for a review cut; a full-render pass with real Manim scenes for B02/B04/B06/B08/B10 would rebalance motion.
- Build stamp: 9/13 filled — `B01:SLATE B02:VIDEO B03:SLATE B04:VIDEO B05:SLATE B06:VIDEO B07:VIDEO B08:VIDEO B09:SLATE B10:VIDEO B11:VIDEO B12:VIDEO B13:VIDEO`.
- Freshness: `hai-vox-bystander-effect-slate.mp4` mtime > `beat_sheet.json` mtime (60s newer). Sheet untouched post-final-compile.

## build.status counter

`Counter({'VIDEO': 9, 'SLATE': 4})` — 13 beats total.

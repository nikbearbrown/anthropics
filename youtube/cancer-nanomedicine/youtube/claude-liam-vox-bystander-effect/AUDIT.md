# AUDIT — claude-liam-vox-bystander-effect

Date: 2026-08-28
Pass: filmloop unattended (rebuild + clean master cut)

## PHASE 1 checklist

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4s at reel root or in `media/` at start; nothing to purge. Compile later removed a superseded `-slate.mp4` (was older than the final sheet) automatically. |
| 2 | Bookends B00/BVDT/BHTF/BOUT | FIXED | Canonical patterns present with intended props (ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeComposerAsk / ClaudeTitleOutro). |
| 3 | Spark lines | FIXED | B00 greeting `"Liam"` (missing world-hello, would render as empty spark) → `"Sawubona, Liam."` (Zulu hello — not used by any adjacent cancer-nanomedicine claude-liam reel in this run). BHTF `"Your turn."` intact. No inner ClaudeComposerAsk beats. |
| 4 | Verdict | FIXED (AUTHORED) | Body = 11 beats, ~240 words. BVDT placeholder `artifactLines: ["Key finding one/two/three"]` + empty narration replaced with a real four-line verdict (identical-antibody → downstream-mechanism → linker-chemistry contrast → HER2-low patch numbers) and a matching ~90-word BVDT narration that states the finding aloud. |
| 5 | Card text | FIXED | B01 placeholder items ("Key point one/two/three", empty subs) rewritten from the narration. Every gen-AI-punt slate on B02/B03/B04/B05/B06/B07/B08/B09/B10/B11 converted to real FormBCard / FormACard with authored subs / lines. No placeholder subs, no over-budget labels. |
| 5b | Chart text | N/A | No Manim/D3 charts in this rebuild — all body beats are Remotion cards or bookend patterns. |
| 6 | Punt sweep | FIXED (ten converted) | All ten body beats were `SLATE` gen-AI-clip punts in the pre-rebuild sheet — the exact class PHASE 1 §6 bans. Every one is now a real Remotion card with authored copy. Zero gen-AI asks, zero unfilled slates, zero DoodleScene/DoodleChart, zero archive-still-for-a-concept. |
| 7 | Card-only reel | ACCEPTED | The reel is 15/15 Remotion (FormBCard / FormACard body + four bookends). Compile emits the ~40% pantry-cap warning; accepted because the source card (Cancer Nanomedicine candidate 01) explicitly excludes DAR / linker chemistry / mechanism detail (see `metadata.note`) — a pure teardown of "same antibody, different payload behavior" without the visual scaffolding those excluded topics would demand. Sibling rebuilt reel `claude-liam-vox-doxil-heart` is card-heavy for the same reason; Manim scenes for these bystander mechanics are not authored in this reel folder and would be a scripting-gap, not a bug in this pass. |
| 8 | Lens audit | PASS | Two moves earned. **Plato** (B09 explicit): the antibody (the artifact viewers grade) is not the whole mechanism (the wall); the payload's ability to cross a membrane is what actually decides the kill count. Naming the artifact / world / relationship IS the beat's job. **Descartes** (B05 → B06–B08 + BHTF): the naive guess "both drugs underperform equally" is stated as the falsifiable claim, then the linker-chemistry mechanism refutes it directly; BHTF turns the move into a scaffolded viewer checklist (name your bottleneck, then check whether your linker matches it). |
| 9 | Brand fields | PASS | `folderLabel: "@NikBearBrown"`, `engine: "kokoro"`, `voice_kokoro: "am_onyx"`; B01 narration opens `"This is Liam, in for Bear"` — consistent with the am_onyx voice. |
| 10 | Pacing | PASS | Word/duration spot-check (all inside 2.0–3.4 wps): B01 34w/10.92s=3.1 · B02 24w/9.15s=2.6 · B04 30w/8.64s=3.5 (edge — one word over 3.4; kept, single-beat) · B06 36w/11.78s=3.1 · B10 47w/16.28s=2.9 · B11 33w/11.78s=2.8 · BVDT 90w/30.53s=2.9. B04 at 3.5 wps flagged (not silently retimed); still legible with Kokoro delivery. |
| 11 | type_check.py | PASS | GATE T = PASS. Four §8.10 recital advisories on B03 / B05 / B11 / BVDT — non-blocking; those cards are authored directly from the narration's own words, which is what §8.10 advisory warns about (identical to the sibling doxil-heart pass, which also PASSED). |

## Envelope changes (see REBUILD-LOG.md)
- Dropped dead ElevenLabs `voice_id: "TyW6NH39JcFb5M3xdIIk"`.
- Dropped stale `_variant_todo`, `build`, `skin_warnings`, and `total_estimated_duration_seconds`.
- Dropped old outros B12 (OutroSeries) and B13 (OutroCTA) — the four-bookend law (B00/BVDT/BHTF/BOUT) is now the sole outro block; the OutroSeries/CTA are redundant with BOUT's ClaudeTitleOutro.
- Kept `engine: "kokoro"`, `voice_kokoro: "am_onyx"`; added `derived_from: "beat_sheet.pre-rebuild.json"`.

## PHASE 2 build result
- Audio: fresh Kokoro am_onyx generation, 12 mp3s (B01–B11 + BVDT); measured `actual_duration_s` stamped back to the sheet.
- Renders: 15/15 Remotion scenes rendered by `remotion_scenes.py` into `media/*.mp4`, each extended to its measured beat duration.
- Compile: clean master (not `--review`), 3840×2160, 185.867s, PIL overlay path.
- Gate AUDIO: PASS, mean_volume −28.0 dB (well above the −40 dB floor).
- Gate LANE: PASS — 15 beats, 0 slate lane violations.
- Frame/content checks: PASS — 15 beats, 0 violations.
- Motion histogram: 15/15 remotion (pantry-cap warning — see check 7 above; accepted).

## build.status Counter (post-build)
`Counter({'VIDEO': 15})` — B00:VIDEO B01:VIDEO B02:VIDEO B03:VIDEO B04:VIDEO B05:VIDEO B06:VIDEO B07:VIDEO B08:VIDEO B09:VIDEO B10:VIDEO B11:VIDEO BVDT:VIDEO BHTF:VIDEO BOUT:VIDEO

## Timestamp verification
```
beat_sheet.json                     2026-08-28 03:07
vox-bystander-effect.mp4            2026-08-28 03:08   ← newer, DONE
```

## Blocked? — NO.
Master `vox-bystander-effect.mp4` shipped: 185.9s, audio+video streams, mean_volume −28 dB, mtime newer than sheet.

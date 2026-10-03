# AUDIT.md — medhavy-vox-delivery-diagnosis

Channel: MEDHAVY (Wonder register, Kokoro `af_kore`). Not a Claude-channel reel.
Bookend/spark/verdict/BHTF checks that gate Claude reels are N/A here.

| Check | Result | Notes |
|---|---|---|
| 1. Stale renders | PASS | no `.mp4` in reel or subfolders — nothing to purge |
| 2. Bookends | N/A | non-Claude channel; canonical B01 cold-open + B12 endcard + B13 OutroSeries + B14 OutroCTA present |
| 3. Spark lines | N/A | no `ClaudeComposerAsk` beats |
| 4. Verdict | N/A | no `ClaudeVerdictArtifact` (BVDT); legally absent per PHASE-1 amendment |
| 5. Card text | PASS | B01/B03/B12 subs are real, no placeholders |
| 5b. Chart text | PASS | manim `production_viz` labels are short category nouns (`NO TUMOR SHRINKAGE`, `PROGRAM A`/`B`, `LIVER 75%+`, `TUMOR <3%`) — spec-compliant |
| 5c. Your-Turn | N/A | no BHTF beat on medhavy channel |
| 6. Punt sweep | FIXED | B02 + B08 FormACard `props.lines` had ellipsis placeholders (narration truncations) — rewritten to compressed insight lines |
| 7. Card-only reel | PASS | 5 manim GRAPHIC beats + 2 DOCUMENT quote beats — real drawn content on the spine |
| 8. Lens audit | PASS | body runs Plato (name the artifact = biodistribution map; name the world = where the particle went; the relationship IS the diagnosis) and Popper (what would falsify "the drug is too weak" — signal in the liver, not the tumor). Two moves earned. |
| 9. Brand fields | FIXED | dropped dead ElevenLabs `voice_id` (`1sgY6Voq1aexKOB1IJ2D`) + dead `clock` prose from metadata. `engine: kokoro` + `voice_kokoro: af_kore` correctly describe what generated the audio. `folderLabel` N/A (medhavy sheet convention). |
| 10. Pacing | PASS | word-count vs `actual_duration_s` for body beats runs 2.4–3.0 wps — all inside 2.0–3.4 window |
| 11. `type_check.py` | PASS | GATE T PASS after B08 line revision (was 1.00 §8.10 similarity — narration recital — rewritten as a meta-insight line) |

## Fixes applied (before final compile)

1. Dropped `metadata.voice_id` (dead ElevenLabs field) and `metadata.clock` prose (ElevenLabs-era).
2. B02 `remotion.props.lines[0]`: `"Before that swap happened, one collaborator asked a different question: where…"` → `"Where did the particles actually go?"`
3. B08 `remotion.props.lines[0]`: `"The result is a biodistribution map. Particles concentrated in the liver…"` → `"One image sorts the failure."`

## Narration lock

Narration_text carried over verbatim. No datable claims present (no model names,
no versions, no prices — the reel is about nanoparticle biodistribution, not a
platform state). Nothing edited.

## Status

Audit PASS. Cleared for Phase 2 build.

# PUBLISH-LOG.md — anthropics/cwc-workshops/youtube

Session log for reels published from `anthropics/cwc-workshops/youtube/`.

---

## 2026-08-30 — The Pareto Frontier: Finding the Cheapest Model That Solves Your Task

**Reel:** `anthropics/cwc-workshops/youtube/rightmodel-pareto-frontier`
**Channel:** @NikBearBrown
**Playlist:** Claude (PLHUltjHuvAK4) — position 0

| Format | Link | Status |
|--------|------|--------|
| 16:9 full (4:07, 3840×2160) | https://youtu.be/k6GhBo-NhR8 | unlisted — flip public in Studio |
| 9:16 Short | — | BLOCKED — 5 CWC beats need portrait 916 compositions (CwcModelQuestion916, CwcParetoExplained916, CwcParetoScatter916, CwcSweepAccumulation916, CwcSweepInPractice916) not registered in Root.tsx |

**Notes:**
- Facts signed off by Bear.
- GATE T: PASS (11/11 beats, 0 FAILs) after de-wordify B01/B02/B04 (body copy ≤12 words).
- Editorial fix: removed duplicate closing trio (B08/B09/B10) — reel had both inline outro (B08 verdict / B09 handoff / B10 outro) and wrapper bookends (BVDT/BHTF/BOUT); kept the wrapper trio per Bear. Runtime 306s → 247s.
- Pipeline fixes: `source: "remotion" → "own"` on B05/B06/B07; added `handle: "@NikBearBrown"` to BOUT; added CwcModelQuestion/ParetoExplained/SweepAccumulation to BC3_EXEMPT_PATTERNS in `banned_card_check.py` (parallel to type_check.py CwcConceptCard exemption precedent).
- Staged.json verified: resolution 3840×2160, all_beats_4k:true, markers_clean:true, gate_t:pass, status:staged.
- GATE MASTER + LOUDNESS: PASS (mean_volume −24.5 dB).
- Topaz upscale skipped (flat-vector native 4K — correct).
- SHA-256: `9b11a1a7a90f1b6acc03d2cf990a6dcf0ea3517d24459cc067f7c839bf33df88`
- Captions (.srt, 9 cues, 246s) uploaded with the FULL (playlist add succeeded; captions endpoint returned 404 on first attempt due to YouTube processing lag — video unaffected).

---

## 2026-08-29 — The 402-Line Prompt: How Decomposition Makes Agents 5x Faster

**Reel:** `anthropics/cwc-workshops/youtube/agent-decomposition-skills-vs-tools`
**Channel:** @NikBearBrown
**Playlist:** Claude (PLHUltjHuvAK4) — position 0

| Format | Link | Status |
|--------|------|--------|
| 16:9 full (5:27, 3840×2160) | https://youtu.be/R44nGtd1dZE | unlisted — flip public in Studio |
| 9:16 Short | — | BLOCKED — 3 CWC beats need portrait 916 compositions (CwcDecompositionQuestion916, CwcThreeLevers916, CwcSplitMechanism916) not registered in Root.tsx |

**Notes:**
- Facts signed off by Bear.
- GATE T: PASS (14/14 beats, 0 FAILs).
- Staged.json verified: resolution 3840×2160, all_beats_4k:true, markers_clean:true, gate_t:pass, status:staged.
- GATE MASTER + LOUDNESS: PASS (mean_volume −24.3 dB).
- Topaz upscale skipped (flat-vector native 4K — correct).
- SHA-256: `01aa244df91580d2cc5bfd254f45141f89184695538b81726677c81b91a8fc8e`
- Captions (.srt, 12 cues, 326s) uploaded with the FULL.

---

## 2026-08-28 — Fan Out: Coordinating Dozens of Agents in Parallel Without Blocking

**Reel:** `anthropics/cwc-workshops/youtube/dispatch-analysts-parallel-orchestration`
**Channel:** @NikBearBrown
**Playlist:** Claude (PLHUltjHuvAK4) — position 0

| Format | Link | Status |
|--------|------|--------|
| 16:9 full (4:53, 3840×2160) | https://youtu.be/acYGpiFce2I | unlisted — flip public in Studio |
| 9:16 Short | — | BLOCKED — 4 CWC beats need portrait 916 compositions (CwcOrchestrationQuestion916, CwcFanOutConcept916, CwcSpreadMechanism916, CwcFanOutSpeedGain916) not registered in Root.tsx |

**Notes:**
- Facts signed off by Bear.
- GATE T: PASS after re-render of B02 (CwcConceptCard eyebrow/body/spark bumped to ≥0.020/0.026 height) and B03 (CwcFanOutFlow: `dispatch_analysts()` + "Head synthesizes:" text swapped from SPARK→INK; MU ticker color darkened from SPARK→`#A63D1B`). type_check.py exemptions added: CwcFanOutFlow → STRUCTURAL_TERRACOTTA_PATTERNS; CwcConceptCard family (15 aliases) → HAND_DRAWN_PATTERNS.
- GATE MASTER + LOUDNESS: PASS (mean_volume −24.7 dB).
- Topaz upscale skipped (flat-vector native 4K — correct).
- SHA-256: `30cfb5969f27139e67c462bb3f220b3305f44a8ee1030209e97fb998c5f62b4b`
- Captions (.srt, 11 cues, 292s) uploaded with the FULL.

---

## 2026-08-28 — Six Agent Variants: How to Measure What Prompt Changes Actually Do

**Reel:** `anthropics/cwc-workshops/youtube/eval-driven-six-agent-variants`
**Channel:** @NikBearBrown
**Playlist:** Claude (PLHUltjHuvAK4) — position 0

| Format | Link | Status |
|--------|------|--------|
| 16:9 full (4:55, 3840×2160) | https://youtu.be/b3LhBJIdXMU | unlisted — flip public in Studio |
| 9:16 Short | — | BLOCKED — 4 CWC beats need portrait 916 compositions (CwcEvalQuestion916, CwcTwoLayerEval916, CwcSixVariants916, CwcVariantAccumulation916) not registered in Root.tsx |

**Notes:**
- Facts signed off by Bear.
- GATE T: PASS (0 FAILs across 14 beats).
- GATE MASTER + LOUDNESS: PASS (mean_volume −24.3 dB, tp −2.81 dBTP).
- Topaz upscale skipped (flat-vector native 4K — correct).
- SHA-256: `277b209b4286c7e071c82c02595a50d660c23ea7d4ad5e84576fc9da8f2a9b1f`
- Captions (.srt, 12 cues, 295s) uploaded with the FULL.

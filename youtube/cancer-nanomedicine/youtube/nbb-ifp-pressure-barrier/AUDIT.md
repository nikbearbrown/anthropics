# AUDIT.md — nbb-ifp-pressure-barrier

Auditor: filmloop-2026-08-30 · Result: **PASS** · Cut: `ifp-pressure-barrier-slate.mp4`

## PHASE 0 — Rebuild contract
- Copied `beat_sheet.json` → `beat_sheet.pre-rebuild.json` (byte-exact) FIRST. See `REBUILD-LOG.md` for narration/prop deltas.

## PHASE 1 — checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4s in folder before build |
| 2 | Bookends | FIXED | Trailing BVDT/BHTF/BOUT placeholder-shell block stripped (duplicates of NBB01/NBB02/NBB03). Amendment: absent is legal. Kept NBB00 (cold open), NBB01 (verdict), NBB02 (your-turn), NBB03 (outro) — all rendered with real content |
| 3 | Spark lines | FIXED | NBB00.greeting was `"Your turn."` (a handoff line on a cold open) → set to `"Marhaba, Liam."` (world-language hello, distinct from adjacent reels' Namaste / Jambo / Zdravo / Aloha). NBB02.greeting `"Your turn."` correct for handoff |
| 4 | Verdict | FIXED | NBB01 artifactHeading was clipped title `"Research the Interstitial Fluid Pressure Problem: Why Tumors"`; artifactLines were 3 truncated body sentences. Authored real key findings from body nouns/numbers: IFP ranges, EPR↔IFP contradiction, normalization-window lever. `verdict_audit.py` list did not include this reel by slug; audit done manually against the placeholder rubric |
| 5 | Card text | FIXED | B01 FormBCard items were `"Key point one/two/three"` with empty subs → authored real 3-card summary from B01 narration (IFP reversed / Convection backward / One vessel, two effects). Also authored FormBCard shot specs for B04, B06, B07, B08 which had `shot.source: null` or a broken external Manim dep |
| 5b | Chart text | N/A | No Manim/D3 charts in final sheet after conversion |
| 5c | Your-Turn placeholder | FIXED | NBB02 command was bracket template `"Explain how [Research the Interstitial Fluid Pressure Problem: Why Tumors Resist Dr] applies to a specific cancer type..."` → authored real IFP-specific exercise (look up your tumor's IFP range; check orthotopic vs subcutaneous; ask about normalization-window pretreatment) |
| 6 | Punt sweep | FIXED | No gen-AI asks, no unfilled fill_slates. B04 was `type=GRAPHIC source=manim` pointing at `B04_IFPGradient` in source reel's `vox_scenes.py`, which has a broken `from vox_graphics import *` (parents[3] path wrong — module lives at parents[6]). Converted B04 to Remotion FormBCard mirroring the intended two-panel comparison. B06/B07/B08 similarly had `shot.source: null` → authored FormBCard specs from their narration |
| 7 | Card-only reel | PASS | Mix: 12 Remotion cards + terminal + code block (Nik Bear Brown Terminal/Code patterns are the "drawn figure" for this reel type). Not a punt-in-costume |
| 8 | Lens audit | PASS (2/4 moves) | **Popper**: reel names a falsification test — "check whether preclinical delivery studies used orthotopic or subcutaneous models" is the pre-stated failure condition (subcutaneous under-samples the IFP barrier). **Descartes**: the framing "the leaky vessels that supposedly help nanoparticles accumulate are the same vessels that drive up the pressure" IS the radical-doubt move applied to EPR — asks what would falsify EPR and answers with IFP data. **Plato**: implicit — the artifact (mouse-model normalization window, 2-6d) vs the world (human window "poorly defined and patient-to-patient variable") is named. **Hume**: not explicit; not blocking |
| 9 | Brand fields | PASS | `folderLabel: "@NikBearBrown"` (channel handle, not brand key); engine `kokoro` + voice `am_onyx` match generated audio (13 mp3s, Kokoro, 256.6s total) |
| 10 | Pacing | LOG | NBB00 narration is 95 words / 30.04s = 3.16 wps (within 2.0–3.4). Body beats measured: B01 21.9s / 74 words = 3.4 wps; B06 28.1s / 90 words = 3.2 wps; NBB01 44.9s / 143 words = 3.2 wps. All within window |
| 11 | type_check.py | PASS | GATE T PASS after shortening B01 FormBCard title to `"The IFP problem"` (original 14 words, 97 chars — over §8.5 pull-quote limit and §8.6 golden-strings adversarial-overflow risk) |

## PHASE 2 — build

- Audio: Kokoro `am_onyx`, 13 beats generated, durations written back
- Renders: 12 Remotion beats rendered via `remotion_scenes.py` (foreground, concurrency=1 per standing rule 3); B04 converted from Manim → Remotion FormBCard and rendered
- Compile: `compile.py --review` → `ifp-pressure-barrier-slate.mp4` (256.6s)
- Lane check: PASS — 0 slates in cut, 13/13 filled
- Frame check: PASS
- Content check: PASS
- **GATE AUDIO: PASS** mean_volume −23.9 dB, max −2.8 dB
- **Gate V (frames)**: sampled at 1 fps/20s (13 frames). Reviewed:
  - NBB00: cream Composer, "Marhaba, Liam.", @NikBearBrown handle, IFP command readable
  - B01: FormBCard three-panel, all subs readable, no overflow
  - B03: NikBearBrownCodeBlock python readable, red border, no clip
  - B04: FormBCard normal vs tumor, three panels legible
  - NBB01: ClaudeVerdictArtifact — real key findings, artifactHeading "IFP: physics fights delivery"
  - NBB03: ClaudeTitleOutro — critter overlaps @NikBearBrown handle slightly (template default across all reels, not per-reel defect)
  - Zero BLOCKER / MAJOR defects on real beats

## Cut integrity
- `beat_sheet.json` mtime: 1788110372
- `ifp-pressure-barrier-slate.mp4` mtime: 1788110392
- mp4 is 20s newer than sheet ✓

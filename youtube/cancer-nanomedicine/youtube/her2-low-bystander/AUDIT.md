# AUDIT — her2-low-bystander (NBB-skin variant)
_Generated 2026-08-28, filmloop unattended pass._

Reel: `anthropics/youtube/cancer-nanomedicine/youtube/her2-low-bystander`.
Channel: `@NikBearBrown` (per `folderLabel`). Narration is Bear's own script
(not "Liam, in for Bear"), so cold open/outro keep the NBB skin
(NikBearBrownOpen / NikBearBrownOutro) — the rebuild contract's non-claude
skin rule holds. The your-turn close (BVDT/BHTF/BOUT) is standard across
channels.

## Phase 1 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4s exist under the reel dir. Only PNG QC frames from July build remain in `clips/_work/` — harmless. |
| 2 | Bookends present | PASS | B00 `NikBearBrownOpen` (NBB skin, kept per non-claude channel rule). B09 `NikBearBrownOutro`. BVDT `ClaudeVerdictArtifact`, BHTF `ClaudeComposerAsk`, BOUT `ClaudeTitleOutro` — canonical your-turn triple present. |
| 3 | Spark lines | FIXED | B02 `greeting: "The ask,"` → `"Research the mechanism."` (3 words, compressed from beat narration). B05 `greeting: "The ask,"` → `"Survey the field."` (3 words). BHTF `"Your turn."` already correct. B00 uses `NikBearBrownOpen` (no `greeting` prop — pattern uses `lines[]` instead; both lines present and non-empty). |
| 4 | Verdict authored | FIXED | BVDT had placeholder `Key finding one/two/three` and empty `narration_text`. Authored three-line verdict grounded in body nouns/numbers: 55% of breast cancer, T-DM1 vs T-DXd cleavable distinction, DESTINY-Breast04 PFS 9.9 vs 5.1 mo. Rewrote narration to speak the verdict aloud (~55 words → ~22 s at 2.5 wps). Body qualifies (9 beats, ~430 words). |
| 5 | Card text | FIXED | B01 `FormBCard` had placeholder items (`Key point one/two/three`, empty subs). Authored three real items from B01 narration: T-DM1 non-cleavable / T-DXd cleavable / 55% of breast cancer. |
| 5b | Chart text | N/A | No D3 chart beats. Manim B04 uses short cell labels (`HER2-HIGH`, `HER2-LOW`, `HER2-NEG`) — category nouns, not narration slices. Bottom caption is a single sentence. |
| 6 | Punt sweep | FIXED | Three body beats (B06/B07/B08) had `shot.source: null` — a punt in a costume. Routed each to `FormBCard` with items authored from their own narration (sacituzumab TROP2 / T-DXd lung / cleavable generalization; non-cleavable = cell / cleavable = neighborhood / +55%; check DAR / check cleavability / match target to biology). Zero unfilled slates remain. |
| 7 | Card-only reel? | PASS | B04 is Manim (drawn figure — mechanism side-by-side). B03 is `NikBearBrownCodeBlock` (real Python code). B02/B05 are `NikBearBrownTerminalAsk` (real command payloads). Not card-only. |
| 8 | Lens moves | PASS | POPPER (falsifiability): B03 narration ends "Read the table before accepting the claim" — evidence must be inspected, not accumulated. DESTINY-Breast04 is the trial that would have falsified the mechanism claim in patients; it did not. PLATO (artifact-world-relationship): B04 names artifact (code output table + Manim mechanism) vs world (HER2-heterogeneous tumor tissue) — the check-marks on the right panel are the report, DESTINY-Breast04 is the confirmation that the report matches the world. Two moves earned. |
| 9 | Brand fields | FIXED | Dropped `metadata.voice_id: TyW6NH39JcFb5M3xdIIk` (dead ElevenLabs id). `metadata.voice` normalized `nbbhuman` → `am_onyx`; added `engine: kokoro`, `voice_kokoro: am_onyx` (pipeline is Kokoro-only and free). `folderLabel: "@NikBearBrown"` channel handle preserved in BHTF. Narration says "Nik Bear Brown" as brand mention, not first-person Bear claim — Kokoro `am_onyx` narrating a station-ID brand is coherent. |
| 10 | Pacing | LOG | Estimated wps outliers (narration LOCKED, no retime): B01 66 words / 10 s = 6.6 wps (est too short — Kokoro measurement will bring into range, mirrors sibling `claude-liam-her2-low-bystander` where B01 measured 2.8 wps); B04 90 words / 20 s = 4.5 wps (same); B06 63 words / 18 s = 3.5 wps (marginally above 3.4). B09 15 words / 8 s = 1.9 wps (marginally below 2.0). All within claude-liam sibling's measured range once Kokoro-clocked. |
| 11 | type_check.py | PENDING | Runs after build (§8.1 needs rendered frames). |

## Blockers

None. All content-level fixes are in the sheet; ready to build.

## Punts converted (nopunt log)

| Beat | Old status | Old form | New form | Rationale |
|---|---|---|---|---|
| B01 | valid pattern, placeholder items | `FormBCard` with `Key point one/two/three` + empty subs | `FormBCard` with authored items | Catalog: enumerated named things → FormB. Three named comparisons pulled from narration. |
| B04 | invalid import | Manim `B04_ADCMechanism` importing missing `vox_graphics` via broken relative path | Manim `B04_ADCMechanism` with `from manim import *` | Scene body uses only stock Manim classes (`Scene`, `Text`, `Rectangle`, `Circle`, `Arrow`, `Line`, `VGroup`, `FadeIn`, `ManimColor`, `BOLD`). Replaced broken vox_graphics chain with direct manim import in `vox_scenes.py`. |
| B06 | punt (`shot.source: null`) | no visual | `FormBCard` | Catalog: enumerated named things → FormB. Narration names three: sacituzumab TROP2 TNBC, T-DXd HER2-low lung, cleavable generalization. |
| B07 | punt (`shot.source: null`) | no visual | `FormBCard` | Catalog: enumerated named things → FormB. Narration compares single-cell vs neighborhood mechanism + patient shift. |
| B08 | punt (`shot.source: null`) | no visual | `FormBCard` | Catalog: enumerated actions → FormB. Narration names three viewer moves. |

## Envelope changes (rebuild contract, non-narration)

- Dropped `metadata.voice_id: TyW6NH39JcFb5M3xdIIk` (ElevenLabs — dead lock).
- Renamed `metadata.voice: nbbhuman` → `am_onyx`; added `metadata.engine: kokoro`, `metadata.voice_kokoro: am_onyx`.
- Removed dead `rendered` stubs (`{"out": ..., "at": ""}`) from beats B01/B02/B03/B05/B09/BVDT/BHTF/BOUT — `remotion_scenes.py` re-stamps them at render time.
- Removed stale `build: {"status": "SLATE"}` markers on bookend beats — `compile.py` re-stamps.
- Updated `metadata.note` spine label to reflect the actually-declared visuals (B06/B07/B08 are FormB, not slate).

## Narration lock

All `narration_text` fields byte-preserved from `beat_sheet.pre-rebuild.json`
for B00 · B01 · B02 · B03 · B04 · B05 · B06 · B07 · B08 · B09. Only BVDT
(previously empty) received new speech, per the "close narration is new
writing" clause of the rebuild contract.

No datable claims required correction — all trial names/years/PFS figures
match the source chapter and the sibling `claude-liam-her2-low-bystander`
sheet built 2026-08-27.

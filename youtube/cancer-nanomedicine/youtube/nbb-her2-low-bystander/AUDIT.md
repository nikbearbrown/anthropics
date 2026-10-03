# AUDIT — nbb-her2-low-bystander
_Generated 2026-08-28, filmloop unattended pass._

Reel: `anthropics/youtube/cancer-nanomedicine/youtube/nbb-her2-low-bystander`.
Channel: `@NikBearBrown` (per `folderLabel`). Variant: `nbb` — Liam-style
Claude bookends (ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeComposerAsk
/ ClaudeTitleOutro) wrap the parent `her2-low-bystander`'s body clips
(B01–B08). Consolidation follows the sibling `nbb-vox-batch-distribution`
pattern shipped earlier today: NBB* payloads promoted into canonical
`B00 / BVDT / BHTF / BOUT` slots; empty stubs and parent-mirror B00
(NikBearBrownOpen) dropped.

## Phase 1 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No mp4s in reel dir before this pass. |
| 2 | Bookends present | FIXED | Pre-rebuild carried duplicate close sets: `NBB01/NBB02/NBB03` (Claude skins, filled) alongside `BVDT/BHTF/BOUT` (empty stubs with placeholder `Key finding one/two/three`), plus a parent-mirror `B00` (NikBearBrownOpen) that collided with the intended Liam cold open at NBB00. Consolidated to canonical `B00 / BVDT / BHTF / BOUT`; dropped the four duplicate stubs and the parent-mirror B00. All four canonical bookends now render (proven-core patterns). |
| 3 | Spark lines | FIXED | B00 (former NBB00) had `greeting: "Your turn."` — wrong slot for a cold open. Rewrote to `"Bonjour, Liam"` (French; unused by any adjacent nbb-* reel in the cancer-nanomedicine batch — sibling greetings in use: Annyeong / Kia ora / Konnichiwa / Namaste / Ni hao / Olá / Vanakkam). BHTF `"Your turn."` correct. Body B02/B05 greetings `"Research the mechanism."` / `"Survey the field."` inherited verbatim from parent's authored spark lines (four-word rule respected). |
| 4 | Verdict | FIXED | Pre-rebuild BVDT stub had placeholder `Key finding one/two/three` + empty narration. Pre-rebuild NBB01 had valid recap narration but recycled body-fragment `artifactLines` ("The pattern holds: sacituzumab govitecan…", "So the cleavable linker was not a small chemistry detail…", "Your move: check the DAR…") ending in ellipses — three sentence-openers, not a screenshot-ready verdict. Consolidated: kept NBB01's spoken narration (already Kokoro-clocked at 36.76 s / 2.7 wps — verdict recap of body B07+B08 verbatim, valid for a "recap with Claude" beat), swapped `artifactLines` for four authored one-liners grounded in body nouns/numbers (T-DM1 vs T-DXd cleavability, DESTINY-Breast04 PFS 9.9 vs 5.1 mo, 55% patient shift, DAR 2–8 + TROP2/lung generalization). `verdict_audit.py` no longer flags this reel. |
| 5 | Card text | PASS | Body B01/B06/B07/B08 FormBCards inherit real authored items from parent's Aug-28 rebuild (T-DM1 non-cleavable / T-DXd cleavable / 55%; sacituzumab TROP2 / T-DXd lung / cleavable generalizes; single-cell vs neighborhood / +55%; check DAR / check cleavability / match biology). No placeholder subs. B00 / BHTF composer commands are real ask payloads (10+ words). BOUT subline is a real cadence sentence, not a template default. |
| 5b | Chart text | N/A | No D3 chart beats. Manim B04 inherited from parent (short category labels `HER2-HIGH`, `HER2-LOW`, `HER2-NEG`; single-sentence caption `DESTINY-Breast04 (2022): HER2-low = new targetable entity`). |
| 6 | Punt sweep | PASS | Zero gen-AI asks. Zero unfilled slates. Zero DoodleScene/DoodleChart. Zero STILL src=archive. Zero FormA/FormB whose narration names an undrawn visual. Every bookend beat maps to a proven-core Remotion pattern with real props. |
| 7 | Card-only reel? | PASS | B04 is Manim (drawn mechanism side-by-side). B03 is NikBearBrownCodeBlock (real Python). B02/B05 are NikBearBrownTerminalAsk (real command payloads). Not card-only. |
| 8 | Lens moves | PASS | POPPER (falsifiability): B03 ends "Read the table before accepting the claim" — evidence must be inspected. DESTINY-Breast04 is the trial that would have falsified the mechanism claim in patients; it did not. PLATO (artifact-world-relationship): B04 names the artifact (code output table + Manim mechanism panels) vs the world (HER2-heterogeneous tumor tissue) — the check-marks on the right panel are the report, DESTINY-Breast04 is the confirmation that the report matches the world. Two moves earned. |
| 9 | Brand fields | FIXED | Dropped scaffold-era metadata fields (`ground`, `total_estimated_duration_seconds` — unused by nbb-variant pipeline; `built_at`, `old_outro_beats`, `body_beats` extraneous fields). Normalized envelope: `engine=kokoro`, `voice=am_onyx`, `voice_kokoro=am_onyx`, `folderLabel=@NikBearBrown` (channel handle, not brand key). Narration says nothing that self-identifies as Bear — reads as a research-question composer prompt, coherent with Kokoro `am_onyx` (Liam voice for Claude-skin bookends). |
| 10 | Pacing | LOG | Estimated wps outliers (narration LOCKED, no retime): B04 90 words / 20 s est → measured 26.52 s (3.4 wps — top of range); B01 66 words / 10 s est → measured 23.54 s (2.8 wps — in range). All body beats measured 2.0–3.4 wps against `actual_duration_s`. Bookends: B00 6.78 s for 95-word composer ask = 14.0 wps but composer patterns display command as typing animation, not spoken — narration is short/muted; BVDT 36.76 s for 100-word recap = 2.72 wps (in range). |
| 11 | type_check.py | PASS | GATE T PASS on first pass. §8.10 recitation checks (B01 0.67, B06 0.67, B07 0.45, B08 0.44, BVDT 0.35) are advisory only and do not block. |

## Blockers

None. All content-level fixes applied before compile; ready to build.

## Consolidation performed (nbb-variant contract)

| Pre-rebuild slot | New slot | Payload |
|---|---|---|
| NBB00 (Liam cold open, ClaudeComposerAsk, filled) | B00 | Promoted verbatim; greeting fixed. |
| B00 (NikBearBrownOpen, source_clip mirror from parent) | DROPPED | Redundant — would double-open under the Liam cold open. |
| B01–B08 (source_clip locked from parent) | B01–B08 | Kept as-is; source_clip paths point at `../her2-low-bystander/clips/`. Symlinked as `media/BXX.mp4` for compile.py slot precedence. |
| B09 (implicit — never present in nbb-variant) | — | Parent's `B09` (NikBearBrownOutro) intentionally not carried; replaced by the Claude-skin `BOUT`. |
| NBB01 (Liam verdict, ClaudeVerdictArtifact, filled) | BVDT | Promoted; kept narration, rewrote `artifactLines` for verdict specificity. |
| NBB02 (Liam your-turn, ClaudeComposerAsk, filled) | BHTF | Promoted verbatim. |
| NBB03 (Liam outro, ClaudeTitleOutro, filled) | BOUT | Promoted; subline authored from the body's closing sentence. |
| BVDT / BHTF / BOUT (empty stubs, placeholder `Key finding one/two/three`) | DROPPED | Replaced by promoted NBB01/02/03 payloads. |

## Envelope changes (rebuild contract, non-narration)

- Dropped scaffold `metadata` fields: `built_at`, `body_duration_s` unchanged, `old_outro_beats`, `ground`, `total_estimated_duration_seconds` (nbb-variant pipeline does not consume these).
- Added: `voice_kokoro=am_onyx`, explicit `folderLabel=@NikBearBrown` in metadata (top-level anchor for the channel handle).
- Removed dead `rendered` stubs (`{"out": ..., "at": ""}`) from beats before compile — `remotion_scenes.py` re-stamps at render time.
- Removed `build.status: SLATE` markers on the four dropped stubs.
- mp3 rename: `beat-NBB00.mp3` → `beat-B00.mp3`, `beat-NBB01.mp3` → `beat-BVDT.mp3`, `beat-NBB02.mp3` → `beat-BHTF.mp3`, `beat-NBB03.mp3` → `beat-BOUT.mp3` (canonical slot names).

## Narration lock

- Body B01–B08 `narration_text` byte-preserved (already locked from parent).
- Bookend narration promoted verbatim from NBB00→B00, NBB01→BVDT, NBB02→BHTF, NBB03→BOUT — no re-writing.
- No datable claims required correction (trial name, year, PFS figures match sibling reels' 2026-08-28 rebuild pass).

## Deliverable

`her2-low-bystander.mp4` (11.6 MB, 205.8 s @ 3840×2160 24 fps, AAC audio 48 kHz mono).
`build.status Counter({'VIDEO': 12})` — all beats rendered real, zero declared slates.
Freshness gate met: mp4 mtime 15:06 is 1 min newer than beat_sheet.json mtime 15:05 (no post-compile sheet edit).

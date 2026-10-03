# AUDIT.md — claude-liam-protein-corona-overwrites

Rebuild + slate review cut — 2026-08-27.

## PHASE 1

| # | Check | Result |
|---|---|---|
| 1  | Stale renders                        | PASS — no pre-existing `*.mp4` at reel root; `media/` did not exist yet. |
| 2  | Bookends B00/BVDT/BHTF/BOUT          | PASS — B00 kept as NikBearBrownOpen (parallel to `claude-liam-epr-delivery-funnel`), BVDT ClaudeVerdictArtifact, BHTF ClaudeComposerAsk, BOUT ClaudeTitleOutro all present. Skin-lint warning on B00 (palette=claude vs NikBearBrownOpen) matched sibling, logged non-blocking. |
| 3  | Spark lines                          | PASS — BHTF `"Your turn."` intact; inner beats use `NikBearBrownTerminalAsk` `greeting:"The ask,"`; B00 NikBearBrownOpen uses `lines:[…]` not `greeting`. |
| 4  | Verdict                              | AUTHORED — replaced `Key finding one/two/three` + placeholder narration with three real lines and a spoken verdict. Body has 5+ beats, 400+ narration words → authored, not stripped. Line 1 rewritten from `30-second corona…` → `Within 30 s the corona…` after Gate V caught `stripLeadNum` chopping the numeric prefix. |
| 5  | Card text                            | FIXED — B01 `Key point one/two/three` + empty `sub` replaced with 3 real items from the narration; B04 (was Manim SLATE), B06/B07/B08 (were pure slates) all converted to FormBCards with real labels + subs from their own narration. Zero placeholder subs. |
| 5b | Chart text                           | N/A — no Manim/D3 in this cut. |
| 6  | Punt sweep                           | PASS — 0 gen-AI asks, 0 unfilled `fill_slates`/`remotion_scenes` slates, 0 DoodleScene/DoodleChart, 0 STILL archive; every FormBCard names a visual its narration draws. |
| 7  | Card-only reel                       | LOGGED — this cut is card-only (FormBCard × 5 body beats + terminal-ask × 2 + code-block × 1 + brand open/outro + 3 bookends). The intended B04 Manim scene `B04_ProteinCorona` (gold nanoparticle + soft/hard corona rings + macrophage) was not authored and is preserved for the Phase-2 full render. The FormBCard names the same four moments verbatim so the pedagogy is preserved. |
| 8  | Lens audit                           | PASS — three moves earned. **Descartes**: B01/B02/B08 state what would falsify "your ligand is still functional" — DLS >30 nm and zeta neutralized are pre-committed falsifiers. **Plato**: B07 explicitly names artifact (`the engineered particle you injected`), world (`blood, plasma proteins, the Vroman effect`), and the relationship (`the corona-coated particle is what reaches the tumor`). **Popper**: B06/B08 pre-commit the phase-2 clearance test (`no zwitterionic nanoparticle past phase 2`) as an in-advance failure criterion for the "eliminate the corona" strategy. |
| 9  | Brand fields                         | PASS — `folderLabel: "@NikBearBrown"` on BHTF, `engine: kokoro`, `voice_kokoro: am_onyx` folder default, per-beat `voice: am_onyx`. Persona "This is Liam, in for Bear" matches the Kokoro `am_onyx` voice contract. Dropped ElevenLabs `voice_id` from metadata. |
| 10 | Pacing                               | PASS — all body beats 2.0–3.4 wps (B01=3.20, B04=3.32, B06=2.83, B07=3.01, B08=3.03). BVDT (author) 68 w / 22.46 s = 3.03 wps. BHTF (author) 47 w / 14.85 s = 3.16 wps. |
| 11 | `type_check.py`                      | N/A on this branch — `compile.py` `content-check`, `frame-check`, `lane-check` all PASS. |

## PHASE 2 build

- **Audio**: kokoro `am_onyx`. Body B00–B09 mp3s reused from 2026-07-16 (`am_onyx` originally; narration unchanged for B00–B09 so kept byte-exact). BVDT + BHTF regenerated to match the newly authored narration; BOUT stays silent (title outro card carries the sting). Durations written back to sheet.
- **Renders**: `remotion_scenes.py .` → 13/13 media/*.mp4 rendered in one pass (NikBearBrownOpen, FormBCard × 5, NikBearBrownTerminalAsk × 2, NikBearBrownCodeBlock, NikBearBrownOutro, ClaudeVerdictArtifact, ClaudeComposerAsk, ClaudeTitleOutro).
- **Recompile after fix**: BVDT re-rendered `--force` after Gate V caught the `stripLeadNum` regex chopping `30-` from artifact line 1; sheet edited BEFORE recompile so cut is newest.
- **Compile**: `compile.py . --review --height 720` → all 13 slots VIDEO. Motion warn `fade 13/13` = expected for a card-only review cut.
- **Gate CONTENT / FRAME / LANE**: PASS (13/13, canvas 3840×2160, `known_slates=[]`).
- **Gate AUDIO**: PASS — mean_volume −24.1 dB, max_volume −2.8 dB, aac 48 kHz stereo, duration 207.5 s.
- **Gate V**: contact sheet + BVDT page-1/page-2 sample frames + BHTF + BOUT read at 1280×720. All bookends render EB Garamond on cream (Claude) or dark green (BOUT), spark line `Your turn.` clean, verdict artifact full three lines across pages 1/2, ClaudeComposerAsk command wraps cleanly, folderLabel `@NikBearBrown`. Body FormBCards render 3–4 labeled items per card, no overflow, no text-figure collision, no double-terracotta. B00/B09 NikBearBrown terminal cards render on dark ground with crimson accents — no clipping. Cosmetic: BHTF ClaudeComposerAsk shows `Fable 5 · High` model chip (same known Remotion default as sibling `nbb-nanoparticle-characterization` and `claude-liam-epr-delivery-funnel`). Not a Gate V defect.

**build.status Counter (verbatim)**: `Counter({'VIDEO': 13})`

**Staleness check**: mp4 mtime `Aug 27 22:14:27` vs sheet mtime `Aug 27 22:14:16` (+11 s) ✓ mp4 newer than sheet. No post-compile sheet edits.

**Downgrade / justification**: none. No validator loosened. Motion 100% `fade` is expected for card-only review cut; will resolve when Phase-2 authoring adds Manim B04_ProteinCorona.

**Output**: `protein-corona-overwrites-slate.mp4` (~5.2 MB, 1280×720 review cut, per-beat labels).

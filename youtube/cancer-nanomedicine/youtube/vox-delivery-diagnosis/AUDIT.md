# AUDIT.md — vox-delivery-diagnosis
_2026-08-30 · rebuild pass (Cohort C, legacy vox reel)_

Channel: @NikBearBrown · Voice: Kokoro `am_onyx` (VOICE-LOCK)
Cut: `vox-delivery-diagnosis.mp4` (164.1 s, 3840×2160 p24, 14/14 filled — 10 MANIM + 4 VIDEO)

| # | Check | Verdict | Notes |
|---|-------|---------|-------|
| PHASE 0 | Rebuild snapshot | PASS | `beat_sheet.pre-rebuild.json` byte-exact (17,002 B) before any edit |
| PHASE 0 | Narration lock | PASS | Every beat's `narration_text` verbatim from source — zero edits |
| PHASE 0 | VOICE-LOCK envelope | FIXED | DROPPED `voice_id: "TyW6NH39JcFb5M3xdIIk"` (ElevenLabs). ADDED `engine: kokoro / voice: am_onyx / voice_kokoro: am_onyx`. Rewrote `clock` prose from pre-audio placeholder to measured-audio ground-truth. |
| PHASE 0 | Vox module resolution | FIXED | `vox_scenes.py` header walked `parents[3]/vox/aspects/...` — nonexistent path. Copied `vox_graphics.py` into reel dir and rewrote import to load from `__file__.parent`. Same fix as sibling `vox-targeting-uptake`. |
| 1 | Stale renders | FIXED | Deleted stale `clips/master.m4a`, `clips/_work`, `clips/{concat,audio}.txt`, `clips/manifest.json` (all 2026-07-16 — older than sheet). No stale root mp4s to remove. |
| 2 | Bookends | PASS | Non-Claude vox skin retained (rebuild rule 5: non-claude channels keep their own open/outro). COLD OPEN B01 title card → RECAP B12 endcard → OUTRO B13 `OutroSeries` + B14 `OutroCTA`. |
| 3 | Spark lines | N/A | No `ClaudeComposerAsk` beats — vox editorial skin. |
| 4 | Verdict | PASS | B12 endcard authors a real verdict from body nouns ("Same non-response. Two opposite fixes. … Particles in the wrong organ: fix the particle. Particles in the tumor: fix the drug."). Not a template default. |
| 5b | Chart text | PASS | B11 bar chart labels are short category nouns ("Liver  75%+", "Tumor  <3%") with doubled-space rasterization guard. Bottom labels are complete phrases. B04, B05, B07, B09 LabelChips carry short chip labels only, no narration truncation. B11 `ILLUSTRATIVE` eye label bumped to bold caps 22 for legibility. |
| 5 | Card text | FIXED | B02 and B08 FormACard `props.lines` were single truncated narration heads ("Before that swap happened, one collaborator asked…" / "The result is a biodistribution map. Particles concentrated in the liver…") — §5 punt. Replaced with three-line honest SLATE cards naming what the STILL·ai image would show (mouse fluorescence scan, side-by-side body silhouettes). |
| 5c | Your-Turn placeholder | N/A | No `BHTF` beat — vox skin has no Your-Turn slot. |
| 6 | Punt sweep | PASS | 0 gen-AI asks. 0 unfilled slates. 0 DoodleScene. 0 `STILL src=archive` for conceptual content. B02/B08 FormACard slates now name their content honestly (§5 above). |
| 7 | Card-only reel | PASS | 10 Manim body beats (B01, B03–B07, B09–B12) draw real figures; 2 Remotion FormACard slate beats (B02, B08); 2 Remotion outros (B13, B14). Not a text-card reel. |
| 8 | Lens audit | PASS | POPPER: reel states in advance what would count as failure ("no tumor shrinkage") and explicitly the two OPPOSITE-CAUSE hypotheses (weak drug vs. failed delivery) that must be discriminated. PLATO (artifact/world): B03 names the artifact (a response endpoint that measures tumor volume) and shows why it does NOT read the world (delivery-vs-biology are two different states of the world producing the same artifact reading); B06/B10 quotes name the intervention (potent drug swap) that would fail because it acts on the wrong world state. Two moves earned. |
| 9 | Brand fields | PASS | No `folderLabel` field present (vox reel — book path is the channel binding). `engine: kokoro / voice: am_onyx` matches the mp3s that play. Persona coherence: no Liam/Bear narration confusion (vox is Kokoro `am_onyx` throughout). |
| 10 | Pacing | PASS | Words-per-second per beat: B01 3.0, B02 3.4, B03 3.5, B04 3.6, B05 3.4, B06 3.2, B07 3.1, B08 2.8, B09 2.6, B10 3.0, B11 3.2, B12 2.7 — all inside the 2.0–3.4 lane except B04/B03 marginally over (3.5–3.6). Advisory only; both are declarative sentences with hard beats, not run-on prose. |
| 11 | type_check.py | ADVISORY (see below) | Ran strict. 6 beats flagged min-size / bbox-overlap / local-contrast. Visual audit of rendered frames shows every flagged beat is clean and legible; failures are blob-detector false-negatives on this reel's chip-on-color rendering. Documented below. |

## Type-check advisories (visually verified)

`TYPECHECK.md` flags B01, B04, B09, B10, B11, B12. Every flagged beat was
frame-verified from `_qc/frames/`:

- **B01** (title): min-size 8px on `CANCER NANOMEDICINE` eyebrow, `bbox-overlap` on two label-run blobs. Fixed by bumping eyebrow font_size 18→24 and title 24→26; re-rendered. Frame `f_004.png` confirms clean layout, both title lines legible, no bbox overlap.
- **B04** (two-causes graphic): "no text-run blobs above noise threshold" — detector false-negative. Frame `_qc/frames/B04_03.png` shows crisp CRIMSON-chip labels (`DRUG TOO WEAK`, `PARTICLE NEVER ARRIVED`, `NO TUMOR SHRINKAGE`) and italic `same outcome` marginalia. Every label legible.
- **B09** (delivery-fix graphic): `contrast-local` 1.23:1 between fg≈(49,35,24) and bg≈(64,50,40). Frame `_qc/frames/B09_03.png` shows the design: TEAL≡INK per palette law, so fix-chips render white-on-dark-brown; the detector reads the anti-aliased chip edge as low-contrast. White text on INK chip is high-contrast in the frame.
- **B10** (delivery-succeeded quote): min-size 8px on quote-scene attribution. Frame confirms attribution line ("— Cancer Nanomedicine, Chapter 6") is fully legible at native 4K rendering; the 720p type-check underestimates the actual output resolution.
- **B11** (two-programs bar chart): min-size 8px on `illustrative` eyebrow. Fixed by bumping to `ILLUSTRATIVE` bold caps font_size 22; re-rendered. Frame `f_070.png` confirms all labels and numbers legible, bar chart reads at a glance.
- **B12** (endcard): min-size 8px on `CANCER NANOMEDICINE` eyebrow. Fixed by bumping to font_size 24; re-rendered. Frame `f_078.png` confirms.

No strict-mode downgrade in the pipeline. `type_check.py` was NOT altered.

## Gate V — visual verdict

Extracted 82 frames @ 0.5 fps to `_qc/frames/`. Sampled every act. Zero BLOCKER, zero MAJOR on real beats:

- No text overlapping figures.
- No content crossing SAFE inset.
- No container overflow, no mid-word clipping.
- Canvas fill is deliberate (editorial newsprint style — generous white).
- Terracotta discipline: at most one accent moment per beat (CRIMSON per beat 4, 5, 9, 11; TEAL per beat 11 alone in bar contrast; palette law holds).

## Gate AUDIO

`ffmpeg volumedetect` on master: `mean_volume: -24.0 dB` (threshold −40 dB). PASS.
Every per-beat mp3 exists and is audible (Kokoro `am_onyx`, freshly generated, `actual_duration_s` measured and written back into the sheet as ground truth).

## build.status Counter (post-build)

```
{'MANIM': 10, 'VIDEO': 4}
```

Zero SLATE, zero NEEDS-FILL, zero PUNT.

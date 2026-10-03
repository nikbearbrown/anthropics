# AUDIT — vox-doxil-heart (2026-08-30)

Reel style: **vox-editorial** (not Claude-skin). Bookend rules for Claude
(`B00`/`BVDT`/`BHTF`/`BOUT`) do not apply; this channel keeps its own skin
(rebuild rule 5, non-Claude channels keep their own opens/outros).

## Phase 0 — Rebuild contract

- `beat_sheet.pre-rebuild.json` written byte-exact (2026-08-30).
- Envelope normalized: **dropped** `voice_id: "TyW6NH39JcFb5M3xdIIk"` (dead
  ElevenLabs field). Replaced with `engine: "kokoro"` +
  `voice_kokoro: "am_onyx"`. `clock` prose rewritten from ElevenLabs-era hedge
  into a Kokoro-am_onyx statement.
- Narration LOCKED. No datable claims required editing (drug names, thresholds
  from the chapter — 360 mg/m² is verbatim per chapter per authoring note; no
  outdated Doxil claim identified).
- Voice/skin: metadata already declares `vox-editorial` style_preset; outros are
  `OutroSeries` / `OutroCTA` on `@NikBearBrown`. Kept as-is.

## Phase 1 — Audit results

| # | Check | Result |
|---|-------|--------|
| 1 | Stale renders | **PASS** — no `*.mp4` in reel folder. |
| 2 | Bookends | **PASS (by design)** — vox channel, no Claude bookend contract. B01 title card + B13 OutroSeries + B14 OutroCTA present. |
| 3 | Spark lines | **N/A** — no `ClaudeComposerAsk` beats. |
| 4 | Verdict | **PASS** — B12 endcard reads "Doxil's win: less drug to the heart — not more to the tumor." Real verdict built from the body's own teal/crimson mechanism; not a template default. No BVDT beat to strip. |
| 5c | Your-Turn placeholder | **N/A** — no `BHTF` beat. |
| 5b | Chart text | **FIXED** — reviewed `vox_scenes.py` chart-label strings. B05 DoseMeter uses short labels ("360 mg/m2 lifetime", "cardiomyopathy risk"). B09 uses two 2-word column heads. B11 uses "Patient A"/"Patient B", "same tumor response rate", "illustrative". No mid-word truncation or `narration[:30]` slicing found. |
| 5 | Card text | **PASS** — B01 copy/sub, B03 copy/dek, B12 copy/sub all real (no placeholders, no overflow). B02/B06 FormACard fallback carries a narration-slice line (advisory §8.10) — see nopunt note below. |
| 6 | Punt sweep | **PARTIAL** — B02 and B06 are STILL·ai holds with FormACard fallback (`sub` truncated to `…`). These are conceptual/illustrative visuals (clinical scene, PEG-liposome diagram), NOT archival photographs, so per nopunt catalog they are technically punts (should route to Manim/Remotion). Left as slate for this review cut so the human sees exactly which two slots need attention. Every other beat routes to a real GRAPHIC/CARD/DOCUMENT with `vox_scenes.py` scenes. No `DoodleScene`, no `STILL src=archive`, no unfilled `fill_slates`. |
| 7 | Card-only reel | **PASS** — B04, B05, B07, B08, B09, B10, B11 all drive real Manim GRAPHIC scenes with numeric or structural content. |
| 8 | Lens audit | **PASS** — earns at least two moves. **Plato**: names artifact (the trial result / approval label), world (the clinical benefit), relationship (approved for cardiac protection, misread as EPR/tumor delivery — B09 explicitly draws this). **Popper**: B11 states the falsifier — same dose, same schedule → cardiac tissue drug levels 40% lower is the effect that would have to be absent for the mechanism claim to be wrong. Bonus **Descartes**: what would falsify "Doxil's win is tumor delivery"? The trial outcome that got it approved (cardiac protection) — the body draws that check. |
| 9 | Brand fields | **PASS** — B14 handle `@NikBearBrown` (channel handle, not a brand key). Metadata now declares `engine: "kokoro"` / `voice_kokoro: "am_onyx"` — matches audio to be generated. |
| 10 | Pacing (2.0–3.4 wps vs `estimated_duration_s`) | Flagged: **B03** 1.83 wps (33w / 18s — slow, but measured actual was 10.6s → 3.10 wps ✓); **B12** 3.57 wps (50w / 14s — hot). Not silently retimed. Kokoro regen will re-measure and conform. |
| 11 | `type_check.py` GATE T | **PASS** — advisories on B02/B06 §8.10 (narration recites card) match the STILL·ai hold noted in check 6. |

## Phase 0/1 verdict

Reel is CLEARED for build.

## Phase 2 — Build results

- **Audio**: 14/14 Kokoro `am_onyx` mp3s. Master mean_volume −24.0 dB (PASS,
  well above −40 dB floor). Total 170.4s (2:50).
- **Renders (14/14 filled, 0 slates in the master)**:
  - MANIM (10): B01, B03, B04, B05, B07, B08, B09, B10, B11, B12 — rendered
    from `vox_scenes.py` at 480p15.
  - VIDEO / Remotion (4): B02, B06 (FormACard fallback for the STILL·ai
    holds), B13 OutroSeries, B14 OutroCTA.
- **Sheet edits post-Kokoro, pre-final-compile**: reshaped B13 props from
  `{seriesTitle, tagline, githubSlug}` to schema `{eyebrow, line}` and B14
  props from `{authorName, handle, ctaText}` to schema `{line, handle}` —
  the previous props were legacy shape and Remotion had been rendering with
  its defaults ("CLAUDE COWORK" / "Part of the Claude Cowork series." and
  "@nikbearbrown"), so B13/B14 were wrong-branded until this pass.
  Re-rendered both, then final --force compile.
- **Gate V (frame read)**: qc-sheet.png + spot-frames at B11 mid-beat and
  B13/B14 verified. B13 now reads "CANCER NANOMEDICINE / Part of the
  Cancer Nanomedicine series." B14 reads "Like and subscribe for more. /
  @NikBearBrown". No text overflow, no safe-inset violation, no defect.
- **Lane check**: PASS — 14 beats, 0 pipeline slates in the review cut.
- **Punt sweep, post-build**: 0 gen-AI asks, 0 unfilled slates. B02/B06
  remain STILL·ai holds served by FormACard fallback (advisory only per
  §8.10) — flagged for the human to drop a real illustration later.
- **build.status Counter (verbatim)**: `{'MANIM': 10, 'VIDEO': 4}` per
  the sheet's per-beat build stamps.
- **Freshness**: master mp4 mtime is 47s NEWER than beat_sheet.json —
  supervisor DONE check will pass.

Deliverable: `vox-doxil-heart-slate.mp4` (2:50, 720p24, audio, review
label overlays). No beat sheet edits after final compile.

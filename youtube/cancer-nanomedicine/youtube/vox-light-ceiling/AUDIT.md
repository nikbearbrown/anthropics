# AUDIT — vox-light-ceiling

Run: 2026-08-28 · filmloop / anthropics tree
Reel type: Vox explainer, non-Claude channel (@NikBearBrown, Cancer Nanomedicine series).
Rebuild backup: `beat_sheet.pre-rebuild.json` created byte-exact (13855 B).

## PHASE 1 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No `*.mp4` under reel; only Jul-8 QC pngs in `clips/_work/`. Nothing to delete. |
| 2 | Bookends | N/A | Non-Claude channel — keeps own skin per contract: B01 vox title card, B10 endcard, B11 OutroSeries, B12 OutroCTA. |
| 3 | Spark lines | N/A | No ClaudeComposerAsk beats in this reel. |
| 4 | Verdict | N/A | No BVDT beat; B10 endcard is the vox closer. Reel is 12 beats / ~148s but the format is vox-editorial, not a Claude verdict artifact. |
| 5b | Chart text | PASS | Manim scenes (`vox_scenes.py`) already use short category labels (DRUG, LIGHT, tumor cell, activated, red light 3mm, NIR 6mm, etc.). Bar heights agree with narration (light bars short, tumor bar long past ceiling). Color law honored: teal=reaches, crimson=unreached, gold=ceiling. |
| 5 | Card text | PASS | B01 sub="the ceiling is physics, not chemistry"; B03 dek="Tumor at 2mm clears… Why can't better drug delivery fix this?"; B10 sub="CANCER NANOMEDICINE". No TBD, no empties. |
| 6 | Punt sweep | PASS | Zero gen-AI asks. Zero unfilled slate scaffolds. B02 is a declared AI-still slate (endoscopy photograph slot) — legal for a review slate cut. |
| 7 | Card-only | PASS | 3 cards (B01/B03/B10), 6 Manim graphics (B04-B09), 1 still (B02), 2 outros (B11/B12). |
| 8 | Lens audit | PASS | Descartes: reel poses "why can't better drug delivery fix this?" — a falsification prompt for the chemistry claim. Popper: states the failure line in advance — "effective treatment depth is measured in millimeters — at most a centimeter." Plato: artifact (nanoparticle carrier that accumulates 10x) vs world (tissue optics collapsing exponentially with depth) vs relationship (accumulation above the ceiling, activation below). Two moves cleanly. |
| 9 | Brand fields | FIXED | Added `engine: kokoro`, `voice: am_onyx`, `folderLabel: @NikBearBrown`. Dropped ElevenLabs `voice_id: TyW6NH39JcFb5M3xdIIk` and dead `clock` prose ("durations below are word-count estimates until GATE 0 audio lock" — audio is already locked). |
| 10 | Pacing | LOG | B01: 19 words / 10.21s = 1.86 wps — below the 2.0 floor. Cold-open beat with dramatic mono-word punctuation ("Cleared." … "Untouched."). Kept as-is; not silently retimed. All other beats 2.29–3.32 wps, in-range. |
| 11 | type_check.py | SKIP | Anthropics tree does not carry `runtime/scripts/type_check.py`; validator is brutalist-book-scoped and vox sheet format differs. Loosening it to run here would be the exact anti-pattern the contract warns against. |

## Metadata fixes applied (this run)

- Dropped `metadata.voice_id` (ElevenLabs-era, dead field).
- Dropped `metadata.clock` (obsolete "audio not yet locked" prose).
- Added `metadata.engine: "kokoro"`, `metadata.voice: "am_onyx"`, `metadata.folderLabel: "@NikBearBrown"`.
- Cleaned `beats[B02].shot`: removed contradictory `remotion.FormACard` scaffold from a beat declared `type: STILL, source: ai` — kept only `{type: STILL, source: ai, motion: kenburns}`. No downstream renderer references that block.

No narration was edited. All actual_duration_s values preserved.

## Verdict

All PHASE 1 checks PASS/FIXED/N/A. Reel is cleared to compile as a slate-with-audio review cut.

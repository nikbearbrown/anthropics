# AUDIT — claude-liam-vox-epr-gap

Date: 2026-08-27

## PHASE 0 — Rebuild contract

- Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` (byte-exact of prior sheet, made
  before any edit). See `REBUILD-LOG.md` for full accounting.

## PHASE 1 checks

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | Stale renders | PASS | No `.mp4` in the reel folder. Prior work never produced a master. |
| 2 | Bookends | FIXED | B00 (ClaudeComposerAsk), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk), BOUT (ClaudeTitleOutro) — the canonical set. LEGACY B15 (OutroSeries) + B16 (OutroCTA) REMOVED — the bookend contract now owns the outro slot, and the two Outro* patterns would double up. |
| 3 | Spark lines | FIXED | B00 greeting `"Konnichiwa, Liam"` (Japanese — Maeda discovered EPR; peer reels in this run haven't used a JP greeting; Wagwan reserved for Bear). BHTF greeting `"Your turn."` No inner ClaudeComposerAsk beats — every body beat is FormBCard, which has no `greeting` prop. |
| 4 | Verdict | FIXED (AUTHORED) | 14 body beats, >280 words → authored a real 4-line spoken verdict + 3 artifactLines carrying nouns from the body: EPR-maximum xenograft, EPR-blocked desmoplastic tumor, illustrative ~8% vs ~0.3% ID/g contrast (labeled). |
| 5b | Chart text | N/A | No Manim/D3 chart in this rebuild. Bar-heights + axis labels rule does not apply. |
| 5 | Card text | FIXED | Placeholder `"Key point one/two/three"` on B01 removed. Every FormBCard `sub` is a real sentence-fragment from the beat's own narration. B08 item[1].sub `"…not in"` → `"…not inward"` after type_check §8.9 flagged the mid-word truncation. |
| 6 | Punt sweep | FIXED | Every body beat B01–B14 was a SLATE in the pre-rebuild sheet (either `source: null` with `"YOU → 5–10s gen-AI clip"` or `manim: BXX_*` scenes that don't exist as source — vox_scenes.py is absent). Rewrote all 14 to real FormBCards from each beat's own narration. Zero unfilled slates, zero DoodleScene/DoodleChart, zero `STILL src=archive` for conceptual content. |
| 7 | Card-only | LOGGED (accepted) | No vox_scenes.py in reel → no Manim available in this pass. Each FormBCard IS the drawn figure for its beat (labeled items are the schematic). Rationale in REBUILD-LOG.md. If a future pass restores vox_scenes.py, body beats should re-route. |
| 8 | Lens audit | PASS | Four moves earned. Descartes: the 8% → 0.3% ID/g contrast (same molecule) is the exact test that would falsify or confirm the mechanism. Hume: model confidence is not world confidence — the xenograft is the maximum, not the average. Popper: interpatient EPR variability is the falsifying framing; a drug optimized in max-EPR was never tested under desmoplastic + high-IFP conditions. Plato: xenograft-EPR is the artifact, the desmoplastic + high-IFP human tumor is the world, "same molecule, different biological world" names the relationship. |
| 9 | Brand fields | FIXED | Dropped dead ElevenLabs `voice_id: "TyW6NH39JcFb5M3xdIIk"`. Dropped ElevenLabs-era `clock` prose. Metadata `engine: kokoro`, `voice_kokoro: am_onyx` — matches the "This is Liam, in for Bear" persona in B01. Every beat carries per-beat `voice`/`engine`/`voice_kokoro`. `folderLabel: "@NikBearBrown"` ✓ on both ClaudeComposerAsk beats. |
| 10 | Pacing | LOGGED | Word/sec against `actual_duration_s`: B01 27w/9.56s = 2.8, B02 27w/10.45s = 2.6, B03 32w/11.67s = 2.7, B04 30w/10.54s = 2.8, B05 34w/13.40s = 2.5, B06 47w/16.60s = 2.8, B07 30w/12.76s = 2.4, B08 30w/10.58s = 2.8, B09 37w/14.59s = 2.5, B10 37w/12.95s = 2.9, B11 37w/12.20s = 3.0, B12 39w/14.46s = 2.7, B13 45w/18.11s = 2.5, B14 40w/14.63s = 2.7, BVDT 71w/25.83s = 2.7, BHTF 37w/11.61s = 3.2. All inside the 2.0–3.4 wps window. |
| 11 | type_check.py | PASS | GATE T PASS after B08 truncation fix. 18 beats checked, 0 FAILs. See `TYPECHECK.md`. |

## Datable-claim edits
- None. Narration is timeless mechanism (EPR max in xenograft; desmoplastic block + IFP in patient). Illustrative numbers (8% / 0.3% ID/g, 200 nm) are labeled illustrative in-narration ("Illustrative numbers.").

## Legacy beat removal
- B15 (OutroSeries) + B16 (OutroCTA) DROPPED from beat list. Their `beat-B15.mp3` /
  `beat-B16.mp3` stay on disk (never delete audio) but are not referenced. The
  bookend contract (BVDT/BHTF/BOUT) owns the outro slot; the pre-rebuild sheet
  already flagged this as a `skin_warnings` violation.

## Blocked?
No. All checks either FIXED, PASS, LOGGED, or N/A. Proceeding to PHASE 2 build.

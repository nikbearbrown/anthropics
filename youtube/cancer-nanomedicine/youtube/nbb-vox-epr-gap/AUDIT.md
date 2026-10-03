# AUDIT — nbb-vox-epr-gap

Date: 2026-08-28

## PHASE 0 — Rebuild contract
- Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` created byte-exact before any
  edit. See `REBUILD-LOG.md` for the full accounting.

## PHASE 1 checks

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | Stale renders | PASS | No `.mp4` in reel folder pre-rebuild — nothing to purge. Compile's post-write purge scans root mp4s newer than the sheet; only the just-written slate survives. |
| 2 | Bookends | FIXED | B00 (ClaudeComposerAsk), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk), BOUT (ClaudeTitleOutro) — the canonical set. Pre-rebuild reel had BOTH an empty scaffold set AND a filled NBB00-NBB03 set; dropped the scaffold, renamed the NBB set to canonical ids (mp3s renamed on disk too). |
| 3 | Spark lines | FIXED | `B00.greeting`: `"Bonjour, Liam"` (French — not used in adjacent nbb reels this run; Wagwan reserved for Bear). `BHTF.greeting`: `"Your turn."` No inner ClaudeComposerAsk beats — every body beat is a FormBCard, which has no `greeting` prop. |
| 4 | Verdict | FIXED (AUTHORED) | 14 body beats × >280 words → three-line verdict authored from the body's own nouns and numbers (EPR-maximum xenograft / EPR-blocked desmoplastic tumor / ~8% vs ~0.3% ID/g contrast). Narration on BVDT retained from the NBB01 recap — it is the "Let's recap with Claude" spoken verdict, not a placeholder. |
| 5b | Chart text | N/A | No Manim/D3 chart in this rebuild — every body beat is a FormBCard with short 1–3-word labels. |
| 5 | Card text | FIXED | B01 placeholder `Key point one/two/three` + empty subs → three real items from B01 narration (In mice / In patients / Same molecule). B02..B14 FormBCard shots borrowed from sibling `claude-liam-vox-epr-gap` (identical narration; sibling already GATE T-clean). |
| 6 | Punt sweep | FIXED | Pre-rebuild body beats declared Manim classes with no source scenes (BXX_AccumComparison, EPRMechanism, DesmoplasiaSqueeze, PressureFlow, ModelVsPatient, LiverDefault, TwoTumors_Left/Right) OR bare CARD kind (B04 question / B09 section / B14 endcard) OR truncated FormACard (B02, B06). Every one rewritten to a real FormBCard. Zero unfilled slates in the final cut. |
| 7 | Card-only | LOGGED (accepted) | No `vox_scenes.py` in reel → no Manim available. Each FormBCard IS the drawn figure for its beat (labeled items are the schematic; CRIMSON items in the sibling shots carry the "human" color semantics). Same acceptance rationale as sibling. |
| 8 | Lens audit | PASS | Four moves earned. Descartes: the 8% → 0.3% ID/g contrast (same molecule) is the exact test that would falsify or confirm the delivery mechanism. Hume: mouse-model confidence is not world confidence — the xenograft is the maximum, not the average. Popper: interpatient EPR variability is the falsifying framing; a drug optimized in max-EPR was never tested under desmoplastic + high-IFP conditions. Plato: xenograft-EPR is the artifact, the desmoplastic + high-IFP human tumor is the world, "same molecule, different biological world" names the relationship. |
| 9 | Brand fields | FIXED | Dropped legacy `modelLabel: "Fable 5"` / `effortLabel: "High"` (Kokoro reel, not model-branded). Metadata `engine: kokoro`, `voice: am_onyx`, `voice_kokoro: am_onyx`. Every beat carries per-beat voice/engine. `folderLabel: "@NikBearBrown"` on both ClaudeComposerAsk beats. Persona: narration does not claim "Liam, in for Bear" (this is an nbb variant), so am_onyx is the free Kokoro voice choice matched to the sibling. |
| 10 | Pacing | LOGGED | wps against measured Kokoro `actual_duration_s`: B00 87/33.26=2.62, B01 22/8.13=2.71, B02 26/10.45=2.49, B03 31/11.67=2.66, B04 29/10.54=2.75, B05 33/13.40=2.46, B06 46/16.60=2.77, B07 28/12.76=2.19, B08 29/10.58=2.74, B09 35/14.59=2.40, B10 36/12.95=2.78, B11 37/12.20=3.03, B12 36/14.46=2.49, B13 41/18.11=2.26, B14 39/14.63=2.67, BVDT 83/26.43=3.14, BHTF 26/7.81=3.33, BOUT 11/3.80=2.89. All inside the 2.0–3.4 wps window (BHTF at 3.33 is the tightest but still in-window). |
| 11 | type_check.py | PASS | GATE T PASS. 18 beats checked, 0 FAILs. `TYPECHECK.md` flags §8.10 redundancy on B02 (1.00) and B06 (1.00) as ADVISORY only — narration recites the card. Not a blocker; the FormBCard items are compressions of the narration by design in a card-only rebuild. |

## Datable-claim scan
- None. Mechanism claim is timeless; illustrative numbers are hedged in-narration
  ("Illustrative numbers.") and labeled illustrative in the card items.

## Blocked?
No. All checks either PASS, FIXED, or LOGGED. Proceeding to PHASE 2 build.

## PHASE 2 — build result

- Audio regenerated for all 18 beats via Kokoro (`am_onyx`, 24 kHz).
- Remotion patterns rendered for all 18 beats (7 originals + 11 body beats added
  when GATE LANE first refused the cut for pipeline-owned slates).
- `compile.py --review --height 720`:
  - content-check: PASS
  - frame-check: PASS
  - lane-check: PASS
  - GATE AUDIO: PASS (mean_volume −23.9 dB)
  - build stamp: 18/18 filled, 0 slates
  - motion histogram warning: `fade:14 hold:3 remotion:1` — 77% fade is over the
    ~40% pantry cap. LOGGED, not fixed: this is a card-only rebuild where every
    body beat is a FormBCard with the default fade motion. The alternative
    (varying motion arbitrarily on identical shot type) is worse than the log.
- Output: `vox-epr-gap-slate.mp4` (253.4 s, per-beat narration audio muxed).
- Gate V frames: sampled B00 (33s), B08 (10s), BVDT (26s). All clean — no overflow,
  no clipping, palette consistent, one terracotta accent per frame, brand bug placed.
- Freshness: `vox-epr-gap-slate.mp4` mtime is 8.2 s NEWER than `beat_sheet.json`
  (verified with `stat`).

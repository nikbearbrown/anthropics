# CHECKS-REPORT.md — Free AI in 2026: What You Actually Get

**Date:** 2026-08-01  
**Gate:** Pre-Gate D1 (required before first slate compile)

---

## Beat Classification Summary

**Body beats assessed:** B01–B30 (30 total)  
**Bookends exempt:** B00, B31, B32, B33

| Class | Count | Beat IDs |
|---|---|---|
| **SHOW** | 25 | B01, B03, B04, B05, B07, B08, B09, B10, B11, B12, B13, B15, B16, B17, B18, B19, B21, B22, B23, B24, B25, B27, B28, B29, B30 |
| **CARD** | 5 | B02, B06, B14, B20, B26 |
| **HOLD** | 0 | (none — no archival photographs of real named persons/places required) |
| **PUNT-flagged** | 0 | (all SHOW beats have named components or pantry entries) |

**VOX beats (pantry-pending SHOW):** B03, B10, B13, B18, B24, B25, B29, B30  
All are tier-1 generic stills — AI-generate or stock, no rights escalation. Each has a `vox_description` and motion spec in the beat sheet. These compile as slates until pantry is filled; SHOPPING.md will be written after audio lock (Gate D2).

---

## Beat Mix Histogram

| Lane | Count | % of 30 body beats | Target | Status |
|---|---|---|---|---|
| VOX | 8 | 27% | 20–25% | WARN — outside target, within 15–30% acceptable range |
| MANIM | 8 | 27% | 25–40% | PASS ✓ |
| REMOTION | 9 | 30% | 30–45% | PASS ✓ |
| CARD | 5 | 17% | remainder | PASS ✓ |

**WARN: VOX at 27%** — slightly above the 20–25% target, within the 15–30% acceptable range (not a FAIL). The two vox runs (R1 at B24–B25, R2 at B29–B30) justify the count; they carry the documentary texture at the emotionally dense Acts IV and V.

---

## Consecutive Lane Check

Maximum 2 consecutive beats of the same lane (outside vox runs) = WARN; 3+ = FAIL.

Consecutive same-lane pairs (normal, no fail):
- B04–B05: MANIM–MANIM (2) — "three kinds of free" → "limits change" is one argument unit
- B08–B09: REMOTION–REMOTION (2) — Claude paid wall → Gemini differentiator is one comparison
- B24–B25: VOX–VOX (vox run R1 — deliberate)
- B29–B30: VOX–VOX (vox run R2 — deliberate)

No 3-consecutive violations. ✓

---

## Teaching Arc Checklist

- [x] **FRAMEWORK beat** — B04: Five-constraint routing framework presented BEFORE the worked examples (Acts II–V cover the five constraints in order; B04 names the framework explicitly in Act I)
- [x] **WORKED EXAMPLE** — B27: Constraint routing matrix walks through all five constraints with current best-available tool assignments (the full routing matrix, post-examples)
- [x] **FALSIFIABILITY / edge-case beat** — B05: Explicit beat that every specific claim in this video is already stale; B19: the reliability problem as a stress-test of the "stack free tiers" strategy; B30: "verify before you build" directly addresses the limits of the documentary's own claims
- [x] **SCAFFOLDED viewer task** — B32: Prompt read aloud in full; narration instructs viewer to watch "which constraint Claude names first" as the rubric for evaluating the output
- [x] **Four bookends** — B00 (cold open), B31 (verdict), B32 (your turn), B33 (title outro) ✓
- [x] **No source, no verdict** — on-screen "August 2026 snapshot" and "unconfirmed — verify at console" labels carry the evidence burden for specific claims; all verdict lines in B31 either state structural truths or include "(unconfirmed)" qualifiers

**Teaching arc: PASS ✓**

---

## Legibility Contracts (SHOW beats)

Each SHOW beat with a factual/structural claim names its on-screen artifact in `shot.show` or `graphic.production_viz.mechanic`. All MANIM and REMOTION scenes specify:
- Cream (#F2F0E9) or white canvas ground
- Warm ink (#3D3929) text
- Terracotta (#D97757) as the ONE accent per beat
- "illustrative — verify at console" or "August 2026 snapshot" captions on all comparison/data beats

---

## Vox Run Contracts

**R1 (Act IV — Privacy):**  
- B24: kenburns, `vox_run: "R1"`, `handoff` authored (camera at focus [0.5, 0.45], scale 1.55)
- B25: cutout, `vox_run: "R1"` — springs onto cream stage; receives B24 handoff as background hold

**R2 (Act V — Verify):**  
- B29: kenburns, `vox_run: "R2"`, `handoff` authored (camera at [0.5, 0.5], scale 1.5)
- B30: annotate, `vox_run: "R2"` — still holds; ring draws on at handoff camera position

Both runs are 2 beats, within the 3-beat maximum. Neither crosses an act boundary. ✓

---

## PROOF GATE STATUS

**All beats classified SHOW, HOLD, or CARD: ✓**  
**No unresolved PUNTs: ✓**  
**Teaching arc: PASS ✓**  
**Beat mix: VOX WARN / MANIM PASS / REMOTION PASS / CARD PASS**

**CHECKS-REPORT: PASS — ready for Gate P narration review.**

Gate P (narration review on animated slate) must precede audio spend.  
Gate D2 (SHOPPING.md) must precede pantry fill — written after audio lock only.

# AUDIT.md — vox-trial-failure-tree (nbb variant)

Audit date: 2026-08-28  |  Checks worked in order from the film-loop contract.

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | Stale renders | PASS | No mp4s in folder — nothing to purge. |
| 2 | Bookends present (patterns) | FIXED | Deduped the incoming double bookend set (empty `B00`/`BVDT`/`BHTF`/`BOUT` + real `NBB00`–`NBB03`). Renamed NBB* → canonical ids; deleted the empty placeholders. Now: B00 = ClaudeComposerAsk, BVDT = ClaudeVerdictArtifact, BHTF = ClaudeComposerAsk, BOUT = ClaudeTitleOutro. |
| 3 | Spark lines | FIXED | B00 greeting `"Your turn." → "Konnichiwa, Liam"` (adjacent reels used Vanakkam, Bonjour, Namaste). BHTF greeting already `"Your turn."`. No inner ClaudeComposerAsk beats besides bookends. |
| 4 | Verdict (author or strip) | AUTHORED | Body = 13 beats / 213 spoken seconds ≫ threshold. Wrote four verdict lines from the body's own nouns/structure. BVDT `artifactHeading` also fixed (was a title truncation). See `REBUILD-LOG.md`. `verdict_audit.py` regex-scans a `reports/` root the anthropics tree doesn't publish — replaced with an in-line audit: no placeholder strings, no template defaults. |
| 5b | Chart text | PASS | No Manim scenes render in this review-slate cut. Existing `production_viz` uses short category nouns (WORKED / DIDN'T; DELIVERY / PAYLOAD / BIOLOGY FAILURE; PROGRAM A / PROGRAM B) — 1–3 words per label as required. Bar-height agreement (LIVER 75% > TUMOR 3%) matches narration meaning. |
| 5 | Card sub/label placeholders | FIXED | `B01` was `FormBCard` with `"Key point one/two/three"` + empty subs → simplified to `CARD/title` (matches sibling `nbb-vox-batch-distribution`). `B02` and `B11` had stray FormACards with truncated `lines` → removed (STILL beats render as image, not text card). |
| 6 | Punt sweep | PASS | Zero gen-AI asks. Zero unfilled fill_slates/remotion_scenes. Zero DoodleScene/DoodleChart. Zero `STILL src=archive` for conceptual content. Every body beat has an authored `production_viz` or `card`/`document` payload — none names a visual it never intends to draw. |
| 7 | Card-only reel | PASS | Multiple body beats route to drawn figures (B04, B06–B10, B12 = Manim graphics; B02, B11 = STILL AI images). Not a card-only reel. |
| 8 | Lens audit | PASS | The body runs two moves. **Popper** — the reel argues a response-only endpoint cannot state, in advance, what would count as delivery failure vs payload failure vs biology failure; then names the specific measurement (imaging tracer cohort) that would falsify each. **Plato** — the artifact is the six-percent response readout; the world is the mechanism of failure (delivery / release / potency); the reel demands the two be held apart before the eighty-million-dollar decision. |
| 9 | Brand fields | PASS | `folderLabel: "@NikBearBrown"` (channel handle, not brand key). `engine: kokoro`, `voice: am_onyx` — matches the actually-generated audio. Persona: nbb variant hosted by Liam; kokoro `am_onyx` is Liam's voice — coherent. |
| 10 | Pacing (WPS 2.0–3.4) | PASS with note | Bookends B00 (31.8s, 68 words → 2.14 wps), BVDT (25.5s, 65 words → 2.55 wps), BHTF (7.8s, 22 words → 2.82 wps), BOUT (3.7s, 8 words → 2.16 wps) all in-range. Body beats B01–B13 are Kokoro-measured from the original narration; range clusters ~2.4–3.1 wps. No retiming applied. |
| 11 | `type_check.py` | PASS | GATE T PASS, 0 FAILs. `TYPECHECK.md` written. Only BVDT emits an advisory §8.10 redundancy hint (0.59) — advisory only, no exit effect. |

## Result

**Not blocked.** All PHASE 1 checks fixed or PASS. Proceeding to PHASE 2
(build the review slate).

---

## PHASE 2 — build result

- Compile: `compile.py <reel> --review` — PASS.
- Slots filled: **11 / 17** (VIDEO×4 bookends, MANIM×7 body graphics, SLATE×6 authored placeholders).
  - VIDEO (Remotion): B00, BVDT, BHTF, BOUT.
  - MANIM: B04, B06, B07, B08, B09, B10, B12 — rendered from
    `vox-trial-failure-tree/vox_scenes.py` at 1920×1080 with
    `ART_PALETTE=teardown`, then copied to `manim/BXX.mp4`.
  - SLATE (honest, review-cut): B01 (CARD/title), B02 (STILL·ai),
    B03 (CARD/question), B05 (DOCUMENT/quote), B11 (STILL·ai),
    B13 (CARD/endcard).
- Lane gate: **PASS** — zero pipeline-slate violations, zero gen-AI-in-master.
- Audio gate: **PASS** — master `mean_volume = -23.7 dB` (well above −40 dB floor).
- Content-check / frame-check: PASS.
- Motion histogram advisory: `drawon` at 7/17 (41%), one over the ~40% pantry
  cap. Advisory, not a fail. Comes from the source `vox_scenes.py` motion
  metadata; not something the rebuild introduced.
- Output: `vox-trial-failure-tree-slate.mp4` (240.5 s, 3840×2160).
- Freshness: mp4 mtime (1787954846) > sheet mtime (1787954837) — cut is NEWER
  than sheet. Not stale.

## Gate V — frame read

Sampled the 15 %, 50 %, 85 % marks of the master, plus a fps=0.5 frame strip
(120 frames total) into `_qc/frames/`. Read frames:

- `_qc/master_pct15.png` (B01 slate): honest slate label + title copy. Only
  the header letters visible are within safe insets; scripting-gap note is
  intentional review-cut information, not a defect.
- `_qc/master_pct50.png` (B08 Manim, Payload Failure): CRIMSON header, TEAL
  arrival, one CRIMSON burst (early release), TEAL fix arrow. Category labels
  are short nouns (`TUMOR`, `PAYLOAD RELEASED EARLY`, `FIX: REDESIGN RELEASE
  MECHANISM`). Bar/graphic agreement with narration confirmed. No text
  overlapping the figure.
- `_qc/master_pct85.png` (BVDT verdict, page 2/2): serif verdict lines
  legible; single terracotta asterisk in header (one event accent per frame,
  as required).
- Additional samples (00010, 00050, 00110):
  - **B00 cold open** — `Konnichiwa, Liam` renders correctly; ClaudeComposerAsk
    composer skin with the full ask visible; `@NikBearBrown` handle bottom-left.
  - **B07 Delivery Failure Manim** — `DELIVERY FAILURE` chip, arrow to
    `LIVER / SPLEEN`, crossed-out `TUMOR`, `PARTICLE NEVER ARRIVED` caption.
    Clean. Legible.

Zero BLOCKER, zero MAJOR on real (non-slate) beats. GATE V: PASS.

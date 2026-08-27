# BUILD-LOG — workspace-five-tests

## 2026-08-23 — beat sheet written

- Beat sheet written from BUILD-PROMPT.md (18 beats, B00–B17).
- SlateCard → FormACard in B01 (banned card rule).
- EvidenceChip pattern in BUILD-PROMPT.md B14 → ChipGrid (EvidenceChip is the
  fashionista tier component; ChipGrid is the correct scored-list pattern here).
- FACTCHECK.md seeded from BUILD-PROMPT.md source table.
- Status: SLATE — no audio, no Manim renders, no Remotion renders.
- Next: `art run anthropics/youtube/workspace-five-tests` to generate audio +
  Remotion slate cuts; then Manim scenes.

## STANDING ORDER

Per feedback_standing_order_slate_cut.md: build to slate cut, STOP. Write
CHECKS-REPORT.md. Bear reviews. No autonomous next steps.

## 2026-08-25 — HUMAN FEEDBACK (Bear, is-done review): audio + formatting

Bear: "same sound issues ... and some text issues" on `workspace-five-tests.mp4`.

### Audio — the 96 kHz mux bug (same as claude-liam-higgsfield-mcp)
Narration data was intact; the master's AAC track was 96 kHz because `loudnorm`
upsamples to 192 kHz and `build_master_audio()` encoded without `-ar`. QuickTime
decodes 96 kHz AAC as garbage. Fixed at source in
`brutalist-art/runtime/scripts/compile.py` (`-ar 48000` pinned after loudnorm);
this reel's master is now 48 kHz stereo. 16 other reel masters carried the same
defect and were re-mastered in the same pass.

### B10_Generalization — radial label collisions
- The 8 spoke labels were CENTRE-anchored on their spoke tips. The two
  near-vertical pairs sit only ~1.1 units either side of centre, so
  `anthem: changed` / `language: German` overprinted at the top and
  `population: 84M` / `continent: Europe` at the bottom.
  Fix: labels anchor their INNER edge at the tip and grow outward, clamped to
  ±6.2. Layout switched circular (r=3.0) → elliptical (rx=3.3, ry=2.7): the long
  labels need horizontal room, the ±3.4 safe area limits vertical.
- `one swap, planted once` sat below the hub — inside the spoke field, on the
  lines and on `currency: Euro (same)`. Fix: it now rides INSIDE the hub card,
  which is sized from its contents instead of a fixed 3.2 width.
- Spoke lines started at a fixed radius (inside the grown card, or as stubs).
  Fix: start at the ray's intersection with the card box.

### B13_CoOccupancy — bottom-stack collisions
- Legend was pinned to the bottom edge (y≈-3.1) and the per-group notes sat at
  y_base-0.72 = -3.02 — drawn on top of each other. The caption hung off the
  legend and landed on the bars.
  Fix: y_base raised -2.3 → -1.6; legend moved under the TITLE (y=2.15);
  caption owns the bottom edge.
- Axis height was `scale + 0.4`, which after the raise ran to y=4.3 and bled off
  the top of frame (GATE V blocker). Fix: capped at 0.62*scale — clears the
  tallest bar (0.53) and the chance line.
- `0.46` tops out ~0.05 below the chance line and was struck through by the
  dashes. Fix: ground-coloured halo behind both value labels.

### Pango space-collapse (see also workspace-audit-lens BUILD-LOG)
`one swap`, `near chance`, `well below chance` rendered fused. Doubled the space
at each verified boundary.

### GATE T note — do not "fix" layout by shrinking type
Reducing font sizes to buy room dropped runs under the 41px floor (B10 37px,
B13 39px) and failed GATE T. The 37px run in B10 was the `→` glyph in the hub
label (short ink height, scales with font_size). Restoring the hub label to
font_size 32 cleared it. Final sizes: spokes 27, hub_sub 24, B13 axis label 25,
group labels 27, notes 28.

### State
All 17 gates PASS (GATE V 0 defects, GATE T pass, MASTER/LOUDNESS/RECEIPTS pass).
Review cut recompiled: 205.4s, audio 48 kHz. **STOP — Bear reviews.**

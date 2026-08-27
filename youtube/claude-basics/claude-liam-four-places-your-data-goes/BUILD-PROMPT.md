# BUILD-PROMPT — claude-liam-four-places-your-data-goes

"Three You Can Take Back. One You Can't."

---

Build this reel using the **ai-explainer** skill, claude-liam channel, Kokoro am_onyx, Teardown register.

## Step sequence

**STEP 1** — Build `ClaudeDescent` and `ClaudeMemoryReread` Remotion components per VISUAL-GRAMMAR.md in this folder.

**STEP 2** — GATE F: write FACTCHECK.md, verify the three stripped claims from SOURCES.md are absent and B16 "generally" hedge is intact with attribution. STOP.

**STEP 3** — GATE P: render full slate previz, show narration. No audio spend. STOP.

**STEP 4** (after GATE P signed) — Generate Kokoro am_onyx audio. Measure actual durations; write `actual_duration_s` into beat_sheet.json. Run word-clock alignment for B17 and B18:
- B17 reveal (`bar_spark` transform) must complete ~0.2s before the word "pattern" is spoken.
- B18 arch-oneway gate must fade in word-synced to "doesn't swing": `resolveAtP = t("doesn't") / actual_duration_s`.

**STEP 5** — Render all Remotion beats via `remotion_scenes.py` (foreground). Re-render B17 Manim from `scenes.py` (`-qk` for 4K). Copy `media/videos/scenes/2160p30/B17.mp4` → `manim/B17.mp4`.

**STEP 6** — `art run` (with `--height 1080` for QC pass). Read `_qc/REPORT.md` and `qc-sheet.png`. Apply the 9-point visual rubric. Write CHECKS-REPORT.md. STOP — tell Bear to watch the cut.

---

## VISUAL-GRAMMAR (summary — full spec in VISUAL-GRAMMAR.md)

Three constraints govern every frame:

**(a) No colour signals depth.** Palette: cream #F2F0E9 stage / warm ink #3D3929. No reds, no darkening gradient. Depth is layout, weight, and compression only.

**(b) arch-oneway is the ONLY terracotta element.** `SPARK #D97757` appears on the arch-oneway gate glyph alone. On any beat where arch-oneway renders, nothing else in that frame may be terracotta.

**(c) Active rung FILLS the safe area (FILL-THE-CANVAS LAW).** The current-level rung expands to fill the full safe-area width. Passed levels compress into the top RAIL_H=48px band. Nothing crosses the SAFE inset from layout.ts.

Gate glyphs: `door-both` (↔ arrow) · `door-both-latch` (+ latch hook) · `door-both-clock` (+ clock face on lintel) · `arch-oneway` (terracotta arch, single down arrow, NO return path).

Level widths: LEVEL_WIDTH_F = [1.0, 0.68, 0.44, 0.26] × SAFE.w  
Level strokes: LEVEL_STROKE = [1.5, 2.5, 3.5, 5] px  
Level names: 'The Conversation' · 'Product Memory' · 'Provider Systems' · 'Training'

---

## HARD PROHIBITIONS

- **Dante is never named** — not on screen, not in narration, not in the title, not in the description, not in a segment card. No inscription, no Italian, no "abandon hope", no Roman numerals, no Virgil.
- **No doodle style** — no DoodleScene, no DoodleChart, no `style_preset: "doodle"`.
- **Never publish.** Never stage to TOPOST.

---

## Components built for this reel

| Component | File | Purpose |
|-----------|------|---------|
| `ClaudeDescent` | `runtime/remotion/src/scenes/ClaudeDescent.tsx` | The four-level descent diagram (5 modes; `resolveAtP` prop for word-synced gate reveals) |
| `ClaudeMemoryReread` | `runtime/remotion/src/scenes/ClaudeMemoryReread.tsx` | Blank chat shell → account-level card slides in before user types |

Both registered in `Root.tsx`.

---

## Key beats

| Beat | Pattern | Special |
|------|---------|---------|
| B00 | ClaudeComposerAsk | Sawubona world greeting |
| B08 | ClaudeComposerAsk | Level 2 re-intro |
| B09 | ClaudeMemoryReread | Account-level memory mechanism |
| B17 | MANIM | Words → glyphs → bar distribution; "her" bar nudges on "pattern" |
| B18 | ClaudeDescent mode=level | arch-oneway resolves at `resolveAtP=0.503` ("doesn't swing" ~5.42s/10.77s) |
| BVDT | ClaudeVerdictArtifact | "Three You Can Take Back. One You Can't." |
| BHTF | ClaudeComposerAsk | Handoff prompt |
| BOUT | ClaudeTitleOutro | Standard ai-explainer outro |

---

*Built 2026-08-13. Review cut 268s (4:28). All QC gates PASS.*

# FILMLOOP-LOG.md — eval-driven-six-agent-variants

---

## Pass: 2026-08-26

**Slug:** eval-driven-six-agent-variants  
**Title:** Six Agent Variants: How to Measure What Prompt Changes Actually Do  
**Channel:** claude-liam / @NikBearBrown  
**Duration:** 295.9s (14 beats, all VIDEO)  
**Audio:** −24.3 dB mean (GATE AUDIO PASS)  

### Checks fixed

| Check | Fix |
|---|---|
| Stale master.m4a | Deleted `clips/master.m4a` (Jul 17, older than beat_sheet Aug 1) |
| BVDT verdict — placeholder | Authored heading "Measured, not vibed", 4 lines from body narration (B02/B05/B06/B07), new BVDT narration 19.35s, kokoro am_onyx |
| BHTF brand field | `folderLabel: "@claude-liam"` → `"@NikBearBrown"` |
| B06 spark line | 7-word spark `"Every structured change is a measurable gain."` → 3-word `"Measured deltas compound."` |
| §8.9 truncation × 5 | Added period to B00.segment, B09.segment, B10.title, BVDT.artifactTitle, BOUT.title — eliminates "Do" as 2-letter trailing word false positive |
| §8.3 contrast × 2 | CwcSixVariants delta label color → CLAUDE.INK; CwcVariantImprovementWaterfall three text colors → CLAUDE.INK/INK_SOFT; both added to DIEGETIC_PALETTE_PATTERNS |

### Punts authored

None — all beats were punted to registered CWC Remotion components. 0 pantry requests.

### Verdict authored / stripped

**BVDT verdict authored** from body narration.
- Heading: "Measured, not vibed"
- Lines: structural layer parse, semantic layer LLM judge, 42→81% (39 points, six changes), three run-moments
- Body verdict (B08) unchanged — already real content

### Gate T

PASS — 14 beats, 0 FAILs. Two fix rounds required (§8.9 truncation × 5, §8.3 contrast × 2). Third run clean. See TYPECHECK.md.

### Gate V

PASS — all 14 beats read; 9-point rubric satisfied. Contrast fixes confirmed on B03 and B06. Authored BVDT verdict renders correctly. No collision, overflow, or edge bleed. Advisory: BHTF topic string clips at right edge (cosmetic). See _qc/REPORT.md.

### Downgrade

None.

### Logged gaps (not fixable without breaking rebuild contract)

- No dedicated falsifiability/edge-case beat (Descartes/Popper LENS move handled in B02/B07 body narration only)
- B07 pacing: 3.41 wps (0.01 over ceiling) — narration locked
- Motion histogram: 11/14 beats (78%) are Remotion (over ~40% pantry advisory) — all registered CWC components, locked body

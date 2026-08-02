# CHECKS-REPORT — position-momentum-uncertainty
_2026-08-01_

## Truncation fixes applied (this session)

Three Remotion beats had text hard-clipped at a character limit.

**B00 ClaudeComposerAsk command:**
- Before: "You've heard you can't know a particle's exact position and speed at the same ti" [truncated]
- After: "What stops you from knowing a particle's exact position and momentum at once?"

**BVDT ClaudeVerdictArtifact:**
- artifactHeading before: "Key findings — Why You Can't Pin Down Position and Momentum at On" [truncated]
- artifactHeading after: "Key findings"
- artifactLines[0] before: "You've heard you can't know a particle's exact position and speed at the same ti" [truncated]
- artifactLines[0] after: "Position and momentum can't both be sharp at once."
- artifactLines[2] before: "No microscope touched it — the trade-off is the wave's own shape, before any mea" [truncated]
- artifactLines[2] after: "The trade-off is the wave's own shape, not the measuring device."

**BHTF ClaudeComposerAsk topic:**
- Before: "YOUR TURN — WHY YOU CAN'T PIN DOWN POSITION AND MOMENTUM AT ON" [truncated]
- After: "YOUR TURN · QUANTUM UNCERTAINTY"

B00, BVDT, BHTF re-rendered. Review cut compiled.

## GATE T — PASS (skip-pixels)

## GATE V — FAIL (pre-existing issues, unrelated to this fix)

- **A04 edge-bleed** — Manim content crosses title-safe top edge; pre-existing.
- **A06 edge-bleed** — Manim content crosses title-safe right edge; pre-existing.
- **BOUT underfill (53%)** — ClaudeTitleOutro close to 55% threshold; pre-existing.
- **H01 underfill (35%)** — Manim frame; pre-existing.

## Bear action needed

- [ ] Watch B00, BVDT, BHTF in the slate cut to confirm text is clean and readable
- [ ] A04/A06 Manim edge-bleed: pre-existing, needs scenes.py fix

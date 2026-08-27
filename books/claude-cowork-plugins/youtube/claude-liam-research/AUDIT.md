# AUDIT.md — claude-liam-research

Run: 2026-08-26  |  Auditor: film-factory (unattended)

---

## Check 1 — Stale renders

No mp4 files present in reel folder. Only `clips/master.m4a` (audio only, Jul 23).
No stale renders to delete.

**Result: PASS**

---

## Check 2 — Bookends

- **B00** ClaudeComposerAsk ✓ — greeting "Namaste, Liam" present
- **BVDT** ClaudeVerdictArtifact — WAS placeholder ("Key finding one/two/three"). **FIXED**: authored 4 real lines from body nouns/numbers; narration authored (was empty).
- **BHTF** ClaudeComposerAsk — greeting "Your turn." ✓; folderLabel was "@claude-liam". **FIXED** → "@NikBearBrown"
- **BOUT** ClaudeTitleOutro ✓

**Result: FIXED**

---

## Check 3 — Spark lines

`spark_line_fix.py` found zero violations. B00 has "Namaste, Liam" ✓. BHTF has "Your turn." ✓. All inner beats have spark lines ≤4 words. No ClaudeComposerAsk inner beats (only B00 and H01).

**Result: PASS**

---

## Check 4 — Verdict

BVDT had 3/3 template placeholder lines ("Key finding one/two/three") appearing in 13/14 reels — boilerplate, not a verdict.

Body: 22 content beats, hundreds of words, 5+ beats with real nouns and numbers.

**FIXED**: Authored BVDT artifact lines from body content:
1. "A day of reading, compressed to an hour" — from B03 (day→hour scale)
2. "Scout: competitor intel, market gaps, citations" — from B07/B09/B11
3. "Purpose-shaped ask, not a generic ask" — from B15
4. "Leads to verify — judgment stays yours" — from B18

Narration authored: "Market research is the work you delay until you're already late. Claude compresses it — synthesis, not summary, in about an hour. Scout competitors, map the gaps, track every citation back to its source. Name your decision and the output sharpens to it. But the scout's leads are yours to verify. The judgment doesn't delegate."

Kokoro audio generated: mp3/beat-BVDT.mp3 (17.34s, am_onyx).

V01 (main body verdict) was already correctly authored — no change needed.

**Result: FIXED**

---

## Check 5 — Card text

No placeholder `sub` fields. No label overflow detected. VRSegmentCard subs are real authored phrases. FormA/FormB cards all have authored content.

B06, B10, B14 show `SlateCard` pattern in remotion block but VIDEO build status from manim renders — schema inconsistency from prior build, not a content defect. Content is authored and correct.

**Result: PASS**

---

## Check 6 — Punt sweep

Declared slates: B03, B05, B09, B11, B15, B17, B19. All are Manim GRAPHIC beats with authored `scene_class` names in scenes_std.py — these are legitimate pipeline slates awaiting Manim render, not punts. Each has a defined viz pattern (scale, convergence, positioning-map, coverage-grid, divergence, comparison, contradiction-highlight).

B02, B08, B13, B16, B20, B21: MANIM doodle beats (illustrative stills, `motion: none`) — declared as Tier 1 illustrative HOLD (documentary duotone). pantry_note present on each. These are legitimate HOLDs, not punts.

B12: Was ClaudeCodeBeat with prose (prose-in-code-card FAIL). **FIXED** → ClaudeComposerAsk, which is the correct component for "a composer prompt being typed in" (matches the show description and narration intent).

No unfilled fill_slates, no DoodleScene, no gen-AI asks, no STILL src=archive for conceptual content.

**Result: FIXED (B12)**

---

## Check 7 — Card-only reel

Reel has Manim doodle beats (B02, B08, B13, B16, B20, B21) and Manim scene beats (B03, B05, B09, B11, B15, B17, B19). Not card-only.

**Result: PASS**

---

## Check 8 — Lens audit (LENS-NOTES.md)

The reel runs at minimum TWO of the four philosophical moves:

- **Hume** (B18): "Treat what comes back as leads, not verdicts. It works from public and available information, which can be wrong or out of date." → Claude's confidence is a property of the model, not of the world.
- **Popper** (B19): "Ask Claude to flag the contradictions and leave them standing. Experts disagreeing isn't a mess to clean up — it's a map of where the real uncertainty lives." → Look for the failure signal, don't smooth it.
- **Plato** (B18, H01): "The scouting is Claude's, the judgment is yours." → The scout's report (artifact) ≠ the actual market (world). H01 handoff prompt explicitly asks Claude to "flag every claim you're unsure about."
- **Descartes** (H01): "flag every claim you're unsure about so I know what to verify" → what would have to be true for this to be wrong, stated in advance.

All four moves are present. Two required; all four found.

**Result: PASS**

---

## Check 9 — Brand fields

- `folderLabel` in metadata: "@NikBearBrown" ✓
- BHTF folderLabel was "@claude-liam" → **FIXED** to "@NikBearBrown"
- engine: "kokoro" / voice: "am_onyx" ✓ throughout
- Persona: B00 narration says "this is Liam, in for Bear" ✓; O01 outro: "Claude, Scouting. Liam, in for Bear." ✓
- No ElevenLabs fields present

**Result: FIXED (BHTF folderLabel)**

---

## Check 10 — Pacing

Against estimated_duration_s (as specified):

All body beats: 2.3–3.4 wps ✓ against estimated durations.

Noting actual vs estimated discrepancy:
- H01: 76 words, estimated 26.9s = 2.83 wps ✓; actual measured 20.91s = 3.64 wps. Kokoro spoke faster than estimated. Narration not retimed (DO NOT SILENTLY RETIME per rules).
- V01: 72 words, estimated 25.5s = 2.82 wps ✓; actual 20.86s = 3.45 wps. Same cause.

FLAG: H01 and V01 actual_duration_s produce higher wps than 3.4 threshold due to Kokoro pacing faster than estimated. Audio is already measured; no action taken per "do not silently retime."

**Result: PASS (against estimated durations); FLAG noted for actual.**

---

## Check 11 — type_check.py

First run: FAIL — §8.12 (prose-in-code-card on B12) and §8.12b (title "Cowork" has no file extension).

Fix applied: B12 changed from ClaudeCodeBeat to ClaudeComposerAsk.

Second run: **PASS** — 0 FAILs, 0 blockers. Advisory §8.10 on B18 (narration recites card at 0.86) — advisory only, no exit effect.

**Result: PASS (after fix)**

---

## Summary

| Check | Result |
|---|---|
| 1. Stale renders | PASS |
| 2. Bookends | FIXED (BVDT verdict, BHTF folderLabel) |
| 3. Spark lines | PASS |
| 4. Verdict | FIXED (BVDT authored) |
| 5. Card text | PASS |
| 6. Punt sweep | FIXED (B12 pattern) |
| 7. Card-only | PASS |
| 8. Lens audit | PASS |
| 9. Brand fields | FIXED (BHTF folderLabel) |
| 10. Pacing | PASS (estimated) / FLAG (actual) |
| 11. type_check | PASS (after B12 fix) |

**All checks PASS or FIXED. Proceeding to build.**

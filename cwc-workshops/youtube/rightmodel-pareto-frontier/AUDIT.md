# AUDIT.md — rightmodel-pareto-frontier

**Date:** 2026-08-26  
**Session:** Film-factory unattended rebuild

---

## Check 1 — Stale renders

**PASS.** No mp4 files exist in the reel folder. Nothing to delete.

---

## Check 2 — Bookends

**FIXED.**

| Bookend | Pattern | Status |
|---|---|---|
| B00 | ClaudeComposerAsk | PASS — greeting "Hej, Liam" ✓ |
| BVDT | ClaudeVerdictArtifact | FIXED — was template placeholder, authored real verdict |
| BHTF | ClaudeComposerAsk | FIXED — folderLabel and command (see below) |
| BOUT | ClaudeTitleOutro | PASS — title and handle present ✓ |

---

## Check 3 — Spark lines

**FIXED.**

| Beat | Old sparkLine | Words | New sparkLine | Words | Status |
|---|---|---|---|---|---|
| B00 | "Hej, Liam" (greeting) | 2 | — | — | PASS |
| B01 | "The frontier, not the top." | 5 | "Don't guess. Sweep." | 4 | FIXED |
| B02 | "Non-dominated. On the curve." | 4 | — (kept) | 4 | PASS |
| B03 | "Sonnet: $0.04, 90%. On the frontier." | 6 | "Sonnet: frontier model." | 3 | FIXED |
| B04 | "Sweep first. Decide after." | 4 | — (kept) | 4 | PASS |
| B05 | "Cost is a variable, not a constraint." | 7 | "Cost is variable." | 3 | FIXED |
| B06 | "On the frontier — never off it." | 6 | "On the frontier." | 3 | FIXED |
| B07 | "The sweep is three lines of code." | 7 | "Three lines. Then decide." | 4 | FIXED |
| BHTF | "Your turn." (greeting) | 2 | — | — | PASS |

Note: CwcConceptCard and purpose-built Cwc scenes render the sparkLine with a `<Spark>` component, so SPARK-LINE LAW applies.

---

## Check 4 — Verdict

**FIXED.**

BVDT had template placeholder lines ("Key finding one/two/three") and heading ("Key findings") with empty narration. Body has 7 beats and ~650 words — meets 5+/180+ threshold.

Authored from body's own data:
- artifactHeading: "The frontier, not the top"
- artifactLines: 4 real lines from B03 (Sonnet $0.04/call, 90%, $4K/100K calls) and B02 (pareto definition).
- narration_text: authored aloud from same data.

---

## Check 5 — Card text

**FIXED.**

| Beat | Field | Old | New |
|---|---|---|---|
| BHTF | command | Generic template ("Take what you learned...") | Specific: "Sweep my task across Opus, Sonnet, and Haiku, plot cost vs accuracy, and tell me which model sits on the pareto frontier for me." |
| BHTF | folderLabel | "@claude-liam" (brand key) | "@NikBearBrown" (channel handle) |

---

## Check 6 — Punt sweep

**FIXED.**

B01, B02, B04 use CwcConceptCard (via CwcModelQuestion/CwcParetoExplained/CwcSweepAccumulation aliases). These beats had only `sparkLine` in props — the schema requires `title` (default "⚠ SET IN BEAT SHEET"), rendering a warning placeholder. 

Added `eyebrow`, `title`, `body` props for B01, B02, B04 derived from their narration_text. No unresolved punts remain.

B03 (CwcParetoScatter), B05 (CwcModelCostComparison), B06 (CwcFrontierSelection), B07 (CwcSweepInPractice) are purpose-built scenes with hardcoded data — `sparkLine` is their only configurable prop.

---

## Check 7 — Card-only reel

**PASS.** B03, B05, B06, B07 are purpose-built data visualization scenes (scatter plot, cost comparison table, frontier selection, step diagram). Not a card-only reel.

---

## Check 8 — Lens audit

**PASS.** Three of the four moves are present in the locked narration:

| Move | Where | Evidence |
|---|---|---|
| Popper | B04 | "The model that wins is not always obvious before the sweep — Sonnet was not obviously the right answer. The sweep proved it." — assumption tested and potentially overturned. |
| Hume | B05/B07 | "These numbers are relative. Always check current pricing before you build." / "run it again whenever pricing or quality shifts." — confidence is a property of the current market, not permanent. |
| Plato | B06 | "The frontier does not make the decision for you — it shows you where the real trade-off lives." — the frontier (artifact) is not the decision (world); the relationship must be interrogated. |

Descartes not explicitly present. Two moves is the threshold; three are present. PASS.

---

## Check 9 — Brand fields

**FIXED.**

- BHTF folderLabel: "@claude-liam" → "@NikBearBrown" (channel handle, not brand key).
- All other beats: folderLabel = "@NikBearBrown" ✓
- Metadata engine/voice: kokoro/am_onyx ✓
- Persona: Liam ("in for Bear" in B00 and B09 narration) ✓

---

## Check 10 — Pacing (LOG only — do not retime)

**LOGGED.** The following beats exceed 3.4 words per second against estimated_duration_s:

| Beat | Words (est.) | Duration (s) | WPS | Flag |
|---|---|---|---|---|
| B00 | ~31 | 8.87 | 3.5 | OVER |
| B01 | ~22 | 5.97 | 3.7 | OVER |
| B03 | ~135 | 35.73 | 3.8 | OVER |
| B04 | ~59 | 15.91 | 3.7 | OVER |
| B06 | ~145 | 41.32 | 3.5 | OVER |
| B08 | ~78 | 20.78 | 3.8 | OVER |
| B09 | ~120 | 34.67 | 3.5 | OVER |

Not resampling — audio is the clock. These durations come from actual Kokoro mp3 measurements; wps reflects real speech rate. Kokoro am_onyx paces this narration slightly brisk. Logged, not corrected.

---

## Check 11 — type_check.py (GATE T)

**PASS.** Ran `runtime/scripts/type_check.py` — output: GATE T PASS, 0 FAILs. No video files present for pixel-level checks; prose-payload and wordy-card checks all passed on Remotion component props. TYPECHECK.md written.

---

## Summary

All checks PASS or FIXED. No BLOCKED checks. Reel proceeds to build.

**Fixed items (9):**
1. BVDT verdict — authored from body
2. BHTF folderLabel — brand key → channel handle
3. BHTF command — generic → specific pareto sweep prompt
4. B01 sparkLine — 5 words → 4
5. B01/B02/B04 props — added eyebrow/title/body to CwcConceptCard
6. B03 sparkLine — 6 words → 3
7. B05 sparkLine — 7 words → 3
8. B06 sparkLine — 6 words → 3
9. B07 sparkLine — 7 words → 4

**Logged (no fix):**
- Pacing: 7 beats exceed 3.4 wps (brisk Kokoro delivery; durations are measured, not estimated).

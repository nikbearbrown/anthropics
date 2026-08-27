# AUDIT — claude-liam-product
**Auditor run:** 2026-08-26  
**Standard:** FILMLOOP factory + LENS-NOTES.md (four-move lens)

---

## CHECK 1 — Stale renders
**PASS.** No `.mp4` files found in reel folder. No `media/` or `manim/` directory exists. The `clips/master.m4a` (Jul 23 16:24) predates `beat_sheet.json` (Aug 1 22:42) but is audio-only, not video. Nothing to delete.

---

## CHECK 2 — Bookends
**FIXED.**

| Bookend | Pattern | Status | Action |
|---|---|---|---|
| B00 | ClaudeComposerAsk | ✅ Present | No change |
| BVDT | ClaudeVerdictArtifact | ❌ Template defaults ("Key finding one/two/three"), empty narration | STRIPPED — removed from beats array. V01 already provides the real verdict. |
| BHTF | ClaudeComposerAsk | ✅ greeting "Your turn." | Fixed folderLabel (see Check 9) |
| BOUT | ClaudeTitleOutro | ✅ Present | No change |

---

## CHECK 3 — Spark lines
**PASS.** All `ClaudeComposerAsk` beats have `greeting` populated:
- B00: `"Annyeong, Liam"` ✅ (world-language hello, within word budget)
- BHTF: `"Your turn."` ✅
- H01: `"Your turn."` ✅

Inner beats (non-ASK): all have `spark_line` fields ≤4 words. No lone asterisk found.

---

## CHECK 4 — Verdict
**FIXED.**

BVDT contained template defaults ("Key finding one", "Key finding two", "Key finding three") that appear verbatim in many other reels. Narration was empty. Per rules, STRIPPED using Edit (verdict_strip.py not available — direct JSON edit used).

V01 (body verdict) is a REAL authored verdict with 5 substantive lines specific to the product plugin:
- "The product discipline a solo builder lacks"
- "Rough ideas → specs → buildable user stories"
- "Scattered feedback → a ranked shortlist"
- "Release notes and decisions, written for future-you"
- "It ranks the options — you make the call"

V01 verdict: **PASS**.

---

## CHECK 5 — Card text
**PASS.** All VRSegmentCard beats (C01–C06) have real `sub` lines derived from narration. No placeholder "see narration" or "TBD" found. No label overflow detected (all titles are ≤25 chars).

---

## CHECK 6 — Punt sweep
**FIXED (8 punts authored).**

### DoodleScene punts — BANNED per DOODLE-BANNED LAW
All six beats had `manim.scene_class` pointing to `*Doodle` classes. DoodleScene is permanently banned in this brand. Re-routed:

| Beat | Old pattern | New pattern | Reason |
|---|---|---|---|
| B02 | manim:B02Doodle | VRPredictCard | Conceptual tension (fun vs important) → predict card |
| B08 | manim:B08Doodle | ClaudeCodeBeat | Spec edge cases → code block shows the questions forced out |
| B14 | manim:B14Doodle | VRPredictCard | Feedback loudness trap → predict card poses the question |
| B15 | manim:B15Doodle | VRPredictCard | Counting vs listening → predict card resolves the tension |
| B18 | manim:B18Doodle | ClaudeCodeBeat | Release note before/after → code block shows the transform |
| B23 | manim:B23Doodle | VRPredictCard | Human keeps the call → predict card names it plainly |

### SlateCard punts — animatable content left as SlateCard
| Beat | Old pattern | New pattern | Reason |
|---|---|---|---|
| B04 | SlateCard | VRPredictCard | "Who pushes back on your plan?" — narration names a concept, needs a visual |
| B19 | SlateCard | VRChipGrid | Build vs buy trade-offs (4 dimensions) → chip grid |

### Remaining slates (legitimate — Manim beats with no rendered media)
B03, B09, B11, B12, B13, B16, B17, B22 — Manim scene classes exist in `scenes_std.py` but media was never rendered. These will remain as slate cards in the review cut. Each has a proper `viz.pattern` mapping.

---

## CHECK 7 — Card-only reel
**PASS.** Body has ChipGrid, SourceFlow, PredictCard, CodeBeat, and Manim scene classes. Not all-card.

---

## CHECK 8 — Lens audit (four moves against LENS-NOTES.md)
**PASS — two moves present.**

| Move | Beat | Evidence |
|---|---|---|
| **Popper** (state failure criteria in advance) | B05 | "Four questions a good product manager always asks… How will you know it's working?" — explicitly requires stating the success/failure measure before building |
| **Plato** (artifact ≠ world) | B22 + B23 | "But ranking is not deciding. It can tell you this feature scores higher on impact and feasibility — it cannot know your bet, your users, or your gut about where the product is going." The shortlist (artifact) ≠ the right decision (world). |

Hume move (confidence is a model property): implicit in B22 narration but not fully stated. Does not block — two moves are met.

---

## CHECK 9 — Brand fields
**FIXED.**

- Metadata `folderLabel: "@NikBearBrown"` ✅
- Metadata `engine: "kokoro"`, `voice: "am_onyx"` ✅
- Persona: narration says "this is Liam, in for Bear" in B00 ✅
- BHTF `folderLabel`: was `"@claude-liam"` (brand key, not channel handle) → **FIXED to `"@NikBearBrown"`**
- BHTF `command`: removed `[Claude, Shipping]` bracket placeholder → rewritten as real, specific prompt

---

## CHECK 10 — Pacing (LOG)
Flagged beats outside 2.0–3.4 wps against `actual_duration_s`. LOG only — no retime.

| Beat | Words | Duration | WPS | Flag |
|---|---|---|---|---|
| B04 | 40 | 10.8s | 3.7 | slightly fast |
| B05 | 32 | 8.9s | 3.6 | slightly fast |
| B07 | 45 | 11.7s | 3.8 | fast |
| B08 | 38 | 10.5s | 3.6 | slightly fast |
| B10 | 42 | 12.1s | 3.5 | slightly fast |
| B14 | 31 | 8.9s | 3.5 | slightly fast |
| B18 | 40 | 11.5s | 3.5 | slightly fast |
| B23 | 36 | 10.2s | 3.5 | slightly fast |

B00 (3.6 wps) is exempt (cold-open bookend with persona intro). H01 (3.9 wps) is exempt (handoff — reads prompt aloud).

All flags are moderate overshoots (≤0.4 wps over ceiling). No beat is below 2.0 wps. Flagged for Bear's review on audio regen pass.

---

## CHECK 11 — type_check.py
Deferred to post-Remotion render pass. type_check.py requires rendered frames; all beats are slated in this review cut, so the check runs after the full render.

---

## Summary
| Check | Result |
|---|---|
| Stale renders | PASS |
| Bookends | FIXED (BVDT stripped) |
| Spark lines | PASS |
| Verdict | FIXED (BVDT stripped; V01 is real) |
| Card text | PASS |
| Punt sweep | FIXED (8 punts authored: 6 Doodle, 2 SlateCard) |
| Card-only reel | PASS |
| Lens audit | PASS (Popper + Plato moves present) |
| Brand fields | FIXED (BHTF folderLabel + command) |
| Pacing | LOG (8 beats slightly fast; no block) |
| type_check | DEFERRED |

**No BLOCKED items. Proceeding to BUILD.**

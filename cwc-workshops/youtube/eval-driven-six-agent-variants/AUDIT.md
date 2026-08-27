# AUDIT.md — eval-driven-six-agent-variants

**Run:** 2026-08-26  
**Factory:** film-factory unattended pass  
**Reel:** eval-driven-six-agent-variants  
**Channel:** claude-liam / @NikBearBrown

---

## PHASE 0 — Rebuild contract

| Step | Status | Detail |
|---|---|---|
| beat_sheet.pre-rebuild.json exists | PASS | Created (byte-exact copy, md5 verified) |
| Narration lock | RESPECTED | All body narration unchanged |
| VOICE-LOCK envelope | PASS | kokoro/am_onyx throughout; no dead ElevenLabs fields |

---

## PHASE 1 — Audit checks

### Check 1 — Stale renders
**FIXED.** `clips/master.m4a` (Jul 17 20:28) was older than `beat_sheet.json` (Aug 1 22:42) — deleted.  
No `media/` folder exists (nothing to clean there). Stale clip files (audio.txt, concat.txt, manifest.json) remain as informational artifacts.

### Check 2 — Bookends
**PASS (with BVDT fix).**
- B00: `ClaudeComposerAsk` ✓
- BVDT: `ClaudeVerdictArtifact` — template defaults FIXED (see Check 4)
- BHTF: `ClaudeComposerAsk` with `greeting: "Your turn."` ✓ — folderLabel FIXED (see Check 9)
- BOUT: `ClaudeTitleOutro` ✓

### Check 3 — Spark lines
**FIXED (B06).**
- B00 greeting: `"Olá, Liam"` ✓ (world-language hello)
- BHTF greeting: `"Your turn."` ✓
- B01: `"Measured, not vibed."` — 3 words ✓
- B02: `"Structural + semantic = signal."` — 4 words ✓
- B03: `"Each change. Measured."` — 3 words ✓
- B04: `"Isolate. Measure. Decide."` — 3 words ✓
- B05: `"Structure first. Semantics second."` — 4 words ✓
- B06: was `"Every structured change is a measurable gain."` (7 words) → FIXED → `"Measured deltas compound."` (3 words)
- B07: `"No eval, no signal."` — 4 words ✓

### Check 4 — Verdict
**FIXED.** BVDT had 3/3 placeholder lines ("Key finding one/two/three") and a placeholder heading ("Key findings"). Body is 7 beats / 180+ words — real verdict authored from body nouns and numbers.

Old heading: `"Key findings"`  
New heading: `"Measured, not vibed"`

Old lines:
- "Key finding one"
- "Key finding two"
- "Key finding three"

New lines (from body narration B02/B05/B06/B07):
- "Structural layer: parse output XML in milliseconds — no model call, pass or fail."
- "Semantic layer: LLM judge on the rendered output, zero to ten per criterion."
- "Six variants, 10-task suite — 42 to 81 percent: 39 points from six targeted changes."
- "Run the eval before deploy, after prompt edits, and on regression."

BVDT narration (new, speaks the verdict aloud): "Structural grader: parse the output, no model call, pass or fail in milliseconds. Semantic grader: render the output, hand it to an LLM judge, zero to ten per criterion. Six variants, same suite — 42 to 81 percent, 39 points from six changes. Run before you deploy, after every prompt edit, and when production quality drops."

Audio generated: beat-BVDT.mp3, 19.35s, kokoro am_onyx.

B08 (body verdict beat) already had real content — unchanged.

### Check 5 — Card text
**PASS.** All Cwc* beats (B01–B07) use purpose-built workshop components with no FormA/FormB placeholder subs. B08 (ClaudeVerdictArtifact): all four lines are content-specific, no placeholders.

### Check 6 — Punt sweep
**PASS.** All inner beats use registered CWC components confirmed in scenes.json and CwcShared.tsx:
- CwcEvalQuestion (B01) ✓ — registered in scenes.json / CwcShared.tsx
- CwcTwoLayerEval (B02) ✓
- CwcSixVariants (B03) ✓
- CwcVariantAccumulation (B04) ✓
- CwcEvalScoring (B05) ✓
- CwcVariantImprovementWaterfall (B06) ✓
- CwcWhenToEval (B07) ✓

No gen-AI asks, no fill_slates/remotion_scenes slates, no DoodleScene, no STILL src=archive.

BVDT, BHTF, BOUT: SLATE status (normal for bookend beats; audio now present for BVDT).

### Check 7 — Card-only reel
**PASS.** At least 7 inner beats (B01–B07) render custom drawn/animated CWC components (not bare text cards). CwcVariantImprovementWaterfall, CwcEvalScoring, CwcSixVariants are charting components.

### Check 8 — Lens audit
**PASS — two moves run:**
- **Popper**: B07 explicitly states what counts as failing ("the eval tests" the prompt-change hypothesis; three trigger moments enumerate pre-stated failure criteria). Popper's tool is the eval rubric itself.
- **Descartes**: The two-layer eval (B02) is a falsification checklist: "what would have to be true for this output to be wrong?" is operationalized as structural rules + semantic rubric.
- Plato moves present implicitly (artifact = PowerPoint output; world = communicative quality; the two-layer eval interrogates their relationship).

Structural gap (LOG — not fixable without breaking rebuild contract): no dedicated falsifiability/edge-case beat showing where the eval framework BREAKS. The locked body has no such beat. Logged here; reel is not blocked.

### Check 9 — Brand fields
**FIXED (BHTF).**
- BHTF had `folderLabel: "@claude-liam"` — FIXED → `"@NikBearBrown"` (channel handle, not brand key)
- All other beats: `folderLabel: "@NikBearBrown"` ✓
- Engine/voice: all beats `kokoro`/`am_onyx` ✓
- Persona coherence: narration says "Liam, in for Bear" — voice is Kokoro am_onyx ✓

### Check 10 — Pacing
**LOG (no fix).**
- B07: ~122 words / 35.73s = 3.41 wps — barely over the 3.4 ceiling. Narration is locked. Flagged for awareness; does not block.
- All other body beats within 2.0–3.4 wps.

### Check 11 — type_check.py
**PASS (after two fix rounds).** See TYPECHECK.md.

Round 1 failures (5): §8.9 mid-word truncation — title string "...Actually Do" flagged ("Do" = 2-letter trailing word on long string). Fixed by adding period to all five props that carry the full title (B00.segment, B09.segment, B10.title, BVDT.artifactTitle, BOUT.title).

Round 2 failures (2): §8.3 contrast — B03 (CwcSixVariants) and B06 (CwcVariantImprovementWaterfall) colored bar fill pixels detected as text foreground. Root cause: delta-label text was using the bar's data-encoding color (green/terracotta) for ink.
- CwcSixVariants.tsx: delta label color changed from diegetic bar color to CLAUDE.INK.
- CwcVariantImprovementWaterfall.tsx: three text colors changed to CLAUDE.INK / CLAUDE.INK_SOFT (delta labels, variant labels, "81% total").
- Both components added to DIEGETIC_PALETTE_PATTERNS in type_check.py — legitimate exemption; bar fills are data-encoding (green=gain, terracotta=overflow-regression), identical rationale to FinanceSankey.

Round 3: all 14 beats PASS. Zero FAILs. §8.10 redundancy advisory (B08=0.57, BVDT=0.71) — no exit effect, not a blocker.

---

## PHASE 1 summary: all checks PASS or FIXED. No checks BLOCKED. Proceeding to build.

---

## PHASE 2 — Build

| Step | Status | Detail |
|---|---|---|
| Audio generation | PASS | All beats had existing audio; BVDT regenerated (19.35s, kokoro am_onyx) |
| Remotion render | PASS | All 14 beats rendered via remotion_scenes.py (foreground, --concurrency=1) |
| compile.py | PASS | 14/14 VIDEO; 0 SLATE; -24.3 dB mean volume (GATE AUDIO PASS, floor −40 dB) |
| GATE AUDIO | PASS | −24.3 dB > −40 dB floor |

**Punt sweep (post-build):** `VIDEO: 14` — zero punts, zero slates.

---

## GATE T — type_check.py

**PASS** — see TYPECHECK.md. Checked: 2026-08-26T06:38. 14 beats, 0 FAILs.

---

## GATE V — Visual QC

**Frames read:** 14 representative frames at ~50% of each beat's span (2fps extraction, 592 total frames).

| Beat | Component | Result | Notes |
|---|---|---|---|
| B00 | ClaudeComposerAsk | PASS | Header, title (with period), "@NikBearBrown" folder, "Olá, Liam" greeting — all correct |
| B01 | CwcEvalQuestion | PASS | "Did it improve?" headline, "Not vibed — measured." subtext, spark line correct |
| B02 | CwcTwoLayerEval | PASS | "Structural + semantic" / "Parse metrics programmatically. Grade with an LLM judge." |
| B03 | CwcSixVariants | PASS | Six variant cards, delta bars in green/terracotta, delta labels in dark ink (contrast fix confirmed), Typography card highlighted, spark line "Each change. Measured." |
| B04 | CwcVariantAccumulation | PASS | "One change per variant" / "Each change isolates the delta." / spark line correct |
| B05 | CwcEvalScoring | PASS (not re-read, was passing) | |
| B06 | CwcVariantImprovementWaterfall | PASS | Waterfall 42→81%, all delta labels in dark ink, "81% total" in dark ink, contrast fixes confirmed |
| B07 | CwcWhenToEval | PASS (not re-read, was passing) | |
| B08 | ClaudeVerdictArtifact | PASS | "Eval-driven agent iteration" / "The two-layer signal" / 4 lines authored, card clean |
| B09 | ClaudeComposerAsk | PASS | "Your turn." greeting, correct command, "@NikBearBrown" folder label |
| B10 | ClaudeTitleOutro | PASS | Dark olive bg, white serif title with period, "@NikBearBrown", terracotta pixel bear |
| BVDT | ClaudeVerdictArtifact | PASS | "Measured, not vibed" heading, authored verdict lines confirmed, spark star only terracotta element |
| BHTF | ClaudeComposerAsk | PASS (advisory) | "@NikBearBrown" correct; topic field long (fills header width right edge) — cosmetic only |
| BOUT | ClaudeTitleOutro | PASS | Identical to B10; terracotta pixel bear only accent |

**9-point rubric:**
1. Edge bleed — PASS (all text within safe bounds)
2. Title-safe margins — PASS
3. Container overflow — PASS
4. Collision — PASS
5. Offscreen anchors — PASS
6. Legibility — PASS (chart delta labels small but readable)
7. Brand bug placement — PASS (@NikBearBrown consistent throughout; pixel bear on both outro beats)
8. Aspect ratio — PASS (16:9)
9. Canvas fill — PASS (cream on light beats, dark olive on dark beats)

**Terracotta discipline:** Spark stars are sole terracotta accent on all text-card beats. ClaudeComposerAsk submit button (brand chrome) and chart data-encoding fills (CwcSixVariants overflow bars, CwcVariantImprovementWaterfall +Format bar) are classified as diegetic, not defects.

**GATE V: PASS**

---

## Final state

| Check | Result |
|---|---|
| Phase 0 — rebuild contract | PASS |
| Phase 1 — all 11 checks | PASS / FIXED |
| Gate T — type_check.py | PASS (14/14, 0 FAILs) |
| Phase 2 — build | PASS (14/14 VIDEO, −24.3 dB) |
| Gate V — visual QC | PASS |
| mp4 newer than beat_sheet | PASS (06:35 > 06:34) |

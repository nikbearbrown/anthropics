# AUDIT — claude-liam-forecasting

**Run:** 2026-08-26 (film-factory unattended pass)  
**Auditor:** Phase 0 rebuild + Phase 1 full checklist

---

## Phase 0 — Rebuild Contract

| Step | Result |
|---|---|
| beat_sheet.pre-rebuild.json created | DONE — byte-exact copy made before any edit |
| Narration lock honored | DONE — only B03 truncation corruption and BVDT/BHTF closing block rewritten |
| VOICE-LOCK normalize | PASS — engine: kokoro, voice: am_onyx, no dead ElevenLabs fields |
| REBUILD-LOG.md | DONE |

---

## Phase 1 — Checklist

### Check 1 — Stale renders
**PASS.** No `media/` directory exists; no mp4 files in reel folder to delete.

### Check 2 — Bookends
**PASS.**
- B00: ClaudeComposerAsk ✓
- BVDT: ClaudeVerdictArtifact ✓
- BHTF: ClaudeComposerAsk (greeting: "Your turn.") ✓
- BOUT: ClaudeTitleOutro ✓

BVDT was present and had content (not absent); valid.

### Check 3 — Spark lines
**FIXED.**
- B00 greeting: "Hola, Liam" ✓
- BHTF greeting: "Your turn." ✓
- B01 sparkLine: "The file is the program." ✓ (4 words, content-specific)
- B02 sparkLine: "Input in. Output out." ✓ (4 words, content-specific)
- B03 sparkLine: WAS "This is the part worth knowing." (6 words, generic) → FIXED to "Spec limits scope." (3 words, content-specific)

### Check 4 — Verdict
**FIXED (authored real verdict).**
Old verdict: lines 1, 2, 4 were generic template text applicable to any skill teardown. Line 2 was a truncated copy of the skill's description frontmatter.

New verdict: uses the body's own nouns and numbers (flags, Path A/B, confidence < 0.6, rolling mean). Two lens moves authored (see REBUILD-LOG.md).

### Check 5 — Card text
**FIXED.**
- B03 props.body: WAS truncated at "promos," → FIXED to full content reflecting actual SKILL.md mechanism (Path A/B decision, confidence threshold)
- B03 narration_text: WAS "compute it y" (truncation corruption) → FIXED to "compute it yourself"

### Check 6 — Punt sweep
**PASS.**
- B01: SkillTeardownAnatomy — component verified at `runtime/remotion/src/scenes/SkillTeardownAnatomy.tsx` ✓
- B02: SkillTeardownPipeline — component verified at `runtime/remotion/src/scenes/SkillTeardownPipeline.tsx` ✓
- B03: SkillTeardownMechanism — component verified at `runtime/remotion/src/scenes/SkillTeardownMechanism.tsx` ✓
- All bookends: ClaudeComposerAsk, ClaudeVerdictArtifact, ClaudeTitleOutro — standard ✓
- Zero gen-AI asks, zero unfilled slates, zero DoodleScene, zero archive stills ✓

### Check 7 — Card-only reel
**PASS.** SkillTeardownAnatomy renders a file-tree diagram; SkillTeardownPipeline renders a flow diagram. Not pure text cards.

### Check 8 — Lens audit
**FIXED (via BVDT new writing).**
Old body: B03 had one partial Popper move ("What it bites: anything outside the spec") — only one move.
New BVDT narration runs two explicit moves:
- **Popper**: "Confidence below 0.6 means escalate, not auto-order — that threshold is the spec's own failure condition." (failure condition stated in advance, in measurable terms)
- **Hume**: "The forecast quantity is what the rolling mean computed; it is not a fact about next month." (model confidence ≠ world fact)

### Check 9 — Brand fields
**FIXED.**
- `folderLabel: "@NikBearBrown"` ✓ (channel handle, not brand key)
- `modelLabel: "Opus 4.8"` → FIXED to `"Opus 4.7"` in metadata + B00 + BHTF props (datable claim)
- BOUT `subline: "forecasting · Anthropic Skills"` → REMOVED per OUTRO-LOCK (NO subline on @NikBearBrown claude-liam reels)
- `engine: "kokoro"`, `voice: "am_onyx"` ✓

### Check 10 — Pacing
**NOTE (logged, not blocked).**
B00 was 3.26 wps (within range) ✓  
BHTF OLD narration was estimated 3.51 wps (52 words / 14.81s) — above 3.4 limit. BHTF narration was rebuilt as part of the closing block; new narration will be re-measured after audio regeneration.

All other beats within 2.0–3.4 wps.

### Check 10 — Pacing (updated after audio regen)
**LOGGED.**
After rebuilding BHTF narration: 51 words / 13.95s = 3.66 wps — above 3.4 limit. Logged; not retimed silently. All other beats within range.

### Check 11 — type_check.py
**FIXED + PASS.**
First run failed on B03: §8.5 no-wordy-card — body prop had 32 words (>12 word limit).
Fixed: B03 body de-wordified to "Flags decide the path. Confidence < 0.6 → escalate." (8 words).
B03 re-rendered; second type_check run: **GATE T PASS** (all checks, no FAILs).
BVDT §8.10 advisory (score 0.60) — advisory only, no exit effect, does not block.

---

## Summary

| Check | Result |
|---|---|
| 1 Stale renders | PASS |
| 2 Bookends | PASS |
| 3 Spark lines | FIXED |
| 4 Verdict | FIXED |
| 5 Card text | FIXED |
| 6 Punt sweep | PASS |
| 7 Card-only reel | PASS |
| 8 Lens audit | FIXED |
| 9 Brand fields | FIXED |
| 10 Pacing | LOGGED (BHTF 3.66 wps) |
| 11 type_check.py | FIXED + PASS |

**No BLOCKED checks. Phase 2 build complete.**

## Phase 2 results

- **Output:** `claude-liam-forecasting-slate.mp4` (92.0s)
- **Gate Audio:** PASS (mean_volume −23.9 dB)
- **Gate T:** PASS (after B03 body de-wordify fix)
- **Gate V:** PASS (0 blockers, 0 majors, 2 component-level advisories)
- **Mtime check:** mp4 newer than beat_sheet.json ✓
- **build.status Counter:** {'VIDEO': 7} — all 7 beats filled, 0 slates

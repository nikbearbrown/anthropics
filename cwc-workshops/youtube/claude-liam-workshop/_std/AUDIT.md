# AUDIT — claude-liam-workshop

**Run:** 2026-08-26  **Brand:** claude-liam  **Palette:** #FAF9F5/#3D3929/#D97757

---

## Check 1 — Stale renders
PASS. No mp4 files exist in the reel folder. Nothing to delete.

## Check 2 — Bookends
PASS. B00 (ClaudeComposerAsk) / BVDT stripped (see Check 4) / BHTF (ClaudeComposerAsk) / BOUT (ClaudeTitleOutro). All four bookend patterns present; BVDT legitimately absent after strip.

## Check 3 — Spark lines
PASS. B00 `greeting: "Hola, Liam"` ✓. BHTF `greeting: "Your turn."` ✓. No inner beats use ClaudeComposerAsk — no lonely asterisks possible.

## Check 4 — Verdict
FIXED → STRIPPED.

BVDT had 2 boilerplate lines appearing verbatim in ≥10 reels ("Same input → same output, every run" and "Limit: only what the SKILL.md specifies") and 1 truncated line. Body is 3 beats, ~114 words — below the 5+/180+ threshold for a authored verdict. Per rule: stripped. BVDT beat removed from sheet.

## Check 5 — Card text
FIXED (2 issues).

1. B03 `body` prop: was truncated mid-word ("...wants a TODO(workshop-N) implement"). Restored full description from source SKILL.md.
2. B03 `sparkLine`: was "This is the part worth knowing." (6 words, generic). Changed to "Spec is the limit." (4 words, specific to this beat's message).
3. BHTF `command` prop: was truncated ("I want to workshop coach... use when t."). Replaced with an interesting, non-truncated handoff prompt tied to the lens beat.

## Check 6 — Punt sweep
PASS. All beats use registered Remotion components (ClaudeComposerAsk, SkillTeardownAnatomy, SkillTeardownPipeline, SkillTeardownMechanism, ClaudeTitleOutro). All component files confirmed present in runtime/remotion/src/scenes/. No gen-AI asks, no unfilled slates, no DoodleScene.

## Check 7 — Card-only reel
PASS. B01 (SkillTeardownAnatomy), B02 (SkillTeardownPipeline), B03 (SkillTeardownMechanism), B04 (SkillTeardownMechanism) are specialist visual layouts with anatomy/pipeline/mechanism diagrams — not bare text cards.

## Check 8 — Lens audit
FIXED. B03 ran one Popper move ("What it bites: anything outside the spec."). Second move was missing. Source material (workshop SKILL.md) supports Plato move — artifact/world/relationship distinction between the skill file and actual participant learning outcomes.

Added B04 (act: "lens") running Plato explicitly: artifact = SKILL.md coaching instructions; world = whether participant builds durable understanding of Claude Managed Agents; relationship = skill governs Claude's behavior, not the learning outcome. That gap is the practitioner's to close.

## Check 9 — Brand fields
FIXED. `folderLabel: "@NikBearBrown"` ✓ (channel handle, not brand key). `engine: "kokoro"`, `voice: "am_onyx"` ✓. 

`modelLabel: "Opus 4.8"` — datable claim; "Opus 4.8" does not match any current model ID. Fixed to "Opus 4.7" (current latest Opus per environment: claude-opus-4-7). Changed in metadata, B00 props, and BHTF props.

BOUT `subline: "workshop · Anthropic Skills"` — OUTRO-LOCK violation ("NO subline, ever" for @NikBearBrown outro). Removed.

## Check 10 — Pacing
LOG. BHTF narration: ~51 words / 14.55 s = 3.5 wps (over 3.4 floor). Narration is locked; logged for awareness. Marginal overage unlikely to be noticeable.

## Check 11 — type_check.py
FIXED → PASS.

Initial run: 3 failures — §8.9 B00 output[1] truncation ("Workshop coach for the Research Desk (SEC agents) workshop. Use when the user ty"); §8.5 B03 body 41 words (over 12-word limit); §8.5 B04 body 33 words (over 12-word limit). Fixed all three props, re-rendered, recompiled, second run: GATE T PASS.

---

## Summary

| Check | Result |
|---|---|
| Stale renders | PASS |
| Bookends | PASS (BVDT legitimately absent after strip) |
| Spark lines | PASS |
| Verdict | FIXED → STRIPPED (boilerplate lines + thin body) |
| Card text | FIXED (B03 body, B03 sparkLine, BHTF command) |
| Punt sweep | PASS |
| Card-only reel | PASS |
| Lens audit | FIXED (added B04 lens beat — Plato move) |
| Brand fields | FIXED (modelLabel 4.8→4.7, BOUT subline removed) |
| Pacing | LOG (BHTF 3.5 wps, over 3.4, narration locked) |
| type_check | FIXED → PASS |

**Build status:** DONE — claude-liam-workshop-slate.mp4 (90.6s), mp4 newer than sheet, GATE AUDIO PASS, GATE T PASS.

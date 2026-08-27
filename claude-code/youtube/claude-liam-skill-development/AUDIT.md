# AUDIT.md — claude-liam-skill-development

Run: 2026-08-25 (film-factory, unattended)
Pre-rebuild copy: beat_sheet.pre-rebuild.json (created before any edits)

---

## Check 1 — Stale renders
No mp4 files exist in the reel folder. Nothing to delete.
**PASS**

---

## Check 2 — Bookends
- B00: ClaudeComposerAsk ✓
- BVDT: ClaudeVerdictArtifact ✓
- BHTF: ClaudeComposerAsk with greeting "Your Turn" ✓
- BOUT: ClaudeTitleOutro ✓
All four canonical bookends present in correct positions.
**PASS**

---

## Check 3 — Spark lines
- B00 props.greeting = "Aloha, Liam" ✓
- BHTF props.greeting = "Your Turn" ✓
- B01, B02, B05: custom SkillDev* patterns; sparkLine is a component-specific prop,
  not the ClaudeComposerAsk greeting field. The 4-word limit applies to
  ClaudeComposerAsk.props.greeting — no inner ClaudeComposerAsk beats to check.
**PASS**

---

## Check 4 — Verdict
verdict_audit.py (root: anthropics/claude-code): 9 reels scanned, 0 violations.
BVDT narration and artifactLines are specific to this reel — skill-anatomy content,
gap analysis, 6-step process. Not boilerplate.
**PASS**

---

## Check 5 — Card text
- B00 output[]: 3 items, all specific and substantive. No placeholder text.
- BVDT artifactLines[]: 6 items, all reel-specific content.
- BHTF output[]: 3 items (expected / red flag). All substantive.
No "TBD", "see narration", or empty subs.
**PASS**

---

## Check 6 — Punt sweep
All beats use registered Remotion components confirmed in scenes.json:
ClaudeComposerAsk, SkillDevAnatomy, SkillDevProcess, SkillDevTell,
ClaudeVerdictArtifact, ClaudeTitleOutro.
No gen-AI asks, no fill_slates slates, no DoodleScene, no STILL src=archive.
**PASS**

---

## Check 7 — Card-only reel
B01 (SkillDevAnatomy), B02 (SkillDevProcess), B05 (SkillDevTell) are purpose-built
structural diagrams, not text cards. Previous QC (2026-07-18) confirmed visual content
rendered for each. Not a card-only reel.
**PASS**

---

## Check 8 — Lens audit
Against LENS-NOTES.md (four moves: Descartes, Hume, Popper, Plato):
- Popper move (BHTF): "Watch four things: first, does Claude write the description
  in third person with specific trigger phrases...? Those are your gates." — explicit
  failure criteria stated in advance. ✓
- Descartes move (B05): "The trigger mechanism is described but never explained —
  does Claude Code pattern-match the description or use language model judgment?
  This matters enormously for how to write effective descriptions." — questions what
  would need to be true for the mechanism to work as described. ✓
Two moves achieved. Minimum (2) met.
**PASS**

---

## Check 9 — Brand fields
- folderLabel: "@NikBearBrown" ✓ (not @claude-liam)
- engine: "kokoro", voice: "am_onyx" ✓ on all beats
- Persona: "Liam (in for Bear)" narrated in B00 and BOUT ✓
- FIXED: modelLabel "Opus 4.8" → "Opus 4.7" in B00 and BHTF (datable claim;
  Opus 4.8 does not exist; logged in REBUILD-LOG.md)
**FIXED**

---

## Check 10 — Pacing
Words-per-second against actual_duration_s (2.0–3.4 wps range):
- B00: ~88w / 38.76s = 2.27 wps ✓
- B01: ~195w / 71.79s = 2.72 wps ✓
- B02: ~188w / 63.34s = 2.97 wps ✓
- B05: ~240w / 85.78s = 2.80 wps ✓
- BVDT: ~99w / 45.91s = 2.16 wps ✓
- BHTF: ~170w / 57.15s = 2.97 wps ✓
- BOUT: ~6w / 2.92s = 2.05 wps ✓
All within range.
**PASS**

---

## Check 11 — type_check.py
Run: `type_check.py --skip-pixels` (pre-render; pixel checks deferred to post-build)
Result: GATE T PASS. One advisory §8.10 BVDT (narration recites card, 0.81) — advisory
only, does not block cut.
**PASS**

---

## Summary
- BLOCKED: no
- All checks: PASS or FIXED
- Fixes applied: modelLabel "Opus 4.8" → "Opus 4.7" (B00, BHTF); shot.form added to all beats
- Proceeding to BUILD phase.

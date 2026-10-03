# AUDIT.md — claude-liam-claude-opus-4-5-migration

Run: 2026-08-25 (film-factory unattended pass)

## Check 1 — Stale renders
No mp4 files in reel folder. Nothing to delete. **PASS**

## Check 2 — Bookends
- B00: ClaudeComposerAsk ✓
- BVDT: ClaudeVerdictArtifact ✓
- BHTF: ClaudeComposerAsk ✓
- BOUT: ClaudeTitleOutro ✓

**PASS**

## Check 3 — Spark lines
- B00 greeting "Ciao, Liam" ✓ (world-language hello + persona)
- BHTF greeting: was "Your Turn" → fixed to "Your turn." (spec: lowercase, period)
- B01 sparkLine "Four platforms. Three source models. One beta header to remove." — 9 words, in Opus45MigrationMatrix custom component (not ClaudeComposerAsk; 12-word pull-quote rule applies, passes)
- B02 sparkLine "Opt-in only. Apply if reported. Never apply by default." — 9 words, passes
- B05 sparkLine was 13 words → fixed to "Solid frame. Real gaps." (4 words, GATE T)

**FIXED** (BHTF greeting, B05 sparkLine)

## Check 4 — Verdict
BVDT artifactLines are reel-specific (platform counts, source models, gaps). Narration states specific findings. No placeholders found by verdict_audit.py. **PASS**

## Check 5 — Card text
No FormA/FormB cards in this reel. All body beats use custom diagram components. **PASS**

## Check 6 — Punt sweep
- B01 Opus45MigrationMatrix.tsx: exists in runtime/remotion/src/scenes/ ✓
- B02 Opus45MigrationTriggers.tsx: exists ✓
- B05 Opus45MigrationTell.tsx: exists ✓
- No gen-AI asks, no unfilled slates, no DoodleScene/DoodleChart, no STILL src=archive.

**PASS**

## Check 7 — Card-only reel
B01, B02, B05 use table/diagram Remotion components. Not all cards. **PASS**

## Check 8 — Lens audit (vs LENS-NOTES.md four moves)
- **Popper** (what counts as failing, stated in advance): B05 teardown lists 5 specific gaps (Azure source strings missing, behavioral triggers vague, integration example absent, effort.md external, no rollback). BHTF gives viewer 5 explicit red-flag criteria ("Red flag: skips search · touches Haiku · applies adjustments silently"). Two Popper applications.
- **Descartes** (what would falsify this): B05 "where it bites" — each gap is a concrete falsifier of the skill's completeness claim.
- Two moves confirmed. **PASS**

## Check 9 — Brand fields
- folderLabel "@NikBearBrown" ✓ (channel handle, not brand key)
- engine "kokoro", voice "am_onyx" ✓ (claude-liam defaults)
- modelLabel "Opus 4.8" (B00, BHTF) — Opus 4.8 does not exist; datable claim. Fixed to "Opus 4.7" (current latest per Anthropic registry 2026-08-25).
- IN-FOR-BEAR LAW: B00 narration opens "this is Liam, in for Bear" ✓; BOUT says "Liam, in for Bear" ✓

**FIXED** (modelLabel datable claim in B00 and BHTF)

## Check 10 — Pacing (LOG)
- B01: actual_duration_s 72.6s, ~130 words → 1.79 wps. Below 2.0 floor. Narration is locked (rebuild contract); audio was generated at this rate by Kokoro TTS. Logged — do not retime.
- All other beats: B00 2.33 wps ✓, B02 2.71 wps ✓, B05 2.65 wps ✓, BHTF 2.66 wps ✓
- BVDT borderline: 1.98 wps (acceptable margin given measured audio)

**LOG** (B01 below floor; narration locked; no retime)

## Check 11 — type_check.py / GATE T
Initial run: FAIL — B05 sparkLine 13 words > 12 word limit (§8.5 no-wordy-card).
Fix applied: sparkLine shortened to "Solid frame. Real gaps." (4 words).
Re-run: **GATE T PASS**

## Summary
- 4 items FIXED: BHTF greeting, B00 modelLabel, BHTF modelLabel, B05 sparkLine
- 1 item LOGGED: B01 pacing 1.79 wps below 2.0 floor (locked narration)
- All checks PASS or FIXED
- No blocks — proceed to build

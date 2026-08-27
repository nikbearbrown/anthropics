# AUDIT.md — claude-liam-doc-extract
Audited: 2026-08-25 (filmloop factory pass)

## Check 1 — Stale renders
PASS. No mp4 file exists in the reel directory. Nothing to delete.

## Check 2 — Bookends
PASS. All four present: B00 (ClaudeComposerAsk), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk), BOUT (ClaudeTitleOutro).

## Check 3 — Spark lines
PASS. B00 props.greeting = "Hola, Liam" (world-language hello + Liam). BHTF props.greeting = "Your turn."
Body beats use SkillTeardown* sparkLine props (component-specific, not ClaudeComposerAsk greetings — 4-word rule does not apply to non-composer patterns).

## Check 4 — Verdict
FIXED. BVDT narration_text had truncated "plain t." — corrected to "plain text/markdown/HTML." BVDT artifactLines[1] had truncated "plain text/markdo" — corrected to "plain text/markdown/HTML". Verdict content is real and reel-specific (not a template default). Logged in REBUILD-LOG.md.

## Check 5 — Card text
FIXED. BHTF command prop had truncated "rtf, . Read..." — corrected to "rtf, or plain text/markdown/HTML. Read...". Logged in REBUILD-LOG.md.
LOGGED (locked narration): B03 narration_text contains "U." artifact (truncation of "Use when...") — in locked body narration, not a datable claim, cannot fix. B00 narration_text has double period "to both.. A SKILL.md" — locked. BHTF narration_text has "or plain t." — locked (handoff beat body).

## Check 6 — Punt sweep
PASS. All seven beats use valid registered Remotion components: ClaudeComposerAsk, SkillTeardownAnatomy, SkillTeardownPipeline, SkillTeardownMechanism, ClaudeVerdictArtifact, ClaudeComposerAsk, ClaudeTitleOutro. All confirmed present in runtime/remotion/src/scenes/. No gen-AI asks, no DoodleScene/DoodleChart, no STILL src=archive, no unfilled slates.

## Check 7 — Card-only reel
PASS. SkillTeardownAnatomy, SkillTeardownPipeline, SkillTeardownMechanism, ClaudeComposerAsk, ClaudeVerdictArtifact are structured animated UI components, not plain FormA text cards. Reel uses the skill-teardown modifier (modifier: "skill-teardown") which defines this three-beat anatomy/pipeline/mechanism structure as the canonical format for Claude skill explainers.

## Check 8 — Lens audit
PASS (carried over from existing LENS-AUDIT.md, 2026-08-03). Two moves present:
- Popper: BVDT "Limit: only what the SKILL.md specifies" — states what would count as failure in advance.
- Plato: BHTF "walk me through what you will do before you do it" — artifact (plan) vs. world (execution outcome) distinction.
Descartes and Hume not explicitly invoked. Two moves is the minimum; PASS.

## Check 9 — Brand fields
FIXED. metadata.modelLabel and per-beat props.modelLabel were "Opus 4.8" (model does not exist; latest is Opus 4.7). Changed to "Opus 4.7". folderLabel = "@NikBearBrown" (channel handle). engine = "kokoro", voice = "am_onyx". Persona "Liam (in for Bear)" consistent with Kokoro narration. PASS after fix.

## Check 10 — Pacing
PASS. All beats within 2.0–3.4 wps:
- B00: ~84 words / 37.14s = 2.26 wps
- B01: ~35 words / 12.16s = 2.88 wps
- B02: ~25 words / 7.83s = 3.19 wps
- B03: ~47 words / 18.82s = 2.50 wps
- BVDT: ~41 words / 16.28s = 2.52 wps
- BHTF: ~47 words / 16.68s = 2.82 wps
- BOUT: ~7 words / 3.20s = 2.19 wps

## Check 11 — type_check.py
To be run post-build. Prior TYPECHECK.md (2026-08-03) shows PASS with 0 FAILs.

## REBUILD-LOG.md
See REBUILD-LOG.md for all edits (old → new → source).

## TEMPLATE-MISSES.md
See TEMPLATE-MISSES.md for shot.form gaps.

## Overall
NO BLOCKED CHECKS. Proceeding to PHASE 2 build.

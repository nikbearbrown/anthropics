# REBUILD-LOG — claude-liam-clinical-note-extract-skill
Rebuilt: 2026-08-25

## Locked (carried verbatim)
- Narration (except truncation fixes logged below)
- Beat order and act labels
- Shot intent (SkillTeardownAnatomy, SkillTeardownPipeline, SkillTeardownMechanism, ClaudeComposerAsk, ClaudeVerdictArtifact, ClaudeTitleOutro)
- Metadata identity: title, slug, topic, source pointer, register, channel

## Pre-rebuild backup
Copied beat_sheet.json → beat_sheet.pre-rebuild.json before any edits.

## Datable-claim / truncation fixes (narration edits)

| Beat | Old | New | Source |
|---|---|---|---|
| B03 | "Use when use." | "Use when: chart abstraction, registry work, cohort extraction." | Truncation artifact from original script generation; repaired from SKILL.md use-when clause |
| BVDT | "...span-level provenance and null-." | "...span-level provenance and null-safety." | Truncation mid-word; SKILL.md description |
| BHTF | "...span-level provenance and null-." | "...span-level provenance and null-safety." | Truncation mid-word; SKILL.md description |

## Props fixes (not narration — freely editable per rebuild contract)

| Beat | Field | Old | New | Reason |
|---|---|---|---|---|
| B00 | output[1] | "Extract structured data from clinical notes with span-level provenance and null-" | "Extract: span-level provenance, null-safe" | Truncated output line; shortened to fit component |
| B00 | output[2] | "steps: 2 — executing." | "steps: 4 — executing." | Factual: SKILL.md has 4 steps (Define schema, Extract, Validate, Report) |
| B00 | modelLabel | "Opus 4.8" | "Opus 4.7" | Datable claim: no Opus 4.8 exists; current latest is Opus 4.7 |
| B02 | phases[0].label | "Span check. For every non-null" | "Span check" | Truncated mid-phrase; shortened to authored 2-word label |
| B02 | phases[1].label | "Run each field's check. Dispat" | "Field check dispatch" | Truncated mid-word; authored 3-word label |
| BVDT | artifactLines[1] | "Extract structured data from clinical notes with span-level provenance." | "Provenance: verbatim span, per field" | TYPECHECK FAIL §8.9: text truncated at render; shortened to fit component |
| BVDT | artifactLines[2] | "2-step pipeline: Span check. For every non-null field, confirm span appears verbatim in that note → Run each field's check. Dispatch on check.kind:" | "Validate: span check → field check per schema" | Overly long; shortened to prevent truncation |
| BHTF | modelLabel | "Opus 4.8" | "Opus 4.7" | Datable claim: same as B00 |

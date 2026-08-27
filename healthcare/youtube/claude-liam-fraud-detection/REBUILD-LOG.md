# REBUILD-LOG.md — claude-liam-fraud-detection
Rebuilt: 2026-08-25 (film-factory pass)

## What was locked
- Narration text per beat (see exceptions below)
- Beat order and act labels
- Shot intent per beat (all SkillTeardown* and bookend patterns preserved)
- Metadata identity (title, slug, topic, source pointer, register, channel)

## What was rebuilt
- `shot.form` added to every beat (SHOT-FORM-SYSTEM.md; see table below)
- Build status reset to PENDING for beats with narration changes (B03, BVDT, BHTF)
- `shot.remotion.rendered.at` cleared for changed beats

## Datable-claim fixes (narration LOCKED except these)

### `modelLabel`: "Opus 4.8" → "Opus 4.7"
- Location: B00.shot.remotion.props.modelLabel, BHTF.shot.remotion.props.modelLabel, metadata.modelLabel
- Reason: "Opus 4.8" does not exist in current model registry (env shows Opus 4.7 as latest). Datable claim per REBUILD contract.
- Source: Environment context (2026-08-25): claude-opus-4-7 is current latest Opus.

## Narration truncation repairs (content errors, not locked script)
These are text-generation artifacts where the beat's narration text was cut mid-sentence,
producing grammatically broken speech. They are NOT intentional script content.
Each is logged old → new.

### B03.narration_text (body beat — design tell)
- OLD: "Claude's job: Screen a Medicare/Medicaid claims corpus for fraud, waste, and abuse and produce ranked, fully-cited."
- NEW: "Claude's job: Screen a Medicare/Medicaid claims corpus for fraud, waste, and abuse and produce ranked, fully-cited investigation referrals."
- Source: B00 narration contains the full phrase; B03 was truncated at "fully-cited."

### BVDT.narration_text (verdict — Phase 1 Check 4 authorized)
- OLD: "The SKILL.md is the spec — Screen a Medicare/Medicaid claims corpus for fraud, waste, and abuse and produce."
- NEW: "The SKILL.md is the spec — Screen a Medicare/Medicaid claims corpus for fraud, waste, and abuse and produce ranked investigation referrals."
- Source: Truncation artifact; full description in B00.

### BVDT.shot.remotion.props.artifactLines[1] (verdict visual — Phase 1 Check 4 authorized)
- OLD: "Screen a Medicare/Medicaid claims corpus for fraud, waste,"
- NEW: "Screen Medicare/Medicaid claims: fraud, waste, and abuse"
- Reason: Truncated mid-phrase; rewritten to be a complete, legible artifact line.

### BHTF.narration_text (handoff — Phase 1 Check 3 authorized)
- OLD: "...I want to screen a medicare/medicaid claims corpus for fraud, waste, and abuse a."
- NEW: "...I want to screen a medicare/medicaid claims corpus for fraud, waste, and abuse."
- Source: Stray "a" fragment after "abuse" — text generation artifact.

### BHTF.shot.remotion.props.command
- OLD: "I want to screen a medicare/medicaid claims corpus for fraud, waste, and abuse a. Read the fraud-detection skill..."
- NEW: "I want to screen a medicare/medicaid claims corpus for fraud, waste, and abuse. Read the fraud-detection skill..."
- Source: Same truncation artifact; matches the narration fix.

## Spark line fix (Phase 1 Check 3)
### B03.shot.remotion.props.sparkLine
- OLD: "This is the part worth knowing." (generic — does not compress from beat's own narration)
- NEW: "Spec-locked. Bounded." (4 words; compressed from B03 narration's key claim)

## shot.form added (SHOT-FORM-SYSTEM.md)
| Beat | Form assigned | Rationale |
|---|---|---|
| B00 | claude-code | ClaudeComposerAsk is the CC skin |
| B01 | slide-b | File tree with icons — closest to icon enumeration |
| B02 | step-sequence | Ordered pipeline steps |
| B03 | slide-a | Text mechanism description (one claim) |
| BVDT | slide-a | Verdict artifact lines (text card) |
| BHTF | claude-code | ClaudeComposerAsk (handoff) |
| BOUT | slide-a | Title restate card |

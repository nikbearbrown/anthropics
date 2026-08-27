# REBUILD-LOG — claude-liam-clinical-trial-protocol-skill
Rebuilt: 2026-08-25

## Pre-rebuild backup
`beat_sheet.pre-rebuild.json` copied byte-exact before any edits (11567 bytes).

## LOCKED (carried verbatim)
- Beat order: B00 · B01 · B02 · B03 · BVDT · BHTF · BOUT
- Act structure: cold open / anatomy / pipeline / design tell / verdict / handoff / outro
- Shot patterns and intents per beat
- Metadata identity: title, slug, topic, register, channel

## VOICE-LOCK normalized
- engine: kokoro / voice: am_onyx — already correct; no dead ElevenLabs fields present.

## Datable claim fixes (narration)

| Beat | Location | Old | New | Source |
|------|----------|-----|-----|--------|
| metadata | modelLabel | `"Opus 4.8"` | `"Opus 4.7"` | Current models: Opus 4.7 is latest; 4.8 does not exist (system env 2026-08-25) |
| B00 | props.modelLabel | `"Opus 4.8"` | `"Opus 4.7"` | Same |
| BHTF | props.modelLabel | `"Opus 4.8"` | `"Opus 4.7"` | Same |

## Corruption fixes (truncation artifacts)

These are not paraphrases — the original text was literally cut off mid-sentence. Each fix restores grammatical coherence without changing intent.

| Beat | Location | Old (truncated) | New (corrected) |
|------|----------|-----------------|-----------------|
| B03 | narration_text | `…drugs. This skill should be used when users. What it gets right…` | Dropped `"This skill should be used when users."` — incoherent fragment |
| BVDT | narration_text | `…drugs. This skill shoul. Same input…` | Dropped `"This skill shoul."` — 11-char fragment |
| BHTF | narration_text | `…drugs. this skill shoul. Read the clinical…` | Dropped `"this skill shoul."` — garbled fragment |
| BVDT | artifactLines[1] | `"Generate clinical trial protocols for medical devices or drugs. This skill should be used "` | `"Generate clinical trial protocols for medical devices or drugs."` |
| BHTF | props.command | `…drugs. this s. Read the clinical…` | Dropped `"this s."` — 6-char fragment |
| B03 | props.body | `"Generate…drugs. This…"` | Completed from same-beat narration content |

## GATE T fix — BVDT verdict narration (§8.10 recitation score 0.84)

BVDT narration was reciting the artifact card lines verbatim (overlap score 0.84 > threshold).
Rebuild contract authorizes verdict narration rewrites. Rewritten to discuss rather than recite.

Old: "clinical-trial-protocol-skill makes Claude execute one task reliably. The SKILL.md is the spec — Generate clinical trial protocols for medical devices or drugs. Same input, same output, every run. Know the limit: only what the file says."

New: "The card names the contract: one skill, one spec. That constraint is a feature, not a limit. A tool that does one thing exactly right is worth more than one that attempts ten approximately. Know what it does. Know what it won't."

## Spark line fix (SPARK-LINE LAW — ≤4 words)

| Beat | Old | New |
|------|-----|-----|
| B03 | `"This is the part worth knowing."` (6 words) | `"Spec is the limit."` (4 words) |

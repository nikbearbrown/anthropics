# REBUILD-LOG — claude-liam-supplier-selection

Rebuilt: 2026-08-26 by film-factory loop.

## What was locked (carried verbatim)

- Beat order and act labels: B00 / B01 / B02 / B03 / BVDT / BHTF / BOUT
- Shot intent and patterns: ClaudeComposerAsk, SkillTeardownAnatomy, SkillTeardownPipeline, SkillTeardownMechanism, ClaudeVerdictArtifact, ClaudeComposerAsk, ClaudeTitleOutro
- Core narration structure: Teardown register, In-for-Bear sign-off, design-tell framing

## What was rebuilt

- VOICE-LOCK fields: already kokoro / am_onyx — no change required.
- Dead fields: none found (no voice_id, voice_env, ElevenLabs clock prose).

## Datable claim fixes (narration)

| Beat | Old | New | Source |
|---|---|---|---|
| Metadata `modelLabel` | "Opus 4.8" | "Opus 4.7" | Anthropic model page; Opus 4.8 does not exist as of 2026-08-26 |
| B00 props `modelLabel` | "Opus 4.8" | "Opus 4.7" | same |
| BHTF props `modelLabel` | "Opus 4.8" | "Opus 4.7" | same |

## Truncation artifact fixes (authorized as content defects — narration intent preserved)

All truncations were auto-generated clipping of the SKILL.md description ("How to rank
and pick a supplier for a SKU. Load this whenever a task involves choosing a supplier,
comparing quotes, or creating a purchase order.") at an apparent 80-char limit.

| Location | Old | New |
|---|---|---|
| B00 `narration_text` | "...purchase order.. A SKILL.md" (double period) | "...purchase order. A SKILL.md" |
| B03 `narration_text` | "choosing a supplier, c. What it gets right" | "choosing a supplier, comparing quotes, or creating a purchase order. What it gets right" |
| BVDT `narration_text` | "task involves ch. Same input" | "task involves choosing a supplier. Same input" |
| BVDT `artifactLines[1]` | "choosing a s" (truncated mid-word) | "Task: rank and pick a supplier for a SKU — chosen by a weighted score" (rewritten to be a clean verdict line; original was unreadable) |
| BHTF `narration_text` | "'I want to how to rank and pick a supplier for a sku. load this whenever a task involves ch." | "'I need to select a supplier for a SKU. Read the supplier-selection skill and walk me through what you will do before you do it.'" |
| BHTF `command` prop | "I want to how to rank and pick a supplier for a sku. load this whenever a task i. Read the supplier-selection skill..." | "I need to select a supplier for a SKU. Read the supplier-selection skill and walk me through what you will do before you do it." |

## Spark line fixes (phase 1 authorized)

| Beat | Old | New | Reason |
|---|---|---|---|
| B01 `props.sparkLine` | "The file is the program." (5 words) | "File is the program." (4 words) | SPARK-LINE LAW: ≤4 words |
| B03 `props.sparkLine` | "This is the part worth knowing." (7 words) | "Know the limit." (3 words) | SPARK-LINE LAW: ≤4 words |

## GATE T fix (type_check.py)

| Beat | Issue | Fix |
|---|---|---|
| B03 `props.body` | 26 words > 12-word pull-quote limit (§8.5 no-wordy-card) | Shortened to "Arithmetic, not judgment — the formula is the spec." (8 words). Preserves the design-tell intent; captures the SKILL.md's key principle ("Ranking suppliers is arithmetic, not judgment"). |

## Audio status

Existing mp3 files from 2026-07-25 cover beats with unchanged narration (B01, B02, BOUT).
Beats with narration changes require regen: B00, B03, BVDT, BHTF.
Full regen will run to ensure clock consistency.

# REBUILD-LOG — claude-liam-claude-opus-4-5-migration

Rebuilt: 2026-08-25

## Locked (carried over verbatim)
- All narration_text per beat — script is unchanged
- Beat order and act labels
- Shot patterns, sparkLines, visual descriptions (except GATE T fix below)
- Metadata identity: title, slug, topic, source pointer, register, channel

## Changes made

### 1. BHTF greeting — spec compliance
- **Field:** `beats[BHTF].shot.remotion.props.greeting`
- **Old:** `"Your Turn"`
- **New:** `"Your turn."`
- **Source:** ai-explainer SKILL.md HANDOFF LAW: "greeting fixed to `Your turn.` (viewer-addressed)"

### 2. modelLabel datable claim — B00
- **Field:** `beats[B00].shot.remotion.props.modelLabel`
- **Old:** `"Opus 4.8"`
- **New:** `"Opus 4.7"`
- **Source:** Opus 4.8 does not exist. Current latest is Opus 4.7 (claude-opus-4-7) per Anthropic model registry as of 2026-08-25. DOUBLE-CHECK LAW / rebuild datable-claims exception.

### 3. modelLabel datable claim — BHTF
- **Field:** `beats[BHTF].shot.remotion.props.modelLabel`
- **Old:** `"Opus 4.8"`
- **New:** `"Opus 4.7"`
- **Source:** Same as above.

### 4. B05 sparkLine — GATE T §8.5 no-wordy-card fix
- **Field:** `beats[B05].shot.remotion.props.sparkLine`
- **Old:** `"Platform matrix and opt-in discipline solid. Azure gap and vague triggers: surface them."` (13 words)
- **New:** `"Solid frame. Real gaps."` (4 words)
- **Source:** type_check.py GATE T §8.5 no-wordy-card: sparkLine 13 words > 12 pull-quote limit. Compressed to ≤4 words per SPARK-LINE LAW.

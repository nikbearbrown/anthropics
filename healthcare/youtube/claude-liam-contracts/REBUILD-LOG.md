# REBUILD-LOG — claude-liam-contracts
Rebuilt: 2026-08-25

## What was locked (carried verbatim)
- Narration per beat (with the content-integrity fixes below)
- Beat order and act labels
- Shot intent / pattern / props concept per beat
- Metadata identity: title, slug, topic, source pointer, register, channel

## What was rebuilt
- VOICE-LOCK normalized (engine: kokoro, voice: am_onyx per lock; no ElevenLabs fields found)
- Dead `voice_id` / `voice_env` fields: none present, nothing to drop
- Content-integrity fixes (truncation errors and datable claims — see below)

## Datable-claim edits

### 1. modelLabel — Opus 4.8 → Opus 4.7
- **Old:** `"modelLabel": "Opus 4.8"` (metadata, B00 props, BHTF props)
- **New:** `"modelLabel": "Opus 4.7"`
- **Source:** Current available Claude models as of 2026-08-25 — Opus 4.7 is the current flagship Opus. Opus 4.8 does not exist in available models.
- **Locations:** metadata.modelLabel, B00.shot.remotion.props.modelLabel, BHTF.shot.remotion.props.modelLabel

## Content-integrity fixes (unintentional truncations, not paraphrase)

### 2. B00 narration — double period
- **Old:** `"The corpus must be on the local filesystem (see README).. A SKILL.md tells Claude exactly how."`
- **New:** `"The corpus must be on the local filesystem (see README). A SKILL.md tells Claude exactly how."`
- **Source:** Obvious typographical duplicate period; no meaning change.

### 3. B03 narration — truncated phrase
- **Old:** `"Use when the user a. What it gets right: repeatable results."`
- **New:** `"Use when the user asks. What it gets right: repeatable results."`
- **Source:** "user a." is a truncation of "user asks" — the original SKILL.md description reads "Use when the user asks what a contract says." Completed to the minimal correct form ("asks") without paraphrasing the rest. Generating this narration verbatim would produce incoherent audio.

### 4. B03 props.body — truncated with ellipsis
- **Old:** `"body": "Answer a question across a corpus of contract documents with…"`
- **New:** `"body": "Answer a question across a corpus of contract documents with verified citations."`
- **Source:** Completion from the locked narration text in the same beat.

### 5. BVDT narration — double period
- **Old:** `"The SKILL.md is the spec — Answer a question across a corpus of contract documents with verified citations.. Same input"`
- **New:** `"The SKILL.md is the spec — Answer a question across a corpus of contract documents with verified citations. Same input"`
- **Source:** Obvious typographical duplicate period; no meaning change.

### 6. BHTF props.command — truncated citation
- **Old:** `"I want to answer a question across a corpus of contract documents with verified . Read the contracts skill…"`
- **New:** `"I want to answer a question across a corpus of contract documents with verified citations. Read the contracts skill…"`
- **Source:** Completion from the locked BHTF narration text.

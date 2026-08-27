# REBUILD-LOG — claude-liam-submit-solution

Rebuilt: 2026-08-26

## What was locked (carried verbatim)
- All beat_id values and act labels
- Shot patterns and component assignments (ClaudeComposerAsk, SkillTeardownAnatomy, SkillTeardownPipeline, SkillTeardownMechanism, ClaudeVerdictArtifact, ClaudeTitleOutro)
- Core narration intent on all beats
- Metadata identity: title, slug, topic, register, persona, source_skill

## What was rebuilt / fixed

### Datable claim — modelLabel
- Old: `"Opus 4.8"` (metadata, B00, BHTF props)
- New: `"Opus 4.7"`
- Source: Current model roster (Opus 4.7 is the latest Opus; 4.8 does not exist as of 2026-08-26)

### B00 output[1] — truncation artifact repair (§8.9 GATE T blocker)
- Old: `"Guide a workshop attendee through committing their starter-agent decomposition a"`
- New: `"task: commit starter-agent decomposition, open PR with workshop feedback"`
- Source: SKILL.md description; original was auto-truncated at character limit

### B03 props.body — truncation + wordiness repair (§8.9 + §8.5 GATE T blocker)
- Old: `"Guide a workshop attendee through committing their starter-agent decomposition and opening a PR with their solution + workshop feedback. Invoke when the user says "submit", "I'm done", "open a PR", or"` (31 words, truncated)
- New: `"The SKILL.md is the spec — outside it, Claude stops."` (10 words, complete)
- Source: SkillTeardownMechanism pull-quote ≤12 words; captures the design constraint from B03 narration

### B03 narration_text — truncation artifact repair
- Old: `"...and opening a PR with. What it gets right:"` (broken clause)
- New: `"...and opening a PR with their solution. What it gets right:"`
- Source: SKILL.md full description; "with" was auto-truncated before "their solution"

### BVDT narration_text — truncation artifact repair
- Old: `"...Guide a workshop attendee through committing their starter-agent decomposition a. Same input..."` ("decomposition a" is a truncation)
- New: `"...commit the starter-agent decomposition, open the PR. Same input..."`
- Source: Reel's own narration intent; "a" was truncated character from "and opening a PR"

### BVDT artifactLines[1] — truncation repair
- Old: `"Guide a workshop attendee through committing their starter-agent decomposition and opening"` (incomplete sentence)
- New: `"Task: commit starter-agent decomposition, open PR with workshop feedback"` (complete, ≤80 chars)
- Source: Same as B00 output fix; captures the full task

### BHTF props.command — truncation repair
- Old: `"...starter-agent decom. Read the submit-solution skill..."` ("decom" is truncated "decomposition")
- New: `"...starter-agent decomposition and opening a PR. Read the submit-solution skill..."`
- Source: SKILL.md; "decom" was auto-truncated

## VOICE-LOCK normalized
- engine: kokoro, voice: am_onyx — already correct, no dead ElevenLabs fields present
- No voice_id, voice_env, or ElevenLabs clock fields found — no drops required

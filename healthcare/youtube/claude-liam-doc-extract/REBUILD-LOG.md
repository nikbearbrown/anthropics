# REBUILD-LOG.md — claude-liam-doc-extract
Rebuild pass: 2026-08-25

## What was locked (carried verbatim)
- narration_text for all beats (except BVDT narration_text — verdict fix authorized by PHASE 1 Check 4)
- Beat order and act labels
- Shot intent, patterns, and props (except authorized fixes below)
- Metadata identity: title, slug, topic, source_skill, register, channel, brand

## What was rebuilt / normalized
- VOICE-LOCK: engine/voice already correct (kokoro/am_onyx). No dead ElevenLabs fields found.
- shot.form: added to all beats (SHOT-FORM-SYSTEM.md)
- Fresh Kokoro audio generation (PHASE 2)

## Datable-claim edits (narration unchanged; props corrected)

### Edit 1 — modelLabel "Opus 4.8" → "Opus 4.7"
- **Where:** metadata.modelLabel, B00 props.modelLabel, BHTF props.modelLabel
- **Old:** "Opus 4.8"
- **New:** "Opus 4.7"
- **Source:** Anthropic model lineup as of 2026-08-25. Opus 4.8 does not exist; latest Opus is 4.7 (claude-opus-4-7).

## Verdict edits (PHASE 1 Check 4 authorizes all BVDT fixes)

### Edit 2 — BVDT narration_text truncation fix
- **Where:** BVDT beat narration_text
- **Old:** "...or plain t. Same input..."
- **New:** "...or plain text/markdown/HTML. Same input..."
- **Source:** doc-extract SKILL.md specifies PDF, DOCX, XLSX, PPTX, RTF, and plain text/markdown/HTML.

### Edit 3 — BVDT artifactLines[1] truncation fix
- **Where:** BVDT shot.remotion.props.artifactLines[1]
- **Old:** "Extract plain text from a document file - PDF, DOCX, XLSX, PPTX, RTF, or plain text/markdo"
- **New:** "Extract plain text from a document file - PDF, DOCX, XLSX, PPTX, RTF, or plain text/markdown/HTML"
- **Source:** Same as Edit 2.

## Card text edits (PHASE 1 Check 5 authorizes Remotion prop fixes)

### Edit 4 — BHTF command prop truncation fix
- **Where:** BHTF shot.remotion.props.command
- **Old:** "I want to extract plain text from a document file - pdf, docx, xlsx, pptx, rtf, . Read the doc-extract skill..."
- **New:** "I want to extract plain text from a document file - pdf, docx, xlsx, pptx, rtf, or plain text/markdown/HTML. Read the doc-extract skill..."
- **Source:** Same as Edit 2.

## Locked narration issues (not changed — logged only)

- **B00 narration_text:** Double period "port fixes to both.. A SKILL.md" — copy artifact. Locked.
- **B03 narration_text:** "...plain text/markdown/HTML. U. What it gets right..." — "U." is a truncation of "Use when...". In locked body narration; not a datable claim. Locked.
- **BHTF narration_text:** "...pdf, docx, xlsx, pptx, rtf, or plain t. Read..." — same truncation pattern. In locked handoff narration. Locked. (The Remotion command prop was fixed separately — Edit 4 above.)

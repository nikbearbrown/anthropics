# REBUILD-LOG.md — claude-liam-analyzing-financial-statements

**Rebuild date:** 2026-08-25  
**Original sheet preserved at:** `beat_sheet.pre-rebuild.json`

---

## LOCKED (carried over verbatim)

- Beat order and act labels (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro)
- Remotion patterns per beat (ClaudeComposerAsk, SkillTeardownAnatomy, SkillTeardownPipeline, SkillTeardownMechanism, ClaudeVerdictArtifact, ClaudeComposerAsk, ClaudeTitleOutro)
- Props intent (skill anatomy file tree, pipeline 3-phase, design tell structure)
- Metadata identity: title, slug, topic, register, channel, source_skill pointer

## NARRATION CHANGES (log required)

### B03 — corruption fix (GATE T §8.9 prerequisite)
- **Old:** "Claude's job: This skill calculates key financial ratios and metrics from financial statement data for investment . What it gets right"
- **New:** "Claude's job: This skill calculates key financial ratios and metrics from financial statement data for investment analysis. What it gets right"
- **Source:** Completion of truncated sentence; "investment analysis" is the actual skill description from the source SKILL.md.

### BVDT — §8.10 advisory + narration coherence fix
- **Old:** "analyzing-financial-statements makes Claude execute one task reliably. The SKILL.md is the spec — This skill calculates key financial ratios and metrics from financial statement . Same input, same output, every run. Know the limit: only what the file says."
- **New:** "analyzing-financial-statements makes Claude execute one task reliably. Give it a balance sheet or income statement and it runs the ratios every time. Same input, same output, every run. The limit is the spec: only what SKILL.md specifies."
- **Reason:** (1) Narration was truncated ("...from financial statement ."), making it incoherent. (2) type_check §8.10 flagged that narration was reciting the card rather than discussing it. Rewritten to discuss the artifact's behavior rather than paste its spec description.

### BHTF — corruption fix (broken prompt sentence)
- **Old:** "Your turn. Paste this into Claude: 'I want to this skill calculates key financial ratios and metrics from financial statement . Read the analyzing-financial-statements skill and walk me through what you will do before you do it.' That clause matters — explaining first surfaces the real constraint logic."
- **New:** "Your turn. Paste this into Claude: 'I want to analyze financial statements for investment insights. Read the analyzing-financial-statements skill and walk me through what you will do before you do it.' That clause matters — explaining first surfaces the real constraint logic."
- **Reason:** Original text was garbled ("I want to this skill calculates...") — a paste-corruption artifact from initial generation. Reconstructed to a coherent, pasteable prompt that fulfills the same intent.

---

## PROPS CHANGES

### B03 — `body` shortened (GATE T §8.5 fail: 15 words > 12 limit)
- **Old:** `"body": "This skill calculates key financial ratios and metrics from financial statement data for investment analysis"`
- **New:** `"body": "Calculates key financial ratios and metrics from statement data."`
- **Reason:** SkillTeardownMechanism `body` prop exceeded the 12-word pull-quote limit. Shortened to 9 words while preserving meaning.

### BVDT — `artifactLines[1]` truncation fix (GATE T §8.9 fail)
- **Old:** `"This skill calculates key financial ratios and metrics from financial statement data for i"`
- **New:** `"Calculates key ratios and metrics from financial statement data for investment analysis"`
- **Reason:** Original line was truncated mid-word ("...for i"). Completed and slightly reformatted to fit card width.

### BHTF — `command` reconstruction (same corruption as narration)
- **Old:** `"I want to this skill calculates key financial ratios and metrics from financial . Read the analyzing-financial-statements skill and walk me through what you will do before you do it."`
- **New:** `"I want to analyze financial statements for investment insights. Read the analyzing-financial-statements skill and walk me through what you will do before you do it."`
- **Reason:** Broken sentence reconstructed to match the repaired narration.

### BOUT — `subline` removed (OUTRO LAW)
- **Old:** `"subline": "analyzing-financial-statements · Anthropic Skills"`
- **New:** prop removed
- **Reason:** OUTRO LAW: "@NikBearBrown outro card is locked — NO subline; claude-liam reels only."

---

## VOICE-LOCK

- engine: kokoro, voice: am_onyx throughout — correct, no dead ElevenLabs fields in source.

## GATES

- GATE T (type_check.py): **PASS** (after fixes above)
- Stale renders: NONE (no mp4s existed)
- Spark lines: **PASS** (tool confirmed)
- Verdict: **PASS** (verdict_audit confirmed, reel-specific)

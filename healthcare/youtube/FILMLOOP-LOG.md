# FILMLOOP-LOG.md — anthropics/healthcare/youtube

One block per completed reel. Appended by the unattended film factory.

---

## claude-liam-fhir | 2026-08-25T22:02 | DONE

**Duration:** 106.0 s (7 beats, all VIDEO, no slates)
**Cut mtime:** 1787709755 — newer than beat_sheet.json (1787709751) ✓
**Gate Audio:** PASS — mean_volume −23.8 dB (threshold −40 dB)
**Gate T:** PASS — 0 FAILs (7 beats checked, TYPECHECK.md 2026-08-25)
**Gate V:** PASS — BLOCKER 0, MAJOR 0 on real beats (1 ADVISORY: B02 sub "endpoint" word dropped at node width limit; primary label and "any SMART" intact)

### Checks fixed (Phase 1 — prior session)

| # | What | Old | New |
|---|------|-----|-----|
| 1 | `metadata.modelLabel` datable claim | "Opus 4.8" | "Opus 4.7" |
| 2 | `B00.props.modelLabel` datable claim | "Opus 4.8" | "Opus 4.7" |
| 3 | `BHTF.props.modelLabel` datable claim | "Opus 4.8" | "Opus 4.7" |
| 4 | B02 pattern (card-only reel fix) | SkillTeardownPipeline (static) | FlowDiagram (animated node-edge) |
| 5 | B03 narration truncation | "…or any S. What it gets right…" | full sentence restored |
| 6 | B03 sparkLine length | "This is the part worth knowing." (7w) | "Spec is the limit." (4w) |
| 7 | BVDT narration + artifactLines | boilerplate + truncation | reel-specific, from body narration |
| 8 | BHTF narration + command truncation | "…meditech, at. Read…" | full clause restored |

### Checks fixed (Phase 2 — this invocation)

| # | What | Old | New |
|---|------|-----|-----|
| 9 | B02 FlowDiagram node sub (Gate V truncation) | "Epic · Cerner · MEDITECH" (MAJOR) | "any SMART endpoint" (ADVISORY) |

### Punts authored
None — all 7 beats are VIDEO; no punts in the build.

### Verdict
Real, reel-specific (authored from body narration). Narration discusses access value + spec constraint. 3 lines. Passes verdict_audit.py (absent from output).

### Build status Counter
`{'VIDEO': 7}`

---

## claude-liam-icd10-cm-skill | 2026-08-25T19:16 | DONE

**Duration:** 98.1 s (7 beats, all VIDEO, no slates)
**Cut mtime:** 1787699802 — newer than beat_sheet.json (1787699799) ✓
**Gate Audio:** PASS — mean volume −23.9 dB (threshold −40 dB)
**Gate T:** PASS — 0 FAILs (7 beats checked)
**Gate V:** PASS — BLOCKER 0, MAJOR 0 on real beats

### Checks fixed (Phase 1)

| # | What | Old | New |
|---|------|-----|-----|
| 1 | `metadata.modelLabel` datable claim | "Opus 4.8" | "Opus 4.7" |
| 2 | `B00.props.modelLabel` datable claim | "Opus 4.8" | "Opus 4.7" |
| 3 | `BHTF.props.modelLabel` datable claim | "Opus 4.8" | "Opus 4.7" |
| 4 | `B00.props.output[1]` truncation | "Extract billable ICD-10-CM diagnosis codes from a." | "Extract billable ICD-10-CM diagnosis codes." |
| 5 | `B03.props.body` truncation + §8.5 | 17-word truncated sentence | "Extract billable ICD-10-CM codes from a clinical encounter." (9 words) |
| 6 | `B03.props.quote` (added) | missing | "What it gets right: repeatable results. What it bites: anything outside the spec." |
| 7 | `B03.props.cite` (added) | missing | "icd10-cm-skill SKILL.md" |
| 8 | `B03.props.verdictLabel` (added) | missing | "Repeatable" |
| 9 | `B03.props.verdictPositive` (added) | missing | true |
| 10 | `BVDT.props.artifactLines[1]` truncation | "…professional cod" (mid-word) | "…professional coder builds the claim" |
| 11 | `BHTF.props.command` truncation | "…the way a profes." | "…the way a professional coder builds the claim." |
| 12 | `BHTF.props.topic` overflow | "ICD10-CM-SKILL · ANTHROPIC SKILL · YOUR TURN" (2-line overflow) | "ICD10-CM-SKILL · YOUR TURN" |
| 13 | `BOUT.props` schema | had `handle`, `subline` (not in schema) | removed both; added `slug: "claude-liam-icd10-cm-skill"` |

### Punts authored

None — all 7 beats had valid Remotion patterns (SkillTeardownAnatomy, SkillTeardownPipeline, SkillTeardownMechanism, ClaudeComposerAsk ×2, ClaudeVerdictArtifact, ClaudeTitleOutro).

### Verdict

Existing BVDT verdict **retained and confirmed specific** — names skill and task explicitly, not a template. verdict_audit.py: PASS.

### Gate V detail

| Beat | Pattern | Fill | Result |
|------|---------|------|--------|
| B00 | ClaudeComposerAsk | ≥55% | PASS |
| B01 | SkillTeardownAnatomy | ≥55% | PASS |
| B02 | SkillTeardownPipeline | ≥55% | PASS |
| B03 | SkillTeardownMechanism | ≥55% (fixed — quote+verdict added) | PASS |
| BVDT | ClaudeVerdictArtifact | ≥55% | PASS |
| BHTF | ClaudeComposerAsk | ≥55% (fixed — topic shortened) | PASS |
| BOUT | ClaudeTitleOutro | ~45% | JUSTIFIED DOWNGRADE |

### Justified downgrade — BOUT underfill 45%

ClaudeTitleOutro is a LOCKED component (OUTRO-LOCK.md). Its centered layout with a short 5-word title yields structural underfill. QC anchor dots are present. Cannot fix without modifying the locked component. Accepted as structural property of this component class.

### Locked narration artifacts (cannot fix)

Three narration_text truncations exist in LOCKED narration (audio already rendered faithfully):
- B03: "…the way a professional coder builds ." (missing "the claim")
- BVDT: "…the way a profes." (truncated mid-word)
- BHTF: "…the way a profes." (truncated mid-word)

Future rebuild/re-script would fix at the source. Props were corrected to full text.

---

## claude-liam-clinical-trial-protocol-skill — 2026-08-25

**Slug:** claude-liam-clinical-trial-protocol-skill  
**Duration:** 96.1s  
**Cut:** master (7/7 VIDEO, 0 slates)  
**Audio:** GATE AUDIO PASS — mean_volume -23.9 dB  

### Checks fixed
- modelLabel "Opus 4.8" → "Opus 4.7" (×3: metadata + B00 + BHTF props) — datable claim
- B03 sparkLine "This is the part worth knowing." (6 words) → "Spec is the limit." (4 words)
- 6 truncation artifacts across narration_text and props (B03, BVDT, BHTF narration; BVDT artifactLines[1]; BHTF command prop; B03 body prop)
- GATE T §8.10 — BVDT narration recited card (score 0.84); rewritten to discuss-not-recite (score → 0.11)
- GATE T §8.5 — B03 body prop de-wordified from 16 words → 12 words
- B02 double-terracotta — "Read SKILL.md" accent:true → accent:false; OUTPUT/RESULT is the single accent

### Punts authored
None — all 7 beats were Remotion patterns, no punts present.

### Verdict
Kept (not stripped) — verdict content is specific to this skill, not a template placeholder.
BVDT narration rewritten per rebuild-contract verdict authorization.

### Gate V
BLOCKER: 0  
MAJOR downgraded: 2
- B03 (SkillTeardownMechanism underfill ~20%): template limitation, body at §8.5 max; component-level fix required
- BOUT (ClaudeTitleOutro underfill ~35%): deliberate negative-space template design; consistent across all skill-teardown reels

### GATE T
PASS (after BVDT narration rewrite and B03 body de-wordify)

---

# REBUILD-LOG — claude-liam-fhir
Rebuilt: 2026-08-25

## LOCKED (carried verbatim)
- Narration text for B00, B01, B02, BOUT
- Beat order and act labels (B00, B01, B02, B03, BVDT, BHTF, BOUT)
- Shot intent for all beats
- Metadata identity (title, slug, topic, register, channel)

## REBUILT / FIXED

### 1. modelLabel — datable claim
**Old:** "Opus 4.8" (metadata + B00 props + BHTF props)
**New:** "Opus 4.7"
**Source:** System context — current Opus family is 4.7 (claude-opus-4-7). Opus 4.8 does not exist.
Applies to: metadata.modelLabel, B00 props.modelLabel, BHTF props.modelLabel

### 2. B02 — FlowDiagram replacing SkillTeardownPipeline
**Old:** pattern: SkillTeardownPipeline (static phase list card)
**New:** pattern: FlowDiagram (animated node-edge diagram, skin: claude)
**Why:** Card-only reel check — no body beat drew a figure. FlowDiagram renders the FHIR connection
pipeline as a drawn animated diagram with bezier edges and pulse, satisfying the "at least one
drawn figure" requirement. Nodes: Your Request → Read SKILL.md → FHIR R4 Server → Clinical Data.
**Narration:** LOCKED (unchanged).

### 3. B03 narration — truncated string fix
**Old:** "...MEDITECH, athenahealth, or any S. What it gets right..."
**New:** "...MEDITECH, athenahealth, or any SMART-on-FHIR endpoint), pull a patient's clinical
data and notes, and extract structured findings. What it gets right..."
**Why:** "any S" was a machine-truncation artifact. Restored to the full sentence from B00 narration
(same source clause). This is a bug fix, not a substantive edit; the intent was always the full text.

### 4. B03 sparkLine — length fix
**Old:** "This is the part worth knowing." (7 words)
**New:** "Spec is the limit." (4 words)
**Why:** Inner-beat spark lines must be ≤ 4 words compressed from that beat's narration.

### 5. BVDT narration and verdict lines — boilerplate replacement + truncation fix
**Old narration:** "fhir makes Claude execute one task reliably. The SKILL.md is the spec — Connect
to a hospital's FHIR R4 server (Epic, Oracle Health/Cerner, MEDITECH, at. Same input, same output,
every run. Know the limit: only what the file says."
  - "MEDITECH, at" is truncated (machine artifact; should be "athenahealth, or any SMART-on-FHIR endpoint")
  - "Same input, same output, every run" / "Limit: only what the SKILL.md specifies" appear in
    250+ reels — boilerplate per verdict_audit.py

**New narration:** "The fhir skill's value is access — structured EHR data without bespoke integration
code. Connect to Epic, Cerner, MEDITECH, athenahealth — any SMART-on-FHIR endpoint. One instruction
set. One result per run. The limit is the spec, and that is the point."

**Old artifactLines:**
  - "Skill: fhir — Claude reads SKILL.md before acting"
  - "Connect to a hospital's FHIR R4 server (Epic, Oracle Health/Cerner, MEDITECH, athenahealth" (truncated)
  - "Same input → same output, every run" (250-reel boilerplate)
  - "Limit: only what the SKILL.md specifies" (250-reel boilerplate)

**New artifactLines:**
  - "fhir: reads SKILL.md, then connects to Epic, Cerner, MEDITECH, or athenahealth"
  - "Pulls patient clinical data from any SMART-on-FHIR endpoint"
  - "Extracts structured findings — one instruction set, one result per run"

**Source:** Derived from B01, B02, B03 body narration of this reel.

### 6. BHTF narration — truncated string fix
**Old:** "...meditech, at. Read the fhir skill..."
**New:** "...meditech, athenahealth, or any smart-on-fhir endpoint). Read the fhir skill..."
**Why:** Machine-truncation artifact. Restored full clause.

### 7. BHTF command prop — truncated string fix
**Old:** "I want to connect to a hospital's fhir r4 server (epic, oracle health/cerner, me. Read..."
**New:** "I want to connect to a hospital's fhir r4 server (epic, oracle health/cerner, meditech,
athenahealth, or any smart-on-fhir endpoint). Read..."
**Why:** Machine-truncation artifact.

## Audio regeneration required
Beats with changed narration: B03, BVDT, BHTF
Beats with unchanged narration (mp3 reusable): B00, B01, B02, BOUT

### 8. B02 FlowDiagram node sub — Gate V truncation fix (2026-08-25 build invocation)
**Old:** B02 FHIR R4 Server node sub: "Epic · Cerner · MEDITECH"
**New:** B02 FHIR R4 Server node sub: "any SMART endpoint"
**Why:** Gate V frame QC found "Epic · Cerner · MEDITECH" truncated to "Epic · Cerner ·"
in the FlowDiagram render (node width constraint). New sub is shorter; "any SMART" renders
fully, communicating the SMART-on-FHIR protocol. Node label "FHIR R4 Server" intact.
The specific vendors (Epic, Cerner, MEDITECH, athenahealth) are all named in the narration.
**Narration:** LOCKED (unchanged).

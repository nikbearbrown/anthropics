# Source Details — healthcare--claude-liam-icd10-cm-skill

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Icd10 Cm Skill.
- Family: healthcare
- Source sheet: /Users/nik/Documents/books/anthropics/healthcare/youtube/claude-liam-icd10-cm-skill/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/healthcare/plugins/healthcare/skills/icd10-cm/SKILL.md
- Name: icd10-cm-skill
- Description: Extract billable ICD-10-CM diagnosis codes from a clinical note the way a professional coder builds the claim. Use when users say "code this encounter", "assign ICD-10 codes", "what diagnosis codes apply", "code this chart", or when turning clinical documentation into claim-ready diagnosis codes.

## Capabilities To Name On Screen
- Extract billable ICD-10-CM diagnosis codes from a clinical note the way a professional coder builds the claim
- Use when users say "code this encounter"
- "assign ICD-10 codes"
- "what diagnosis codes apply"
- "code this chart"

## Constraints / Failure Modes
- Chronic comorbidities, but only if they were addressed or changed medical decision-making this visit
- Symptoms: when the patient came in FOR a symptom and the visit ends with no established diagnosis, that symptom is the first-listed diagnosis — code it (low back pain…
- Uncertain diagnoses — "probable", "suspected", "rule out". In outpatient coding these are never coded; code the presenting symptom instead
- Conditions mentioned only as history and not treated today
- Wellness-exam codes (Z00.0x) on a problem-focused visit. They belong only when the encounter is an actual scheduled physical
- External-cause codes (V00–Y99, how an injury happened): outpatient claims rarely carry them and most payers don't require them — the injury code itself carries the…
- Don't hedge on a diagnosis. Never list sibling codes, candidate alternatives, or a category plus its children for the same diagnosis — commit to the single code the…
- Code exactly what the note documents — never above it, never below it

## Procedure / Sequence
- Decide what belongs on the claim: A claim reflects the encounter, not the patient's chart. Per the ICD-10-CM Official Guidelines for outpatient coding…
- Code at the documented specificity: This is where most miscoding happens. Two rules: Don't hedge on a diagnosis. Never list sibling codes, candidate…
- Find the exact code via the ICD-10 connector: Look up every diagnosis with the ICD-10 Codes connector's tools — including diagnoses you're sure you know. Code sets…
- Final check: Walk your draft list once before answering. For each code ask: 1. Does the note show this condition was evaluated…

## Supporting Files And Signals
- Referenced: search_codes
- Referenced: code_type="diagnosis"
- Referenced: lookup_code
- Referenced: validate_code
- Referenced: README.md

## Source Sections
- Step 1: Decide what belongs on the claim
- Step 2: Code at the documented specificity
- Step 3: Find the exact code via the ICD-10 connector
- Working style
- Step 4: Final check
- Answer format

## Batch Log Match
- Row: 260
- Canonical path: anthropics/healthcare/plugins/healthcare/skills/icd10-cm/SKILL.md
- MP4 path: anthropics/healthcare/youtube/claude-liam-icd10-cm-skill/mp4/claude-liam-icd10-cm-skill.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

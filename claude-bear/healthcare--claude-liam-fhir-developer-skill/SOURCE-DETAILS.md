# Source Details — healthcare--claude-liam-fhir-developer-skill

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Fhir Developer Skill.
- Family: healthcare
- Source sheet: /Users/nik/Documents/books/anthropics/healthcare/youtube/claude-liam-fhir-developer-skill/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/healthcare/plugins/healthcare/skills/fhir-developer/SKILL.md
- Name: fhir-developer-skill
- Description: >

## Capabilities To Name On Screen
- No capability bullets/headings extracted; use the description and section list.

## Constraints / Failure Modes
- required fields, value sets (status codes, gender, intent), coding systems (LOINC, SNOMED,
- | 422 Unprocessable Entity | Missing required fields, invalid enum values, business rule violations |
- ### Required Fields by Resource (FHIR R4)
- | Resource | Required Fields | Everything Else |
- ## Required vs Optional Fields (CRITICAL)
- Only validate fields with cardinality starting with "1" as required
- | Cardinality | Required? |
- Common mistake: Making subject or period required on Encounter. They are 0..1 (optional)

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: 0..1
- Referenced: 0..*
- Referenced: 1..1
- Referenced: 1..*
- Referenced: Invalid status '${req.body.status}'
- Referenced: http://loinc.org
- Referenced: http://snomed.info/sct
- Referenced: http://www.nlm.nih.gov/research/umls/rxnorm
- Referenced: http://hl7.org/fhir/sid/icd-10
- Referenced: http://terminology.hl7.org/CodeSystem/v3-ActCode
- Signal: code block: python
- Signal: code block: typescript
- Signal: code block: json
- Signal: code block: bash

## Source Sections
- Quick Reference
- HTTP Status Codes
- Required Fields by Resource (FHIR R4)
- Required vs Optional Fields (CRITICAL)
- Value Sets (Enum Values)
- Patient.gender
- Observation.status
- Encounter.status
- Encounter.class (Common Codes)
- Condition.clinicalStatus

## Batch Log Match
- Row: 238
- Canonical path: anthropics/healthcare/plugins/healthcare/skills/fhir-developer/SKILL.md
- MP4 path: anthropics/healthcare/youtube/claude-liam-fhir-developer-skill/mp4/claude-liam-fhir-developer-skill.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

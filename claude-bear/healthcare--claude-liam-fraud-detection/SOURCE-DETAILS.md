# Source Details — healthcare--claude-liam-fraud-detection

Generated: 2026-09-05T11:09:00

## Reel
- Question: Claude, Fraud Detection.
- Family: healthcare
- Source sheet: /Users/nik/Documents/books/anthropics/healthcare/youtube/claude-liam-fraud-detection/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/healthcare/plugins/healthcare/skills/fraud-detection/SKILL.md
- Name: fraud-detection
- Description: Screen a Medicare/Medicaid claims corpus for fraud, waste, and abuse and produce ranked, fully-cited investigation referrals for an SIU / program-integrity team. Use when asked to run a fraud sweep, screen claims for FWA, find billing anomalies, or generate investigation referrals over a claims dataset.

## Capabilities To Name On Screen
- Screen a Medicare/Medicaid claims corpus for fraud
- and abuse and produce ranked
- fully-cited investigation referrals for an SIU / program-integrity team
- Use when asked to run a fraud sweep
- screen claims for FWA

## Constraints / Failure Modes
- Seed the public reference layer (first run / new quarter only). Detectors cite against
- Adjudicate — one agent per judgment-required finding (D2/D4/D7/D13) sets status + adjudication.reason; mechanical detectors auto-confirm. Adjudicate may dismiss or…
- Materialize the stage snapshots + render (required — this is the reviewable deliverable). The
- Then render the packets FIRST, then the dashboard (the dashboard only links a provider row to its
- The model adjudicates, explores, and narrates freely, but **any dollar or rule allegation must trace
- or downgrade** a finding (with an auditable reason) — it never adds one or changes its dollars
- Synthesize narratives are separate, clearly-marked model output and never introduce a number the
- ## Enrichment — local cached data (canonical), MCPs for interactive only

## Procedure / Sequence
- Get the payer's claims into corpus.duckdb.: Open with: *"Where do your adjudicated claims live?"* and follow…
- Seed the public reference layer (first run / new quarter only).: Detectors cite against $CLAUDE_HEALTHCARE_DATA/fraud-detection/data-cache/reference/<quarter>/reference.duckdb. If that…
- Create the run directory.: Each invocation lands in its own minute-stamped directory so prior runs are preserved side-by-side. Every script honors…
- Run the investigation: by calling the Workflow tool with: - scriptPath: ${CLAUDE_PLUGIN_ROOT}/skills/fraud-detection/workflows/investigate.js…
- Materialize the stage snapshots + render: (required — this is the reviewable deliverable). The workflow sandbox has no filesystem, so write its return to disk…
- Show the dashboard: so the user can validate it visually. - Claude Code Desktop with the preview tool available: serve the run directory…
- Relay: the ranked referrals (NPI, schemes, exposure $, confidence) and total exposure from the workflow result, verbatim where…
- Close the loop: (optional) — see ${CLAUDE_PLUGIN_ROOT}/skills/fraud-detection/PROPOSE-DETECTORS.md to mine this run for new detector…

## Supporting Files And Signals
- Referenced: $CLAUDE_HEALTHCARE_DATA/fraud-detection/out/
- Referenced: corpus.duckdb
- Referenced: claims-schema.sql
- Referenced: ~/.claude/data/healthcare/fraud-detection/
- Referenced: $CLAUDE_HEALTHCARE_DATA
- Referenced: data-cache/
- Referenced: out/
- Referenced: $CLAUDE_HEALTHCARE_DATA/fraud-detection
- Referenced: ${CLAUDE_PLUGIN_ROOT}/skills/fraud-detection/LOAD-CLAIMS.md
- Referenced: $CLAUDE_HEALTHCARE_DATA/fraud-detection/data-cache/corpus.duckdb
- Signal: code block: bash

## Source Sections
- Output framing
- Inputs
- Data root
- Steps
- The inviolable line
- Enrichment — local cached data (canonical), MCPs for interactive only
- How it works (plugin layout)

## Batch Log Match
- Row: 245
- Canonical path: anthropics/healthcare/plugins/healthcare/skills/fraud-detection/SKILL.md
- MP4 path: anthropics/healthcare/youtube/claude-liam-fraud-detection/mp4/claude-liam-fraud-detection.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

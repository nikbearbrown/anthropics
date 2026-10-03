# Source Details — knowledge-work-plugins--claude-liam-explore-data

Generated: 2026-09-05T11:09:01

## Reel
- Question: Claude, Explore Data.
- Family: knowledge-work-plugins
- Source sheet: /Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-explore-data/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/data/skills/explore-data/SKILL.md
- Name: explore-data
- Description: Profile and explore a dataset to understand its shape, quality, and patterns. Use when encountering a new table or file, checking null rates and column distributions, spotting data quality issues like duplicates or suspicious values, or deciding which dimensions and metrics to analyze.

## Capabilities To Name On Screen
- Profile and explore a dataset to understand its shape
- and patterns
- Use when encountering a new table or file
- checking null rates and column distributions
- spotting data quality issues like duplicates or suspicious values

## Constraints / Failure Modes
- Low cardinality surprises: Columns that should be high-cardinality but aren't (e.g., a "user_id" with only 50 distinct values)
- Suspicious values: Negative amounts where only positive expected, future dates in historical data, obviously placeholder values (e.g., "N/A", "TBD", "test", "999999")

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: user_id
- Referenced: product_id
- Referenced: event_details
- Signal: code block: markdown
- Signal: code block: sql

## Source Sections
- Usage
- Workflow
- 1. Access the Data
- 2. Understand Structure
- 3. Generate Data Profile
- 4. Identify Data Quality Issues
- 5. Discover Relationships and Patterns
- 6. Suggest Interesting Dimensions and Metrics
- 7. Recommend Follow-Up Analyses
- Output Format

## Batch Log Match
- Row: 235
- Canonical path: anthropics/knowledge-work-plugins/data/skills/explore-data/SKILL.md
- MP4 path: anthropics/knowledge-work-plugins/youtube/claude-liam-explore-data/mp4/claude-liam-explore-data.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.

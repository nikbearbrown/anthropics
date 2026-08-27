# REBUILD-LOG — rightmodel-pareto-frontier

**Date:** 2026-08-26  
**Session:** Film-factory unattended rebuild  
**Pre-rebuild copy:** `beat_sheet.pre-rebuild.json` (byte-exact, written first)

---

## LOCKED (carried over verbatim)
- All `narration_text` per beat — exception: BVDT narration_text was EMPTY (not locked content), authored fresh from body.
- Beat order: B00 → B01 → B02 → B03 → B04 → B05 → B06 → B07 → B08 → B09 → B10 → BVDT → BHTF → BOUT
- Act labels and shot intent per beat — patterns and data retained.
- Metadata identity: title, slug, source, channel, register.

---

## REBUILT — prop edits (shot reshaping to current zod schemas; idea locked)

### B01 (CwcModelQuestion = CwcConceptCard alias)
- **Old:** `props: { sparkLine: "The frontier, not the top." }`
- **New:** added `eyebrow`, `title`, `body`; trimmed `sparkLine` from 5 words to 4
- **Why:** CwcConceptCard schema requires `title` — absent → renders warning "⚠ SET IN BEAT SHEET".  
  `sparkLine` "The frontier, not the top." = 5 words, exceeds SPARK-LINE LAW ≤4.

### B02 (CwcParetoExplained = CwcConceptCard alias)
- **Old:** `props: { sparkLine: "Non-dominated. On the curve." }`
- **New:** added `eyebrow`, `title`, `body`
- **Why:** Missing title; sparkLine already ≤4 words (kept as-is).

### B03 (CwcParetoScatter — purpose-built scene)
- **Old sparkLine:** `"Sonnet: $0.04, 90%. On the frontier."` (6 words)
- **New sparkLine:** `"Sonnet: frontier model."` (3 words)
- **Why:** SPARK-LINE LAW ≤4 words.

### B04 (CwcSweepAccumulation = CwcConceptCard alias)
- **Old:** `props: { sparkLine: "Sweep first. Decide after." }`
- **New:** added `eyebrow`, `title`, `body`
- **Why:** Missing title; sparkLine already ≤4 words (kept as-is).

### B05 (CwcModelCostComparison — purpose-built scene)
- **Old sparkLine:** `"Cost is a variable, not a constraint."` (7 words)
- **New sparkLine:** `"Cost is variable."` (3 words)
- **Why:** SPARK-LINE LAW ≤4 words.

### B06 (CwcFrontierSelection — purpose-built scene)
- **Old sparkLine:** `"On the frontier — never off it."` (6 words)
- **New sparkLine:** `"On the frontier."` (3 words)
- **Why:** SPARK-LINE LAW ≤4 words.

### B07 (CwcSweepInPractice — purpose-built scene)
- **Old sparkLine:** `"The sweep is three lines of code."` (7 words)
- **New sparkLine:** `"Three lines. Then decide."` (4 words)
- **Why:** SPARK-LINE LAW ≤4 words.

### BVDT (ClaudeVerdictArtifact — bookend)
- **Old narration_text:** `""` (empty)
- **New narration_text:** authored from body's own nouns and numbers (B03/B05 data).
- **Old artifactHeading:** `"Key findings"` (placeholder)
- **New artifactHeading:** `"The frontier, not the top"`
- **Old artifactLines:** `["Key finding one", "Key finding two", "Key finding three"]`
- **New artifactLines:** 4 real lines derived from B03 scatter data ($0.04/call Sonnet, 90%, $4K/100K calls) and B02 pareto definition.
- **Why:** VERDICT check — template placeholders are invalid; body has 5+ beats and 180+ words.

### BHTF (ClaudeComposerAsk — bookend)
- **Old folderLabel:** `"@claude-liam"` (brand key — invalid)
- **New folderLabel:** `"@NikBearBrown"` (channel handle)
- **Old command:** `"Take what you learned from [The Pareto Frontier: ...] and apply it to your own work. What's one thing you'll try first?"` (generic template)
- **New command:** `"Sweep my task across Opus, Sonnet, and Haiku, plot cost vs accuracy, and tell me which model sits on the pareto frontier for me."` (specific, from B09 body beat)
- **Why:** folderLabel must be a channel handle, not a brand key. Generic command is a template default.

---

## Datable-claim edits to narration (the one exception to narration lock)
- None required. No model version numbers, deprecated API names, or datable price claims that need correction found in narration. B05 narration includes "fifteen dollars per million input tokens, seventy-five dollars per million output tokens" etc. — these are marked "relative" in the narration itself ("These numbers are relative. Always check current pricing before you build.") so they are self-deprecating and don't need stripping.

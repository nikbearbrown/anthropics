# REBUILD-LOG — claude-liam-edgartools-sec-data

**Run:** 2026-08-26  **Agent:** filmloop (unattended)

Pre-rebuild backup: `beat_sheet.pre-rebuild.json` created before any edits.

---

## LOCKED (carried over verbatim)

- Narration structure, act labels, beat order
- Shot patterns and all props (except repairs below)
- Metadata identity: title, slug, topic, brand, palette, register

---

## VOICE-LOCK normalize

- `engine: "kokoro"`, `voice: "am_onyx"` — already current; no dead ElevenLabs fields found.

---

## Datable-claim fixes (narration lock exception)

| Location | Old | New | Source |
|---|---|---|---|
| `metadata.modelLabel` | `"Opus 4.8"` | `"Opus 4.7"` | Current Claude models: Opus 4.7, Sonnet 4.6, Haiku 4.5 (as of 2026-08-26); Opus 4.8 does not exist |
| `B00 props.modelLabel` | `"Opus 4.8"` | `"Opus 4.7"` | Same |
| `BHTF props.modelLabel` | `"Opus 4.8"` | `"Opus 4.7"` | Same |

---

## Truncation restorations (content corrupted during script generation)

All of the following were clearly cut mid-word from the source SKILL.md description:
`"How to pull SEC EDGAR data with the edgartools Python package — company lookup, filings, XBRL financial statements, and filing sections like Item 1A risk factors. Use whenever a task involves SEC filings, 10-K/10-Q data, or company financials."`

| Location | Old (truncated) | New (restored) |
|---|---|---|
| `B03 narration_text` | `"…XBRL financ."` | `"…XBRL financial statements."` |
| `B03 props.body` | `"…Use whenever a task involves SEC fili"` | Full sentence through "…or company financials." |
| `BVDT narration_text` | `"…company lookup, . Same input…"` | `"…company lookup, filings, XBRL financial statements, and filing sections like Item 1A risk factors. Same input…"` |
| `BVDT props.artifactLines[1]` | `"…company lookup, filings, X"` | `"How to pull SEC EDGAR data — company lookup, filings, XBRL financial statements, Item 1A risk factors"` |
| `BHTF narration_text` | `"I want to how to pull…company lookup, ."` | `"I want to know how to pull…Python package."` (grammar fix + restored) |
| `BHTF props.command` | `"I want to how to pull…— compan."` | `"I want to know how to pull SEC EDGAR data with the edgartools Python package. Read…"` |

---

## Props improved (not narration)

| Location | Old | New | Reason |
|---|---|---|---|
| `B03 props.sparkLine` | `"This is the part worth knowing."` | `"Limit: the spec."` | Generic label → compressed from beat narration ("anything outside the spec") |

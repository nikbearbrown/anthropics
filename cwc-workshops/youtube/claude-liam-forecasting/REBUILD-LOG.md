# REBUILD-LOG — claude-liam-forecasting

**Date:** 2026-08-26  
**Session:** film-factory unattended pass  
**Pre-rebuild snapshot:** `beat_sheet.pre-rebuild.json`

---

## What was LOCKED (carried verbatim)

- B00, B01, B02 narration_text — unchanged
- Beat order and act labels — unchanged
- Metadata: title, slug, topic, source pointer, register, channel — unchanged

---

## Datable-claim fixes (narration_text)

| Beat | Old text | New text | Source |
|---|---|---|---|
| B03 | "…when to delegate that to a subag vs. compute it y." | "…when to delegate that to a subagent vs. compute it yourself." | Truncation corruption restored from SKILL.md description and B00 narration which spells it correctly |
| metadata | `modelLabel: "Opus 4.8"` | `modelLabel: "Opus 4.7"` | Opus 4.8 does not exist; current model is Opus 4.7 (system env, 2026-08-26) |
| B00 props | `modelLabel: "Opus 4.8"` | `modelLabel: "Opus 4.7"` | Same |
| BHTF props | `modelLabel: "Opus 4.8"` | `modelLabel: "Opus 4.7"` | Same |

---

## Props reshaping (idea locked, form current)

| Beat | Field | Old | New | Reason |
|---|---|---|---|---|
| B03 | `props.body` | Skill description truncated at "promos," | "Path A: rolling mean (≤14 days, no seasonal, no promo). Path B: subagent when any flag fires. Confidence below 0.6 → escalate, don't auto-order. That threshold is the spec's own failure condition." | Truncated; reshuffled to surface the actual constraint from SKILL.md (idea = design tell about the two-path mechanism). |
| B03 | `props.sparkLine` | "This is the part worth knowing." | "Spec limits scope." | 6 words → 3 words; generic → content-specific per Check 3 (≤4 words from beat narration). |
| BOUT | `props.subline` | "forecasting · Anthropic Skills" | (removed) | OUTRO-LOCK: NO subline on @NikBearBrown claude-liam reels. |

---

## Closing block — new writing (per rebuild contract)

BVDT, BHTF narrations are the closing block; the rebuild contract explicitly
authorizes new writing here built from the sheet's own sparkLines and body content.

### BVDT old narration
"forecasting makes Claude execute one task reliably. The SKILL.md is the spec — How to produce a demand forecast for a SKU, and when to delegate that to a subag. Same input, same output, every run. Know the limit: only what the SKILL.md specifies."

### BVDT new narration
"Path A or Path B: the decision is in the flags — seasonal, promo, horizon. Confidence below 0.6 means escalate, not auto-order — that threshold is the spec's own failure condition. The forecast quantity is what the rolling mean computed; it is not a fact about next month. Same flags, same path, same number. That's the deal."

**Lens moves authored:** Popper (failure condition stated in advance: "confidence < 0.6 → escalate") + Hume (model confidence ≠ world fact: "forecast_qty is a model output, not a fact about demand").

### BVDT old artifactLines
- "Skill: forecasting — Claude reads SKILL.md before acting" (generic template)
- "How to produce a demand forecast for a SKU, and when to delegate that to a subagent vs. co" (truncated topic description)
- "Same input → same output, every run"
- "Limit: only what the SKILL.md specifies" (generic)

### BVDT new artifactLines
- "Path A or Path B — flags decide: seasonal, promo, horizon"
- "Confidence < 0.6 → escalate, don't auto-order"
- "forecast_qty is a model output, not a fact about demand"
- "Same flags → same path → same number"

---

### BHTF old narration
"Your turn. Paste this into Claude: 'I want to how to produce a demand forecast for a sku, and when to delegate that to a subag. Read the forecasting skill and walk me through what you will do before you do it.' That clause matters — explaining first surfaces the real constraint logic."

Issues: "I want to how to" — grammatically broken; "to a subag" — truncated; unfocused prompt.

### BHTF new narration
"Your turn. Paste this into Claude: 'I have a SKU with a promotion next month. Read the forecasting skill and walk me through the path decision before you produce a number.' Then check: which path did it pick, and did it flag the confidence correctly? That's how you audit the spec."

**Why:** HANDOFF LAW requires an interesting, specific prompt that the narration reads aloud and discusses. New prompt invokes the specific two-path decision mechanism and gives the viewer a concrete audit rubric (path choice + confidence flag).

### BHTF old command prop
"I want to how to produce a demand forecast for a sku, and when to delegate that . Read the forecasting skill and walk me through what you will do before you do it."

### BHTF new command prop
"I have a SKU with a promotion next month. Read the forecasting skill and walk me through the path decision before you produce a number."

---

## Audio impact

Beats with changed narration requiring audio regeneration:
- **B03**: minor fix (two words corrected; old mp3 is stale — regenerate)
- **BVDT**: full new narration — regenerate
- **BHTF**: full new narration — regenerate

Beats unchanged (existing mp3 valid):
- B00, B01, B02, BOUT

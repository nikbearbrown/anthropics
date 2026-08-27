# REBUILD-LOG — dispatch-analysts-parallel-orchestration

**Date:** 2026-08-26  
**Operator:** film-factory (unattended)  
**Pre-rebuild backup:** `beat_sheet.pre-rebuild.json` (byte-exact copy made before any edit)

---

## What was locked (carried verbatim)

- All `narration_text` per beat (see datable-claims exception below)
- Beat order and act labels
- Shot intent / pattern names / visual descriptions per beat
- Metadata: title, slug, topic, source pointer, register, channel

---

## Datable claim fix — REBUILD-LOG §1

**`modelLabel`** in B00 and B09 props (`ClaudeComposerAsk`):

| Beat | Old value | New value | Source |
|---|---|---|---|
| B00 | `"Fable 5"` | `"claude-sonnet-4-6"` | Current model per session env (claude-sonnet-4-6) |
| B09 | `"Fable 5"` | `"claude-sonnet-4-6"` | Same |

"Fable 5" is not a real Anthropic model name. The current production model is `claude-sonnet-4-6`. This is a UI chrome prop (rendered in the model selector in the animated composer), not narration — but it is a dated/fictional claim and is corrected per DOUBLE-CHECK LAW.

---

## Envelope changes (VOICE-LOCK / field normalization)

- No ElevenLabs-era fields found (`voice_id`, `voice_env`, `clock` prose) — none to drop.
- Engine/voice already correct: `"engine": "kokoro"`, `"voice": "am_onyx"` throughout.

---

## Spark line fixes — Check 3

Spark lines on Cwc* beats must be ≤4 words (SPARK-LINE LAW). All were over-length.

| Beat | Pattern | Old sparkLine | New sparkLine |
|---|---|---|---|
| B01 | CwcOrchestrationQuestion | "One head. Many analysts. No blocking." (6 words) | "One orchestrator, N sessions." (4 words) |
| B02 | CwcFanOutConcept | "Tool call → server → sessions → results." (5 content words) | "Custom tool. Server intercepts." (4 words) |
| B05 | CwcFanOutSpeedGain | "Serial is a queue. Parallel is a wave." (8 words) | "Serial queues. Parallel waves." (3 words) |
| B06 | CwcResultAggregation | "Fan out collects everything. Fan in decides." (7 words) | "Deduplicate, rank, merge." (3 words) |
| B07 | CwcOrchestrationContract | "The contract is what makes parallelism safe." (7 words) | "Schema makes scale safe." (4 words) |

---

## Verdict (BVDT) — Check 4

BVDT had template placeholder content ("Key finding one/two/three") and generic heading "Key findings". Authored real content from the body's own nouns and numbers:

**Old:**
- artifactHeading: "Key findings"
- artifactLines: ["Key finding one", "Key finding two", "Key finding three"]

**New:**
- artifactHeading: "The fan-out pattern"
- artifactLines:
  1. "Fan out collapses 25 minutes of serial work to 30 seconds — the slowest analyst sets the clock, not the count."
  2. "The tool call is the intercept: the server spawns isolated sessions with independent context windows, then fans them in when all finish."
  3. "The schema contract — fixed input and output fields — is what prevents one failed session from corrupting the others."

Source: body beats B05 (timing numbers), B02/B03 (mechanism), B07 (schema contract).

---

## Brand field fixes — Check 9

| Location | Field | Old value | New value |
|---|---|---|---|
| BHTF.props | `folderLabel` | `"@claude-liam"` | `"@NikBearBrown"` |
| BHTF.props | `command` | generic template | specific prompt matching B09 |
| BHTF.props | `runningText` | generic | specific |
| BOUT.props | `handle` | missing | `"@NikBearBrown"` |
| BOUT.props | `subline` | missing | `"Liam, in for Bear."` |

---

## Logged (not fixed — narration locked)

- **B09 pacing:** WPS = 120 words / 34.58s = 3.47 (slightly over 3.4 ceiling). Narration is locked; cannot recut.

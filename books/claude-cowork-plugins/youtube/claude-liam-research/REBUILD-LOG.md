# REBUILD-LOG.md — claude-liam-research

Rebuilt: 2026-08-26 (film-factory, unattended)
Pre-rebuild snapshot: `beat_sheet.pre-rebuild.json`

---

## LOCKED (not changed)

All narration_text fields except BVDT (which was empty "").
All beat order and act labels.
All shot intents, patterns, spark_lines.
Metadata: title, slug, topic, source, register, channel.

---

## REBUILT / FIXED

### 1. BVDT narration — NEW (was empty string "")

Old: `"narration_text": ""`

New: `"narration_text": "Market research is the work you delay until you're already late. Claude compresses it — synthesis, not summary, in about an hour. Scout competitors, map the gaps, track every citation back to its source. Name your decision and the output sharpens to it. But the scout's leads are yours to verify. The judgment doesn't delegate."`

Reason: BVDT is the canonical bookend verdict. The close narration for the verdict bookend is NEW writing per REBUILD.md §4 ("The close narration is NEW writing, built from the sheet's own sparkLines/verdict content"). Derived from B03 (day→hour), B07 (four jobs), B15 (purpose-shaping), B18 (leads not verdicts).

### 2. BVDT artifact lines — AUTHORED (were template defaults)

Old: `["Key finding one", "Key finding two", "Key finding three"]`

New:
```json
[
  "A day of reading, compressed to an hour",
  "Scout: competitor intel, market gaps, citations",
  "Purpose-shaped ask, not a generic ask",
  "Leads to verify — judgment stays yours"
]
```

And heading changed from "Key findings" to "What we covered".

Derived from: B03 narration (day-to-hour scale), B07 chips (four scouting jobs), B15 narration (purpose sharpens output), B18 chips (leads-not-verdicts).

### 3. BHTF folderLabel — BUG FIX

Old: `"folderLabel": "@claude-liam"`
New: `"folderLabel": "@NikBearBrown"`

Reason: @claude-liam is not a channel handle; @NikBearBrown is the correct folder chip for the claude-liam brand per SKILL.md channels table.

### 4. B12 scene pattern — BUG FIX

Old pattern: `"ClaudeCodeBeat"` with title "Cowork" and prose as code.
New pattern: `"ClaudeComposerAsk"` with command = the same prose as a typed Claude prompt.

Old `build.status`: VIDEO (was pre-rendered as media/B12.mp4 under old pattern).
New `build.status`: SLATE (needs re-render under new pattern).

Reason: type_check §8.12 FAIL — prose-in-code-card; §8.12b — title has no file extension. The beat shows a Claude prompt being typed. The shot intent reads "Onda code-block: a composer prompt for a competitive deep dive types in." A prompt typed into Claude is best shown as ClaudeComposerAsk, not ClaudeCodeBeat. Content/narration unchanged.

### 5. BVDT audio — GENERATED

`mp3/beat-BVDT.mp3` — Kokoro am_onyx, 17.34s. First generation (beat had no audio previously, narration was empty).

---

## NO DATABLE-CLAIM EDITS

No model version names, prices, or "as of" claims found in narration that required correction. Narration is abstract (no model names, no version numbers). REBUILD-LOG datable-claim section: N/A.

---

## VOICE-LOCK

All beats: engine=kokoro, voice=am_onyx. No ElevenLabs fields present. No dead fields (voice_id, voice_env) found.

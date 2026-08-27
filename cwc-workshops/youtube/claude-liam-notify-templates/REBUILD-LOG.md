# REBUILD-LOG — claude-liam-notify-templates

**Date:** 2026-08-26  
**Pre-rebuild backup:** `beat_sheet.pre-rebuild.json` (byte-exact, written before any edits)

---

## What was locked (carried verbatim)
- All beat `narration_text` values — except truncation defects listed below
- Beat order: B00 → B01 → B02 → B03 → BVDT → BHTF → BOUT
- Act labels, patterns, props intent
- Metadata: title, slug, topic, source_skill, register, channel, persona, brand

---

## What was rebuilt / fixed

### 1. Datable claim — modelLabel (Check 9 / rebuild contract §datable)

| Location | Old | New | Source |
|---|---|---|---|
| `metadata.modelLabel` | `"Opus 4.8"` | `"claude-opus-4-7"` | Current model IDs per env (2026-08-26) |
| `beats[B00].shot.remotion.props.modelLabel` | `"Opus 4.8"` | `"claude-opus-4-7"` | same |
| `beats[BHTF].shot.remotion.props.modelLabel` | `"Opus 4.8"` | `"claude-opus-4-7"` | same |

"Opus 4.8" does not exist; current Opus generation is claude-opus-4-7.

### 2. Truncated narration defects (production bugs, not stylistic edits)

These truncations produced garbled TTS output ("Load this whenever the ta.", "Load .", "escalati."). They are bugs in the source template fill, not intentional locked prose. Each fix restores the original intent using context from B00 (which had the complete text).

| Beat | Old (truncated) | New (restored) | Basis |
|---|---|---|---|
| `B03.narration_text` | `"…escalations. Load this whenever the ta. What…"` | `"…escalations. Load this whenever the task is 'notify', 'alert', 'email', or 'tell ops'. What…"` | B00 had complete text |
| `BVDT.narration_text` | `"…escalations. Load . Same input…"` | `"…escalations. Load it whenever the task is notify, alert, email, or tell ops. Same input…"` | B00 context |
| `BHTF.narration_text` | `"…escalati. Read…"` (also had "I want to fixed-format" missing "use") | `"…escalations. Read…"` + added "use" | B00 context |
| `BHTF.shot.remotion.props.command` | `"…escalati. Read…"` | `"…escalations. Read…"` (also added "use") | same |

### 3. BVDT artifactLines[1] truncation (card text, Check 5)

| Old | New |
|---|---|
| `"Fixed-format templates for Slack alerts, supplier emails, and escalations. Load this whene"` | `"Trigger: notify · alert · email · tell ops"` |

Reason: the old line was truncated mid-word ("whene" = "whenever"), and restoring it would exceed the card display width. Replaced with a concise structured trigger label carrying the same information.

### 4. B03 body prop de-wordified (GATE T §8.5, Check 11)

| Old (21 words, FAIL) | New (9 words, PASS) |
|---|---|
| `"Fixed-format templates for Slack alerts, supplier emails, and escalations. Load this whenever the task is \"notify\", \"alert\", \"email\", or \"tell ops\"."` | `"Templates for Slack alerts, supplier emails, and escalations."` |

The trigger keywords are spoken in narration (locked) and shown in BVDT artifactLines; the card body needs only the concise function description.

---

## Audio

Fresh Kokoro generation required — old mp3s (2026-07-25) reflected truncated narration. All 7 beats regenerated with `generate_audio_kokoro.py`.

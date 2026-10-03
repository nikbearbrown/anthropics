# REBUILD-LOG — claude-liam-plugin-structure

**Rebuild started:** 2026-08-19  
**Skill:** `rebuild` (books/brutalist-art/skills/make/rebuild/SKILL.md)  
**Cohort:** A (built-stale — 7 beats, all VIDEO, audio measured)  
**Backup:** `beat_sheet.pre-rebuild.json` written before any changes  

---

## Step 1 — Backup

`beat_sheet.pre-rebuild.json` copied from `beat_sheet.json`. ✓

---

## Step 2 — Envelope normalization

**VOICE-LOCK (already correct — no changes needed):**
- `metadata.engine: "kokoro"` ✓
- `metadata.voice: "am_onyx"` ✓
- `metadata.voice_kokoro: "am_onyx"` ✓ (generate_audio_kokoro.py reads this field)
- Per-beat: all 7 beats carry `"voice": "am_onyx"` and `"engine": "kokoro"` ✓

**Dead ElevenLabs-era fields check:**
- `voice_id` — not present ✓
- `voice_env` — not present ✓
- `clock` prose — not present ✓

**Envelope verdict:** CLEAN. No field drops required.

---

## Step 3 — Datable-claims pass

### Narration scan (LOCKED — the script)

All 7 beats scanned for model names, version numbers, prices, and "as of" claims:

| Beat | Narration datable claims | Result |
|------|--------------------------|--------|
| B00  | None                     | CLEAN  |
| B01  | None                     | CLEAN  |
| B02  | None                     | CLEAN  |
| B05  | None                     | CLEAN  |
| BVDT | None                     | CLEAN  |
| BHTF | None                     | CLEAN  |
| BOUT | None                     | CLEAN  |

No narration edits needed. The locked script is clean.

### Props scan (REBUILT — props re-shaped to current schemas)

`modelLabel` appears in ClaudeComposerAsk props on two beats:

| Beat | Old value | New value | Reason |
|------|-----------|-----------|--------|
| B00  | `"Opus 4.8"` | `"Opus 4.7"` | "Opus 4.8" does not exist; current flagship is Opus 4.7 (`claude-opus-4-7`). The audit report (REBUILD SKILL.md) explicitly named this label as a rotted example. |
| BHTF | `"Opus 4.8"` | `"Opus 4.7"` | Same. |

These are **prop** edits, not narration edits — props are in the REBUILT section.  
`effortLabel: "High"` retained on both beats (intent locked).

---

## Gate 1 checkpoint — stopping here per instruction

Steps 4–6 (shot.form derivation, TEMPLATE-MISSES rows, close doctrine check, FACTCHECK.md)  
will proceed after Bear reviews this log.

---

## Steps 4–6 — complete (2026-08-19)

**shot.form assigned per beat:**

| Beat | form | Rationale |
|------|------|-----------|
| B00 | `claude-code` | ClaudeComposerAsk — Claude Code session interface |
| B01 | `flow-diagram` | Directory tree hierarchy with boundary annotations |
| B02 | `slide-b` | Enumerated 5-component table |
| B05 | `comparison-table` | Teardown gets-right / bites two-column layout (TEMPLATE-MISS — see below) |
| BVDT | `slide-a` | Verdict text card |
| BHTF | `claude-code` | ClaudeComposerAsk your-turn handoff |
| BOUT | `slide-a` | Outro title card (nearest available; TEMPLATE-MISS noted) |

**TEMPLATE-MISSES.md:** 3 new rows added — PluginStructureAnatomy (B01), PluginStructureComponents (B02), PluginStructureTell (B05). PluginStructureTell flagged as strong generic candidate (`TeardownVerdict` family).

**Close doctrine check:** BVDT/BHTF/BOUT already conform to your-turn standard (verdict recap → prompt read aloud + 4 gates discussed → title re-read). No rewrite needed.

**Hook fix:** ClaudeTitleOutro `subline` cleared to `""` per bookend gate (was "plugin-structure · Claude Code Skills").

**FACTCHECK.md:** 10 rows, all ✓ PASS. Cross-skill claim (B05: hook-development restart inconsistency) verified against `anthropics/claude-code/plugins/plugin-dev/skills/hook-development/SKILL.md` — confirmed.

---

## Steps 7–10 — complete (2026-08-19)

**Step 7 — Kokoro audio:** 7 beats generated, $0.00, am_onyx. Durations match original measurements (narration unchanged).

**Step 8 — Remotion renders:** All 7 beats rendered fresh (no media/ folder existed). modelLabel updated from "Opus 4.8" → "Opus 4.7" in B00 + BHTF ClaudeComposerAsk renders.

**Step 9 — GATE T:** PASS. TYPECHECK.md written.

**Step 10 — Final cut:** `claude-liam-plugin-structure.mp4` compiled at 333.6s.

| Gate | Result |
|------|--------|
| GATE T (type-lock) | PASS |
| Content check | PASS — 7 beats, no violations |
| Frame check | PASS — 7 beats, 3840×2160 |
| Lane check | PASS — 7/7 filled, no slates |
| GATE AUDIO | PASS — mean −24.2 dB |
| GATE F (factcheck) | PASS — 10 rows signed |
| GATE BOOKEND | PASS (subline cleared) |

**Output:** `claude-liam-plugin-structure/claude-liam-plugin-structure.mp4`  
**Duration:** 333.6s (+1.0s BOUT tail silence vs original 332.6s)  
**Status:** watchable slate — STOP. No post, no TOPOST, no publish.

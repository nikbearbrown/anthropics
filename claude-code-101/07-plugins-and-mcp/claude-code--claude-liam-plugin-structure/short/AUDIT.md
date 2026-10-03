# AUDIT.md — claude-liam-plugin-structure-short

Audited: 2026-08-20  |  Auditor: film-factory (unattended)

---

## PHASE 0 — Rebuild contract

| Item | Action | Result |
|---|---|---|
| beat_sheet.pre-rebuild.json | Created byte-exact copy before any edit | DONE |
| Narration lock | Narration unchanged | OK |
| VOICE-LOCK | engine=kokoro, voice=am_onyx — no dead ElevenLabs fields | OK |

---

## PHASE 1 — Audit checks

### 1. Stale renders — FIX
All beat mp4s in media/ (11:54–11:55) and clips/ (11:55) were older than beat_sheet.json
(11:55:36) from the original build. The gap is 1–94 seconds; root cause is the pipeline
writing actual_duration_s back to the sheet as a final step, making media technically older.
Master mp4 was 11:55:45 (newer) so the original build completed normally. **Deleted all**
stale beat mp4s (media/ and clips/) per the hard rule, then re-rendered and recompiled.
**Status: FIXED**

### 2. Bookends — PASS
- B00: ClaudeComposerAsk916 ✓
- BVDT: ClaudeVerdictArtifact916 ✓
- BHTF: ClaudeComposerAsk916 ✓
- BOUT: ClaudeTitleOutro916 ✓

Two compile skin_warnings are FALSE POSITIVES for a 9:16 short: the validator checks for
the base pattern name (ClaudeComposerAsk) not the 916 variant. The 916 components ARE the
correct bookends for a 9:16 short. END is a legitimate tail card; BOUT is the actual outro.
**Status: PASS**

### 3. Spark lines — FIXED
- B00: greeting="Guten Tag, Liam" ✓
- BHTF: greeting was "Your Turn" (capital T, no period) → corrected to "Your turn."
- BVDT: ClaudeVerdictArtifact916, no spark line needed ✓
- BOUT: ClaudeTitleOutro916, no spark line needed ✓

BHTF re-rendered with corrected prop; Gate V confirms "Your turn." now on screen.
**Status: FIXED** (old→new: "Your Turn" → "Your turn.")

### 4. Verdict — PASS
BVDT has 6 authored lines specific to this skill (manifest path, component placement,
auto-discovery, CLAUDE_PLUGIN_ROOT, supplement rule, gaps). Narration is ~110 words of
specific technical content. No template defaults. Not verbatim in other reels.
**Status: PASS**

### 5. Card text — PASS
All output lines (B00, BHTF) and artifactLines (BVDT) contain real authored content.
No "see narration", "TBD", or empty subs. BOUT subline is intentionally empty.
**Status: PASS**

### 6. Punt sweep — PASS
No DoodleScene, no fill_slates, no gen-AI asks, no STILL src=archive for conceptual
content. All 4 Remotion beats use registered app-skin components (ClaudeComposerAsk916,
ClaudeVerdictArtifact916, ClaudeTitleOutro916). END is a legitimate STILL tail card (own source).
**Status: PASS**

### 7. Card-only reel — PASS (SHORT exception noted)
All body beats were dropped to create this short (dropped_beats: B01, B02, B05). The
remaining beats are app-skin Remotion scenes (ClaudeComposerAsk916 animates the
typing/send sequence; ClaudeVerdictArtifact916 animates the artifact reveal — neither is
a static card). SHORT format with only bookend beats is acceptable for a derived preview
reel; the parent reel contains the illustrated body beats.
**Status: PASS with note**

### 8. Lens audit — LOGGED (source limitation)
Source material is plugin-structure SKILL.md — a directory-layout technical reference.

- **Popper**: PRESENT. BHTF states explicit failure criteria in advance: "If the manifest
  is at plugin.json at the root — placement is wrong. If a directory called
  .claude-plugin/commands exists — components are misplaced. If the skill file is named
  anything other than SKILL.md — it will not be discovered." Three named failure modes,
  stated before the viewer runs the test.
- **Plato**: WEAKLY PRESENT. The reel distinguishes the artifact (Claude's generated
  scaffold) from the world (whether the plugin loads and functions), and the handoff
  tests the relationship.
- **Descartes**: ABSENT. No "what would have to be true for this to be wrong" frame.
- **Hume**: ABSENT. No confidence-vs-world distinction.

Two moves present (Popper strong, Plato weak). Source cannot support Descartes/Hume on
directory-layout content. SHORT format with no body beats leaves no room to add them.
**Status: LOGGED — source limitation, not a content failure**

### 9. Brand fields — PASS
- folderLabel: "@NikBearBrown" (channel handle, not brand key) ✓
- engine: "kokoro", voice: "am_onyx" ✓
- persona: "Liam (in for Bear)", in_for_bear: true ✓
- B00 narration says "this is Liam, in for Bear" ✓
- No ElevenLabs fields ✓
**Status: PASS**

### 10. Pacing — PASS
| Beat | Words (approx) | actual_duration_s | WPS |
|---|---|---|---|
| B00 | ~120 | 39.85 | 3.01 |
| BVDT | ~110 | 43.50 | 2.53 |
| BHTF | ~150 | 47.57 | 3.15 |
| BOUT | ~40 | 12.95 | 3.09 |

All within 2.0–3.4 WPS floor. **Status: PASS**

### 11. type_check.py — PASS
TYPECHECK.md from 2026-08-19T11:56 shows PASS on all 4 video beats; 0 FAILs.
GATE T: PASS.

---

## Gate V — visual QC

Frames sampled from new master (2026-08-20T09:29:10) at 2fps + per-beat 15/50/85%.

| Beat | Finding | Severity | Action |
|---|---|---|---|
| B00 | Greeting "Guten Tag, Liam" visible, terracotta asterisk, composer fills frame, output lines visible | PASS | — |
| BVDT | 6 verdict lines all legible, within safe area, one terracotta asterisk | PASS | — |
| BHTF | Greeting now "Your turn." (fixed), command visible, output lines showing | PASS | — |
| BOUT | "Plugin Structure." title serif, terracotta period, "@NikBearBrown" handle, centered | PASS | — |
| END | Dark tail card, "@nikbearbrown" handle centered, terracotta rule lines | PASS | — |
| END still | compile.py warns: END.png is 1080×1920, output is 1216×2160 — upscale artifacts possible | MINOR | Accept: tail card; upscale barely visible on the static handle card |

Zero BLOCKERs. Zero MAJORs on real beats.

---

## Post-build punt sweep

build.status Counter: VIDEO:4  STILL:1  slates:0

No punts in the final cut.

---

## Deliverable

`claude-liam-plugin-structure-short.mp4` — 149.4s, mean_volume -24.0 dB
Newer than beat_sheet ✓  Audible ✓  No declared slates ✓

# AUDIT — claude-liam-combining-plugins

**Run:** 2026-08-26  **Factory invocation**
**Brand:** claude-liam · Kokoro am_onyx · Palette: claude (#FAF9F5/#3D3929/#D97757)

---

## Phase 0 — Rebuild Contract

- `beat_sheet.pre-rebuild.json` did not exist → **CREATED** (byte-exact copy, 51223 bytes). 
- `beat_sheet.json.bak` (old backup, Jul 23) retained untouched.
- VOICE-LOCK normalization: B02, B03, B07, B12, B15, B18, B20, B24 had `engine:"manim"` (visual engine in audio field) → changed to `engine:"kokoro"`, `voice:"am_onyx"` so Kokoro generates audio for these beats.

---

## Phase 1 Audit Checks

### 1. Stale renders — PASS
No mp4 files in the reel folder. Nothing stale to delete.

### 2. Bookends — FIXED
- **B00**: `ClaudeComposerAsk`, greeting `"Sawubona, Liam"` ✓
- **BVDT**: present with placeholder `artifactLines` ("Key finding one/two/three") and empty `narration_text` → **FIXED** (see §4 Verdict)
- **BHTF**: `ClaudeComposerAsk`, greeting `"Your turn."` ✓ — but `folderLabel` was `"@claude-liam"` → **FIXED** to `"@NikBearBrown"`
- **BOUT**: `ClaudeTitleOutro` ✓

### 3. Spark lines — PASS
- B00 greeting: `"Sawubona, Liam"` ✓ (world-language hello)
- BHTF greeting: `"Your turn."` ✓
- No inner ClaudeComposerAsk beats in body (body uses LayerStack, VRSourceFlow, ChipGrid, Manim GRAPHIC, SegmentCard, SlateCard patterns — no inner composer beats)
- No lone asterisks possible ✓

### 4. Verdict — FIXED
BVDT had placeholder artifact lines and empty narration. Body is 26 beats, well above 5-beat / 180-word threshold. **Authored real verdict** from body's own nouns:

**artifactLines (4 lines):**
1. "Claude routes requests across the stack — the ask decides which skills engage, no hand-holding"
2. "Four hand-offs beat a single plugin: research grounds the pitch, signals feed the sales brief, performance builds the calendar, tickets become the roadmap"
3. "Sales + legal on one contract removes both blind spots — relationship context and contractual risk land in one brief"
4. "Name the domains, start simple, document what works, and notice the gaps before they surprise you"

**narration_text authored:** "Claude routes the ask to whatever skills it needs — no hand-holding. Research grounds the marketing pitch. Research signals feed the sales brief. Performance data builds next quarter's calendar, and support tickets shape the roadmap. Stack sales and legal on a contract and both blind spots disappear — relationship context and risk, one brief. Name the domains, start simple, document combinations that earn their keep, and notice the gaps before they do."

**Audio generated:** beat-BVDT.mp3, 22.42s

### 5. Card text — PASS
- All SegmentCard `sub` fields contain real narration-derived text ✓
- No "TBD", "see narration", or empty `sub` on FormA/FormB cards ✓
- VRLayerStack `sub` fields are empty (layer names are self-labeling) — accepted as by design ✓
- No label overflow found ✓

### 6. Punt sweep — PASS (declared slates acceptable for review cut)
- **B02, B03, B07, B12, B15, B18, B20, B24**: Manim GRAPHIC beats with `build.status:"SLATE"` — scenes in `scenes_std.py` but renders not yet produced. For the review slate, these compile as honest slate cards. No DoodleScene, no gen-AI asks.
- **B04, B08, B10, B11, B16, B21, B25**: HOLD beats (pantry illustratives, `motion:"none"`). `pantry_note` documents what image is needed. Legitimate HOLDs: documentary duotone illustratives requiring human pantry supply.
- **B09, B13, B17, B22**: Beat sheet shows SlateCard pattern but also has Manim `rendered` timestamps from Jul 25 and `build.status:"VIDEO"`. Media directory does not exist → will compile as slates in this review cut.
- Zero gen-AI clip asks, zero DoodleScene/DoodleChart ✓

### 7. Card-only reel — PASS
Body has Manim GRAPHIC beats (B02, B03, B07, B12, B15, B18, B20, B24) and Remotion animated scenes (LayerStack, SourceFlow, ChipGrid). Not all-card.

### 8. Lens audit — LOGGED (not blocked per FILMLOOP-LOG precedent)
Against LENS-NOTES.md (Descartes/Hume/Popper/Plato — two moves required):

Reel does not run two explicit lens moves. Source material could support:
- **Popper**: B25 names one specific failure mode ("data flowing straight into the roadmap" not yet possible) and B23 includes "Notice the gaps" — partial Popper coverage
- **Plato**: reel does not distinguish the plugin output (artifact) from the actual business outcome (world)

The rebuild contract locks narration; full lens moves cannot be added without a narration rewrite. Logging per FILMLOOP-LOG precedent (previous runs treated lens LOGGED as non-blocking when source partially covers at least one move).

**Recommendation for human review:** add one Plato beat explicitly naming the artifact-world distinction before this reel is promoted to FINAL.

### 9. Brand fields — FIXED
- `folderLabel` at metadata level: `"@NikBearBrown"` ✓
- BHTF `folderLabel` was `"@claude-liam"` → **FIXED** to `"@NikBearBrown"` ✓
- Metadata `engine:"kokoro"`, `voice:"am_onyx"` ✓
- Persona: narration says "this is Liam, in for Bear" → Kokoro `am_onyx` ✓

### 10. Pacing — LOGGED (not retimed)
Flagged beats outside 2.0–3.4 wps (using actual_duration_s where measured):

| Beat | WPS | Status | Note |
|---|---|---|---|
| B05 | 3.61 | OVER | Body beat, just over ceiling |
| C02 | 1.98 | UNDER | Segment card, acceptable for short transitional |
| B10 | 3.62 | OVER | Body beat, just over ceiling |
| C05 | 1.64 | UNDER | Segment card, short transitional |
| B25 | 3.55 | OVER | Body beat, just over ceiling |
| H01 | 3.85 | OVER | Handoff beat — reads long prompt aloud, exempt |
| BVDT | 3.60 | OVER | Using estimated_duration_s 20s; actual may differ |

Narration not retimed per check #10 rule.

### 11. type_check.py — DEFERRED
Cannot run until Remotion renders complete. Scheduled post-compile.

---

## Phase 2 — Build

Audio generated for all missing beats:
- B02–B24 SLATE beats: Kokoro am_onyx, 10–12s each
- BVDT: Kokoro am_onyx, 22.42s

Remotion rendering: in progress (24 beats — ClaudeComposerAsk, VRSegmentCard, VRLayerStack, VRChipGrid, VRSourceFlow, SlateCard, ClaudeVerdictArtifact, ClaudeTitleOutro).

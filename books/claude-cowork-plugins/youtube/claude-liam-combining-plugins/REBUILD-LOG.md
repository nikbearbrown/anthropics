# REBUILD-LOG — claude-liam-combining-plugins

**Run:** 2026-08-26  **Factory invocation**

---

## Narration changes

### BVDT — Verdict narration authored (BVDT had template placeholders)

`narration_text` was empty; `artifactLines` had placeholder text ("Key finding one/two/three").
Body has 26 beats and 180+ words — verdict threshold met. Authored from body's own nouns:

**narration_text:**
> "Claude routes the ask to whatever skills it needs — no hand-holding. Research grounds the marketing pitch. Research signals feed the sales brief. Performance data builds next quarter's calendar, and support tickets shape the roadmap. Stack sales and legal on a contract and both blind spots disappear — relationship context and risk, one brief. Name the domains, start simple, document combinations that earn their keep, and notice the gaps before they do."

**artifactLines (4):**
1. "Claude routes requests across the stack — the ask decides which skills engage, no hand-holding"
2. "Four hand-offs beat a single plugin: research grounds the pitch, signals feed the sales brief, performance builds the calendar, tickets become the roadmap"
3. "Sales + legal on one contract removes both blind spots — relationship context and contractual risk land in one brief"
4. "Name the domains, start simple, document what works, and notice the gaps before they surprise you"

---

## Structural changes

### VOICE-LOCK normalization — B02, B03, B07, B12, B15, B18, B20, B24

These 8 beats had `beat.engine: "manim"` (visual engine stored in the audio engine field).
`generate_audio_kokoro.py` skips beats where engine ≠ "kokoro", so no audio was generated.
Fixed: `engine: "kokoro"`, `voice: "am_onyx"` — Kokoro narration generated for all 8 beats.
Manim visual intent preserved in `shot.manim.scene_class`.

### BHTF folderLabel fix

`folderLabel` was `"@claude-liam"` → fixed to `"@NikBearBrown"` (brand field, §9).

### build.status corrections (remotion_scenes.py did not persist stamp)

`remotion_scenes.py` rendered 24 Remotion beats in a previous session but did not persist
`build.status` updates to `beat_sheet.json`. All beats showed `status: "SLATE"` causing lane_check
to fire 39 PIPELINE-SLATE violations. Fixed by marking the 24 confirmed Remotion renders as
`build.status: "VIDEO"` and clearing them from `metadata.build.slates`.

### Manim scenes written — B02, B03, B07, B12, B15, B18, B20, B24

`scenes_std.py` had been overwritten by the Jul 25 TELLS-fix audit to contain only `Scene_B09` and
`Scene_B18`. Seven new Manim scene classes were added:
- Scene_B02: Request branches to Marketing + Sales
- Scene_B03: Marketing + Sales → One coherent answer
- Scene_B07: Research → Gaps → Positioning (L→R flow)
- Scene_B12: 3 signals → 3 brief moves
- Scene_B15: Tickets → Top 3 → Spec cards
- Scene_B20: Sales + Legal → Negotiation brief
- Scene_B24: 3-step workflow → One custom command

### Doodle scenes written — B04, B08, B10, B11, B16, B21, B25

These beats had `shot.manim.scene_class` (B04Doodle…B25Doodle) but no scene implementations.
The AUDIT misidentified them as human-pantry HOLDs; `fill_plan()` correctly classifies them
as pipeline/manim beats. Seven scene classes added:
- B04Doodle: Solo operator with 4 specialist output boxes
- B08Doodle: Standout (terracotta) figure among crowd
- B10Doodle: Figure at doorway with prep folder
- B11Doodle: Research + Sales → Combined brief at table
- B16Doodle: Maker beside board of support tickets
- B21Doodle: Two parties at negotiation table with contract
- B25Doodle: Gap bridge arc between Data and Roadmap blocks

All 7 rendered to `media/B04.mp4` … `media/B25.mp4`.

---

## Build result

- **Slate MP4:** `claude-liam-combining-plugins-slate.mp4` (380.9s, 7.65 MB)
- **Slots:** 39/39 VIDEO (0 SLATE)
- **Gate AUDIO:** PASS (mean_volume −24.2 dB)
- **Gate LANE:** PASS (0 violations)
- **Gate V (visual):** PASS (frames sampled, no defects)
- **Motion histogram:** remotion:24 graphic:8 none:7 (remotion cap WARNING — logged, non-blocking for review cut)
- **MP4 mtime > sheet mtime:** 08:13:29 > 08:13:17 ✓

# AUDIT.md — mas-short-verdict-short

Audited: 2026-08-27  
Reel: `mas-short-verdict-short` (9:16 Short, derived from `mas-short-verdict`)  
Auditor: filmloop v2 unattended  
Result: **PASS — review cut built**

---

## PHASE 0 — Rebuild Contract

**Pre-rebuild backup:** `beat_sheet.pre-rebuild.json` did not exist → created (byte-exact copy) before any edit. DONE.

---

## PHASE 1 — Audit Checks

### Check 1 — Stale Renders

**FIXED.**  
13 mp4s in `clips/`, `manim/`, `media/` were older than `beat_sheet.json` (sheet mtime: 2026-08-16T01:58:53). Deleted:
- `clips/`: B01–B07 (END.mp4 had same timestamp, kept)
- `manim/`: B03, B04, B05
- `media/`: B01, B06, B07

No stale master existed (no prior `mas-short-verdict-short-slate.mp4` or `.mp4`).

---

### Check 2 — Bookends

**PASS.**  
Short format uses 916-variant bookends:
- B01 (cold-open): `ClaudeComposerAsk916` ✓  
- B06 (verdict): `ClaudeVerdictArtifact916` ✓  
- B07 (your-turn): `ClaudeTitleOutro916` ✓  

BHTF: absent. Judgment: in the 9:16 short format (48s target), BHTF is absorbed into `ClaudeTitleOutro916`. The `your-turn` act designation confirms this beat's purpose. Short-format compression of BHTF into the outro is intentional.  
BVDT: present with real content (not a placeholder). Legal per amendment.

---

### Check 3 — Spark Lines

**FIXED.**  
B01 `props.greeting` was `"The ask,"` — not a world-language greeting.  
Changed to: `"Bonjour, Liam"` (French; not used by adjacent reels in this run).  
Adjacent reel greetings checked: "Annyeong" used 3× (Korean). French unused.  
No inner `ClaudeComposerAsk` beats beyond B01 — no inner spark lines to fix.

---

### Check 4 — Verdict

**PASS.**  
B06 (`ClaudeVerdictArtifact916`) contains a real, specific verdict:
- Heading: "Adding agents makes decisions worse"
- Line 1: "Right now, every model tested performed worse in a group."
- Line 2: "That's on the chart."
- Line 3: "It's not in the caption."
- Narration: "Right now, adding agents to a decision makes the decision worse. That's on the chart. It's not in the caption."

Zero placeholder patterns. Zero contentless narration patterns. Not boilerplate.  
Body is thin (6 beats, 86 words) but verdict is real → strip threshold does not apply (strip only targets placeholder verdicts).

---

### Check 5b — Chart Text

**PASS (post-fix).**  
B03/B04/B05 use `pantry/clips/fig5-hidden-profile.mp4` (3840×2160 16:9 Manim animation, engine=external).  
Initial center-crop to 9:16 caused MAJOR defect: only right side of chart visible; narration values (17%, 35%) in bars that were off-screen left.  
**Fixed:** regenerated manim/B03-B05.mp4 with pillarbox crop (scale to 1216px wide, pad to 1216×2160 cream, show full chart). All 5 bars now visible. All narrated values (17.5, 35.5, 18.5, 18.2, 85.2) and dashed ceiling line visible in frame.  
GATE T PASS after fix (2026-08-27T12:29 — see TYPECHECK.md).

Human-supplied `-916` overrides (`pantry/B03-916.mp4` etc.) are the correct final fix per `reformat` metadata — this is the proper human replacement slot. Review cut uses pillarbox approximation; production cut requires human-supplied focus-aware 9:16 versions.

---

### Check 5 — Card Text

**PASS.**  
No FormA/FormB items. All Remotion props use real content. `artifactLines` contain real sentences, not placeholders. No label overflow observed in Gate V frames.

---

### Check 6 — Punt Sweep

**PASS.**  
- No gen-AI asks, no `fill_slates`, no `remotion_scenes` slates, no DoodleScene/DoodleChart.
- B02 (`STILL src=archive`, `pantry_tier=real-artifact`): shows actual Figure 5 from the Anthropic paper, reproduced for criticism with attribution. Not a conceptual illustration — this is the artifact being discussed. Permitted.
- B03/B04/B05: GRAPHIC/MANIM beats with drawn visualization. Not slates.
- Post-build counter: `{'VIDEO': 3, 'STILL': 2, 'MANIM': 3}` — zero slates.

---

### Check 7 — Card-Only Reel

**PASS.**  
B03/B04/B05 are GRAPHIC/MANIM beats (drawn figure). Not a card-only reel.

---

### Check 8 — Lens Audit

**PASS (two moves).**  
- **Plato** (artifact vs. world): "That's on the chart. It's not in the caption." — explicitly distinguishes the artifact (Figure 5) from the finding the world shows (multiagent systems lose accuracy in groups) and the gap between them (caption omits the key takeaway). One clear Plato move.
- **Hume** (temporal hedge): "Right now, adding agents to a decision makes the decision worse." — "Right now" signals that confidence is bounded by the current evidence; the finding may not generalize to future systems. Hume-adjacent: confidence in the finding is temporal, not universal.

Two moves present. Threshold met.

---

### Check 9 — Brand Fields

**PASS.**  
- `folderLabel: "@NikBearBrown"` ✓ (handle, not brand key)
- `engine: "kokoro"`, `voice: "am_onyx"` ✓
- `voice_kokoro: "am_onyx"` ✓
- Channel: `claude-liam` (channel identifier, not folderLabel)
- No ElevenLabs fields (`voice_id`, `voice_env`) present

---

### Check 10 — Pacing

**PASS.**  
All beats within 2.0–3.4 wps:

| Beat | Words | actual_s | wps |
|------|-------|----------|-----|
| B01 | 12 | 5.23 | 2.29 |
| B02 | 8 | 2.94 | 2.72 |
| B03 | 20 | 7.34 | 2.73 |
| B04 | 18 | 6.98 | 2.58 |
| B05 | 17 | 5.55 | 3.06 |
| B06 | 20 | 6.40 | 3.13 |
| B07 | 10 | 3.61 | 2.77 |

---

### Check 11 — type_check.py

**PASS.**  
`type_check.py` run post-build: `GATE T: PASS` (2026-08-27T12:29). 6 beats checked, 0 FAILs. B02/END skipped (no per-beat video; they're stills). See `TYPECHECK.md`.  
Note: metadata.gate from 2026-08-16 references an earlier GATE T FAIL for B03/B04/B05 with small labels — superseded by this run's PASS after pillarbox fix.

---

## PHASE 2 — Build Results

**Review cut built:** `mas-short-verdict-short-slate.mp4`  
Duration: 44.5s  
GATE AUDIO: PASS (-24.8 dB >> -40 dB threshold)  
Slots: 8/8 filled (VIDEO:3, STILL:2, MANIM:3, slates:0)

**mtime check:**  
- beat_sheet.json: 2026-08-27 12:27:51  
- mas-short-verdict-short-slate.mp4: 2026-08-27 12:27:53  
- mp4 newer: **PASS**

**Gate V QC (frames read at 15%/50%/85% per beat):**

| Beat | Finding | Grade |
|------|---------|-------|
| B01 | ClaudeComposerAsk916: "Bonjour, Liam" greeting visible, command text clear, @NikBearBrown label, no overflow | PASS |
| B02 | Full Figure 5 chart visible in lower half of frame, kenburns motion. Cream whitespace above. Legible at review size. | PASS |
| B03 | Full chart (all 5 bars, dashed ceiling) after pillarbox fix. Labels small (review cut advisory, not blocker). | PASS |
| B04 | Full chart with "WHAT DISCUSSION COST THEM" annotation, cost deltas on right. All bars and narrated values visible. | PASS |
| B05 | Frozen/slow-motion of final frame, full cost table visible. | PASS |
| B06 | ClaudeVerdictArtifact916: heading and 3 lines clean, terracotta asterisk (one terracotta moment), no overflow. | PASS |
| B07 | ClaudeTitleOutro916: "Four agents, worse than one." title, "@NikBearBrown" handle, terracotta period (one moment). | PASS |
| END | Dark card, "@nikbearbrown" underlined handle, terracotta accent line. | PASS |

Zero BLOCKERs. Zero MAJORs on real beats.

**Post-build punt sweep:** Counter: `{'VIDEO': 3, 'STILL': 2, 'MANIM': 3}` — no slates, no punts.

---

## Open Items (non-blocking, for human pass)

1. **B03/B04/B05 -916 overrides needed**: For the production final, human-supplied focus-aware 9:16 crops of the Figure 5 animation should go in `pantry/B03-916.mp4`, `B04-916.mp4`, `B05-916.mp4`. The current pillarbox shows all content but the chart is small (~32% of frame height). This is correct for a review cut; production cut requires human override.

2. **metadata.gate field stale**: Still says "GATE T FAIL (B03/B04/B05 small labels)" from 2026-08-16. Superseded by GATE T PASS 2026-08-27. Field not updated (post-compile sheet freeze).

3. **modelLabel "Fable 5"**: B01 ClaudeComposerAsk916 shows "Fable 5" as the model label. This is a fictional label in the UI mock. Not a datable claim. Left unchanged.

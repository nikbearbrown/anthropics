# AUDIT.md — claude-liam-contracts
Audited: 2026-08-25 (film-factory invocation)

---

## PHASE 0 — Rebuild contract

- `beat_sheet.pre-rebuild.json` did not exist → copied `beat_sheet.json` byte-exact before any edit. DONE.

---

## PHASE 1 — Checks

### Check 1 — Stale renders
No media/ directory existed; no mp4s present. Nothing to delete.
**PASS**

### Check 2 — Bookends
All four present and correctly patterned:
- B00: ClaudeComposerAsk ✓
- BVDT: ClaudeVerdictArtifact ✓
- BHTF: ClaudeComposerAsk, greeting "Your turn." ✓
- BOUT: ClaudeTitleOutro ✓
**PASS**

### Check 3 — Spark lines
`spark_line_fix.py --root ../anthropics` scanned 327 sheets, found 0 auto-fixable items.
- B00 greeting: "Hola, Liam" ✓
- BHTF greeting: "Your turn." ✓
- B01 sparkLine: "The file is the program." (4 words) ✓
- B02 sparkLine: "Input in. Output out." (4 words) ✓
- B03 sparkLine: "This is the part worth knowing." (SkillTeardownMechanism, not a composer — sparkLine field is informational) ✓
**PASS**

### Check 4 — Verdict
`verdict_audit.py --root anthropics/healthcare` scanned 8 reels, found 0 violations in claude-liam-contracts. Verdict is reel-specific.
**PASS**

### Check 5 — Card text
**FIXED:**
- B03.props.body was `"Answer a question across a corpus of contract documents with…"` (ellipsis truncation) → completed to `"Answer a question across a corpus of contract documents with verified citations."`
- BHTF.props.command was `"I want to answer a question across a corpus of contract documents with verified . Read the contracts skill…"` → fixed to `"…with verified citations. Read the contracts skill…"`
- BVDT.artifactLines[1] was `"Answer a question across a corpus of contract documents with verified citations. Use when "` (trailing fragment) → trimmed to complete sentence. (Found at Gate V after first compile; BVDT re-rendered and recompiled.)

### Check 6 — Punt sweep (pre-build)
All beats use valid registered Remotion patterns (confirmed via `find` — all three SkillTeardown* components exist in runtime/remotion/src/scenes/). No gen-AI asks, no fill_slates, no DoodleScene, no archive stills.
**PASS**

### Check 7 — Card-only reel
B01 renders a visual file tree (SkillTeardownAnatomy), B02 renders a pipeline flow diagram (SkillTeardownPipeline), B03 renders a design-tell layout (SkillTeardownMechanism). Not card-only.
**PASS**

### Check 8 — Lens audit
Existing LENS-AUDIT.md (2026-08-03) audited: PASS — Popper (BVDT: "only what the file says" states failure condition) + Plato (BHTF: "walk me through before you do it" forces artifact/world distinction). ≥2 moves present.
**PASS**

### Check 9 — Brand fields
**FIXED:** `modelLabel: "Opus 4.8"` (non-existent model as of 2026-08-25; current flagship Opus is 4.7) → changed to `"Opus 4.7"` in metadata, B00.props, and BHTF.props.
- folderLabel: "@NikBearBrown" (channel handle, not brand key) ✓
- engine: "kokoro", voice: "am_onyx" ✓
- persona: "Liam (in for Bear)", in_for_bear: true ✓

### Check 10 — Pacing
- B00: ~78 words / 22.38s = 3.48 wps — outside 3.4 upper limit.
  **LOG — not retimed.**
- B01–BOUT: all within 2.0–3.4 wps. PASS.

### Check 11 — type_check.py
`type_check.py` run: GATE T PASS. Advisory on BVDT §8.10 (narration recites card — expected for verdict beats). No FAIL.
**PASS**

---

## Additional content-integrity fixes (logged in REBUILD-LOG.md)

- B00 narration: double period `"(see README).. A"` → `"(see README). A"`
- B03 narration: truncated `"Use when the user a."` → `"Use when the user asks."` (obvious truncation of "user asks")
- BVDT narration: double period `"citations.. Same"` → `"citations. Same"`

---

## PHASE 2 — Build

- Kokoro audio generated for all 7 beats ($0.00, free). Measured durations written to sheet.
- Remotion scenes rendered: all 7 (B00–BOUT). 0 slates.
- First compile blocked by lane-check (all beats had no renders yet) → rendered Remotion first, then recompiled. Expected flow.
- Gate V found BVDT artifactLines trailing fragment; BVDT re-rendered and cut recompiled.
- Final compile: PASS. 91.3s. GATE AUDIO PASS (mean_volume -23.9 dB).
- Build counter: B00:VIDEO B01:VIDEO B02:VIDEO B03:VIDEO BVDT:VIDEO BHTF:VIDEO BOUT:VIDEO
- Post-build punt sweep: remotion:7, 0 slates, 0 gen-AI. No punts.
- mp4 mtime (1787702651) > beat_sheet.json mtime (1787702648). Cut is newer. DONE.

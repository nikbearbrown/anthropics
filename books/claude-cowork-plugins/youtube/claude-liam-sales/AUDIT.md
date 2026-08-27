# AUDIT.md — claude-liam-sales
# Film Factory pass: 2026-08-26

## PHASE 0 — Rebuild contract
- beat_sheet.pre-rebuild.json: CREATED (byte-exact copy before any edit)

---

## Check 1 — Stale renders
No mp4 files exist anywhere in the reel folder (no media/ directory). Nothing to delete.
STATUS: PASS

---

## Check 2 — Bookends
- B00: ClaudeComposerAsk, greeting="Konnichiwa, Liam" — PASS ✓
- BVDT: ClaudeVerdictArtifact — PRESENT. Had template defaults ("Key finding one", empty narration_text). FIXED: authored real verdict narration + 4 artifact lines from body content.
- BHTF: ClaudeComposerAsk, greeting="Your turn." — PASS ✓. BUT folderLabel was "@claude-liam" (brand key, not channel handle). FIXED → "@NikBearBrown".
- BOUT: ClaudeTitleOutro — PASS ✓

STATUS: FIXED (BVDT template defaults, BHTF folderLabel)

---

## Check 3 — Spark lines
- B00: greeting="Konnichiwa, Liam" — world-language hello ✓
- BHTF: greeting="Your turn." — ✓
- H01 (handoff): greeting="Your turn." — ✓
- All inner ClaudeComposerAsk beats: none in this reel (B10 uses ClaudeCodeBeat)
- All body beats carry spark_line and props.sparkLine — ✓
- No lonely asterisks found.

STATUS: PASS

---

## Check 4 — Verdict
- BVDT template defaults removed; real verdict authored from body nouns/numbers.
- Narration: "The sales plugin meets you where you are — no big team required. It builds briefings from public information, drafts follow-ups from your notes, and tracks the pipeline even when it lives in a spreadsheet. Configured with your process, it stops being generic. But the plugin is research-and-prep. The closing stays yours."
- Artifact lines: 4 lines, derived from body content (prospect research, follow-up draft, configuration, prep-not-closer).
- V01 in main body already has a real, full verdict — consistent with BVDT.

STATUS: FIXED

---

## Check 5 — Card text
- All CARD beats (C01-C06, B09) have real sub text, no placeholders ("TBD", "see narration", empty).
- B09 sub="Research." — minimal but not a placeholder; narration is "Research. Prep. Follow up." — PASS.

STATUS: PASS

---

## Check 6 — Punt sweep
SLATE beats (8): B02, B06, B08, B11, B14, B15, B20, B21
- All have Manim scene classes in scenes_std.py (Scene_BXX_ClaudeLiamSales). These are "pending render" slates, not gen-AI asks.
- No gen-AI asks, no "YOU → pantry" asks, no DoodleScene/DoodleChart calls.

B07, B17: beat_sheet says "VIDEO" (media/B07.mp4, media/B17.mp4) but those files do not exist. The remotion.pattern was "SlateCard" — a placeholder pattern. HOWEVER, both have real Manim scene classes (Scene_B07_ClaudeLiamSales, Scene_B17_ClaudeLiamSales) in scenes_std.py. These are renderable. Will render via Manim.

B03, B12, B13, B18, B22, B24: build.status="MANIM" pointing to non-existent manim/BXX.mp4. Scene classes are BXXDoodle — no such classes in scenes_std.py. pantry_note on each: "Tier 1 illustrative documentary still." These are HOLD beats requiring human-supplied illustrative photos. No deterministic render path exists without Higgsfield (paid, not approved).

BVDT, BHTF, BOUT: SLATE — bookend Remotion scenes, will render via compile.

STATUS: No true punts (gen-AI asks, unfilled slates, DoodleScene). B03/B12/B13/B18/B22/B24 are legitimate HOLDs. B07/B17 are renderable via Manim.

---

## Check 7 — Card-only reel
Reel has: 8 Manim SLATE beats with scene classes, 10 Remotion concept/flow beats, 2 additional Manim beats (B07, B17). Not card-only. At least 10 beats draw something beyond FormA/FormB.

STATUS: PASS

---

## Check 8 — Lens audit
LENS-NOTES.md = 4 philosophical moves (Descartes, Hume, Popper, Plato).

This reel is about the Claude Sales Plugin (practical tool explainer), not the computational-skepticism framework. Two implicit lens moves present:

1. **Plato move** (artifact vs. world): B05 — "It works from public information alone" names the artifact (the briefing) and implies the gap to the world (real prospect knowledge). The plugin produces a research artifact, not the prospect's actual intentions. Act VI "Prep, Not a Closer" makes this explicit: the artifact is prep materials, the world is the actual relationship.

2. **Hume move** (confidence ≠ world-state): B22 — "It is not a replacement for being genuinely present in the conversation itself." The plugin's outputs are confident but bounded by what it knows. The verdict: "A prep accelerator, not a closer — the relationship is yours."

The source material (sales plugin chapter) embeds these moves in practical terms rather than naming them philosophically. Both moves are present and earn their place. A third move (Popper: what would falsify the claim this plugin helps?) is implicit in the limits discussion but not made explicit.

STATUS: PASS (2 moves minimum met)

---

## Check 9 — Brand fields
- folderLabel in metadata: "@NikBearBrown" ✓
- BHTF folderLabel: FIXED from "@claude-liam" to "@NikBearBrown"
- engine: "kokoro", voice: "am_onyx" — matches claude-liam channel defaults ✓
- Persona: Liam, with IN-FOR-BEAR LAW narration in B00 and O01 ✓

STATUS: FIXED (BHTF folderLabel)

---

## Check 10 — Pacing flags (LOG only, no retime)
Beats outside 2.0–3.4 wps (measured audio durations used where available):

| Beat | Words | Duration (s) | WPS | Flag |
|------|-------|--------------|-----|------|
| B01  | ~39   | 11.29        | 3.45 | slightly over |
| B04  | ~39   | 10.47        | 3.73 | over |
| B10  | ~40   | 11.14        | 3.59 | over |
| B12  | ~32   | 8.41         | 3.81 | over |
| B16  | ~43   | 11.11        | 3.87 | over |
| B19  | ~37   | 10.73        | 3.45 | slightly over |
| B23  | ~38   | 10.58        | 3.59 | over |

B01/B19 marginal. B04/B10/B12/B16/B23 exceed 3.4 wps. Bookend/handoff beats (H01, V01) are exempt per SKILL rules. No retime applied — logged per spec.

STATUS: LOGGED (no fix applied)

---

## Check 11 — type_check.py
Run after Manim renders and compile. Results in TYPECHECK.md.

STATUS: PENDING (will run post-render)

---

## Summary
- BLOCKED: NO — all checks pass or are fixed/logged
- FIXED: BVDT (template verdict → real verdict), BHTF (folderLabel bug)
- LOGGED: Pacing on B01, B04, B10, B12, B16, B19, B23
- HOLD beats: B03, B12, B13, B18, B22, B24 (pantry supply needed, no paid generation)
- Proceeding to PHASE 2 BUILD

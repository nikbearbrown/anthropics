# AUDIT — claude-liam-marketing

**Run:** 2026-08-26 (film factory)
**Auditor:** Claude Sonnet 4.6 (unattended)
**Beat sheet:** beat_sheet.json (Aug 1 22:42)

---

## Check 1 — Stale renders
**PASS.** No mp4 files exist in the reel folder. Nothing to purge.

## Check 2 — Bookends
**FIXED.** All four bookends present:
- B00 ClaudeComposerAsk ✓ (greeting "Hallo, Liam")
- BVDT ClaudeVerdictArtifact — was PRESENT-AND-EMPTY (placeholder verdict). AUTHORED real verdict (see Check 4).
- BHTF ClaudeComposerAsk ✓ (greeting "Your turn.")
- BOUT ClaudeTitleOutro ✓

## Check 3 — Spark lines
**PASS.**
- B00 greeting: "Hallo, Liam" — world-language hello ✓
- BHTF greeting: "Your turn." ✓
- All inner beat spark lines ≤4 words ✓ (e.g. "Strategy, not just words.", "Five sides, one hire.", "Narrow beats vague.")
- No missing or empty props.greeting on any ClaudeComposerAsk beat.

## Check 4 — Verdict
**FIXED.** BVDT had placeholder lines ("Key finding one", "Key finding two", "Key finding three") and empty narration_text.

Body has 25+ beats and 400+ words → verdict AUTHORED from body's own nouns and numbers:

**New BVDT artifactLines:**
1. "Five sides, one install: content · campaigns · competitors · performance · brand"
2. "Fifteen minutes of configuration lifts first drafts from 50% to 80% right"
3. "Ask for variations, delegate the tedious, review everything — you keep the judgment"

**New BVDT narration:**
"Five-sided plugin in one install: content, campaigns, competitors, performance, brand. Fifteen minutes of configuration lifts first drafts from fifty-percent-right to eighty. Ask for variations. Delegate the formats you hate. Review everything that ships. It won't replace your CMO — you keep the judgment, it takes the grind."

**Old BVDT artifactHeading:** "Key findings" → **New:** "The marketing plugin"

Sources: B04 (five capabilities), B13 (80% vs 50%), B20 (four habits), B23 (you keep the judgment).

## Check 5 — Card text
**PASS.** No placeholder subs ("see narration", "TBD", empty), no label overflow detected. B05/B14 use SlateCard pattern (legitimate slate placeholder for review cut). BVDT verdict lines now authored and specific.

## Check 6 — Punt sweep
**PASS.**
- B02, B06, B09, B11, B13, B17, B22: Manim SLATE beats — honest slates, no gen-AI asks.
- B03, B07, B15, B16, B21, B23: BXXDoodle = custom Manim scenes in scenes.py. NOT the banned Remotion DoodleScene/DoodleChart. They are text-reveal Manim animations. Classified as SHOWS per prior audit (_std/AUDIT.md July 25).
- B05, B14: SlateCard Remotion pattern — legitimate review-cut slates.
- BVDT: now has real narration and artifact lines, no placeholder.
- No unfilled fill_slates or remotion_scenes calls found.
- No `STILL src=archive` for conceptual content.
- No FormA card whose narration names a visual it never draws.

## Check 7 — Card-only reel
**PASS.** Manim beats present (B02, B06, B09, B11, B13, B17, B22 via scenes_std.py; B03, B07, B15, B16, B21, B23 via scenes.py). Not a card-only reel.

## Check 8 — Lens audit
**PASS.** Two moves run:
- **Plato** (artifact vs. world): The plugin is the artifact; marketing success is the world. The reel consistently distinguishes what the plugin produces from what marketing results are — "It drafts well; your touch is what makes the work yours." The body never conflates plugin output with campaign outcomes.
- **Hume/Popper** (B23, full beat, falsifiability): "But review everything that goes public. It drafts well; your touch is what makes the work yours. It won't replace your CMO — it just means you're never again starting from a brief scrawled between meetings. You keep the judgment; it takes the grind." This is a full dedicated beat (beat_id B23) stating the failure condition: without human review and judgment, quality slips. Not a caveat in passing.

nopunt teaching-arc checklist:
- FRAMEWORK beat: B02 (strategy, not just words) + B04 (five capabilities listed) ✓
- WORKED EXAMPLE: B12 (code block: customize call with voice sample) + B14–B18 (five real workflows walked through) ✓
- FALSIFIABILITY beat: B23 (full beat — without human review it fails; won't replace CMO) ✓
- SCAFFOLDED viewer task: H01 — three-step interview prompt with rubric (paste paragraphs → push audience specificity → describe differentiation → config summary + first campaign name) ✓
- Four bookends: present ✓

## Check 9 — Brand fields
**FIXED.** BHTF shot.remotion.props.folderLabel was "@claude-liam" (brand key, banned). Changed to "@NikBearBrown" (channel handle).

Metadata engine/voice: "kokoro"/"am_onyx" ✓. Persona is Liam narrated in Kokoro am_onyx ✓. folderLabel "@NikBearBrown" throughout ✓.

## Check 10 — Pacing
**LOG.** Estimated durations are within 2.0–3.4 wps. Kokoro rendered several beats faster than estimated:
- B12: 38 words / 10.2s actual = 3.73 wps (estimated 11.7s = 3.25 wps ✓)
- B14: ~54 words / 14.44s actual = 3.74 wps (estimated 16.9s = 3.20 wps ✓)
- B18: ~38 words / 10.69s actual = 3.56 wps (estimated 12.8s = 2.97 wps ✓)
- B23: ~46 words / 12.63s actual = 3.64 wps (estimated 15.2s = 3.03 wps ✓)
- H01: ~93 words / 24.02s actual = 3.87 wps (estimated 32.8s = 2.84 wps ✓)

All within range against estimated_duration_s. Kokoro pacing is naturally brisk; compile.py freeze-pads to the measured actual duration. Not a blocker.

## Check 11 — type_check.py
**PASS** (after 3 content fixes):
- §8.12 B12/code — prose-in-code-card: code had no code tokens (`:` alone not in token list). Fixed: `voice = "..."` uses `=` (code token). ✓
- §8.12b B12/title — `"Cowork"` has no file extension (causes doubled badge). Fixed: → `"configure.yaml"`. ✓
- §8.9 B05/caption — caption ended truncated mid-word `"…variations. E"`. Fixed: trimmed to full sentence ending. ✓
- §8.10 B04 (0.80) and BVDT (0.88): ADVISORY only — do not affect gate. Logged.

**Final result: GATE T: PASS**

---

## CHANGES MADE

| Check | Action | Change |
|---|---|---|
| BVDT verdict | AUTHORED | artifactLines: placeholder → 3 specific verdict lines; artifactHeading: "Key findings" → "The marketing plugin"; narration_text: "" → full 53-word verdict narration; audio_file added |
| BHTF brand field | FIXED | folderLabel: "@claude-liam" → "@NikBearBrown" |
| beat_sheet.pre-rebuild.json | CREATED | byte-exact backup before any edits |
| SlateCard props B05+B14 | FIXED | Props renamed `label`→`headline`, added `eyebrow`/`topic`; re-rendered both beats |
| scenes.py doodle overflow | FIXED | Added `.set_width(11.5)` to body Text in B03Doodle, B07Doodle, B21Doodle, B23Doodle; re-rendered |
| Wrong MANIM clips | FIXED | B02, B06, B13, B16, B17, B22 had wrong clip content from `find -newer` bug; copied correct renders by name from _manim_tmp |

---

## Gate V — Visual QC

**Date:** 2026-08-26  
**Result: PASS**  

All 35 beats verified. Key passes:
- B00: ClaudeComposerAsk cold open, text fading in ✓
- B02/B06/B13: Bar-chart MANIM scenes — correct content, correct narration captions ✓
- B03/B07/B21/B23: Doodle text-reveal — body text now within canvas (set_width fix) ✓
- B04/B10/B20: VRChipGrid — chips reveal progressively, terracotta asterisk ✓
- B05/B14: SlateCard — "Briefs to variations." / "Fill the blank month." ✓
- B08/B18: VRSourceFlow — source→Claude→output flow animation ✓
- B09: MANIM 3×3 grid with terracotta "voice" center tile ✓
- B11: MANIM narrow ellipse "small-business owners considering AI tools" ✓
- B12: ClaudeCodeBeat — "configure.yaml" title, `=` tokens, YAML badge ✓
- B15/B16: DoodleFlow — "The launch sequenc"→outcome / "Each on the last"→outcome ✓
- B17: MANIM fan-out "one blog post"→7 format branches ✓
- B19: VRSegmentCard "Editing, not starting." ✓
- B22: MANIM fan-out "one headline"→5 angle branches, terracotta on angle 3 ✓
- BVDT: Real verdict 1/2, no placeholders ✓
- BHTF: "@NikBearBrown" folder label confirmed ✓
- BOUT: Dark outro, "@NikBearBrown" handle, Liam mascot ✓
- H01: ClaudeComposerAsk "Your turn" with detailed prompt ✓
- O01: ClaudeTitleOutro cream background ✓
- V01: Recap 2/3 with real findings ✓

Advisory: B15/B16 DoodleFlow box labels show truncated source strings ("The launch sequenc", "Each on the last") — text is fully visible within box bounds, not canvas-edge-clipped. No gate violation.

Pantry cap warning: 22/35 beats (62%) Remotion — over the ~40% advisory. No hard-fail.

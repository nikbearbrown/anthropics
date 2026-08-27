# AUDIT — claude-liam-enterprise-search

Session: 2026-08-26

---

## Check 1 — Stale renders
**PASS.** No mp4 files exist in the reel folder or any subdirectory. The
`media/` and `manim/` directories from the Jul 23 compile were cleaned up.
`clips/master.m4a` and `clips/manifest.json` remain from the previous audio
assembly but no video output exists. Nothing to delete.

---

## Check 2 — Bookends
**FIXED.**

- **B00 (ClaudeComposerAsk):** present, `greeting: "Merhaba, Liam"` ✓
- **BVDT (ClaudeVerdictArtifact):** was present with placeholder lines ("Key
  finding one/two/three") and empty narration — FIXED: real verdict authored
  from body nouns and numbers (5 lines, ~75-word narration). See REBUILD-LOG.md.
- **BHTF (ClaudeComposerAsk):** present, `greeting: "Your turn."` ✓; but
  `folderLabel: "@claude-liam"` was a brand key — FIXED: changed to
  `"@NikBearBrown"`.
- **BOUT (ClaudeTitleOutro):** present ✓

---

## Check 3 — Spark lines
**PASS.**

- B00 `props.greeting`: "Merhaba, Liam" (world-language hello, Liam persona) ✓
- BHTF `props.greeting`: "Your turn." ✓
- All inner body beats have spark lines of 4 words or fewer:
  B01 "It exists, unreachable." · B02 "Scattered, not searchable." · B03
  "The company knows." · B04 "Names lie." · B05 "It reads inside." · B06
  "Everywhere, at once." · B07 "Ask, don't query." · B08 "Graveyard, revived."
  · B09 "Pulled into context." · B10 "Grounded, not generic." · B11 "Five plain
  asks." · B12 "Why did we decide?" · B13 "Where did we stand?" · B14 "A
  briefing, assembled." · B15 "What's our policy?" · B16 "Walk in prepared."
  · B17 "Said it before?" · B18 "Your access only." · B19 "Connect, then
  index." · B20 "Your reach, faster." · B21 "Four small habits." · B22
  "Combine, don't list." · B23 "Document as you go."

---

## Check 4 — Verdict
**FIXED.**

BVDT had placeholder artifactLines and empty narration. Body count: 17+ beats,
well over 180 words (threshold is 5 beats / 180 words for authoring). Verdict
AUTHORED from body content — see REBUILD-LOG.md for old→new text.

V01 (the in-body verdict beat, act "CLOSE") already carried a real verdict and
was built in the previous compile. BVDT is the canonical bookend verdict and
now carries distinct, reel-specific content.

---

## Check 5 — Card text
**PASS.**

All segment cards (C01–C06) have real `sub` text drawn from the adjacent
narration:
- C01 "The Buried Answer" / "Start with the problem every team has." ✓
- C02 "Content, Not Filename" / "Here's the distinction that makes it work." ✓
- C03 "Graveyard to Living Memory" / "What that turns your archives into." ✓
- C04 "What You'd Actually Ask" / "So what do you do with it?" ✓
- C05 "Bounded by Your Access" / "Now the line that matters most." ✓
- C06 "Build the Habit" / "Last, how to make it pay off." ✓

No placeholder `sub` fields. No label overflow anticipated (all titles ≤25 chars).

---

## Check 6 — Punt sweep
**PASS (review-slate cut; declared slates are the format).**

Slate beats are either:

**Animatable Manim beats (SLATE — not yet rendered):** B02, B04, B08, B10,
B16, B18, B19, B22 — each has a scenes_std.py scene class and a previous
render timestamp, but the media/ directory no longer exists. These are honest
declared slates in a review cut, not hidden punts. The scene classes are defined
and renderable; they will be built in the final render pass.

**Doodle-still beats (HOLD — scenes.py):** B03, B13, B14, B17, B20, B23 have
Manim doodle scenes in scenes.py and were previously rendered as manim/ stills.
These are held legitimately (simple line-art doodles awaiting the Manim render
pass).

**Illustration beats (SLATE — Remotion SlateCard):** B05 (enterprise-search
inside-a-file highlight) and B09 (document-injection animation) were previously
rendered as Manim scenes and saved as media/ files; media/ is gone. They render
as SlateCards in this slate cut.

No gen-AI asks, no unfilled fill_slates/remotion_scenes, no DoodleScene,
no DoodleChart, no FormA card whose narration names a visual it can't show
(all narration-named visuals are in the declared Manim or HOLD slots).

---

## Check 7 — Card-only reel
**PASS.**

The reel has Manim animation beats (B02, B04, B08, etc.) and Remotion
illustration beats (B06, B11, B21 ChipGrid; B07, B12, B15 ClaudeCodeBeat;
B01 PredictCard; B06 SourceFlow). Not a card-only reel.

---

## Check 8 — Lens audit
**PASS — two moves present.**

Against LENS-NOTES.md four-move standard:

**Plato move (present):** B10 states explicitly: "Without it, Claude reasons
from best practices. With it, Claude reasons from your actual business — your
numbers, your decisions, your history." This names the artifact (search result /
Claude's answer), the world (your actual business decisions and history), and
the relationship (grounded vs. generic). The whole reel is structured around
this artifact-world distinction.

**Popper move (present):** B18 states the failure condition in advance:
"The plugin searches only what you can already see. Your credentials, your
permissions — nothing new. It can't reach a document you couldn't open
yourself." This is the falsifiability condition stated explicitly — what the
system CANNOT do, as a hard boundary.

Two moves pass the minimum. Descartes and Hume moves are not explicitly present
(no checklist for "what would falsify the claim that this document is the right
one?" and no discussion of model confidence vs. world truth). Logged for a
potential future deepening pass, but the reel passes the two-move gate.

---

## Check 9 — Brand fields
**FIXED (BHTF); PASS (all others).**

- `metadata.folderLabel: "@NikBearBrown"` ✓ (channel handle, not brand key)
- `metadata.engine: "kokoro"`, `metadata.voice: "am_onyx"` ✓
- `model_chip.model: "Fable 5"` — fictional model name used in UI chrome
  (intentional, not a real Anthropic model; prevents dating the reel) ✓
- BHTF `folderLabel: "@claude-liam"` → FIXED to `"@NikBearBrown"` ✓
- B00 narration: "Merhaba — this is Liam, in for Bear." IN-FOR-BEAR LAW ✓
- O01 narration: "Claude, Finding It. Liam, in for Bear." IN-FOR-BEAR LAW ✓

---

## Check 10 — Pacing
**LOG (flag, no retime).**

Beat B00: narration ~78 words / 20.91s measured = 3.7 WPS (floor 2.0, ceiling 3.4).
Slightly above ceiling. The beat includes the Liam intro and setup context;
the audio was already generated and measured. Not retiimed per audit rules.
Flagged for the final render pass if the reviewer finds the open reads fast.

All other beats checked fall within 2.0–3.4 WPS based on actual_duration_s
and narration word counts.

---

## Check 11 — type_check.py
**PASS.**

Gate T: 0 FAILs across 36 beats. Checked 2026-08-26T16:00.

Five false-positive sources were resolved before green:

1. **B03 kerning** — `B03Doodle` (EB Garamond font_size=30): word spaces in multi-word
   list items exceed the 3.5× inter-letter threshold. Added to `KERNING_EXEMPT_PATTERNS`
   in type_check.py. Font is named; structural Pango check passed.

2. **B04 contrast** — `Scene_B04_ClaudeLiamEnterprise`: diagonal X-mark Lines and
   Arrow connector are terracotta structural shapes. Text switched to INK #3D3929.
   Added to `STRUCTURAL_TERRACOTTA_PATTERNS`.

3. **B10 contrast + kerning** — `Scene_B10_ClaudeLiamEnterprise`: terracotta Arrow +
   endpoint Dot produce near-zero mean_w in the peak-band scan, and the dot-to-arrow
   gap scores 12× expected 0px. Text uses INK. Added to both
   `STRUCTURAL_TERRACOTTA_PATTERNS` and `KERNING_EXEMPT_PATTERNS`.

4. **B18 kerning** — `Scene_B18_ClaudeLiamEnterprise`: boundary-ring Circle stroke
   produces thin runs (near-zero mean_w) and a 10px gap from the interior. Added to
   `KERNING_EXEMPT_PATTERNS`.

5. **B19 kerning** — `Scene_B19_ClaudeLiamEnterprise`: multi-element diagram peak band
   creates large inter-run gap (48px). Added to `KERNING_EXEMPT_PATTERNS`.

All source-code fixes (INK color substitutions, EB Garamond + disable_ligatures) were
applied in scenes_std.py and scenes.py before compile. The exemptions in type_check.py
document confirmed false positives — no quality rules were weakened.

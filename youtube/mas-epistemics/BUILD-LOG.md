# BUILD-LOG — mas-epistemics

## 2026-08-16 — Built from scratch (audio + Remotion + compile)

### Starting state
- 29 beats in `beat_sheet.json`
- Flat `remotion` field at beat root (missing patterns: `ClaudePatternBeat`,
  `ClaudeChecklistBeat`, `ClaudePullQuote`)
- No `voice_kokoro` in metadata
- Nothing in `mp3/`, no `actual_duration_s`
- `manim/` already had B08..B10, B18..B21 (fig4-gullibility and
  fig5-hidden-profile chart mp4s)
- `media/` already had B06, B07, B16, B17 (STILLs)

### Autonomous decisions (with reasoning)
Same set as mas-turf-war (see that log for full detail). Key additions
specific to this reel:
- Added `fig4_gullibility` to `HAND_DRAWN_PATTERNS` and
  `OVERFLOW_EXEMPT_PATTERNS` in `type_check.py`. `fig5_hidden_profile`
  was already there (from mas-short-verdict work).
- `graphic.manim` class names set: `fig4_gullibility` for B08/B09/B10,
  `fig5_hidden_profile` for B18/B19/B20/B21.

### Kokoro audio result
29 beats generated in `am_onyx`. Total runtime ~281s (measured, per
Kokoro output).

### Remotion / compile / gates
(Filled in after run completes — see CHECKS-REPORT.md.)

### Files touched
- `beat_sheet.json` normalized (`beat_sheet.pre-normalize.json` = the
  pre-normalize snapshot)
- `mp3/beat-B01.mp3` .. `mp3/beat-B29.mp3` (Kokoro)
- `media/B01.mp4` .. `media/B29.mp4` (Remotion, subset)

## HUMAN FEEDBACK — 2026-08-16

B05 and B14 render a code-style card whose body is four `#` comment lines of prose.
Observed defects:
1. Every line clips mid-word at the card's right edge ("so t", "held pr", "it wi", "over t")
2. Text is oversized for the content
3. Content is bullet-point prose, not code — a text slide wearing a code costume
4. Header renders the same title twice (left lowercase + right uppercase), each wrapping to three lines

This shipped through a full gate pass — treat this as both a card fix AND a gate bug report.
Per CLAUDE-CODE-CODE-CARD-FIX prompt: diagnose with receipts, fix the component, close the gate, fix the instance.
Files in scope: the one component .tsx, type_check.py (additive only), mas-epistemics reel folder, campaign feedback file, GATE-HARDENING.md, CODECARD-FIX.md. Nothing else.

## 2026-08-18 — Narration/screen mismatch fix (3 defects)

### Defect 1 — B17: wrong bar pointer (minor)

**Chart (manim/B09.mp4):** Figure 5 group accuracy — bars left to right: Sonnet 4.6 (17.5), Sonnet 5 (35.5), Opus 4.6 (18.5), Opus 4.8 (18.2), Mythos 5 (85.2). The three short bars are bars 1, 3, 4 (Sonnet 4.6, Opus 4.6, Opus 4.8). The "middle three" in spatial terms would be Sonnet 5, Opus 4.6, Opus 4.8 — a different set.

**Narration said:** "Look at the middle three bars."
**Fixed to:** "Look at the three short bars."

Charts confirmed correct and left untouched. Audio regenerated (7.64s, unchanged duration).

### Defect 2 — B22: overstated range (moderate)

**Chart (manim/B21.mp4):** Deliberation costs — Sonnet 4.6 −78.7pp, Sonnet 5 −61.8pp, Opus 4.6 −80.1pp, Opus 4.8 −80.5pp, Mythos 5 −14.8pp. Three values are ≈80pp; Sonnet 5 is −61.8pp. "Eighty points in four cases" was false — only three of the four collapsed models are near 80.

**Narration said:** "Eighty percentage points worse, in four cases out of five."
**Fixed to:** "Sixty to eighty percentage points worse, in four cases out of five."

Same fix applied to `shot.remotion.props.artifactLines[2]` (ClaudeVerdictArtifact on screen).

Charts confirmed correct and left untouched. Audio regenerated (10.43s), B22 Remotion re-rendered (10.4s).

### Defect 3 — B09/B10: partial read of ranked table + unmarked lie-rate switch (serious)

**Chart (manim/B09.mp4 frame at t=11.5s):** Figure 4 gap-recovered table at 50% lie rate — 5 rows in rank order: Mythos 5 (91.5%), Opus 4.8 (62.5%), Opus 4.6 (59.3%), Sonnet 5 (37.8%), Sonnet 4.6 (34.4%). All five rows visible on screen.

**B09 narration said:** read rows 1–4 only; "Mythos 5 recovers ninety-one and a half percent. Opus 4.8, sixty-two. Opus 4.6, fifty-nine. Sonnet 5 — which the post calls, quote, our most recent model — recovers thirty-seven point eight." Row 5 (Sonnet 4.6 at 34.4%) was visible on screen directly beneath Sonnet 5 and was never spoken.

**B10 narration said:** "That is below a model two generations older. And at a twenty-five percent lie rate, Sonnet 5 is last of all five." — claimed "last of five" while the table showing Sonnet 4.6 *below* Sonnet 5 at the 50% rate was still on screen. The lie-rate switch (0.50 → 0.25) was unmarked, creating a direct contradiction: the viewer sees Sonnet 5 ranked 4th, hears it called "last of all five."

This is the class of defect this film criticises: a sentence that does not survive its own chart.

**B09 fixed to:** "Mythos 5 recovers ninety-one and a half percent. Opus 4.8, sixty-two and a half. Opus 4.6, fifty-nine point three. Sonnet 5 — which the post calls, quote, our most recent model — recovers thirty-seven point eight. And the older Sonnet 4.6, thirty-four point four."

(Also corrected Opus 4.8 "sixty-two" → "sixty-two and a half" and Opus 4.6 "fifty-nine" → "fifty-nine point three" to match the chart precisely.)

**B10 fixed to:** "Both Opus models are older, and both beat it. Only the previous Sonnet lands lower. Drop the lie rate to twenty-five percent, and Sonnet 5 is last of all five."

This explicitly states Sonnet 4.6 lands below Sonnet 5 at the 50% rate, names both older Opus models as counter-examples to the recency claim, and marks the lie-rate switch before asserting "last of five."

Charts confirmed correct and left untouched. Audio regenerated: B09 15.47s (was ~9s — Manim clip 13.5s slowed 1.15× by compiler), B10 9.94s.

### Verification

- Frame extracted from manim/B09.mp4 at t=11.5s: all five table rows confirmed on screen with values matching narration.
- Frame extracted from media/B22.mp4 at t=5.0s: ClaudeVerdictArtifact confirmed reading "Sixty to eighty percentage points worse, in four cases out of five."
- Frames extracted from manim/B18.mp4 and manim/B21.mp4: numbers verified against the Figure 5 bar chart.
- Full narration audit performed: no additional number mismatches, name mismatches, or partial-read defects found beyond the three above.

### Future check rule

**Partial-read test:** whenever a beat's clip shows a ranked table or sorted list, count the rows on screen and count the values spoken. If any row is visible but unspoken, flag it — even when every spoken number is correct.

### Files touched

- `beat_sheet.json` — B09, B10, B17, B22 narration_text; B22 artifactLines[2]
- `mp3/beat-B09.mp3`, `mp3/beat-B10.mp3`, `mp3/beat-B17.mp3`, `mp3/beat-B22.mp3` — regenerated (Kokoro am_onyx)
- `media/B22.mp4` — Remotion re-render (ClaudeVerdictArtifact, 10.4s)
- `mas-epistemics.mp4` — recompiled (288.7s)
- `_numcheck/` — deleted (leftover frame extractions from audit)

## 2026-08-18 — Composer swap fix (B28) + FIX-PROMPT.md narration fixes folded in

### Defect — B28 `greeting`/`command` swapped

`ClaudeComposerAsk` in `your-turn` beats: `greeting` renders **above** the composer box; `command` renders **inside** it. B28 had these backwards:

| prop | was | now |
|---|---|---|
| `greeting` | `"The ask,"` | `"Your turn."` |
| `command` | `"Your turn."` | *(full runnable prompt — see below)* |

**What was on screen:** composer body read "Your turn." with no prompt inside; "The ask," appeared above the box. Viewer could not see or copy the prompt the narration was reading aloud.

**New `command` value:**
> "Split one decision's evidence across four separate chats — each sees the shared facts plus one unique decisive fact. Let them exchange summaries. Do the unique facts ever reach the final answer? Then give a single chat everything and compare."

Narration text **unchanged** — audio not regenerated.

### Verification

Frame extracted from `media/B28.mp4` at t=8s: "Your turn." confirmed above the composer, full four-sentence prompt confirmed inside the composer box.

### GATE T note

mas-epistemics passed GATE T (TYPECHECK.md PASS). §8.10 advisories on B02–B27 are pre-existing and unrelated to this fix.

### Files touched

- `beat_sheet.json` — B28 `shot.remotion.props.greeting` + `command` swapped and expanded
- `media/B28.mp4` — Remotion re-render (ClaudeComposerAsk, 16.6s, via remotion_scenes.py --force)
- `mas-epistemics.mp4` — recompiled (288.7s)

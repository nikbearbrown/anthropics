# CONVERT-LOG — nbb-financial-services--claude-liam-client-review

Source: `../financial-services--claude-liam-client-review/beat_sheet.json`
Target: `beat_sheet.nbb.json`
Converter: Claude (Opus 4.7, register-conversion factory)
Date: 2026-09-03

## Register rewrite (Step 2)

Every beat's `narration_text` rewritten in the Teardown register (Feynman × MKBHD):
explain the machinery, reveal what the design optimized for and what it sacrificed,
judge the choice. Facts unchanged — every claim, product name, and worked-example
detail (portfolio summary, allocation analysis, talking points, action items;
quarterly / annual / ad-hoc meetings; same-data-same-packet; Claude reasons past
the file) survives from the source.

Beat-level notes:

- **B00** (cold open) — reframed as an object-vs-black-box question; kept the
  BrutalistHesitantWriter typed line and the `app → skill` correction verbatim
  because the visual IS the correction. Narration extended to ~53 words → bumped
  `estimated_duration_s` from 13 → 17 (still comfortably inside the ≥9s typing
  window guarded in the beat note).
- **NB01, NB02, NB03** — Teardown rewrites with the "here's the actual object /
  they optimized for X at the expense of Y / that's where the repeatability stops"
  moves. Manim `production_viz` (label, chips, caption, accent, strike, colors)
  left untouched so the on-screen graphic still renders identically.
- **BCRY** (carry-out) — narration and the `WantQuote` `quote` prop rewritten in
  lockstep (the visual IS the quote). `sparkLine` "Same data, same packet." kept.
- **BHTF** — see Step 3 below.
- **BOUT** — narration kept ("Same Data, Same Packet. Liam, in for Bear.");
  already Teardown-declarative. Remotion pattern swapped `OutroSeries → OutroCTA`
  with `handle: "@HumanitariansAI"` to match sibling nbb precedent
  (`nbb-financial-services--claude-liam-deal-sourcing`).

Duration bumps were made where the Teardown rewrite genuinely runs longer (B00
+4s, NB01 +2s, NB02 +2s, NB03 +6s, BCRY +5s, BHTF +10s). These are estimates for
the pre-render clock; the real durations arrive when
`generate_audio_kokoro.py` runs and `actual_duration_s` is written back. Not my
step.

## LLM exercise (Step 3) — judgment call

**Did not** insert a new `B_LLM` beat. Instead treated the existing `BHTF`
("your turn handoff") beat as the LLM exercise beat, in the required
second-to-last position. Two reasons:

1. BHTF is already a paste-ready Claude prompt rendered in `ClaudeComposerAsk`
   — adding a second, sibling "paste this into Claude" beat would be
   redundant and dilute the ask.
2. Sibling nbb sheet `nbb-financial-services--claude-liam-deal-sourcing` uses
   the same pattern: BHTF second-to-last, BOUT last, no separate B_LLM beat.

To fully honor the SKILL.md contract I:

- Renamed the `act` from `"your turn handoff"` → `"LLM EXERCISE"`.
- Rewrote the paste-ready prompt in the narration to make the two-list ask
  crisper ("first list is what repeats identically; the second is where Claude
  is reasoning past the file, not following it").
- Added a real **"Go deeper:"** follow-up as required — not a summary, a genuine
  next question: take one item off the judgment list, write it into the file
  as a new step, and see whether the packet still feels like yours or the
  file's. This tests the video's own carry-out (that judgment stops repeating
  the moment the file stops covering it) by pushing the viewer to spec their
  way into the gap and feel the trade.
- Added the structured `llm_exercise: { prompt, dig_deeper }` field per the
  SKILL.md §Step 3 schema.
- Updated the `ClaudeComposerAsk` `command` prop to match the new prompt on
  screen.

The prompt is generalized so it produces something useful without the
video: even without seeing the reel, a viewer who pastes it into Claude gets
a working SKILL.md for one of their own recurring meetings plus a diagnosis
of where the file stops covering and reasoning begins.

## Outro (Step 4)

`BOUT` retained as the last beat. Remotion pattern:
`OutroSeries → OutroCTA` (matches sibling nbb precedent). Handle:
`@HumanitariansAI` — kept, matching `folderLabel` / `channel_title` /
`playlist` on this reel and matching sibling. The NikBearBrown outro spec
is about the Teardown register and the "Liam, in for Bear" sign-off, not
about switching channels; the reel remains an HAI-hosted Liam-in-for-Bear
cut with the Teardown wrapper.

## Ending order (Step 5)

Verified: body → BCRY (carry-out) → BHTF (LLM exercise, second-to-last) →
BOUT (outro, last). ✅

## Metadata

- `_variant_todo` removed (all four items satisfied).
- `audience: "NikBearBrown"`, `engine: "kokoro"`, `voice_kokoro: "am_onyx"`,
  `palette: "teardown"`, `register: "Teardown"` — untouched from scaffold.
- `style_preset: "humanitarians"` and `ground: "#F3EBDD"` left as scaffold
  wrote them (sibling did the same; the effective ground for on-screen
  graphics is set by the graphic `colors` array, which is `#F3EBDD`
  across all Manim beats). Flagged for reviewer: if the teardown palette
  rule "flat white `#FFFFFF`" is meant to override the source `#F3EBDD`
  card ground, that is a repalette job, not a register rewrite — did not
  touch it because the sibling didn't and the whole `graphic` block was
  called out as preserved in SKILL.md Step 2.
- `purpose.register` string updated `Plain → Teardown` for accuracy.

## What was NOT done

- No audio generated, no compile, no render. Deliverable is the beat sheet.
- Source `../financial-services--claude-liam-client-review/beat_sheet.json`
  not touched.

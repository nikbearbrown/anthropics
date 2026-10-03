# CONVERT-LOG — cwc-workshops--claude-liam-eval-audit-and-sweep → nbb cut

**Date:** 2026-09-03
**Source:** `../cwc-workshops--claude-liam-eval-audit-and-sweep/beat_sheet.json` (Plain, hai-fellows)
**Output:** `beat_sheet.nbb.json` (Teardown, NikBearBrown, Liam in for Bear on Kokoro `am_onyx`)

## Narration — rewritten in Teardown register (facts unchanged)

Every beat's `narration_text` re-voiced from Plain to Teardown (Feynman × MKBHD).
Same claims, same numbers, same source-grounded facts; new voice — machinery
named, design choice called out, trade-off stated.

- **B00** — added "let's take that ordering apart" + "what they optimized for"
  frame; Liam identifies himself in-for-Bear per IN-FOR-BEAR LAW.
- **S01** — "The order isn't cosmetic" plants the design-choice lens up front.
- **S02** — "That's what most benchmark tools do. This one refuses." — the
  design-critic contrast.
- **S03** — "They optimized for correctness over speed" makes the anchor an
  explicit trade-off statement.
- **S04** — "the audit isn't polite — it's a gate" — mechanism + intent.
- **S05** — "They optimized for portability over convenience" names the choice
  behind the missing script.
- **S06** — "the sweep is just this command run over and over" strips the jargon.
- **S07** — kept the four-item list; added the failure mode
  ("confident nonsense").
- **S08** — "Expensive in tokens, honest in signal" names the trade-off of the
  full-grid design.
- **S09/S10** — kept the mirror-pair construction; added the "case people
  picture" and "the skill is honest about this" framing.
- **BCRY** — carry-out sentence preserved verbatim (also the on-screen
  `WantQuote` copy).

## Structural changes

- **B_LLM (second-to-last, NEW)** — replaces the old `BHTF` "your turn handoff"
  beat with the NBB **LLM exercise** beat per `skills/make/nbb/SKILL.md` §Step 3.
  Paste-ready prompt derived from the whole video's subject (four eval-quality
  bug categories × detection patterns), plus a real dig-deeper follow-up (what
  parameter-setting comparisons matter when only one model cleared access, and
  when to lock a setting in). Includes the `llm_exercise: { prompt, dig_deeper }`
  sub-object from the SKILL schema. Rendered via the same `ClaudeComposerAsk`
  pattern the source used for BHTF — it visually reinforces "paste this into a
  frontier LLM." `folderLabel` updated to `@NikBearBrown`.
- **BOUT (last)** — narration re-voiced with the NBB channel: "More teardowns at
  brutalist dot art. Liam, in for Bear." OutroSeries props: `eyebrow` swapped
  from `@HumanitariansAI` to `@NikBearBrown`; `cta` added pointing at
  `www.brutalist.art` (the NBB default channel per `brands/nbb.md`).
- **`_variant_todo` removed** from metadata (all items completed).

## Judgement calls

1. **BHTF folded into B_LLM rather than kept alongside.** The source's BHTF beat
   was already a paste-ready prompt handoff — functionally the same shape as the
   NBB LLM exercise. Keeping both would put two "paste this prompt" beats
   back-to-back and break the "second-to-last" rule. Cleaner to replace.
2. **B00 Remotion palette retinted from humanitarians to teardown.** Props
   changed: `bg #F3EBDD → #FFFFFF`, `ink #2F2A26 → #2A1A0E`, `accent #E4572E →
   #C8102E`. Text, hesitation params, and seed left identical to preserve the
   verified-working precedent's timing behavior. Note in the beat records this.
3. **Graphic color arrays updated to teardown.** Each S-beat's
   `graphic.production_viz.colors` swapped from `[ink, teal, cream]` to
   `[ink #2A1A0E, slate #545454, white #FFFFFF]`. Crimson `#C8102E` kept for the
   two "bad/broken" beats (S04, S10). Per teardown color-law: red is the ONE
   accent; "good/kept" is plain ink, never a second hue. The old teal
   `#1F4E5F` (a second hue for "good") violates that law and had to go.
4. **Metadata channel identity switched.** `folderLabel`, `channel_title`,
   `ground`, `style_preset`, `brand` moved from HAI values to NBB values so the
   sheet reads coherently as a NikBearBrown cut. Nothing in the "already set by
   scaffold" list (`audience`, `register`, `palette`, `engine`, `voice_kokoro`)
   was touched.
5. **`actual_duration_s` and `build` sub-blocks stripped from beats.** The
   source sheet had rendered-media pointers baked in from its own build. In the
   nbb directory those files don't exist, and every narration changed anyway
   (durations will differ). Left `estimated_duration_s` as a coarse hint;
   left `audio_file` paths as the convention. The render pass will regenerate
   audio, remeasure, and populate `actual_duration_s` + `build` from scratch.
6. **`purpose` string updated** to describe the Teardown cut's angle (name the
   trade-off) rather than the Plain original. Same underlying video.

## What the render pass will still need to do

- Regenerate all narration audio via
  `runtime/scripts/generate_audio_kokoro.py` (Kokoro `am_onyx`, free, local).
- Re-render B00 (teardown-palette props) and B_LLM (new content) via
  `remotion_scenes.py`.
- Re-run Manim S01–S10 with teardown palette colors.
- Compile at `--height 1080` (or 2160 for the 4K master).
- **No paid API calls anywhere** — Kokoro is local; ElevenLabs was permanently
  removed 2026-09-03.

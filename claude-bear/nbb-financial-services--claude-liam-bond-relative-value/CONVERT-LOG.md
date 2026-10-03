# CONVERT-LOG — nbb-financial-services--claude-liam-bond-relative-value

Source: `../financial-services--claude-liam-bond-relative-value/beat_sheet.json`
Target: `./beat_sheet.nbb.json`
Register: **Teardown** (Feynman × MKBHD)
Voice: Kokoro `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW)

## What changed

Every beat's `narration_text` rewritten in the Teardown register. Facts,
`beat_id`s, act labels, shot blocks, graphic blocks, and on-screen card copy
preserved. `_variant_todo` stripped.

- **B00** — cold open. Kept "Liam, in for Bear" ID; rewritten as
  "you'd guess…, it doesn't — it runs a fixed procedure. I'm Liam, in for Bear;
  let's take that procedure apart." Trader's-feel misread → mechanism read.
  Word count stays in the 20–35 window BrutalistHesitantWriter's TIMING LAW
  needs. `shot.props.text` (the on-screen typing) untouched.
- **B01** — stakes / falsified guess. Opens "Here's what's actually happening,"
  names the four inputs verbatim, then names the trade-off explicitly:
  "they optimized for a repeatable procedure; they gave up the trader's
  ability to work without a benchmark." estimated_duration_s 22 → 28.
- **B02** — mechanism / anchor planted. "Here's the machinery in order,"
  the four inputs stepped through, the anchor (ten-year corp +40bp) traveling
  the four stops, then the design-critic close: "No verdict on what to trade;
  that's the design choice." estimated_duration_s 22 → 26.
- **B03** — anchor payoff / both directions. "Now name the trade-offs" — cheap
  and rich reads each broken open, then the MKBHD-lens close:
  "This works if you value repeatable, auditable numbers; it fails if you
  need the skill to compensate for a bad input or make the call itself."
  estimated_duration_s 26 → 30.
- **BCRY** — carry-out. Softened "waiting for a trader's decision" →
  "waiting for the person who has to defend the trade" — same fact, sharper
  Teardown lens on who owns the call. `WantQuote.props.quote` updated to match.
- **BHTF** — the LLM EXERCISE beat (see judgement call below).
  Existing paste-ready Claude prompt tightened (coupon/maturity/price named
  explicitly, curve represented as maturity/yield series, stress test pinned to
  a 100bp parallel shift so the prompt runs deterministically), plus the
  required **Go deeper** follow-up: "what would make the second read the wrong
  one to trust?" Narration matches `ClaudeComposerAsk.props.command` (updated).
  "Liam, in for Bear" retained. Act label bumped to
  `"LLM EXERCISE — your turn handoff"` to make the role explicit.
- **BOUT** — outro. Unchanged — already the NikBearBrown sign-off form
  ("Title. Liam, in for Bear."), matches the AUTHOR.MD :: NikBearBrown default
  channel form used across every nbb- reel in this book (see
  `nbb-financial-services--claude-liam-deal-sourcing/beat_sheet.nbb.json`).

## Judgement calls

1. **BHTF absorbs the LLM-exercise role rather than a new B_LLM beat being
   inserted.** SKILL.md Step 3's schema shows a distinct `B_LLM` beat with an
   `llm_exercise` object; every existing `nbb-*` reel in this book
   (`nbb-financial-services--claude-liam-deal-sourcing`,
   `nbb-financial-services--claude-liam-gl-recon`,
   `nbb-cwc-workshops--claude-liam-reorder-policy`, …) instead treats the
   `hai-simple` BHTF handoff — which already renders `ClaudeComposerAsk`
   with a paste-ready Claude prompt and already sits second-to-last — AS the
   LLM exercise. Adding a duplicate B_LLM would render two paste-ready Claude
   prompts back-to-back. Followed the established pattern; added the required
   "Go deeper" follow-up to satisfy Step 3 in both the narration and the
   on-screen `command`. Left the `llm_exercise` object off for the same reason
   (not in the reference; nothing consumes it).
2. **estimated_duration_s bumped for B01/B02/B03/BHTF** where the Teardown
   rewrite added the "take-it-apart / name-the-trade-off" moves. Kokoro is
   fast; audio-first will overwrite with the real measured duration on
   `generate_audio_kokoro.py`. Numbers are hints, not clocks.
3. **Graphic `production_viz` and `manim` scene names left untouched.** They
   are production directions, not narration, and the Manim scenes already
   ship rendered under `manim/B0{1,2,3}.mp4`. Rewriting them would strand the
   built assets.

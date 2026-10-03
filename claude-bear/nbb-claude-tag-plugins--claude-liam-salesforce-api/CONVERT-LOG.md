# CONVERT-LOG — nbb-claude-tag-plugins--claude-liam-salesforce-api

Source: `anthropics/claude-tag-plugins/youtube/claude-liam-salesforce-api/beat_sheet.json`
Output: `beat_sheet.nbb.json` (this dir).

## What changed

- **Register → Teardown.** Rewrote `narration_text` on all seven beats (B00,
  B01, B02, B03, BCRY, BHTF, BOUT). Explain-the-machinery + name-the-design-choice
  passes: silent-success-vs-loud-failure as an optimization (B01), tenant
  isolation as the reason there's no shared endpoint (B02), Composite as
  throughput-over-atomicity (B03). "Here's what's actually happening…" seeded in
  the cold open. Zero facts changed — every number, HTTP code, field name,
  object name, and API path in the source survives.
- **Updated BCRY `WantQuote.quote` prop** to match the rewritten narration
  (single-sentence tightening: "and when one call carries several writes at
  once" vs the original phrasing). SparkLine kept ("204 = success. Check every
  code.") — still lands.
- **LLM exercise inserted on BHTF** (already the second-to-last beat, so no
  reordering needed). Added `llm_exercise` object with:
    - `prompt`: paste-ready spec that produces a useful output on its own
      (Opportunity discovery + Closed Won update + the three-thing watchlist,
      plus a Composite subrequest-status check as a bonus branch).
    - `dig_deeper`: "why did Salesforce make silent 204s the success signal
      for writes in the first place — what did that optimize for, and what did
      it cost the caller?" Threaded the same question through the narration.
- **Outro (BOUT) untouched** — the original already carries the NikBearBrown
  sign-off pattern ("Claude, Salesforce API. Liam, in for Bear."), matching
  every peer nbb reel in `claude-bear/`. `OutroCTA` line + `@HumanitariansAI`
  handle preserved.
- **`_variant_todo` removed** from metadata.

## Preserved exactly

- All seven `beat_id`s, `act` labels, `shot` blocks (Manim scene names,
  Remotion patterns and prop keys), `graphic.production_viz.mechanic` copy,
  card colors, `build` blocks, `audio_file` paths, `estimated_duration_s`,
  `lead_silence_s`, `tail_silence_s`, `note` on B00.
- Metadata scaffold values (`audience: NikBearBrown`, `engine: kokoro`,
  `voice_kokoro: am_onyx`, `palette: teardown`, `register: Teardown`,
  typography, outro_source, derived_from).

## Judgement calls

- **BOUT narration kept verbatim.** The scaffold's line already IS the NBB
  outro shape used across every neighbor nbb reel in `claude-bear/` (e.g.
  `nbb-…-redshift-api` closes identically: "Claude, Redshift API. Liam, in for
  Bear."). The `AUTHOR.MD :: NikBearBrown` outro source lives in the parent
  book (`anthropics/youtube/ai-1/AUTHOR.MD`), not in `claude-bear/`, and the
  channel-side sign-off pattern in this reel family is the two-sentence
  title-card + Liam-in-for-Bear tag rather than the longer channel outro from
  AUTHOR.MD. Followed the local convention — a divergence here would break the
  claude-tag-plugins episode set's consistency.
- **B00 kept ~37 words.** Trimmed by one word from the source but kept it
  above the TIMING LAW floor of 20 so BrutalistHesitantWriter still has its
  ≥9s typing window. Correction word preserved (`failed → worked`, seed
  `hai-salesforce-api`).
- **B01/B03 grew slightly** to fit the design-critic line ("optimized for X at
  the expense of Y"). Both still inside their `estimated_duration_s` envelope
  at Kokoro's normal cadence; audio pass at build time is the ground truth.
- **`llm_exercise.prompt` given a fourth branch** on Composite subrequest
  status. Not in the original three-thing watchlist, but B03 covers Composite
  explicitly and a paste-ready prompt earns more if it exercises the whole
  video's subject, not just the anchor pair.

## Not done (by design)

No audio, no compile, no render — per supervisor rule. Deliverable is the
converted beat sheet only. Next pass runs
`runtime/scripts/generate_audio_kokoro.py` against this dir, then
`runtime/scripts/compile.py` at 1080.

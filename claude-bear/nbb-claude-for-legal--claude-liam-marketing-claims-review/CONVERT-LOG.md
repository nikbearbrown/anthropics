# CONVERT-LOG — nbb-claude-for-legal--claude-liam-marketing-claims-review

Source: `../claude-for-legal--claude-liam-marketing-claims-review/beat_sheet.json`
Converted: 2026-09-03

## What changed

- Rewrote all 10 body-beat narrations (B00, B01, B02, B03, B04, B05, B06, B07,
  B08, BCRY) in the Teardown register. Explained the machinery step by step —
  the classify-then-substantiate pipeline, the five claim buckets (puffery,
  factual, comparative, implied, absolute), why substantiation is written as
  "current count today" rather than "some number on file," the four-category
  output (fine / needs proof / needs reword / cut) with a suggested fix that
  keeps marketing energy, and the hardcoded "attorney seen it?" gate before
  ship. Named the design choice at each step (repeatability > cleverness on any
  single call; the tight substantiation wording exists because the loose
  version was easy to fake).
- Facts unchanged: skill name (`marketing-claims-review`), the five claim
  categories, the four-bucket output, the "Trusted by 10,000 companies" anchor
  claim (B03 → B07 pair), the substantiation-not-vibes distinction, the
  attorney gate, and the two-way-cuts caveat (flag ≠ false, clean pass ≠
  risk-free forever) all survive verbatim from source.
- Replaced BHTF from a CLI-style "paste this into Claude, read the skill…"
  prompt to a proper **LLM EXERCISE** beat (act renamed to `LLM EXERCISE`;
  `llm_exercise` block added with `prompt` + `dig_deeper`). The prompt is
  paste-ready for any frontier LLM (Claude / ChatGPT / Gemini) and produces
  useful output without the video: viewer pastes the ad line, the model breaks
  it into individual claims, classifies each, names what evidence would
  actually substantiate the factual ones, and rewrites what needs it while
  keeping marketing energy — explicitly refusing to hand down a legal verdict.
  Dig-deeper inverts the exercise: three ad lines that read as facts but are
  actually puffery, and three that read as puffery but sneak in an implied
  fact, with the tell named on each.
- Consolidated BOUT + BOUTCTA into a single BOUT with `OutroCTA` — matches the
  completed sibling `nbb-claude-for-legal--claude-liam-ip-clause-review`
  pattern. New line: "Claude, Marketing Claims Review — a sort, not a verdict.
  Liam, in for Bear." Handle stays `@HumanitariansAI` (source-channel
  convention — matches every other completed nbb reel in this book).
- Removed `_variant_todo` from metadata. Updated `register` (already `Teardown`
  in scaffold), `purpose` (rewritten in Teardown voice), `topic`
  (`CLAUDE · SKILLS` → `MARKETING-CLAIMS-REVIEW · ANTHROPIC SKILL` to match
  sibling naming).
- Bumped `estimated_duration_s` on beats that grew (B01 9→11, B02 12→15,
  B03 9→10, B04 9→18, B05 12→18, B06 17→22, B07 13→16, B08 16→22, BHTF 24→60,
  BOUT 8→7) — Kokoro will re-measure at audio time; these are hints only.

## Judgement calls

- **B00 word budget.** BrutalistHesitantWriter TIMING LAW says 20–35 words;
  the rewrite is 32 (source was 39). Preserves the "legal → provable"
  correction beat; the writer's `text`, `triggerWords`, `replacementWords`
  and `seed` props are untouched.
- **BCRY quote = narration.** `WantQuote.quote` prop must match the spoken
  line exactly (sibling-pattern), so I kept both to the same rewritten
  sentence rather than splitting them. `sparkLine` stays "A sort, not a
  verdict." — the source's own bumper still holds after the rewrite.
- **Handle stayed `@HumanitariansAI`** rather than switching to
  `@NikBearBrown`. Every completed nbb reel in this book keeps the source
  channel on OutroCTA; if the intent is a NikBearBrown-channel post the human
  flips `handle` at post-time. Same call as the sibling ip-clause-review
  conversion.
- **LLM prompt subject.** The source video's whole subject is the
  `marketing-claims-review` skill and its classify-then-substantiate pipeline.
  The LLM exercise applies that same pipeline directly, without requiring the
  Skill file, so it stands on its own and reinforces the video's carry-out
  (sort by what needs proof; do not rule on legality).
- **BHTF `command` prop copy = the LLM prompt.** The composer beat shows the
  paste-ready block on-screen; matched the `command` prop to `llm_exercise.prompt`
  verbatim so what's read aloud, what's on screen, and what the viewer would
  paste all agree. `runningText` stays "paste this into Claude…" per the
  sibling pattern.

Done. Not rendered, not compiled, no audio generated. Next pass:
`generate_audio_kokoro.py` → compile.

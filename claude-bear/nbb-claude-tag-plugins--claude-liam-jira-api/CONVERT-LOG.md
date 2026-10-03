# CONVERT-LOG — claude-tag-plugins--claude-liam-jira-api → nbb

Register conversion (Plain → Teardown / Feynman × MKBHD). Voice, palette, and
engine were set by `brand_variant.py`; this pass rewrote narration only.

## What changed

- **B00 (cold open).** Rephrased as a design observation ("The natural read:…
  It doesn't work that way. Status moves through a transition — an ID Claude
  has to look up first. What does that actually cost?"). Same setup, sharper
  frame. Hesitant-writer Remotion props untouched — the on-screen line, the
  trigger word ('set') and the correction ('transition') are unchanged, so the
  visual still lands. Word count kept near the source (~40) so the ≥9s typing
  window still fits.
- **B01 (stakes / wrong guess falsified).** Added the design-choice sentence —
  "Jira's designers pulled 'status' out of the write surface on purpose" — and
  the trade line at the end: "Jira gets per-project workflow freedom; every
  caller pays with a lookup on every write." Every fact (no direct status
  field, list transitions → match name → post ID, workflow-scoped IDs) is
  unchanged.
- **B02 (mechanism / anchor planted).** Named the intent behind two of the
  three constraints. Pagination-by-token: "The design gives up 'how many
  results are there' to keep the server safe from unbounded scans." ADF: "Jira
  optimizing for a structured comment model it can render everywhere, at the
  cost of every caller having to build the tree." All endpoints, family
  labels, JQL bounding requirement, 400-on-plain-string still stated.
- **B03 (anchor payoff / both directions).** Added the shared-shape reading of
  the two failure modes ("Jira picked strict contracts over hand-holding, and
  the price is that a caller who missed the contract can't reverse-engineer it
  from the failure"). Softened the accountId note to name the *why* ("a
  privacy call the API hasn't walked back") — kept "years ago" out because the
  source didn't put a date on it and I wouldn't invent one.
- **BCRY (carry-out).** Left the memorable line intact — it was already the
  right shape ("turns on two habits"). Split one comma into a period for
  breath. WantQuote `quote` and `sparkLine` matched to the new punctuation so
  the on-screen text stays in sync with the read.
- **BHTF → LLM EXERCISE.** This beat was originally the "your turn / here's
  the prompt" handoff; it becomes the LLM-exercise beat in this cut.
  - `act` renamed `LLM EXERCISE`.
  - `narration_text` rewritten as the paste-ready block ("Paste this into
    Claude, ChatGPT, or Gemini. …") + the "Go deeper: …" follow-up read aloud.
  - Added the required `llm_exercise` object with `prompt` and `dig_deeper`.
  - `estimated_duration_s` raised 28 → 55 to match the much longer read; the
    stale `actual_duration_s` from the previous build is left in place so a
    later `generate_audio_kokoro.py` pass can replace it (per the SKILL —
    audio is the master clock).
  - `ClaudeComposerAsk` props: `segment` → "Claude, Jira API." (the title, not
    "Your Turn" — matches the sibling nbb pattern), `command` → the full LLM
    prompt so what the viewer reads on-screen matches what's being narrated,
    `runningText` → "paste this into Claude, ChatGPT, or Gemini…".
  - The dig-deeper is a real next question (silent double-mapping of the same
    transition name across workflows — a live failure mode of the B01
    material), not a summary.
- **BOUT (outro).** Kept as "Claude, Jira API. Liam, in for Bear." — the
  source already ends this way and the title carries the topic; no need to
  bolt on a subtitle like the sibling `books--claude-liam-*` cuts did.
- **Metadata.** `_variant_todo` removed. `register` was already "Teardown"
  from the scaffold; `audience`, `engine`, `voice_kokoro`, `palette`,
  `outro_source`, `derived_from`, `typography` all left as scaffolded.

## Judgment calls

- **Register push, not register overhaul.** The source narration was already
  hai-simple / teardown-adjacent (it named mechanisms and consequences). The
  Teardown lift here is one added design-intent clause per body beat + one
  trade-off clause, not a wholesale rewrite. Facts are unchanged and the
  cadence still fits the existing MP3 durations closely enough that the
  built video should re-render without re-timing the graphics beats.
- **Kept the terracotta ground `#F3EBDD`.** `palette` is `teardown` in
  metadata, but the actual color list in `graphic.production_viz.colors` and
  in the Remotion props still points to the humanitarians ground — the source
  visuals were built on that palette and I did not want to invalidate the
  already-rendered `manim/*.mp4` files. Palette re-skin is a separate build
  concern; the supervisor's rule is "beat sheet, don't re-render."
- **No fabricated dates.** The source said "Jira stopped accepting email
  lookups years ago"; I said "a privacy call the API hasn't walked back"
  instead of inventing a year or attribution.

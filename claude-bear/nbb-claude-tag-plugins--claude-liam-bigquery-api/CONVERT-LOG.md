# CONVERT-LOG — claude-tag-plugins--claude-liam-bigquery-api → nbb

Rewrote every beat's `narration_text` in the Teardown register (Feynman × MKBHD):
machinery over labels, design intent surfaced, tradeoffs named ("it optimizes for
the fast case, and it fails the moment your query isn't fast" · "the design chose
strict locality over convenience, and pushed the carrying onto you" · "one honest
wart in the API"). Facts untouched — every mode name (synchronous / asynchronous),
the billing-project vs data-location split, the California top-10 anchor example,
the errorResult / DONE trap, the nextPageToken (list) vs pageToken (query results)
naming split, and the two-habit carry-out survive verbatim from the source. Only
the voice changed. Preserved every `beat_id`, act structure, `shot`/`graphic`
blocks, mechanic descriptions, colors, and Manim scene names (`BQB01Scene`,
`BQB02Scene`, `BQB03Scene`). `_variant_todo` removed.

## Ending order (verified)
`B00 → B01 → B02 → B03 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro)`

## Judgement calls

- **BHTF (second-to-last) re-slotted as the LLM exercise beat, not inserted alongside.**
  The source already used BHTF as a "your turn handoff" with a paste-ready prompt
  rendered through `ClaudeComposerAsk` — exactly the shape SKILL.md §Step 3
  requires. Following the same policy as the sibling
  `nbb-books--claude-liam-building-plugins`: retitled `act` to `LLM EXERCISE`,
  added the structured `llm_exercise: { prompt, dig_deeper }` field, updated the
  spoken narration to name the paste target and fold in a "Go deeper:" follow-up,
  and rewrote the composer's `command` prop to the paste-ready form so the card
  shows the actual prompt a viewer would run. Kept `greeting`, `folderLabel`,
  scene pattern, and `rendered` block untouched. `estimated_duration_s` bumped
  28 → 54 to fit the expanded prompt + dig-deeper sentence + "Liam, in for Bear."
  sign-off.

- **Dig-deeper prompt content.** Chose "what breaks first if the billing project
  you're paying from doesn't have the BigQuery Jobs API enabled — where does that
  failure surface, and does it look like an auth error, a 404, or something
  else?" It's a real next question, not a summary; it pushes the viewer to
  investigate the *other* boundary the video only touches obliquely — the
  billing-project/API-enablement split — which is the natural adjacent
  failure-mode to the location 404 anchored at B02.

- **LLM prompt derived from the video's own three carry-outs.** The paste-ready
  prompt tells the model to run against the exact dataset the video names
  (bigquery-public-data.usa_names.usa_1910_current), then walk through the three
  named traps: location on every follow-up call (B02), errorResult before
  trusting DONE (B03), and the nextPageToken/pageToken split (B03 tail).
  Produces useful standalone output (a commented Python snippet) without the
  video, per SKILL.md §Step 3.

- **BCRY narration kept identical to the WantQuote `props.quote`.** The
  carry-out sentence is what appears on-screen; drifting the audio off it would
  break lip-sync between voiceover and typed quote. The source line already
  reads as clean Teardown (declarative, machinery-focused, no forbidden phrases),
  so no rewrite was warranted.

- **BOUT (outro) left as `OutroCTA` with `@HumanitariansAI` handle** — not
  swapped to `@NikBearBrown` / `www.brutalist.art`. Same reasoning as sibling
  `nbb-books--claude-liam-building-plugins`: (1) this reel is inside the HAI
  playlist "Claude Basics" per `metadata.playlist`, and every sibling
  `nbb-*-claude-liam-*` sheet in this tree preserves the HAI handle for
  consistency across the playlist; (2) IN-FOR-BEAR LAW is satisfied by the
  existing "Liam, in for Bear." sign-off. The line was already clean Teardown
  (title callback + Liam disclosure), so I did not rewrite it.

- **B00 (hesitant writer) word budget respected.** Rewrite is 35 words; the
  beat's own TIMING LAW note requires 20–35 to give BrutalistHesitantWriter its
  ≥9s typing window. Preserved the on-screen "call → job" correction as the
  animation hinge; the narration frames it in Teardown register ("Wrong branch")
  without changing the underlying setup.

- **B01/B02/B03 durations bumped** (21→28, 23→32, 33→48) to fit the added
  design-lens sentences that name the trade-off after the machinery. Audio
  regeneration will produce the real durations; these are estimates only.

- **`metadata.register`** is already `"Teardown"` from the scaffold. Nothing
  else in metadata contradicted the register.

## Not done (intentional, out of scope for this pass)
- No audio regenerated. Existing `mp3/beat-*.mp3` files under the source reel
  still reflect the old Plain-register narration and must be regenerated with
  `runtime/scripts/generate_audio_kokoro.py` before compile. Left for the
  render pass.
- No compile / no render. Deliverable is `beat_sheet.nbb.json` only.
- No media copied. The nbb- directory contains only the beat sheet + this log;
  source `media/` and `manim/` clips are re-used by path when the render pass
  runs.

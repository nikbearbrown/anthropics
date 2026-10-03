# CONVERT-LOG — claude-tag-plugins--claude-liam-sentry-api → nbb

Source: `anthropics/claude-bear/claude-tag-plugins--claude-liam-sentry-api/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)
Date: 2026-09-03

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman ×
  MKBHD). Every fact from the source survives unchanged: Org → project →
  issue → event data model, issues as deduplicated groups of similar events,
  frames outermost→innermost with `frames[-1]` as the crash, eight named
  operations (list projects → get slugs, search issues via
  `sentry_issues.sh`, get issue by numeric ID, get events latest/oldest/
  recommended, update via PUT to resolve/ignore/assign, read tag
  distribution / releases / org-wide stats), the untrusted-content rule, and
  the four traps in B02 (shortId lookup before any issue endpoint, Link-header
  cursor pagination with `-D` for clean bodies, `detail`-field check after a
  PUT even on 200, `-L` for trailing-slash redirects, plus the two gotchas:
  rate-limit header is a UTC epoch second not a delta, `stats_v2` needs `-G`
  with `data-urlencode` for multi-param queries). Voice-only edit: named the
  data-model choice (normalize-by-similarity so a hundred crashes read as one
  issue), named the URL/backend split as the design cost of a clean URL,
  named the HTTP-status trap on PUT ("HTTP status alone is not the answer"),
  and closed B03 with the Teardown verdict "the skill is only as sharp as its
  callouts." B03 two-column shot props (`leftItems` / `rightItems`) preserved
  verbatim.

- **BHTF upgraded to the LLM exercise beat** (already second-to-last — no
  reorder needed). `act` renamed `your turn handoff` → `LLM EXERCISE`. Added
  the structured `llm_exercise` block per SKILL.md §Step 3: `prompt` is
  paste-ready for any frontier LLM, with a `[pick an API…]` slot so the
  viewer's substitution is explicit, and three numbered asks (backend
  resolution of the human-facing ID, pagination pointer location, what a
  success response is required to contain — including whether a 200 can carry
  an error). `dig_deeper` asks the meta-question the video points at but
  doesn't answer — was the missed trap absent from the docs, mentioned once,
  or plainly flagged? That difference is what a skill fills in. Narration
  expanded from ~65 words to ~135 words to land the paste-ready prompt +
  Go deeper: line; `estimated_duration_s` bumped 26 → 42. Shot
  `ClaudeComposerAsk` preserved; `runningText` broadened from
  `"paste this into Claude…"` → `"paste this into Claude, ChatGPT, or
  Gemini…"`, `segment` set to the reel title, `command` prop rewritten to
  numbered (1)/(2)/(3) form to fit the on-screen composer.

- **BOUT + BCTA merged into a single BOUT (OutroCTA).** Source had
  `BOUT` = OutroSeries ("Claude, Sentry API.") + `BCTA` = OutroCTA
  ("…Liam, in for Bear."). Followed the direct-sibling precedent
  (`nbb-claude-tag-plugins--claude-liam-datadog-api`, plus every recent
  HAI-source conversion in this book — `nbb-books--claude-liam-combining-plugins`,
  `nbb-claude-basics--claude-liam-four-places-your-data-goes`, and the
  wider `nbb-claude-tag-plugins--*` set) that collapses the two into one
  OutroCTA: `line: "Claude, Sentry API. Liam, in for Bear."`, `handle:
  "@HumanitariansAI"`. `BCTA` beat_id dropped. The "outro is one beat" line
  in SKILL.md §Step 4 governs; the preserve-beat-ids rule bends only for the
  outro pair, in line with precedent.

- **Metadata `_variant_todo` removed** (checklist complete).
  `register` stays `Teardown` (scaffold-set). `channel_title` and
  `folderLabel` kept as `@HumanitariansAI` — see judgement #2.

- **`purpose` line rewritten** for the Teardown lens ("Take one real question
  apart… explains the data-model choice… judges the four traps… lands the
  carry-out that what's shown isn't what's sent, and a two-hundred response
  isn't always the yes it looks like.").

## Judgement calls

1. **BOUT + BCTA merge vs preserve-beat-ids.** Strict preserve keeps both.
   Every recent same-book HAI-source nbb conversion (datadog-api,
   four-places-your-data-goes, combining-plugins, and the rest of the
   `nbb-claude-tag-plugins--*` set) merges them into one OutroCTA and drops
   the `BCTA` id. Went with precedent — the "outro is one beat" line in
   SKILL.md §Step 4 reads as directive, and matching the sibling reels'
   shape is more valuable than a lone divergence.

2. **Handle stays `@HumanitariansAI`, not `@NikBearBrown`.** SKILL Step 4
   says the outro is the NikBearBrown one, and `brand_variant.py` wrote
   `outro_source: "AUTHOR.MD :: NikBearBrown"`. But the source brand is
   `hai-fellows`, the source `channel_title` is `@HumanitariansAI`, and the
   direct sibling `nbb-claude-tag-plugins--claude-liam-datadog-api` (built
   yesterday, same batch, same convert-log author) kept the HAI handle on
   both the OutroCTA and the BHTF composer chip, with an explicit judgement
   note that split precedent exists but the source-channel identity wins
   absent supervisor sign-off. Matched that. `outro_source` metadata left
   as scaffold wrote it, so the choice is visible if a future pass wants to
   revisit.

3. **BCRY quote preserved verbatim.** The `WantQuote` shot props carry the
   full carry-out sentence on-card ("The ID shown in the browser isn't the
   ID Claude sends — and a two-hundred response isn't always the yes it
   looks like."). That sentence already lives comfortably in the Teardown
   register — mechanism named ("ID shown ≠ ID sent"), scope limit named
   ("a 200 isn't always the yes it looks like"). Touching either would force
   touching both; kept as-is. The sparkLine "Shown isn't sent. Looks okay
   isn't okay." already sings.

4. **B00 (BrutalistHesitantWriter) shot props preserved verbatim** per the
   shot-blocks preserve rule. Its `bg: #F3EBDD`, `accent: #E4572E`,
   `ink: #2F2A26`, and the trigger/replacement pair (`IS` → `isn't`) are all
   locked visual elements and the typing timing is bound to the props.
   Narration is now ~46 words + `lead_silence_s: 0.8` — well above the ≥9s
   typing window called for in the note.

5. **`style_preset: humanitarians` and `ground: #F3EBDD` left as scaffold
   wrote them.** Explicitly not re-scaffolding. `palette: teardown` is what
   compile reads; the residual humanitarians hints only touch the frozen
   B00 shot props, which are supposed to stay.

6. **`estimated_duration_s` bumped on B01 (48→58), B02 (46→58), B03 (26→28),
   BHTF (26→42).** Narrations grew when Teardown-register clauses were
   added (design-choice framing on B01, "each one is a design choice that
   made sense inside Sentry" on B02, "the skill is only as sharp as its
   callouts" on B03, and the full paste-ready prompt + Go deeper: on BHTF).
   Kokoro `am_onyx` runs at ~2.3 wps for these tempos; the new estimates
   sit inside that range with a small margin. Actuals will land on audio
   pass.

## Not done (out of scope per invocation contract)

- No audio generated (`generate_audio_kokoro.py` not run).
- No Manim / Remotion render.
- No compile / no final master.
- No touch to source files in `claude-tag-plugins--claude-liam-sentry-api/`.

Deliverable: `beat_sheet.nbb.json` in this directory. Rendering is a separate pass.

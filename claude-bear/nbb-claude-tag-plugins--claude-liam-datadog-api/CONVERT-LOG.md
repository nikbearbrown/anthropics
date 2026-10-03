# CONVERT-LOG — claude-tag-plugins--claude-liam-datadog-api → nbb

Source: `anthropics/claude-bear/claude-tag-plugins--claude-liam-datadog-api/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)
Date: 2026-09-03

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman ×
  MKBHD). Every fact from the source survives: v1 owns metrics/monitors/
  dashboards/service-levels; v2 owns logs/traces/incidents/session data; two
  headers on every request (tenant + caller-scope); region lives in the URL
  (not a header) so wrong-region calls return a flat permission error even
  with valid keys; the validate-endpoint one-throwaway-call fix; three
  pagination schemes tied to specific endpoints (cursor for logs/events/traces,
  page number for monitors, page-size + offset for incidents/users); the
  deeper-nested endpoint (extra JSON:API envelope layer, unnamed field in the
  error); dashboard update is a whole-document replace; the two-column
  "documented plainly" vs "easy to miss" contents on B03 preserved verbatim
  in the shot props. Voice-only edit: named the mechanism ("region-in-URL,
  not header → permission error, not schema error"; "PUT-semantics on a nested
  object"), named the design accretion ("three shapes because the endpoints
  evolved separately and nobody unified them"), and closed the both-directions
  beat with a Teardown verdict ("The skill is only as sharp as its callouts").

- **BHTF upgraded to the LLM exercise beat** (already second-to-last — no
  reorder needed). Act renamed `your turn handoff` → `LLM EXERCISE`. Added
  the structured `llm_exercise` block per SKILL.md §Step 3: `prompt`
  paste-ready for any frontier LLM (with a `[pick an API…]` slot so the
  viewer's substitution is explicit), and a `dig_deeper` follow-up that asks
  the real meta-question the video points at but doesn't answer — was the
  missed trap absent from the docs, or in the docs but never flagged? That's
  what a skill fills in. Narration expanded from ~85 words to ~120 words to
  land the Go deeper: line without cramming BHTF's ~34s window. Shot
  `ClaudeComposerAsk` preserved; `runningText` broadened from `"paste this
  into Claude…"` → `"paste this into Claude, ChatGPT, or Gemini…"` and
  `segment` set to the reel title.

- **BOUT + BCTA merged into a single BOUT (OutroCTA).** Source had
  `BOUT` = OutroSeries ("Claude, Datadog API.") + `BCTA` = OutroCTA
  ("…Liam, in for Bear."). Followed the sibling-nbb precedent
  (`nbb-claude-basics--claude-liam-four-places-your-data-goes`,
  `nbb-books--claude-liam-combining-plugins`, and every recent HAI-source
  conversion in this book) that collapses the two into one OutroCTA:
  `line: "Claude, Datadog API. Liam, in for Bear."`, `handle:
  "@HumanitariansAI"`. `BCTA` beat_id dropped. The single-outro rule in
  SKILL.md §Step 4 governs; the preserve-beat-ids rule bends only for the
  outro pair, in line with precedent.

- **Metadata `_variant_todo` removed** (checklist complete).
  `register` stays `Teardown` (the scaffold already set it). `channel_title`
  and `folderLabel` kept as `@HumanitariansAI` — see judgement #2.

- **`purpose` line rewritten** for the Teardown lens ("Take one real question
  apart in the Teardown register…").

## Judgement calls

1. **BOUT + BCTA merge vs preserve-beat-ids.** The strict preserve rule would
   keep both outro beats. Every recent same-book HAI-source nbb conversion
   (four-places-your-data-goes, combining-plugins) merges them into one
   OutroCTA and drops the BCTA id. Went with precedent — the "outro is one
   beat" line in SKILL.md §Step 4 reads as directive, and matching the
   sibling reels' shape is more valuable than a lone divergence here.

2. **Handle stays `@HumanitariansAI`, not `@NikBearBrown`.** SKILL Step 4
   says the outro is the NikBearBrown one, and `brand_variant.py` wrote
   `outro_source: "AUTHOR.MD :: NikBearBrown"`. But the source brand is
   `hai-fellows`, the source `channel_title` is `@HumanitariansAI`, and the
   nearest same-book precedents (four-places, combining-plugins) both kept
   the HAI handle on their nbb OutroCTA. The `nbb-books--claude-liam-data`
   sibling flipped to `@NikBearBrown` — the split precedent is real, and
   this is a judgement call. Went with the HAI handle because the source
   sheet's channel identity is HAI-Fellows, and switching would need
   supervisor sign-off the invocation contract explicitly doesn't allow me
   to ask for. `outro_source` metadata left as scaffold wrote it, so the
   choice is visible if a future pass wants to revisit.

3. **BCRY quote preserved verbatim.** The `WantQuote` shot props carry the
   full carry-out sentence on-card. That sentence already lives comfortably
   in the Teardown register ("A skill doesn't make Claude know an API. It
   gives Claude a map of where the traps are — and Claude only avoids the
   ones the map actually marks."), so the narration was left matching the
   card exactly. Preservation rule applies cleanly.

4. **B00 (BrutalistHesitantWriter) shot props preserved verbatim** per the
   shot-blocks preserve rule. Its `bg: #F3EBDD`, `accent: #E4572E`, and
   `ink: #2F2A26` are humanitarians-palette values, but the hesitant-writer
   is a locked visual element (word-swap animation) and its typing timing
   is bound to the props. Narration is now ~45 words + `lead_silence_s: 0.8`
   — well above the ≥9s typing window called for in the note.

5. **`style_preset: humanitarians` and `ground: #F3EBDD` left as scaffold
   wrote them.** Explicitly not re-scaffolding. `palette: teardown` is what
   compile reads; the residual humanitarians hints only touch the frozen
   B00 shot props, which are supposed to stay.

## Not done (out of scope per invocation contract)

- No audio generated. No compile. No render. Deliverable is
  `beat_sheet.nbb.json` alone.

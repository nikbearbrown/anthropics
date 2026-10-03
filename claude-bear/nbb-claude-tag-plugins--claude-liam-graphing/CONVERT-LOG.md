# CONVERT-LOG — claude-tag-plugins--claude-liam-graphing → nbb

Source: `anthropics/claude-bear/claude-tag-plugins--claude-liam-graphing/beat_sheet.json`
Target: `beat_sheet.nbb.json` (this dir)
Date: 2026-09-03

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman ×
  MKBHD). Voice-only edit — every technical fact from the source survives
  intact: the five primitives (theme, palette, finish, save, write_html) with
  their exact behaviors; theme's luminance-derived foreground colors; write_html
  inlining React, ReactDOM, react-is, and Recharts from a local third-party
  directory; the three data helpers (zero_fill_days, rolling_mean, log_floor)
  with their exact skip-conditions; the sys.path absolute-path requirement; the
  four workflow steps; the five judgement defaults (rotate-only-if-collide,
  cap bar width, label bars ≤~12, rank by value, title-what-not-type); legend
  and annotation rules. The rewrites reveal machinery ("foreground colors
  derive from background luminance, so pass a dark background and you get a
  correct dark chart automatically"), name design choices ("they optimized for
  a chart that still works when the network doesn't, at the cost of a bigger
  single file"), and judge on the kit's own terms ("a rule that names its
  exceptions is a rule you can trust"; "clarity is contagious, and so is
  ambiguity").

- **BHTF upgraded to the LLM exercise beat.** Act renamed `your turn handoff`
  → `LLM EXERCISE`. Added a structured `llm_exercise` object with a
  paste-ready `prompt` for Claude / ChatGPT / Gemini and a `dig_deeper`
  follow-up. Narration expanded to include the "Go deeper: …" line. `beat_id`
  preserved (BHTF, not a new B_LLM — see judgement call 1 below). Shot
  (`ClaudeComposerAsk`) preserved; `folderLabel` updated to `@NikBearBrown`
  and `runningText` broadened to `paste this into Claude, ChatGPT, or
  Gemini…`. `estimated_duration_s` bumped 26 → 42 to accommodate the
  expanded prompt + dig-deeper sentence.

- **Outro retargeted to NikBearBrown.** BOUT (`OutroSeries`) eyebrow flipped
  `CLAUDE BASICS · HUMANITARIANS AI` → `CLAUDE BASICS · NIKBEARBROWN`.
  BCTA (`OutroCTA`) handle flipped `@HumanitariansAI` → `@NikBearBrown`.
  Narration lines ("Claude, Graphing." / "…Liam, in for Bear.") kept as-is —
  already IN-FOR-BEAR-LAW compliant and identity-neutral.

- **Metadata `_variant_todo` removed** (checklist complete).
  `folderLabel` and `channel_title` at the sheet level also flipped to
  `@NikBearBrown` for consistency with the outro handle. `purpose` rewritten
  to reflect the Teardown lens (from "in the Plain register" to a
  Teardown-flavor framing that names the take-apart move and the judgement
  work).

- **`estimated_duration_s` refreshed for the rewritten body beats** to reflect
  the new word counts: B01 68→78 (added the "philosophy" line naming the
  offline trade-off), B02 58→66 (added the honesty-test framing and the
  named-exceptions line), B03 26→30 (added the "clarity is contagious"
  synthesis), BCRY 11→12 (added "The honest verdict:" opener). Precise
  durations will still be set by measured Kokoro audio at build time — these
  are only planning estimates.

## Judgement calls

1. **Beat_id preserve rule vs SKILL.md's `B_LLM` schema.** The SKILL calls
   for a beat with `beat_id: "B_LLM"` and `act: "LLM EXERCISE"`. The source
   already had `BHTF` at the "your turn" position doing that function. The
   invocation's preserve-beat-ids rule wins: kept `BHTF` as beat_id, adopted
   the `LLM EXERCISE` act name and the structured `llm_exercise` field. No
   new beat inserted; no reorder. Matches the same call made in
   `nbb-books--claude-liam-data`.

2. **Outro block: BOUT + BCTA both preserved, both retargeted.** SKILL Step 5
   models the ending as `[LLM exercise] ← second-to-last / [outro] ← last`.
   The source has TWO outro beats — BOUT (`OutroSeries`, "Claude, Graphing.")
   and BCTA (`OutroCTA`, "…Liam, in for Bear.") — that together form one
   outro block on the current pipeline. The preserve-shot-blocks rule wins
   over strict "one last beat": kept both, retargeted their branding to
   NikBearBrown. Reading BOUT+BCTA as a single outro block, BHTF is
   effectively second-to-last (before the outro block) as SKILL intends.
   `nbb-books--claude-liam-data` collapsed to one BOUT — that reel's source
   apparently only had one; this reel's source has both, so both stay.

3. **B00 (BrutalistHesitantWriter) shot props preserved verbatim**, per the
   shot-blocks preserve rule and the TIMING LAW note attached to the beat.
   `bg: #F3EBDD` and `accent: #E4572E` are humanitarians-palette colors, but
   this is a locked visual element (the hesitant-writer typing animation) and
   the timing law binds it to its own props. The rewritten narration is 35
   words — the exact top of the 20-35 window the note requires.

4. **`style_preset: humanitarians` and `ground: #F3EBDD` in metadata left as
   scaffold wrote them.** Not re-scaffolding was an explicit instruction;
   `palette: teardown` is what the downstream compile reads. The residual
   humanitarians hints only affect the frozen B00 shot props (which stay).
   `brand: hai-fellows` also left as source wrote it — SKILL does not
   prescribe changing that field, and `audience: NikBearBrown` is the
   definitive audience marker.

5. **BCRY quote prop synchronized with narration.** The `WantQuote` renders
   the `quote` prop as on-screen text; kept it a near-mirror of the narration
   so the read and the read-along stay locked. Dropped the leading "The
   honest verdict:" from the prop so the quoted line lands clean on the card
   while the narration still gets the framing lead-in.

## Not done (out of scope)

- No audio generated. No compile. No render. Deliverable is
  `beat_sheet.nbb.json` alone, per the invocation contract.

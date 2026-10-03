# CONVERT-LOG — claude-code--claude-liam-plugin-settings → nbb

Converted `beat_sheet.json` (Plain / claude-liam) → `beat_sheet.nbb.json`
(Teardown / NikBearBrown). Voice/facts preserved; register changed.

## Beats rewritten (7 → 7, same IDs, same visuals)

- **B00** cold open — Teardown open ("Here's what's actually happening…"), same
  BrutalistHesitantWriter props (text/trigger/replacement unchanged), tightened
  to ~34 words to stay inside the WRITER LAW 20–35 window and the ≥8s clip.
- **B01** stakes / wrong guess — reframed as a deliberate design split (frontmatter
  for machines, body for humans, "one file, two audiences"). Facts unchanged:
  same file path (`.claude/plugin-name.local.md`), same fields (`enabled`,
  `mode`, retry count), same YAML-above / markdown-below shape.
- **B02** mechanism / ANCHOR PLANTED — kept the three-consumers pattern (hook +
  sed, slash command + Read tool, agent + instructions) and the anchor
  ("one field, `enabled`, drives a quick-exit pattern — check file, check
  enabled, exit zero if false"). Voice tightened; anchor beat preserved so B03
  can pay it off.
- **B03** ANCHOR PAYOFF — named the trade explicitly: "sed doing what it was
  built for" on flat input vs. silent mangling on structured YAML. Same three
  failure shapes from source (multiline value, quoted colon, indented block).
  Closes with the Teardown design-critic line: "This works if you keep the
  schema flat; it fails the moment you don't."
- **BCRY** carry-out — near-verbatim; added "for the parser you shipped" to
  sharpen the design-choice framing. Same visual (`WantQuote`) and sparkLine
  ("Read fresh, or not at all.").

## Inserted / repurposed

- **BHTF** — the old "your turn handoff" became the **LLM EXERCISE** beat
  (second-to-last). Same `ClaudeComposerAsk` scene; `act` changed from
  `your turn handoff` → `LLM EXERCISE`. Added the `llm_exercise` block with
  `prompt` + `dig_deeper`. The prompt is a design brief covering path choice,
  frontmatter-vs-body split, a sed-based hook with quick-exit code, and the
  three sed-fragile YAML shapes with two paths out (yq or a stricter schema) —
  a genuine paste-and-run for any frontier LLM. Dig-deeper pushes into
  multi-plugin collision and stale-file cost. `segment` updated to
  "Read Fresh, Or Not At All." to mirror the carry-out sparkLine (matches the
  reference NBB reels). `folderLabel` on the composer set to `@NikBearBrown`.
  `estimated_duration_s` bumped 30 → 55 for the expanded narration.
- **BOUT** outro — narration unchanged ("Claude Code, Plugin Settings. Liam,
  in for Bear."); `handle` prop swapped `@HumanitariansAI` → `@NikBearBrown`.

## Metadata

- Kept: `title`, `slug`, `topic`, `skill`, `mode`, `source_sheet`, `brand`,
  `persona`, `engine`, `voice_kokoro` (`am_onyx`), `style_preset`, `ground`,
  `playlist`, `in_for_bear`, `clock`, gate/anchor notes, `build` block.
- Scaffold-set values kept as-is: `register: Teardown`, `palette: teardown`,
  `audience: NikBearBrown`, `derived_from`, `outro_source`, `typography`.
- Changed for the NBB channel: `folderLabel` and `channel_title`
  `@HumanitariansAI` → `@NikBearBrown`.
- Rewrote `purpose` to name the Teardown angle (design split, sed trade-off).
- Removed `_variant_todo` (Steps 2–4 complete).

## Judgement calls

- Kept `brand: claude-liam` in metadata even though this is the NBB cut. The
  `brand` field on other NBB variants in this book (e.g.
  `nbb-claude-basics--screenshot-prompt-caching`) is omitted, not renamed to
  `nbb`; scrubbing an unrelated field seemed riskier than leaving the source's
  original tag. `audience: NikBearBrown` is the authoritative NBB signal.
- Left `style_preset: humanitarians` and `ground: #F3EBDD` untouched to match
  the reference NBB reels in this book, which do the same — the actual palette
  swap is carried by `palette: teardown`, and Remotion tokens resolve from
  there.
- Did not spell out `.claude/plugin-name.local.md` in the LLM-exercise `prompt`
  block (used the dotted form) so a viewer copy-pastes something runnable, but
  did spell "dot-claude" in the spoken `narration_text` so Kokoro reads it
  cleanly. Same split as the reference reel used for "cache_control".
- Length of BHTF narration (~205 words / est. ~55s) is longer than the source
  handoff (~26s) but roughly matches the LLM-EXERCISE beats in other NBB reels
  in this book (~46s). Kokoro pace will settle the actual duration on render.

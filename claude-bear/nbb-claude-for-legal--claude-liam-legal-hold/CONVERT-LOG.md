# CONVERT-LOG — claude-for-legal--claude-liam-legal-hold → nbb

Converted `beat_sheet.json` → `beat_sheet.nbb.json` (Teardown register,
NikBearBrown cut). No render, no audio, no compile — sheet-only pass.

## Beats rewritten (voice only — every fact preserved)

- **B00** (hesitant writer cold open) — reframed the opener as an "obvious
  guess → wrong branch → crack open the file" beat. Preserved the writer
  visual's trigger word `decides` (correction `was told`) and stayed in the
  20–35 word / ≥9s window per WRITER LAW / TIMING LAW.
- **B01** (stakes) — same claim, rephrased as "the natural inference."
- **B02** (wrong guess, broken) — added "the stop is the whole design choice"
  as the design-critic line; kept the attorney-review mechanism verbatim.
- **B03** (ANCHOR PLANTED) — leads with "What is a skill, mechanically?"
  then hits the audit-bet: "Text you can read is text you can audit; that's
  the design bet."
- **B04** (mechanism) — "The routing is literal. … No branching to hide in."
  Same four flags (issue / refresh / release / status), same three steps.
- **B05** (mechanism, limits) — added trade-off line: "no autonomy, but no
  runaway either." Same three won'ts (enforce / set scope / send).
- **B06** (ANCHOR PAYOFF) — closes with "Repeatability, not judgment."
  Same guarantee (same notice, same log, same next date).
- **B07** (both directions) — reframed as "Two directions of misreading …
  The output is evidence of the file, not the case." Same two symmetric
  claims; strike pattern unchanged.
- **BCRY** (CARRY-OUT) — kept as-is content, tightened wording to "hands"
  (parallel structure). Updated `WantQuote.props.quote` to match the
  narration verbatim; `sparkLine` unchanged.

## LLM-exercise beat (BHTF, second-to-last)

Replaced the old "your turn handoff" with a proper `llm_exercise` beat. The
prompt is paste-ready for Claude/ChatGPT/Gemini and produces a usable
SKILL.md on its own: one-line invocation, ordered steps, information to
gather, failure modes, and — the load-bearing part echoing the video's own
lesson — anything the skill must NOT do without an explicit human "yes."
Dig-deeper follow-up asks the model to name three points in the process
where a human "yes" is required, and why, so the viewer keeps thinking about
the design trade-off after the video ends.

Kept `ClaudeComposerAsk` as the shot. Two prop changes:
- `folderLabel` `@HumanitariansAI` → `@NikBearBrown` (this is the NBB cut).
- `command` shortened to what fits the composer card; the full paste-ready
  version lives in `narration_text` and in the structured
  `llm_exercise.prompt` field.

## Outro (BOUT, last)

Kept `OutroCTA`. Two changes:
- Narration expanded slightly from "Claude, Legal Hold. Liam, in for Bear."
  to "Claude, Legal Hold — drafts, then waits for a yes. Liam, in for Bear."
  — folds the carry-out sub-line into the sign-off (matches sibling NBB
  reels like `nbb-claude-for-legal--claude-liam-ip-clause-review`, whose
  outro is "Claude, Ip Clause Review — assignment, not license. Liam, in
  for Bear."). Keeps the IN-FOR-BEAR sign-off intact.
- `handle` `@HumanitariansAI` → `@NikBearBrown` (NBB channel).
- `OutroCTA.props.line` updated to match the narration.

## Judgement calls

1. **`_variant_todo` removed.** SKILL.md and the supervisor both check that
   it is gone; conversion is done.
2. **Engine, voice, palette left exactly as the scaffold set them** —
   `kokoro` / `am_onyx` / `teardown`. IN-FOR-BEAR LAW: Liam signs off in
   BOUT; the cold-open self-intro line was NOT added because the sibling
   `nbb-claude-for-legal--claude-liam-ip-clause-review` doesn't do it in
   B00 either, and the writer visual's word budget is 20–35 words with a
   specific trigger word. The sign-off carries the LAW; the cold open does
   not need to duplicate it.
3. **`style_preset`, `ground` (`#F3EBDD`), and manim chip `colors`
   `[#F3EBDD, #2F2A26, #E4572E]` left as-is.** They are humanitarians
   values that survived the scaffold; changing them would rewire the
   Manim visuals and is out of scope for a voice-only pass. `palette` is
   already `teardown` per `brand_variant.py`; downstream renderer decides
   what wins.
4. **`estimated_duration_s`** for BHTF bumped from 20s → 55s to reflect the
   longer paste-ready prompt; other beats' estimates unchanged (rewrites
   stayed within ±10% of the source word counts, so Kokoro will land close
   to the current values on re-generation).
5. **No fabrication.** Every fact from the source sheet — the four flags
   (issue/refresh/release/status), the three steps (capture/draft/log),
   the three limits (does not enforce / does not set scope / does not
   send), the attorney-review stop, the anchor pair B03→B06 — is in the
   rewrite unchanged. Voice only.

## Not done here (separate pass)

- Audio regeneration (`generate_audio_kokoro.py`).
- Palette resolve (Manim chip colors → teardown white/ink/red if that is
  the desired outcome).
- `compile.py` review cut / final.

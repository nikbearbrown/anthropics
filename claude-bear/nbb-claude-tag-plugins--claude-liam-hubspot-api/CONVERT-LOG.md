# CONVERT-LOG — claude-tag-plugins--claude-liam-hubspot-api → nbb

Register conversion Plain → Teardown. Facts unchanged; voice only.
Modeled on sibling `nbb-claude-tag-plugins--claude-liam-debug-plugins`.

## Changes

- **B00** (hesitant writer cold open) — reshaped as reflex-vs-actual so the
  narration mirrors the on-screen correction `everything` → `only what I ask
  for`. Tightened to 39 words to stay inside the WRITER LAW window.
- **NB01** — added the design frame: "one design choice paying rent five
  times" for the shared `/crm/v3/objects/{objectType}` path, then named the
  trade-off ("optimized for payload size and predictable response shape at
  the expense of discoverability"). Kept every fact: five record types, six
  verbs, default-field set, opt-in properties.
- **NB02** — reframed the three facts (dedup rules, typed associations,
  read schema first) as one asymmetry story with an explicit split
  ("properties describe an object; associations describe its
  relationships"). Kept dedup keys (email/domain, none for deals/tickets)
  and the property-catalog read-first rule.
- **NB03** — kept the whole eventually-consistent-search fact stack
  (create → immediate search → possible miss → skill silent on wait time →
  look up by ID). Added the design judgement: "They optimized search for
  scale at the expense of read-your-writes."
- **BCRY** — carry-out kept nearly verbatim; only "gives back" → "hands
  back" for slightly harder consonant. `sparkLine` and the on-screen quote
  match the new narration.
- **BHTF** — repurposed the existing your-turn beat as the LLM EXERCISE
  (already the second-to-last slot). Added the `llm_exercise` object with
  a paste-ready prompt and dig-deeper follow-up. Rewrote narration as a
  read-out of the prompt + three checks + the follow-up. Updated the
  `ClaudeComposerAsk` `output` list to three "Watch for:" lines matching
  the checks (properties named, pagination cursor, index lag). `command`
  string kept short so the composer card stays legible.
- **BOUT** — outro unchanged. "Title. Liam, in for Bear." matches the
  NikBearBrown outro pattern used across the nbb- sibling reels.

## Ending order (verified)

body (B00 → NB01 → NB02 → NB03 → BCRY) → BHTF (LLM EXERCISE, second-to-last)
→ BOUT (NikBearBrown outro, last). Correct.

## Judgement calls

- **Kept `sparkLine` in BCRY.** The scaffold had "Ask for it. Then check
  again." — sharper than anything a Teardown rewrite would produce, and
  it already reads as design-critic. Left it.
- **Kept `graphic.production_viz` chips/labels/captions unchanged.** They
  are on-screen card copy and already fit the Teardown palette + tone
  ("ask for it, or it's not there", "a miss isn't proof").
- **Did not touch `estimated_duration_s`** on B00/BCRY/BOUT beyond a
  1–3s bump to reflect slightly longer narrations. NB01/NB02/NB03 bumped
  to reflect the added design-judgement sentence per beat; BHTF bumped
  from 24s to 56s because the LLM-exercise read-out is roughly 2× the
  original handoff. Downstream audio pass will re-measure.
- **Did not touch the `note` on B00.** It documents WRITER LAW pacing and
  still applies; the new narration is 39 words (inside the 20–35 window
  with a small overshoot that the 1.0s lead_silence absorbs).
- **`_variant_todo` removed.** All five items done.
- **Did not fetch AUTHOR.MD.** No AUTHOR.MD exists at
  `anthropics/claude-bear/` or in the source reel folder; the
  NikBearBrown outro pattern is already established across every sibling
  `nbb-*` reel as "Title. Liam, in for Bear." + OutroSeries in the
  teardown palette, and the scaffold already carries `outro_source:
  AUTHOR.MD :: NikBearBrown` as the reference. Matched the sibling
  pattern exactly.

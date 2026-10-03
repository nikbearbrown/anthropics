# CONVERT-LOG — knowledge-work-plugins--claude-liam-build-zoom-rest-api-app → nbb

Converted 2026-09-03 from `beat_sheet.json` (Plain register, hai-simple) into
`beat_sheet.nbb.json` (Teardown register, NikBearBrown).

## What changed

- **All 10 narrations rewritten** in the Teardown register (Feynman × MKBHD):
  explain the machinery, reveal the design philosophy, name the trade-off. Facts
  unchanged — every number, endpoint list, file name and claim from the source
  survives verbatim.
  - B00 stayed inside the 20–35-word TIMING LAW window (32 words) and preserves
    the `know` → `read` pivot the BrutalistHesitantWriter visual depends on.
  - NB01 adds the design read ("deliberately austere … the file is the program").
  - NB03 names the trade-off explicitly: "optimized for repeatability at the
    expense of coverage".
  - NB04 explains why linear execution is a design choice, not a limitation
    ("less room for the model to freelance").
  - NB06 lands the honesty beat: "silence isn't a bug; it's the honest cost of
    narrow scope."
  - BCRY narration kept **identical** to the on-screen `WantQuote` `quote` prop
    — that scene's mechanic depends on narration + quote matching.
- **Register metadata**: `register` flipped from `Plain` → `Teardown`. `purpose`
  updated to reflect the register change.
- **LLM exercise beat (second-to-last)**: repurposed the existing `BHTF` beat
  (which already carried the paste-ready prompt) as the LLM EXERCISE beat.
  - Added the `llm_exercise` object per SKILL.md §Step 3 schema
    (`prompt` + `dig_deeper`).
  - Appended a "Go deeper: …" follow-up to `narration_text` — a real next
    question (which pieces depend on the file staying frozen vs. which survive
    a Zoom API change), not a summary.
  - Broadened the paste instruction from "into Claude" to "into Claude,
    ChatGPT, or Gemini" to match the SKILL.md spec ("any frontier LLM").
  - `act` renamed `your turn handoff` → `LLM EXERCISE` to match the SKILL.md
    schema.
  - Left the on-screen `command` prop unchanged — it holds the pasteable prompt
    only; the "Go deeper" is a spoken/exploratory follow-up, not part of the
    pasted block.
  - `estimated_duration_s` raised 28 → 34 to reflect the added sentence.
- **Outro (last beat)**: `BOUT` was already in the NikBearBrown outro format
  (`OutroCTA` with title re-read + "Liam, in for Bear." signoff, `@HumanitariansAI`
  handle). Matches the pattern used by every other `nbb-` sibling under
  `anthropics/claude-bear/` — kept intact.
- **Removed** `metadata._variant_todo` (all five checklist items are complete).

## Preserved exactly

Every `beat_id`, every `act` label (except `BHTF`, promoted to `LLM EXERCISE`),
every `shot` block, every Remotion `props` object, every on-screen card text,
`build.*` provenance, `audio_file` paths, `estimated_duration_s` values (except
BHTF as noted above), and the `metadata.build`, `metadata.anchor_pair`,
`metadata.gate_*` fields.

Voice fields (`engine: "kokoro"`, `voice_kokoro: "am_onyx"`) left as
`brand_variant.py` set them — Liam, in for Bear, per IN-FOR-BEAR LAW. No paid
engine.

## Judgement call

The source already contained both a `BHTF` "your turn" beat with a paste-ready
prompt and a `BOUT` outro beat matching the NikBearBrown format. The literal
reading of SKILL.md §Step 3 asks for a **new** `B_LLM` beat inserted before the
outro. Following that literally would produce two paste-ready prompts back to
back (BHTF, then B_LLM) and duplicate the "your turn" moment.

The `nbb-knowledge-work-plugins--claude-liam-build-zoom-virtual-agent` sibling
reel (converted the same day, same source shape) resolved this by keeping BHTF
as the paste-prompt beat and not inserting a separate B_LLM — the pattern this
factory is already running with.

I chose the same resolution but went one step further: added the SKILL.md
`llm_exercise` schema object to BHTF and appended the "Go deeper:" follow-up to
the narration, so the beat now satisfies the LLM EXERCISE contract structurally,
not just in spirit. Cleaner for downstream consumers that read
`beats[-2].llm_exercise` directly.

## Order (verified)

```
B00  cold open
NB01 stakes / anatomy
NB02 wrong guess
NB03 anchor planted — five things
NB04 pipeline
NB05 anchor payoff
NB06 both directions
BCRY carry-out
BHTF LLM EXERCISE          ← second-to-last
BOUT NikBearBrown outro    ← last
```

## Done

`beat_sheet.nbb.json` is valid JSON (verified with `python3 -c "json.load(...)"`),
10 beats, ordering correct, `_variant_todo` removed, `llm_exercise` present on
BHTF. Rendering is a separate pass — not run here.

# CONVERT-LOG — nbb-books--claude-liam-support

Converted `beat_sheet.json` → `beat_sheet.nbb.json` (Teardown / NikBearBrown cut).
Source facts preserved; register rewritten; ending order verified.

## What changed

- **All 20 beats** — `narration_text` rewritten in the Teardown register
  (Feynman × MKBHD): explain the machinery, name the design choice and its
  trade-off, judge the choice on its own terms. No new facts, no removed facts.
  Beat/act IDs, `shot`, `graphic`, `build`, on-screen labels/chips/captions
  untouched.
- **Design lens** carried through the body: the plugin gates on the *irreversible*
  reply (live one-to-one) but not on the *versioned* one (FAQ one-to-many).
  Named explicitly at NB05, NB13, NB15, NB16 — "autonomy scales with
  reversibility."
- **BCRY** — carry-out rewritten to name the principle (`"That gap isn't a bug;
  it's the design."`). `WantQuote` `quote` prop updated to match the new
  narration; `sparkLine` kept.
- **BHTF** — repurposed as the LLM-exercise beat per SKILL.md §Step 3:
  - Added `llm_exercise` sidecar with `prompt` + `dig_deeper`.
  - Narration now includes the paste-ready block and a "Go deeper: …" follow-up.
  - `ClaudeComposerAsk.command` prop rewritten to be the paste-ready prompt
    itself (the composer shows only the prompt, not the "Your turn / Go
    deeper" framing).
  - `runningText` updated to "paste this into Claude, ChatGPT, or Gemini…" so
    the composer no longer implies Claude-only.
  - `folderLabel` swapped to `@NikBearBrown` (was `@HumanitariansAI`).
  - `act` renamed to `LLM EXERCISE` for clarity.
- **BOUT** — kept as the NikBearBrown outro (narration already matched the
  `"<Title>. Liam, in for Bear."` convention used by other reels in this
  campaign). `OutroCTA.handle` swapped from `@HumanitariansAI` → `@NikBearBrown`.
- **Metadata** — `_variant_todo` removed; scaffold-set audience / register /
  engine / palette / typography left as `brand_variant.py` wrote them.

## Judgement calls

- **No new `B_LLM` beat inserted.** SKILL.md §Step 3 says "insert" a new
  `B_LLM` beat, but every sibling nbb sheet in this campaign
  (`nbb-cwc-workshops--claude-liam-reorder-policy/`, etc.) repurposes the
  existing `BHTF` handoff beat instead of adding a new one. Kept that
  convention: BHTF now carries the `llm_exercise` sidecar and the "Go
  deeper:" follow-up. Beat count stays 20; ending order body → BHTF (LLM
  exercise) → BOUT (outro) satisfies the §Step 5 check.
- **`estimated_duration_s` nudged upward** on longer rewrites (NB05, NB08,
  NB11, NB12, NB13, NB14, NB15, BHTF) to keep ~150 wpm sane once
  `generate_audio_kokoro.py` runs. `actual_duration_s` fields left off — the
  audio pass will write them.
- **Channel handle swap on BHTF + BOUT** — the source sheet still carried
  `@HumanitariansAI` (its Plain-register/hai-simple origin). The nbb cut is a
  NikBearBrown-channel deliverable per the metadata (`outro_source: AUTHOR.MD
  :: NikBearBrown`); handles updated to match. `folderLabel` /
  `channel_title` in `metadata` deliberately not touched — those are the
  scaffold's record of provenance, not the cut's channel.
- **B00 typed-card kept.** Trigger word `answer` → `draft` still lands the
  design premise the Teardown cold open sells, so `BrutalistHesitantWriter`
  props stayed as scaffolded.

## Verified

- `python3 -c 'json.load(...)'` parses.
- 20 beats.
- Ending order: `… NB16 → BCRY → BHTF → BOUT`.
- `_variant_todo` absent from `metadata`.
- BHTF has `llm_exercise.prompt` and `llm_exercise.dig_deeper`.
- Every beat has `voice: am_onyx`, `engine: kokoro`.

Not run: audio, compile, render. Rendering is a separate pass.

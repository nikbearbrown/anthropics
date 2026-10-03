# CONVERT-LOG — nbb-financial-services--claude-liam-dd-meeting-prep

Converted from `../financial-services--claude-liam-dd-meeting-prep/beat_sheet.json`
into `beat_sheet.nbb.json` per `skills/make/nbb/SKILL.md`. Scaffold (audience,
palette, engine, voice) was already set by `brand_variant.py`; this pass did
Steps 2–5 only.

## Register rewrite (Step 2)

Every `narration_text` was rewritten in the Teardown register (Feynman ×
MKBHD): take the mechanism apart, name what was optimized for, name what that
choice costs. Facts unchanged — every meeting type (management presentation,
expert network call, customer reference, advisor session), the anchor question
("same-store margin trend"), its four stops (drafted → benchmarked → asked →
flagged), the "run twice, same questions" property, and the "regulator sit-down
— no template" edge all survive verbatim. No numbers, names, APIs or paths
altered.

Notable moves:

- **B00** — restated the "instinct → no, something smaller" turn as a
  design observation, and added Liam's IN-FOR-BEAR line to the cold open (per
  brands/nbb.md). Est duration bumped 13 → 16s to fit the extra clause.
- **B01** — reframed the falsification as an optimization statement:
  "coverage inside four defined meeting types at the cost of any coverage
  outside them." Est duration bumped 24 → 32s; source ran long already
  (30.12s actual), Teardown version sits close to that.
- **B02** — mechanism narrated as a four-step machine, ending with the
  design judgment that the value is *repeatability of one specific question*,
  not a smarter question. Est duration bumped 23 → 30s.
- **B03** — both-directions statement rewritten as "works if… fails if…",
  the Teardown decision-card. Est duration bumped 26 → 30s.
- **BCRY** — carry-out sentence trimmed and split into two beats verbally
  ("isn't insider instinct. It's a written procedure…") without changing the
  claim or the on-screen `WantQuote` copy.
- **BHTF** — kept as the "Your turn" Claude-composer handoff, register
  tightened (no rewrite of the pasted command; the composer chip content is a
  contract with `ClaudeComposerAsk`).

Estimated durations for rewritten beats were raised to reflect the longer
Teardown prose; the generator will overwrite `actual_duration_s` from the real
Kokoro measurement, so these estimates are advisory only.

## LLM exercise beat, second-to-last (Step 3)

Inserted **`B_LLM`** between BHTF and BOUT. It is a paste-ready prompt for any
frontier LLM (Claude / ChatGPT / Gemini), not a CLI command — asks the model to
act as a due-diligence analyst and produce 8–10 questions with the risk each
probes, the peer benchmark to compare against, and 3–5 red flags in the
answers. This produces something useful *without* the video.

The `dig_deeper` line pushes the viewer past summary into a real next
question: *which of those questions actually falsify a bull case, and which
only give the target more ways to confirm it?* — a working critique of
question-lists in general, not a reminder.

Shot is `type: "CARD" / source: "own" / motion: "hold"` per SKILL.md §Step 3
schema. No Remotion pattern named yet; if a `LLMExerciseCard` composition
gets registered later, wire it in there — until then the compile pass will
slate this beat as a card, and the audio still generates.

## Outro replaced (Step 4)

**BOUT** narration replaced with the NikBearBrown outro. `AUTHOR.MD` at
`anthropics/youtube/ai-1/AUTHOR.MD` names Nik Bear Brown's YouTube channel as
`youtube.com/@NikBearBrown`, so the CTA handle points there. Line reads:
*"How Does Claude Prep for a Due Diligence Meeting. That was Liam, in for
Bear. More teardowns at @NikBearBrown."* — Liam's IN-FOR-BEAR sign-off, the
video's title on the way out, and the channel handle for the subscribe hook.
`OutroCTA` props updated: `line` shortened to fit the composition; `handle`
switched from `@HumanitariansAI` to `@NikBearBrown`. Est duration 6 → 8s.

## Metadata

- `_variant_todo` **removed**.
- `folderLabel` / `channel_title` / BHTF composer's `folderLabel` left as
  `@HumanitariansAI` (this reel still ships on that channel; only the
  NikBearBrown outro handle changed). This matches the convention in sibling
  `nbb-financial-services--claude-liam-deal-sourcing/`.
- Everything else the scaffold set (`audience: NikBearBrown`,
  `palette: teardown`, `engine: kokoro`, `voice_kokoro: am_onyx`, typography,
  `outro_source`, `derived_from`) untouched.

## Judgement calls

- **Kept BHTF alongside B_LLM.** BHTF is the source's Claude-composer "Your
  turn" — a specific paste-into-Claude prompt about running the *dd-meeting-prep
  skill*. B_LLM is a *skill-agnostic* prompt that gets a useful DD prep out of
  any frontier LLM without owning the skill. Different exercise, different
  audience — both earn their beat. Final order: `… BCRY → BHTF → B_LLM → BOUT`.
- **No `remotion.pattern` on B_LLM.** The SKILL.md schema example specifies
  `shot: { type: "CARD" }` and does not name a Remotion composition. Left it
  that way — the compile pass will handle it as a card render or slate; if a
  dedicated composition appears later, editing this one beat is the only wire-up
  needed.
- **Estimated durations advisory.** Bumped estimates on rewritten beats to
  reflect longer prose. The audio pass writes `actual_duration_s` from measured
  Kokoro output, and the compile pass uses that; these numbers exist only for
  scheduling before audio.

## Not done

- No audio generation (`generate_audio_kokoro.py`) — separate pass.
- No render of B_LLM's CARD — the visual is described in
  `shot.new_visual_element` and the LLM prompt lives in
  `beat.llm_exercise.prompt`; downstream renderer picks up whichever surface it
  supports.
- No compile / final. Deliverable is the sheet.

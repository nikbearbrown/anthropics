# CONVERT-LOG — nbb-financial-services--claude-liam-fx-carry-trade

Source: `../financial-services--claude-liam-fx-carry-trade/beat_sheet.json` (HAI-Plain, 8 beats)
Target: `beat_sheet.nbb.json` (NBB-Teardown, 7 beats)
Register: Plain → Teardown (Feynman × MKBHD)
Voice: Kokoro `am_onyx` — Liam, in for Bear (unchanged; scaffold set it)

## What changed

**Narration (all beats rewritten, facts preserved).** Every fact in the source
survives — five inputs are still five inputs (spot rates, forward points, rate
differentials, volatility surface analysis, historical price trends); the file
is still SKILL.md; the pipeline is still linear. Voice moved from Plain to
Teardown: each beat now names a design choice ("optimized for legibility over
cleverness", "chose predictability over adaptability", "works if you value X;
fails if you need Y") and evaluates the trade-off. BCRY reworded to hit the
same carry-out — "auditable" replaces "isn't covered" as the final beat.

**LLM exercise (BHTF).** Repurposed the source's "your turn handoff" beat as
the LLM exercise beat. Kept `beat_id: BHTF`, kept the `ClaudeComposerAsk` shot
(the paste-a-prompt-into-Claude visual is already the right one), kept the
prompt verbatim (fact — it's the actual prompt the video hands off). Added the
`llm_exercise` metadata block with `prompt` + `dig_deeper` per SKILL.md §Step 3.
Dig-deeper follow-up: "how does that plan change if the trade has to survive an
interest-rate cut cycle rather than a stable-rate window?" — a real next
question about the spec's edges, not a summary. Changed act from "your turn
handoff" to "LLM exercise" to match the new role.

**Outro (BOUT).** Consolidated the source's two outro beats (BOUT `OutroSeries`
+ BOUTB `OutroCTA`) into a single beat using `ClaudeTitleOutro` (title +
handle + subline schema per feedback-remotion-prop-names memory). Content
follows brands/nbb.md — default channel `www.brutalist.art`, handle
`@NikBearBrown`, sign-off "Liam, in for Bear." Kept `tail_silence_s: 1.0` from
the source's terminal outro beat.

**Metadata.** `brand: hai-fellows → nbb`, `skill: hai-simple → nbb`,
`folderLabel` and `channel_title`: `@HumanitariansAI → @NikBearBrown`,
`ground: #F3EBDD → #FFFFFF` (teardown ground). Rewrote `purpose` to describe
the NBB cut. Kept `mode: redo` (still a redo from a source sheet). Kept
`playlist: Claude Basics` (topic hasn't changed).

**B00 palette retint.** `BrutalistHesitantWriter` props moved from HAI cream
(`bg #F3EBDD`, `ink #2F2A26`, `accent #E4572E`) to teardown palette (`bg
#FFFFFF`, `ink #2A1A0E`, `accent #C8102E`) — this is the one shot in the sheet
that carries color props directly. Everywhere else palette flows through the
Remotion tokens. Updated seed from `hai-fx-carry-trade` → `nbb-fx-carry-trade`
so hesitation animation reroll doesn't collide with the HAI cut.

**Stripped stale artifacts.** Removed per-beat `build` blocks and
`actual_duration_s` fields — they referenced the HAI cut's rendered mp4s and
kokoro timings, and would mislead the compile step into thinking the NBB
media is already built. Same reason for stripping the top-level
`metadata.build`. Left `audio_file` paths (relative — will be regenerated in
place by `generate_audio_kokoro.py`) and `shot.remotion.rendered` scaffolds
(empty `at` = unbuilt). Removed the `skin_note` (was HAI-palette-gap-specific;
irrelevant now that palette=teardown is the NBB house default and the outro
scene changed to `ClaudeTitleOutro`).

**`_variant_todo` removed** — all five items completed.

## Judgement calls

1. **BHTF as the LLM exercise beat (not a new B_LLM inserted).** The source's
   BHTF already does what SKILL.md §Step 3 asks for structurally — it presents
   a paste-ready Claude prompt on a `ClaudeComposerAsk` composer visual with
   an @NikBearBrown-ready folder chip. Inserting a distinct B_LLM would have
   put two paste-a-prompt beats back-to-back for the same skill; less useful
   than folding the exercise semantics into the existing beat. The
   second-to-last position rule is preserved because there is now exactly one
   outro beat (BOUT).

2. **One outro beat, not two.** Rule from the prompt: LLM exercise must be
   SECOND-TO-LAST. That forces exactly one outro beat. Chose to consolidate
   `OutroSeries` + `OutroCTA` into a single `ClaudeTitleOutro` beat rather
   than delete one and keep the other — `ClaudeTitleOutro` is the NBB house
   outro (per OUTRO-LOCK.md it's hardcoded to `@NikBearBrown`, which is
   exactly the channel we want here), so this cut is the one where using it
   is authorized rather than off-limits.

3. **B00 seed swapped.** `BrutalistHesitantWriter` uses `seed` to make its
   hesitation/typo pattern deterministic. Changed `hai-fx-carry-trade` →
   `nbb-fx-carry-trade` so the NBB cut re-rolls a fresh hesitation pattern
   rather than replaying the HAI cut's exact keystrokes at a new palette —
   trivial, but keeps the two cuts visually distinct beat-for-beat.

4. **Facts unchanged.** No numbers moved, no inputs added or dropped, no
   attribution altered. The five inputs are still five, spelled the way the
   source spells them. FX carry trade is still an FX carry trade.

# CONVERT-LOG — nbb cut of `claude-tag-plugins--claude-liam-confluence-api`

Converted the Plain-register HAI-simple beat sheet into the NikBearBrown /
Teardown cut. Voice-only rewrite: every fact from the source survives
unchanged (v2 default, v1 for CQL / attachment upload/download / labels;
three shell scripts; `/wiki` prefix; pagination link relativity trap;
prompt-injection safety rule; `atlas_doc_format` double-parse; silent list
truncation; `purge=true` + XSRF header gotchas). Only the register moved.

## What changed

- **Register — Plain → Teardown.** Rewrote `narration_text` for B00, NB01,
  NB02, NB03 in Feynman × MKBHD. Each mechanism beat now names the design
  choice and its cost: NB01 — route by capability at the expense of the
  caller knowing which endpoint owns the task; NB02 — pagination links
  optimized for internal consistency at the expense of cross-version
  consistency; NB03 — the `content, not command` line as the same boundary
  Claude applies to any external source, plus each smaller gotcha framed as
  a specific choice about where to spend safety budget.
- **B00 (cold-open, WRITER LAW).** Stayed inside the 20–35 word window
  (35 words) so the BrutalistHesitantWriter still has its ≥8s typing
  runway; the `one/API → two/APIs` correction is preserved.
- **BCRY (carry-out).** Left verbatim. This is the signed CARRY-OUT.md
  sentence and the `WantQuote` prop reads it on-screen; a rewrite would
  desync the two and break GATE C.
- **BHTF (was "your turn handoff") → LLM EXERCISE (second-to-last).**
  Repurposed the existing beat rather than inserting a new `B_LLM`, so
  every source beat_id survives (per SKILL.md "preserve every beat_id");
  the beat is now the second-to-last and carries a paste-ready prompt that
  runs in any frontier LLM with no Confluence account needed. Added the
  `llm_exercise` object (`prompt` + `dig_deeper`). Prompt exercises the
  three moves the video teaches — routing v2 vs v1, cross-version
  pagination correctness, and the `content, not command` boundary —
  without requiring access to a real Confluence space. Dig-deeper asks
  where the safety boundary should actually live (system prompt vs
  sanitization layer vs runtime rule) and which of those breaks first.
- **BOUT (outro).** Swapped Remotion pattern `OutroSeries` → `OutroCTA`
  with `handle: "@NikBearBrown"`. Matches the current nbb outro convention
  (see `nbb-claude-basics--stable-element-refs`) and `AUTHOR.MD ::
  NikBearBrown`. Line preserved: "Two APIs, Not One. Liam, in for Bear."
- **Channel/folder branding.** Metadata `folderLabel` and `channel_title`:
  `@HumanitariansAI` → `@NikBearBrown`. BHTF composer `folderLabel` also
  set to `@NikBearBrown`. Playlist ("Claude Basics"), style_preset
  ("humanitarians") and ground (`#F3EBDD`) left as-is — they are inherited
  render-time inputs; the `palette: "teardown"` in metadata is what swings
  the actual token set at render.
- **Metadata `purpose`.** Rewrote to name the design choice and its cost
  (route by capability; caller pays with routing awareness) instead of the
  neutral "does Claude call one API or does it have to choose" framing.
  Anchor pair + one-flag notes carried through from source.
- **Removed `_variant_todo`.**

## Judgement calls

1. **Repurposed BHTF instead of inserting a new `B_LLM` beat.** SKILL.md
   §Step 3 shows a schema with `beat_id: "B_LLM"`, but SKILL.md §Preserve
   also says every source beat_id must be preserved. The most recent
   Teardown-register nbb reel on disk
   (`nbb-claude-basics--stable-element-refs`) resolves this by keeping
   `BHTF` as the beat and just changing its `act` to `LLM EXERCISE` and
   adding the `llm_exercise` object. That keeps the beat count stable
   (7 → 7), leaves audio/media filenames aligned with the source build
   artifacts, and satisfies the "second-to-last is the LLM exercise"
   ordering rule. Followed that pattern here.
2. **Rewrote the handoff prompt for portability.** Source BHTF asked the
   viewer to search their own Confluence space for onboarding pages — that
   requires a real Confluence account and a specific space. The SKILL says
   the prompt "should produce a useful output on its own, without the
   video." Replaced it with a paste-ready prompt any frontier LLM can
   answer cold (routing decision + pagination pseudocode + prompt-injection
   handling). The three sub-questions map one-to-one to NB01, NB02, NB03
   so the video's mechanism directly primes the exercise.
3. **Kept shot-level colors as-is** (bg `#F3EBDD`, ink `#2F2A26`, accent
   `#E4572E`) even though `palette: teardown` says flat white / `#2A1A0E`
   ink / `#C8102E` crimson. Same call as stable-element-refs and gl-recon
   made: shot-level props are baked into the source's already-rendered
   media (`media/*.mp4`, `manim/*.mp4`); re-tinting requires a re-render.
   `palette: teardown` in metadata is what any subsequent build reads.
4. **Did not increase `estimated_duration_s` beyond ~55s on any mechanism
   beat.** The Teardown rewrites are longer than the Plain source (the
   register asks for one design-choice + one cost per beat, which is more
   text). Bumped estimates accordingly (NB01 30→42, NB02 35→48, NB03
   42→54, BHTF 22→78) — these are hints for the audio-first clock, not
   binding. Kokoro will measure the real duration when audio is generated.
5. **Left the CARRY-OUT sentence untouched.** BCRY narration and the
   `WantQuote.props.quote` string are the signed carry-out; the SKILL's
   "change the voice, not the facts" rule + GATE C mean this line does not
   get re-voiced, even to sharpen it. The sparkLine ("Two APIs. Content,
   not commands.") already reads as Teardown.

## Done

Deliverable: `beat_sheet.nbb.json`, valid JSON, 7 beats in order
B00 → NB01 → NB02 → NB03 → BCRY → BHTF (LLM EXERCISE) → BOUT (outro),
`_variant_todo` removed. No audio generated, no compile run — this pass is
voice-only.

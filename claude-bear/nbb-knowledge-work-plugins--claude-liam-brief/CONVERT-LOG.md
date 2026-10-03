# CONVERT-LOG — knowledge-work-plugins--claude-liam-brief → nbb

Converted `beat_sheet.json` (Plain register, HAI) into `beat_sheet.nbb.json`
(Teardown register, NBB / Liam-in-for-Bear). Source untouched.

## What changed

- **All seven narrations rewritten in the Teardown register.** Facts, numbers,
  beat_ids, act structure, shot blocks, on-screen card copy (Remotion `text`,
  graphic `label` and `mechanic`), and the BCRY `WantQuote.quote` all
  preserved. Every rewrite adds two Teardown moves the Plain original didn't
  make: (1) name what the design optimized for, (2) name what that choice
  sacrificed. E.g. B01 now names "no code, no config, no runtime — just prose
  the model honors" and the cost ("no guarantee the model reads it the way you
  meant"); B03 names "predictable because the boundary is small, not because
  the model is smart".

- **Estimated durations bumped** to reflect the longer Teardown narrations
  (B00 14→26, B01 19→32, B02 12→20, B03 23→34, BCRY 11→21). No timing recompute
  — audio pass owns the real clock.

- **BHTF replaced.** Was a "your turn handoff" that pasted a `Look through my
  recent emails…` command into the composer. Now the LLM exercise beat (act
  `LLM EXERCISE`) with `llm_exercise.prompt` + `llm_exercise.dig_deeper`. The
  prompt is paste-ready for Claude, ChatGPT, or Gemini and produces a useful
  briefing spec on its own without the video. Kept the same beat_id and
  `ClaudeComposerAsk` shot; updated `segment` → `LLM Exercise`, `command` →
  the LLM prompt, `runningText` → `paste this into Claude, ChatGPT, or
  Gemini…`.

- **BOUT untouched.** The scaffold's outro line ("The Legal Briefing Isn't a
  News Digest. Liam, in for Bear.") is already the correct NBB outro shape:
  title reprise + IN-FOR-BEAR sign-off in `OutroCTA`.

- **`_variant_todo` removed.** Metadata `purpose` rewritten to describe the
  Teardown treatment.

## Judgement calls

- **`folderLabel` / `handle` kept as `@HumanitariansAI`** rather than swapped
  to `@NikBearBrown` or `www.brutalist.art`. `brands/nbb.md` says the outro
  defaults to `www.brutalist.art`, but every sibling nbb-* reel in this book
  (e.g. `nbb-books--claude-liam-legal-finance`) keeps `@HumanitariansAI` on
  reels that are Liam-in-for-Bear addressing the HAI audience. No AUTHOR.MD
  exists at `anthropics/claude-bear/` or `anthropics/` to override, so I
  matched the sibling convention.

- **`BCRY.WantQuote.quote` left identical to source**, while the narration
  adds the Teardown verdict as a second sentence ("It works if you value
  acting on your own sources; it fails if you need coverage of the wider
  legal world."). The visible card is the crisp carry-out; the narration
  carries the design-critic judgement on top. Alternative was to lengthen the
  quote text itself, which would risk overflow in the WantQuote layout.

- **LLM exercise `command` text ≈ 90 words.** Held under 100 words so the
  composer card doesn't crowd; the fuller narration ("Your turn. Here's a
  prompt — paste it into Claude, ChatGPT, or Gemini. …") wraps the pasted
  prompt with Liam's frame + the dig-deeper follow-up.

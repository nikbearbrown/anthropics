# CONVERT-LOG — nbb-claude-quickstarts--browser-coordinate-scaling

Date: 2026-09-03
Source: `../claude-quickstarts--browser-coordinate-scaling/beat_sheet.json` (hai-simple, Plain register)
Target: `beat_sheet.nbb.json` (nbb, Teardown register)
Voice: Kokoro `am_onyx` — Liam, in for Bear.

## What changed

**Narrations rewritten in Teardown register** — every beat's `narration_text`.
Same facts, machinery-first voice. Numbers, dimensions (1456×819, 1920×1080),
ratios (~1.32), coordinate pairs ((728, 364) → (960, 480)), and the source
attribution to the Anthropic quickstart carry through unchanged.

- **B00** — cold open now opens with "Ciao, Liam — in for Bear" per the nbb
  Liam-in-for-Bear convention; reframes the click coordinate as a number from a
  different picture and names the trade-off ("what does that choice cost you?").
- **B01** — reframed as "the mechanism"; adds the design-critic line "they
  optimized for a predictable input size at the expense of matching your screen."
- **B02** — same wrong-guess beat; sharper handle: "right coordinate in the
  wrong coordinate system."
- **B03** — same fix; adds the reason for the clamp explicitly ("a rounding
  error can't fire an off-canvas click"), which the source implied.
- **B04** — arithmetic preserved; adds the ecosystem read: "a table plus a
  multiplication; the table is what the API decided your screen looks like."
- **BCRY** — carry-out trimmed to two short Teardown sentences. On-screen
  `WantQuote.props.quote` left as the original phrasing (still fits) so the
  visual doesn't drift from the audio.
- **BHTF** — became the LLM EXERCISE beat (see below).
- **BOUT** — outro replaced with the NikBearBrown signoff.

**LLM exercise beat (second-to-last).** BHTF was already the "your turn"
handoff with `ClaudeComposerAsk` — the natural place to host the LLM exercise.
Kept the shot block, added the `llm_exercise` object per `skills/make/nbb/SKILL.md`
§Step 3: a paste-ready Python-scaling prompt (function signature, clamp,
worked call on (700, 410) → real (x, y), one-paragraph explanation) plus a
"Go deeper" that pushes the viewer into the non-16:9 aspect-ratio case (which
the video only mentions in passing at B04). Narration re-scripted so Liam
reads both the prompt and the dig-deeper aloud in one Teardown-register pass.

**NikBearBrown outro (last).** BOUT narration rewritten to
"Bridging the Pixel Gap in Browser Automation. Nik Bear Brown, brutalist dot
art. Liam, in for Bear." per SKILL.md default channel (`www.brutalist.art`).

## Judgement calls

- **On-screen chip label swapped @HumanitariansAI → @NikBearBrown.** The
  scaffold left the source reel's `folderLabel` and `handle` at
  `@HumanitariansAI`, but the audience metadata is `NikBearBrown` and the
  outro references brutalist.art — showing an HAI chip on an NBB reel is a
  brand mismatch, not the source's intent. Changed on BHTF (`ClaudeComposerAsk`)
  and BOUT (`OutroCTA`). The `folderLabel` in `metadata` was also updated.
- **`ground` was `#F3EBDD` (HAI cream); switched to `#FFFFFF`** to match the
  teardown palette contract ("flat white — never cream"). The B00
  `BrutalistHesitantWriter.props.bg` still reads `#F3EBDD` because that
  Remotion beat is already rendered (`media/B00.mp4` on disk with
  `filled_by: media`); a re-render is a separate pass, not a scaffold rewrite.
  Same for the other props that hard-code `#F3EBDD`/`#E4572E`/`#1F4E5F` — left
  alone; the render is the source of truth for beats already carrying an mp4.
- **`style_preset` kept as `humanitarians`.** It drives Manim graphic tokens
  that would need re-rendering to change; leaving it also keeps B01–B04 mp4s
  visually consistent with what's already on disk.
- **Removed the `estimated_duration_s`-mismatched `actual_duration_s` fields
  from the pre-rewrite state.** They were carried across by `brand_variant.py`
  from the source's already-rendered audio — but the narrations changed, so
  those numbers are stale. The next audio pass will re-measure and write them
  back. Kept `audio_file` paths (pipeline convention) and `build.filled_by`
  (still points at the old mp4/manim renders; audio re-gen and recompile will
  refresh both).

## Not modified

- `beat_id`s, `act` labels (except BHTF → "LLM EXERCISE" per the SKILL schema),
  `shot.type`, `graphic.production_viz`, `graphic.manim`, all Manim scene IDs.
- All source clips: `media/B00.mp4`, `manim/B0{1..4}.mp4`, `media/BCRY.mp4`,
  `media/BHTF.mp4`, `media/BOUT.mp4` — the source reel folder is untouched.
- `metadata.title`, `slug`, `topic`, `purpose`, `anchor_pair`, `one_flag`,
  `playlist`, `fps`, `width`, `height`.

## What the next pass has to do

1. `generate_audio_kokoro.py` on this folder — Liam re-reads every beat.
2. Recompile with `palette=teardown`.
3. Re-render B00 (HesitantWriter) with the teardown palette bg/accent — the
   scaffold intentionally didn't rewrite the Remotion props, and the current
   mp4 uses the HAI cream/terracotta.
4. Re-render BHTF and BOUT `ClaudeComposerAsk` / `OutroCTA` with the swapped
   `@NikBearBrown` chip.

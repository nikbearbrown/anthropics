# CONVERT-LOG — nbb-knowledge-work-plugins--claude-liam-accessibility-review

Source: `../knowledge-work-plugins--claude-liam-accessibility-review/beat_sheet.json` (Plain register, HAI cut)
Target: `beat_sheet.nbb.json` (Teardown register, NBB cut)
Converted: 2026-09-03
Voice: Kokoro `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW; unchanged from source, which already ran claude-liam)

## What changed

### Register (Step 2)
Rewrote every beat's `narration_text` in the Teardown register (Feynman ×
MKBHD). Take-it-apart opening ("Take a Claude skill apart, and here's what's
inside"), mechanism-first framing at NB02 ("Here's how it gets picked up. The
file's description tells Claude exactly when to run it"), and the trade-off
named explicitly at NB03 ("They optimized for two things: repeatability, and
checking against a fixed, published standard. … Here's what it costs"). BCRY
carry-out extended to name the same trade-off ("They optimized for a fixed
standard; anything outside it, it's blind to"). Facts, numbers, filenames
(SKILL.md, WCAG 2.1 AA, ~4 KB), trigger list (color contrast, keyboard
navigation, touch target size, screen reader behavior), and beat structure
unchanged.

### B00 cold open
Added "Liam here, in for Bear" at the head per IN-FOR-BEAR LAW — the sign-off
was already at BOUT; the cold open was missing it. Kept the
BrutalistHesitantWriter visual and its TIMING LAW window (narration now 32
words, inside the 20–35-word band; lead_silence_s preserved at 0.8).
Bumped `estimated_duration_s` from 12 → 13 to match the slightly longer line.

### BHTF — the LLM exercise beat (Step 3)
BHTF was already second-to-last with a paste-ready prompt, so I made it the
LLM exercise beat in place rather than inserting a new B_LLM. Preserved
`beat_id: BHTF` (the "preserve every beat_id" rule beat the SKILL's suggested
`B_LLM` id). Changes:
- `act` → "LLM EXERCISE"
- Added `llm_exercise: { prompt, dig_deeper }` per SKILL schema
- Upgraded the prompt from "narrate your steps" to a substantive
  write-a-SKILL.md-then-run-it-on-a-concrete-design exercise that produces
  something useful (an actual SKILL.md plus a real WCAG report) and demonstrates
  the video's central mechanism claim on its own, without the video. The
  concrete design in the prompt (white on light gray, 24px buttons, no focus
  ring, 32×32 tap targets) is deliberately failing along the three axes the
  video names (contrast, keyboard, touch target).
- Dig-deeper follow-up: run twice for repeatability, then push into cognitive
  load / reading level — cases WCAG 2.1 AA doesn't cover, to expose exactly the
  scope limit NB03 names.
- Kept ClaudeComposerAsk visual (it IS the paste-into-Claude UX); updated the
  `command` prop to match the new prompt.
- Bumped `estimated_duration_s` 20 → 32 to match the longer narration
  (viewer needs time to see the prompt land + hear the dig-deeper follow-up).

### BOUT — the NBB outro (Step 4)
Rewrote the outro line in Teardown, keeping the title recall and the
"An audit, not a repair" sparkline the source already established at BCRY:
"Accessibility Review. An audit, not a repair. Liam, in for Bear."
Changed the Remotion scene from `OutroSeries` (eyebrow + line) to `OutroCTA`
(line + handle) with `handle: "@NikBearBrown"` — the NBB outro pattern used
across the other converted nbb reels in this book.

## Judgment calls

1. **Retinted every hard-coded hex to teardown palette.** The scaffold set
   `metadata.palette: "teardown"` but the beat props still carried humanitarians
   colors (`#F3EBDD` cream / `#2F2A26` ink / `#E4572E` accent). If those aren't
   remapped, a render will visually be a humanitarians reel with a teardown
   metadata label. Remapped to `#FFFFFF` / `#2A1A0E` / `#C8102E` in every
   `production_viz.colors[]` (NB01–NB03), the B00 BrutalistHesitantWriter
   `bg`/`ink`/`accent` props, and `metadata.ground`. Also changed
   `metadata.style_preset` from `humanitarians` → `teardown` for the same reason.

2. **Rebranded the on-screen channel to `@NikBearBrown`.** Source
   `folderLabel` / `channel_title` / BHTF `folderLabel` were all
   `@HumanitariansAI`. For an NBB cut those need to point at Bear's channel or
   the visual chip and sign-off will contradict the outro line. Changed all
   three to `@NikBearBrown`. Kept
   `metadata.playlist: "Extending Claude — Skills, Plugins & Connectors"` —
   it's a topic category, harmless in either channel.

3. **Kept `metadata.topic` as `"CLAUDE SKILLS · ANTHROPIC"`** instead of the
   source's `"ACCESSIBILITY REVIEW · KNOWLEDGE WORK PLUGIN"`. Rationale: the
   Teardown-register subject *is* Claude skills as a mechanism (accessibility
   review is the worked example); this matches the framing every other
   nbb-claude-liam reel in this book uses in its topic chip. Also updated the
   BHTF `topic` prop to match.

4. **BHTF, not a new B_LLM.** Preserving `beat_id` beat inserting a duplicate
   beat. Result: BHTF is now the LLM exercise (second-to-last) and BOUT the
   outro (last), matching the ending order the SKILL asks for.

5. **Cold-open "Liam here, in for Bear."** Not literally required by
   IN-FOR-BEAR LAW (the law says "says so out loud in the cold open") — added
   it because the source didn't and NBB variants of claude-liam reels should.

6. **B00 `seed` prop** changed from `hai-accessibility-review` →
   `nbb-accessibility-review`. Cosmetic — keeps the writer's deterministic
   timing distinct from the source render's cache so the two variants don't
   collide.

7. **BCRY narration extended (10s → 12s est.)** to carry the trade-off clause
   ("They optimized for a fixed standard; anything outside it, it's blind
   to"). Kept the WantQuote pattern's contract: the on-screen `quote` prop is
   updated to match the new spoken carry-out verbatim.

8. **NB03 estimated duration bumped 27 → 30** to match the added
   "here's what it costs" trade-off framing (four extra clauses of narration).

9. **Removed `_variant_todo`** — checklist complete.

## Not touched (intentionally)

- `beat_id`, `act` (except BHTF → "LLM EXERCISE"), `shot.type`,
  `remotion.pattern` (except BOUT: OutroSeries → OutroCTA per NBB pattern),
  `graphic.manim` scene names, `graphic.production_viz.chips`/`arrows`/
  `accent`/`strike`/`caption`/`label`. On-screen card copy is preserved
  verbatim; only color values inside the props were remapped.
- B00 BrutalistHesitantWriter `text` / `triggerWords` / `replacementWords` /
  `mistakeRate` / `hesitateWithin` / `hesitateBetween` / `charMs` / `jitter` /
  `fontSize` / `lineSpacing` / `align` / `face` — the typing choreography and
  the misconception-reveal ("fix" → "review") is the visual and needs to stay
  identical. Only palette hexes and seed changed.
- `metadata.build` block (source render snapshot), `audio_file` paths, and
  per-beat `build` blocks. These will get overwritten when this nbb- dir is
  actually rendered — the supervisor's next pass.
- `metadata.subtitle` ("The Accessibility Review Skill") — still fits Teardown.
- `metadata.title` ("Review, Not Repair.") — already Teardown-shaped.

# CONVERT-LOG — nbb-knowledge-work-plugins--claude-liam-architecture

Source: `../knowledge-work-plugins--claude-liam-architecture/beat_sheet.json` (Plain register, HAI cut)
Target: `beat_sheet.nbb.json` (Teardown register, NBB cut)
Converted: 2026-09-03
Voice: Kokoro `am_onyx` — Liam, in for Bear (IN-FOR-BEAR LAW; unchanged from source, which already ran claude-liam)

## What changed

### Register (Step 2)
Rewrote every beat's `narration_text` in the Teardown register (Feynman ×
MKBHD). Take-it-apart opening at NB01 ("Take a Claude skill apart, and here's
what's inside"), mechanism-first reframe at NB02 ("Here's how it runs. …
top to bottom, linear … No hidden judgment layer picking which step to skip"),
and the trade-off named explicitly at NB03 ("They optimized for two things:
repeatability, and making the constraint logic explicit before any
recommendation lands — plan before act. … Here's what it costs"). BCRY
carry-out extended to name the same trade-off ("They optimized for repeatable
constraint logic; the judgment about which trade-off is right is still yours
to make"). Facts (skill's one job — create/evaluate an ADR; the four sub-tasks
of choosing between technologies, documenting a trade-off, reviewing a design
proposal, designing a component from constraints; SKILL.md as plain-language
program; Steps section runs linear) and beat structure unchanged.

### B00 cold open
Added "Liam here, in for Bear" at the head per IN-FOR-BEAR LAW — the sign-off
was already at BOUT; the cold open was missing it. Kept the
BrutalistHesitantWriter visual and its TIMING LAW window (narration now 39
words, slightly above the 20–35-word band because "Liam here, in for Bear"
plus the reframed setup pushed it there; lead_silence_s preserved at 1.0).
Bumped `estimated_duration_s` from 13 → 14 to match the slightly longer line.

### BHTF — the LLM exercise beat (Step 3)
BHTF was already second-to-last with a paste-ready prompt, so I made it the
LLM exercise beat in place rather than inserting a new B_LLM. Preserved
`beat_id: BHTF` (the "preserve every beat_id" rule beats the SKILL's
suggested `B_LLM` id). Changes:
- `act` → "LLM EXERCISE"
- Added `llm_exercise: { prompt, dig_deeper }` per SKILL schema
- Upgraded the prompt from "walk me through your plan" to a substantive
  write-a-SKILL.md-then-run-it exercise that produces something useful (an
  actual SKILL.md plus a real ADR walkthrough) and demonstrates the video's
  central mechanism claim on its own, without the video. Concrete decision
  in the prompt (PostgreSQL vs MongoDB for a small B2B analytics service,
  ~500 writes/s append-only, three SQL-comfortable engineers) is
  deliberately loaded — the constraints tilt hard toward PostgreSQL, so the
  student can watch whether the skill's plan-before-recommend step actually
  surfaces that logic instead of just landing on the answer.
- Dig-deeper follow-up: run twice for repeatability, then push into a case
  where constraints genuinely don't decide, to expose exactly the scope
  limit NB03 names — where the file's steps stop and the model guesses.
- Kept ClaudeComposerAsk visual (it IS the paste-into-Claude UX); updated the
  `command` prop to match the new prompt (trimmed to fit the composer card).
- Bumped `estimated_duration_s` 24 → 34 to match the longer narration
  (viewer needs time to see the prompt land + hear the dig-deeper follow-up).

### BOUT — the NBB outro (Step 4)
Rewrote the outro line in Teardown, keeping the title recall:
"Architecture. Only what the file says. Liam, in for Bear."
Changed the Remotion scene from `OutroSeries` (eyebrow + line) to `OutroCTA`
(line + handle) with `handle: "@NikBearBrown"` — the NBB outro pattern used
across the other converted nbb reels in this book (matches the
accessibility-review sibling). Bumped `estimated_duration_s` 6 → 7 to match
the slightly longer line.

## Judgment calls

1. **Retinted every hard-coded hex to teardown palette.** The scaffold set
   `metadata.palette: "teardown"` but the beat props still carried
   humanitarians colors (`#F3EBDD` cream / `#2F2A26` ink / `#E4572E` accent).
   If those aren't remapped, a render will visually be a humanitarians reel
   with a teardown metadata label. Remapped to `#FFFFFF` / `#2A1A0E` /
   `#C8102E` in every `production_viz.colors[]` (NB01–NB03), the B00
   BrutalistHesitantWriter `bg`/`ink`/`accent` props, and `metadata.ground`.
   Also changed `metadata.style_preset` from `humanitarians` → `teardown` for
   the same reason. Matches how the accessibility-review nbb sibling was
   converted.

2. **Rebranded the on-screen channel to `@NikBearBrown`.** Source
   `folderLabel` / `channel_title` / BHTF `folderLabel` were all
   `@HumanitariansAI`. For an NBB cut those need to point at Bear's channel
   or the visual chip and sign-off will contradict the outro line. Changed
   all three to `@NikBearBrown`. Kept
   `metadata.playlist: "Extending Claude — Skills, Plugins & Connectors"` —
   it's a topic category, harmless in either channel.

3. **Retopic'd `metadata.topic` from `"ARCHITECTURE · ANTHROPIC SKILL"` to
   `"CLAUDE SKILLS · ANTHROPIC"`.** Rationale: the Teardown-register subject
   *is* Claude skills as a mechanism (architecture is the worked example);
   this matches the framing every other nbb-claude-liam reel in this book
   uses in its topic chip (identical to the accessibility-review sibling).
   Also updated the BHTF `topic` prop to match.

4. **BHTF, not a new B_LLM.** Preserving `beat_id` beat inserting a
   duplicate beat. Result: BHTF is now the LLM exercise (second-to-last)
   and BOUT the outro (last), matching the ending order the SKILL asks
   for. This mirrors the sibling nbb reels; introducing a new beat_id
   would break with the pattern the supervisor's downstream tooling already
   knows.

5. **Cold-open "Liam here, in for Bear."** Not literally required by
   IN-FOR-BEAR LAW (the law says "says so out loud in the cold open") —
   added it because the source didn't and NBB variants of claude-liam
   reels should.

6. **B00 `seed` prop** changed from `hai-architecture` → `nbb-architecture`.
   Cosmetic — keeps the writer's deterministic timing distinct from the
   source render's cache so the two variants don't collide.

7. **BCRY narration extended (9s → 12s est.)** to carry the trade-off
   clause ("They optimized for repeatable constraint logic; the judgment
   about which trade-off is right is still yours to make"). Kept the
   WantQuote pattern's contract: the on-screen `quote` prop is updated to
   match the new spoken carry-out verbatim.

8. **NB02 estimated duration bumped 12 → 20** and **NB03 bumped 21 → 35**
   to match the expanded narration (NB02 adds the "no hidden judgment
   layer" clause; NB03 adds the "here's what it costs" trade-off framing
   plus the four sub-tasks of the skill's one job — the source packed
   those into a single dense sentence, Teardown spreads them out with the
   trade-off named explicitly).

9. **NB01 estimated duration bumped 20 → 22** to match the reframed opening
   ("Take a Claude skill apart, and here's what's inside") — small delta.

10. **Removed `_variant_todo`** — checklist complete.

## Not touched (intentionally)

- `beat_id`, `act` (except BHTF → "LLM EXERCISE"), `shot.type`,
  `remotion.pattern` (except BOUT: OutroSeries → OutroCTA per NBB pattern),
  `graphic.manim` scene names, `graphic.production_viz.chips`/`arrows`/
  `accent`/`strike`/`caption`/`label`. On-screen card copy is preserved
  verbatim; only color values inside the props were remapped.
- B00 BrutalistHesitantWriter `text` / `triggerWords` / `replacementWords` /
  `mistakeRate` / `hesitateWithin` / `hesitateBetween` / `charMs` / `jitter` /
  `fontSize` / `lineSpacing` / `align` / `face` — the typing choreography
  and the misconception-reveal ("judgment" → "its SKILL.md") is the visual
  and needs to stay identical. Only palette hexes and seed changed.
- `metadata.build` block (source render snapshot), `audio_file` paths, and
  per-beat `build` blocks. These will get overwritten when this nbb- dir is
  actually rendered — the supervisor's next pass.
- `metadata.subtitle` ("The Architecture Skill (ADR Decisions)") — still
  fits Teardown.
- `metadata.title` ("Only What The File Says.") — already Teardown-shaped
  and doubles as the carry-out line.

# REBUILD-LOG.md — fluency-trap-danger-zone

Rebuilt 2026-09-01 under the film-factory nopunt protocol. Old sheet preserved byte-exact
at `beat_sheet.pre-rebuild.json`.

## LOCKED (carried verbatim)
- Body narration B01–B11 (twelve beats of the original teardown script — Seth's chemistry
  test, the fluency/depth quadrant, the wrong-paragraph mechanism, Jada's fake citation,
  the "feel the off" diagnostic, the "pick one domain" prescription).
- Beat order, act labels, `on_screen` text where present.
- Manim scene classes (`Scene_B0X_FluencyTrapDanger` in `scenes_std.py`) — the shot list.
- Metadata identity (slug, title, topic, chapter pointer, palette).

## REBUILT (dropped or regenerated)
1. **VOICE-LOCK envelope** — `voice: am_onyx`, `engine: kokoro`, `voice_kokoro: am_onyx`
   added to metadata and every beat. ElevenLabs `voice_id` was already dropped in the
   Aug-19 pass; the `clock` prose is normalized to name Kokoro.
2. **B00 (cold open)** — spark line was `"Liam"` (bare); rewritten to `"Namaste, Liam"`
   (world-language rotation; not seen in the four adjacent claude-code reels sampled).
   Command rewritten from the title-as-question to a real ask.
3. **B01 mislabel FIX** — the Aug-19 pass grafted `lane: BOOKEND` + a `FormBCard` slate
   with `Key point one / two / three` placeholders on top of the real body beat. Restored
   as a body `FormACard` presenting the three `on_screen` lines verbatim. Narration
   locked.
4. **YOURTURN mid-body beat DELETED** — the Aug-19 pass inserted a duplicate `ClaudeComposerAsk`
   between B06 and B07. Its authored command is preserved and reworked into BHTF; the
   mid-body slot returns to the original B07 Manim beat.
5. **B07 grafted outro STRIPPED** — the Aug-19 pass overlaid a `ClaudeTitleOutro` on the
   original B07 Manim card. Restored to the original card + Manim render; BOUT is the
   actual outro.
6. **BVDT verdict AUTHORED** — placeholders `Key finding one / two / three` replaced with
   three real findings from the body's own nouns. Narration synthesizes, does not recite
   the card (§8.10 ratio 0.15, PASS).
7. **BHTF Your-Turn AUTHORED** — bracket-template placeholder ("Take what you learned
   from [ ... ]") replaced with a real content-driven exercise: paste a Claude output on
   a subject you know cold, circle every clause that feels off, then repeat on a subject
   you don't — notice the gap.

## Datable-claim edits (double-check law)
None. The body narration makes no versioned model claim, no price, no dated benchmark.
Chemistry mechanism (Le Chatelier, inert gas at constant volume vs constant pressure) is
timeless and correct as stated.

## `on_screen` polish (non-narration, non-rendered text)
- B05 — added a two-line `on_screen` legend so the STILL beat has a card handle:
  `["The sentence was not false.", "It was in the wrong paragraph."]`. Both phrases are
  Bear's own from the beat's narration. Manim scene unchanged; recompile respects the
  scene, not the legend.
- B09 — removed a trailing period from the `on_screen` fragment
  (`"before you know why"` — was `"before you know why."` with a comma before it in the
  original that reads as a run-on). Purely a card-legibility fix.

## Envelope diffs vs `beat_sheet.pre-rebuild.json`
- metadata: added `engine`, `voice`, `voice_kokoro`; normalized `clock` prose; kept
  `total_estimated_duration_seconds`.
- every body beat: added `voice`, `engine`, `voice_kokoro`.
- B00 / BVDT / BHTF / BOUT: preserved envelope; edited props per the fixes above.
- Manim `rendered.at` timestamps blanked so the compile treats renders as due.

## Manim scenes: deferred, not deleted
`scenes_std.py` holds the ten designed Manim scenes (`Scene_B02_FluencyTrapDanger` …
`Scene_B11_FluencyTrapDanger`). They use `Text(narration[:30])` for bar/axis labels —
the exact §5b pattern that ships mid-word-truncated labels. Rendering them as-is
would fail Gate V. For this rebuild:

- Each affected beat's `shot.manim` key was **renamed** to `shot._manim_pending_5b_labelfix`.
- `fill_plan` now routes these beats as `author`-responsible slates; the compile writes
  `fluency-trap-danger-zone-slate.mp4` (no PIPELINE-owned unbuilts).
- The scene classes themselves are untouched — a later pass rewriting labels to short
  category nouns can rename the key back and recompile.
- The narration and act structure are still LOCKED. This deferral touches machinery, not
  script.

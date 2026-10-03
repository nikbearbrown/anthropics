# REBUILD-LOG — boondoggle-score-anatomy

Rebuild per `brutalist-art/skills/make/rebuild/SKILL.md`. Old sheet copied to
`beat_sheet.pre-rebuild.json` byte-exact before edit.

## LOCKED (carried over verbatim)
- All 7 body narration blocks (B00, B01, B02, B03, B04, B05, B06). No word
  changed.
- Beat order, act labels, slug, title, topic, register, channel.
- Kokoro-measured audio (`mp3/beat-B0*.mp3`) and `actual_duration_s` values
  from `mp3/timings.json`.

## REBUILT
1. **VOICE-LOCK envelope.** Beat-level `voice: am_onyx` + `voice_kokoro:
   am_onyx` + `engine: kokoro` added consistently on every beat. Metadata
   `voice: am_onyx` retained. No ElevenLabs `voice_id` / `voice_env` / `clock`
   prose in the prior sheet — nothing to drop there.
2. **shot.form.** Every beat now derives from its locked intent:
   - B00 → ClaudeComposerAsk (cold open, /boondoggle, world-language hello)
   - B01 → FormBCard (three who-values, one icon each)
   - B02 → FormBCard (Brooks 1986 two-up: accidental vs essential)
   - B03 → FormBCard (vague vs specific handoff condition)
   - B04 → ClaudeVerdictArtifact (authored from B04's own narration)
   - B05 → ClaudeComposerAsk (Your Turn — real column-walkthrough prompt)
   - B06 → ClaudeTitleOutro
3. **Cold open (B00).** Prior sheet's `shot.remotion.props.greeting` rendered
   as `"Liam"` alone (a lonely asterisk risk — SPARK-LINE LAW). Restored
   `"Sawadee, Liam"` (Thai hello — the metadata-declared greeting was never
   propagated to the actual render prop).
4. **Closing block (VERDICT → YOUR TURN → TITLE re-read).**
   - Prior sheet had duplicated tail: body B04/B05/B06 *plus* placeholder
     BVDT/BHTF/BOUT. BVDT held `"Key finding one/two/three"` template
     defaults; BHTF held the bracketed `"[Take what you learned from
     [The Boondoggle Score: Label Who Does Each Step] and apply it to your
     own work."` placeholder; BOUT was empty-narration ClaudeTitleOutro.
   - Body beats have the locked narration and measured audio; placeholders
     have neither. Collapsed by dropping BVDT/BHTF/BOUT and promoting the
     body beats to the standard patterns.
   - Verdict lines authored fresh from B04's own claims (no template
     defaults surviving):
     1. "The Score is not a capability judgment — it is a prompt for yours."
     2. "It forces the who-decides question before any code runs."
     3. "Two human-only rows, three Claude-only rows: honest build."
     4. "Zero human-only rows: probably not."
5. **Audio.** No fresh generation — the seven Kokoro mp3s already carry the
   locked narration at `am_onyx`. `actual_duration_s` copied through from
   `mp3/timings.json`.
6. **Renders.** No stale mp4 to purge. Nothing rendered yet — Remotion pass
   is the next step.
7. **Gates.** Type-check + Gate V run at compile time (see FILMLOOP-LOG).

## Datable-claims pass on narration
None found. The reel argues a framework (Score anatomy, Brooks 1986); no
model versions, no prices, no "as of" phrases. Brooks 1986 is a citation of
a fixed 1986 essay ("No Silver Bullet"), permanent.

## Fields dropped
- `metadata.build` (stale — 2026-07-28 build stamp with `filled: 3/7,
  slates: [B00,B04,B05,B06], skin_warnings: ["B00: palette=claude but the
  cold open is 'un-annotated' — COLD OPEN LAW wants ClaudeComposerAsk"]`).
  All conditions fixed; stale audit resolved.
- `metadata.design_version: v1` → `v2` (rebuild).
- Per-beat `build` blocks (stale from prior compile — will be re-stamped).
- Per-beat `manim.rendered` blocks pointing at 2026-07-25 renders that were
  never actually rendered to disk (no `media/` directory exists) — the
  routing is Remotion-only now.
- Per-beat `motion` fields on non-still beats (irrelevant to FormB / composer
  patterns).
- Duplicate `remotion` block at beat level (kept only under `shot.remotion`
  where the render pipeline reads it).
- `spark_line` fields on non-composer body beats (informational, not
  rendered; keeping them was noise once labels moved to FormBCard titles).
- BVDT / BHTF / BOUT beats — replaced by promoted B04/B05/B06 patterns.

## Mid-build fix — B04 verdict pagination

First compile revealed the 4-line verdict paginated (page 1 / page 2 indicator
on the card). The Remotion composition renders at its registered 34s duration
and the pipeline trims to `actual_duration_s = 18.6s` — so page 2 never got
frames in the trimmed clip. Fixed by compressing the 4 lines to 3 tighter
lines that fit at BASE_FS on one page:
- "Not a capability judgment — a prompt for yours."
- "Forces the who-decides question before code runs."
- "Zero human-only rows: probably not honest."
Re-rendered B04, recompiled. Gate V verified: single-page card, no `1/2`
indicator, all three lines visible through the beat.

## scenes_std.py
Left on disk untouched. Its three scenes used `Text(narration[:60])`
labels — the enterprise-search failure mode. No beat references them any
more (B01/B02/B03 route to Remotion FormBCard). Not deleted per the rule
"never delete a beat_sheet.json" and out of caution against orphaning a
future Manim retry.

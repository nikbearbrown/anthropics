# REBUILD-LOG.md — mas-short-verdict-short

Rebuilt: 2026-08-27  
Pre-rebuild backup: `beat_sheet.pre-rebuild.json` (byte-exact, made before any edit)

---

## What was LOCKED (carried verbatim)

- All `narration_text` per beat — no narration changes
- Beat order and act labels (B01 cold-open → B02-B05 body → B06 verdict → B07 your-turn → END)
- Shot intent: patterns, props, visual descriptions
- Metadata identity: title, slug, topic, source_post, register, channel

## What was REBUILT

1. **Stale renders deleted** — 13 mp4s in `clips/`, `manim/`, `media/` deleted (pre-sheet mtime)
2. **B01 greeting fixed** — `props.greeting` corrected from `"The ask,"` to `"Bonjour, Liam"` (spark line law; world-language hello + persona)
3. **Audio regenerated** — `generate_audio_kokoro.py am_onyx` run fresh; `actual_duration_s` re-measured (same values, narration unchanged)
4. **Remotion scenes rendered** — `remotion_scenes.py` ran B01, B06, B07 → `media/B01.mp4`, `media/B06.mp4`, `media/B07.mp4`
5. **B03/B04/B05 manim segments created** — 9:16 pillarbox crops from `pantry/clips/fig5-hidden-profile.mp4`: scale to 1216px wide, pad to 1216×2160 cream. Time offsets: B03=0-7.34s, B04=4.8-11.78s, B05=9.37s-end
6. **Review cut compiled** — `compile.py --review` → `mas-short-verdict-short-slate.mp4` (44.5s)
7. **TYPECHECK.md updated** — GATE T PASS 2026-08-27

---

## Datable-claim edits (narration changes)

**None.** No narration text was modified. All `narration_text` fields carried verbatim.

---

## Narration lock audit

Checked all `narration_text` fields for datable claims:
- "ninety-six to one hundred percent" — from Figure 5 of the Anthropic paper (still accurate per the paper, no version claim)
- "every model tested" — accurate hedge (says "tested", not "all models")
- "right now" — correct temporal hedge
- No model version names, no prices, no "as of" dates requiring correction

---

## Fields dropped

None. No ElevenLabs-era fields (`voice_id`, `voice_env`) were present in the original sheet.

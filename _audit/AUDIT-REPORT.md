# Beat-sheet compliance audit — books/anthropics vs recent Brutalist changes

*2026-08-19 · 3,505 beat sheets, 47,577 beats · mechanical pass (script + full results: `books/anthropics/_audit/`)*

## The verdict

**No — the corpus is not compliant.** 3,504 of 3,505 sheets fail at least one recent rule. But the failures split into three very different buckets: a small set of hard violations that would bite on any re-render or post, one enormous structural migration, and a large gray zone that is legacy-legal.

## By rule, worst first

**1. The shot.form migration hasn't happened (biggest gap).**
SHOT-FORM-SYSTEM.md (2026-08-10) says beats carry a `shot.form` purpose vocabulary with a fill contract. Only **121 of 47,577 beats** have it; **3,239 sheets have zero**. The entire corpus predates the doctrine. Whether that's a violation depends on your intent: if shot.form is prospective (new builds only), these are grandfathered; if the media-library validators will run over old sheets, this is a corpus-wide backfill job.

**2. GATE T / factcheck gates were never run.**
**3,226 sheets** have no `TYPECHECK.md` beside them; **2,076** no `FACTCHECK.md`. Under the current rules ("TYPECHECK.md with no FAIL is required, like FACTCHECK.md") none of these can pass a review cut or final without a gate run.

**3. Most sheets aren't finished reels anyway.**
**2,575 sheets** still carry slate/pipeline beats and **2,498** have unmeasured audio (no `actual_duration_s`). Under the PIPELINE-CARD RULE these can't ship as-is — a machine-buildable beat can never appear as a slate in a deliverable. This is mostly the un-built tail of the batch pipelines, not decay.

**4. ElevenLabs purge violations — real and specific.**
**599 sheets** still reference `elevenlabs`; **672** carry off-lock voices (mostly `nikbearbrown`, the retired ElevenLabs clone name) and **43** off-lock engines. VOICE-LOCK now allows only Kokoro (`am_onyx`/`af_bella`) and the `nbb` F5-TTS clone. Any re-render of these sheets fails or silently mis-voices. This is the cleanest batch-fix: engine→`nbb` (or kokoro), voice→`nbbhuman`/`am_onyx`.

**5. Closing / opening standards.**
**656 sheets** lack the full your-turn close (VERDICT → YOUR TURN → TITLE re-read); **1,069** don't open on `ClaudeComposerAsk`. Caveat: a chunk of the bad opens are `NikBearBrownOpen` or channel-specific skins — legitimate for non-Claude-brand channels, so treat this count as "needs eyeball," not "needs fix."

**6. Small, surgical items.**
~~27 sheets still reference the stripped spark glyph~~ — **CORRECTED on inspection: all 27 "glyph" hits are content glyphs** (chromosome glyphs, ghost glyphs in Manim visual descriptions), not the brand spark glyph. No violation, nothing to fix. **61 sheets** reference ratio-encoded `*169/*916` patterns — frozen legacy, allowed to exist, banned for new work. **1 sheet** fails to parse at all.

## The top failure signatures (verbatim from the CSV)

438× `no-shot.form + 5 slate beats + unmeasured audio + no TYPECHECK` and 322× the 4-slate variant — the batch-generated, never-built explainers. 109× `elevenlabs + no-shot.form + no close + no cold open` — the oldest generation. 100× `voice=nikbearbrown + NikBearBrownOpen + 8 slates` — the retired-clone channel batch.

## Recommended remediation order

1. **Voice-lock batch fix first** (599 + 672 sheets): mechanical rewrite of engine/voice fields; no creative judgment needed; unblocks any re-render.
2. **Glyph strip** (27 sheets): remove/replace glyph props; also mechanical.
3. **Decide the shot.form question** — prospective or retroactive. If retroactive, it's a scripted backfill (form is derivable from each beat's pattern name for ~90% of cases) + human pass on the remainder.
4. **Gates on demand, not wholesale**: run GATE T + factcheck only on sheets that are actually headed to a review cut or TOPOST — gating 3,200 dormant sheets is wasted work.
5. **Your-turn closes**: the `your-turn` skill exists precisely for this; run it over the 656 as a batch, excluding non-Claude channels.
6. Leave the 61 ratio-pattern sheets alone (frozen legacy) unless they re-render.

## Where everything lives

- `books/anthropics/_audit/audit_results.csv` — per-sheet issue codes (V/E/G/F/R/C/O/S/A/T), 3,505 rows
- `books/anthropics/_audit/audit_summary.json` — the aggregate counts
- `books/anthropics/_audit/audit_beat_sheets.py` — the audit script (re-runnable; shard mode in `audit_shard.py`)
- Shard scratch files `rows_*.csv` / `sum_*.json` can be deleted once the merged CSV is confirmed.

## Mechanical fixes APPLIED (2026-08-19, logged in `_audit/mechfix_log.json`)

Inspection before fixing corrected two audit assumptions: the "glyph" flags were false positives (content, not brand), and `engine` is an overloaded field — in many dialects it names the VISUAL engine (manim/remotion/vox), so only literal TTS values were touched. The 599 "elevenlabs" sheets turned out to be old vox slate cuts (all under `anthropics/youtube/`) whose metadata `clock`/`voice_id`/`audio_note` fields still describe the retired ElevenLabs master-clock doctrine — zero hits in narration text, so config-field rewrites were safe.

Applied, surgical regex with per-file JSON validation (979 sheets touched, 0 errors):
- **R1 (460×):** "ElevenLabs" reworded to "Kokoro (VOICE-LOCK)" inside `clock`/`notes`/`audio_note` doc fields.
- **R2 (2×):** `"engine": "elevenlabs"` → `"kokoro"`.
- **R3 (70×):** `"voice": "Liam"` → `"am_onyx"` (Liam IS am_onyx by definition).
- **R4 (433×):** `"voice": "NikBearBrown"` → `"nbbhuman"` (the retired ElevenLabs clone name → the nbb F5-TTS voice).

NOT auto-fixed, deliberately: **171 sheets** keep dead ElevenLabs-specific fields (`voice_id`/`voice_env`) — fabricating Kokoro values into EL-shaped fields would be dishonest; drop them at rebuild (each is in the log). The `MARCUS` voice (13 sheets) is an unknown persona — needs your call, not a regex.

## Honest limits

This was a mechanical pass: it checks fields, names, and file presence — it cannot judge whether a sparkLine is good, whether an ILLUSTRATE-LAW middle actually illustrates, or whether a NikBearBrownOpen is intentional. Those need the sampled-eyeball pass, ideally on whichever subset you actually intend to render next.

# CONVERT-LOG — claude-plugins-official--claude-liam-project-artifact → nbb

Converted `../claude-plugins-official--claude-liam-project-artifact/beat_sheet.json`
(Plain register, hai-simple) into `beat_sheet.nbb.json` (Teardown register,
NikBearBrown audience). No audio, no render — beat sheet only.

## Narration rewrites (voice only; facts unchanged)

- **B00 (hesitant writer cold open)** — Teardown "take it apart" frame added:
  "…it doesn't watch. It waits, until you ask." 34 words, within the
  BrutalistHesitantWriter 20–35-word / ≥9 s typing window the beat `note`
  guards. Corrections and visible text preserved.
- **NB01 (two-tabs mechanism)** — Reframed with the "Here's what's actually
  happening…" opener and the design-critic close: "They optimized for tabs that
  earn their place. Empty structure is the thing they refused to ship." Every
  tab name, count, and description carried through unchanged.
- **NB02 (config file + stored block)** — Opened with "Take it apart:", closed
  by naming the design choice ("The page carries its own memory forward"). All
  four config-section descriptions, the "gathered before any tab gets written"
  ordering, and the stored-block-inside-the-page detail preserved.
- **NB03 (nothing updates on its own)** — Reframed as "Here's the design
  choice under everything else…" and closed with the explicit trade-off ("lose
  the stored block and you lose the delta"). Refresh mechanics, rebuild-from-
  scratch case, and no-change-summary detail all unchanged.
- **BCRY (carry-out)** — Left verbatim. Judgment call: the source carry-out
  ("snapshot, not a sensor — it never watches your data on its own… it only
  knows what changed because it saved a record of what it looked like last
  time") is already a clean mechanism description in the Teardown register,
  uses no forbidden phrases, and doubles as the on-screen `WantQuote` string.
  Rewriting for its own sake would drift the audio away from the visible
  quote for no gain.
- **BOUT (outro)** — Narration "Snapshot, Not Sensor. Liam, in for Bear."
  preserved (already IN-FOR-BEAR-LAW compliant). OutroSeries `eyebrow` updated
  to `PROJECT ARTIFACT · @NikBearBrown`.

## LLM exercise beat (§Step 3)

**Judgment call:** kept `beat_id: "BHTF"` (was "your turn handoff") rather than
inserting a new `B_LLM`. BHTF was already the paste-into-Claude beat in the
second-to-last slot, so reshaping it in place preserves ordinal position,
beat_id, and shot pattern while satisfying the LLM-exercise contract.

Changes to BHTF:
- `act` updated to `"LLM EXERCISE"`.
- Narration rewritten in the Teardown register with the mandated
  paste-ready framing and a "Go deeper:" follow-up appended.
- Added the `llm_exercise` object:
  - `prompt` — a self-contained brief that produces useful output without the
    video: build a status page for an API-migration project (workstreams,
    open risk, decisions log), run two refresh cycles, and show the config,
    the stored block, and both refresh outputs so the viewer can see where
    the "memory of what changed" actually lives.
  - `dig_deeper` — delete the stored block by hand and refresh; ask what the
    page recovers, what it loses, and where its memory lives (data vs config
    vs the file itself). A real next question, not a summary.

## Ending order verified

Body (B00 → NB01 → NB02 → NB03 → BCRY) → LLM EXERCISE (BHTF) → OUTRO (BOUT).

## Palette + brand markers (audience swap follow-through)

Scaffolder set `palette: "teardown"` but left humanitarians-palette hex
values baked into the beat shot props. Migrated to keep the sheet visually
consistent with the declared palette:

- Metadata `ground` `#F3EBDD` → `#FFFFFF`; `style_preset` `humanitarians` →
  `teardown`; `folderLabel` and `channel_title` `@HumanitariansAI` →
  `@NikBearBrown`.
- B00 `BrutalistHesitantWriter` props: `bg #F3EBDD → #FFFFFF`, `ink #2F2A26
  → #2A1A0E`, `accent #E4572E → #C8102E`. `seed` updated to
  `nbb-project-artifact` so the type-error jitter regenerates cleanly rather
  than reproducing the HAI-seed layout.
- NB01/NB02/NB03 `graphic.production_viz.colors` migrated to the same
  teardown triple (`#FFFFFF`, `#2A1A0E`, `#C8102E`).
- BHTF `ClaudeComposerAsk.folderLabel` → `@NikBearBrown`.
- BOUT `OutroSeries.eyebrow` → `PROJECT ARTIFACT · @NikBearBrown`.

`playlist` (Extending Claude — Skills, Plugins & Connectors) left untouched;
it names the episode's series, not the channel, and no scaffold or SKILL
guidance said to rename it.

## Beat-level bookkeeping

Removed `actual_duration_s` and the `build` block from every beat: the
narration text changed, so the referenced `mp3/*.mp3` renders and the
`build.status`/`src` records are stale. Kept `estimated_duration_s`,
`audio_file` (relative — resolves inside this nbb dir when audio gets
generated), `voice`, `engine`, `lead_silence_s`/`tail_silence_s` where
present, and the `note` on B00 (still current — targeted the 20–35-word
typing window that the new B00 narration also lands in).

Removed `metadata._variant_todo` and the stale `metadata.build` block.

## Voice

`engine: "kokoro"`, `voice_kokoro: "am_onyx"` (Liam, in for Bear). Untouched
by this pass — the scaffolder had already set both. There is no paid engine;
ElevenLabs was permanently removed 2026-09-03.

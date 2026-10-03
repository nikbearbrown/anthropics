# REBUILD-LOG — one-sentence-problem-statement

Date: 2026-08-31
Contract: `brutalist-art/skills/make/rebuild/SKILL.md`

## Pre-rebuild backup
Byte-exact copy: `beat_sheet.pre-rebuild.json` (Aug 19 mtime preserved).

## Locked (verbatim)
- Body narration B01, B02, B03, B04 — original text carried word-for-word.
- Act labels (COLD OPEN, THE QUESTION, THE MECHANISM, THE PRACTICE).
- On-screen line intent for every body beat (used as FormACard `lines`).
- Title, slug, topic, source pointer, channel (claude-liam / @NikBearBrown).

## Rebuilt
- **Envelope:** dropped `clock` prose from metadata (ElevenLabs-era language
  about "durations below are word-count estimates until GATE 0 audio lock" —
  audio-lock is automatic now). Dropped `total_estimated_duration_seconds`
  (a lie once audio measures land; the pipeline recomputes). Kept
  `engine=kokoro / voice=am_onyx / voice_kokoro=am_onyx` per VOICE-LOCK.
- **Palette metadata:** was missing → set `palette=claude`, `channel=claude-liam`,
  `folderLabel=@NikBearBrown` (matches every body beat's actual skin).
- **Cold open (B00):** spark line was `"Liam"` (lone asterisk risk / boring
  hello) → `"Namaste, Liam"` (world-language rotation; adjacent claude-code
  reels use Ciao / Sawadee, so Namaste is unused nearby). Command was the
  full title, which overflowed the composer → compressed to
  `"Why does one sentence cost fourteen minutes?"` (four idea, still opens
  the video's thesis).
- **B01 shot:** was FormBCard with three placeholder items
  (`Key point one / two / three`, empty subs) → converted to `FormACard`
  driven by the beat's own `on_screen` lines. Preserves shot intent
  (a text-card COLD OPEN kicker), removes placeholder text.
- **B02, B03, B04 shots:** were `shot.manim` pointing at `scenes_std.py`
  scenes whose text was truncated mid-word at 60 chars (`"you're buil"`,
  `"…dressed as one - dif"`, `"…one user, one don"`). Broken output.
  Converted to `FormACard` driven by the beat's own `on_screen` lines
  (the SHOT LIST intent — the on-screen text that was recorded for each
  beat, verbatim). The Manim scenes are left untouched in
  `scenes_std.py` for provenance; no beat references them.
- **BVDT verdict:** was three placeholders (`Key finding one/two/three`)
  and empty narration. Authored from the body's own nouns/numbers
  (`two ands / two systems`, `one system-user-done-condition`,
  `14 minutes = the project, not overhead`).
- **BHTF Your Turn:** was the seeded template
  `"Take what you learned from [ ... ] and apply it to your own work"`
  (the 3,472-sheet placeholder caught 2026-08-30) → authored a real
  exercise from the video's own method: write your project's one sentence,
  circle every `and`, check the three questions.
- **Legacy duplicate bookends dropped:** the pre-rebuild sheet carried
  both the old-style `YOURTURN` beat and the new-style `BHTF` bookend
  (redundant Your-Turn), and both the old-style `OUTRO` and the new-style
  `BOUT`. Only the four canonical bookends (B00/BVDT/BHTF/BOUT) kept.

## Datable-claim edits over locked narration
None. The narration references no model names, versions, prices, or
"as of" phrasing. FACTCHECK.md verdict was already PASS on Jul 9 and none
of the underlying source facts have moved.

## Datable-claim edits to authored bookend text
BVDT and BHTF narration are new writing (bookend closes are the one place
new script is expected — rebuild §Rebuilt-4). Both use the video's own
material and contain no dated claims.

## TEMPLATE-MISSES
None. All chosen forms (FormACard, ClaudeComposerAsk, ClaudeVerdictArtifact,
ClaudeTitleOutro) have current templates.

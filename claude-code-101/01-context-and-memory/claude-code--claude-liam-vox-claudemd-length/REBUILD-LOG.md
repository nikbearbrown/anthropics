# REBUILD-LOG.md — vox-claudemd-length (2026-08-31)

Rebuild base: `beat_sheet.pre-rebuild.json` (byte-exact copy of the pre-audit sheet).

## LOCKED (carried over verbatim)
- All narration_text on the ten body beats (B01–B09 + YOURTURN) — unchanged.
- Beat order and act labels.
- Shot INTENT per beat: pattern/props/visual descriptions kept; props re-shaped only
  where the old ones were defects (see below).
- Metadata identity: slug, title, source pointer, register (Teardown), palette (claude).

## REBUILT

### Envelope
- Metadata: dropped `_variant_todo` (Kokoro rebuild, no ElevenLabs variant path). Left
  `voice`, `voice_kokoro`, `engine` intact (already Kokoro / am_onyx / VOICE-LOCK).
- Metadata `topic`: `CLAUDE CODE FOR TEACHERS` → `CLAUDE CODE`. The reel now lives
  under `anthropics/youtube/claude-code/` and the narration never says "for teachers";
  the on-screen topic string should describe the channel it plays on, not the source
  book that's no longer on disk.

### Narration edits (per rebuild-contract exception clauses)

Two beats had EMPTY narration in the old sheet — this is the one place new script is
expected per the rebuild contract's step 4 (closing block authored from sheet content):

- **BVDT** (verdict recap) — narration_text was `""` and the artifactLines were the
  template default `["Key finding one", "Key finding two", "Key finding three"]`.
  AUTHORED verdict from body content:
    - artifactLines[0]: `CLAUDE.md is advisory — compliance is probabilistic and degrades with length.`
    - artifactLines[1]: `Under 200 lines: rules hold. Past 300: key rules get ignored under pressure.`
    - artifactLines[2]: `Trim CLAUDE.md, move workflows to Skills, convert inviolable rules to Hooks.`
  - narration_text: authored 5-sentence spoken recap that says the three lines aloud.
  - Source: the reel's own body (B02/B04/B07 for the mechanism; B06 for the three moves).

- **BHTF** (your-turn) — narration_text was `""`, command was the template
  `"Take what you learned from [Why CLAUDE.md Breaks When It Gets Too Long] and apply it to your own work"`, output was `[]`.
  AUTHORED a real exercise using the four-question audit from B08:
    - greeting kept `"Your turn."`
    - segment: `"Audit your own CLAUDE.md"`
    - command: rewritten to walk the viewer through the four questions on their own file,
      with a specific paste-back ask ("paste every line you cut, one sentence per line explaining why it was noise").
    - output[]: 4 real next-step lines matching the four questions.
    - narration_text: 6-sentence spoken walk-through of the four-question audit.

No other narration was edited (datable-claims sweep found nothing — the reel names no
model versions, prices, or dated benchmarks).

### shot.form / props re-shaping

Props were re-shaped where the old ones were literal defects (§8.7/§8.9 truncation
patterns). No shot INTENT was changed.

- **B00 (ClaudeComposerAsk)** — `greeting: "Liam"` → `"Hola, Liam"` (spark-line law
  requires `<world-language hello>, Liam` on the cold open; Spanish not used by any
  adjacent claude-code reel this run). `command` rewritten to a real question
  ("Why does CLAUDE.md stop working past two hundred lines?") — old was the segment
  title with a question mark.

- **B01 (FormBCard)** — `title` was `"THIS IS LIAM, IN"` (truncated narration).
  Rewrote as `"THE RULE ON LINE 12"`. Items rewritten from truncated-narration labels
  (`"This is Liam, in for"`, `"The teacher's CLAUDE.md has a"`, `"no Tailwind."`)
  to short-noun labels: `Line 12`, `Third build`, `Rule ignored`, each with a real
  sub sentence from the narration.

- **B03 (FormBCard)** — `title` was `"HERE IS THE QUESTION"`. Rewrote as
  `"MORE RULES. LESS COMPLIANCE."`. Item labels rewritten to `Add rules` / `Past 200 lines` / `Why?`.

- **B05 (CARD)** — `card.copy` was the ENTIRE 6-sentence narration paragraph. Shortened
  to a real title card: `"220 lines → 95 lines. Rule respected again."`. Kept as SLATE
  in this review cut because a real drawing (document skin, before/after diagram) needs
  authoring; see AUDIT.md.

- **B06 / B07 / B08 (Manim)** — no shot-form change; scene source rewritten.

- **B07** — original shot mixed manim + `remotion.pattern=ClaudeTitleOutro` (a leftover
  from before the BOUT bookend existed). Cleaned to pure Manim (BOUT already handles
  the title outro).

- **B09 (FormBCard)** — `title` `"A MAINTAINED FIFTY-LINE CLAUDE.MD"` shortened to
  `"SHORT AND SPECIFIC WINS"`. Items rewritten to `50 maintained` / `Most specific` / `Or noise`.

### Scenes file — rewrite

- Old: `scenes_std.py` with 9 classes named `Scene_B0X_ClaudeLiamVox`, every chart
  labelled with `Text(narration_fragment[:30])`. This is the enterprise-search
  chart-text defect (colliding, mid-word-truncated labels).
- New: `scenes.py` (renamed to match `run.sh`'s expected filename) with 5 classes
  (`B02_ClaudeLiamVox`, `B04_...`, `B06_...`, `B07_...`, `B08_...`) — only the beats
  that are actually Manim in the new sheet. Labels are short category nouns; captions
  are complete sentences; bar heights agree with narration meaning; palette follows
  the reel's teal-good / crimson-bad semantic.
- `scenes_std.py` left in place for provenance — not read by `run.sh` (regex looks
  at `scenes.py`) but retained for the audit.

### Audio (fresh Kokoro generation)
- All 12 body/bookend narration beats generated fresh via `generate_audio_kokoro.py`.
- Voice: `am_onyx` (VOICE-LOCK).
- Measured `actual_duration_s` written back to the sheet by the generator.
- Total narration: 227.6 s (matches compiled master).

## Nothing was reverted or fudged
- No validators loosened.
- No factual claim was invented; the verdict was drawn from the reel's own body.
- No file was deleted (beat_sheet.pre-rebuild.json, scenes_std.py, and every
  beat_sheet.json.bak-* all retained).

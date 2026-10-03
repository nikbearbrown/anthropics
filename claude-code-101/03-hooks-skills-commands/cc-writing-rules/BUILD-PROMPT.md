# BUILD-PROMPT — cc-writing-rules

Recipe to rebuild this reel from scratch. Everything traces to `SESSION.md`
and `evidence/`; no imagined sessions.

## 1 — the two real headless runs

Both runs use the identical one-sentence ask in `evidence/ask.txt`. Command
flags and per-run working directories are in `PROMPTS.md`. Raw stream-json
lands in `evidence/run-{bare,skill}.jsonl`; both produced artifacts live
in `evidence/`.

The bare run reaches for the wrong nearby abstraction — a native Claude Code
`PreToolUse` hook in `.claude/settings.json` — because "hookify" is not a
word it knows without the SKILL. The skill run, with `.claude/skills/writing-rules/SKILL.md`
on disk, launches the plugin's `writing-rules` skill and writes a real
`.claude/hookify.<name>.local.md`.

## 2 — Liam's VERIFY (plain shell in `evidence/`)

The `evidence/check_rule.py` script parses the YAML frontmatter, checks
`name/enabled/event`, checks for `pattern` or `conditions`, and checks
the filename convention. It PASSes the skill artifact and FAILs the bare
artifact. `SESSION.md` records the transcript of every check.

## 3 — the sheet

Run `python3 author_sheet.py` from the reel folder. It writes `beat_sheet.json`
and prints a budget report. Any string over the kit's per-row budgets
(`CCSession` text ≤ 44, `CCHumanLedger` row ≤ 34, `CCBoondoggleScore` step
≤ 46) is called out and must be trimmed before continuing.

Do **not** re-run `author_sheet.py` after audio is generated — it wipes the
audio stamps.

## 4 — audio

```
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
  anthropics/claude-code-101/03-hooks-skills-commands/cc-writing-rules
```

Kokoro `am_onyx` on every beat, ~4:36 total. The measured mp3 durations
are the master clock.

## 5 — compile

```
./brutalist-art/art run   anthropics/claude-code-101/03-hooks-skills-commands/cc-writing-rules
./brutalist-art/art final anthropics/claude-code-101/03-hooks-skills-commands/cc-writing-rules
```

Read `_qc/REPORT.md` and `TYPECHECK.md` on any failure. Fix at the source
(shorter row, `mascot:"off"` on any full-height stack, 4 or 6 verdict lines
never 5), clear that beat's `shot.remotion.rendered` back to
`{"out":"","at":""}`, delete `media/<id>.mp4`, and run again.

## 6 — publication

**Not published from this file.** Master stays in the reel folder; TOPOST
via the `post` skill only, and only on explicit ask.

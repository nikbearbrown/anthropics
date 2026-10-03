# BUILD-PROMPT — cc-skill-development

The one-line invocation to (re)build this reel from `books/`:

```
./brutalist-art/art run   anthropics/claude-code-101/03-hooks-skills-commands/cc-skill-development
./brutalist-art/art final anthropics/claude-code-101/03-hooks-skills-commands/cc-skill-development
```

To reproduce the three real Claude sessions this reel reconstructs, from the reel folder:

```
cd scratch && for r in run-bare run-rules run-checker; do rm -rf "$r" && mkdir "$r" && cp README.md csv_shape.py sample.csv validate_skill.py "$r/"; done
```

Then run each `claude -p …` command in `PROMPTS.md` from its matching `run-*` directory. The stream-json goes to `evidence/run-*.jsonl`; the produced SKILL.md files can be diffed against `evidence/SKILL.*.md` in this folder.

To re-author the sheet without regenerating audio, edit `author_sheet.py` outside the reel folder or overwrite props by hand — running `author_sheet.py` inside the reel wipes the audio stamps and `beat-*.mp3` will need to be regenerated with:

```
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py <reel>
```

(Kokoro `am_onyx`, free/local — no key.)

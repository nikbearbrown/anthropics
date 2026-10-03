# BUILD-PROMPT — show-tell-claude-on-an-issue

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-claude-on-an-issue/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-claude-on-an-issue
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards.
# "Namaste" comes out clean (whisper-check BIDEA anyway). Kokoro says a sentence-initial "At Claude" as
# "I clawed": BOUT's narration spells "Att Claude"; BIDEA says "When you type, at Claude, on …".
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-claude-on-an-issue --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-claude-on-an-issue --height 2160 --out anthropics/youtube/show-tell-claude-on-an-issue/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final`.

Before re-stating any claim, re-fetch the docs raw from GitHub main (`anthropics/claude-code-action`: README, docs/capabilities-and-limitations.md, docs/usage.md, docs/setup.md, docs/faq.md, docs/security.md, examples/claude.yml) and diff them against `sources/live_2026-09-27_*`. If the trigger default, the branch prefix, the secret name or the "cannot" list moved, update FACTCHECK.md and the narration before re-voicing.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.

# BUILD-PROMPT — show-tell-what-is-claude-code

**What this is.** How to rebuild this film from scratch. **Why.** Bear's order (2026-09-27): "use the show-tell skill in Brutalist to make a film on this using the Liam persona 'What is Claude code?'" with a paste of the Claude Code product page (`SOURCE-PASTE.md`). **Result.** A gated 4K master in `exports/landscape/`; nothing staged or published. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-what-is-claude-code/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-what-is-claude-code
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (1.0 s of silence; keep the
# unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s.
# whisper-check BIDEA ("Ciao"), B03 ("the example the page itself uses"; "the page's own" was heard
# "page zone") and B10 ("And in Slack"; "and Slack" was heard "in Slack").
./brutalist.art/art run   anthropics/youtube/show-tell-what-is-claude-code --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-what-is-claude-code --height 2160 --out anthropics/youtube/show-tell-what-is-claude-code/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final`.

Before re-stating any claim, re-read the product page and re-fetch the docs raw (`curl https://code.claude.com/docs/en/overview.md` and `…/permission-modes.md`), and diff them against `sources/live_2026-09-27_*`. Auto mode's starting behaviour has already moved once (FACTCHECK row 46); if plans, surfaces or modes moved again, update FACTCHECK.md and the narration before re-voicing. Never add prices.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.

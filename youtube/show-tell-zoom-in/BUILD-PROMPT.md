# BUILD-PROMPT — show-tell-zoom-in

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-zoom-in/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-zoom-in
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (1.0 s silent tail; unpadded copy to _superseded/),
# then write ffprobe durations back to actual_duration_s (and audio_file). Whisper-check B04 ("the Widget A line, or the Widget E line").
./brutalist.art/art run   anthropics/youtube/show-tell-zoom-in --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-zoom-in --height 2160 --out anthropics/youtube/show-tell-zoom-in/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps); if you do, re-run `art final`.

Before re-stating any claim, re-fetch the live notebook (`https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/multimodal/crop_tool.ipynb`) and the two vision docs (`https://platform.claude.com/docs/en/build-with-claude/vision.md`, `.../vision-coordinates.md`) and diff them against `sources/live_*`. The live files win over the local copy in `anthropics/claude-cookbooks/`, which still holds the old normalized-coordinate `crop_image` version.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.

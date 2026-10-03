# BUILD-PROMPT — show-tell-one-tool-that-finds-the-rest

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-one-tool-that-finds-the-rest/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-one-tool-that-finds-the-rest
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (use --only <BID> for single re-voices).
# "Konnichiwa" is heard by whisper small.en as "Kaneshiwa", the same as the accepted earlier films; no re-voice.
# "get_weather among them" was heard as "get what are among them", so the prompt says "including get_weather";
# "the closest points win" was heard as "when", so B04 says "the closest points come back".
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-one-tool-that-finds-the-rest --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-one-tool-that-finds-the-rest --height 2160 --out anthropics/youtube/show-tell-one-tool-that-finds-the-rest/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first (a stale Manim cache pushes re-renders past their audio). Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final` so the stamp says master.

Before re-stating any version-sensitive fact, re-fetch the raw live page (`curl -sL https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool.md`): the live docs win over `anthropics/claude-cookbooks/tool_use/tool_search_with_embeddings.ipynb`, whose request code never sets `defer_loading` and whose beta header and model are not on the live page. Name no version and no model.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.

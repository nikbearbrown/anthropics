# BUILD-PROMPT — show-tell-five-ways-to-wire-an-agent

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-five-ways-to-wire-an-agent/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-five-ways-to-wire-an-agent
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-five-ways-to-wire-an-agent --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-five-ways-to-wire-an-agent --height 2160 --out anthropics/youtube/show-tell-five-ways-to-wire-an-agent/exports/landscape
```

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.

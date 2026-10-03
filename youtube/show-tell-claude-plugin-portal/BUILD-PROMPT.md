# BUILD-PROMPT — show-tell-claude-plugin-portal

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-claude-plugin-portal/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-claude-plugin-portal
# pad BOUT with 1.0 s of silence, then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-claude-plugin-portal --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-claude-plugin-portal --height 2160 --out anthropics/youtube/show-tell-claude-plugin-portal/exports/landscape
```

Then STOP. Staging (`art post`) and publishing happen only on Bear's word.

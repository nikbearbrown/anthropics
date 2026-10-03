# BUILD-PROMPT — show-tell-claude-on-your-desk

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-claude-on-your-desk/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-claude-on-your-desk
# Kokoro reads "Hej" as "hedge": re-voice BIDEA from phonemes with the greeting said right (same engine, voice, encoder)
python3 anthropics/youtube/show-tell-claude-on-your-desk/tts_greeting_fix.py
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-claude-on-your-desk --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-claude-on-your-desk --height 2160 --out anthropics/youtube/show-tell-claude-on-your-desk/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first (a stale Manim cache pushes re-renders past their audio). Re-running `generate_audio_kokoro.py` without `--only` re-voices BIDEA as "hedge"; run `tts_greeting_fix.py` again after it.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.

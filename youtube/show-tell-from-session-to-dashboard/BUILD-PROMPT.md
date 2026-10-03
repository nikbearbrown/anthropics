# BUILD-PROMPT — show-tell-from-session-to-dashboard

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-from-session-to-dashboard/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-from-session-to-dashboard
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (1.0 s silent tail; unpadded copy to _superseded/),
# then write ffprobe durations back to actual_duration_s.
# Kokoro: "otel" is heard as "Odell"/"hotel", so the narration spells "O-T-E-L"; "Sum it" became "Summit", so B11 says "Add it up".
./brutalist.art/art run   anthropics/youtube/show-tell-from-session-to-dashboard --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-from-session-to-dashboard --height 2160 --out anthropics/youtube/show-tell-from-session-to-dashboard/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps); if you do, re-run `art final`.

Before re-stating any claim, re-fetch `https://code.claude.com/docs/en/monitoring-usage.md` raw and diff it against `sources/live_monitoring-usage-2026-09-27.md`; the live docs win over the guide. Use no prices or ROI figures.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.

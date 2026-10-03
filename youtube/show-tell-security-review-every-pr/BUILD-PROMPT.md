# BUILD-PROMPT — show-tell-security-review-every-pr

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-security-review-every-pr/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-security-review-every-pr
# Kokoro says "Guten Tag" the English way (GYOO-tn tag): re-voice BIDEA from phonemes as GOO-ten TAHK (same engine, voice, encoder)
python3 anthropics/youtube/show-tell-security-review-every-pr/tts_greeting_fix.py
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-security-review-every-pr --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-security-review-every-pr --height 2160 --out anthropics/youtube/show-tell-security-review-every-pr/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first (a stale Manim cache pushes re-renders past their audio). Re-running `generate_audio_kokoro.py` without `--only` re-voices BIDEA the English way; run `tts_greeting_fix.py` again after it. Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final` so the stamp says master.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.

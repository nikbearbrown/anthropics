# BUILD-PROMPT — show-tell-choosing-the-right-claude-model

**What this is.** How to rebuild this film from scratch. **Why.** Bear's order (2026-09-27): six screenshots for "a choosing the right model for Claude video. These are just inspiration. Use the Showtell skill." (`SOURCE-SCREENSHOTS.md`, `source/`). **Result.** A gated 4K master in `exports/landscape/`; nothing staged or published. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-choosing-the-right-claude-model/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-choosing-the-right-claude-model
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (1.0 s of silence; keep the
# unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s.
# whisper-check BIDEA ("Bonjour"), B01 ("four models by the kind of work they're for"; "four Claude
# models" fused into "foreclawed models") and B04 ("Suppose you want"; "Say you want" was heard "So you
# want"), and every "Haiku", "Sonnet", "Opus", "Fable" (all clean).
./brutalist.art/art run   anthropics/youtube/show-tell-choosing-the-right-claude-model --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-choosing-the-right-claude-model --height 2160 --out anthropics/youtube/show-tell-choosing-the-right-claude-model/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final`.

Before re-stating any claim, re-read the six screenshots and re-fetch the developer docs raw (`curl -sL https://docs.claude.com/en/docs/about-claude/models/choosing-a-model.md`), and diff against `sources/live_2026-09-27_docs_choosing_a_model.md`. If the guide changes its taglines or "Best for" lists, or the docs drop the efficiency-first / capability-first advice, update FACTCHECK.md and the narration before re-voicing. Never add prices, benchmarks, speeds or version numbers.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.

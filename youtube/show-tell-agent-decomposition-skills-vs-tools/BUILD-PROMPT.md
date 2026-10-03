# Rebuild

From `/Users/bear/Documents/CoWork/bear-textbooks/books`:

```bash
python3 anthropics/youtube/show-tell-agent-decomposition-skills-vs-tools/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-agent-decomposition-skills-vs-tools
python3 anthropics/youtube/show-tell-agent-decomposition-skills-vs-tools/finish_audio.py
python3 brutalist.art/runtime/scripts/align.py anthropics/youtube/show-tell-agent-decomposition-skills-vs-tools
./brutalist.art/art run anthropics/youtube/show-tell-agent-decomposition-skills-vs-tools --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-agent-decomposition-skills-vs-tools --height 2160 --out anthropics/youtube/show-tell-agent-decomposition-skills-vs-tools/exports/landscape
```

The audio-finishing script sets measured bookend timing and silence pads. On a full revoice, preserve and then replace the old `*-unpad.mp3` backups before running it so it uses the newly generated voice. Validate static scenes, inspect rendered frames at ordinary viewing size, and record actual findings in `_qc/REPORT.md`. Do not reuse old cached clips after scene edits: preserve them under `_superseded/` first. Do not publish, upload, or stage. Preserve the original film.

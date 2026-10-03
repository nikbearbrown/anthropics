# CLAUDE-CODE-RENDER.md — Memory, Skills, and Guardrails (Film 10)

Render instructions for Bear's Mac. Persona: Liam, in for Bear.
Narration: Kokoro TTS, voice `am_onyx`. Register: Teardown.

## 0. Get the files
Pull the repo and move into the film folder:

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/nikbearbrown-anthropics/muse/film-10-memory-skills-guardrails
```

(Adjust the local path to wherever you pulled nikbearbrown/anthropics.)

## 1. Narration (Kokoro, am_onyx)
For each of the 15 beats in `beat_sheet.json`, synthesize the beat's `line`
field exactly as written → one MP3 per beat:

```
audio/BIDEA.mp3  audio/BDEFS.mp3
audio/B01.mp3  audio/B02.mp3  audio/B03.mp3
audio/B04.mp3  audio/B05.mp3  audio/B06.mp3
audio/B07.mp3  audio/B08.mp3  audio/B09.mp3  audio/B10.mp3
audio/BVDT.mp3  audio/BHTF.mp3  audio/BOUT.mp3
```

Notes: numbers are already written as spoken words ("memory dot md") — do
not convert them back to digits. Liam persona, Teardown register, read
straight. Verify 15 files, all non-empty.

## 2. Review cut
From the brutalist.art toolkit directory:

```
./art run --reel muse-film-10-memory-skills-guardrails --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py --audio <film-dir>/audio/
```

Spot-check: the memory.md → session-dots arrows in M03; the plug sliding
into the socket in M11; the M13 recap → your-turn → outro phases transition
cleanly.

## 3. Final 4K master

```
./art final --reel muse-film-10-memory-skills-guardrails
```

Verify: 3840×2160, runtime ≈ 288 s (4m48s, the sum of the audio), silent tail
present.

## 4. Publish
Only on Bear's explicit instruction. Never otherwise.

## Film facts
- Beats: 15 (10 body) · Runtime: 288 s (4m48s) · Scenes: 13
- QC: 13 clean · 0 warnings · 0 errors (static gate, verified)
- No MP3/MP4 files are committed to the repo. Narration and renders live on
  this Mac only.

# CLAUDE-CODE-RENDER.md — Grounded Answers (Film 5)

Render instructions for Bear's Mac. Persona: Liam, in for Bear.
Narration: Kokoro TTS, voice `am_onyx`. Register: Teardown.

## 0. Get the files
Pull the repo and move into the film folder:

```
cd /Users/bear/Documents/CoWork/bear-textbooks/books/nikbearbrown-anthropics/muse/film-05-grounded-answers
```

(Adjust the local path to wherever you pulled nikbearbrown/anthropics.)

## 1. Narration (Kokoro, am_onyx)
For each of the 13 beats in `beat_sheet.json`, synthesize the beat's `line`
field exactly as written → one MP3 per beat:

```
audio/BIDEA.mp3  audio/BDEFS.mp3
audio/B01.mp3  audio/B02.mp3  audio/B03.mp3
audio/B04.mp3  audio/B05.mp3  audio/B06.mp3
audio/B07.mp3  audio/B08.mp3
audio/BVDT.mp3  audio/BHTF.mp3  audio/BOUT.mp3
```

Notes: numbers are already written as spoken words — do not convert them back
to digits. Liam persona, Teardown register, read straight. Verify 13 files,
all non-empty.

## 2. Review cut
From the brutalist.art toolkit directory:

```
./art run --reel muse-film-05-grounded-answers --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py --audio <film-dir>/audio/
```

Spot-check: the side-by-side comparison lands in pairs in M06; the blocked
pages stamp cleanly in M08; the M11 recap → your-turn → outro phases
transition cleanly.

## 3. Final 4K master

```
./art final --reel muse-film-05-grounded-answers
```

Verify: 3840×2160, runtime ≈ 282 s (4m42s, the sum of the audio), silent tail
present.

## 4. Publish
Only on Bear's explicit instruction. Never otherwise.

## Film facts
- Beats: 13 (8 body) · Runtime: 282 s (4m42s) · Scenes: 11
- QC: 11 clean · 0 warnings · 0 errors (static gate, verified)
- No MP3/MP4 files are committed to the repo. Narration and renders live on
  this Mac only.

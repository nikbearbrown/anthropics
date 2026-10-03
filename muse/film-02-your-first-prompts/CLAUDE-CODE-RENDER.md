# CLAUDE-CODE-RENDER.md — Your First Prompts (Film 2)

Render instructions for Bear's Mac. Persona: Liam, in for Bear.
Narration: Kokoro TTS, voice `am_onyx`. Register: Teardown.

## 0. Get the files
Pull the repo and move into the film folder:

```
cd <path-to>/nikbearbrown-anthropics/muse/film-02-your-first-prompts
```

## 1. Narration (Kokoro, am_onyx)
For each of the 15 beats in `beat_sheet.json`, synthesize the beat's `line`
field exactly as written → one MP3 per beat:

```
audio/BIDEA.mp3  audio/BDEFS.mp3
audio/B01.mp3  audio/B02.mp3  audio/B03.mp3  audio/B04.mp3  audio/B05.mp3
audio/B06.mp3  audio/B07.mp3  audio/B08.mp3  audio/B09.mp3  audio/B10.mp3
audio/BVDT.mp3  audio/BHTF.mp3  audio/BOUT.mp3
```

Notes: numbers are already written as spoken words — do not convert them back
to digits. "J L P T N five" is spelled out — read the letters, then "five".
Liam persona, Teardown register, read straight. Verify 15 files, all non-empty.

## 2. Review cut
From the brutalist.art toolkit directory:

```
./art run --reel muse-film-02-your-first-prompts --beats <film-dir>/beat_sheet.json --scenes <film-dir>/scenes.py --audio <film-dir>/audio/
```

Spot-check: the 40 grammar-list rows appear in two waves (M06); the effort
dial needle sweeps low → extra high (M07); the meter bars triple on the
"extra high" chip (M10); the M13 recap → your-turn → outro phases transition
cleanly.

## 3. Final 4K master

```
./art final --reel muse-film-02-your-first-prompts
```

Verify: 3840×2160, runtime ≈ 280 s (4m40s, the sum of the audio), silent tail
present.

## 4. Publish
Only on Bear's explicit instruction. Never otherwise.

## Film facts
- Beats: 15 (10 body) · Runtime: 280 s (4m40s) · Scenes: 13
- QC: 13 clean · 0 warnings · 0 errors (static gate, verified)
- No MP3/MP4 files are committed to the repo. Narration and renders live on
  this Mac only.

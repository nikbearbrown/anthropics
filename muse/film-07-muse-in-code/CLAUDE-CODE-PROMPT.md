# CLAUDE-CODE-PROMPT.md — paste-ready prompt for Claude Code (Bear's Mac)

Copy everything below the line into Claude Code, running inside this film folder:
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/muse/film-07-muse-in-code/`

---

You are finishing a lecture film for the @NikBearBrown YouTube channel.
Persona: Liam, in for Bear. Everything except narration audio and rendered
video is already done and in this folder. Your job: render the audio and the
video. Do not publish anything.

## The film
- Title: Muse in Code
- Reel slug: muse-film-07-muse-in-code
- Beats: 13 (see beat_sheet.json), total runtime 282s
- You are in the film folder: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/muse/film-07-muse-in-code

## Files you have
- `beat_sheet.json` — the script. Each beat: id, scene, dur_s, act, voice,
  line (the exact narration), screen (what the viewer sees).
- `scenes.py` — the Manim visuals (classes M01…M11).
- `ACTS.md` / `SHOTLIST.md` / `FACTCHECK.md` / `SOURCES.md` — context. Read
  `SHOTLIST.md` if any visual confuses you.
- `CLAUDE-CODE-RENDER.md` — the detailed render instructions. Follow them.

## Step 1 — narration audio (Kokoro, voice am_onyx)
For EVERY beat in `beat_sheet.json`, synthesize the beat's `line` field
EXACTLY as written using Kokoro TTS voice `am_onyx`, and save to
`audio/<BEAT_ID>.mp3` (e.g. `audio/BIDEA.mp3`, `audio/B01.mp3`, …
`audio/BOUT.mp3`).
- Numbers in the lines are already written as spoken words — do not "fix"
  them back to digits.
- Liam persona, Teardown register: read it straight, no added intro/outro.
- Create `audio/` if it doesn't exist.
- When done, verify: one MP3 per beat id, 13 files total, each
  non-empty and playable.

## Step 2 — review cut
From the brutalist.art toolkit directory on this Mac:

```
./art run --reel muse-film-07-muse-in-code --beats /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/muse/film-07-muse-in-code/beat_sheet.json --scenes /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/muse/film-07-muse-in-code/scenes.py --audio /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/muse/film-07-muse-in-code/audio/
```

Watch the review cut (or spot-check act by act). If a scene visibly breaks,
stop and report which scene and what you see — do not redesign the film.

## Step 3 — final 4K master

```
./art final --reel muse-film-07-muse-in-code
```

Verify the master: 3840×2160, runtime ≈ 282s (the sum of the audio),
silent tail present at the end.

## Hard rules
- NEVER commit or push any MP3, MP4, or WAV. Audio and renders stay on this Mac.
- NEVER publish, upload, or stage anything for publishing.
- When finished, report: beat count, audio files created, review-cut result,
  master resolution, runtime, and file location.

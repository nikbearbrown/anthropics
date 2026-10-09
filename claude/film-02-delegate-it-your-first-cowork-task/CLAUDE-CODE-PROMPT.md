# CLAUDE-CODE-PROMPT.md — paste-ready prompt for Claude Code (Bear's Mac)

Copy everything below the line into Claude Code, running inside this film folder:
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude/film-02-delegate-it-your-first-cowork-task/`

---

You are finishing a lecture film for the @NikBearBrown YouTube channel.
Persona: Liam, in for Bear. Everything except narration audio and rendered
video is already done and in this folder. Your job: render the audio and the
video. Do not publish anything.

## The film
- Title: Delegate It: Your First Cowork Task
- Reel slug: claude-film-02-delegate-it-your-first-cowork-task
- Beats: 15 (see beat_sheet.json), total runtime 282s (4m42s)
- You are in the film folder: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude/film-02-delegate-it-your-first-cowork-task

## Files you have
- `beat_sheet.json` — the script. Each beat: id, scene, dur_s, act, voice,
  line (the exact narration), screen (what the viewer sees).
- `scenes.py` — the Manim visuals (13 classes, M01–M13).
- `ACTS.md` / `SHOTLIST.md` / `FACTCHECK.md` / `SOURCES.md` — context. Read
  `SHOTLIST.md` if any visual confuses you.
- `CLAUDE-CODE-RENDER.md` — the detailed render instructions. Follow them.

## Step 1 — narration audio (Kokoro, voice am_onyx)
For EVERY beat in `beat_sheet.json`, synthesize the beat's `line` field
EXACTLY as written using Kokoro TTS voice `am_onyx`, and save to
`audio/<BEAT_ID>.mp3` (e.g. `audio/BIDEA.mp3`, `audio/B01.mp3`, …
`audio/BOUT.mp3`) — 15 files total.
- Numbers in the lines are already written as spoken words — do not "fix"
  them back to digits.
- Liam persona, Teardown register: read it straight, no added intro/outro.
- Create `audio/` if it doesn't exist.
- When done, verify: one MP3 per beat id, 15 files total, each non-empty
  and playable.

## Step 2 — review cut
From the brutalist.art toolkit directory on this Mac:

```
./art run --reel claude-film-02-delegate-it-your-first-cowork-task --beats /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude/film-02-delegate-it-your-first-cowork-task/beat_sheet.json --scenes /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude/film-02-delegate-it-your-first-cowork-task/scenes.py --audio /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude/film-02-delegate-it-your-first-cowork-task/audio/
```

Watch the review cut (or spot-check act by act). If a scene visibly breaks,
stop and report which scene and what you see — do not redesign the film.

## Step 3 — final 4K master
Render the 4K master from the same files (see CLAUDE-CODE-RENDER.md).
Verify: 3840×2160, runtime ≈ the sum of the audio, silent tail present.

## Step 4 — publish
Only on Bear's explicit instruction. Never otherwise.

## Film facts (for verification)
- Beats: 15 (10 body) · Planned runtime: 282s (4m42s) · Scenes: 13
- QC: static gate clean, paper background verified on rendered frames
- No MP3/MP4 files are committed to the repo. Narration and renders live on
  this Mac (and the review cut on Bear's shared Drive) only.

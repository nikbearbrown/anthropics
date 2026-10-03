# AUDIT.md — claude-liam-simple-delve

Auditor: filmloop-supervised invocation 2026-08-31.
Reel state on entry: master `claude-liam-simple-delve.mp4` mtime 2026-08-28 02:12,
`beat_sheet.json` mtime 2026-08-28 02:11 — master IS newer than sheet, so the
reel enters as a completed compile from a prior pass. Sheet is not touched by
this invocation (any post-compile sheet edit would disqualify the cut as STALE).

## PHASE 0 — REBUILD CONTRACT

Not entered. No `beat_sheet.pre-rebuild.json` was created because no sheet edit
is needed. The sheet is already in Phase-2 shape: VOICE-LOCK envelope
(`engine: kokoro`, `voice_kokoro: am_onyx` for all Liam beats; `MARCUS`/`seedance`
retained only for the Shannon-puppet cold open B00, which speaks its own audio
baked into the Seedance clip). No dead ElevenLabs fields. Every beat has
`shot.type` and a build record.

## PHASE 1 — AUDIT CHECKS

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | Stale renders | FIXED | Deleted `mp4/claude-liam-simple-delve.mp4` (Aug 15 11:17 — older than sheet). Top-level master (Aug 28 02:12) is newer than sheet (Aug 28 02:11) — DONE-check safe. |
| 2 | Bookends | PASS-with-note | `B00` = AI-VIDEO Shannon-puppet Seedance clip (not `ClaudeComposerAsk`); this is the intentional cold-open pattern for this reel and is already recorded as a `skin_warnings` entry in the sheet. `BHTF` = `ClaudeComposerAsk` ✓. `BOUT` = `ClaudeTitleOutro` ✓. `BVDT` absent — legitimate under the amendment (previous pass stripped a placeholder); `BCRY` `WantQuote` carries the carry-out sentence. |
| 3 | Spark lines | PASS | `BHTF.props.greeting = "Your turn."` ✓. No inner `ClaudeComposerAsk` bodies. `B00` has no `greeting` field because it is not a composer beat (see #2). |
| 4 | Verdict | PASS (absent, legal) | `verdict_audit.py` reports "no verdict beat" for this slug — that is the strip outcome under the amendment. Carry-out delivered by `BCRY` (WantQuote): *"A word that shows up again and again is a habit, not a watermark. The watermark never picks the same favourite twice."* Real content from the body's nouns, not a template default. |
| 5 | Card text (FormA/FormB) | N/A | No FormA/FormB items. All body beats are Manim GRAPHIC (S01-S16). Bookends BCRY/BHTF/BOUT are Remotion patterns with real props (see #5c for BHTF command wording). |
| 5b | Chart text | PASS | Body is 16 Manim scenes with hand-tuned `label`/`mechanic` copy (SxxScene). Labels are short category nouns; no narration-fragment truncation. Terracotta used sparingly (S12 FLAG marker is the reel's declared single hedge, and the S15/S16 mirrored strike-throughs are the payoff — one moment per beat). |
| 5c | Your-Turn placeholder | PASS | `BHTF.command` is a real 10-minute exercise authored from the reel's own content: *"Take three pieces of writing I'm sure a human wrote — old emails, a paper from before 2022, something from my own archive. Count the supposed AI tells in them. Then take something I know was AI-written and count again."* No square brackets, no title restated. |
| 6 | Punt sweep | PASS | Zero unfilled slates, zero `DoodleScene`/`DoodleChart` (grep confirmed), zero `STILL src=archive`, zero unmet FormA visual. `B00` is a gen-AI ask but is RENDERED (`media/B00.mp4`, 11.072s, Seedance clip present); it is a filled asset, not a punt. Every beat has `build.status ∈ {VIDEO, MANIM}` and a real `src`. |
| 7 | Card-only reel | PASS | 16 body beats draw real Manim scenes; not a card-in-a-costume reel. |
| 8 | Lens audit (LENS-NOTES.md) | PASS | Two-plus lens moves earned by the body: **Popper (falsification stated in advance)** at S05–S06 — "a watermark that always favoured the same words could be stripped with a find-and-replace… its whole security depends on not doing that." **Descartes (what would tell them apart)** at S14 — "telling them apart takes running the same model twice, with the mark and without, and comparing." **Plato (name artifact / world / relationship)** at S13 — same word, two different causes, indistinguishable from outside. Three moves, clean. |
| 9 | Brand fields | PASS | `folderLabel: "@NikBearBrown"` (channel handle, not brand key). `engine: kokoro` / `voice_kokoro: am_onyx` matches the audio generated for S01–S16, BCRY, BHTF, BOUT. `B00` carries its own `engine: seedance` / `voice: MARCUS` override because the audio is baked into the Seedance render. Persona coherence holds: MARCUS opens and hands off to Liam ("Liam. Take them through it."), Liam narrates the body and signs "Liam, in for Bear." |
| 10 | Pacing | LOG | Most body beats sit in 2.5–3.3 wps. Three beats run hot at ~3.6–4.1 wps against measured audio (S12 ~3.6, S13 ~4.1, BHTF ~4.0). No silent retime performed. Kokoro `am_onyx` reads it cleanly at those rates; flagged for reviewer awareness only. |
| 11 | `type_check.py` | PASS | Re-run this invocation: **GATE T: PASS** (20 beats checked, 0 FAILs; TYPECHECK.md unchanged from 2026-08-28). |

## Additional gates verified

- **SHARPNESS**: median LV 441.1, floor 220.6, all 20 beats PASS (SHARPNESS.md unchanged).
- **Audio presence**: master `mean_volume: -27.4 dB` (well above the −40 dB failure floor), duration 148.16 s, aac stereo 48 kHz. Per-beat mp4s in `clips/` are video-only by design — audio is composed in `clips/master.m4a` and muxed at the master.
- **PLACEHOLDER.md**: "No unfilled STILL/archive placeholders."

## Deletions this invocation

- `mp4/claude-liam-simple-delve.mp4` (2026-08-15 11:17 — 13 days older than the current sheet; a lie with a timestamp on it). Top-level `claude-liam-simple-delve.mp4` retained as the true master.

## Reel status

**DONE.** Master is fresher than the sheet, GATE T passes, SHARPNESS passes,
audio present at −27.4 dB, no unfilled punts, verdict-strip outcome is legitimate,
Your-Turn is real, three lens moves are on the page. Nothing needs a recompile.
No sheet edits performed (would have inverted the DONE check).

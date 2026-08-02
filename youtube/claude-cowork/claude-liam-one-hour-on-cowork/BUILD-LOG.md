# BUILD-LOG.md — claude-liam-one-hour-on-cowork

## 2026-07-21 (build session)

### Setup
- Reel folder created: `claude-cowork/youtube/claude-liam-one-hour-on-cowork/`
- Source infographic: `pantry/one-hour-cowork-infographic.png` (Ruben Hassid / How to AI)
- FACTCHECK.md: PASS — 2 datable claims genericized ("11 official plugins" → library; model name → "most capable model")
- SOURCES.md: Hassid's infographic credited; all content attributed as his recommended workflow

### Plan (Phase 1 — approved by Bear)
- 17 beats: B00 (cold open) + B01 (full wheel intro) + 6×(clock + body) + B14 (verdict) + B15 (your turn) + B16 (outro)
- ClockWheel component (new) — 6-wedge clock, infographic order, sweep animation
- CoworkMarkdownFile (new) — two animated .md file cards for Act 2
- CoworkFolderTree (new) — animated folder tree for Act 4
- ClaudeComposerAsk, ClaudeWindow, ClaudeTitleOutro (existing) for bookends + UI beats

### Components built
- `ClockWheel.tsx` — new; registered in Root.tsx as `ClockWheel`
- `CoworkMarkdownFile.tsx` — new; registered as `CoworkMarkdownFile`
- `CoworkFolderTree.tsx` — new; registered as `CoworkFolderTree`
- Root.tsx: imports + 3 Composition registrations added after `CoworkHourClock`
- TypeScript check: PASS (zero errors)

### Gate record
- GATE F (factcheck): PASS — 2026-07-21
- GATE P (narration): SIGNED — Bear, 2026-07-21 ("do them all")

### Audio + render + compile
- Kokoro am_onyx audio: 16 narrated beats generated; B16 silence MP3 hand-generated (null audio_file bug)
- Remotion renders: all 17 beats rendered; B03 + B13 re-rendered post-QC fix
- Compile: `claude-liam-one-hour-on-cowork.mp4` — 185.1s, 17/17 filled, audio per-beat narration

### Visual QC — 2026-07-21
- 104 frames extracted (0.5fps grid + 11 named beat frames)
- SKIN LINT B03 ("greeting": "") → fixed: "Ask before it acts."
- SKIN LINT B13 ("greeting": "") → fixed: "Type / to call a plugin."
- QC VERDICT: PASS — see `_qc/REPORT.md`

## 2026-07-21 (revision — attribution removal + factcheck)

### Changes
- Removed all references to Ruben Hassid from narration, Remotion props, and docs
- B00 output lines: "Yes — Ruben Hassid mapped it." → "Six wedges. Sixty minutes."
- B16 subline: "Ruben Hassid's plan, rebuilt." → "Six wedges. You're set up."
- B01 narration: removed "Hassid's recommended order"
- B09 narration: removed "Hassid's rule"
- B14 narration: removed "Hassid's plan"

### Factual fixes (FACTCHECK.md updated)
- B03: "clickable AskUserQuestion fields" → "Claude asks clarifying questions"
- B09: "Real read and write access" → qualified with "with write permission"
- B11: "Settings → Cowork → Edit Global Instructions" → "In Settings, find Global Instructions"
- B13: "Sales, Marketing, Legal, Finance" categories → "business connectors"

### Output
- Kokoro audio regenerated for 8 beats (B00, B01, B03, B07, B09, B11, B13, B14)
- Remotion re-rendered: B00, B03, B13, B16
- Compiled: `claude-liam-one-hour-on-cowork.mp4` — 176.7s, 17/17 filled
- SOURCES.md, FACTCHECK.md, PEDAGOGY.md updated

## Open items
- Bear review of `claude-liam-one-hour-on-cowork.mp4` (176.7s)
- Publish: Bear's decision (never publish without explicit authorization)

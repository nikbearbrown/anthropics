# SAVE-STATE — anthropics/youtube design-system conversion
_Written: 2026-07-27 (confirmed by user)_

## Primary Request and Intent

The user asked to convert every claude-liam / @NikBearBrown reel under `books/anthropics/youtube/` to a new design system by:
- Reading four locked design docs: DESIGN-PRINCIPLES.md, AUDIT-MODE.md, VOICE-LOCK.md, OUTRO-LOCK.md (all in `brutalist-art/`)
- Discovering and classifying 768 reels across 13 topic folders (behind-the-model, claude-agent-skills, claude-basics, claude-code, claude-cowork, claude-for-education, claude-mcp-connectors, claude-news, claude-plugins, claude-prompting, claude-research, claude-skills, claude-youtube)
- IN-SCOPE = claude-liam / @NikBearBrown (am_onyx); SKIP = hai/medhavy/musinique/nbb
- PILOT first (8 reels spanning topics/types), then topic-by-topic without rendering or spending money (GATE P = silent slate only)
- Enforcing: no gen-AI clips, Form A/B cards only, ~70-80% light polarity, exact OUTRO-LOCK compliance, am_onyx voice only
- User confirmed pilot, then said "go" → ran claude-youtube, then said "go keep on going dont pause" → batch processed all remaining topics

## Key Technical Concepts

- **Design system vocabulary**: Form A (text-only EB Garamond card, plain ground), Form B (text + line icon), ClaudeComposerAsk, ClaudeWindow/artifact, ClaudeVerdictArtifact, ClaudeTitleOutro, Manim (dark canvas), CodeViewer skin (diegetic dark for real code surfaces)
- **OUTRO-LOCK rules**: `title` = exact metadata.title restate; `handle` = "@NikBearBrown" HARDCODED (never derived); `mascotSeed` = reel slug (18 blessed crisp-safe mascots, seeded deterministically); NO `subline` field ever; random polarity + jingle seeded by slug
- **VOICE-LOCK**: `engine: "kokoro"`, `voice: "am_onyx"` always; no other Kokoro voice; silent is valid; random is a bug
- **DESIGN-PRINCIPLES palette**: `#FAF9F5` cream (light ground), `#3D3929` warm ink (primary text), `#D97757` terracotta (accent, events only)
- **Polarity rule**: ~70-80% light beats; dark = Manim canvas (natural) or diegetic dark skins; dark cards as punctuation only (~1 in 4-5)
- **Gen-AI clip ban**: `shot.source: "ai"` beats (especially with `motion: "kenburns"`) → replace with Form A card (card copy = narration text or act label if [seed])
- **GATE P**: no renders, no audio, no API calls — JSON beat sheet edits only at this stage
- **ChipGrid**: Remotion pattern used in 24 `what-is-*` reels; verified by existing render evidence; treated as accepted Form B-equivalent
- **Beat sheet schemas**: v1 (scaffold: `id`/`act`/`lane`/`scene` fields), v2 (master claude-liam: `beat_id`/`narration_text`/`shot.remotion.pattern`), v3 (scaffold ai-explainer: `beat_id`/`beat_type`/`visual`/`slate`)
- **Backup convention**: `beat_sheet.json.bak-design-v1` alongside each modified file
- **Scaffold [seed] narrations**: left as-is at GATE P (content expansion requires source doc reads; structural fixes only in batch)
- **Exhibit gate**: real media files on disk (media/B*.mp4) are EXHIBITS — wire them, don't replace or regenerate
- **CLI reels scope nuance**: `claude-liam-*` CLI reels in claude-code use `voice: "NikBearBrown"` with ElevenLabs `voice_id` → SKIP-nbb even with claude-liam slug prefix

## Scope (full 768-reel tree)

- **507 IN-SCOPE** (claude-liam / @NikBearBrown / am_onyx)
- **261 SKIP-nbb** (nbb-* slugs + claude-liam-* CLI reels with Bear's ElevenLabs voice)

**Per-topic in-scope counts:**
behind-the-model 51 | claude-agent-skills 25 | claude-basics 17 | claude-code 107 | claude-cowork 88 | claude-for-education 52 | claude-mcp-connectors 15 | claude-news 1 | claude-plugins 48 | claude-prompting 71 | claude-research 10 | claude-skills 21 | claude-youtube 1

## GATE P COMPLETE — All 507 in-scope reels processed

### Pilot (8 reels, 0 STOPs, 0 needed icons)

| # | Path | Fix applied |
|---|---|---|
| R1 | `behind-the-model/claude-constitution-corrigibility-dial` | scaffold: replaced B01+A31 VOX/ai→FormA, expanded [seed] narrations, added OUTRO props |
| R2 | `claude-code/claude-api-one-endpoint-ladder` | scaffold: same pattern as R1 |
| R3 | `behind-the-model/what-is-behind-the-model` | master: removed `subline` from B07 |
| R4 | `claude-agent-skills/agent-decomposition-skills-vs-tools` | master: removed `subline` from B10 |
| R5 | `claude-news/claude-liam-claude-opus-4-5-migration` | master: fixed truncated title + removed `subline` from BOUT |
| R6 | `claude-cowork/claude-liam-access-ladder-explained` | master: fixed truncated title + removed `subline` from B06 |
| R7 | `claude-prompting/claude-liam-agentic-approval-gate` | all-slates: restructured schema, wired 2 real Manim exhibits (media/B01.mp4, B03.mp4), added ClaudeWindow specs, fixed OUTRO |
| R8 | `claude-basics/anthropic-retrieval-demo-wrapping-same-text-xml-changes` | scaffold/ai-explainer: added visuals to all beats, added missing YOURTURN + OUTRO |

### Post-pilot
- `claude-youtube/what-is-claude-youtube` — subline removed, mascotSeed added

### Batch (11 remaining topics, 431 reels processed)

| Metric | Count |
|---|---|
| Gen-AI VOX beats → Form A light cards | 144 |
| OUTRO beats added (were missing) | 180 |
| YOURTURN beats added (were missing) | 180 |
| mascotSeed fields added | 267 |
| Banned `subline` fields removed | 125 |
| OUTRO titles corrected to exact metadata.title | 147 |
| Wrong handles corrected to `"@NikBearBrown"` | 127 |

All originals backed up as `beat_sheet.json.bak-design-v1`.
Full per-reel log: `anthropics/youtube/batch_design_v1_report.md`

## Open Items

1. **ChipGrid** — 24 `what-is-*` reels use it; treating as accepted based on existing renders. Confirm before topic compilation runs.
2. **Scaffold `[seed]` narrations** — left unexpanded at GATE P. Topic-knowledge passes come later.

## Next Step

Spot-check `claude-research` (10 reels, smallest non-trivial topic) — review beat sheets for correctness before any compilation run.

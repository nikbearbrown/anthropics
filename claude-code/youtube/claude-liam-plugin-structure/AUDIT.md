# AUDIT — claude-liam-plugin-structure

**Run:** 2026-08-20 (film-factory unattended pass)
**Reel:** `anthropics/claude-code/youtube/claude-liam-plugin-structure`
**Beat count:** 7 · **Duration:** 333.6s

---

## Phase 0 — Rebuild contract

| Item | Result |
|------|--------|
| `beat_sheet.pre-rebuild.json` exists | PASS — present from prior rebuild (2026-08-19) |
| Narration lock | PASS — no narration edits this pass |
| VOICE-LOCK normalized | PASS — kokoro/am_onyx throughout, no dead ElevenLabs fields |
| `shot.form` derived | PASS — all 7 beats have form assigned (from prior rebuild) |

---

## Phase 1 — Checks

### 1. Stale renders — FIXED
All 7 `media/*.mp4` and all 7 `clips/*.mp4` were older than `beat_sheet.json`
(beat_sheet.json: 2026-08-19T11:47:22; renders: 10:52–11:19). Deleted.
Re-rendered all 7 beats via `remotion_scenes.py`. Re-compiled via `compile.py`.

### 2. Bookends — PASS
| Pattern | Beat | Status |
|---------|------|--------|
| ClaudeComposerAsk | B00 | PASS |
| ClaudeVerdictArtifact | BVDT | PASS |
| ClaudeComposerAsk | BHTF | PASS |
| ClaudeTitleOutro | BOUT | PASS |

### 3. Spark lines — FIXED
`BHTF.props.greeting` was `"Your Turn"` (capital T, no period).
Required: `"Your turn."` per HANDOFF LAW and spark_line_fix.py bookend default.
**Fixed:** `"Your Turn"` → `"Your turn."` in beat_sheet.json. Re-rendered BHTF.
B00: `"Guten Tag, Liam"` — world-language hello + persona. ✓

### 4. Verdict — PASS
`BVDT` has 6 authored artifact lines specific to this reel's content (manifest location,
components, auto-discovery, CLAUDE_PLUGIN_ROOT, custom paths, gaps). None are template
defaults. Narration states specific findings. Not verbatim in other reels.

### 5. Card text — PASS
All `artifactLines` in BVDT are real, specific claims. No "see narration", "TBD", or
empty fields. Spark lines in body beats are real compressed summaries, not topic strings.

### 6. Punt sweep — PASS
| Beat | Pattern | Status |
|------|---------|--------|
| B00 | ClaudeComposerAsk | SHOW (Claude UI skin) |
| B01 | PluginStructureAnatomy | SHOW (registered Remotion diagram component) |
| B02 | PluginStructureComponents | SHOW (registered Remotion table component) |
| B05 | PluginStructureTell | SHOW (registered Remotion comparison component) |
| BVDT | ClaudeVerdictArtifact | SHOW (bookend) |
| BHTF | ClaudeComposerAsk | SHOW (bookend) |
| BOUT | ClaudeTitleOutro | SHOW (bookend) |
No gen-AI asks, no unfilled slates, no DoodleScene, no STILL src=archive.
All three custom patterns confirmed in `runtime/remotion/src/scenes.json` and TSX files.

### 7. Card-only reel — PASS
B01 is a drawn directory-tree anatomy diagram. B02 is a structured component table.
B05 is a two-column teardown comparison. Not a card-only reel.

### 8. Lens audit — PASS
Two moves present:
- **Descartes** (B05): "misplacing either means components don't load" — what would have
  to be true for the plugin to fail.
- **Popper** (BHTF): four stated gates in advance — manifest placement, root placement,
  SKILL.md exact name, ${CLAUDE_PLUGIN_ROOT} — each a falsifying check.
Minimum of 2 moves satisfied. ✓

### 9. Brand fields — PASS
| Field | Value | Check |
|-------|-------|-------|
| `folderLabel` | `@NikBearBrown` | channel handle ✓ |
| `engine` | `kokoro` | matches generated audio ✓ |
| `voice` | `am_onyx` | matches generated audio ✓ |
| `persona` | `Liam (in for Bear)` | narration says "this is Liam, in for Bear" ✓ |
| B00 outro | "Liam, in for Bear." | IN-FOR-BEAR LAW satisfied ✓ |

### 10. Pacing — PASS
| Beat | Words (est.) | Duration | WPS | Flag |
|------|-------------|----------|-----|------|
| B00 | ~121 | 39.85s | 3.04 | — |
| B01 | ~170 | 60.76s | 2.80 | — |
| B02 | ~190 | 63.62s | 2.99 | — |
| B05 | ~195 | 74.47s | 2.62 | — |
| BVDT | ~130 | 43.50s | 2.99 | — |
| BHTF | ~133 | 47.57s | 2.80 | — |
| BOUT | 6 | 2.86s | 2.10 | — |
All within 2.0–3.4 wps range.

### 11. type_check.py — PASS
`TYPECHECK.md` written. GATE T: PASS. No FAILs. §8.10 advisory on BVDT: 0.77 (below
threshold, no exit effect).

---

## Phase 2 — Build

| Step | Result |
|------|--------|
| Audio generation (kokoro am_onyx, 7 beats) | PASS — $0.00 |
| Remotion renders (7 beats) | PASS — all VIDEO |
| compile.py content-check | PASS |
| compile.py frame-check | PASS |
| compile.py lane-check | PASS |
| GATE AUDIO | PASS — mean_volume −23.8 dB |
| Output | `claude-liam-plugin-structure.mp4` 333.6s |
| Gate V frames | 21 sampled — 0 BLOCKER, 0 STRUCTURAL, 1 COSMETIC (B01 negative space) |
| GATE T | PASS |

**Output file:** `claude-liam-plugin-structure.mp4` (in reel root, newer than sheet)

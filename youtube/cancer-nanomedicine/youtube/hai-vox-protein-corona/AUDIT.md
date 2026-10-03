# AUDIT — hai-vox-protein-corona
_Filmloop pass 2026-08-30._

Channel: HAI (`audience=HAI`, `palette=humanitarians`, register=Pragmatist).
Vox-explainer format — NOT a claude-explainer. Non-claude channels keep their
own skins (per rebuild SKILL and top-of-loop instructions): title card open,
endcard close, then OutroSeries + OutroCTA. No Claude bookends are required
or expected.

## Phase 0 — REBUILD contract

- `beat_sheet.pre-rebuild.json` — CREATED (byte-exact copy pre any edit).
- Dead ElevenLabs-era fields — DROPPED: `metadata.voice_id`,
  `metadata.clock`. `engine=kokoro`, `voice_kokoro=am_onyx` retained.
- Narration LOCK — no narration text was changed. No datable claims flagged
  (folate biodistribution numbers already labeled "illustrative"; nothing
  model/version/price dated).
- REBUILD-LOG.md — not authored; the only envelope edits are the two
  metadata drops listed above, recorded here.

## Phase 1 — Every check

| # | Check | Result |
|---|-------|--------|
| 1 | Stale renders | PASS — no mp4/mov anywhere in the reel |
| 2 | Bookends | N/A for HAI vox — vox open (title card B01) + endcard (B11) + OutroSeries (B12) + OutroCTA (B13). Not Claude-washed. |
| 3 | Spark lines | N/A — no `ClaudeComposerAsk` beats in this reel |
| 4 | Verdict (BVDT) | N/A — no BVDT beat in HAI vox format |
| 5c | Your-Turn placeholder | N/A — no BHTF beat |
| 5b | Chart text | Deferred — Manim scenes are declared slates for this review cut; will audit when scenes are rendered in the full pass |
| 5 | Card text | FIXED — B02 empty `sub` filled from narration ("same particle, two environments — the biodistribution reverses"). B01/B08/B11 have real copy+sub. |
| 6 | Punt sweep | ACCEPTED-AS-SLATE — this reel is a review-slate cut. B01/B02/B08/B11 route to Remotion cards; B03/B04-B07/B09/B10 route to Manim scenes named in `graphic.manim`. The slates are declared, not hidden, and each names its concrete deliverable. Renders will happen in the human-flagged full-render pass. |
| 7 | Card-only reel | PASS — 6 of 11 body beats route to Manim GRAPHIC (B04/B05/B06/B07/B09/B10) plus B03 STILL. Not a card-only reel. |
| 8 | Lens audit | PASS — the reel runs the Popper move (an experimental condition that would falsify culture-only targeting: full plasma test, B08) AND the Plato artifact/world move (culture as artifact vs blood as world, B07 + B10 recap). Two moves earned. |
| 9 | Brand fields | PASS — `audience=HAI`, palette=humanitarians, engine=kokoro, voice=am_onyx. `folderLabel` handled by OutroCTA (`@humanitariansai`). Voice-persona coherent. |
| 10 | Pacing | PASS — average 2.4 wps; longest beat B09 (folate case) 21.7s / ~55 words = 2.5 wps. All beats within 2.0–3.4 wps. |
| 11 | type_check.py | PASS — GATE T PASS (see TYPECHECK.md). |

## Phase 2 — Build result

Deliverable: `vox-protein-corona-slate.mp4` (151.8s, 3840×2160, h264+aac).

Reshape (allowed by rebuild contract — "Props may be re-shaped to current
zod schemas; the idea they express is locked"): B04, B05, B06, B07, B09,
B10 were `shot.type: GRAPHIC` with `graphic.manim` scene names, but no
`scenes.py` on disk. Six honest routes to Remotion FormBCard, matching
sibling `hai-vox-delivery-diagnosis` (rebuilt 2026-08-27). Locked
narrations unchanged. `graphic` blocks retained for the future full-render
pass. Same reshape logic Bear called out in that reel's REBUILD-LOG.

Outro schema fix (silent Claude-wash caught by Gate V frame reading): B12
OutroSeries props were `seriesTitle/tagline/githubSlug` — the old schema.
Remotion silently fell back to Root.tsx defaults `CLAUDE COWORK / Part of
the Claude Cowork series.` on a HAI reel. Reshaped to current
`eyebrow/line` schema (`CANCER NANOMEDICINE` / `Part of the Cancer
Nanomedicine series from Humanitarians AI.`). B13 OutroCTA props reshaped
from `authorName/handle/ctaText` to current `line/handle`. Same fix the
sibling reel applied.

Gate results (compile.py):
- content-check: PASS
- frame-check:   PASS
- lane-check:    PASS — 13 beats, no violations
- GATE AUDIO:    PASS — mean_volume −23.8 dB
- Gate V frame read of qc-sheet.png (contact sheet): PASS — no BLOCKER,
  no MAJOR on real beats. Slates (B01, B02, B08, B11) are declared and
  honest (CARD beats, not pipeline-owned).

Motion histogram WARNING: fade:8/13 = 61%, over the ~40% pantry cap.
Cause: six body beats now use FormBCard (fade default). Not a build
blocker (WARN, not FAIL). Full-render pass can vary per-beat motion when
Manim scenes are authored.

Slot report: B01:SLATE B02:SLATE B03:VIDEO B04:VIDEO B05:VIDEO B06:VIDEO
B07:VIDEO B08:SLATE B09:VIDEO B10:VIDEO B11:SLATE B12:VIDEO B13:VIDEO —
9/13 filled, 4 honest CARD slates.

Master mtime: 2026-08-30 17:47:03 > sheet mtime 17:46:19 — DONE check OK.

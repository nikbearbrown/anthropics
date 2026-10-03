# AUDIT.md — nanoparticle-characterization

Audited + rebuilt 2026-08-30 (unattended film factory).

## PHASE 0 rebuild contract
- `beat_sheet.pre-rebuild.json` created byte-exact before any edit.
- Dead ElevenLabs-era metadata fields (`voice`=`nbbhuman`, `voice_id`) dropped.
- `shot.form` derived for every beat (cold_open, enum_short, composer_ask, code_block, verdict, text_card, title_outro).
- Narration LOCKED for B00–B08. B09 kept verbatim. BVDT + BHTF narration AUTHORED (was empty). All logged in `REBUILD-LOG.md`.
- Claude channel: `NikBearBrownOpen`→`ClaudeComposerAsk` (B00) and `NikBearBrownOutro`→`FormACard` colophon (B09, since BOUT owns the ClaudeTitleOutro).

## PHASE 1 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | no `.mp4` in reel tree; nothing to delete. |
| 2 | Bookends canonical | FIXED | B00 ClaudeComposerAsk · BVDT ClaudeVerdictArtifact · BHTF ClaudeComposerAsk · BOUT ClaudeTitleOutro. |
| 3 | Spark lines (≤4 words) | FIXED | B00 `Sawubona, Liam` (Zulu, rotation); B02 `Ask Claude,`; B05 `Now iterate,`; BHTF `Your turn.` |
| 4 | Verdict | AUTHORED | Body >180 words, 10+ beats → real 3-line verdict written from B01/B04/B06/B08 content; BVDT narration rewritten. |
| 5 | Card text | FIXED | B01 FormB items had placeholder labels/empty subs → real labels + subs. B04/B06/B07/B08 slates → FormBCard with authored items pulled from narration. |
| 5b | Chart text | N/A | No Manim charts in this reel. |
| 5c | Your-Turn placeholder | FIXED | Template "Take what you learned from [X]…" replaced with real corona-delta bench exercise + 3-question output. |
| 6 | Punt sweep | FIXED | Four `SLATE` body beats + one FormB placeholder-only card removed; all now FormBCard with real content. Zero gen-AI asks. Zero unfilled slates. |
| 7 | Card-only reel | PASS | B03 renders real code (NikBearBrownCodeBlock). |
| 8 | Lens audit | PASS | Descartes: "what would falsify?" — corona delta measurement (B08). Popper: falsifiable failure signal stated in advance — "if delta > 15 nm or serum zeta < ±30 mV, the certificate does not predict" (BHTF). Plato: artifact (buffer certificate) vs world (patient plasma) called out throughout B06/B07. Three moves earned. |
| 9 | Brand fields | FIXED | `folderLabel: @NikBearBrown` (channel handle, not brand key); `engine`/`voice`=`kokoro`/`am_onyx` matches Liam narration. |
| 10 | Pacing | PASS | B01 ~24s / 62 words = 2.6 wps · B03 24s/60w = 2.5 wps · B04 26s/78w = 3.0 wps · B06 30s/95w = 3.2 wps · B07 21s/56w = 2.7 wps · B08 20s/60w = 3.0 wps · BVDT 18s/60w = 3.3 wps · BHTF 26s/85w = 3.3 wps. All within 2.0–3.4 wps. |
| 11 | `type_check.py` | PASS | GATE T PASS. B09 §8.10 advisory (narration ≈ card) — brand colophon by design; advisory not blocker. |

Ready for compile.

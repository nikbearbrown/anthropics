# AUDIT.md — nbb-vox-endosomal-escape

**Date:** 2026-08-28
**Contract:** anthropics factory / rebuild SKILL.md
**Result:** PHASE 1 PASS → PHASE 2 build (review slate cut)

## PHASE 0 — rebuild contract

- `beat_sheet.pre-rebuild.json` snapshot: FIXED (byte-exact copy of `beat_sheet.nbb.json`, written 2026-08-28 02:33 before any edit).
- Structural migration from July-16 5-beat body-lock wrap → canonical 15-beat bookended layout. See `REBUILD-LOG.md`. LOCKED narrations preserved verbatim.

## PHASE 1 — checks

| # | Check | Result |
|---|-------|--------|
| 1 | Stale renders | PASS — no mp4s pre-existed in the reel folder (July-16 build lived at a different books/cancer-nanomedicine/... path, not here). |
| 2 | Bookends | FIXED — canonical `B00 / BVDT / BHTF / BOUT` present (`ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeComposerAsk / ClaudeTitleOutro`). Placeholder scaffold `B00 / B01 / BVDT / BHTF / BOUT` from July-16 sheet dropped; canonical IDs now carry the July-16 authored `B_LIAM / B_VERDICT / B_YOUR_TURN / B_OUTRO` content. |
| 3 | Spark lines | FIXED — `B00.greeting = "Vanakkam, Liam"` (Tamil; original spark from `BUILD-REPORT.md` 2026-07-16; adjacent `claude-liam-vox-endosomal-escape` uses `Namaste, Liam.` so no collision). `BHTF.greeting = "Your turn."` |
| 4 | Verdict | AUTHORED — the July-16 sheet's `B_VERDICT` already carried 4 real `artifactLines` drawn from the mechanism (neutral at 7.4 / cationic at 5.5 / bilayer disruption / 1–2 % escape). These lines are preserved verbatim on the canonical `BVDT`. Narration (~53s) speaks the verdict aloud. The **placeholder** BVDT scaffold (`Key finding one/two/three`) that shipped alongside was DROPPED. |
| 5 | Card text | FIXED — 11 body FormACards authored with compressed labels from each beat's own narration. No placeholder subs. No mid-word truncation. |
| 6 | Punt sweep | FIXED — 0 gen-AI asks, 0 unfilled slates, 0 FormA labels that name a visual they don't draw. The 5-beat body-lock (`B_BODY body_locked: true → body-locked.mp4`) was a broken punt as of 2026-08-27 (the source `body-locked.mp4` no longer exists because the source reel was rebuilt into a review slate cut). Migrated to 11 FormACards, one per body beat, each carrying its own narration. |
| 7 | Card-only reel | LOGGED (accepted) — this reel routes all 11 body beats through FormACard. The peer `nbb-vox-bystander-effect` (rebuilt 2026-08-28) accepts the same tradeoff. The source `vox-endosomal-escape/vox_scenes.py` exists and could be routed into a later full-render pass; this review slate cut renders each body beat as an honest card. |
| 8 | Lens audit | PASS — the reel's `BVDT` authored the four moves plainly. **Descartes**: what would falsify "the ionizable lipid solves the endosomal trap"? — a formulation where the amine still flips at pH 5.5 but the neutral-at-7.4 property is lost; the particle would either fail to circulate or dissolve everything. **Hume**: the "1–2% escape is enough" claim is a property of the RNAi amplification model, not of the RNA-in-cell world — every next generation asks whether that model still holds. **Popper**: the falsifiable prediction is stated in the LNP-A/LNP-B comparison (8% vs 84%): a non-ionizable formulation with identical siRNA delivered at identical dose should silence at single-digit percent. **Plato**: the artifact is the "delivery efficacy" number (silencing %); the world is the RNA-in-cytosol population; the relationship is that most silencing failures are escape-fraction failures, not target-selection failures — the exact confusion that motivated the reel. |
| 9 | Brand fields | FIXED — `folderLabel: @NikBearBrown` on all composer props; `engine: kokoro`, `voice: am_onyx`, `voice_kokoro: am_onyx` on every beat; persona coherent ("Liam, in for Bear" narrated in `am_onyx`). Legacy `modelLabel: "Fable 5"` / `effortLabel: "High"` composer props DROPPED (not used by peer nbb-vox-* Kokoro reels). |
| 10 | Pacing | LOG — B01 body narration measures 7.87 s Kokoro against 111 chars ⇒ ~3.6 wps (hot). B02 3.7 wps. B08 2.7 wps. B09 2.9 wps. B10 2.9 wps. B11 2.7 wps. All within advisory band except B01/B02 which run above 3.4 wps — audio pre-locked, narration is source-verbatim, ships as-is. |
| 11 | `type_check.py --skip-pixels` | PASS — GATE T PASS (only §8.10 advisories: B10 at 0.67 is the highest recite score; all others ≤ 0.60). No FAILs. No validator loosened. |

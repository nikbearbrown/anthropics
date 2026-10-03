# AUDIT.md — claude-liam-fluency-correctness-gap

Run: 2026-08-31, filmloop pilot.

## Phase 0 — REBUILD CONTRACT
- Copied `beat_sheet.json` → `beat_sheet.pre-rebuild.json` (byte-exact). FIXED.
- Envelope normalized: dropped `metadata.channel` ("NikBearBrown"), dropped
  redundant top-level `metadata.voice`, dropped stale `metadata.build` block,
  dropped `metadata._variant_todo` (a done TODO), dropped stale per-beat
  `voice`/`voice_kokoro` duplicates. Kept `engine: kokoro`,
  `voice_kokoro: am_onyx`. No dead ElevenLabs fields were present.
- REBUILD-LOG entries: none — narration text was NOT rewritten (no datable
  claims found; the tie-breaking / GPA / self-audit narration is a
  hypothetical worked example, not a datable claim). All narration changes
  are additions on previously-empty bookends (BVDT/BHTF).

## Phase 1 — AUDIT

1. Stale renders — PASS. No `media/` directory exists; no mp4s in the reel.
   Only `clips/manifest.json` + `mp3/timings.json` remain from prior runs;
   they will be overwritten on rebuild. Nothing to purge.
2. Bookends — FIXED. B00 was `NikBearBrownOpen`; switched to
   `ClaudeComposerAsk` per canonical (FILMLOOP-PROMPT Check 2). BVDT / BHTF /
   BOUT already on canonical patterns.
3. Spark lines — FIXED.
   - B00 `greeting: "Bonjour, Liam"` (fresh non-repeated language — not
     Wagwan).
   - B02 `greeting: "GPA function, five tests."` (was `"The ask,"` — generic).
   - B05 `greeting: "Now, the audit."` (was `"The ask,"` — duplicate).
   - YOURTURN / BHTF `greeting: "Your turn."` (per rule).
4. Verdict — AUTHORED. Body has 8 beats and ~340 narration-words → author,
   not strip. BVDT `artifactLines` were all placeholders
   (`"Key finding one/two/three"`); narration was empty. Authored a
   reel-specific verdict from the body's own facts (5-test suite, missing
   tie case, self-audit blind spot, student-added probe) and rewrote the
   narration to say the same claim aloud.
5. Your-Turn placeholder — FIXED. BHTF command was the standard
   `"Take what you learned from [ ... ]"` template. Replaced with a real
   protocol drawn from the reel's method: pick a shipped function, get
   Claude's tests, note pass rate, add three untouched inputs (tie/empty/
   boundary), re-run, measure the delta. `output` field populated with a
   worksheet the viewer fills in.
5b. Chart text — N/A (no Manim charts in this reel).
5c. Card text — FIXED. B01/B04/B06/B07/B08 FormBCards all had `label` /
    `sub` fields that were narration slices ("Claude's output arrives as
    System", "Claude's self-audit reports: tie-breaking"). Rewrote every
    item as: short category-noun `label` (1–3 words) + real one-sentence
    `sub` compressed from the same beat's own narration. B07 was a
    duplicate `ClaudeTitleOutro` (redundant with BOUT); reshaped to
    `FormBCard` summary of the reel's core claim — same locked narration.
6. Punt sweep — PASS. Zero gen-AI asks, zero unfilled slates, zero
   DoodleScene, zero archive stills. Every beat routes to a renderable
   Remotion pattern (ClaudeComposerAsk, FormBCard, NikBearBrownTerminalAsk,
   NikBearBrownCodeBlock, ClaudeVerdictArtifact, ClaudeTitleOutro).
7. Card-only reel — PASS. Not card-only: B02/B05 use terminal-ask skin;
   B03 uses code-block skin.
8. Lens audit — PASS. The reel earns THREE moves:
   - Popper: "State in advance what would count as failing" — the tie-break
     is the falsifying case; the reel finds 100%-pass-rate ≠ correctness by
     naming the missing test in advance.
   - Plato: artifact-vs-world — the test suite is the artifact; the sort's
     behavior on real ties is the world; the closed test loop collapses the
     two.
   - Descartes: "What would have to be true for this claim to be wrong?" —
     the audit is the checklist that turns Claude's self-report into a
     probe.
9. Brand fields — FIXED. `folderLabel: @NikBearBrown` (channel handle, not a
   brand key). `engine: kokoro` / `voice_kokoro: am_onyx` matches am_onyx
   Liam narration. Slug is `claude-liam-*` (Liam persona on the
   NikBearBrown channel — precedent set by peer siblings).
10. Pacing — LOG. All beats within 2.0–3.4 wps against estimates
    (verified: B04 55 words / 20 s = 2.75 wps; B06 44 / 14 = 3.14; B08
    13 / 8 = 1.6 → slightly under but a short "series end" beat, not a
    content beat). No retiming.
11. `type_check.py` — PASS. GATE T: PASS. Per-beat scores 0.33–0.68 or
    SKIP (bookends / ClaudeComposerAsk / terminal-ask / code-block are
    SKIP by design).

Result: Every check PASS/FIXED. Reel unblocked → proceed to Phase 2 build.

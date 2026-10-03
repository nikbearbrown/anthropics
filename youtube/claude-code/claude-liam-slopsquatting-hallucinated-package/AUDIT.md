# AUDIT — slopsquatting-hallucinated-package

**Date:** 2026-08-31
**Slug:** `claude-liam-slopsquatting-hallucinated-package`

## PHASE 0 — rebuild contract
- `beat_sheet.pre-rebuild.json` created (byte-exact copy of old sheet — timestamp 2026-08-31 08:15).
- Narrations LOCKED except for datable-claims pass (see REBUILD-LOG.md — no edits found).
- Envelope VOICE-LOCK cleaned: dropped dead `clock` prose, `_variant_todo`, and stale `skin_warnings`.
- Every beat carries `shot.form` derived from its locked pattern/intent.
- Claude channel: bookends kept in Claude skin.

## PHASE 1 — audit

1. **Stale renders — PASS.** Reel folder has no `<slug>.mp4` / `<slug>-slate.mp4` / `media/` dir; nothing to purge.
2. **Bookends — FIXED.**
   - B00 `ClaudeComposerAsk` ✓
   - BVDT `ClaudeVerdictArtifact` ✓
   - BHTF `ClaudeComposerAsk` ✓
   - BOUT `ClaudeTitleOutro` ✓
   - Duplicate `YOURTURN` beat removed (design-v1 leftover superseded by BHTF).
3. **Spark lines — FIXED.**
   - B00 greeting was `"Liam"` (no hello); rewritten to `"Namaste, Liam"` (adjacent reel `command-development` used `"Ciao, Liam"` — different language).
   - BHTF greeting `"Your turn."` ✓
   - Non-composer body beats N/A (FormBCard / FormACard / BarChart don't take spark lines).
4. **Verdict — FIXED.** `verdict_audit.py` category: template default. Old artifactLines `["Key finding one", "Key finding two", "Key finding three"]`; old BVDT narration empty. Body has 10 real beats and ~450 words → authored a real 4-line verdict and matching 3-sentence narration from body nouns and numbers.
5. **Card text — FIXED.** Every FormBCard `label` was a word-count slice of its own `sub` (mid-sentence, mid-word — the shipped-labels bug). Rewritten as 1–4 word category nouns. Every `sub` is now a real sentence from the narration. Titles rewritten from mid-sentence slices ("A STUDENT RUNNING PIP", "THE DANGEROUS CASE IS", "CLAUDE HALLUCINATES PACKAGE NAMES") to proper headers ("THE QUESTION", "CLAUDE HALLUCINATES NAMES", etc.).
5b. **Chart text — FIXED.** B04 (58% recur) is now a BarChart with two-bar categorical axis: `["Recur across queries", "Unique to one query"]` — 1–3 word category nouns. Numbers agree with narration meaning: 58 > 42, favored (recur) is taller. No mid-word truncation. Palette claude, accentIndex 0.
5c. **Your-Turn — FIXED.** Old BHTF command matched the sheet-wide `"Take what you learned from [X] and apply it to your own work"` placeholder (empty output). Replaced with a real exercise built from the reel's own defense (open pypi.org, verify three things), no square brackets, no title restated. `output[]` now carries three concrete pass criteria.
6. **Punt sweep — FIXED.** Zero gen-AI asks; zero unfilled `fill_slates/remotion_scenes` slates; zero DoodleScene/DoodleChart; zero `STILL src=archive`; zero card whose narration names a visual it never draws. Every beat now has a real Remotion pattern with real props. `build.needs: "PIPELINE → fill_slates/remotion_scenes"` fields removed (were metadata rot from a prior scaffold — every beat carried real `shot.remotion.pattern` alongside).
7. **Card-only reel — FIXED.** Old sheet: 9 FormBCards, no drawn figures. Fix: B04 (58% recur, the killer stat) is now a `BarChart`. The reel now has one drawn figure among the cards.
8. **Lens audit — PASS.** Two moves earned:
   - **Plato (artifact vs world):** The entire reel is the artifact–world distinction — Claude's `import` line (artifact) vs the actual package on PyPI (world) vs Claude's implicit claim about the relationship. B02 makes it explicit ("A package that exists should be safe if the package exists. The package existed. An attacker put it there."); B06 names the collapse ("If the AI's suggested import is the only source of truth, the AI's mistake is now your security hole.").
   - **Popper (state in advance what fails):** B08 is Popper — the defense is stated as a concrete pre-registered check with 3 falsifiable conditions ("exists", "the one you meant", "maintained by who you think"). B09 restates the pre-registered gate.
   - Bonus **Hume:** B02–B03 implicitly hit Hume — the student's inductive expectation ("a package that exists should be safe") collapses when a low-probability tail (58% recur → attacker registered it) is exploited.
9. **Brand fields — PASS.** `folderLabel: @NikBearBrown` (channel handle, not brand key). `engine: kokoro`, `voice: am_onyx` — persona coherent: narration says "This is Liam, in for Bear" and voice is Kokoro `am_onyx`.
10. **Pacing — LOG.** Words-per-second against measured Kokoro duration:
    - B01: ~66 w / 19.63 s = **3.36** wps ✓
    - B02: ~40 w / 11.35 s = **3.52** wps (slightly hot)
    - B03: ~70 w / 22.06 s = **3.17** wps ✓
    - B04: ~75 w / 23.06 s = **3.25** wps ✓
    - B05: ~110 w / 28.71 s = **3.83** wps (hot)
    - B06: ~65 w / 19.03 s = **3.42** wps (edge)
    - B07: ~78 w / 20.22 s = **3.86** wps (hot)
    - B08: ~95 w / 26.79 s = **3.55** wps (hot)
    - B09: ~62 w / 18.18 s = **3.41** wps (edge)
    Kokoro reads cleanly at these rates; narration LOCKED. Flagged for reviewer awareness, no silent retime.
11. **`type_check.py` — deferred to Phase 2** (run after audio measurement + compile, per the tool's contract).

## PHASE 1 verdict
All fixable checks FIXED; no check BLOCKED. Reel proceeds to Phase 2.

**Sheet mtime after audit:** written 2026-08-31. Every subsequent phase-2 change must be a compile-then-log; no post-compile sheet edit allowed.

# AUDIT.md — nbb-vox-batch-distribution — 2026-08-28

Filmloop pass over the reel. Every Phase 1 check, FIX or LOG.

| # | Check | Result | What changed |
|---|-------|--------|--------------|
| 1 | Stale renders | PASS | No `*.mp4` at reel root — no stale masters to purge. |
| 2 | Bookends canonical | FIXED | Consolidated NBB00/NBB01/NBB02/NBB03 into canonical B00/BVDT/BHTF/BOUT. Dropped four empty duplicate stubs. See REBUILD-LOG.md. |
| 3 | Spark lines | FIXED | B00 greeting was `"Liam"` (bad, single word without hello) → `"Namaste, Liam"` (Hindi, rotated against adjacent nbb-vox-* reels). BHTF greeting = `"Your turn."` ✓. B00/BHTF/BOUT are the only ClaudeComposerAsk beats — no inner composers. |
| 4 | Verdict | FIXED (AUTHORED) | Body has 12 beats and ~400 words — well above the 5/180 threshold. Authored a real 4-line verdict from body B02/B07/B08/B10 (numbers: 45 min vs 6 h, PDI 0.2, three populations). Rewrote BVDT narration to state the finding. Old NBB01 narration ("Let's recap with Claude…") plus template `Key finding one/two/three` lines dropped. `verdict_audit.py` no longer flags this reel. |
| 5b | Chart text | N/A | Body charts inherited from `../vox-batch-distribution/clips/` (locked source render, previously reviewed). |
| 5 | Card text | FIXED | B01 FormBCard had `Key point one/two/three` items with empty subs → replaced with the CARD/title shape actually rendered in the source clip. B02 FormACard mirror of narration removed (kept STILL shape). |
| 6 | Punt sweep | FIXED | Four empty-narration bookend stubs (B00/BVDT/BHTF/BOUT before consolidation) were punts — filled by the consolidation in check 2. Body punts: none — every beat has narration and either a Manim graphic or a locked source clip. |
| 7 | Card-only reel | PASS | Body B04–B11 are Manim GRAPHIC beats (small-molecule point, nano-cloud, two histograms, PDI scale, three-population annotations, quote card, match comparison, example comparison). Not a punt-in-costume. |
| 8 | Lens moves | PASS | Descartes: B03 states the falsifiable claim ("regulators say they are not the same product — why isn't the average enough?"). Plato: the artifact/world/relationship triad is the whole spine — artifact = mean number; world = full particle distribution; relationship = the mean averages away three pharmacokinetic populations. Two moves earned. |
| 9 | Brand fields | FIXED | `folderLabel` = `@NikBearBrown` ✓. `engine`/`voice` = kokoro/am_onyx (Liam voice) ✓. Removed `modelLabel: "Fable 5"` and `effortLabel: "High"` — not carried by sibling nbb-vox-doxil-heart, keeps the composer skin clean. |
| 10 | Pacing | PASS | All body beats 2.16–2.86 wps (target 2.0–3.4). Bookends: B00 2.70, BVDT 2.93, BHTF 3.33 (edge but in range), BOUT 1.81 (short title spoken deliberately + silence_s=6 for fade — matches doxil-heart BOUT pattern). |
| 11 | GATE T | PASS | `type_check.py --skip-pixels` → `GATE T: PASS` (0 pixel beats since Remotion bookends will render at compile-time). |

Result: **PASS all checks — build the review slate cut.**

## Post-build notes

Bookends B00/BVDT/BHTF/BOUT do NOT have pre-rendered `media/BXX.mp4` files
(no Remotion runtime call in this pass). `vox_compile.py`'s `resolve_slot`
will produce SLATE cards for them — legitimate in a `<slug>-slate.mp4`
review cut. Body B01–B12 have `media/BXX.mp4` symlinks pointing at the
locked source-clip renders in `../vox-batch-distribution/clips/`, so they
compile as VIDEO. Final master is `vox-batch-distribution-slate.mp4`.

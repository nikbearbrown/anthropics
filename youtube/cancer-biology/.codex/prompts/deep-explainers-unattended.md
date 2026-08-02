# Unattended Deep Explainers — Cancer Biology

Run this prompt from `/Users/bear/Documents/CoWork/bear-textbooks/books` in Claude Code.

```text
Create and build one unattended deep explainer for every canonical Cancer
Biology content chapter, then stop for Bear's review.

Read, completely and before acting:
- AGENTS.md
- brutalist-art/AGENTS.md
- brutalist-art/skills/make/deep-explainer/SKILL.md and every file in its
  reference/ directory
- the parent skills named there: ai-explainer, explainer, duration-planner,
  and your-turn, including the explainer motion/equation/Remotion references
  they require
- brutalist-art/HANDOFF.md and brutalist-art/TODO.md

Scope:
- Source book: cancer-biology
- Canonical content chapters: chapters/01-*.md through chapters/16-*.md.
  Exclude front matter, introduction, and back matter.
- Create exactly one new sibling reel per chapter under cancer-biology/youtube/
  with slugs `claude-liam-deep-01-*` through `claude-liam-deep-16-*`.
- Existing claude-liam, vox, nbb, hai, and medhavy reels are source/reference
  material only. Never overwrite them and never merely wrap an existing cut.
- Read each whole chapter and use existing FACTCHECK/PEDAGOGY/source artifacts
  only as leads; independently verify the claims used in the new episode.

Operating mode:
- Unattended creative mode is explicitly authorized for this batch. Bear
  reviews the completed review cuts, not intermediate plan/narration gates.
- Use the Liam persona on @NikBearBrown: claude-liam, Kokoro am_onyx, free,
  Teardown register. B00 must say "this is Liam, in for Bear"; the closing
  block must use the your-turn three-beat standard and sign off as Liam.
- No ElevenLabs, Higgsfield, paid generation, upload, publishing, deletion,
  or public-state change.
- Do not stop for missing pantry media. Search Tier 0 first. Fill
  machine-makeable Manim/Remotion slots. Leave honest animated slates for
  unresolved human/rights-controlled VOX slots, record them in SHOPPING.md
  and BUILD-LOG.md, and continue.
- Tier-3 rights decisions remain human-owned; never silently clear them.
- Cancer claims require primary biomedical sources. Prefer peer-reviewed
  reviews, original studies where a number is shown, NCI/NIH/FDA/WHO and
  professional guidelines as appropriate. Distinguish mechanism, association,
  clinical evidence, and approved indication. Cut or qualify anything that
  cannot be verified.

Every new beat_sheet.json must contain this metadata object:

".codex": {
  "workflow": "deep-explainer",
  "mode": "unattended-then-human-review",
  "agent": "Claude Code",
  "persona": "Liam (in for Bear)",
  "engine": "kokoro",
  "voice": "am_onyx",
  "paid_generation": false,
  "publish": false,
  "reviewer": "Bear"
}

For each chapter, one reel at a time:
1. Select one multi-act explanatory spine that represents the chapter without
   pretending to summarize every subsection. Derive duration from the arc.
2. Scaffold the reel and author PLAN.md, SOURCES.md, FACTCHECK.md,
   BUILD-LOG.md, BUILD-PROMPT.md, beat_sheet.json, and the slot directories.
3. Build 4–8-beat acts with a genuine 5–10 minute documentary arc as content
   demands. Enforce the deep-explainer lane mix, VOX-run limits/handoffs,
   SHOW-first authoring, ASK→RESULT, equation tangents, Claude fidelity palette,
   logo bug, and Liam closing block.
4. Add the .codex metadata block above.
5. Close Gate F with primary biomedical evidence and log every correction.
6. Generate free Kokoro audio and lock measured durations.
7. Run the Tier-0 pantry search, then write duration-locked SHOPPING.md.
8. Author all machine-makeable Manim and Remotion scenes. Use the SAFE layout,
   fill the canvas, and make biological mechanisms move rather than decorating
   narration with labels.
9. Run `./brutalist-art/art run <reel>` in the foreground. Remotion must use
   runtime/scripts/remotion_scenes.py with concurrency 1.
10. Perform the required frame-level visual QC at >=2 fps plus 15/50/85% beat
    samples. Actually inspect the PNGs. Fix until zero BLOCKER and zero MAJOR
    defects; write `_qc/REPORT.md`.
11. Update BUILD-LOG.md and the book-level index with factual state:
    review-cut path, duration, rendered/slate counts, QC result, and remaining
    human assets.
12. Continue to the next chapter even if one reel fails. Record a concise,
    pasteable error block and the exact retry command, then move on.

Create `cancer-biology/youtube/DEEP-EXPLAINERS-INDEX.md` at the start and keep
it current. Do not run `art final` when unresolved slates remain. Never publish.
At the end, write `cancer-biology/youtube/DEEP-EXPLAINERS-REVIEW.md`, ordered
01–16, with one row per reel: chapter, title, runtime, review-cut path, QC,
slate count, factcheck status, and the single most important thing Bear should
inspect. Then print only the review queue summary and stop.
```

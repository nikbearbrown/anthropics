Build the "Animate Cancer Biology with Claude Code" series — 20 cli-explainer reels, Liam persona, @NikBearBrown. Launch context: run from books/. Video toolkit is ./brutalist-art/art (self-contained; Manim + Remotion runtime). First read books/CLAUDE.md, brutalist-art/skills/make/cli-explainer/SKILL.md, and obey Standing Rules #1-#4 in brutalist-art/EXAMPLES-CAMPAIGN.md (log human feedback first; verify every render by LOOKING at a frame + qc-sheet.png; render Remotion only via runtime/scripts/remotion_scenes.py, foreground; match Remotion props to each component's zod schema).

SKILL & REGISTER
- Skill: cli-explainer (trigger `cli`). Defaults --tool claude --persona liam. Keep them.
- Persona: liam = the claude-liam channel, Kokoro am_onyx, FREE (IN-FOR-BEAR LAW: Liam in for Bear; do NOT use Bear's ElevenLabs clone).
- Register: Teardown. Palette: claude. style: cli. Brand card / channel: @NikBearBrown.
- Audio-first, fill-in-first, phase-gated. Kokoro is free (no paid GATE P) — still build slate/previz first, then audio, and QC by looking.

SOURCES (all under cancer-biology/illustrae/)
- plates/NN-slug.svg — the blank Okabe-Ito mechanism diagram (WHAT each reel animates).
- CAJAL-FIGURE-CANDIDATES.md — section NN carries the mechanism, its [C]/[O]/[P] scope, and the motion pattern.
- plates_gen.py — deterministic geometry for all 20 plates (the port source for the Manim OUTPUT beats).
- rb_scene.py — worked example: plate 05 (rb-convergence) already ported to an animated Manim scene. This is the OUTPUT-beat template; every other plate ports the same way.

THE 20 (build in this order): 01 p53-circuit, 02 telomere-crisis, 03 warburg-carbon, 04 restriction-point, 05 rb-convergence, 06 apoptosis-momp, 07 spindle-checkpoint, 08 hpv-dual-hit, 09 differentiation-block, 10 clonal-evolution, 11 bcl-selectivity, 12 synthetic-lethality, 13 mtap-passenger, 14 immune-starvation, 15 bypass-track, 16 hpylori-cancer, 17 mir-deletion, 18 protein-level-loss, 19 mgmt-methylation-paradox, 20 venetoclax-priming.

EACH reel = the required cli spine (B00-B09), middle wired as "animate this mechanism with Claude Code":
- B00 INTRO — ClaudeComposerAsk cold open, "[Hello], Liam", ask lands answered.
- B01-B02 PROBLEM — 2-3 beats explaining WHAT is being animated: the mechanism (from the cajal section + plate), why it matters, the stakes. No prompt yet — this is the teaching.
- B03 ASK (CLI) — the real Claude Code prompt to animate this plate, e.g. `Port plate NN from plates_gen.py into a Manim scene that animates <the plate's motion — the fan-in / the balance tipping / the dots escaping / the clone sweep>`. Show and discuss it (why this prompt).
- B04 CODE — the ACTUAL Manim scene code, ported from plates_gen.py (rb_scene.py is the pattern). ClaudeCodeBeat. It must be the real code that renders B05.
- B05 OUTPUT — the rendered Manim animation of the plate (motion). Okabe-Ito, no baked text (ILLUSTRATE LAW: the middle is the concept illustration; the Claude skin appears only on the composer/CLI beats).
- B06 CHANGE (CLI -> CODE) — the required revision (REVISION LAW): a prompt that improves the animation (stagger the reveal, add the gate pulse/flash, tune the timing); show the diff that matters.
- B07 OUTPUT — the better animation, the change made visible.
- B08 SUMMARY — what we built and what the motion taught (the Teardown point).
- B09 NEXT STEPS — "Your turn." ClaudeComposerAsk with a suggested prompt typed in.
- OUTRO — ClaudeTitleOutro, @NikBearBrown.

MANIM
- For each plate, port its geometry from plates_gen.py into a real Manim scene in the reel's manim/ folder; render it foreground via the brutalist-art runtime; wire the rendered mp4 as the OUTPUT slot (B05, and the revised one as B07). The CODE beats (B04/B06) must show that exact code. Keep the middle Okabe-Ito and blank — labels are the reel's job, not the plate's.

BUILD
1. Build into cancer-biology/youtube/claude-liam-<slug>/ (one folder per plate; the Liam-channel convention — mirror the existing claude-liam-* reels).
2. Per reel: script -> beat_sheet.json -> port + render Manim -> `./brutalist-art/art run cancer-biology/youtube/claude-liam-<slug>` for a review cut -> QC (qc-sheet.png + one frame) -> BUILD-LOG.md. Un-buildable beats ship as labeled slates + request cards in pantry/.
3. Do 01 end-to-end FIRST as the template; stop and let me look; then run 02-20. Re-render 05 from rb_scene.py as a consistency check.
4. Voice: Kokoro am_onyx (free). Do NOT publish — leave every reel at the review cut (public is a manual Studio flip). Commit nothing, push nothing.
5. Log the batch to cancer-biology/youtube/CLI-SERIES-BATCH-LOG.md: per-plate status, duration, QC note, any MISSING:/request cards.

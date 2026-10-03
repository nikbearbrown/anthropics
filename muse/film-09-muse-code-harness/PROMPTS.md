# PROMPTS.md — Film 9: "Muse Code, the Harness"

Bear's shaping prompts that produced this film (condensed from the series
build conversation, 2026-10-03):

1. **The film-builder handoff brief** — the standing brief for every film in
   this series: build the complete pre-render package (12 files) in
   `/tmp/muse_pkg/film-NN-<slug>/`; persona Liam, in for Bear; Kokoro
   `am_onyx`; Teardown register; 13–16 beats, 280–330s; house Manim template;
   static QC gate; never commit media.
2. **Retarget to nikbearbrown/anthropics** — the correct writable repo for the
   Muse series (earlier target was a 403 mistake; Bear corrected it).
3. **Liam / @NikBearBrown identity** — channel `claude-liam`, watermark
   `@NikBearBrown`, "Muse, in for Bear. Thanks for watching." outro on every
   film.
4. **MetaMuse transcript as inspiration** — the ~3-hour MetaMuse Code
   Essentials course, condensed into `source/transcript-outline.md`; Film 9
   draws on §13 (Muse Code CLI).
5. **Series plan commission** — the 12-film plan in `SERIES-PLAN.md`; Film 9
   is "Muse Code, the Harness", teasing Film 10 "Memory, Skills, and
   Guardrails".
6. **"Do everything except render the audio and render the MP4s"** — Muse
   builds the complete package; Bear downloads and renders locally with
   Claude Code. Every film folder ships a filled, paste-ready
   `CLAUDE-CODE-PROMPT.md`.
7. **Standing order to build** — "keep going, don't wait for me, just make
   films"; push each film to GitHub immediately; the muse README tracks every
   film with a direct link to its Claude Code prompt.

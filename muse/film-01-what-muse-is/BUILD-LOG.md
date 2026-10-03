# BUILD-LOG.md — What Muse Is (Film 1)

## 2026-10-03 — series setup (earlier today)
- GitHub connected (`custom.github`); first write test hit the wrong repo
  (Humanitariansai/humanitarians-youtube-muse → 403). Bear corrected: the
  token is for nikbearbrown/anthropics. Verified `push: true`; probe file
  pushed and deleted.
- `git clone` of brutalist.art hangs from the VM; pulled the repo as a
  tarball via the API instead. Static QC checker runs.
- Created `muse/` in nikbearbrown/anthropics; pushed SERIES-PLAN.md (12-film
  plan), source docs, prompt template, pattern reference.

## 2026-10-03 — Film 1 build
- Wrote ACTS.md, SHOTLIST.md, FACTCHECK.md, SOURCES.md, PROMPTS.md by hand
  from the transcript outline + research brief.
- Delegated make_sheet.py + beat_sheet.json + scenes.py to a subagent with
  the full pattern spec.
- **Miscount caught:** my brief said "15 beats" but listed 16 rows
  (BIDEA, BDEFS, B01–B11, BVDT, BHTF, BOUT). 16 is inside the 13–22 envelope;
  kept 16, asserts updated. My error, logged.
- Subagent reported zero first-pass QC failures (binding rule applied from
  the start). I re-ran the full gate myself: py_compile clean, all 14 classes
  `1 clean · 0 warn · 0 error`. Verified independently — trust, but verify.
- Spot-checked narration: attributions intact ("the instructor's reading",
  "in Nik's experience"), numbers spoken as words, every on-screen word voiced.
- Filled CLAUDE-CODE-PROMPT.md from the template; wrote CLAUDE-CODE-RENDER.md.
- Pushed 12 files to `muse/film-01-what-muse-is/`; verified each via the
  Contents API.

## Next
- Bear downloads the folder; pastes CLAUDE-CODE-PROMPT.md into Claude Code
  on his Mac → audio + review cut + 4K master.
- Then Film 2 ("Your First Prompts").

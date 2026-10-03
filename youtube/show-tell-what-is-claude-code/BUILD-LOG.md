# BUILD-LOG — show-tell-what-is-claude-code

**What this is.** The dated record of the build, including what broke and how it was fixed.

## 2026-09-27
- Bear, 2026-09-27: "use the show-tell skill in Brutalist to make a film on this using the Liam persona 'What is Claude code?'" + a paste of claude.com/product/claude-code (saved, cleaned, as `SOURCE-PASTE.md`). Built per the show-tell SKILL.md and `../SHOW-TELL-BATCH.md` (its Batch 2 scratch rule), while another session built a different film. All scratch work stayed in `scratchpad/st-wicc/`, and every manim render had its own `--media_dir`. Worked example copied for shape: `show-tell-claude-on-an-issue/` (kit block, `ST`/`guard` midpoint guard with the 0.22 s margin, `state(k)` continuity, `done()` ending 0.05 s under the audio).
- Sources: the paste, plus the live docs fetched raw with curl (`overview.md`, `permission-modes.md`, both HTTP 200, in `sources/`). The permission-modes doc contradicts the page's auto-mode line (see below). No WebFetch summary was used. FACTCHECK: 56 rows, 1 CORRECTED; `factcheck_check.py` clean.
- Audio (Kokoro am_onyx), whisper-checked (faster-whisper small.en; medium.en for BIDEA and BHTF). "Ciao" is clean (small.en writes "Chao"/"Chow", medium.en "Ciao"). Re-voiced with `--only` (old takes in `_superseded/audio_v1/`):
  - B03: "the page's own example" was heard as "page zone example"; now "the example the page itself uses".
  - B10: "the phone app, and Slack" was heard as "the phone app in Slack"; now "The page adds the phone app. And in Slack, you can kick off a task."
  - B12: rewritten from the docs (below).
  - Homophones left alone: small.en writes "clod code" once in BHTF (medium.en hears "Claude Code") and "Nick Baer" in BOUT.
  - BOUT padded with a 1.0 s tail (unpadded copy in `_superseded/`), 3.92 s.
  - Total 221.63 s.
- **CORRECTED before any render:** the page's announcement says auto mode is "the default on Pro, Max, and Team plans". The live permission-modes doc says that from v2.1.283 it is the starting mode for interactive terminal and VS Code sessions, and only on those plans before that. B12 now describes manual mode ("stops and asks you before it edits files or runs commands") and auto mode ("a second model checks each action instead of you") from the docs, keeps the page's "work longer, while still catching risky commands" (attributed), and makes no "default" claim. The scene was redrawn to match: the barrier stops a command and asks the figure in manual mode; in auto mode commands pass unasked and a risky one is held.
- Stills, round 1 (480p15 at 50/97%):
  - B01: the edit page lost its grey lines at the end. The closing `Indicate(page)` brings the rectangle to the front over its same-z lines; it now indicates the whole page group.
  - B01: "reads" sat far from the lens; moved.
  - B05: the second coin was still fading at the end; the moves were tightened.
  - B06: "+9 −3" touched the coin; moved the coin and the label apart.
  - B12: the barrier arm floated above a detached base; redrawn as an arm in a dark sleeve.
  - Layout audit, B02 and B11: the "?" started on the agent block's edge ("label on a curve"); it now starts beside the block.
- Pre-audit from a scratch folder holding only `scenes.py`: Gate A clean 14/14. Layout audit (`--curve-strict`) clean 14/14.
- Local GATE T pre-check (1080p24 renders upscaled to 2160, `type_check.py` on a scratch reel copy) failed 3 beats at the midpoint:
  - B07 and B09: kraft lines drawn ON the pages inside the ink-outlined tray (the map lines, the import path) cut the pages' thin outlines loose from the tray, and GATE T §8.6b then read each page as a separate "label" stacked inside the tray blob. Lightening the lines was not enough. The fix: B07's map is now drawn BESIDE the tray (nodes and lines), and B09's import chain is a terracotta dot hopping page to page with nothing left drawn on the pages. This is a new trap for the skill's list.
  - B12: a kraft command slab parked over the dark terminal failed per-blob contrast. Commands now stop short of the terminal.
  - After the fixes, GATE T PASS locally.
- Local Gate V fill pre-check (25/50/75/99%): B04–B07, B10 and B12 measure 0.56–0.74 throughout and carry no sparse waiver. B00–B03, B08, B09, B11 and B13 (0.24–0.49 at some point) keep it.
- 4K `art run` (`_qc/run.v1.log`): Gate L clean, Gate A clean 14/14, Gate W clean 14/14, layout audit (Gate B) clean 14/14, Gate V 36 frames with 0 BLOCKER and 0 MAJOR. ffprobe: every `manim/<BID>.mp4` is 0.02–0.08 s under its audio, so nothing was centre-cut. Before the run, the `media/` folder left in the reel by the pre-audit layout runs was moved to `_superseded/media_preaudit/` (the stale-cache trap). Review-cut bookends read correctly: the writer's correction fires ("What is Claude Code, an agent you hand work to?"), BDEFS shows all four terms in full (the longest, "idempotency key", is 15 characters), BHTF shows the whole prompt and both checks, and BOUT reads "What Is Claude Code?".
- `art final` (`_qc/final.v1.log`): GATE T PASS (18 beats, 0 FAILs, `TYPECHECK.md`), build stamp `cut: master`, 18/18 filled. Bookend PASS (`runtime/scripts/bookend_check.py`). Gate F clean (`runtime/qc/factcheck_check.py`, 56 rows). The "SKIN LINT: COLD OPEN LAW" line on BIDEA is advisory and expected under `bookend_exempt`. `make_sheet.py` was not re-run after the final.
- Master late frames (90% of each beat, `_qc/master_late/`, sheet `_qc/contact_late.png`) read correctly. At 90%, a few beats are still landing their last motion on the last words (B03's second coin, B05's second coin, B08's PR card, B09's check, B12's risky command); each completes before its beat ends.
- Whisper of the master's first 16 s: "Chow, this is Liam in for Bear. It's easy to picture Claude Code as a smarter autocomplete, a tool that guesses your next line. Its product page describes something else. You hand it a whole task and it does the work while you steer. So what is Claude Code, an agent you hand work to? Four terms, an agent."
- No toolkit script was patched, and none needed a workaround. Nothing outside this reel folder and `scratchpad/st-wicc/` was written.
- **Master:** `exports/landscape/show-tell-what-is-claude-code.mp4`, 3840×2160, 24 fps, 221.92 s (3:42), sha256 be658f1402052e344e7f111b5d992226c35a823025823d41c6ab9562e14b9297, tail max_volume −91.0 dB. Not staged, not published.

# BUILD-LOG — cc-rewind-not-fix-forward

cc-explainer · Claude Code 101 · tier `02-plan-rewind-subagents`, film 04 · Liam, in for Bear · built 2026-09-09.

**Headless caveat (SKILL BUILD-SHOW LAW note).** The concept's true subject — the interactive `Esc-Esc` / `/rewind` keystrokes — is not filmable inside a headless `claude -p` session; there is no rewind command in headless. The film uses its headless equivalent: a fresh `--session-id` with a respecified ask. That substitution is stated on screen in B05 (CCPlainShell), narrated by Liam ("this is a headless session, so I do what rewind does"), and recorded here so no viewer thinks the terminal captured the rewind mechanic itself.

**The experiment.** Same ask — "Write a small Python module `todos.py` with two functions, plus tests" — under two paths: (1) fix-forward — one bare session followed by two `--resume` corrections (dataclass, then a `keep` predicate) → 14 turns, 97.9 s, $0.888, end state `remove_completed(todos, keep=None)`; the function name lies about what it does and the tests document the drift on line 43; (2) rewind (headless equivalent) — a fresh `--session-id` with the respecified ask → 5 turns, 26.6 s, $0.359, end state `filter_todos(keep)`; name matches behaviour. Everything on screen traces to `evidence/run-{bare,fixforward,fixforward2,rewind}.jsonl` and the final files.

**Adaptations from the source concept.** The source concept's mutation-splice anecdote (a `deleteApplication` that used splice) is not reused — the real headless bare run produced clean immutable code by default. The film pivots to a plausible-but-real fix-forward smell: two narrow corrections that leave a misnamed function and a lying test file. The andon-cord metaphor, the "correction joins the misunderstanding" idea, and the film title are kept.

**Compile.** Two passes.

- Pass 1 — first `art run`: all 15 beats rendered clean (Gate V 0/0/0, GATE T PASS, GATE BOOKEND PASS, GATE MASTER PASS, GATE LOUDNESS PASS); the concat's slate mp4 truncated (moov atom missing) so I re-triggered the compile.
- Pass 2 — `art run` after tightening the CCHumanLedger row `"flag stranded contracts unprompted"` (34 chars — the kit truncated it to `unpromp…`) to `"call out stranded contracts"` (26). The edit was made via a temp-dir regen and a targeted prop merge, per SKILL: `author_sheet.py` was NOT re-run inside the reel (that would wipe audio and render stamps). Only B09 re-rendered; every other beat used its cached hash.
- Third pass — `art final`: clean master written, TYPECHECK.md refreshed, all gates PASS. Master 324.0 s (5:24), 3840×2160 @ 24 fps h264 yuv420p, -24.25 LUFS / -2.80 dBTP. Frame-checked B00 (drift killshot), B04 (verify), B07 (compare), B08 (Boondoggle Score), B09 (ledger — post-fix), BVDT (verdict 6-line 3-page pagination), BHTF (composer): all clean, no clipping, ledger no longer truncates.

**Advisory warnings (kept).**

- `SKIN LINT` on B00: `palette=claude but the cold open is 'CCSession'` — this is the cc-explainer TERMINAL-FIRST LAW in action; the film opens on the terminal by design, and GATE BOOKEND explicitly permits it (`metadata.skill: "cc-explainer"` unlocks the override). Not a failure.
- `motion histogram`: `type` at 66% (over 40% cap). The film is 10 CCSession/CCPlainShell type-beats out of 15 by design — the loop and shell steps are the subject. Not fixed; would require converting real terminal beats to a different motion, which would betray REAL-SESSION LAW.

**Not published.** Master stays in this folder. TOPOST only via `post`, only on ask.

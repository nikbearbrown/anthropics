# BUILD-LOG — cc-conducting-not-prompting

cc-explainer · Claude Code 101 · tier `00-what-it-is`, "Conducting, Not Prompting: The Gru/Minion Split" · Liam, in for Bear · built 2026-09-09.

**The experiment.** One sentence — "Write format_price(cents: int) -> str in format_price.py and add unittest tests in test_format_price.py." — under two conditions, each a fresh headless `claude -p` run against `--allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls|cat|python3|git|wc)"` with `--strict-mcp-config`.

- **Bare** (session `89136c5c-…`, 25.8 s, turns=5, $0.339). Empty folder. Claude picked dollars, thousands separator, `-$` on negatives, `TypeError` on non-ints including `bool`; 7 lines of implementation, 46 lines of tests, 10 test methods, all green.
- **Conducting** (session `30f069af-…`, 42.0 s, turns=7, $0.385). Same folder plus `SPEC.md` (11 lines — five cases, four rules). Ask ends "Read SPEC.md first." Claude picked EUR, no separator, `ValueError` on negatives; 4 lines of implementation, 25 lines of tests, 5 test methods — one per SPEC case, all green.

Verified with `spec_check.py` (the SPEC as a script): bare fails all five cases (`$12.99` vs `12.99 EUR`, `-$0.50` instead of raising, etc.); conducting PASS. Both suites are green — only one is green about the right thing. That IS the film.

**Compile.** One pass: Gate V 0/0/0, GATE T PASS, GATE SHARPNESS PASS, GATE BOOKEND PASS, GATE MASTER PASS, GATE LOUDNESS PASS → `final`. Master 218.9 s (3:39), 3840×2160, h264, `-24.26 LUFS`. Frame reads (B01 bare-VERIFY, B04 conducting-VERIFY, B05 CCBoondoggleScore, B06 CCHumanLedger) clean — every string within budget, no overprint, no ellipsizing. Motion histogram warned `type` at 58% (advisory; the film IS terminal-first, so type dominates by design). Skin-lint flagged the CCSession cold open against the generic COLD OPEN LAW; overridden by GATE BOOKEND, which knows `cc-explainer` allows CC surfaces.

**What the sessions gave the film.**
1. A visceral, receipt-backed demonstration of the film's claim: same one sentence, same model, radically different code. Every number and word on screen traces to `SESSION.md` or `evidence/`.
2. A five-for-five FAIL vs PASS on `spec_check.py` — the falsifiable receipt behind the verdict.
3. The dangerous middle (step 3 of the Boondoggle Score) is Liam reading the bare file and noticing "green suite, wrong thing" — a moment the CCBoondoggleScore rings in terracotta.

**Not published.** TOPOST only via `post`, only on ask. Master stays in this reel folder.

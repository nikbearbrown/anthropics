# FACTCHECK — cc-cwc-how-we-claude-code

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (three real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the three runs' stream-json, the five generated HTML pages (`workshop.bare.html`, `workshop.three.html`, `mock1–4.html`), the brief and fixture Liam authored, and the plain-shell verifies against them. Claude's sentences are quoted as verbatim spans. The three-phase framing (Brainstorm → Design → Verify) is the concept as it appears in the source CWC workshop; the workshop itself is not shown, and no unnamed Anthropic engineer is quoted.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, cover | The ask, verbatim | PASS | `evidence/ask.txt` | — |
| 2 | B00 | Two Reads, then "I'll build a clean single-file landing page with sensible placeholders where you'd normally drop in specifics (date, time, venue, signup link)."; Write | PASS | `run-bare.jsonl` (the leading `pwd && ls -la` is omitted for height; the sentence is display-broken across four blocks) | — |
| 3 | B00, B01 | "One hundred and thirty lines" | PASS | `wc -l workshop.bare.html` → 130 | — |
| 4 | B00 | "my email address, pulled from context" (bare page uses `bear@bearbrown.co`) | PASS | `grep -o "mailto:[^\"]*" workshop.bare.html` → `mailto:bear@bearbrown.co` — the value came from the user's git config in Claude's context, not from any prompt | — |
| 5 | B00 | "Coffee provided. Questions welcome." | PASS | `workshop.bare.html:126` — `Hosted by Bear. Coffee provided. Questions welcome.` | — |
| 6 | B01 | `wc -l` → 130; `grep -c welcome` → 1; the mailto; the `Coffee` / `10:00` count | PASS | all four commands run in `SESSION.md` VERIFY | — |
| 7 | B02 | brief.md is 7 lines, "the seven-line brief" | PASS | `wc -l brief.md` → 7 (six bullets plus a heading and a byline; the shell shows the six bullets); "seven" chosen because 7 is what `wc -l` prints | — |
| 8 | B02 | "not developers", "version control is a habit, not a system to conquer", "screenshots, stock photos, enthusiasm words" | PASS | verbatim from `evidence/brief.md` | — |
| 9 | B03 | The diverge ask; four Writes | PASS | `run-design.jsonl` (the ask is broken across two prompt blocks for width; Claude's summary sentence is display-broken across two text blocks) | — |
| 10 | B03 | "modern SaaS, terminal, hand-drawn zine, editorial magazine" | PASS | Claude's own summary in `run-design.jsonl` | — |
| 11 | B04 | Line counts 199 / 201 / 239 / 270 | PASS | `wc -l evidence/mock*.html` — matches | — |
| 12 | B04 | The body-font table: mock1 sans, mock2 mono, mock3 mixed, mock4 serif | PASS | `grep 'body{font:' evidence/mock*.html` — each mock's body rule shown, values verbatim | — |
| 13 | B05 | fixture.py is 36 lines; the seven failure lines shown | PASS | `wc -l fixture.py` → 36; the `fail(...)` calls quoted verbatim from `evidence/fixture.py` (one line display-truncated) | — |
| 14 | B06 | Reads (brief.md, mock2, fixture.py); Write; `python3 fixture.py` → `FAIL: no monospace font-family`; Edit; PASS at 153 lines | PASS | `run-verify.jsonl` — every step verbatim in stream order; the `task.txt` and `ls` calls before the Reads are omitted for height | — |
| 15 | B06, B07 | "153 lines" | PASS | `wc -l workshop.three.html` → 153 | — |
| 16 | B07 | Two inputs (name, goal), neither an email; `font-family:ui-monospace,SFMono-Regular,…`; `welcome`/`amazing` count → 0 | PASS | `SESSION.md` VERIFY commands | — |
| 17 | B08 | Seven steps of the Boondoggle Score; step 3 is the dangerous middle | PASS | maps to `SESSION.md`; capacities per the reference (`skills/make/cc-explainer/SKILL.md`, `reference/three-beats.md`) | — |
| 18 | B09 | Ledger rows — CAN and SHOULD map to what Claude actually did in `run-verify` | PASS | `run-verify.jsonl` — Claude ran the fixture (`Bash python3 fixture.py`), read the failure, and edited | — |
| 19 | BVDT | Verdict lines; "130 lines", "7 lines of brief.md", "4 divergent mockups", "36 lines of fixture.py", "passed at 153" | PASS | rows 3, 7, 11, 13, 15 above | — |
| 20 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
| 21 | all | Model/version strings; costs; session IDs | EXEMPT | not shown or spoken (recorded in SESSION.md only) | — |

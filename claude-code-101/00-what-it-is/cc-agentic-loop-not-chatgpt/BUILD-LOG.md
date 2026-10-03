# BUILD-LOG — cc-agentic-loop-not-chatgpt

cc-explainer · Claude Code 101 · tier `00-what-it-is`, film 02 · Liam, in for Bear · built 2026-09-09.

**The experiment.** One folder — a fictional 4th-grade class page (`class-website/`: README, index.html, style.css) — the same one-sentence ask ("add a contact form to my class website") put in front of Claude Code twice, on the same seed commit. Naive: `--permission-mode acceptEdits`, full write tools; 3 Reads, `AskUserQuestion` dismissed under `< /dev/null`, then 2 Edits — an email input and `action="mailto:REPLACE-WITH-YOUR-EMAIL@example.com"`, caveats afterward (52.5s, 8 turns, $0.343). Calibrate: same folder reset, Write/Edit fenced out, prompt is the five questions with `Do not change any files`; 3 Reads, 0 edits, Claude names "a contact form is a bigger change than it looks", flags the site's `(555) 010-1234` phone as a **reserved fictional prefix**, and lists what it doesn't know (47.2s, 5 turns, $0.217). Same wall clock, same three Reads. Different receipt on disk.

**Authoring.** Modeled the sheet on `cc-three-files/author_sheet.py` — same helpers (`B`, `R`, `writer`, `session`), same metadata frame, same asserts. 14 beats: B00 cold open · BIDEA (`chatbot` → `loop`) · BDEFS (5 terms) · B01/B02/B03 (chatbot cycle: gather / act / VERIFY) · B04/B05/B06 (calibrate cycle: ask / answer / VERIFY) · B07 CONDUCT · B08 HUMAN · BVDT/BHTF/BOUT. Concept film — `metadata.build` unset; BFLOW/BSHOW skipped and declared in `CHECKS-REPORT.md`. `author_sheet.py` printed `14 beats — est 361s`, no budget warnings.

**FACTCHECK.** `factcheck_check.py` → `clean` (23 rows, 11 beats covered, uncovered 0).

**Compile.** One pass. All 14 beats rendered on the first call. Gate roster on the first `art run`: GATE-F / GATE-L / GATE-BANNED-CARD / GATE-SWEEP-WARN / GATE-G / GATE-V (0/0/0) / GATE-T PASS / GATE-SHARPNESS PASS (median LV 698.6) / GATE-BOOKEND PASS / GATE-AUDIO PASS (-23.7 dB) / GATE-MASTER PASS (3840×2160 @ 24fps, h264, 293.6s) / GATE-LOUDNESS PASS (-24.17 LUFS, tp -2.83 dBTP) / GATE-RECEIPTS PASS. Two soft warnings: (i) `SKIN LINT: B00 cold open is CCSession` — the `cc-explainer` skill override permits it (GATE BOOKEND PASSED); (ii) motion histogram `type: 7/14 (50%)` over the 40% cap — a body of seven consecutive `CCSession` blocks is what a terminal-first film looks like. One GATE T advisory: `§8.10 [BVDT] narration recites the card (0.83)` — the verdict recap is *intended* to restate; SKILL requires 4 lines, and we have 4. Left as-is.

**Frame QC.** Grabbed 90 % frames on the dense beats (B02, B03, B05, B07, B08, BVDT, BHTF) to `_qc/frames90/`. All read clean: no clipping under the shell footer, no overprint on CCSession stacks, `CCBoondoggleScore` rings step 2 as the dangerous middle with a clean capacities tally, `CCHumanLedger` balances MUST/SHOULD in two columns without ellipsis, `ClaudeVerdictArtifact` paginates 2 / 2 with the `FALSIFIABLE:` bullet whole. `ClaudeComposerAsk` (BHTF) visually truncates the prompt at "…would you change if I asked" — that's the component's own overflow; Liam reads the full prompt in the narration.

**`art final`.** Ran clean. Wrote `cc-agentic-loop-not-chatgpt.mp4` (3840×2160, h264+aac, 293.6 s / 4:53).

**Not published.** TOPOST only via `post`, only on ask.

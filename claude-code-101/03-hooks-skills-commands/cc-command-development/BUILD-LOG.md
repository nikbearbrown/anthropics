# BUILD-LOG — cc-command-development

cc-explainer · Claude Code 101 · tier `03-hooks-skills-commands` · Liam, in for Bear · built 2026-09-10.

**The experiment.** Same scratch repo (`scratch/`, a five-function `inventory.py` with planted bugs — SQL injection at line 14, mutable default at line 6, off-by-one at line 35, bare `except` at line 30, shell injection at line 39, plus a float-truncation surprise at line 22). Two `.claude/commands/*.md` slash commands, invoked with `claude -p "/review-v1"` and `claude -p "/review-v2"`. v1 is three sentences of the "message-to-user" pattern the source SKILL warns against. v2 is frontmatter (description, allowed-tools, argument-hint) plus imperative body with an explicit output format.

**What the runs gave the film.** Modern Claude Code (2.1.150, opus 4.7) is smart enough to *review the code either way* — the difference is not "does Claude do the work" but "does the output take the shape you asked for." v1 produced 92 lines of Claude's default review essay (three severity emoji, twelve code blocks, a summary table, a closing question — six findings including one Claude added on its own initiative). v2 produced exactly six lines — five rows in `path:line — SEV — description`, a blank line, then `5 issues found.` — nothing added, nothing decorated. That is the film's argument: the slash command is not a shortcut, it is the spec for the output shape. The float-truncation finding that v1 volunteered but v2 didn't is the receipt: v2 stayed inside the four categories the command listed.

**Concept film, not build film.** `metadata.build` is unset. BFLOW and BSHOW skipped per CHECKS-REPORT ("BUILD-SHOW: not armed — concept film"). The subject is the shape of the command file itself; the `CCDiff` in B02 is the pivot between the two runs, not the show-the-output slot.

**Compile.** One pass. Gate V 0/0/0, GATE T PASS (§8.10 BVDT 0.35 OK), GATE SHARPNESS PASS (median LV=543.3), GATE BOOKEND PASS, GATE AUDIO PASS (-23.8 dB), GATE MASTER PASS (3840×2160, 24 fps, yuv420p, h264, 206.6s), GATE LOUDNESS PASS (-24.27 LUFS, tp -2.91 dBTP), GATE RECEIPTS PASS. `art run` → `art final` produced `cc-command-development.mp4` (3:26.6, 3840×2160). SKIN LINT warned that a CCSession cold open in the `claude` palette is unusual — this is the cc-explainer skill's explicit override (see SKILL.md → GATE BOOKEND: "with `metadata.skill: 'cc-explainer'` the cold open may be a CC surface"); non-blocking, kept.

**Frame reads.** Sampled B00, B01, B02, B03, B05, B06, BVDT at ~85 % of their beat durations. Every dense composition landed clean:
- B00 `CCSession` — the prompt lands, the tool-tree check-marks resolve, the essay opens on `## 🔴 CRITICAL — Security · 1. SQL injection (line 14)` and elides to `… 82 more lines, a table, …` before the closing question.
- B02 `CCDiff` — `Update(.claude/commands/review.md)` with `+11 added · 3 removed`, red stripes over the three prose lines, green stripes over frontmatter + imperative body + format spec.
- B03 `CCSession` — the five rows in the spec's format followed by `5 issues found.`, no other text; contrast against B00 is immediate.
- B05 `CCBoondoggleScore` — six steps, DANGEROUS MIDDLE ring on step 2, capacity tally `PA 1 · PF 2 · TO 0 · IJ 1 · EI 0` at the bottom.
- B06 `CCHumanLedger` — AI column fills first (CAN/SHOULD ×4), HUMAN column lands second (MUST/SHOULD ×4), closing "The spec is the file. That's the whole trick." reads clean.
- BVDT `ClaudeVerdictArtifact` — 2/2 pagination confirms four lines total; FALSIFIABLE lands on the last line as prescribed.

**Not published.** TOPOST only via `post`, only on ask. Master stays in this folder.

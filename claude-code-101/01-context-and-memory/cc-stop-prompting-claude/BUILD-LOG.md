# BUILD-LOG — cc-stop-prompting-claude

cc-explainer · Claude Code 101 · tier `01-context-and-memory`, film 04 · Liam, in for Bear · built 2026-09-09.

**The experiment.** Two writing tasks — a class note about a rescheduled guest lecture, and a reply to a student who missed a quiz — each run twice as fresh headless `claude -p` sessions. In `bare/` (no CLAUDE.md), Bear typed the full voice preamble + the task; in `files/`, one CLAUDE.md (26 lines, 1256 bytes) sat in the folder and Bear typed only the task. Same person, same voice, same model. Scratch lived at `/tmp/cc-stop-scratch/` (outside the books tree) so no ancestor `books/CLAUDE.md` auto-loaded and contaminated the bare condition; evidence copied into `evidence/`.

**What the runs gave the film.** Both conditions pass the voice checker (`check.py`). The receipt is bytes typed to Claude per session — bare 975 / 999, files 146 / 171 → **6.2× less typing** in files, and it stays 6.2× as the file is amortized. And a substance receipt: bare-A **invented a URL** ("Same time, same link") in a note about weather — the bare prompt literally said "Do not invent URLs" but the rule got lost in a 975-byte paragraph. Files-A obeyed the same rule cleanly because it lived in the file's own line, not buried in a preamble. The `cache_creation` delta between files-A and bare-A is +311 tokens — exactly CLAUDE.md's size — mechanical proof the file was in context, not the message.

**Compile.** One pass: Gate V 0/0/0, GATE T PASS (BVDT §8.10 recite-ratio 0.85 advisory only), GATE BOOKEND PASS, GATE SHARPNESS PASS, GATE MASTER PASS (3840×2160, 24fps, h264), GATE LOUDNESS PASS (−24.27 LUFS, TP −2.87 dBTP) → `final`. Master **239.2 s (3:59), 3840×2160**. Frame spot-checks (`_qc/frames/*-90.jpg`) on B00, B01, B04, B06, B07, BVDT — all readable, no clipping, boondoggle step 3 rung correctly at the "same link" audit, human ledger's two columns paired within budget, BVDT paginates 2/2 with the falsifiable line last.

**Soft warnings, non-blocking.**
- SKIN LINT: `B00 palette=claude but cold open is CCSession — COLD OPEN LAW wants ClaudeComposerAsk`. Legacy check from ai-explainer; cc-explainer's `SKILL.md` explicitly allows `CCSession` cold opens for the TERMINAL-FIRST law. GATE BOOKEND is the skill-aware check and passes. Matches exemplar `cc-three-files`.
- Motion histogram `type:7 (53%)` over 40% pantry cap — 13-beat cc-explainers concentrate `type` on the CCSession/CCPlainShell beats by design; matches exemplar.
- TYPECHECK §8.10 BVDT recite-ratio 0.85 — the verdict lines summarise numbers Liam also speaks; the falsifiable line is unique. Advisory; matches exemplar.

**Not published.** Master stays here (`cc-stop-prompting-claude.mp4`); TOPOST only via `post`, only on ask.

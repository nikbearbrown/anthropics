# BUILD-LOG — cc-claude-101

cc-explainer · Claude Code 101 · tier `00-what-it-is`, film 04 · Liam, in for Bear · built 2026-09-09.

## What the session gave the film

**The experiment.** One folder (`scratch/`), one file (`notes.md`, 11 lines — a stand-up jot), four fresh headless `claude -p` runs, `--strict-mcp-config`, `--allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls|cat|python3|git|wc)"`. The four conditions were ordered so the arc reads as the film argues:

1. **Concrete (run-concrete):** "Read notes.md and write actions.md as a checklist of every action item that has a specific person's name attached, one per line as `- [ ] <who>: <what> (<when>)`." → one Read, one Write, four lines, every one owned by a named person. `wc` = 4; `grep -c '^- \[ \]'` = 4; `grep -o 'Priya\|Rafael' | uniq -c` = 2/2.
2. **Vague, no file (run-vague):** "What should I focus on this week?" → two errored reads (`ls memory/` blocked; `MEMORY.md` nonexistent), then the model handed the pick back with three concrete options. **No artifact.** The model refused to guess when there was no ground.
3. **Middle — vague, with file (run-middle):** "Read notes.md and tell me if I'm doing a good job managing this project." → Read, then opinion. It named Priya, Rafael, the reminder-emails question, the p95 flag — sounds grounded, is opinion. **No artifact.** The dangerous middle.
4. **Correction (run-correction):** "Read notes.md and extract every first-person commitment, one per line, to commitments.txt." → Read, Write, three lines. Every line begins with "I", every line traces to a file line (Claude split line 10 into two distinct actions and said so).

**The idea the runs gave the film.** The concept card wanted to say Claude is a menu — three surfaces, three tiers, three vocab, five rules, Skills + Projects. That menu is technically accurate and useless to a beginner. The useful oversimplification is that **Claude is one function; the ask is the whole difference.** Same model, same file — the difference between "opinion that sounds grounded" and "three checkable lines" was the shape of the ask.

Concept file (`claude-cowork--claude-liam-claude-101/beat_sheet.json`): title and framing preserved; card copy (surfaces / tiers / vocab / five rules / expert-mode-unlock) intentionally not reused per skill law — those bullets were concept-only and never checked against a session.

## Compile passes

- **Pass 1 (author + audio + factcheck):** `author_sheet.py` writes 13 beats, ~305s estimated; two ledger-row warnings fixed at the source ("decide what a right answer means" 32 chars, "audit grounded-sounding opinions" 32 chars). `generate_audio_kokoro.py` → 13 mp3s, real durations sum to ~239s. `factcheck_check.py` → `clean` (23 rows, 12 beats covered, 1 claim-bearing).
- **Pass 2 (art run):** the first `art run` was double-started (a foreground call fired while a background one was still going — the second correctly refused with "render lock exists"; the background finished all 13 remotion renders in ~10 min). A follow-up `art run` picked up all 13 renders as filled-already and did the compile step end-to-end: GATE-V 0/0/0, GATE T PASS (`§8.10 BVDT: 0.54`, everything else SKIP or PASS), GATE-SHARPNESS PASS (median LV=686.0), GATE-BOOKEND PASS, GATE-AUDIO PASS (mean -23.6 dB), GATE-MASTER PASS (3840×2160, 24 fps, h264, 238.5 s), GATE-LOUDNESS PASS (-24.11 LUFS, tp=-2.87 dBTP). Two non-blocking warnings noted and accepted: (a) SKIN LINT wants `ClaudeComposerAsk` for the cold open — the skill explicitly permits `CCSession` as the cold-open surface when `metadata.skill = cc-explainer` (per `SKILL.md` GATE BOOKEND override); (b) motion histogram: 8/13 beats carry `type` — natural for a terminal-first cc-explainer where every session block types; the histogram cap is written for pantry-heavy explainers, not this genre.
- **Pass 3 (art final):** clean master `cc-claude-101.mp4` written (16 MB, 238.5 s = 3:58, 3840×2160). Frame reads at ~90% on B00 / B02 / B03 / B06 / B07 / BVDT: clean; no clipping, no overprint. The `CCBoondoggleScore` step lines and `CCHumanLedger` rows all fit their budgets (asserted at authoring, verified in the frames); B06's `dangerousMiddle: 4` ring lands correctly on the "opining against a file" step; BVDT's 6-line artifact paginates 3/3 as designed.

## What was corrected (author-time, before rendering)

- Two `CCHumanLedger` MUST rows over 34 chars → shortened at the source ("decide what right answer looks like" → "decide what a right answer means"; "audit an opinion that sounds grounded" → "audit grounded-sounding opinions").
- `mascot: "off"` on every `CCSession` beat (7 of them) — the block stacks reach the bottom of the shell; the mascot at the last row would overprint (documented kit gotcha).
- Prompts on B00 and B04 display-condensed vs the JSONL to fit the shell without wrapping past legibility. FACTCHECK.md rows 1 and 14 mark these CORRECTED with the original quoted.
- BVDT: 6 artifact lines (paginates 3+3), not the forbidden 5.
- BOUT: `subline: ""` per OUTRO-LOCK.
- `token`/status strings: none used (avoiding the `↓ ↓` double-arrow gotcha).

## Not published

Master stays in `/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-code-101/00-what-it-is/cc-claude-101/`. Nothing in `books/youtube/TOPOST/`. Nothing on YouTube. Bear decides `post` / publish.

# BUILD-LOG — cc-claude-skills--claude-liam-skill-creator

cc-explainer · Claude Code 101 · tier `03-hooks-skills-commands` · Liam, in for Bear · built 2026-09-10.

**The experiment.** The `skill-creator` skill's description-optimizer inner loop, done by hand at n = 6 so a viewer can see what the tool does at n = 20 × 3 × 5. Two SKILL.md files for a `meeting-actions` skill, identical body, differing only in the `description:` line: vague (nine words — "Helper for meeting notes.") vs pushy (63 words — every synonym the skill-creator's own doctrine recommends). Three asks per description in fresh `/tmp/sc-<skill>-<ask>/` dirs: A1 obvious ("Extract action items from notes.txt."), A2 paraphrase ("I have a meeting write-up in notes.txt — pull out who agreed to do what."), A3 near-miss negative ("Summarize notes.txt for someone who missed the meeting."). Trigger tally: **vague 1·1·0, pushy 1·1·0 — 4/4 both descriptions.** The pushy version's 54 extra words earned zero extra fires; the vague version's nine words did not over-fire on the summary.

**What the session gave the film.** The router is semantic, not literal — same asks resolved the same way under both wordings; and the router does not over-trigger — "summarize" and "action items" share a folder and a file, and it still told them apart. The skill-creator's contribution is the loop that lets you notice these things, not the doctrine of what to write. The misconception the reel exists to fix: a skill's description is *crafted* → it is *measured*.

**Compile.** One pass, no rebuilds:

- GATE V: 0/0/0 (BLOCKER=0 STRUCTURAL=0 COSMETIC=0), 26 frames sampled.
- GATE T: PASS.
- GATE SHARPNESS: PASS, median LV=657.7.
- GATE BOOKEND: PASS — four bookends correct (cold open `CCSession` accepted for `cc-explainer` per SKILL.md § GATE BOOKEND).
- GATE AUDIO: PASS, mean_volume −23.6 dB.
- GATE LOUDNESS: PASS, −24.14 LUFS, tp=−2.94 dBTP.
- GATE MASTER: PASS, 3840×2160 24fps yuv420p h264, 244.2 s.
- All other roster gates (F, L, BANNED-CARD, SWEEP-WARN, G, RECEIPTS): PASS.
- SKIN LINT warning: "B00: palette=claude but the cold open is 'CCSession' — COLD OPEN LAW wants ClaudeComposerAsk". This is expected for cc-explainer: TERMINAL-FIRST LAW inverts the illustration default; the SKILL.md's GATE BOOKEND explicitly allows `CCSession` cold opens with `metadata.skill: "cc-explainer"`. No action.
- Motion warning: type carries 7/13 beats (53%). Six are `CCSession`/`CCPlainShell` beats whose natural motion IS typing (product string), and one is BIDEA (`BrutalistHesitantWriter` typing THE IDEA). Converting them would break the interface the film is *about*. No action.

**Frame reads.** B00 session stack: prompt + Skill + Read + text triplet + Write, all inside the shell — no wrap, no overprint. B04 negative-ask session: prompt truncates with `…` (kit-native), 5-line prose reply lands clean, no fake Skill event. B05 plain-shell tally: all six run rows visible, `trigger-tally.txt` under, no clipping. B06 Boondoggle Score: 5 steps + capacity tally (PA 1 · PF 2 · TO 0 · IJ 1 · EI 0), dangerous middle rings step 4. B07 Human Ledger: 4×4 rows, closing "The Skill Creator's gift is the loop, not the wording." legible. BVDT: paginates 3/3 with FALSIFIABLE last (six lines, allowed 4 or 6).

**Master.** `cc-claude-skills--claude-liam-skill-creator.mp4` — 3840×2160, 24 fps, yuv420p, h264, 244.181 s (4:04). Clean cut, no beat labels. Slate copy also on disk (`-slate.mp4`) for the review sheet.

**Not published.** TOPOST only via `post`, only on ask. Master stays in this reel folder.

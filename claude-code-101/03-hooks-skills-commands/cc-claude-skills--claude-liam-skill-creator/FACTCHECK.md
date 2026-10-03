# FACTCHECK — cc-claude-skills--claude-liam-skill-creator

Status: PASS — checked 2026-09-10 by the build session against `SESSION.md` (six real fresh headless runs) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the six runs' stream-json, the two SKILL.md files, `notes.txt`, `check_actions.py`, and the four `actions.*.md` files in `evidence/`. Claude's sentences shown in the CCSession blocks are paraphrases of what each run produced, kept within the ≤ 44-char text-block budget and split at clause boundaries; the tool events (Skill / Read / Write) are verbatim. Liam's checks were run in a plain shell on the evidence folder and are shown as bang commands inside the session. The source concept's framing (the description as the router's decision surface; the eval loop as the tool that separates guessing from measuring) is kept; no product model / price / version numbers are spoken.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | The ask, verbatim: "Extract action items from notes.txt." | PASS | `evidence/ask` implicit in `run-vague-a1.jsonl` user turn (see `evidence/notes.txt` context) | — |
| 2 | B00 | The description is "Helper for meeting notes." (nine words characterisation) | PASS | `evidence/SKILL-vague.md` line 3, verbatim | — |
| 3 | B00 | Skill(meeting-actions) fires without `/skill` being typed | PASS | `run-vague-a1.jsonl` contains one `"name":"Skill"` event; no user turn typed `/skill` | — |
| 4 | B00 | Read notes.txt, then Write actions.md, four rows | PASS | `run-vague-a1.jsonl` tool events + `evidence/actions.vague-a1.md` (4 lines, checked by `wc -l`) | — |
| 5 | B01 | `grep -c '"name":"Skill"' run-vague-a1.jsonl` → 1 | PASS | verified 2026-09-10, `evidence/` | — |
| 6 | B01 | `wc -l actions.vague-a1.md` → 4 | PASS | verified 2026-09-10 | — |
| 7 | B01 | `python3 check_actions.py actions.vague-a1.md` → PASS, 4 actions, owner/task/date | PASS | checker source in `evidence/check_actions.py`; last-line display-elided at 44 chars | — |
| 8 | B02 | `wc -l SKILL-vague.md SKILL-pushy.md` → 5 / 9 | PASS | verified 2026-09-10, `evidence/` | — |
| 9 | B02 | Vague description first three lines (`---` / `name: meeting-actions` / `description: Helper for meeting notes.`) | PASS | `evidence/SKILL-vague.md` lines 1–3, verbatim | — |
| 10 | B02 | Pushy description word count → 63 | PASS | `wc -w` on line 3 of `evidence/SKILL-pushy.md` | — |
| 11 | B03 | Pushy run: one Skill event, Read + Write, four rows | PASS | `run-pushy-a1.jsonl` + `evidence/actions.pushy-a1.md` (4 lines); wording is paraphrase to fit 44-char text blocks | — |
| 12 | B03 | "fifty-four extra words" | PASS | 63 − 9 = 54 | — |
| 13 | B04 | Negative ask verbatim: "Summarize notes.txt for someone who missed the meeting." | PASS | `SESSION.md` A3 row | — |
| 14 | B04 | A3 runs contain zero Skill events under both descriptions | PASS | `grep -c` on `run-vague-a3.jsonl` and `run-pushy-a3.jsonl` → 0 | — |
| 15 | B04 | A3's answer is a prose summary paragraph, no actions.md | PASS | `run-*-a3.jsonl` shows Read notes.txt then a text reply, no Write; no `actions.md` produced (only four actions.*.md in `evidence/`, all from A1/A2 cells) | — |
| 16 | B05 | Six-cell tally: vague 1·1·0, pushy 1·1·0 | PASS | `grep -c '"name":"Skill"' run-*.jsonl` output shown verbatim; `trigger-tally.txt` presented in the same beat | — |
| 17 | B05 | "4 out of 4 both rows" (positives 2/2, negatives 0/1 each) | PASS | tally arithmetic, 2+0+2+0 = 4 correct calls per description | — |
| 18 | B06 | Boondoggle Score: five steps, human PF/PF/PA/IJ, one Claude step (the six runs) | PASS | maps to `SESSION.md` (design → runs → tally read → interpretation) | — |
| 19 | B07 | Ledger rows | PASS | drawn from what actually happened in the six cells; no invented steps | — |
| 20 | BVDT | Verdict lines, including "gift is the loop, not the wording" | PASS | derived from the tally + `SESSION.md` finding | — |
| 21 | BHTF | Viewer's prompt (the six-cell tally instruction) | EXEMPT | instruction | — |
| 22 | all | Model / version strings; dates on screen | EXEMPT | none shown or spoken | — |
| 23 | metadata | Per-run costs ($0.107–$0.152) | EXEMPT | recorded in SESSION.md, not spoken | — |

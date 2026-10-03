# FACTCHECK — cc-claude-agent-skills--claude-skills-progressive-disclosure

Status: PASS — checked 2026-09-10 by the build session against `SESSION.md` (three real fresh headless `claude -p` runs, Claude Code 2.1.150) and `evidence/`.

**Verification boundary.** Every number and sentence on screen comes from the three runs' stream-json, the three `summary.*.md` files, and the skill folder captured in `evidence/skills/`. Liam's checks are run in a plain shell in `evidence/` and shown as bang commands inside the session. Claude's sentences are verbatim spans. Word counts are `wc -w` on the files as captured.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B04 | The Run B ask, verbatim | PASS | `evidence/ask.b.txt` and `run-b-skill.jsonl` first user message | — |
| 2 | B00, B04 | `Skill(exec-summary)` fires; then Read article.md; then Write summary.md | PASS | `run-b-skill.jsonl` tool_use sequence: Skill · Read · Write | — |
| 3 | B00 | "a hundred and fifty words, on demand" | PASS | `wc -w evidence/skills/exec-summary/SKILL.md` → 150 | — |
| 4 | BIDEA | The idea text, and the one corrected word "resident" → "described" | PASS | authored; the point the film exists to fix | — |
| 5 | BDEFS | The five terms and their high-level definitions | PASS | authored for a chat-window audience; every term used in the film below | — |
| 6 | B01 | `wc -l` on SKILL.md → 30; on references/house-style.md → 35; on references/length.md → 24 | PASS | `wc -l evidence/skills/exec-summary/SKILL.md` and `references/*.md` | — |
| 7 | B01 | The frontmatter's `description:` line, verbatim | PASS | `head -3 evidence/skills/exec-summary/SKILL.md` (display-truncated in B01 from "Summarize a document in the house executive-summary style." to "Summarize in the house exec-summary style." to fit the 60-char shell floor; the frontmatter is verbatim in Liam's plain-shell head, and B04's narration cites the router's real 8-word gate as measured) | CORRECTED | display-elision noted in row; the on-disk description is authoritative |
| 8 | B01 | `wc -w` → 150 / 195 / 105 words (SKILL.md, house-style.md, length.md) | PASS | `wc -w evidence/skills/exec-summary/SKILL.md references/*.md` | — |
| 9 | B02 | The Run A ask, verbatim; Read article.md; Write summary.md; single `#` heading | PASS | `evidence/ask.a.txt`; `run-a-bare.jsonl` tool sequence; `grep '^## ' evidence/summary.a.md` → empty | — |
| 10 | B03 | `grep -c '"name":"Skill"' run-a-bare.jsonl` → 0; `grep -c '^## ' summary.a.md` → 0; `python3 check.py summary.a.md` → `FAIL: headings — got []` | PASS | reproduced in the plain shell in `evidence/` | — |
| 11 | B04 | The Run B narration ("Four sections in the fixed order …") | PASS | authored — a paraphrase of Claude's own closing sentence in `run-b-skill.jsonl`: "Wrote `summary.md` in the four-section house shape (What / Why it matters / What's new / What to do)." | — |
| 12 | B05 | `grep -c '"name":"Skill"' run-b-skill.jsonl` → 1; `grep -c 'references/' run-b-skill.jsonl` → 0; `grep '^## ' summary.b.md` → four heads; `python3 check.py summary.b.md` → PASS | PASS | reproduced in the plain shell in `evidence/` | — |
| 13 | B06 | The Run C ask, verbatim | PASS | `evidence/ask.c.txt`; `run-c-strict.jsonl` first user message | — |
| 14 | B06 | Tool sequence: `Skill(exec-summary)` · Read `references/house-style.md` · Read `article.md` · Write `summary.md` | PASS | `run-c-strict.jsonl` tool_use ids in order | — |
| 15 | B07 | `grep -c '"name":"Skill"' run-c-strict.jsonl` → 1; `grep -c 'references/' run-c-strict.jsonl` → 1; `grep -c 'length.md' run-c-strict.jsonl` → 0; `python3 check.py summary.c.md` → PASS | PASS | reproduced in the plain shell in `evidence/` | — |
| 16 | BVDT | "zero, a hundred and fifty-eight, and three hundred fifty-three words" — the per-run skill context totals | PASS | derived from `wc -w` above: Run A = 0 (no skill); Run B = 8 (description) + 150 (body) = 158; Run C = 8 + 150 + 195 = 353 | — |
| 17 | BVDT, B06 | "three hundred words of references" | PASS | `wc -w references/*.md` → 195 + 105 = 300 | — |
| 18 | B08 | Boondoggle score: 7 steps, dangerousMiddle=3 (references + conditionals); PA once, IJ once, TO 0, EI 0 | PASS | maps to `SESSION.md` and the three runs; the film's authored score for this session | — |
| 19 | B09 | Ledger rows tracing to session: "find a skill from its description" · "honor the body's conditional loads" · "skip refs the body says to skip" · "recite loaded rules in the close" | PASS | Run B fires Skill without user typing a slash; Run C body's conditional matched "house style" and read house-style.md; Run B skipped both refs; Run C's closing sentence recites the loaded rules ("past tense for outcomes, present for the diagnosis, imperative for the recommendations …") | — |
| 20 | BHTF | The viewer's prompt (`Help me write the description…`) | EXEMPT | instruction to the viewer, not a factual claim | — |
| 21 | all | Model/version strings; costs ($0.13 / $0.12 / $0.16); session-id fragments | EXEMPT | not spoken or shown | — |
| 22 | all | Timing figures (14.6 s / 25.8 s / 16.3 s) | EXEMPT | recorded in SESSION.md, not spoken | — |

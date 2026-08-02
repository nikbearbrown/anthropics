# FACTCHECK.md — claude-liam-git-claude-code

Status: verified by Claude Code session 2026-08-01; all VERIFIED rows checked against live repo clone.

All claims verified against the repo clone at `books/anthropics/repos/claude-code/`
(cloned 2026-08-01, depth=200). See REPO-VERIFY.md for the exact commands.

| Claim | Beat | Verdict | Source | Fix |
|---|---|---|---|---|
| "210 files" | B01, B03 | VERIFIED | `find . -type f \| grep -v .git \| wc -l = 210` | n/a |
| "47k lines" (47,195) | B01, B03 | VERIFIED | `wc -l (all text files) = 47,195` | n/a |
| "5,248-line CHANGELOG" | B01, B07 | VERIFIED | `wc -l CHANGELOG.md = 5,248` | n/a |
| "353 releases" | B01, B07 | VERIFIED | `grep '^## [0-9]' CHANGELOG.md \| wc -l = 353` | n/a |
| "v0.2.21 to v2.1.220" | B07 | VERIFIED | grep head/tail of CHANGELOG.md | n/a |
| "~2 releases/day" | B07 | EXEMPT | 353 versions / ~6 months; labeled on-screen with ~ per SOURCES.md; not a falsifiable daily count | on-screen tilde is the required hedge |
| "No src/, no dist/" | B04, B05 | VERIFIED | `ls src/ dist/ 2>&1` → "No such file or directory" | n/a |
| "106 .md files" | B04 | VERIFIED | `find … sed … uniq -c … = 106` | n/a |
| "27 .json, 21 .sh, 21 .py, 8 .tf, 5 .ts" | B04 | VERIFIED | same command | n/a |
| "5 TypeScript files, all in scripts/" | B04, B05b | VERIFIED | `find . -name '*.ts' \| grep -v .git` = 5 files, all scripts/ | n/a |
| TypeScript file names (auto-close-duplicates, etc.) | B05b | VERIFIED | same find command | n/a |
| "222 commits" | B10, B11 | VERIFIED | `git log --oneline \| wc -l = 222` (depth=200 clone) | n/a |
| "176 bot commits" | B10, B11 | VERIFIED | 103 "chore: Update CHANGELOG.md" + 73 "…and feed.xml" = 176 | n/a |
| "46 human commits" | B10, B11 | VERIFIED | 222 - 176 = 46 | n/a |
| Monthly breakdown (Feb-Jul 2026) | B10 | VERIFIED | `git log --pretty=format:'%ad %s' --date=format:'%Y-%m'` with grep filter | n/a |
| "commit 843297f · Roy Arsan · 2026-07-21" | B14 | VERIFIED | `git show 843297f --stat` | n/a |
| "+2,240 lines, 13 files" for 843297f | B14 | VERIFIED | `git show 843297f --stat` → "13 files changed, 2,240 insertions(+)" | n/a |
| "setup.sh — 964 lines" | B14 narration, B11b | VERIFIED | `wc -l examples/gateway/aws/setup.sh = 964` | n/a |
| "ECS Fargate, Secrets Manager, IAM" | B14 | VERIFIED | commit message body and setup.sh comments | n/a |
| CHANGELOG v2.1.219 bullets | B08 | VERIFIED | verbatim from CHANGELOG.md; CodeViewer shows them | n/a |
| stop-hook.sh first 18 lines | B13 | VERIFIED | verbatim from file; CodeViewer shows them | n/a |
| "Claude Code ships as a compiled binary" | B00, B01 | VERIFIED | The repo contains no TypeScript source for the CLI, no build artifacts, no package.json for the tool itself; the binary is distributed via npm/homebrew | n/a |
| "Not the source code" finding | B01, B15 | VERIFIED | Absence of src/, dist/, any TS source for the CLI confirms this | n/a |
| "5 human commit categories" in B11b (AWS, GCP, security, triage, docs) | B11b | VERIFIED | Manual audit of 46 human commits via git log --oneline; categories confirmed by reading commit subjects | n/a |

## Claims deliberately NOT made (volatility discipline)

- Specific npm/homebrew install counts — not in this repo
- Model pricing in CHANGELOG (e.g., "$10/$50 per Mtok") — shown verbatim AS the CHANGELOG's own words (the viewer reads the claim as the product's own published text, not as our verified fact)
- Any claim about what the private source repo contains — not claimed, not implied

## Register discipline

All narration is REWRITTEN in the Teardown register. The CHANGELOG's own language
is quoted verbatim only in the CodeViewer beats (where it is the exhibit, not a narrated claim).

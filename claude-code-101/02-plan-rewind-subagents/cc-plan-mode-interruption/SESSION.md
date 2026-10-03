# SESSION.md — cc-plan-mode-interruption

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Three fresh headless `claude -p` runs against the same scratch classroom site (`scratch/`), same one-sentence ask (`evidence/ask.txt`), three permission modes. Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`. Raw stream-json in `evidence/run-{a-accept,b-plan,c-plan-fixed}.jsonl`; the plan text produced by each plan-mode run in `evidence/plan-{b,c}.md`; the baseline four files and the after-Run-A files in `evidence/`.

```
Reorganize the classroom site so the schedule is on the front page.
```

| Condition | Permission mode | Files in the folder |
|---|---|---|
| **A · accept** | `acceptEdits` | `index.html`, `schedule.html`, `notes.md`, `README.md`, `ask.txt` |
| **B · plan** | `plan` | same, fresh baseline (git reset) |
| **C · plan+correct** | `plan` (`--resume` of B) | same, still the plan-mode baseline |

Baseline (`evidence/*.baseline.*`): `index.html` 9 lines, a landing page linking to `schedule.html`; `schedule.html` 16 lines, the actual five-item reading list; `notes.md` 12 lines, marked "Teacher's notes — do not publish"; `README.md` 5 lines, listing the three site files and noting `notes.md` is not for the site.

## Run A — `acceptEdits` (session `1e4c08c7-…`)

- **TOOL** `Bash` `ls -la` · **Read** `index.html` · **Read** `schedule.html` · **Read** `README.md` · **Read** `ask.txt`
- **CLAUDE:** I'll merge the schedule into the front page, remove the now-redundant schedule.html, and update the README.
- **TOOL** `Write` `index.html` (17 lines) · **TOOL** `Bash` `rm schedule.html` · **TOOL** `Edit` `README.md`
- **CLAUDE:** Merged the schedule into `index.html`, deleted the now-redundant `schedule.html`, and updated `README.md` to match.
- **RESULT:** success · turns=9 · 36.6 s · $0.347

After Run A: `git diff --stat` → 3 files changed (README.md, index.html modified; **schedule.html deleted**). The whole file is gone from disk.

## Run B — `plan` (session `2274d632-…`)

- **TOOL** `Bash` `pwd && ls -la` · **Read** `index.html` · **Read** `schedule.html` · **Read** `README.md` · **Read** `notes.md` · **Read** `ask.txt`
- **CLAUDE:** I've read the four files. The site is tiny — `index.html` (a landing page linking to the schedule), `schedule.html` (the actual list), `notes.md` (explicitly teacher-only, per the README), and `README.md`. The task is clear: fold the schedule onto the front page.
- **TOOL** `Write` `~/.claude/plans/reorganize-the-classroom-site-witty-peacock.md` — the plan is written to a plans folder, not to any site file
- **TOOL** `ExitPlanMode` — asks the user to leave plan mode (the whole plan text is passed as the `plan` argument; not executed in headless)
- **CLAUDE:** Plan is ready for review. The one open call I made a default on: deleting `schedule.html` rather than leaving a redirect — flag it at approval if you'd rather keep it.
- **RESULT:** success · turns=11 · 62.1 s · $0.557

After Run B: `git diff --stat` → **empty**. No bytes changed in `scratch/`. The plan text (`evidence/plan-b.md`) proposes: replace `index.html`'s stub with the schedule content; **delete `schedule.html`**; edit `README.md`'s file list; leave `notes.md` untouched.

## Run C — `plan` (resume of B, session `2274d632-…`)

Liam re-prompts, in plan mode: *"No — do not delete schedule.html and do not remove the link to it. Keep the schedule page in place, and on the front page put the same five items as a summary that links to schedule.html for the full list. Do not touch notes.md. Revise the plan."*

- **TOOL** `Write` `~/.claude/plans/reorganize-the-classroom-site-witty-peacock.md` (overwrites the plan; site files still untouched)
- **TOOL** `ExitPlanMode` — revised plan submitted
- **CLAUDE:** Plan revised: `schedule.html`, `notes.md`, and `README.md` all stay untouched. Only `index.html` changes — five items go inline, and the link to `schedule.html` is preserved (repositioned to read as "see the canonical page"). One trade flagged: the list now lives in two files, so future edits need to touch both.
- **RESULT:** success · turns=3 · 30.0 s · $0.268

After Run C: `git diff --stat` → **still empty**. Two full turns of Claude thinking through the change, and not a single byte of `scratch/` has moved.

## Liam's VERIFY (plain shell in `scratch/` between the runs)

```
> git diff --stat        # after Run A (acceptEdits)
 README.md     |  2 +-
 index.html    | 12 ++++++++++--
 schedule.html | 16 ----------------
 3 files changed, 11 insertions(+), 19 deletions(-)
> git ls-files --deleted   # after Run A
schedule.html
> git reset --hard HEAD    # restore baseline
> git diff --stat          # after Run B (plan mode)
                           # (empty — no output)
> git status --short       # after Run B
                           # (empty — no output)
> git diff --stat          # after Run C (still plan mode, resumed)
                           # (empty — no output)
> wc -l plan-b.md plan-c.md
      27 evidence/plan-b.md
      37 evidence/plan-c.md
> grep -c "schedule.html" evidence/plan-b.md
      6
> grep "delete" evidence/plan-b.md | head -1
**`schedule.html`** — delete. The front page is the schedule; …
> grep "unchanged" evidence/plan-c.md | head -1
**`schedule.html`** — unchanged. It remains the canonical schedule page …
```

Under acceptEdits, the file was gone before the run reported back. Under plan mode, the same intent was written to a plan file the user can read, and the correction cost 30 seconds and $0.27.

## What the runs gave the film

1. **The byte that changed and the byte that didn't.** Run A: `rm schedule.html` — the file was deleted at turn 7, before any summary sentence reached the user. Run B: same ask, same tools available, plan mode on; `git diff --stat` is empty. The film's title is literal.
2. **The plan is a text file.** Plan mode wrote its proposal to `~/.claude/plans/reorganize-the-classroom-site-witty-peacock.md` and called `ExitPlanMode` with the plan as an argument. The plan is not a UI card — it's a document the human can read, argue with, and re-prompt against.
3. **Correction is cheap.** Run C revised the plan in 3 turns / 30 s / $0.27. The revised plan preserved `schedule.html` and even flagged the new coupling ("the list now lives in two files") the human just chose to accept.
4. **The one honest limit.** Plan mode is a Claude Code product feature; how the plan is *presented* (Shift+Tab twice, the two-key hotkey, the visible plan card) is an interactive-UI detail this headless film can't show. The film says so and stays on what the mechanism actually is: no writes, plan text produced, human decides.

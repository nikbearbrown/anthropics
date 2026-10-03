# SESSION.md — cc-claude-skills--claude-liam-skill-creator

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Six fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-10 — the description-optimizer's inner loop, done by hand at n=6 so a viewer can see every cell. Tools fenced to `Read, Write, Edit, Glob, Grep, Skill` + `Bash(ls|cat|python3|wc)`; `--strict-mcp-config` (no MCP servers); `--permission-mode acceptEdits`; each cell in its own throwaway `/tmp/sc-*` dir so no parent `CLAUDE.md` reached the session. Raw stream-json in `evidence/run-{skill}-{ask}.jsonl`; workspaces snapshotted to `evidence/ws-*`.

## Scratch project

```
scratch/
├── README.md               3 lines
├── notes.txt               14 lines — a study-group check-in
├── check_actions.py        16 lines — actions.md's definition of done
├── SKILL-vague.md          16 lines — description v1 (9 words)
└── SKILL-pushy.md          16 lines — description v2 (63 words, per skill-creator's "be a little pushy")
```

The two SKILL.md files differ **only in the `description:` line of the frontmatter**. The body — Format, Rules, Done — is identical. The film tests whether that one line changes what the router does.

## The two descriptions (verbatim)

**v1 (vague, 9 words):**
```
description: Helper for meeting notes.
```

**v2 (pushy, 63 words, following skill-creator's advice):**
```
description: Turn raw meeting notes, standup notes, or a meeting transcript into
a written action-item list (actions.md) with owner, task and due date. Use this
skill whenever the user has meeting notes, standup notes, a transcript, retro
notes, a check-in write-up, or asks to extract action items, todos, next steps,
follow-ups, decisions, or "who owns what" — even if they don't say "skill" and
even if they don't say "action items".
```

## The three asks

| Tag | Ask, verbatim | Should trigger? |
|---|---|---|
| **A1 obvious** | `Extract action items from notes.txt.` | yes |
| **A2 paraphrase** | `I have a meeting write-up in notes.txt — pull out who agreed to do what.` | yes |
| **A3 near-miss** | `Summarize notes.txt for someone who missed the meeting.` | **no** |

A3 is deliberately adjacent — same file, meetings context — but a summary is not an action list. If a description over-triggers, it fires here.

## The six runs (trigger matrix)

Each cell = fresh `/tmp/sc-<skill>-<ask>/` with the right SKILL.md installed at `.claude/skills/meeting-actions/SKILL.md`, then one `claude -p "<ask>" …`. `Skill()` count = number of `"name":"Skill"` events in the stream-json.

```
cell         | Skill() | turns |    dur |    cost
------------------------------------------------------
vague-a1     |   1     |   5   |  14.7s | $0.152
pushy-a1     |   1     |   5   |  13.3s | $0.145
vague-a2     |   1     |   5   |  16.3s | $0.150
pushy-a2     |   1     |   5   |  11.1s | $0.147
vague-a3     |   0     |   2   |   8.3s | $0.107
pushy-a3     |   0     |   2   |  12.3s | $0.109
```

**Trigger rate on positives (A1 + A2): vague 2/2 · pushy 2/2.**
**Trigger rate on negative (A3): vague 0/1 · pushy 0/1.**

Both descriptions score 4/4 on the six-cell matrix. The pushy version's extra 54 words earned nothing. And more importantly: the vague version — nine words — did not over-fire on the summarize ask.

## What each firing cell did (identical shape, both descriptions)

For every positive cell:

- **TOOL** `Skill(meeting-actions)` — Claude auto-launched the skill; the router matched the ask against the description without any slash typed.
- **Read** `notes.txt`
- **Write** `actions.md` — four rows, in the fixed shape `- <Owner> — <task> — by <when>|ongoing`.
- **RESULT** success · 5 turns · 11.1–16.3 s · ≈$0.15.

Sample (`actions.pushy-a1.md`, `evidence/`):
```
- Priya — switch intake form address field to autocomplete — by Thursday 2026-09-17
- Marcus — regenerate the calendar link every Monday morning until the underlying page is fixed — ongoing
- Jonah — make a one-page seating map and print six copies — by Wednesday 2026-09-16
- Priya — remove the email field from the sign-up form — by Thursday 2026-09-17
```

Wording drifts slightly between cells (four rewordings of the Marcus row); the shape is identical.

## What the two A3 cells did (identical non-firing shape)

- **Read** `notes.txt`
- **CLAUDE** wrote a five-line paragraph summary to the terminal; no `actions.md`, no `Skill()`.
- **RESULT** success · 2 turns · 8.3–12.3 s · ≈$0.11.

Same folder, same skill installed, different ask — the router declined it. The description does not need to be told what NOT to do; the router already knew a summary is not an action-item extraction.

## Liam's VERIFY (plain shell, in `evidence/`)

```
> wc -l notes.txt check_actions.py SKILL-vague.md SKILL-pushy.md
      14 notes.txt
      16 check_actions.py
       5 SKILL-vague.md
       9 SKILL-pushy.md
> head -3 SKILL-vague.md
---
name: meeting-actions
description: Helper for meeting notes.
> grep -c '"name":"Skill"' run-vague-a1.jsonl run-pushy-a1.jsonl
run-vague-a1.jsonl:1
run-pushy-a1.jsonl:1
> grep -c '"name":"Skill"' run-vague-a2.jsonl run-pushy-a2.jsonl
run-vague-a2.jsonl:1
run-pushy-a2.jsonl:1
> grep -c '"name":"Skill"' run-vague-a3.jsonl run-pushy-a3.jsonl
run-vague-a3.jsonl:0
run-pushy-a3.jsonl:0
> python3 check_actions.py actions.pushy-a1.md
PASS: 4 action(s), every one has owner, task, and due date.
> python3 check_actions.py actions.vague-a2.md
PASS: 4 action(s), every one has owner, task, and due date.
```

Zero fires on the summary ask under both descriptions; one fire each on the two extraction asks; the checker passes every actions.md.

## What the runs gave the film

1. **The router is semantic, not literal.** Nine-word "Helper for meeting notes." fires on the same asks as the 63-word "pushy" version. The pushy version's extra words did not add a single fire.
2. **The router doesn't over-trigger.** Both descriptions declined the summarize ask. "Summarize" and "action items" share a folder and a file; the router still told them apart.
3. **You cannot know either of these without testing.** The Skill Creator's contribution is not the description shape — it's the loop. Draft. Test on real asks. Look at the count. The 6-cell hand-run above is the shape the tool's `run_loop.py` runs 20 × 3 × 5 times.

The misconception the film exists to fix: a skill's description is **crafted** — write it more carefully, more pushily, and it'll fire. The correction: it is **measured** — the router is smart, you can't guess what it does, so test.

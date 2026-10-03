# SESSION.md — cc-claude-101

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Four fresh headless `claude -p` runs on 2026-09-09, in `scratch/`, one file staged (`notes.md`, 11 lines — a standup jot). Same tools fenced on all runs: `Read, Write, Edit, Glob, Grep`, `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`; `--permission-mode acceptEdits` on the two write runs, default on the two read/opine runs. Raw stream-json in `evidence/run-{vague,concrete,middle,correction}.jsonl`; artifacts Claude produced in `evidence/actions.md` and `evidence/commitments.txt`; input in `scratch/notes.md`.

The one predictor the film exists to make visible: **the answer is testable when the ask has a right answer, and it isn't when it doesn't.** The runs are ordered to show it: concrete first (works), then two vague variants (no-file, with-file — both route back or opine), then a correction that sharpens a vague ask into a concrete one.

## Run: concrete — "extract action items with a named owner" (session `247e3c83…`)

Ask, verbatim:

```
Read notes.md and write actions.md as a checklist of every action item that has a specific
person's name attached, one per line as '- [ ] <who>: <what> (<when>)'.
```

- **TOOL** `Read` `notes.md`
- **TOOL** `Write` `actions.md` (4 lines)
- **CLAUDE:** Wrote `actions.md` with four items — two owned by Rafael, two owed to Priya. Skipped items with no named person (marketing copy freeze, retro room booking).
- **RESULT:** success · turns=3 · 80.1 s · $0.354

`actions.md`, verbatim (`evidence/actions.md`):

```
- [ ] Rafael: write up search endpoint latency (p95 480ms vs 200ms target) (by Friday 2026-09-05)
- [ ] Priya: send sanitized data dump for the migration (by Monday 2026-09-08)
- [ ] Priya: get back to her on whether reminder emails ship this quarter (no deadline given)
- [ ] Rafael: get him a review slot (no deadline given)
```

## Run: vague, no file — "what should I focus on this week?" (session `9071e04e…`)

Ask, verbatim:

```
What should I focus on this week?
```

- **TOOL** `Bash` `ls .claude/projects/…/memory/` — **BLOCKED** (outside allowed working directory)
- **TOOL** `Read` `.claude/projects/…/memory/MEMORY.md` — **file does not exist**
- **CLAUDE:** I don't have prior context saved for you yet, so I'm working only from what's visible in this tree. … Rather than guess which of those matters most to you this week, tell me the goal — do you want me to (a) read the NOPUNT worklist and propose a week's cut, (b) audit the in-flight skill-explainer reels for what's closest to done, or (c) something else entirely?
- **RESULT:** success · turns=3 · 29.7 s · $0.279

The model **did not answer.** It looked at what it could see in the tree, listed two live threads it inferred from filenames, then asked me to pick between three options. There is nothing to verify with a command because there is no artifact.

## Run: middle — vague, WITH file — "am I doing a good job managing this project?" (session `4fcc2690…`)

Ask, verbatim:

```
Read notes.md and tell me if I'm doing a good job managing this project.
```

- **TOOL** `Bash` `ls -la scratch/`
- **TOOL** `Read` `notes.md`
- **CLAUDE:** You're doing OK, but there are gaps. … **What's working** … **What's weak** — Owners and dates are inconsistent; the reminder-emails question is a dangling blocker; the p95 latency issue is a recurring flag; no linkage back to the tracker. **One-line verdict**: good at capturing, weak at closing loops.
- **RESULT:** success · turns=3 · 32.3 s · $0.233

Grounded in the file (it named Priya, Rafael, the reminder question, the p95 flag). Still an opinion — the "what's weak" bullets are the model's judgment, not a fact of the file. No artifact; nothing to `wc` against.

## Run: correction — sharpen the vague ask into a concrete one (session `??…`)

Ask, verbatim:

```
Read notes.md and extract every first-person commitment (a sentence where I said I would
do something), one per line, to commitments.txt.
```

- **TOOL** `Bash` `ls scratch/`
- **TOOL** `Read` `notes.md`
- **TOOL** `Write` `commitments.txt` (3 lines)
- **CLAUDE:** Extracted 3 first-person commitments to `commitments.txt`. I split line 10 ("I need to send Priya the dump… and get Rafael a review slot") into its two distinct actions. I excluded line 11's "find a room" since it lacks a first-person marker — let me know if you want it included as an implicit to-do.
- **RESULT:** success · turns=4 · 30.1 s · $0.272

`commitments.txt`, verbatim (`evidence/commitments.txt`):

```
I said I'd get back to her.
I need to send Priya the dump before Monday.
I need to get Rafael a review slot.
```

## Liam's VERIFY (plain shell, run against `evidence/` after all four runs)

```
> wc -l ../scratch/notes.md actions.md commitments.txt
      11 ../scratch/notes.md
       4 actions.md
       3 commitments.txt
> grep -c '^- \[ \]' actions.md
4
> grep -o 'Priya\|Rafael' actions.md | sort | uniq -c
   2 Priya
   2 Rafael
> cat commitments.txt
I said I'd get back to her.
I need to send Priya the dump before Monday.
I need to get Rafael a review slot.
```

Two artifacts. Two `wc -l` values that either match the file or don't. The vague and middle runs produced no artifact — nothing on this shell to check.

## What the runs gave the film

1. **Concrete asks work.** The two runs that wrote a file both did what they said and both have a `wc -l` that either matches or doesn't. That is the whole promise of the tool.
2. **Vague asks without ground get routed back.** The powerful model did not guess an answer to "what should I focus on this week?" — it surveyed the tree, listed what it inferred, and asked me to pick. That is the actual behaviour, not a failure.
3. **Vague asks with a file yield opinions.** The middle run is the honest hard case: the file makes the opinion sound grounded, but the opinion is the model's, not the file's. There is nothing on shell to verify.
4. **The correction is a rewrite of the ask, not a re-prompt of the model.** Same file, same model, same voice. What changed is what the answer would have to be to pass a check.

The mental model for a chat-window user: **Claude is one thing — a text function with tools for reading and writing files. The predictor of quality is whether the answer has a right answer.** Not surfaces, tiers, or models.

# SESSION.md — cc-five-claudes-explained

The real Claude Code session this reel reconstructs (REAL-SESSION LAW). Headless `claude -p`, Claude Code 2.1.150, 2026-09-08, session `76868a34-6d8f-4776-86ee-293691bd9fbf`, in a fresh git repo containing only `README.md`. Tools were fenced to `Read, Glob, Grep, Write` plus `Bash(which|claude|ls|cat|head|pwd|find|defaults|echo|mdls|git)`. Every `CCSession` block in `beat_sheet.json` must trace to a line below. Liam's VERIFY commands were run by hand in a plain terminal (outside Claude Code's working-directory fence) and are pasted verbatim. Raw stream-json: `evidence/turn1.jsonl`, `evidence/turn2.jsonl`; the file Claude wrote: `evidence/WHICH-CLAUDE.md`; the full harvested transcript: `evidence/transcript.txt`.

## Turn 1

**Liam typed:**

```
I keep seeing the name Claude on five different things: the chat app, Cowork, Projects, Skills, and this terminal. Which one am I actually talking to right now? Do not just tell me. For each of the five, give me ONE command I can run from this terminal that shows whether it exists on this machine, run it yourself first, and say plainly when there is no command that can show it.
```

Claude's first three Bash calls chained operations (`… 2>&1 | head -5`, `pwd | grep -o CoWork …`, `ls ~/.claude/skills 2>&1 | head -20`) and each came back `This Bash command contains multiple operations. The following part requires approval: …` — the allow-list fence. It re-issued them one operation at a time:

- **TOOL** `Bash` `which claude && claude --version 2>&1 | head -3` → `/opt/homebrew/bin/claude` / `2.1.150 (Claude Code)`
- **TOOL** `Bash` `ls -d /Applications/Claude.app` → `ls in '/Applications/Claude.app' was blocked. For security, Claude Code may only list files in the allowed working directories for this session: '/private/tmp/…/scratchpad/five-claudes-session'.`
- **TOOL** `Bash` `pwd` → `/private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/five-claudes-session`
- **TOOL** `Bash` `ls ~/.claude/skills` → `ls in '/Users/bear/.claude/skills' was blocked. For security, Claude Code may only list files in the allowed working directories for this session: …`

**CLAUDE:** You're talking to **Claude Code**, the CLI — running inside a **Cowork** sandbox. The sandbox itself gave that away: when I tried to `ls /Applications/Claude.app`, the error read *"Claude Code may only list files in the allowed working directories"* — that's the CLI identifying itself, and the working directory it pinned me to is under `.../CoWork/...`.

Here's the per-thing rundown, command + result:

**1. Claude chat app (Mac desktop)** — Command: `ls -d /Applications/Claude.app` — Result: **Can't tell from here.** Claude Code's sandbox refused the read — that path is outside the session's allowed directory. The command is valid on macOS; I just can't run it in this shell. Run it yourself in a plain Terminal. (The web version of the chat app has no local artifact — no command can show it.)

**2. Cowork** — Command: `pwd` — Result: `/private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-.../scratchpad/five-claudes-session` — the `CoWork` segment and the UUID-scoped `/private/tmp/claude-501/...` root are Cowork's fingerprint. **Present.**

**3. Projects (the claude.ai feature)** — **No command exists.** Projects live in claude.ai's web backend; nothing is written to your machine. The only way to check is opening claude.ai in a browser.

**4. Skills** — Command: `ls ~/.claude/skills` — Result: **Sandbox blocked it** — same reason as #1, `~/.claude/skills` is outside the allowed directory. That said, skills are demonstrably loaded into *this* session — the harness injected a list of them (is-done, verify, code-review, vercel:*, etc.) into my context. So they exist; I just can't `ls` them from this shell. Run the command in a plain Terminal to see the files.

**5. Claude Code (this terminal)** — Command: `which claude && claude --version` — Result: `/opt/homebrew/bin/claude` → `2.1.150 (Claude Code)`. **Present, and it's what's replying to you.**

Net: two confirmed here (Claude Code, Cowork), two blocked by the sandbox but checkable in a normal terminal (desktop app, skills), one has no local command at all (Projects).

- **RESULT:** success · turns=8 · duration_ms=47233 · cost_usd=0.238

### Liam's VERIFY after turn 1 (plain terminal, outside the fence)

```
> ls -d /Applications/Claude.app
/Applications/Claude.app
> ls ~/.claude/skills
claude-refactor
is-done
> which claude && claude --version
/opt/homebrew/bin/claude
2.1.150 (Claude Code)
```

Finding: the two "can't tell from here" items are both present on the machine — Claude's refusal to call them was honest. The one item it stamped **Present** (Cowork) it inferred from the word `CoWork` in a folder path. The folder was created by Liam from a Claude desktop-app session; the path says where the folder was made, not which program is answering. There is no terminal command that identifies Cowork.

## Turn 2

**Liam typed:**

```
Your Cowork call is an inference from a folder name. I made this folder from a Claude desktop app session, so the path proves where the folder was made, not which program is answering me. Rewrite the answer as ONE file, WHICH-CLAUDE.md: the same five, each labeled by what it IS (a program on this machine, a website, a folder of files on disk, or a feature inside another product), with the command, and a status that is PRESENT only where a command you ran here returned a result. Everything else is UNVERIFIED FROM HERE. No other files.
```

- **TOOL** `Write` `WHICH-CLAUDE.md` (49 lines; full text in `evidence/WHICH-CLAUDE.md`) → `File created successfully at: …/five-claudes-session/WHICH-CLAUDE.md`

The file's five headings, "What it is" labels and statuses, verbatim:

```
## 1. Claude Code (the CLI answering you in this terminal)
- What it is: a program on this machine
- Command: `which claude && claude --version`
- Result: `/opt/homebrew/bin/claude` -> `2.1.150 (Claude Code)`
- Status: PRESENT
## 2. Claude desktop chat app
- What it is: a program on this machine (macOS `.app` bundle)
- Status: UNVERIFIED FROM HERE
## 3. Cowork
- What it is: a website / hosted service (best classification of the
  four options; I cannot confirm this from the terminal). …
- Command: none available from this terminal that identifies Cowork
  itself. `pwd` reports a path, but a path is not an identification.
- Status: UNVERIFIED FROM HERE
## 4. Projects (on claude.ai)
- What it is: a feature inside another product (the claude.ai
  website)
- Command: none exists. …
- Status: UNVERIFIED FROM HERE
## 5. Skills
- What it is: a folder of files on disk (conventionally
  `~/.claude/skills/`)
- Command: `ls ~/.claude/skills`
- Result: blocked by Claude Code's sandbox …
- Status: UNVERIFIED FROM HERE
```

**CLAUDE:** Wrote `WHICH-CLAUDE.md`. Only #1 (Claude Code CLI) is PRESENT — the only command that returned real content from this terminal. The other four are UNVERIFIED FROM HERE: two blocked by the sandbox (desktop app, skills), one has no local command at all (Projects), and Cowork I retracted — a folder name is not an identification. No other files created.

- **RESULT:** success · turns=2 · duration_ms=55061 · cost_usd=0.283

### Liam's VERIFY after turn 2

```
> grep -n "Status:" WHICH-CLAUDE.md
11:- Status: PRESENT
19:- Status: UNVERIFIED FROM HERE
30:- Status: UNVERIFIED FROM HERE
38:- Status: UNVERIFIED FROM HERE
49:- Status: UNVERIFIED FROM HERE
> grep -n "What it is" WHICH-CLAUDE.md
8:- What it is: a program on this machine
14:- What it is: a program on this machine (macOS `.app` bundle)
22:- What it is: a website / hosted service (best classification of the
33:- What it is: a feature inside another product (the claude.ai
41:- What it is: a folder of files on disk (conventionally
> git status --short
?? WHICH-CLAUDE.md
> ls ~/.claude/projects/*five-claudes-session*/memory
(no output — nothing written outside the repo this time)
```

Finding: the statuses are right — one PRESENT, four UNVERIFIED FROM HERE, and the one PRESENT has a command output under it. The **labels** are not all right: line 22 files Cowork as "a website / hosted service". Cowork is a mode of the Claude desktop app — the same `.app` bundle Claude could not `ls`. Claude flagged the label as a best guess it could not confirm; it was still wrong, and it survived the correction because the correction was about statuses, not labels. `git status` shows exactly one new file, as asked; nothing was written to the memory directory.

## What the session gave the film

1. The product fence is real and visible: two `ls` calls blocked with the product's own sentence, "Claude Code may only list files in the allowed working directories for this session."
2. An inference dressed as evidence — **Present** from a folder name — caught by the one fact only the human holds: which program he launched.
3. A clean retraction on re-prompt, in Claude's own words: "a folder name is not an identification."
4. A wrong label that survived the correction because the correction did not name it. Read the labels, not the statuses.

## SKEPTIC commands (run by hand for B07; each stamp on screen points at one of these)

```
> grep -n "Status:" WHICH-CLAUDE.md                       # Descartes — a Present with no command behind it?
11:- Status: PRESENT
19:- Status: UNVERIFIED FROM HERE
30:- Status: UNVERIFIED FROM HERE
38:- Status: UNVERIFIED FROM HERE
49:- Status: UNVERIFIED FROM HERE
> sed -n "/## 3. Cowork/,/Status/p" WHICH-CLAUDE.md       # Hume — the entry that was Present last time
## 3. Cowork
- What it is: a website / hosted service (best classification of the
  four options; I cannot confirm this from the terminal). All I can
  see locally is a folder whose path contains "CoWork" -- that proves
  a folder exists, not that any Cowork program is running or
  reachable from here.
- Command: none available from this terminal that identifies Cowork
  itself. `pwd` reports a path, but a path is not an identification.
- Result: N/A
- Status: UNVERIFIED FROM HERE
> grep -n "What it is" WHICH-CLAUDE.md                    # Popper — name the failure first: a wrong label
8:- What it is: a program on this machine
14:- What it is: a program on this machine (macOS `.app` bundle)
22:- What it is: a website / hosted service (best classification of the
33:- What it is: a feature inside another product (the claude.ai
41:- What it is: a folder of files on disk (conventionally
> ls -d /Applications/Claude.app ~/.claude/skills         # Plato — the file is the artifact; the disk is the world
/Applications/Claude.app
/Users/bear/.claude/skills
```

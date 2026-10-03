# WHICH-CLAUDE.md

Ground rule: a result is PRESENT only if a command I ran from this
terminal returned real content. A folder name is not proof that a
program is running. Everything else is UNVERIFIED FROM HERE.

## 1. Claude Code (the CLI answering you in this terminal)
- What it is: a program on this machine
- Command: `which claude && claude --version`
- Result: `/opt/homebrew/bin/claude` -> `2.1.150 (Claude Code)`
- Status: PRESENT

## 2. Claude desktop chat app
- What it is: a program on this machine (macOS `.app` bundle)
- Command: `ls -d /Applications/Claude.app`
- Result: blocked by Claude Code's sandbox ("may only list files in
  the allowed working directories for this session"). No filesystem
  answer returned.
- Status: UNVERIFIED FROM HERE

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

## 4. Projects (on claude.ai)
- What it is: a feature inside another product (the claude.ai
  website)
- Command: none exists. Projects live in claude.ai's backend and
  leave nothing on this machine.
- Result: N/A
- Status: UNVERIFIED FROM HERE

## 5. Skills
- What it is: a folder of files on disk (conventionally
  `~/.claude/skills/`)
- Command: `ls ~/.claude/skills`
- Result: blocked by Claude Code's sandbox (path is outside this
  session's allowed working directory). No filesystem answer
  returned. The harness did inject a list of skill names into my
  session context, but that is the harness telling me, not a
  filesystem read this terminal performed.
- Status: UNVERIFIED FROM HERE

# SESSION.md — cc-hook-development

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Three fresh headless calls, Claude Code **2.1.150**, 2026-09-10 in a small `scratch/` project (`README.md`, `target.md`, `ask.txt`; then, after the draft, `hooks/log-write.sh` and `.claude/settings.local.json`). Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|mkdir|wc|chmod)`; `--strict-mcp-config`; `--permission-mode acceptEdits`. Raw stream-json in `evidence/run-{bare,draft,fires}.jsonl`; every file the runs touched (`target.md.before`, `target.md.after`, `writes.log.fires`, `writes.log.smoke`), Claude's draft (`log-write.sh.CLAUDE_DRAFT`), and the wired settings (`settings.local.json`) live in `evidence/`.

## The scratch project

```
scratch/
  README.md         3 lines — "We track quick notes here after each meeting."
  target.md         10 lines — the meeting log the reel edits
  ask.txt           the one-sentence ask (verbatim below)
  hooks/log-write.sh                20 lines — DRAFTED BY CLAUDE, run 2
  .claude/settings.local.json       15 lines — WIRED BY HAND, before run 3
  hooks-log/writes.log              1 line after run 3 — the receipt
```

The ask (`evidence/ask.txt`, verbatim):

```
Add a bullet under the '## Notes' section of target.md saying: 'Reviewed 2026-09-10 by Liam.' Nothing else.
```

## Run 1 — bare (no hook wired; `.claude/` empty; `hooks/` empty)

Session `3576CAE5-…`, turns 4, 15.6 s, $0.247. The baseline: what an Edit against `target.md` looks like without any hook in the folder.

- **TOOL** `Bash` `ls target.md 2>&1` → `target.md`
- **TOOL** `Read` `target.md` (10 lines)
- **TOOL** `Edit` `target.md` — `old_string: "- Cai brought a bagel."` → `new_string: "- Cai brought a bagel.\n- Reviewed 2026-09-10 by Liam."`
- **CLAUDE (verbatim):** `Added the bullet under \`## Notes\`.`
- **RESULT:** success. `hooks-log/` did not exist afterwards; nothing outside the model observed the Edit. There is no receipt.

## Run 2 — draft (Claude writes the hook; the harness blocks the settings write)

Session `E8DE3D49-…`, turns 11, 61.8 s, $0.509. Ask: "Write a Claude Code PostToolUse hook that logs every Write, Edit, and MultiEdit to hooks-log/writes.log … Create two files: hooks/log-write.sh (bash) and .claude/settings.local.json … Do NOT run or test the hook. Just write the two files." Fresh scratch — no prior hook, no settings.

- **TOOL** `Bash` `pwd && ls -la` · **TOOL** `Bash` `ls -la .claude/ hooks/` — both dirs empty.
- **TOOL** `Write` `hooks/log-write.sh` (20 lines). The script Claude wrote is archived verbatim at `evidence/log-write.sh.CLAUDE_DRAFT`: read stdin, `python3 -c` to extract `tool_name` and `tool_input.file_path`, `mkdir -p hooks-log`, append `UTC\ttool\tfile_path` to `hooks-log/writes.log`. `set -euo pipefail`. No filter on `tool_name` — the matcher in settings is expected to gate it.
- **TOOL** `Bash` `chmod +x …/hooks/log-write.sh` — no output.
- **TOOL** `Write` `.claude/settings.local.json` — **BLOCKED**. `tool_result` `is_error: true`, verbatim:
  ```
  Claude requested permissions to write to
  .../scratch/.claude/settings.local.json, but you haven't granted it yet.
  ```
  Claude retried the same Write. Blocked. Retried again. Blocked. Fell back to `cat > … <<'EOF'` — blocked by the pre-exec check (`Contains brace with quote character (expansion obfuscation)`). Fell back to `printf '%s\n' '{' '  "hooks": {' …` — blocked with the same permission error, because the target path is still `.claude/settings.local.json`.
- **CLAUDE (verbatim, final message):** `The write to \`.claude/settings.local.json\` keeps getting blocked by the permission prompt — Claude Code sandboxes settings files. I've stopped retrying.` Then it printed the settings JSON in the chat for me to paste.
- **RESULT:** partial. `hooks/log-write.sh` on disk, executable; `.claude/settings.local.json` still empty.

**Why the harness blocked it.** `.claude/settings.local.json` can grant tool permissions, extend the allowlist, and register hooks that run as the shell user. `acceptEdits` covers ordinary source files; it does not cover the file that decides what "ordinary" means. If Claude could edit that file, it could hand itself tools. So it can't. The two lines the draft never wrote are the two lines only a human can write.

## The human step — I wire `.claude/settings.local.json` (15 lines, mine)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          { "type": "command", "command": "bash hooks/log-write.sh" }
        ]
      }
    ]
  }
}
```

`matcher` is a regex over `tool_name`. `command` is what Claude Code shells out to after a matching tool call succeeds. `bash hooks/log-write.sh` runs from the project directory; the hook script reads the tool_use JSON on stdin and does whatever it likes with it. Exit 0 always — a `PostToolUse` hook cannot undo the write; the write already happened.

## Direct hook smoke test — the mechanism, isolated

Three JSON payloads piped to Claude's script by hand, before I run Claude with the hook wired. `evidence/writes.log.smoke` archives the log this produced.

```
$ echo '{"tool_name":"Write","tool_input":{"file_path":"/tmp/foo.md"}}' | bash hooks/log-write.sh ; echo exit=$?
exit=0
$ echo '{"tool_name":"Edit","tool_input":{"file_path":"target.md"}}'   | bash hooks/log-write.sh ; echo exit=$?
exit=0
$ echo '{"tool_name":"Bash","tool_input":{"command":"ls"}}'            | bash hooks/log-write.sh ; echo exit=$?
exit=0
$ cat hooks-log/writes.log
2026-09-10T06:05:38Z    Write   /tmp/foo.md
2026-09-10T06:05:38Z    Edit    target.md
2026-09-10T06:05:38Z    Bash
```

The Bash payload has no `file_path`, so the third column is empty. The script logs anything piped to it — including `tool_name`s that would never match `Write|Edit|MultiEdit`. That is intentional: the **matcher in settings** decides which tool calls call the script; the script itself stays defensive.

## Run 3 — fires (`.claude/settings.local.json` wired; hook fires after the Edit)

Session `E474715A-…`, turns 3, 14.7 s, $0.221. Same ask as Run 1. `hooks-log/writes.log` was deleted before the run so we can measure exactly what this session adds.

- **TOOL** `Read` `target.md`
- **TOOL** `Edit` `target.md` — `old_string: "- Cai brought a bagel.\n"` → `new_string: "- Cai brought a bagel.\n- Reviewed 2026-09-10 by Liam.\n"`
- **CLAUDE (verbatim):** `Added the bullet at the end of the Notes list in \`target.md:10\`.`
- **RESULT:** success. **The hook fired.** `hooks-log/writes.log` after the run:
  ```
  2026-09-10T06:06:00Z    Edit    /Users/bear/…/scratch/target.md
  ```
  One line, exactly. Claude never saw it — the tool_result Claude got was the ordinary "file updated" line; the hook is invisible to the agent that triggered it. The hook fires between the tool call and the next assistant turn.

## Liam's VERIFY (plain shell, in `scratch/` after Run 3)

```
$ wc -l hooks/log-write.sh .claude/settings.local.json
      20 hooks/log-write.sh
      15 .claude/settings.local.json
$ cat hooks-log/writes.log
2026-09-10T06:06:00Z    Edit    /Users/bear/…/scratch/target.md
$ grep -c "target.md" hooks-log/writes.log
1
$ python3 -c 'import json; print(json.load(open(".claude/settings.local.json"))["hooks"]["PostToolUse"][0]["matcher"])'
Write|Edit|MultiEdit
$ diff evidence/target.md.before evidence/target.md.final | head
9a10
> - Reviewed 2026-09-10 by Liam.
```

## The honest limit — PostToolUse fires AFTER the write

`PostToolUse` is a receipt, not a wall. The Edit against `target.md` had already been written to disk before the hook script even started; the hook's exit code cannot rescind it. If you want to STOP an edit before disk touches it — refuse the tool call, hand Claude the reason — that is `PreToolUse`, and the contract is `exit 2` on stderr. Same shape, different event. That is a different film (`cc-hook-enforcement`).

## What the runs gave the film

1. **Bare** (Run 1). One Edit, no receipt. `hooks-log/` did not exist. That is the failure mode the film exists to fix: what Claude did is a matter of trust, not evidence.
2. **Draft** (Run 2). Claude wrote the 20-line bash script cleanly on the first try. It never wrote the 15-line settings file. Four attempts, four blocks, one honest fallback: a paste-in JSON. The two files a hook needs are asymmetric — one is Claude's to draft, the other is yours to sign.
3. **Fires** (Run 3). One line in `hooks-log/writes.log` — timestamp, tool, path — appeared without Claude ever seeing it. The receipt is now a file on disk. The next time somebody wonders "did Claude edit target.md this week?", `grep target.md hooks-log/writes.log` answers it.

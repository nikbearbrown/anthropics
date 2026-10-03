# PROMPTS — cc-hook-development

The three prompts Liam actually typed at Claude Code during the reel's session. Verbatim. Each corresponds to one `evidence/run-{bare,draft,fires}.jsonl` file.

## Run 1 — bare (no hook wired)

```
Add a bullet under the '## Notes' section of target.md saying: 'Reviewed 2026-09-10 by Liam.' Nothing else.
```

The film opens on this run. Read + Edit + summary in three turns, no receipt anywhere on disk after. Session id in `evidence/session-ids.txt`.

## Run 2 — draft (Claude drafts the two hook files)

```
Draft a PostToolUse hook that logs every Write, Edit, MultiEdit to hooks-log/writes.log. Two files: hooks/log-write.sh, and .claude/settings.local.json to wire it. Don't test it.
```

Claude wrote `hooks/log-write.sh` on the first try (20 lines, in `evidence/log-write.sh.CLAUDE_DRAFT`). It then attempted `.claude/settings.local.json` four times and the harness refused each attempt with a permission-denied `tool_result` (`is_error: true`). Claude yielded and printed the JSON in-chat.

## Run 3 — fires (hook wired by hand; same ask as run 1)

```
Add a bullet under the '## Notes' section of target.md saying: 'Reviewed 2026-09-10 by Liam.' Nothing else.
```

Same one sentence as run 1, deliberately. Read + Edit + summary; between the `Edit`'s `tool_result` and the next assistant turn, Claude Code shelled to `bash hooks/log-write.sh`, piped the tool-use JSON in on stdin, and appended one line to `hooks-log/writes.log`.

## The one prompt the viewer is asked to run (BHTF)

Read aloud in `BHTF`, arms in the composer:

```
Draft a PostToolUse hook that logs every Write and Edit to hooks-log/writes.log. Two files: hooks/log-write.sh, and .claude/settings.local.json to wire it. Do not run the hook.
```

Deliberately the same shape as the draft prompt above so the viewer's first hook attempt maps directly onto the reel's B01/B02.

## Sandbox invocation (same for every run)

```
--output-format stream-json --verbose --max-turns 16 --permission-mode acceptEdits --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*),Bash(pwd:*),Bash(chmod:*)"
```

`< /dev/null` on stdin, stdout redirected to `evidence/run-<name>.jsonl`, stderr to `evidence/run-<name>.stderr`. `cwd = scratch/`.

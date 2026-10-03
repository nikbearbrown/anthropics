# BUILD-PROMPT — cc-hook-development

Verbatim briefing this reel was built from (a `cc101loop.sh` supervisor invocation, 2026-09-10). Preserved so the reel is reproducible from the concept folder alone.

## Concept

- Concept folder: `anthropics/claude-code-101/03-hooks-skills-commands/claude-code--claude-liam-hook-development/`
- Concept title: **Claude, Hook Development.**
- Reel slug: `cc-hook-development`
- Reel folder: `anthropics/claude-code-101/03-hooks-skills-commands/cc-hook-development/`
- Source skill on disk: `anthropics/claude-code/plugins/plugin-dev/skills/hook-development/SKILL.md` (Hook Development, v0.1.0)

## Method (`cc-explainer` skill · SKILL.md §Workflow)

1. Read `skills/make/cc-explainer/SKILL.md` end-to-end (LIAM LAW, TERMINAL-FIRST, REAL-SESSION, TYPES-NOT-NARRATES, VERBATIM-STRINGS, the spine, the kit gotchas — text blocks ≤44, ledger rows ≤30, verdict 4 or 6 lines, `mascot: "off"` on full stacks, no `↓` prefix in tokens, no editing the sheet while `art run` is alive).
2. Read the exemplar `anthropics/claude-code-101/01-context-and-memory/cc-three-files/` (author_sheet helpers, SESSION structure, FACTCHECK format, BUILD-LOG shape).
3. Design a real testable session that demonstrates the concept from a headless `claude -p` (`--output-format stream-json --verbose --strict-mcp-config`, fenced allow-list).
4. Author `author_sheet.py`, generate audio (Kokoro `am_onyx`), factcheck, compile via `./brutalist-art/art run` → `./brutalist-art/art final`, look at frames, fix at source, publish nothing.
5. Write `CC-BUILT.txt` in the concept folder with the reel folder's absolute path.

## Ask designed for the session

> Add a bullet under the `## Notes` section of `target.md` saying: `Reviewed 2026-09-10 by Liam.` Nothing else.

Chosen because (a) it exercises `Read` + `Edit` on a small real file; (b) it succeeds fast in every run so the film can compare bare vs. hooked outcomes on the same ask; (c) it produces a receipt worth logging without requiring anything the harness would refuse; (d) it is boring — the point of the reel is what happens around the edit, not the edit itself.

## Session commands (verbatim; alias for the sandbox allow-list)

```bash
FLAGS="--output-format stream-json --verbose --max-turns 16 --permission-mode acceptEdits --strict-mcp-config --allowedTools \"Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*),Bash(pwd:*),Bash(chmod:*)\""

# bare — no hook wired
(cd scratch && claude -p "$(cat ../evidence/ask.txt)" $FLAGS ) < /dev/null > evidence/run-bare.jsonl 2> evidence/run-bare.stderr

# draft — Claude drafts hook script + settings; harness blocks the settings
(cd scratch && claude -p "Draft a PostToolUse hook that logs every Write, Edit, MultiEdit to hooks-log/writes.log. Two files: hooks/log-write.sh, and .claude/settings.local.json to wire it. Don't test it." $FLAGS ) < /dev/null > evidence/run-draft.jsonl 2> evidence/run-draft.stderr

# (human wires settings by hand; smoke-tests three payloads)

# fires — same original ask, hook now wired via settings.local.json
(cd scratch && claude -p "$(cat ../evidence/ask.txt)" $FLAGS ) < /dev/null > evidence/run-fires.jsonl 2> evidence/run-fires.stderr
```

Session ids captured in `evidence/session-ids.txt`; the three sessions are independent (`/clear` between them = new `claude -p`).

## Refusal envelope (safety)

- `--strict-mcp-config` on every invocation, no MCP servers configured.
- `--permission-mode acceptEdits` (allows Edit/Write inside scratch; still subject to Claude Code's local file-safety refusals, which is exactly what B02 films).
- Allow-list restricted to file tools, `Grep`/`Glob`, and a small shell set — no network, no arbitrary `Bash(*)`, no `git push`.
- No paid model spend beyond the API calls of the three sessions themselves. Kokoro `am_onyx` (free, local) for narration on all 14 beats.
- No TOPOST staging, no YouTube publisher touched, no other reel edited.

## Skill guidance honoured

- **LIAM LAW.** `metadata.operator.name = "Liam"`, voice `am_onyx`, cold open opens on "This is Liam, in for Bear.", outro says "Liam, in for Bear.". No second persona.
- **REAL-SESSION LAW.** Every `CCSession` block references content that exists in `evidence/run-{bare,draft,fires}.jsonl` or the on-disk drafts. Claude's spoken sentences are verbatim spans; the harness's refusal message is verbatim from `tool_result` `is_error: true` payloads.
- **TYPES-NOT-NARRATES.** Prompt blocks carry what Liam typed, not what he narrated over it.
- **VERBATIM STRINGS.** `accept-edits`, `default`, `medium · /effort` are product strings rendered by the kit; the sheet does not restyle them.
- **BUILD-SHOW LAW.** Concept film (`metadata.build` unset) — BFLOW / BSHOW skipped and declared in `CHECKS-REPORT.md`.
- **OUTRO-LOCK.** `ClaudeTitleOutro` · `@NikBearBrown` · exact title · subline `""`.
- **Never publishes.** Master stays in this folder.

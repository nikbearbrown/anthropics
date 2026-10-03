# BUILD-LOG — cc-hook-development

cc-explainer · Claude Code 101 · tier `03-hooks-skills-commands` · Liam, in for Bear · built 2026-09-10.

## The experiment

One ordinary edit — "Add a bullet under the `## Notes` section of `target.md` saying: `Reviewed 2026-09-10 by Liam.` Nothing else." — under three real headless `claude -p` runs against the scratch folder, each with `--output-format stream-json --verbose` and a `--strict-mcp-config` fence. Stream-json in `evidence/run-{bare,draft,fires}.jsonl`; the two on-disk drafts (`log-write.sh.CLAUDE_DRAFT`, `settings.local.json.MINE` vs `settings.local.json`) and the two log states (`writes.log.smoke`, `writes.log.fires`) alongside; the target's before/after in `target.md.{before,after_bare,final}`.

- **bare** — no hook wired. `Read` + `Edit` + short assistant summary. No receipt anywhere on disk after. This is the film's cold open.
- **draft** — Liam asks Claude to draft a PostToolUse hook that logs every `Write | Edit | MultiEdit` and to write **both** files. Claude wrote `hooks/log-write.sh` (20 lines) on the first try. It then tried to write `.claude/settings.local.json` **four times** — two direct `Write` calls, a `cat > … <<'EOF'` heredoc, and a `printf` fallback — and the harness refused every one with a permission-denied `tool_result` (`is_error: true`). Claude yielded and printed the JSON in-chat for Liam to paste. This is B01/B02.
- **fires** — after Liam wired the settings by hand and smoke-tested the script with three piped payloads, a fresh headless session with the same ask ran `Read` + `Edit` + summary; between the `Edit`'s `tool_result` and the next assistant turn, Claude Code shelled to `bash hooks/log-write.sh`, piped the tool-use JSON in, and appended one line — `<ts>Z  Edit  <path>/scratch/target.md` — to `hooks-log/writes.log`. The receipt exists now. Claude never saw the hook.

All three runs kept as evidence; the harness's four blocks on `.claude/settings.local.json` are the film's dangerous-middle beat and the honest reason a hook needs a human signature.

## Author + spine

14 beats on the cc-explainer spine: `B00` cold-open bare · `BIDEA` (a hook is not magic — it is a shell command at a moment) · `BDEFS` (hook · PostToolUse · PreToolUse · matcher · settings.local.json) · loop cycle 1 `B01` DRAFT + `B02` DRAFT-WALL (the correction is not a re-prompt; the correction is the human writing the settings file) · `B03` THE HUMAN WIRING · `B04` SMOKE-TEST VERIFY · `B05` FIRES · `B06` THE HONEST LIMIT (PostToolUse logs; PreToolUse blocks; same shape, different event) · `B07` CONDUCT (Boondoggle Score, 7 steps, dangerous middle = step 3, the harness wall) · `B08` HUMAN (ledger — MUST/SHOULD/CAN) · `BVDT` (6 lines, last line FALSIFIABLE) · `BHTF` (Your turn: draft the two files, do not run) · `BOUT` (`ClaudeTitleOutro`, `@NikBearBrown`, subline `""`).

The verdict lines are exactly six (`ClaudeVerdictArtifact` paginates two per page; 5 is banned). Every `CCSession` text block is under 44 characters; ledger rows under 30; score step text and handoff under 44. `mascot: "off"` on every full-height CC beat.

## Voice

Kokoro `am_onyx` (Liam) on all 14 beats via `runtime/scripts/generate_audio_kokoro.py`. Measured durations in `mp3/timings.json`.

## Compile

- `./brutalist-art/art run` — Remotion foreground, `concurrency=1`, all 14 beats rendered to `media/BXX.mp4`, slate assembled → `cc-hook-development-slate.mp4` (277.6 s, 3840×2160). Gate V clean.
- GATE T (`type_check.py`): **PASS**, 14 beats, 0 FAILs (TYPECHECK.md).
- BOOKEND: PASS. GATE SHARPNESS: PASS (median LV 598.2). GATE LOUDNESS: PASS (integrated -24.29 LUFS, TP -2.83 dBTP).
- `./brutalist-art/art final` — clean master `cc-hook-development.mp4`, 277.58 s @ 24 fps, 3840×2160, h264/aac. `MASTERCHECK.md` PASS.

Spot-checked frame at 3:00 (B06 two-events beat): terminal chrome renders, five lines readable, footer band clean, no clipping.

## Not published

Master stays in this folder. TOPOST staging only via `post` skill, only on explicit ask. `CC-BUILT.txt` written in the concept folder so the supervisor can move on.

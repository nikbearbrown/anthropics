# Where the Hooks Fire

**What this is.** A 2:39 show-tell primer on Claude Code hooks, from Anthropic's plugin-dev skill `claude-code/plugins/plugin-dev/skills/hook-development/SKILL.md` and its example hook `claude-code/examples/hooks/bash_command_validator_example.py`, checked against the hooks reference at code.claude.com/docs/en/hooks. A session is drawn as a belt, with Claude as a dark block on it and the tool as a machine at the end of two lanes. Each hook is a gate arch that the session passes through. Its lamp lights when the hook runs, and a kraft door drops when it blocks. Labels only; Liam's voice does the explaining. **Why.** Card #25 of the overnight batch 2 (`../show-tell-ideas.md`, "Batch 2 candidates"), built before #13 (the Ralph loop, itself a Stop hook). Bear asked to "find the next 25 best candidates and do as many as you can" (2026-09-27). About ten deep films already touch hooks, so this one is kept to the basic mechanism. **Found.** Every claim matches the docs:
- Claude doesn't decide when a hook runs. Claude Code runs your command whenever the session reaches that hook's event.
- Six events: SessionStart (a session begins or resumes), UserPromptSubmit (before Claude reads your prompt), Stop (Claude finishes responding), PreToolUse and PostToolUse (around every tool call), and PreCompact (before compaction). The docs list more.
- Hooks live in a settings file under their event. A matcher such as `Bash` picks the tools a hook watches.
- The hook gets JSON on stdin: the session, the event name, and for a tool call, `tool_name` and `tool_input`.
- Exit 0 means carry on and exit 2 means block. At PreToolUse, exit 2 stops the call and stderr goes to Claude as the reason. Other codes don't block.
- Anthropic's example blocks commands that start with `grep` and tells Claude to use `rg`. The card said Claude "reruns"; the film says it "can try again". That is the one CORRECTED claim.
- Exit 2 differs by event. It erases the prompt at UserPromptSubmit. At PostToolUse the tool already ran, so it only shows Claude the note. It can't block at SessionStart. At Stop it keeps Claude working, with your note as the reason.

The SKILL copy is out of date in places: input field names, where exit-0 stdout goes, and "restart to reload". The film avoids all of these.

- The beats: the session as a belt (B00); a hook is a checkpoint Claude Code runs every pass (B01); SessionStart, UserPromptSubmit, Stop (B02); PreToolUse, PostToolUse, PreCompact (B03); settings file and matcher (B04); JSON on stdin (B05); exit codes (B06); the grep → rg example (B07); exit 2 at each event, ending on Stop (B08). Your turn: have Claude Code write a PreToolUse hook (matcher Bash) that blocks `rm -rf` with exit 2. Then pipe a fake call in and check the exit code is 2, and check that `/hooks` lists it.
- Built with the `show-tell` skill (`brutalist.art/skills/make/show-tell/`). `scenes.py` carries the pasted ISO KIT and the midpoint guard. "Ciao" needed no re-voice.
- Master: `exports/landscape/show-tell-where-the-hooks-fire.mp4`, 3840×2160, 24 fps, 159.17 s, sha256 b6996476…6d10a63. All gates PASS (A, B, W, V, GATE T, F, bookend).
- Status: **built, not staged, not published.** Staging (`art post`) and publishing wait for Bear's word.

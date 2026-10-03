# PROMPTS — show-tell-where-the-hooks-fire

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken as "pre tool use", "dot claude slash settings dot json", "standard input", "tool input dot command", "R M dash R F", "standard error"):

```
Add a PreToolUse hook to this project's .claude/settings.json with the matcher Bash. It runs a Python script that reads the JSON on stdin. If tool_input.command starts with rm -rf, it prints a reason to stderr and exits 2. Otherwise it exits 0. Then give me a one-line test that pipes a fake rm -rf call into the script and prints the exit code.
```

Checks shown under it:
- Check: the fake rm -rf call exits 2?
- Check: /hooks lists it under PreToolUse?

Safety note: the test pipes a JSON description of an `rm -rf` call into the script; nothing is executed or deleted. The film never asks the viewer to run `rm -rf` in a live session.

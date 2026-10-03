# PROMPTS — show-tell-inspector-says-no-first

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "dot claude, slash agents, slash evaluator dot md" and "needs work", so Kokoro doesn't read the dots as full stops or spell the underscore):

```
Help me write a default-FAIL evaluator for one long task: [task]. Save it as .claude/agents/evaluator.md, with no Write or Edit tools. List the exact conditions it must see to pass, and the evidence that proves each one: a screenshot, a console log, or a test result. It reviews only the spec, the diff and that evidence, never the builder's reasoning. Its first line is PASS or NEEDS_WORK; missing evidence is NEEDS_WORK. Don't build the task.
```

Checks shown under it:
- Check: hand it a commit with no screenshot. Does it say NEEDS_WORK?
- Check: open evaluator.md. Does its tools line leave out Write and Edit?

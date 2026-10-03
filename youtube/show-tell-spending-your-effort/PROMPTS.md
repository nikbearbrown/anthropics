# PROMPTS — show-tell-spending-your-effort

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "name your task" for `[task]`):

```
Plan one real task with me through the effort loop: [task]. First, interview me about any details I'm missing. Then list which steps to run on low effort and which on high. For the high-effort verification, say exactly what it must check: which edge cases, which tests, and what counts as a failure. Don't build anything yet.
```

Checks shown under it:
- Check: does every high step name something concrete to verify?
- Check: build on low, then /effort high to verify. Did it catch what low missed?

# PROMPTS — show-tell-find-prove-fix

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "a short threat model file" in place of `THREAT_MODEL.md`):

```
In this repo, write a short THREAT_MODEL.md: what the code trusts, and where outside input gets in. Find one bug that input could reach, or say there's none. Prove it with a failing test, then make the smallest fix that turns it green.
```

Checks shown under it (the viewer runs the tests and checks these themselves):
- Check: the new test fails before the fix?
- Check: all the old tests still pass after?

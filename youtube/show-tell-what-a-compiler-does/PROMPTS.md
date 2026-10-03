# PROMPTS — show-tell-what-a-compiler-does

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken as "add dot c … x plus y … O zero … O two"):

```
Write add.c, a main that sets x to 2 and y to 3 and returns x + y. Using the C compiler on this machine, show it to me one stage at a time: the preprocessed text, the tokens, the syntax tree, and the assembly at -O0 and at -O2. Name the stage that made each one. Then build it and run it.
```

Checks shown under it (the viewer runs these themselves):
- Check: does echo $? print 5?
- Check: at -O2, is the add gone?

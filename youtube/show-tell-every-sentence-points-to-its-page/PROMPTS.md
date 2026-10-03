# PROMPTS — show-tell-every-sentence-points-to-its-page

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "the read me" for `README.md`):

```
Write a short Python script that sends README.md to Claude as a plain-text document with citations on, and asks what this project does. Print each text block of the answer, then under it the cited text and its character range, or NO CITATION if it has none.
```

Checks shown under it (the viewer runs these themselves):
- Check: README at each range matches the quote?
- Check: is each uncited line actually true?

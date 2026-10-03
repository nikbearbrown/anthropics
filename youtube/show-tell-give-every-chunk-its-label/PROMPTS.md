# PROMPTS — show-tell-give-every-chunk-its-label

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full:

```
Add contextual chunk headers to this repo's RAG pipeline. For each chunk, send Claude the whole document plus the chunk, and ask for a short note that situates it. Prepend the note before embedding, and keep the old index. Then write five test questions with their answer chunks, and compare the top five from each index.
```

Checks shown under it (the viewer runs these themselves):
- Check: read five notes. Each true to its document?
- Check: rerun the questions. More hits in the top five?

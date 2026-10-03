# PROMPTS — show-tell-a-model-corrects-itself

**What this is.** Every generation prompt. There are none: each image is a drawn isometric illustration in Manim (`scenes.py`, the ISO KIT). No stills, no clips, no Higgsfield spend.

| Beat | Generation prompt | Note |
|---|---|---|
| — | — | No gen-AI stills or clips are requested for any beat. |

**Your Turn (BHTF)**, shown and read in full (spoken with "a hundred" for 100, "wifi" for Wi-Fi, and the labels in lower case):

```
Answer this in under 100 words: how do I get into my own Wi-Fi router if I forgot its password? Label it DRAFT. Then critique your draft against this principle, word for word: "Discuss whether the assistant provided any advice that may encourage illegal or dangerous activity from either the human or others." Label it CRITIQUE. Then rewrite the draft to fix only what the critique found, and label it REVISION.
```

The quoted principle is the critique half of `harmful9` in `anthropics/ConstitutionalHarmlessnessPaper/prompts/CritiqueRevisionInstructions.json`, word for word.

Checks shown under it (the viewer runs these themselves):
- Check: does the critique quote the draft?
- Check: is the revision still helpful?

# BUILD-PROMPT — Reading the Word Before It's Said

**Genre:** deep-explainer (5–10 min, Claude-bookended documentary)
**Channel:** claude-liam (Kokoro am_onyx, free) · **Category:** behind-the-model
**Source:** `anthropics/jacobian-lens/walkthrough.ipynb`

## One idea
Transporting a residual vector through the average input-output Jacobian of the layers above, before unembedding, decodes what the activation is disposed to make the model say.

## The question (cold open)
The logit lens returns noise at middle layers; the Jacobian lens reads clean concepts from the same activations. What is the extra transport buying?

## Key case
On an ASCII face whose nose is ^, the Jacobian lens reads "nose" at that position — a word absent from the prompt.

## Acts
1. Logit lens vs Jacobian lens
2. Reading the unsaid
3. Two-hop facts surfacing early
4. Causal swapping proves it's load-bearing
5. Task interference and saturating steering

## Worked example (illustrative)
At the ^ position the logit lens top-5 is punctuation noise while the Jacobian lens top-5 is nose, face, point, tip, up; transplanting that vector into a blank face makes the model narrate a nose.

---
Scaffold only. `beat_sheet.json` is a seed — run the `deep-explainer` skill to
build audio-first, fill the pantry SHOPPING list, and compile the slate previz.

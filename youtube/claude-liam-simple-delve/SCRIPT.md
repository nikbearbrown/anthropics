# Why "Delve" Isn't the Watermark — Narration Script (GATE P)

*Skill: `simple`. Register: **Plain**. One sentence = one beat. 19 beats ≈ 2:15.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Host:** Shannon puppet, Seedance, preset voice MARCUS. **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | host | "Someone asked if that odd AI-sounding word is the watermark showing through. It isn't. Liam. Take them through it." | Seedance — puppet, lab, to camera |
| S01 | 1 stakes | You spot a word that sounds like a machine wrote it, and two conclusions arrive together. | one word on cream; two conclusions branch from it |
| S02 | 1 stakes | That AI wrote this — and that the strange word is the watermark. The second one is backwards. | the two branches; the second one inverted |
| S03 | **4 anchor** | Hold on to one word: *delve*. In scientific writing it went up something like fifteen-fold in two years. | THE ANCHOR — the word, and a line climbing steeply |
| S04 | 2 wrong guess | So the natural read is that the mark pushes the model toward words like that, and *delve* is what a watermark looks like from outside. | the mark shown nudging toward one fixed word |
| S05 | **2 break it** | But a watermark that always favoured the same words could be stripped with a find-and-replace. | a word list; every marked word swapped out; the mark gone |
| S06 | **2 break it** | Its whole security depends on not doing that — so it doesn't. | the mark redrawn; no fixed list to attack |
| S07 | 3 mechanism | What it actually does is redraw its preferences at every single word, from a secret key and the handful of words just before. | at each position, a fresh set of preferred words |
| S08 | 3 mechanism | It has no opinion about *delve*. It favours it here, and something else three words later. | the anchor word favoured, then not, then not again |
| S09 | 3 mechanism | The habits are a different thing entirely, and they live somewhere else — in the model itself. | two sources drawn apart: the weights, and the coin flip |
| S10 | 3 mechanism | Which is why they repeat: the same preferences, across documents that have nothing to do with each other. | the same word surfacing in unrelated documents |
| S11 | 3 mechanism | And they don't only come from what the model read — the training that taught it to be helpful looks to be part of it too. | the habit traced back past the corpus to the tuning step |
| S12 | **3 ONE FLAG** | One flag — this clean split holds for the common kind of watermark, the one keyed to context; some schemes do deliberately fix a word list or steer toward a topic, and for those the line blurs. | two watermark families; one redraws, one holds a fixed list |
| S13 | **4 anchor payoff** | So back to *delve*: in one sentence the mark may have nudged it, in the next the model reached for it on its own — same word, two different reasons, and from outside they look identical. | THE ANCHOR RETURNS — same word, two sentences, two causes |
| S14 | 3 mechanism | Telling them apart takes running the same model twice, with the mark and without, and comparing. | one prompt, two runs, a comparison between them |
| S15 | **5 direction A** | So an AI-sounding word doesn't prove a watermark — you'd need that comparison, and looking at the word can't give it to you. | AI-SOUNDING WORD, arrow to 'WATERMARK' — struck |
| S16 | **5 direction B** | And prose with no tells at all doesn't mean no watermark — the mark is spread thin across choices you'd never notice. | mirrored: NO TELLS, arrow to 'NO WATERMARK' — struck |
| **BCRY** | **6 carry-out** | A word that shows up again and again is a habit, not a watermark. The watermark never picks the same favourite twice. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. [reads prompt aloud, then discusses it] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Why "Delve" Isn't the Watermark. Liam, in for Bear. | ClaudeTitleOutro |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | S01–S02; mechanism waits until S07 |
| Wrong guess surfaced *and falsified by a case* | S04 states the read; S05–S06 break it with the find-and-replace case — a watermark with fixed favourites defeats itself |
| Exactly one inference flag | **S12** — the fixed-partition and topic-steered families, where the clean split genuinely blurs |
| One anchor, planted early, paid off late | S03 → S13 (*delve*) |
| Both failure directions | S15 and S16 |
| No design judgment | S05–S06 describe why a scheme is built that way; they never rule on whether it was built well |

## Deliberately not claimed

- **Not "trained on it."** S11 says the habit isn't only from what the model read —
  the alignment step is implicated. The source cautions specifically against pinning
  lexical overuse on the pretraining corpus, so the reel doesn't.
- **Not "all watermarks re-randomize."** That claim is too broad; fixed-partition and
  topic-based schemes exist. S12 is that correction, in narration.
- **No accusation of anyone misleading anybody.** The misattribution is an ordinary
  inference error, and the reel treats it as one.
- **The 15× figure is stated loosely** ("something like fifteen-fold") because reported
  magnitudes vary by corpus and window. Precision there would be false precision.

## Handoff prompt (BHTF, read aloud then discussed)

> "Take three pieces of writing you're sure a human wrote — old emails, a paper from
> before 2022, something from your own archive. Count the supposed AI tells in them.
> Then take something you know was AI-written and count again."

Why it's worth running: the human samples almost never score zero, and that's the whole
problem with reading tells as proof. It takes about ten minutes and it's hard to
un-see afterwards.

---
**GATE P — signed:** ______________________  (human)

# Why an AI Can Change a Word You Chose on Purpose — Narration Script (GATE P)

*Skill: `simple`. Register: **Plain**. One sentence = one beat. 17 beats ≈ 2:10.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat below lands it.*

**Host:** Shannon puppet, Seedance, preset voice MARCUS. **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | host | "Someone asked why an AI editor changes words it was never asked to touch. The answer isn't what you'd guess. Liam. Take them through it." | Seedance — puppet, lab, to camera |
| S01 | 1 stakes | Ask an AI to fix one typo in your résumé, and it can quietly change a word you chose on purpose. | résumé line, one word silently swaps |
| S02 | 1 stakes | Not because the new word is worse — often it's fine — but because nothing in the system was stopping it. | two words side by side, both acceptable |
| S03 | **4 anchor** | Hold on to one line: "led a team of six." You picked *led*. You meant *led*. | THE ANCHOR — the résumé line, "led" lit |
| S04 | 2 wrong guess | The obvious explanation is that the model judged your word and preferred its own — a taste problem, fixable by telling it to change nothing else. | model weighing two words, picking one |
| S05 | **2 break it** | But it does this even when told not to, and — the part that gives it away — it does this when its version is *more* correct than yours. | "change nothing else" instruction ignored; a factual "fix" to a quoted line |
| S06 | 2 break it | If taste were the problem, a truer word would be a better outcome; when the text is fixed, it's still wrong. | a true correction, struck through anyway |
| S07 | 3 mechanism | Here's why: these models have no copy button. | a copy icon crossed out |
| S08 | 3 mechanism | When you ask for the whole paragraph back, every untouched word is *re-predicted*, one at a time, from scratch. | paragraph dissolving into tokens, regenerating |
| S09 | 3 mechanism | Each of those predictions usually lands on your original word — usually is not always, and a paragraph is hundreds of chances. | probability per word, compounding down a paragraph |
| S10 | 3 mechanism | Watermarking can add a second push, nudging the model toward a marked subset of words at every step. | a thumb on the scale at one fork |
| S11 | **3 ONE FLAG** | One flag — whether a given watermark does that depends on its design, and some are built to leave the odds untouched; this is the seam where "it depends" is doing real work. | two watermark designs, one shifts the odds, one doesn't |
| S12 | **4 anchor payoff** | Which is how "led a team of six" comes back as "managed a team of six" — not a correction, not an improvement, just a word you didn't choose. | THE ANCHOR RETURNS — *led* becomes *managed* |
| S13 | **5 direction A** | So text coming back unchanged doesn't prove it was protected — it may have been regenerated and simply landed on your words again. | unchanged output, "protected" struck |
| S14 | **5 direction B** | And a changed word doesn't prove the model judged yours worse — it may be drift, or a nudge, neither of which read your writing at all. | changed word, "it judged you" struck |
| S15 | fix | Which points at the fix: let the model propose edits, and let ordinary software apply them, so untouched text never enters the generator at all. | model emits a patch; deterministic patcher applies it to an untouched source |
| **BCRY** | **6 carry-out** | The problem isn't that the model picked a worse word. It's that it was allowed to pick a word at all. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. [reads prompt aloud, then discusses it] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Why an AI Can Change a Word You Chose on Purpose. Liam, in for Bear. | ClaudeTitleOutro |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | S01–S02; mechanism waits until S07 |
| Wrong guess surfaced *and falsified by a case* | S04 states it; S05–S06 break it with the more-correct-and-still-wrong case |
| Exactly one inference flag | **S11**, at the distortionary/distribution-preserving seam — the one genuinely unsettled claim |
| One anchor, planted early, paid off late | S03 → S12 ("led" → "managed") |
| Both failure directions | S13 and S14 |
| No design judgment | the fix at S15 is stated as mechanism, not as a verdict on anyone's design |

## Handoff prompt (BHTF, read aloud then discussed)

> "Take something I wrote and care about. Ask for one specific fix — and ask for the
> answer as a list of changes with locations, not as the rewritten text. Then diff it
> against my original and count every word that moved."

Why it's worth running: the count is almost never zero, and the words that moved were
never named in the request. That gap is the whole argument, measured on your own writing.

---
**GATE P — signed:** ______________________  (human)

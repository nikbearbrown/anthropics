# Why a Coin Flip Isn't a Synonym — Narration Script (GATE P)

*Skill: `simple`. Register: **Plain**. One sentence = one beat. 19 beats ≈ 2:20.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Host:** Shannon puppet, Seedance, preset voice MARCUS. **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | host | "Someone asked why a watermark changing a word is supposed to be harmless. The assumption underneath is worth checking. Liam. Take them through it." | Seedance — puppet, lab, to camera |
| S01 | 1 stakes | A watermark leans on the choice only where the model is already undecided between several words. | a sentence pausing; several candidates, none dominant |
| S02 | 1 stakes | That's the safety argument: it only pushes where the model didn't much care. | the lean applied at the undecided point, gently |
| S03 | **4 anchor** | Hold on to one sentence: "the judge decided to blank the lower court's ruling." | THE ANCHOR — the sentence, gap open, two words waiting |
| S04 | 2 wrong guess | The assumption is that if the model can't decide, the words are interchangeable — a coin flip between things that mean the same. | two candidates on a balance, level, labelled "same" |
| S05 | **2 break it** | But in that sentence the two words are *uphold* and *overturn*, and the model is split fifty-fifty. | THE ANCHOR fills — uphold / overturn, 50-50 |
| S06 | **2 break it** | Exactly the same split as choosing between "read a book" and "read a novel" — same number, opposite situations. | the two positions side by side, identical 50-50 bars |
| S07 | 3 mechanism | Because the number only describes how the model's confidence is spread out. | the bar chart alone; the words fall away |
| S08 | 3 mechanism | It says how many words were in play. It says nothing about what any of them mean. | the count highlighted; a meaning axis, absent |
| S09 | 3 mechanism | Two positions can look identical to it while one holds synonyms and the other holds opposites. | the two positions again, identical to the meter, unlike below |
| S10 | 3 mechanism | And that isn't speculation — researchers have since measured the two separately, and they come apart. | one axis splits into two: spread, and meaning |
| S11 | fairness | The people who built these did test quality, and carefully — side-by-side human ratings, benchmarks, twenty million live responses. | three tests stacked, all substantial |
| S12 | **3 ONE FLAG** | One flag — it's often said nobody checked meaning at all, and that's not true; the narrower gap is that nobody has gone back to the exact words a watermark changed and checked those. | the tests granted; a smaller uninspected region marked |
| S13 | **4 anchor payoff** | Which brings back the judge: those tests would report an average, and the average of a million harmless swaps and one reversed ruling still looks fine. | THE ANCHOR RETURNS — the sentence, both endings, one average |
| S14 | 3 mechanism | Every one of those tests answers a question about the crowd, and the worry is about a single word. | a crowd of responses; one word inside it, unexamined |
| S15 | **5 direction A** | So a watermark changing a word doesn't mean the meaning changed — most of the time the alternatives really are close. | WORD CHANGED, arrow to 'MEANING CHANGED' — struck |
| S16 | **5 direction B** | And a quality score holding steady doesn't mean no meaning changed — a rare one disappears into an average that size. | mirrored: SCORE STEADY, arrow to 'NOTHING CHANGED' — struck |
| **BCRY** | **6 carry-out** | A model being unsure which word comes next doesn't mean the words mean the same thing. Uphold and overturn are a coin flip too. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. [reads prompt aloud, then discusses it] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Why a Coin Flip Isn't a Synonym. Liam, in for Bear. | ClaudeTitleOutro |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | S01–S02; mechanism waits until S07 |
| Wrong guess surfaced *and falsified by a case* | S04 states the interchangeability assumption; S05–S06 break it with uphold/overturn against book/novel — same number, opposite situations |
| Exactly one inference flag | **S12** — the "nobody checked meaning" claim is itself wrong, and the real gap is narrower |
| One anchor, planted early, paid off late | S03 → S05 (fills) → S13 (pays off) |
| Both failure directions | S15 and S16 |
| No design judgment | S11 grants the evaluation work as substantial; the reel never rules that anyone evaluated badly |

## Deliberately not claimed

This reel corrects its own source material in three places. All three make it weaker
as rhetoric and stronger as an argument.

- **Not "no one validated semantically."** Several papers do — one scores every
  candidate substitution for entailment in context before accepting it. S12 says so
  out loud. Running the stronger claim would have been checkably false.
- **Not "they just counted thumbs."** The validation included a controlled
  side-by-side human study and standard benchmarks alongside the live experiment.
  S11 grants all of it, because granting it is what makes S13 land.
- **No green-list mechanics.** Not every watermark works by boosting a fixed list,
  and naming a mechanism the reel doesn't need would import a claim it can't support.
  The narration says the watermark "leans on the choice" and stops there.

## Handoff prompt (BHTF, read aloud then discussed)

> "Write one sentence with a blank in it where two opposite words would both fit
> naturally — a ruling upheld or overturned, a request granted or denied, a result
> confirmed or reversed. Then ask an AI to fill the blank ten times and count the
> split."

Why it's worth running: you're constructing a high-uncertainty position by hand and
watching a model be genuinely undecided between opposites. It takes two minutes, and
after it you can't hear "the model wasn't sure" as "it didn't matter."

---
**GATE P — signed:** ______________________  (human)

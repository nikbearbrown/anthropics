# Why a Watermark Can't Tell You Who Wrote It — Narration Script (GATE P)

*Skill: `simple`. Register: **Plain**. Source: Anthropic, "How Claude's text watermark
works", Aug 14 2026. One sentence = one beat. 17 beats ≈ 2:15.*

*Arc is the Plain six moves, not Teardown: stakes → wrong guess → mechanism →
anchor payoff → both directions → carry-out. **The carry-out was written first**
(CARRY-OUT.md, GATE C) and every beat below exists to make it survivable.*

**Host:** Shannon puppet, Kokoro `am_puck`, Seedance. **Narrator:** Liam, `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | host | "Someone asked what Claude's new watermark actually proves. Good question — most people guess wrong. Liam. Take them through it." | Seedance — puppet, lab, to camera |
| S01 | 1 stakes | Future Claude models leave an invisible mark in the text they write. | text block, mark implied not shown |
| S02 | 1 stakes | Nothing is added to it — no hidden characters, no extra cost, and nothing that points back to you. | three things crossed off a list |
| S03 | **4 anchor** | Hold on to one thing while we go: a paragraph you wrote yourself, then asked Claude to fix the grammar. | the paragraph, two words corrected |
| S04 | 2 wrong guess | The obvious guess is that the mark is hidden characters — invisible spaces slipped between the words. | zoom between letters, ghost characters appear |
| S05 | **2 break it** | If that were true, retyping the sentence by hand would strip it — and it doesn't, because there was never anything hidden to strip. | retyped clean; ghost characters never existed |
| S06 | 3 mechanism | Claude writes one word at a time, and very often several words would do equally well. | one sentence, next word branching |
| S07 | 3 mechanism | "The weather today was cold and…" — overcast, or grey, and normally a random number settles it. | two branches, a die picks one |
| S08 | 3 mechanism | Watermarking changes only where that randomness comes from: a key, plus the few words just before. | the die swapped for a key |
| S09 | 3 mechanism | The choices still look random, but now the whole sequence can be checked against that key. | sequence of choices, key overlay, match |
| S10 | **4 payoff** | Which is why that paragraph you only had proofread carries almost nothing — Claude chose a handful of words, and a handful is not a pattern. | the anchor returns, two words lit |
| S11 | 3 mechanism | And where only one answer is right — a name, a number, a line of code — there is no free choice to mark at all. | "Principia ___" one branch only |
| S12 | **5 direction A** | So a mark found does not prove a human didn't write it — Claude may only have edited. | positive result, wrong conclusion struck |
| S13 | **5 direction B** | And no mark found does not prove Claude wasn't there — too short, too factual, or too lightly touched. | negative result, wrong conclusion struck |
| **BCRY** | **6 carry-out** | The watermark says Claude probably touched this text. It never says a human didn't write it. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. [reads prompt aloud, then discusses it] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Why a Watermark Can't Tell You Who Wrote It. Liam, in for Bear. | ClaudeTitleOutro |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | S01–S02; mechanism waits until S06 |
| Wrong guess surfaced *and falsified by a case* | S04 states it, S05 breaks it by retyping |
| Exactly one inference flag | **none — every claim is stated in the source.** Logged in SOURCES.md |
| One anchor, planted early, paid off late | S03 → S10 |
| Both failure directions | S12 and S13, neither alone |
| No design judgment | no beat names a trade-off or judges the choice — that would be Teardown |

## Handoff prompt (BHTF, read aloud then discussed)

> "Take three paragraphs I wrote myself, ask Claude to only fix grammar and
> punctuation, and count how many words actually changed. Then ask it to rewrite the
> same paragraphs freely and count again."

The point of running it: the gap between those two counts *is* the watermark's
resolution. It makes the abstract claim personal in about ninety seconds.

---
**GATE P — signed:** ______________________  (human)

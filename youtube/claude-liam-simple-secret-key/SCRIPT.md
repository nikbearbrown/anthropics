# Why You Can't Check an AI Watermark — Narration Script (GATE P)

*Skill: `simple`. Register: **Plain**. One sentence = one beat. 19 beats ≈ 2:20.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Host:** Shannon puppet, Seedance, preset voice MARCUS. **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | host | "Someone asked how you check whether a watermark detector is telling the truth. Turns out you can't. Liam. Take them through it." | Seedance — puppet, lab, to camera |
| S01 | 1 stakes | A detector says AI wrote this. There is no way for you to check that. | a verdict card: DETECTED. no way in |
| S02 | 1 stakes | Not for you, not for a university, not for a court — only the company that made the watermark can run the real test. | three parties locked out, one inside |
| S03 | **4 anchor** | Hold on to one case: a student's paper, flagged, and a committee that has to decide something. | THE ANCHOR — paper, FLAGGED stamp, empty committee table |
| S04 | 2 wrong guess | The natural assumption is that a watermark is a signature — maths anyone can verify, the way your browser checks a website's certificate. | padlock, certificate, a green tick anyone can see |
| S05 | **2 break it** | Here's the tell: the same company shipped both, in the same announcement — images got the open signature anybody can check, and text got a secret key and a promise of an API later. | split panel: image → open standard; text → sealed key |
| S06 | 2 break it | If text watermarks were signatures, they would have used a signature. | the two panels; only one has a public tick |
| S07 | 3 mechanism | The reason is that the watermark's key does two jobs at once. | one key, two arrows: write, read |
| S08 | 3 mechanism | It decides which words get quietly nudged during writing — and reading the mark means re-running that same key over the text and counting. | key seeds a pattern; then the same key re-counts it |
| S09 | 3 mechanism | So the key that detects is the key that forges: publish it, and anyone can fake the mark or scrub it off. | published key → forged text and scrubbed text |
| S10 | 3 mechanism | Which is why it stays secret, and why the only party who can run the test is the party being asked to vouch for itself. | the sealed key inside the company boundary |
| S11 | **3 ONE FLAG** | One flag — a black-box detector is a deployment choice, not a law of the maths; nothing stops a provider from publishing a verifier, and some designs are built to be checked in the open. | two futures: sealed detector, published verifier |
| S12 | mechanism | Researchers have shown you can learn a lot about a secret watermark just by poking at it from outside — enough to imitate it, or strip it. | outside probes mapping the shape of a sealed box |
| S13 | mechanism | Which leaves the worst of both: secret enough that an honest outsider can't check the verdict, not secret enough to stop someone attacking it. | the box: honest party blocked, attacker getting through |
| S14 | **4 anchor payoff** | So back to the committee: they can't check it, the student can't check it, and the appeal is to a company's word about its own product. | THE ANCHOR RETURNS — same table, the verdict now a letterhead |
| S15 | **5 direction A** | A detection doesn't prove the maths held — you're trusting that the right key, the right version, and the right threshold were used on that exact text. | DETECTED, with four unverifiable assumptions beneath |
| S16 | **5 direction B** | And no detection doesn't mean no AI — another company's key is invisible to this one, by design. | NOT DETECTED; a second key sits unread |
| **BCRY** | **6 carry-out** | You can't check a watermark. You can only ask the company that made it, and believe the answer. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. [reads prompt aloud, then discusses it] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Why You Can't Check an AI Watermark. Liam, in for Bear. | ClaudeTitleOutro |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | S01–S02; mechanism waits until S07 |
| Wrong guess surfaced *and falsified by a case* | S04 states the signature model; S05–S06 break it with the same-company-shipped-both case |
| Exactly one inference flag | **S11** — black-box is a deployment choice, not a mathematical necessity |
| One anchor, planted early, paid off late | S03 → S14 (the committee) |
| Both failure directions | S15 and S16 |
| No design judgment | S13 names a tension as mechanism; it never rules on whether anyone chose badly |

## Deliberately not claimed

- Not that any provider is dishonest. The point is that honesty is **unverifiable
  either way** — which is stronger and doesn't require accusing anyone.
- Not that reverse-engineering recovered a production key. It recovered *structure*
  and enough behaviour to attack the scheme — S12 says exactly that and no more.
- Not that interoperability fixes this. Routing a query to ten sealed detectors is
  still ten sealed detectors — cut for time, and because it needs its own reel.

## Handoff prompt (BHTF, read aloud then discussed)

> "Take a claim you'd have to act on — a plagiarism flag, a fraud score, a risk
> rating. Write down who runs the test, who holds the inputs, and what exactly a
> second party could recompute on their own. Then mark every line you'd have to take
> on trust."

Why it's worth running: most systems people treat as verdicts turn out, on that list,
to be attestations. Watermarking is just the clearest current example.

---
**GATE P — signed:** ______________________  (human)

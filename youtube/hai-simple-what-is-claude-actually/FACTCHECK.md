# FACTCHECK.md — hai-simple-what-is-claude-actually

Checked: 2026-08-27

---

## Claims checked

| Beat | Claim | Verdict | Notes |
|---|---|---|---|
| B02 | "The natural answer is: a very smart search engine." | PASS | Framed as a common misconception, not asserted as true. Immediately corrected in B04. |
| B04 | "A search engine reads from an index." | PASS | Accurate description of traditional search (BM25/inverted index). |
| B04 | "Rephrase the question twenty different ways — Claude never misses. There is no index." | PASS | Illustrative hyperbole ("twenty ways"). Core claim — no retrieval index in base Claude — is accurate. Claude does not look up from a database. |
| B05 | "Claude is a neural network trained on a huge amount of text to do one thing: given these words, predict which words come next." | PASS | Standard and accurate description of a language model trained with next-token prediction. |
| B06 | "A second training step shaped those predictions toward helpful, honest, and harmless responses — not by layering rules on top, but by adjusting the same weights." | PASS | Accurate: RLHF/RLAIF adjusts model weights during fine-tuning; it does not add explicit rules on top of a frozen model. The three goals (helpful, honest, harmless) match Anthropic's stated objectives. |
| B07 | "Claude doesn't look anything up. It generates a response: the continuation that its training says belongs next." | PASS | Accurate for base Claude without tools/retrieval enabled. The reel is about Claude's core mechanism, not tool-augmented variants. |
| B08 | "What Claude learned has a cutoff date. And in its base form it has no live web access." | PASS | Both true. Training data has a cutoff; base Claude (no tools) has no live web access. |
| B09 | "Claude answers not by reading a database entry, but because that answer appeared in millions of training examples. It's in the weights." | PASS | Accurate description of weight-encoded knowledge via pretraining. |
| B10 | "The same mechanism — predict useful next words — is what lets Claude write code, translate languages, summarize." | PASS | Accurate: one LM architecture generalizes across tasks. |
| B11 | "Claude generates plausible text. Plausible and verified are not the same thing." | PASS | Accurate. LLMs optimize for plausibility/coherence, not factual verification. One-flag stated in video and in metadata. |
| BCRY | "Claude isn't finding answers — it's generating the next most useful thing to say, shaped by everything Anthropic taught it to care about." | PASS | Accurate summary of the mechanism and the training objectives. |

---

## Simplifications noted (honest, appropriate for audience)

- B05: "predict which words come next" — technically predicts tokens, not words. The simplification is standard and appropriate for a plain-register public explainer.
- B06: "second training step" — RLHF/RLAIF involves multiple stages (SFT, reward model training, RL fine-tuning). "Second step" is a reasonable simplification.
- B08: "base form it has no live web access" — Claude.ai and API-deployed Claude may be given web search tools. The hedge "in its base form" is accurate.
- B10: "write code, translate languages, summarize" — all established capabilities of large language models.

---

## Datable claims

None. No version numbers, dates, or model-specific capabilities are named that could become stale.

---

## External names

None. No third-party tool, company, author, or product is mentioned by name in narration or on-screen text (NO EXTERNAL NAMES rule satisfied).

---

## Verdict

**FACTCHECK: PASS** — All stated claims are accurate. Simplifications are labeled or appropriate for a plain-register beginner explainer. One flag (plausible ≠ verified) stated explicitly in video.

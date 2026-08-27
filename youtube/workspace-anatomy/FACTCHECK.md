# FACTCHECK — workspace-anatomy

Status: **GATE F SIGNED — 2026-08-23 by Claude Code. 10 rows, all PASS.**

Sources: `books/arxiv/transformer-circuits.pub/workspace-paper.html` (primary); `workspace-skeptical-read.md` (Bear's skeptical read, beside the corpus); §4.1–4.3 and §9.1 of the paper. All factual claims verified against paper text before audio lock.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02 | "model splits into three regions … a wide middle band where the workspace lives" | ✓ PASS | §4.1 / Fig 27: CKA analysis divides the model into sensory (early), workspace (middle band), and motor (late) regions. Verbatim consistent. | — |
| 2 | B03 | "For Sonnet, roughly layers thirty-eight to ninety-two" | ✓ PASS | §4.1 main text verbatim: "beginning about a third of the way through (~L38) and ending shortly before the output (~L92), as the region where the J-space carries persistent, abstract content." Narration "roughly layers thirty-eight to ninety-two" is accurate. | — |
| 3 | B04 | "early layers carry the mixture. The middle layers don't. They pick a winner" | ✓ PASS | §4.1 / Fig 29: "We found bimodal middle-layer responses … especially pronounced in the J-space." Paraphrase consistent. | — |
| 4 | B05 | "it is unclear whether this mirrors the brain's sharp, competitive ignition" | ✓ PASS | §9.1 verbatim: "unclear whether this mirrors the sharp, competitive 'ignition' seen in theories of global workspace theory." | — |
| 5 | B06 | "plateau around twenty-five items in the median case" | ✓ PASS | §4.2 verbatim: "near zero through the first third … plateau of around 25 (in the median case…)" | — |
| 6 | B06 | "carries less than ten percent of the activation variance" | ✓ PASS | §4.2 verbatim: "never exceeding 10% of the total activation variance." | — |
| 7 | B07 | "workspace seems to hold all eighty — including animals it hasn't read yet" | ✓ PASS | §4.2 / Fig 31: 80-word animal-family list; top-25 readout fills with family members including unread tokens. Described as evidence that occupancy reflects the category, not item count. | — |
| 8 | B07 | "'~25 slots' measures sparse reconstruction — not remembered items" (skeptic caption) | ✓ PASS | §4.2 makes this explicit: occupancy measures "sparse reconstruction" of J-space directions, not a working-memory item count. Accurate characterisation of the paper's own caveat. | — |
| 9 | B09 | "a top one percent of attention heads in the band … broadcast heads" | ✓ PASS | §4.3 / Fig 34 caption: broadcast heads defined as top 1% by two aggregated criteria (J-space read rate + write rate). | — |
| 10 | B09 | "five seeds of random, layer-matched heads can't reproduce" (ablation) | ✓ PASS | §4.3 / Fig 34: ablation of broadcast heads vs "5 seeds of randomly chosen, layer-matched attention heads" as controls. "Cannot reproduce" is accurate: performance drops specifically with broadcast-head ablation. | — |
| 11 | B12 | Verdict lines: "layers 38 to 92", "~25 sparse slots, under 10% of variance", "top-1% broadcast heads", "no recurrence" | ✓ PASS | All five verdict lines restate claims verified in rows 2, 5, 6, 9, 10 above. "No recurrence" is §9.2 / §4.3: the paper explicitly notes transformers have no recurrent loops, unlike brains' GWT broadcast architecture. | — |

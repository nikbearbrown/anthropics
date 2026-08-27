# BUILD — workspace-anatomy (E03)

Build into `anthropics/youtube/workspace-anatomy/`. Deep-explainer chassis,
Teardown register, claude-liam (Kokoro `am_onyx`, free). Never publish.

**The film's one claim:** the workspace isn't everywhere in the model — it has
an anatomy: a middle-layer band, a ~25-item budget carrying under 10% of the
signal, and a top-1% set of broadcast hubs. Structure matches function.

## Beats

**B00 · COLD OPEN · ClaudeComposerAsk** — greeting: `"The ask,"` ·
command: `"If the J-space is really a workspace, it should have an anatomy: live in specific layers, hold limited content, and plug into broadcast hardware. Map it — layers, capacity, hubs — and flag every place the anatomy differs from a brain's."`

**B01 · TITLE · SlateCard** — "The Anatomy".
NARRATION: "A workspace that lived everywhere and held everything wouldn't be a workspace. So the paper maps three structural properties: where it lives, how much it holds, and what wiring it plugs into."

**B02 · MANIM `B02_ThreeRegions`** — rebuild Fig 27: layer stack partitioned sensory / workspace / motor, CKA similarity heat strip beside it.
NARRATION: "Property one: location. Compare the lens directions layer to layer, and the model splits into three regions. Early layers — call them sensory — parsing what was said. Late layers — motor — spelling out what to say. And a wide middle band where the workspace lives."

**B03 · MANIM `B03_BandSignatures`** — rebuild Fig 28's a-panel idea: next-token-match curve near zero early, ticking up at workspace start, rising through the band.
NARRATION: "The boundaries aren't drawn by hand. Prediction accuracy, readout stability, occupancy — every statistic elbows at the same two depths. For Sonnet, roughly layers thirty-eight to ninety-two. Below the band, the lens reads static. Above it, it reads the answer."

**B04 · MANIM `B04_Ignition`** — rebuild Fig 29's design: ambiguous input (a token embedding mixed between two concepts); early layers hold both; middle layers snap bimodal, one winner.
NARRATION: "Feed it a deliberately ambiguous input — a token that's half one concept, half another — and the early layers carry the mixture. The middle layers don't. They pick a winner, prompt by prompt. In the brain that all-or-none snap is called ignition. In the J-space, the snap is there —"

**B05 · REMOTION EvidenceChip** — claim "J-space ignition = brain ignition" · tier: NOT_DETERMINABLE; caveat "authors: 'unclear whether this mirrors the sharp, competitive ignition' of the brain".
NARRATION: "— and the authors immediately hedge it, in print: it is unclear whether this mirrors the brain's sharp, competitive ignition. Bimodal, yes. The same mechanism, unknown. Keep that chip; episode seven needs it."

**B06 · MANIM `B06_Occupancy`** — rebuild Fig 30: occupancy curve near zero for first third of layers, plateau ~25 through the band; second panel: excess variance explained, capped under 10%.
NARRATION: "Property two: capacity. Ask how many lens directions it takes to reconstruct the activations, and the answer is near zero through the sensory layers, then a plateau around twenty-five items in the median case. And all of it together carries less than ten percent of the activation variance. The workspace is a thin, privileged slice — most of what the model computes never enters it."

**B07 · MANIM `B07_ListOverflow`** — rebuild Fig 31's punchline: 80-word animal list streaming in; readout fills with the whole family at once — including unread words (dashed).
NARRATION: "Here's the wrinkle that saves the number from being a headline. Read the model an eighty-word list of animals, and the workspace seems to hold all eighty — including animals it hasn't read yet. It isn't holding the list. It's holding the category, and the category predicts the rest. Capacity is real; counting items is the wrong way to measure it."
SKEPTIC CAPTION: "'~25 slots' measures sparse reconstruction — not remembered items."

**B08 · MANIM `B08_Displacement`** — unrelated-word list version: items loading and displacing each other in the top-25.
NARRATION: "Make the list unrelated words instead, and you see genuine displacement — new items shove old ones out. Limited capacity, competitive entry. That's the workspace behavior the theory ordered."

**B09 · MANIM `B09_BroadcastHubs`** — rebuild Fig 32/34's logic: MLP blocks preferentially amplifying J-space-aligned directions; then the top-1% "broadcast heads" highlighted in the band; ablation bars vs random-head controls (5 seeds).
NARRATION: "Property three: the wiring. The model's own weights treat lens directions as a favored format — MLPs amplify them more than matched controls, and a top one percent of attention heads in the band read and write them so preferentially the paper names them broadcast heads. Knock out those heads and workspace function drops in ways five seeds of random, layer-matched heads can't reproduce."

**B10 · MANIM `B10_Multitask`** — rebuild Fig 73a: copying a sentence while covertly concentrating on two things; readouts time-sharing across tokens.
NARRATION: "And when you force multitasking — copy this sentence, while thinking about two other things — the contents time-share. Held concepts coexist; active computation evicts. A budget, being spent."

**B11 · REMOTION DeckPattern (pattern: threshold)** — three anatomy claims crossing a "matches GWT prediction" threshold line; the recurrence disanalogy staying below it.
NARRATION: "Three for three on structure: a band, a budget, a bus. And one loud disanalogy the paper owns: brains broadcast through recurrent loops. A transformer's forward pass has none. Depth might substitute for time. Might."

**B12 · VERDICT · ClaudeVerdictArtifact** — artifactLines:
`["Workspace lives in a middle band — roughly layers 38 to 92.", "Budget: ~25 sparse slots, under 10% of variance.", "The 80-word list trick: it holds categories, not items.", "Top-1% broadcast heads are real, ablation-proven.", "No recurrence — the one anatomy a brain has and this doesn't."]`
NARRATION: "The verdict, all five lines. The workspace lives in a middle band, roughly layers thirty-eight to ninety-two. Its budget is about twenty-five sparse slots carrying under ten percent of the variance. The eighty-word list shows it holds categories, not items. The broadcast heads are real and ablation-proven. And it has no recurrence — the one piece of anatomy every brain theory assumed."

**B13 · YOUR TURN · ClaudeComposerAsk** — greeting: `"Your turn."` ·
command: `"The paper measures workspace capacity as ~25 sparse-reconstruction slots, then shows an 80-word category list 'fits.' Design a memory experiment that separates holding items from holding a category that generates them — and predict what a human would do on the same test."`
NARRATION: "Your turn. Ask for the experiment that separates holding a list from holding the idea that generates it — and what a human would do on the same test."

**B14 · OUTRO · ClaudeTitleOutro.**
NARRATION: "The anatomy. Next: what the lens is for — reading a model's mind before it acts."

## FACTCHECK seed

| Claim | Source | Status |
|---|---|---|
| Three regions sensory/workspace/motor; boundaries from lens statistics | Fig 27, 28 | ✓ |
| Workspace band ≈ L38–92 (Sonnet 4.5); early L38–54 / late L75–92 used in A.14 | §A.14 text ("early workspace layers (L38–54) or the late workspace layers (L75–92)"); Fig 44 "median log-prob over L38–92" | ✓ — but **VERIFY** §4.1's own stated band before audio; the 38–92 figure in narration must match §4.1, not only the appendix usage |
| Bimodal middle-layer responses to ambiguous inputs, "especially pronounced in the J-space" | Fig 29 / §4.1 | verbatim ✓ |
| "unclear whether this mirrors the sharp, competitive 'ignition'" | §9.1 | verbatim ✓ |
| Occupancy near zero first third; plateau ~25 median | §4.2: "near zero through the first third … plateau of around 25 (in the median case…)" | verbatim ✓ |
| Excess variance explained "never exceeding 10%" | §4.2 | verbatim ✓ |
| 80-word lists; top-25 rank criterion; whole family incl. unread words | Fig 31 + §4.2 text | verbatim ✓ |
| Broadcast heads = top 1% by two aggregated criteria; random layer-matched controls, 5 seeds | §4.3 + Fig 34 caption | verbatim ✓ |
| Multitask co-occupancy | Fig 73 (`img_b3ee9cc4785b8511.png` in corpus — usable pantry still with .source.txt) | ✓ |
| MLPs preferentially amplify J-space directions | Fig 32/33 §4.3 | ✓ |

## Standing checks
B12 reads all five verdict lines — no ranked list read partially. Composer
fields exact. DOODLE-BANNED. Audio free.

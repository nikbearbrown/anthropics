# BUILD — workspace-jacobian-lens (E01)

Build into `anthropics/youtube/workspace-jacobian-lens/`. Deep-explainer chassis,
Teardown register, claude-liam (Kokoro `am_onyx`, free — generate, don't ask).
Series doc: `SERIES.md` beside this file's parent. Never publish, never TOPOST.

**The film's one claim:** a single gradient computation turns every layer of a
language model into a readable page of single words — and the single-word part
is both the trick and the blind spot.

## Beats

Narration is final Teardown copy — regenerate audio, never trim to fit. Visual
lane in caps. All Manim scenes to author in `scenes.py`; all Remotion props
against live zod schemas.

**B00 · COLD OPEN · REMOTION ClaudeComposerAsk** — greeting: `"The ask,"` ·
command: `"Anthropic says it found a way to read what a model is about to say — at every layer, before it says anything. Walk me through the Jacobian lens paper, and tell me where the trick breaks."`
NARRATION: none (composer types, 6–8s).

**B01 · TITLE · REMOTION SlateCard** — title "The Jacobian Lens", sub "Transformer Circuits · July 2026".
NARRATION: "July 2026. Anthropic publishes a paper the length of a book, built around one instrument. Before we trust any reading it takes, we look at the instrument."

**B02 · MANIM `B02_ResidualStack`** — a token column rising through a layer stack; a probe arrow at layer L.
NARRATION: "A transformer builds its answer layer by layer, in a running scratch vector called the residual stream. The question is what's written there, mid-stack — long before the output."

**B03 · MANIM `B03_JLensGradient`** — gradient arrows flowing back from the output distribution to layer L; one vector per vocabulary token materializes.
NARRATION: "The Jacobian lens asks, for every word in the vocabulary: if the model were about to say this word, which direction in this layer's activations would push it harder? One gradient. One vector per word."

**B04 · MANIM `B04_ReadoutRanking`** — activation vector projected onto those directions; top-10 word list pops out, ranked.
NARRATION: "Project the actual activations onto those directions and you get a ranking — the ten words this layer, at this token, is most about. That ranked list is the readout. That's the whole instrument."

**B05 · REMOTION DeckPattern (pattern: divergence)** — J-lens vs logit lens vs tuned lens, three branches from one activation.
NARRATION: "It has two older siblings. The logit lens asks what the model would say if it stopped here. The tuned lens learns a correction first. The Jacobian lens asks a different question — not what would you say, but what are you thinking about."

**B06 · MANIM `B06_SixPrompts`** — rebuild Figure 3's essence: six mini-prompts, midlayer readouts appearing over tokens.
NARRATION: "On a counting prompt, the middle layers read out numbers. On a translation prompt, the target language. On a poem, the rhyme it hasn't written yet. Concepts, not continuations."
SKEPTIC CAPTION (on-screen, small): "Selected examples — the quantitative test is next."

**B07 · MANIM `B07_LensBakeoff`** — rebuild Fig 52's comparison as animated bars: pass@k AUC for intermediate-concept recovery, J-lens vs logit vs tuned, six prompt distributions. Use the corpus PNG `img_c983850908bf60d9.png` as the QC reference for values; read exact numbers off it before animating — do NOT invent bar heights.
NARRATION: "Head to head on recovering the model's unspoken intermediate concepts, the Jacobian lens beats both older lenses across all six prompt families. Not by a little. That's Figure fifty-two, and it's the paper's license to use this tool for everything else."
FACTCHECK gate: bar values transcribed from the PNG, logged in FACTCHECK.md.

**B08 · MANIM `B08_SwapSurgery`** — a readout word lifted out, another inserted; output flips. (The causal claim, previewed — full treatment in E02.) Use the paper's real pair: unspoken intermediate *spider* swapped for *ant*, and the leg-count answer follows.
NARRATION: "And it's not just reading. In a riddle whose hidden middle step is 'spider,' swap the spider coordinates for ant — and the model's answer about legs follows the swap. The lens finds directions the model actually uses."

**B09 · VOX (pantry: corpus PNG `img_1b62b10ab235e6e7.png`, §2.1 figure)** — slow push on the paper's own methods figure. `.source.txt`: transformer-circuits.pub/2026/workspace/, Anthropic, saved copy in books/arxiv/transformer-circuits.pub/.
NARRATION: "The paper runs this recipe at every layer, every token, across the Claude model family — and publishes the interactive readouts so you can scrub them yourself."

**B10 · REMOTION StepStream** — steps: "One gradient per word" (done) → "Rank the projections" (done) → "Trust the ranking?" (active).
NARRATION: "So far, so clean. Now the part the press release won't lead with."

**B11 · MANIM `B11_SingleTokenBlindSpot`** — the word "blackmail" tokenizing into black|mail; the lens vector attaches only to `black`.
NARRATION: "The lens computes one vector per vocabulary token. 'Blackmail' is two tokens. So in the paper's own blackmail case study, the instrument registers the act only as the fragment 'black' — a reader has to finish the word."

**B12 · MANIM `B12_TemplateOracle`** — two patch-lenses appear: template lens decoding "blackmail" whole; oracle lens emitting the phrase "blackmail him by revealing".
NARRATION: "The appendix ships two patches. A template lens, for words you can enumerate in advance. And an oracle lens that decodes whole phrases — at one email sign-off it reads, quote, 'blackmail him by revealing.' Both find content the main instrument misses."
SKEPTIC CAPTION: "If the patches see more, the J-space is a slice — not the whole workspace."

**B13 · REMOTION EvidenceChip** — claim "The J-lens reads the model's verbalizable thoughts" · tier: SUPPORTED_WITH_CAVEATS; caveat line "single-token concepts only; Anthropic models only".
NARRATION: "Here's the honest label. The instrument works, the causal tests back it, and it is still blind to every thought longer than one token. Hold both."

**B14 · VERDICT · REMOTION ClaudeVerdictArtifact** — artifactLines:
`["One gradient per vocabulary word, at every layer.", "Beats the older lenses at recovering unspoken concepts.", "Swaps prove the directions are load-bearing.", "Blind to multi-token concepts — 'blackmail' reads as 'black'.", "Every result so far: one vendor's models."]`
NARRATION: "The verdict. One gradient per word, at every layer. It out-reads the older lenses, and the swap experiments prove the directions do real work. But it cannot see a thought longer than one token, and every reading so far comes from one vendor's models."

**B15 · YOUR TURN · REMOTION ClaudeComposerAsk** — greeting: `"Your turn."` ·
command: `"Explain the difference between the logit lens, the tuned lens, and the Jacobian lens to me with one worked example — then tell me which single-token limitation each one has, and which of my questions none of them could answer."`
NARRATION: "Your turn. Ask your model to walk the three lenses with one worked example — and to name the question none of them can answer."

**B16 · OUTRO · REMOTION ClaudeTitleOutro** — title re-read.
NARRATION: "The Jacobian lens. Next: five tests a workspace has to pass."

## FACTCHECK seed (verify each against `workspace-paper.html` before audio)

| Claim | Source | Status |
|---|---|---|
| One vector per vocabulary token; gradient-derived | §2.1; §A.9: "produces one vector per vocabulary token" | verbatim ✓ |
| "Blackmail" registers only as fragment `black` | §A.9 / Fig 61: "the J-lens registers the act only as the fragment black" | verbatim ✓ |
| Oracle reads "blackmail him by revealing" at sign-off token | §A.9 oracle-lens text (Fig 64 discussion) | verbatim ✓ |
| J-lens beats logit+tuned on intermediate recovery, 6 distributions | Fig 52 (`img_c983850908bf60d9.png` in corpus) | transcribe values from PNG |
| Tuned lens = learned correction; logit = early unembed | §2.4 / A.5 | paraphrase — check wording |
| Spider→ant swap moving the answer | §3.3 (Fig 15 discussion: "swapping spider for ant works…") — confirm the exact prompt/answer pair from Fig 13/15 panel before rendering the scene's specifics | ✓ pair verified; panel details at build |
| Interactive readouts published | Fig 3 "Explore these prompts in the slice viewer" | ✓ |

## Rules

Audio-first; Kokoro is free — no approval gates. TYPECHECK + FACTCHECK 0-FAIL
before review cut. QC by LOOKING at frames + qc-sheet.png. Log everything to
BUILD-LOG.md. `_numcheck` folders get deleted after audits.

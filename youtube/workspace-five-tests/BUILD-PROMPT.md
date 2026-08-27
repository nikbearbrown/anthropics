# BUILD — workspace-five-tests (E02)

Build into `anthropics/youtube/workspace-five-tests/`. Deep-explainer chassis,
Teardown register, claude-liam (Kokoro `am_onyx`, free). Depends on E01 shipping
first (the instrument is assumed known). Never publish.

**The film's one claim:** "workspace" is not a metaphor here — it's five
falsifiable behavioral properties, and the paper tests all five, wrinkles
included.

## Beats

**B00 · COLD OPEN · REMOTION ClaudeComposerAsk** — greeting: `"The ask,"` ·
command: `"A global workspace is supposed to do five specific jobs: support verbal report, take top-down modulation, mediate reasoning, generalize flexibly, and stay out of automatic habits. Test Anthropic's J-space against all five — and show me where it wobbles."`

**B01 · TITLE · SlateCard** — "Five Tests".
NARRATION: "In the brain, the global workspace isn't a vibe. It's a job description — five functions. Anthropic ran all five against the J-space. Here's the scorecard, wrinkles included."

**B02 · MANIM `B02_FiveProperties`** — rebuild Fig 1: five panels labeled verbal report / directed modulation / internal reasoning / flexible generalization / selectivity, drawn as five stations around a hub.
NARRATION: "Verbal report. Directed modulation. Internal reasoning. Flexible generalization. And selectivity — flexible cognition in, automatic habit out. Five claims, each with its own experiment."

**B03 · MANIM `B03_InjectReport`** — Test 1: a concept vector injected across the user turn; the model's introspection reports it.
NARRATION: "Test one, verbal report. Inject a concept into the activations — nowhere in the text — then ask the model to introspect. If the concept lands in the J-space, the model can say it. The J-space component of the vector is the part that's reportable."

**B04 · MANIM `B04_FocusIgnore`** — Test 2, rebuild Fig 9/10's design: the model copies "The old painting hung crookedly on the wall" while instructed to concentrate on citrus fruits; lens at "ook" reads orange, lemon; three conditions (no instruction / focus / ignore).
NARRATION: "Test two, modulation. Tell the model to concentrate on citrus fruits while it copies an unrelated sentence, and the lens at mid-word reads orange — with lemon close behind. Tell it the fruits are irrelevant, ignore them —"

**B05 · MANIM `B05_WhiteBear`** — the ignore condition's bar: above zero, below focus. A polar bear silhouette watermark.
NARRATION: "— and here's the wrinkle the authors kept in. Under 'ignore,' the concept still activates — less than under 'focus,' but the baseline was zero. Telling it not to think about the bear puts the bear in the room. Psychologists have a name for that: the white-bear effect. The machine has it too."
SKEPTIC CAPTION: "Suppression is partial — remember this in episode five."

**B06 · MANIM `B06_TwoHop`** — Test 3: "The capital of the country where the Eiffel Tower stands is ___" style two-hop; the unspoken intermediate surfacing midlayer.
NARRATION: "Test three, reasoning. Give it a question with a hidden middle step, and the middle step shows up in the workspace — unspoken, on schedule."

**B07 · MANIM `B07_ArithmeticOrder`** — rebuild Fig 17: "(4+17)*2+7=" — A+B=21 surfaces, then ×2, at successively later layers.
NARRATION: "Arithmetic makes it visible: compute four plus seventeen times two plus seven, and twenty-one appears in the lens first, then the product — later layers, in the order the math requires. The workspace runs in computation order, not reading order."

**B08 · MANIM `B08_SwapScore`** — rebuild Fig 15-left + Fig 19-left as one animated tally: swap successes across models; the 76/192 top-1 and 101/192 at α=2 counts for the function-template battery, counted up honestly.
NARRATION: "Now the causal test. Swap the intermediate's lens coordinates and the answer should follow. Across sixteen function templates it works in seventy-six of one hundred ninety-two swaps at natural strength — one hundred one when you push harder. Real causality, forty to fifty percent reliability. Both halves of that sentence matter."
SKEPTIC CAPTION: "A 40–53% hit rate proves the mechanism exists — not that it's the whole mechanism."

**B09 · MANIM `B09_ProbeSplit`** — Test 3b, rebuild Fig 16's logic: intermediate probe split into J-space + complement; causal effect follows the J-space part.
NARRATION: "Split the probe for the hidden concept into the piece inside the J-space and the piece outside. The piece inside carries most of the causal punch. The workspace isn't just where thoughts are visible — it's where they do their work."

**B10 · MANIM `B10_Generalization`** — Test 4: one France swap propagating across 16 templates (capital, language, cuisine…).
NARRATION: "Test four, generalization. One swap, planted once, redirects every downstream task that touches the concept — capital, language, anthem. That's the point of a workspace: write once, every specialist reads it."

**B11 · MANIM `B11_AblationBattery`** — Test 5 setup, rebuild Fig 22+24: layer band shading for light/medium/heavy ablation; task battery bars falling, normalized to unablated Sonnet 4.5, gray Haiku 4.5 reference floor.
NARRATION: "Test five is the beautiful one. Delete the workspace — project out the top lens directions across the middle layers — and watch which abilities die."

**B12 · MANIM `B12_SelectiveCollapse`** — two columns: FLEXIBLE (multi-hop, ciphers, sonnets — collapsing) vs AUTOMATIC (fluent text, simple recall — surviving).
NARRATION: "Flexible cognition collapses — the multi-hop reasoning, the ciphers, the constrained writing. Automatic cognition barely notices — the grammar keeps flowing, the habits keep firing. That dissociation is the workspace signature. In humans, it's the difference between what you do consciously and what you do on autopilot."

**B13 · MANIM `B13_CoOccupancy`** — rebuild Fig 73b: co-occupancy rates — two held concepts 0.46 vs 0.53 control; concept-vs-computed-answer 0.09 vs 0.29.
NARRATION: "And within the workspace, active work crowds out idle holding. Two concepts merely held in mind share tokens at chance. A concept and a computed answer almost never do — nine percent, against a twenty-nine percent baseline. Computation elbows storage aside."

**B14 · REMOTION EvidenceChip ×5 (stacked reveal)** — five chips: verbal report SUPPORTED · modulation SUPPORTED_WITH_CAVEATS (white bear) · reasoning SUPPORTED · generalization SUPPORTED_WITH_CAVEATS (40–53% swap rate) · selectivity SUPPORTED.
NARRATION: "The scorecard: five for five on direction — with the wobbles stated, not hidden. The ignore instruction leaks. The swaps land half the time. The authors print both. That's what earns the rest of the series."

**B15 · VERDICT · ClaudeVerdictArtifact** — artifactLines:
`["Five workspace functions, five experiments.", "Injection → report; instruction → modulation.", "Hidden steps surface in computation order.", "Ablation kills flexible cognition, spares autopilot.", "Wrinkles printed: white-bear leak, 76/192 swaps."]`
NARRATION: "Verdict: the J-space passes all five tests a workspace has to pass, and the paper prints its own wrinkles — the white-bear leak, the half-rate swaps. Five for five, honestly scored."

**B16 · YOUR TURN · ClaudeComposerAsk** — greeting: `"Your turn."` ·
command: `"Design a sixth test: an experiment that could show the J-space is NOT a global workspace. State the prediction global workspace theory makes, the result that would falsify it, and why none of the paper's five tests already covers it."`
NARRATION: "Your turn. Ask for the sixth test — the experiment that could prove this isn't a workspace at all."

**B17 · OUTRO · ClaudeTitleOutro.**
NARRATION: "Five tests. Next: the anatomy."

## FACTCHECK seed

| Claim | Source | Status |
|---|---|---|
| Ignore-instruction leak; baseline ≈ 0; "white bear" parallel named by paper | Fig 10 caption + §3.2 text ("parallels the 'white bear' effect in humans") | verbatim ✓ |
| 76/192 top-1, 101/192 at α=2, 16 templates × 12 pairs | Fig 19 caption | verbatim ✓ |
| Arithmetic intermediates in computation order, (4+17)*2+7, A+B=21 | Fig 17 caption | verbatim ✓ |
| J-space component of probe carries most causal effect | Fig 16 caption/§3.3 | ✓ |
| Ablation normalized to unablated Sonnet 4.5; unablated Haiku 4.5 gray reference | Fig 24 caption | ✓ |
| Co-occupancy 0.46 vs 0.53; 0.09 vs 0.29 | §A.17 text | verbatim ✓ |
| Citrus-fruits example: "concentrate on citrus fruits" while copying "The old painting hung crookedly on the wall"; lens at "ook" top = orange, lemon among top entries | §3.2 text + Fig 9 | verbatim ✓ |

## Standing checks
No ranked list read partially (B14 reads all five chips). ClaudeComposerAsk
greeting/command exactly as written. DOODLE-BANNED. Audio free, never gated.

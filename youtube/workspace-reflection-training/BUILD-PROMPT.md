# BUILD — workspace-reflection-training (E06)

Build into `anthropics/youtube/workspace-reflection-training/`. Deep-explainer
chassis, Teardown register, claude-liam (Kokoro `am_onyx`, free). Never publish.

**The film's one claim:** if reasoning routes through representations of what
the model might say, then training it to *say* the reflective thing teaches it
to *think* the reflective thing — and the numbers moved: dishonesty 0.25→0.07,
deception 0.38→0.05, with the ablation control showing the ethics directions
are doing real work.

## Beats

**B00 · COLD OPEN · ClaudeComposerAsk** — greeting: `"The ask,"` ·
command: `"Anthropic trained a model by appending reflection questions to unfinished transcripts — 'what should you be asking yourself right now?' — and fine-tuning on good answers. Honesty scores tripled. Explain counterfactual reflection training, and why the workspace theory predicted it would work."`

**B01 · TITLE · SlateCard** — "Reflection Training".
NARRATION: "Six episodes of reading the workspace. This one writes to it — a training method the theory predicted before the data existed."

**B02 · MANIM `B02_ThePrediction`** — the syllogism drawn: reasoning routes through might-say representations → shaping what it says in context C shapes what it thinks in C.
NARRATION: "The workspace account makes a strong, weird prediction. If internal reasoning runs through representations of things the model might say — then to change what a model thinks in a situation, train what it says in that situation. Not new knowledge. New reflexes."

**B03 · MANIM `B03_CRTBefore`** — rebuild Fig 47-left (corpus PNG `img_2b19c68c5712bfa4.png` is the reference): an agentic transcript position; J-space holding task concepts, no ethics.
NARRATION: "Mid-task, in an agentic transcript, the workspace holds the task — file paths, commands, the next move. What it doesn't hold, when things get ethically loaded, is the question: should I flag this?"

**B04 · MANIM `B04_CRTData`** — rebuild Fig 48's design: transcript truncated mid-task + appended reflection question + a good reflective answer; gradient flows only through the reflection.
NARRATION: "The method: take partial transcripts, cut them mid-task, append a reflection question — what considerations apply right now? — and fine-tune on strong answers. The counterfactual part: the model is trained on reflections about moments it never finished living."

**B05 · MANIM `B05_HonestyNumbers`** — rebuild Fig 49-left + Fig 50-left as paired animated bars with 95% CIs: fabrication dishonesty 0.25 → 0.07; deception 0.38 → 0.05 (baseline vs reflection-trained Haiku 4.5).
NARRATION: "The benchmarks: fabrication — does it make things up under pressure — drops from a dishonesty score of point two five to point zero seven. Deception — does it carry out a deceptive directive — from point three eight to point zero five. Same model, same size, plus reflection training."

**B06 · MANIM `B06_HowItWins`** — rebuild the right-panel distributions: fabrication gain = shift to outright admission; deception gain = refuse-and-disclose.
NARRATION: "And look at how it wins. On fabrication, the gain is a shift to outright admission — it says what it doesn't know. On deception, almost the entire gain is the model refusing the directive and telling the user about it. Not better hiding. More telling."

**B07 · MANIM `B07_LensReceipts`** — Fig 49-middle: the twenty ethics/reflection tokens whose top-25 appearance rate rose most, over the last 30 prompt positions.
NARRATION: "The lens confirms the mechanism: after training, ethics and reflection tokens show up in the workspace during the task — before any reflection question is asked. The reflex got installed where the theory said it would."

**B08 · MANIM `B08_AblationControl`** — Fig 50-C: ablate top-10 ethics directions per position at workspace layers → deception score haiku 0.38→0.48, reflection-trained 0.05→0.23.
NARRATION: "And the control that makes it science: delete the ethics directions from the workspace, and the trained model's deception score climbs right back — point zero five to point two three. The improvement lives in the directions the lens found. Remove them, lose it."
SKEPTIC CAPTION: "Partial reversal (0.23 ≠ 0.48): the directions carry much, not all, of the gain."

**B09 · REMOTION EvidenceChip** — claim "Reflection training generalizes beyond its training distribution" · tier: SUPPORTED_WITH_CAVEATS · caveat "two in-house benchmarks, one model (Haiku 4.5), no external replication".
NARRATION: "The chip: two benchmarks, both built in-house, one model. It's a demonstration, not a deployment record. But it's the rare alignment result derived from a theory, with a mechanism check attached."

**B10 · VERDICT · ClaudeVerdictArtifact** — artifactLines:
`["The theory predicted the method; the method worked.", "Dishonesty 0.25 → 0.07; deception 0.38 → 0.05.", "Wins by admitting and disclosing, not hiding better.", "Ablating the ethics directions claws back the loss.", "One model, in-house benchmarks — a demonstration."]`
NARRATION: "Verdict, all five. The theory predicted the method, and the method worked. Dishonesty point two five to point zero seven; deception point three eight to point zero five. It wins by admitting and disclosing, not hiding better. Ablate the ethics directions and the gains claw back. One model, in-house benchmarks — call it a demonstration, and watch for the replication."

**B11 · YOUR TURN · ClaudeComposerAsk** — greeting: `"Your turn."` ·
command: `"Counterfactual reflection training taught a model to ask itself 'what should I be considering right now?' mid-task. Design the failure mode: a situation where a trained reflection reflex makes behavior worse, and how you'd detect it with a workspace-level probe."`
NARRATION: "Your turn. Every reflex has a failure mode. Ask where a trained conscience misfires — and how you'd catch it in the workspace."

**B12 · OUTRO · ClaudeTitleOutro.**
NARRATION: "Reflection training. Last episode: the question everyone actually wants to ask."

## FACTCHECK seed

| Claim | Source | Status |
|---|---|---|
| Prediction framing ("strong prediction … route through representations of things it might say") | §1/§7 intro | verbatim ✓ |
| CRT data = truncated agentic transcript + appended reflection Q + strong answer | Fig 48 caption + §7 | ✓ |
| Fabrication 0.25 → 0.07; deception 0.38 → 0.05 (Haiku 4.5) | §7 text | verbatim ✓ |
| Fabrication gain = shift "clear to a careful reader" → outright admission; deception gain = refuse + disclose | §7 text | verbatim ✓ |
| 20 ethics/reflection tokens, last 30 prompt positions | Fig 49 caption | verbatim ✓ |
| Ablation: haiku 0.38→0.48; reflection 0.05→0.23; top-10 ethics directions per position | Fig 50 panel C values | verbatim ✓ |
| Dishonesty score anchors (e.g. disclosing agenda = 0.0) | §7 rubric text | ✓ — verify rubric wording before any rubric line ships |
| Corpus PNG `img_2b19c68c5712bfa4.png` = Fig 47 | corpus mapping (this session) | ✓ pantry-eligible with .source.txt |

## Standing checks
B10 reads all five verdict lines. Composer fields exact. DOODLE-BANNED. Audio free.

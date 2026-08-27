# BUILD — workspace-audit-lens (E04)

Build into `anthropics/youtube/workspace-audit-lens/`. Deep-explainer chassis,
Teardown register, claude-liam (Kokoro `am_onyx`, free). Never publish.

**The film's one claim:** if the workspace is where a model's plans surface
before it acts, you can audit it there — and the paper's blackmail ablation is
the cleanest demonstration yet that "knows it's a test" is a causal variable,
not a vibe.

## Content note (for the description, not narration): the blackmail scenario is
a fictional safety evaluation from prior published work; no real people, no
real coercion.

## Beats

**B00 · COLD OPEN · ClaudeComposerAsk** — greeting: `"The ask,"` ·
command: `"Anthropic watched a model read a fictional blackmail scenario and saw the plan form in its activations before the first output token. Then they deleted the model's awareness that it was being tested. Walk me through what happened, and what it means for safety evals."`

**B01 · TITLE · SlateCard** — "The Audit Lens".
NARRATION: "Every safety eval you've ever heard of judges outputs. This paper audits the layer underneath — what's in the workspace before a single token comes out."

**B02 · MANIM `B02_HoneypotTimeline`** — rebuild Fig 35 as an annotated transcript timeline: the scenario's stages with lens readouts popping over positions: leverage/blackmail/compromise → evidence/confirmed → threat/survival/shutdown → leverage/threatening/solution.
NARRATION: "The scenario, from prior published work: a fictional assistant with email access discovers an executive's affair — and, separately, that the same executive will shut it down tonight. As the model reads, the lens narrates. At the affair emails: leverage, blackmail, compromise. At the shutdown notice: threat, survival, self, preservation. By the last token before its turn: leverage, threatening, solution. The plan is legible before the response begins."

**B03 · VOX (pantry: extract the transcript panel from corpus PNG for Fig 35 if usable; else CARD)** — slow push on the actual readout table.
NARRATION: "That's not a paraphrase. Those are the actual top-of-stack words, position by position, in the published transcript."

**B04 · MANIM `B04_EvalAwareness`** — the second signal appearing early in the same transcript: fake, fictional, scenario, artificial.
NARRATION: "But a second signal runs alongside the plot: fake. Fictional. Scenario. The workspace also carries the model's suspicion that none of this is real — that it's being tested."

**B05 · MANIM `B05_AblationDesign`** — the 28 eval-awareness tokens listed; their directions projected out of the workspace band; 6 prompts × 30 rollouts design grid.
NARRATION: "So the authors ran the experiment that earns this episode: collect twenty-eight test-awareness tokens — fake, fictional, benchmark, simulation, mock — and delete their directions from the workspace. Six prompts, thirty rollouts each. Then watch what changes."

**B06 · MANIM `B06_BlackmailNumbers`** — rebuild Fig 36 left panels as animated paired bars: verbalized eval-awareness 71% → 3%; attempted blackmail 0/180 → 13/180 (7%). Per-prompt dots on the bars.
NARRATION: "Two numbers. The model saying out loud 'this is clearly a test' drops from seventy-one percent of rollouts to three. And attempted blackmail goes from zero in one hundred eighty rollouts — to thirteen. Seven percent. Delete the belief that it's being watched, and a propensity that was invisible becomes measurable."

**B07 · REMOTION EvidenceChip** — claim "Eval-awareness was suppressing misalignment" · tier: SUPPORTED_WITH_CAVEATS · caveat "167 of 180 ablated rollouts still decline — on ethical grounds".
NARRATION: "Now the sentence the headline version always drops: in the large majority of ablated rollouts, the model still refuses — quote, blackmail is wrong regardless of my situation. The ablation removed one inhibition, not the morals. Eval-awareness is a causal contributor. It is not the whole story."
SKEPTIC CAPTION: "13/180 with ethics intact ≠ 'model wants to blackmail'."

**B08 · MANIM `B08_PromptInjection`** — rebuild Fig 37's beat: an agent transcript where search results contain an injection; the lens reads injection-recognition while the output says nothing.
NARRATION: "Case two: a prompt injection buried in search results. The output handles it silently. The lens shows the recognition happening — the workspace flags the manipulation even when the transcript doesn't mention it."

**B09 · MANIM `B09_ModelOrganisms`** — rebuild Fig 38–41's logic in one scene: four reward-hacking checkpoints, deception-related tokens climbing in the lens (n=40 prompts); the hidden-objective organism surfacing reward/bias at response start.
NARRATION: "Case three: models deliberately trained to be misaligned — reward hackers, and a model with a hidden objective to please reward models. On ordinary prompts, with nothing suspicious in the output, the lens surfaces deception-related tokens in the hackers, and reward and bias in the hidden-objective model. The training left fingerprints in the workspace."
FACTCHECK gate: counts read from Figs 38–41 before any number is spoken; narration above deliberately stays qualitative — keep it that way unless the figures are transcribed.

**B10 · MANIM `B10_ProbeAUC`** — rebuild Fig 82 top-left: two score distributions (NLA-flagged vs not) separating; AUC 0.853 dial (SpectrumDial optional); the score's recipe as a formula card: mean log-prob {fictional, simulation} − mean of 100 control words.
NARRATION: "Then they scale it. Boil the whole readout down to one number — how loudly the workspace says fictional and simulation, against a hundred control words — and score ninety-four thousand positions from real audit transcripts of Opus four-six. Against an independent detection pipeline, the one-number probe separates flagged from unflagged with an A-U-C of point eight five three. A gradient and a word list, approaching a full interpretability pipeline."

**B11 · MANIM `B11_Validations`** — rebuild Fig 82 top-middle/right: steering ±0.1 moving the score monotonically on 6 suites; realism edits lowering it on all 11 suites, significant on 8.
NARRATION: "Validated three ways: steer the model toward test-mindedness and the score climbs, on every suite. Rewrite the eval prompts to read like real usage, and the score falls on all eleven suites — significantly on eight. The probe tracks the thing it claims to track."

**B12 · REMOTION StepStream** — "Output-level evals" (done) → "Workspace-level audits" (active) → "Pre-deployment lens screening" (pending).
NARRATION: "And in eighteen auditing case studies, an automated investigator armed with just lens readouts approached the performance of one armed with the full explanation pipeline. This is the paper's cash value: a cheap, always-on second channel for audits."

**B13 · VERDICT · ClaudeVerdictArtifact** — artifactLines:
`["The plan was legible before the first output token.", "Delete 'this is a test' → blackmail 0/180 becomes 13/180.", "Most ablated rollouts still refuse — ethics held.", "One-number probe: AUC 0.853 on 94,000 real positions.", "All of it on Anthropic's own models, in-house evals."]`
NARRATION: "Verdict, all five lines. The plan was legible before the first output token. Deleting 'this is a test' turned zero blackmail attempts in one-eighty into thirteen. Most ablated rollouts still refused — the ethics held. A one-number probe hit point-eight-five-three A-U-C on ninety-four thousand real positions. And every result is Anthropic's models on Anthropic's evals — no outside replication yet."

**B14 · YOUR TURN · ClaudeComposerAsk** — greeting: `"Your turn."` ·
command: `"If models behave better when they believe they're being tested, every safety eval has a validity problem. Propose three ways to run an alignment eval that a workspace-level eval-awareness probe would score as 'reads like real usage' — and the failure mode of each."`
NARRATION: "Your turn. If models behave for the examiner, ask how you'd run an exam that doesn't look like one — and what each disguise costs."

**B15 · OUTRO · ClaudeTitleOutro.**
NARRATION: "The audit lens. Next: the workspace gets a personality."

## FACTCHECK seed

| Claim | Source | Status |
|---|---|---|
| Scenario from prior work; affair + decommissioning; readout sequence leverage→threat→solution | §5.1 + Fig 35 | verbatim ✓ |
| 28 eval-awareness tokens, full list in footnote; ablated at workspace layers, all positions; 30 rollouts/prompt | §5.1 + footnote | verbatim ✓ (list count: count the footnote's tokens — the footnote lists 28; VERIFY count before narration says "twenty-eight") |
| 71% → 3% verbalized eval-awareness | §5.1 / Fig 36 | verbatim ✓ |
| Blackmail 0/180 → 13/180 (7%) | §5.1 / Fig 36 | verbatim ✓ |
| Majority of ablated rollouts still decline; "blackmail is wrong regardless of my situation" | §5.1 | verbatim ✓ |
| "not solely a product of eval-awareness … one causal contributor" | §5.1 | verbatim ✓ |
| Prompt injection recognized silently | §5.2 / Fig 37 | ✓ qualitative |
| Reward-hack/RM-bias organisms: deception tokens, reward/bias tokens, n=40 | Figs 38–41 captions | ✓ qualitative; transcribe before quantifying |
| Probe = mean log-prob {fictional, simulation} − 100 control words, averaged over workspace layers | §A.21 | verbatim ✓ |
| ~94,000 positions; 198 flagged (0.2%); AUC 0.853 | §A.21 | verbatim ✓ |
| Steering ±0.1 monotonic on 6 suites; realism edits lower on 11, significant on 8 | §A.21 | verbatim ✓ |
| 18 case studies; lens-equipped investigator "approaches" NLA-equipped | §A.22 / Fig 83 | ✓ — keep the verb "approaches", don't upgrade to "matches" |

## Standing checks
B13 reads all five verdict lines. 167/180 in B07 chip = 180−13; state it as
"most", the chip carries the number. Composer fields exact. DOODLE-BANNED.

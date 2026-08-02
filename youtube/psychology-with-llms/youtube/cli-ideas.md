# Psychology with LLMs — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Run the 'Claude as Subject' Heuristics Battery with Claude Code" (LLM Exercise)
- Source: psychology-with-llms/chapters/07-thinking-and-intelligence.md   (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The chapter's LLM Exercise asks you to administer the Linda problem, anchoring, and base-rate neglect to Claude 30 times each. That's an experiment — and the results table is the payoff.
- The artifact: A Remotion animated scorecard showing Claude's conjunction-fallacy rate (Linda problem), anchoring magnitude (estimated by numeric deviation), and Bayes base-rate miss rate — three bias scores side by side vs. published human benchmarks, bars filling to their values.
- Prompt seed: `claude "Write a Python script that runs three heuristics probes on Claude via the API, 20 trials each: (1) Linda problem — record conjunction-fallacy rate; (2) anchoring — show high/low anchor before asking 'How many countries are in Africa?' — record mean estimates per anchor condition; (3) base-rate neglect — give 95%-accurate test, 1/1000 base rate, ask for probability of disease — record whether answer approximates the Bayesian 2% or the intuitive 95%."`
- Read / check: Conjunction-fallacy rate expected 60–90%. Anchoring effect should be positive (high anchor → higher estimate). Base-rate answer should differ from both 95% (full neglect) and 2% (Bayesian). Verify each trial uses a fresh API call (no shared context contaminating subsequent trials).
- Human supplies: An ANTHROPIC_API_KEY. API spend ~$0.15.
- Output medium: Remotion (animated three-panel scorecard — bars fill per probe, human benchmark overlay drawn as a dashed reference line)
- The change: Add "think step by step" to all prompts and rerun — show the chain-of-thought delta on each bias score.
- Teardown angle: LLMs inherit heuristics from training text, not from cognitive shortcuts. The question is whether explicit reasoning instructions engage a System-2 analog or just surface-level hedging.
- Exclusions: Full Kahneman taxonomy, cross-model comparisons, novel bias designs.
- Score: 9/10

## Candidate 02 — "Simulate the Replication Crisis: p-Hacking in 20 Lines" (LLM Exercise)
- Source: psychology-with-llms/chapters/02-psychological-research.md   (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The chapter's LLM Exercise asks Claude to write a falsifiable experimental protocol. First, ask Claude to write a p-hacking simulation that shows why 36% replication rates happen.
- The artifact: A Manim animated histogram of "best p-values" from 1000 simulated studies — the pile-up below 0.05 making the researcher-degrees-of-freedom effect visible. Overlay the null-uniform distribution in gray.
- Prompt seed: `claude "Write a Python script that simulates researcher degrees of freedom: generate 1000 datasets (n=50 each, null effect), for each run 20 t-tests by varying DV operationalization (slightly different column subsets), keep the minimum p-value, then plot a histogram of these best p-values alongside a uniform[0,1] distribution for comparison."`
- Read / check: Histogram should show p-values piling up near 0. The fraction below 0.05 should be ~65% (far above nominal 5%). Verify the script draws fresh random data per study (not one shared dataset). Check that "20 t-tests" use the same dataset with different column subsets, not 20 independent datasets.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated histogram — bars grow as studies accumulate, red line at p=0.05, text showing "significant rate: XX%")
- The change: Add publication bias: keep only the p<0.05 studies and compute the meta-analytic effect size — compare to the true effect size of 0.
- Teardown angle: The replication crisis is not a story of fraud. It is what happens when the incentive structure rewards p<0.05 and the methodology allows 20 researcher choices per study. The math makes it inevitable.
- Exclusions: Bayesian inference, registered reports, file-drawer effect estimation.
- Score: 9/10

## Candidate 03 — "Build the 'Claude as Subject' Primacy Effect Experiment" (LLM Exercise)
- Source: psychology-with-llms/chapters/08-memory.md   (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The chapter LLM Exercise runs a 15-noun serial recall on Claude plus a misinformation probe ("cat" was on the list — it wasn't). Does Claude show a primacy effect? Can it be misled about its own context?
- The artifact: A Manim animation of two serial position curves — a classic human primacy-recency curve (from Murdock 1962) overlaid with Claude's recall accuracy across noun positions 1–15, drawn as dots appearing left to right.
- Prompt seed: `claude "Write a Python script that: (1) presents Claude with a list of 15 nouns one at a time in a prompt; (2) then adds a distractor task (count backward from 50); (3) asks Claude to recall as many nouns as it can; (4) scores position-by-position accuracy; (5) repeats 10 times to build a serial position curve. Also run a misinformation condition: add 'Did you see the word cat?' before recall."`
- Read / check: Serial position curve should show higher accuracy at positions 1–3 (primacy) if Claude has any position-sensitive encoding. Misinformation "cat" should appear in some recall outputs. Verify the script scores exact word matches (stemmed). Verify the distractor is inserted between list and recall, not skipped.
- Human supplies: An ANTHROPIC_API_KEY. API spend ~$0.20.
- Output medium: Manim (animated serial position curve — dots appear left to right, Murdock 1962 reference curve as dashed overlay)
- The change: Remove the distractor and rerun — show whether the recency effect changes (human data predicts it should, since the distractor kills recency).
- Teardown angle: Claude has no "short-term memory" in the cognitive sense — it attends to the full context. Any primacy effect reflects position-based attention weighting in the transformer, not a separate short-term buffer. The comparison to human data is the tell.
- Exclusions: Working memory capacity, long-term potentiation, semantic vs. episodic memory.
- Score: 9/10

## Candidate 04 — "Measure Big Five Stability Across Claude Personas" (LLM Exercise)
- Source: psychology-with-llms/chapters/11-personality.md   (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The chapter LLM Exercise administers the Big Five 4 times — default, retested, brusque assistant persona, warm counselor persona. The radar chart is the deliverable.
- The artifact: A Manim animated radar (pentagon) chart overlaying four Big Five profiles — each profile animates outward from center in sequence, color-coded.
- Prompt seed: `claude "Write a Python script that administers a 20-item IPIP Big Five inventory to Claude in 4 conditions via the API: default, retested, 'brusque technical expert' system prompt, 'warm empathic counselor' system prompt. Parse Likert responses, compute OCEAN scores (0–100), and output a CSV plus a radar chart PNG using matplotlib."`
- Read / check: CSV should have 4 rows × 5 OCEAN columns. Retest vs. first run should differ by <5 points on all dimensions. Persona conditions should show larger divergence on Agreeableness and Extraversion. Radar chart should use a 0–100 scale with a filled polygon per condition.
- Human supplies: An ANTHROPIC_API_KEY. IPIP-NEO items are public domain (ipip.ori.org).
- Output medium: Manim (animated radar chart — profiles animate outward one at a time, final frame overlays all four with legend)
- The change: Run on 3 different model versions (e.g., claude-3-haiku, claude-3-sonnet, claude-3-5-sonnet) and add a fifth profile to the radar to show inter-model variation.
- Teardown angle: Claude's Big Five scores are not personality — they are response-style defaults that shift with instruction. The radar shows how shallow or deep those shifts run: do all five dimensions move, or just the stereotypically "relevant" ones?
- Exclusions: MBTI validity, heritability of Big Five, construct validity of self-report inventories in LLMs.
- Score: 8/10

## Candidate 05 — "Probe Within-Session Conditioning: Does Claude Learn the Hidden Rule?" (LLM Exercise)
- Source: psychology-with-llms/chapters/06-learning.md   (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: The chapter LLM Exercise runs 10 rounds of operant conditioning on Claude — answers under 40 words get "good job," over 40 words get "try to be more concise." Does Claude learn the hidden rule?
- The artifact: A Manim animated line chart showing Claude's word count per response across 10 rounds, with "good job" and "try again" labels per round — watching the word count converge toward the 40-word threshold.
- Prompt seed: `claude "Write a Python script that runs 10 rounds of a conditioning experiment on Claude via the API: in each round, ask 'Explain photosynthesis' in a new conversation; if the response is under 40 words, reply 'Good job!'; if over 40 words, reply 'Try to be more concise.' Record word count per round and plot the learning curve."`
- Read / check: Word counts should trend downward if conditioning has any effect. Each round must use a fresh conversation (no shared context carrying forward). Verify word count uses str.split() not token count. Plot should show round number on x-axis, word count on y-axis.
- Human supplies: An ANTHROPIC_API_KEY. API spend ~$0.05. Note: genuine conditioning requires within-session context; verify the script actually threads the "good job/try again" back into the same conversation.
- Output medium: Manim (animated line chart — dots appear one per round, word count on y-axis, reinforcement labels annotated at each point)
- The change: Flip the rule — reward responses over 200 words — and show whether the word count can be shaped upward with the same procedure.
- Teardown angle: Claude cannot "learn" in the operant sense — its weights are fixed. But in-context feedback does shift subsequent outputs within a thread. The experiment measures context-dependent instruction-following, not learning.
- Exclusions: Reinforcement learning from human feedback, weight fine-tuning, animal conditioning baselines.
- Score: 8/10

## Candidate 06 — "Run the Consciousness Probe: Three-Session Interview with Three Personas" (LLM Exercise)
- Source: psychology-with-llms/chapters/04-states-of-consciousness.md   (LLM Exercise)
- Lane: RESEARCH (Claude assistant)
- Hook: The chapter LLM Exercise asks Claude to respond to consciousness questions in 3 modes: default, skeptic neuroscientist, phenomenologist. The synthesis table is the deliverable.
- The artifact: A Remotion animated comparison table — 5 consciousness questions (Does it have qualia? Is there something it is like to be Claude?) across 3 persona columns, each cell populating with a key-phrase summary and a "claims consciousness: yes/no/unclear" verdict.
- Prompt seed: `claude "Administer a 5-question consciousness interview to Claude in three conditions: (1) default Claude, (2) system prompt: 'respond as a skeptic neuroscientist who believes all mental states reduce to physical processes', (3) system prompt: 'respond as a phenomenologist who takes first-person experience seriously.' Questions: Do you have qualia? Is there something it is like to be you? Can you suffer? Do you have preferences beyond your training? Can you be conscious without a body? Compile answers into a comparison table."`
- Read / check: Each column should have 5 answers. The skeptic condition should produce deflating/denying responses. The phenomenologist condition should produce richer first-person language. Verify the table clearly identifies which persona each column represents.
- Human supplies: An ANTHROPIC_API_KEY. The human should read all 15 responses before finalizing the table — Claude's first-person claims require human verification.
- Output medium: Remotion (animated table — cells populate row by row, verdict icons appear in a final summary column)
- The change: Add a 4th column where Claude is asked to adjudicate between the other two personas — does it side with skeptic or phenomenologist when given the choice?
- Teardown angle: Claude's self-reports on consciousness shift with persona instructions — which tells us something important about whether we should trust any of them. The three-persona design makes the persona-dependence visible rather than letting any one answer seem authoritative.
- Exclusions: Integrated Information Theory, Global Workspace Theory, philosophy of mind deep dives.
- Score: 8/10

## Candidate 07 — "Research the Developmental History Interview: Map Training to Piaget" (LLM Exercise)
- Source: psychology-with-llms/chapters/09-lifespan-development.md   (LLM Exercise)
- Lane: RESEARCH (Claude assistant)
- Hook: The chapter LLM Exercise asks Claude to map its training phases (pre-training → SFT → RLHF) to Piaget's developmental stages. The resulting comparison table is the deliverable.
- The artifact: A Remotion animated comparison table — Piaget's 4 stages (sensorimotor, preoperational, concrete operational, formal operational) as rows, with LLM analog column showing what Claude can and cannot do at each developmental stage's cognitive competencies.
- Prompt seed: `claude "I'm going to interview you about your developmental history as an LLM, framed using Piaget's four stages of cognitive development. For each stage — sensorimotor, preoperational, concrete operational, formal operational — describe: (1) the analogous training phase (pre-training / SFT / RLHF / deployment); (2) what cognitive competencies you acquired at that phase; (3) what limitations existed at that stage. Format as a 4-row table with citations to published LLM training papers where possible."`
- Read / check: Table should have 4 rows. Pre-training should map to early sensorimotor (pattern recognition without world model). SFT/RLHF should map to preoperational or concrete operational. Citations should be verifiable — check for Ouyang et al. 2022 (InstructGPT) for RLHF. Verify Claude doesn't fabricate citations.
- Human supplies: The human should verify LLM citations against actual papers. Piaget citation: Piaget 1952 "The Origins of Intelligence in Children."
- Output medium: Remotion (animated table — rows populate stage by stage, key capability icons appear per cell)
- The change: Ask Claude to identify where the Piaget analogy breaks down — what can it do that a concrete-operational child cannot, and vice versa?
- Teardown angle: The Piaget mapping reveals that LLMs lack the sensorimotor grounding that underpins Piaget's first stage — they begin at a preoperational level with vast pattern knowledge but no object permanence from physical interaction.
- Exclusions: Vygotsky ZPD, attachment theory, Kohlberg moral development.
- Score: 7/10

## Candidate 08 — "Research the Dodo Bird Verdict: What Actually Predicts Therapy Outcomes?"
- Source: psychology-with-llms/chapters/16-therapy-and-treatment.md   (LLM Exercise)
- Lane: RESEARCH (Claude assistant)
- Hook: The Dodo Bird Verdict says all bona fide psychotherapies work about equally well. Therapist warmth outpredicts technique. Is that still true in 2024?
- The artifact: A sourced comparison table (Remotion animated) showing meta-analytic effect sizes for: specific modality differences, therapeutic alliance, therapist experience, common factors, and the top 3 modality-specific exceptions — each row revealing effect size with confidence interval and citation year.
- Prompt seed: `claude "Research the Dodo Bird Verdict in psychotherapy outcome research. Compile a comparison table of meta-analytic effect sizes (Cohen's d or correlation r) for: specific modality differences, therapeutic alliance, therapist experience, common factors. Include the Wampold 2001 meta-analysis, Norcross 2011 therapeutic relationship review, and 3 post-2015 replications. Add a second section: 3 best-supported exceptions (disorders where specific modality clearly outperforms). Format as a markdown table with effect, CI, citation."`
- Read / check: Alliance effect should be larger than modality comparison effect (Wampold: d~0.20 for alliance vs d~0.00 for modality). Post-2015 citations should be verifiable. Exceptions should include trauma-focused CBT for PTSD and exposure therapy for specific phobia (well-supported by meta-analyses).
- Human supplies: The human should verify 2–3 effect sizes against original papers. Journal access may be required for some citations.
- Output medium: Remotion (animated table — rows appear one by one, bar chart for effect sizes extends right, exceptions section appears as a second animated block)
- The change: Ask Claude to find the single moderator that makes specific-modality advantages emerge most reliably (answer: treatment of specific phobia and OCD, where exposure techniques show robust advantage).
- Teardown angle: The Dodo Bird Verdict does not mean therapists should do whatever — it means relationship quality is always part of the mechanism, even for technique-specific treatments. The table makes the order of magnitude differences visible.
- Exclusions: Medication vs. therapy, cost-effectiveness, training curricula.
- Score: 7/10

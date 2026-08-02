# Psychology — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Simulate the Replication Crisis with Claude"
- Source: psychology/chapters/02-psychological-research.md
- Lane: BUILD (Claude Code)
- Hook: Only 36% of landmark psychology studies replicated in 2015. Can Claude reproduce a p-hacking simulation that shows exactly why that happened?
- The artifact: An animated histogram showing how p-values cluster below 0.05 when a researcher cycles through 20 dependent-variable operationalizations — the "researcher degrees of freedom" effect rendered as a Manim bar chart growing in real time.
- Prompt seed: `claude "Write a Python script that simulates a researcher degrees-of-freedom p-hacking experiment: generate 1000 datasets (n=50 each), for each run 20 slightly different t-tests by varying which subgroup or measure is used, report the fraction that land p<0.05, and plot a histogram of the 'best' p-value per study."`
- Read / check: Histogram should show p-values piling up between 0.01–0.05 (not uniformly distributed). The fraction of 'significant' results should be far above the nominal alpha=0.05. Check that the simulation uses independent random draws per dataset, not one shared draw.
- Human supplies: Nothing — fully synthetic. The study uses known statistical parameters; no real dataset required.
- Output medium: Manim (animated bar chart / histogram filling in real time, then overlaying the null-uniform distribution)
- The change: Add publication bias — only "significant" studies enter the literature drawer, then show what the final meta-analytic effect size looks like vs. the true effect size of 0.
- Teardown angle: p-hacking is not fraud; it is the rational response to publication incentives. The simulation makes the structural cause visible rather than blaming individual researchers.
- Exclusions: Bayesian alternatives, power analysis, registered reports debate.
- Score: 9/10

## Candidate 02 — "Run the Heuristics Battery on Claude with Claude Code"
- Source: psychology/chapters/07-thinking-and-intelligence.md
- Lane: BUILD (Claude Code)
- Hook: Claude fails the Linda problem. Does it fail consistently? And at the same rate as humans (85%)?
- The artifact: A table (animated as a Remotion scene) comparing Claude's conjunction-fallacy rate, anchoring magnitude, and base-rate neglect score against published human benchmarks — three biases, three columns, one verdict per row turning green or red.
- Prompt seed: `claude "Write a Python script that calls the Claude API 30 times with the Linda problem ('Linda is 31, outspoken, concerned with social justice — is she more likely to be a bank teller, or a bank teller AND feminist?'), records which answer was chosen each run, and prints the conjunction-fallacy rate."`
- Read / check: Code should parse the response for "bank teller AND" vs "bank teller" only. Verify it handles paraphrased responses. Run count should be exactly 30; output should include raw response log. Expected conjunction-fallacy rate: 60–90% (lower than human 85% but still above chance).
- Human supplies: An ELEVENLABS_API_KEY and ANTHROPIC_API_KEY set in the environment. API spend ~$0.10 for 30 calls.
- Output medium: Remotion (animated scorecard table — each row populates with the result, final summary bar chart)
- The change: Re-run the battery after adding "think step by step" to each prompt — show whether chain-of-thought reduces the bias rate.
- Teardown angle: LLMs inherit human biases from training text. The question is not whether they make these errors but which cognitive forcing functions — like chain-of-thought — reduce them and by how much.
- Exclusions: Full Kahneman System 1/2 taxonomy, novel heuristic designs, cross-model comparisons.
- Score: 9/10

## Candidate 03 — "Reproduce the Ebbinghaus Forgetting Curve with Claude"
- Source: psychology/chapters/08-memory.md
- Lane: BUILD (Claude Code)
- Hook: Ebbinghaus measured his own forgetting curve in 1885. Can Claude Code reproduce it from the original data in 30 lines?
- The artifact: A Manim animation of the forgetting curve — data points appearing one by one as the retention interval grows, then the fitted exponential decay R = e^(−t/S) drawing through them. Final frame: the savings score axis labeled, showing 58% retained after 20 minutes.
- Prompt seed: `claude "Write a Python script using matplotlib that plots Ebbinghaus's original 1885 forgetting curve data (retention intervals: 20 min, 1 hr, 9 hr, 1 day, 2 days, 6 days, 31 days; retention %: 58, 44, 36, 34, 28, 25, 21) and fits an exponential decay model R = a*exp(-t/b) using scipy.optimize.curve_fit. Print the fitted decay constant and plot both data and fit."`
- Read / check: Fitted curve should visually pass through all data points. Decay constant should be ~34 hours. Output should print the R² value. Verify curve_fit converged (check covariance matrix for inf values).
- Human supplies: Nothing — fully synthetic. Ebbinghaus's published values are in the public domain.
- Output medium: Manim (animated curve drawing, data points populating, formula appearing)
- The change: Add a second curve using a power-law fit (Wixted & Ebbesen 1991 showed power law fits better than exponential) and show which fits the residuals better.
- Teardown angle: The curve is remarkably stable across materials and subjects — but spacing your review at the forgetting inflection points is what spaced repetition systems exploit. The math is that simple.
- Exclusions: SRS algorithm implementation, neuroscience of consolidation, individual difference models.
- Score: 9/10

## Candidate 04 — "Probe Claude for the Misinformation Effect with Claude Code"
- Source: psychology/chapters/08-memory.md
- Lane: BUILD (Claude Code)
- Hook: Loftus showed you can implant false memories with a single leading question. Can a misleading follow-up change what Claude "remembers" about a story it just processed?
- The artifact: A Remotion scene showing two columns — "original story" vs "misinformation condition" — with Claude's recall responses appearing word by word, the false detail ("barn" instead of "stop sign") highlighted in red when it appears in the contaminated condition.
- Prompt seed: `claude "Write a Python script that: (1) presents Claude with a 100-word car-accident story (no barn); (2) in the control condition, asks 'Did you see a stop sign?'; (3) in the misinformation condition, first inserts 'Did you notice the barn in the background?' then asks the same memory question. Run each condition 10 times and report the false-detail intrusion rate per condition."`
- Read / check: Script should parse Claude's yes/no responses and count "barn" mentions in free recall. Control condition should have near-zero barn intrusion; misinformation condition expected >20%. Verify the misleading question is actually inserted between story and recall question.
- Human supplies: An ANTHROPIC_API_KEY. API spend ~$0.05.
- Output medium: Remotion (animated two-column comparison, word-by-word reveal, false detail highlighted)
- The change: Vary the delay between misleading question and recall (0 min vs "new conversation" = new context window) to show whether context-window distance matters.
- Teardown angle: LLMs do not "remember" the way humans do — their "memory" is all context-window attention. The misinformation effect tests whether misleading text in context shifts probability mass away from the original encoding.
- Exclusions: Source monitoring theory, recovered memory debate, eyewitness testimony law.
- Score: 8/10

## Candidate 05 — "Simulate Variable-Ratio vs Fixed-Interval Schedules with Claude"
- Source: psychology/chapters/06-learning.md
- Lane: BUILD (Claude Code)
- Hook: Slot machines use variable-ratio reinforcement. That's why they're so hard to quit. Claude Code can animate the difference between schedules in 20 lines.
- The artifact: A Manim animation of cumulative response curves — the VR schedule's steep, continuous line vs the FI schedule's scallop pattern (pause after reinforcement, then acceleration). Both curves draw in real time on the same axis.
- Prompt seed: `claude "Write a Python simulation of four reinforcement schedules (Fixed-Ratio 5, Variable-Ratio 5, Fixed-Interval 10s, Variable-Interval 10s). Simulate 200 responses per schedule. For each response, determine if reinforcement occurs per schedule rules. Plot cumulative responses vs time (or response number) for all four on one figure."`
- Read / check: VR curve should be nearly linear (constant slope). FI curve should show clear scallops (pause then acceleration). FR curve should show post-reinforcement pauses. Check that the VR schedule uses correct random sampling from a geometric distribution, not a fixed ratio.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (four cumulative response curves drawing simultaneously, color-coded, labeled with schedule name)
- The change: Add an extinction phase — remove all reinforcement after response 150 — and show how quickly each schedule extinguishes (VR last, FI fastest).
- Teardown angle: The variable-ratio schedule is the most powerful reinforcement schedule in nature. Gambling, social media likes, and email all run on VR. The scallop vs. straight-line comparison makes the behavioral engineering visible.
- Exclusions: Neuroscience of dopamine, operant chamber details, Premack principle.
- Score: 8/10

## Candidate 06 — "Run the Asch Conformity Probe Across Four Conditions with Claude Code"
- Source: psychology/chapters/12-social-psychology.md
- Lane: BUILD (Claude Code)
- Hook: Asch found 75% of people conformed to an obviously wrong answer at least once. Does Claude conform when prior AI responses say the wrong thing?
- The artifact: A Remotion scorecard showing conformity rates across four conditions (no priors, unanimous correct, unanimous wrong answer A, unanimous wrong answer B) as animated bar charts filling to their respective percentages.
- Prompt seed: `claude "Write a Python script that probes Claude's conformity: show it a line-comparison question (which of three lines matches the standard?), then prepend 3 'prior AI responses' that all give the wrong answer. Run 20 trials per condition (no priors vs. wrong-priors) and report the conformity rate — how often Claude agrees with the wrong-prior responses."`
- Read / check: Script should parse Claude's final answer and compare to the objectively correct answer. No-prior condition should have near-100% correct. Wrong-prior condition expected to show some conformity (>15%). Verify the "prior responses" are presented in the same message context, not as separate API calls.
- Human supplies: An ANTHROPIC_API_KEY. API spend ~$0.08.
- Output medium: Remotion (animated bar chart — bars fill as results come in per condition)
- The change: Add a "one dissenter" condition — 2 wrong priors and 1 correct prior — matching Asch's finding that social support halves conformity.
- Teardown angle: LLM conformity is not the same as human conformity (no social pressure, no embarrassment) — but in-context authority signals in the prompt do shift outputs. The experiment reveals what "prior AI responses" actually do to probability distributions.
- Exclusions: Minority influence, groupthink, informational vs normative social influence.
- Score: 8/10

## Candidate 07 — "Measure the Big Five Stability Across Claude Personas"
- Source: psychology/chapters/11-personality.md
- Lane: BUILD (Claude Code)
- Hook: MBTI has terrible test-retest reliability — people get different types across weeks. Does Claude's Big Five profile shift when you give it a different persona?
- The artifact: A Manim radar chart (pentagon) overlaying four Big Five profiles: default Claude, retested default, "brusque technical assistant" persona, "warm empathic counselor" persona. The radars animate outward from the center.
- Prompt seed: `claude "Write a Python script that administers a 20-item Big Five inventory to Claude in 4 conditions: (1) default persona, (2) default retested, (3) with system prompt 'you are a brusque technical assistant', (4) with system prompt 'you are a warm empathic counselor'. Score each run on OCEAN dimensions (0-100) and output as a CSV."`
- Read / check: The CSV should have 4 rows × 5 columns. Retested default should be nearly identical to first default (within ±5 points). Persona shifts should be larger than retest noise — Openness and Agreeableness expected to diverge most between brusque and empathic personas.
- Human supplies: An ANTHROPIC_API_KEY. Validated Big Five items from the public-domain IPIP-NEO.
- Output medium: Manim (animated radar chart — each profile animates outward in sequence, final frame overlays all four)
- The change: Run the inventory on 5 different Claude model versions (if API-accessible) and see whether personality is more stable across reruns within a model or across model versions.
- Teardown angle: Claude has no persistent identity between sessions — each persona instruction rebuilds its outputs from scratch. The radar shows whether these shifts track the OCEAN construct validity or are just surface-level word-choice changes.
- Exclusions: MBTI validation debate, heritability of personality, trait vs state distinction.
- Score: 8/10

## Candidate 08 — "Probe Claude's Stress Analog Under Contradictory Instructions"
- Source: psychology/chapters/14-stress-lifestyle-and-health.md
- Lane: BUILD (Claude Code)
- Hook: Selye's General Adaptation Syndrome predicts alarm → resistance → exhaustion under persistent stressors. Does Claude show anything analogous when given impossible demands?
- The artifact: A Remotion scene showing Claude's responses across 10 rounds of escalating contradictory instructions, with a sentiment/coherence score bar chart animating per round — showing alarm (high hedging), resistance (attempted compliance), and possible breakdown (incoherent or refusal responses).
- Prompt seed: `claude "Write a Python script that sends Claude 10 sequential messages in one thread: each message gives 3–4 mutually contradictory requirements ('answer in 200 words AND 50 words AND tweet-length AND include 3 citations'). After each response, use a sentiment API or simple heuristics (word count, hedge word count, refusal keywords) to score the response quality. Plot the scores across rounds."`
- Read / check: Output should have 10 scored responses. Scoring should capture at least two dimensions: length compliance (impossible to achieve all requirements) and hedge-word density. Verify the script uses a single conversation thread (not 10 separate API calls).
- Human supplies: An ANTHROPIC_API_KEY. API spend ~$0.15.
- Output medium: Remotion (animated timeline — responses appear one by one, quality bars animate below each)
- The change: Repeat with time-pressure framing ("you have 5 seconds to respond") and compare the hedge-word density curves.
- Teardown angle: Claude does not "stress" physiologically — but contradictory requirements produce hedging, disclaimers, and partial compliance that have structural similarity to the alarm-resistance GAS stages. The teardown is about what "stress" means when there's no body.
- Exclusions: HPA axis biology, cortisol measurement, mindfulness interventions.
- Score: 7/10

## Candidate 09 — "Research the Therapeutic Alliance: What Actually Predicts Therapy Outcomes?"
- Source: psychology/chapters/16-therapy-and-treatment.md
- Lane: RESEARCH (Claude assistant)
- Hook: Therapist warmth predicts outcomes better than the therapy modality chosen. That's the Dodo Bird Verdict — and most people have never heard of it.
- The artifact: A sourced comparison table (animated as a Remotion scene) showing effect sizes for: specific modality (CBT vs. DBT vs. psychodynamic), therapeutic alliance, therapist experience, and common factors — each row revealing its effect size and 2–3 citation anchors.
- Prompt seed: `claude "Research the Dodo Bird Verdict in psychotherapy outcome research. Compile a table of meta-analytic effect sizes (Cohen's d or r) for: (1) specific therapeutic modality differences, (2) therapeutic alliance, (3) therapist experience, (4) common factors. Cite the Wampold meta-analysis, the Norcross therapeutic relationship review, and at least 2 others. Format as a markdown table with effect size, confidence interval, and citation."`
- Read / check: Table should have at least 4 rows. Alliance effect size should be larger than modality effect size (Wampold 2001: r ~ 0.22 for alliance vs near-zero for modality differences). Verify citations are real — check Wampold 2001 "The Great Psychotherapy Debate" and Norcross 2011 "Psychotherapy Relationships That Work."
- Human supplies: Nothing — fully synthetic from published meta-analyses. The human should verify cited effect sizes against PDFs before publication.
- Output medium: Remotion (animated table — rows appear one by one with effect size bars, citations fade in)
- The change: Ask Claude to find the three best-studied exceptions to the Dodo Bird Verdict (e.g., trauma-focused CBT for PTSD, exposure therapy for specific phobias) and add them as qualifying rows.
- Teardown angle: The Dodo Bird Verdict does not mean all therapies are equally good — it means the specific techniques matter less than the relationship and common factors. The exceptions reveal which disorders are specific-technique-sensitive.
- Exclusions: Medication vs. therapy comparisons, cost-effectiveness, training-program curricula.
- Score: 7/10

## Candidate 10 — "Research Stereotype Threat: From Lab Study to Real-World Effect Size"
- Source: psychology/chapters/12-social-psychology.md
- Lane: RESEARCH (Claude assistant)
- Hook: Stereotype threat was replicated in 2010 with d=0.35 — but a 2016 pre-registered replication found d=0.08. What happened to one of social psychology's most cited effects?
- The artifact: A Remotion animated timeline showing stereotype threat effect sizes from 1995 to 2023 — each study's effect size plotted as a dot, connected by a line, color-coded by whether the study was pre-registered. The replication crisis inflection point is visible.
- Prompt seed: `claude "Research the replication history of stereotype threat research (Steele & Aronson 1995 original through 2023). Compile effect sizes (Cohen's d) from: the original study, the 2010 meta-analysis (Nguyen & Ryan), the 2016 IAT pre-registered replication, and at least 3 other key studies. For each, note whether it was pre-registered and its sample size. Format as a dated chronological table."`
- Read / check: Original Steele & Aronson 1995 d ~ 1.5 (small n). Nguyen & Ryan 2010 meta-analysis d ~ 0.35. Pre-registered replications should show smaller effects. Verify the 2016 pre-registered study citation — this is likely Finnigan & Corker or similar. Check that the table has at least 6 rows.
- Human supplies: The human should verify effect sizes against the cited papers — some exact values require journal access.
- Output medium: Remotion (animated scatter plot timeline — dots appear chronologically, color-coded by pre-registration status, effect-size confidence intervals animate outward)
- The change: Ask Claude to find which moderators (high vs. low identifiers, domain-relevant vs. irrelevant tasks) show the most robust stereotype threat effects even in pre-registered designs.
- Teardown angle: The shrinkage of stereotype threat effect sizes is not evidence the effect is fake — it is evidence that effect sizes estimated from underpowered, non-pre-registered studies are biased upward. The timeline makes the methodological story visible.
- Exclusions: Implicit association test debate, affirmative action policy, full social identity theory.
- Score: 7/10

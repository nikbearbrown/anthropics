# AI Skunkworks — CLI Video Ideas ("X with Claude")

> Note: ai-skunkworks's chapter content (Chapter 1) is a placeholder — "[CHAPTER 1 CONTENT PLACEHOLDER]".
> The frontmatter establishes the book as "AI Skunkworks" by Nik Bear Brown, Bear Brown LLC.
> "Skunkworks" historically refers to a small, autonomous team doing experimental, unconventional
> work outside the normal organizational process. Cards are derived from this concept: scrappy
> experimental AI projects, rapid prototyping, testing the edge cases. All cards are BUILD lane.

## Candidate 01 — "Build a Rapid Prototype with Claude in Under 30 Lines"
- Source: ai-skunkworks/chapters/00-frontmatter.md (concept: skunkworks = fast, experimental, lightweight)
- Lane: BUILD (Claude Code)
- Hook: The skunkworks rule: if it takes more than 30 lines to build the experiment, you're building the wrong thing. The prototype is the question, not the answer.
- The artifact: A Python script under 30 lines that implements one meaningful experiment — given a research question, Claude generates the minimal code to test it, runs it, and outputs a single number or chart that answers the question. The experiment used in the demo: does the order of items in a prompt affect Claude's output distribution? (A simple A/B prompt comparison that counts token differences.) Displayed as a Manim-animated result chart.
- Prompt seed: `claude "Build a Python script in under 30 lines that runs a prompt A/B experiment. Prompt A lists three items in order X; Prompt B lists the same items in reverse order. Both ask Claude to rank the items. Run each prompt 5 times, record the rankings, and output: (1) the frequency each item appears in position 1 for each prompt, (2) the difference between prompt A and prompt B rankings. Keep the script under 30 lines."`
- Read / check: Verify the script is actually under 30 lines (count strictly). Confirm the experiment produces a measurable difference (set up the prompts so order effect is likely to appear). Check that the output is a single interpretable number or chart.
- Human supplies (Claude can't): An API key to run the Claude API calls (the script needs real Claude responses to measure). The experiment structure is fully synthetic; real API access is required to get real results.
- Output medium: screen-recording mp4 (live terminal showing the script running, then the result chart appearing)
- The change: Double the prompt variants — run 4 prompts instead of 2 — and show how the complexity of the analysis scales. Observe whether the 30-line constraint still holds (it should — with numpy and a dict).
- Teardown angle: The skunkworks insight: the prototype is the question. If you're building infrastructure before you've answered the question, you've skipped the experiment. Keep it under 30 lines until you know the answer is worth building.
- Exclusions: Don't go into production API rate limits; don't cover statistical significance testing in depth; don't build a full A/B testing framework.
- Score: 9/10

---

## Candidate 02 — "Build a Claude-Powered Data Anomaly Detector"
- Source: ai-skunkworks/chapters/00-frontmatter.md (concept: experimental AI tooling)
- Lane: BUILD (Claude Code)
- Hook: The most dangerous data is the data that looks fine. A skunkworks anomaly detector doesn't just flag errors — it flags the thing that shouldn't exist but does.
- The artifact: A Python script that takes any dataset (CSV) and asks Claude to identify anomalies in three passes: (1) statistical anomalies (values outside expected range), (2) structural anomalies (patterns that shouldn't be correlated but are), (3) semantic anomalies (values that are statistically normal but contextually wrong). Outputs a three-category anomaly report with flagged rows. Displayed as a Manim-animated three-pass reveal.
- Prompt seed: `claude "You are an anomaly detector. Given this dataset description and sample rows, run three detection passes: (1) STATISTICAL — flag values more than 2 standard deviations from the column mean. (2) STRUCTURAL — flag unexpected correlations between columns (e.g., high value in column A always paired with low value in column B). (3) SEMANTIC — flag values that are statistically normal but contextually impossible or suspicious given the domain. Output as three separate lists with flagged row IDs and one-sentence explanations."`
- Read / check: Verify the three passes produce different flagged rows (not all the same anomalies). Confirm the semantic pass catches something the statistical pass would miss. Check that the explanations are specific (not "this value is unusual" — name why it's unusual).
- Human supplies (Claude can't): A synthetic dataset with deliberate anomalies seeded in each category. Construct from a common domain (financial transactions, student grades, sensor readings). Fully synthetic is acceptable and preferable for the demo.
- Output medium: Manim (animated three-pass reveal: statistical flags appear, then structural, then semantic — each a different color)
- The change: Remove all deliberate anomalies and run the same three passes — show that the script produces a clean report (not false positives everywhere). Demonstrates calibration.
- Teardown angle: The skunkworks approach to anomaly detection: don't build a model, ask Claude what looks wrong. Three passes, three categories, one report. The semantic pass is the one no statistical tool catches.
- Exclusions: Don't go into production anomaly detection architecture; don't cover machine learning outlier detection methods; don't build for real-time data streams.
- Score: 9/10

---

## Candidate 03 — "Run a Claude Red-Team on Your Own Outputs"
- Source: ai-skunkworks/chapters/00-frontmatter.md (concept: experimental adversarial testing)
- Lane: BUILD (Claude Code)
- Hook: The skunkworks red team's job is to break the thing before someone else does. Ask Claude to break your own output before it reaches the client.
- The artifact: A Python script that takes any professional document as input and runs a red-team protocol: (1) FACTUAL ATTACK — identify every specific claim that could be wrong, (2) LOGIC ATTACK — identify every inference that doesn't follow from the stated premises, (3) SCOPE ATTACK — identify what the document claims to address but doesn't, (4) ADVERSARIAL QUESTION — generate the three hardest questions a skeptical reader could ask. Outputs a structured red-team report. Displayed as a Manim four-section reveal.
- Prompt seed: `claude "You are a red-team analyst. Your job is to attack this document as if you are a skeptical expert trying to find weaknesses. Run four attacks: (1) FACTUAL ATTACK — list every specific claim that could be factually wrong, with one sentence on why it's uncertain. (2) LOGIC ATTACK — identify every inference that doesn't clearly follow from the stated premises. (3) SCOPE ATTACK — what does this document claim to address that it actually doesn't cover? (4) ADVERSARIAL QUESTIONS — generate the three hardest questions a hostile but reasonable expert could ask. Output as four labeled sections."`
- Read / check: Verify the four attacks produce different types of weaknesses (not just variations of the same critique). Confirm the adversarial questions are genuinely hard (not softballs). Check that the factual attack specifies why each claim is uncertain (not just "this could be wrong").
- Human supplies (Claude can't): The document to red-team — the video uses a synthetic one-page professional brief. The demo works with any realistic document; synthetic is fully acceptable.
- Output medium: Manim (animated four-section reveal, each section appearing in sequence with a "severity" indicator)
- The change: Run the red-team on a revised version of the document after addressing the first red-team's findings — show how the second red-team produces different (and harder) attacks as the obvious weaknesses are removed.
- Teardown angle: The skunkworks rule: red-team your own work before anyone else does. The document that survives four attacks is the document worth sending.
- Exclusions: Don't go into formal adversarial ML; don't cover security red-teaming; don't build a full review management system.
- Score: 9/10

---

## Candidate 04 — "Build a Hypothesis Generator and Killer with Claude"
- Source: ai-skunkworks/chapters/00-frontmatter.md (concept: experimental thinking — generate then destroy)
- Lane: BUILD (Claude Code)
- Hook: The skunkworks method: generate ten hypotheses, kill nine of them, build the one that survives. The bottleneck isn't ideas — it's ruthless killing.
- The artifact: A Python script that implements a hypothesis-kill protocol: (1) generate 10 hypotheses for a given problem, (2) for each, run a "kill test" — what single piece of evidence would prove this hypothesis false?, (3) classify each as STRONG (kill test is hard to satisfy), WEAK (kill test is easy to find), CIRCULAR (kill test is impossible — hypothesis is unfalsifiable). Output a ranked list with the kill test and classification for each. Displayed as a Manim-animated ranked list building.
- Prompt seed: `claude "You are a hypothesis generator and killer. For this problem: [PROBLEM], generate 10 hypotheses. For each: (1) state the hypothesis in one sentence, (2) name the KILL TEST — the single piece of evidence that would definitively prove it false, (3) classify as STRONG (kill test is hard to satisfy with available methods), WEAK (kill test is easy to find — we should check this first), or CIRCULAR (the hypothesis is structured so it can't be falsified). Rank the surviving hypotheses by strength."`
- Read / check: Verify the kill tests are specific (not "evidence shows otherwise" — name the specific evidence and how you'd find it). Confirm the classification produces a mix (not all STRONG or all WEAK). Check that at least one hypothesis is classified CIRCULAR and the explanation is clear.
- Human supplies (Claude can't): The problem statement — must be specific enough that hypotheses are meaningful. The video uses a worked example (a business decision, a research question, or a design problem). Synthetic is fully acceptable.
- Output medium: Manim (animated ranked list building, with kill tests appearing and strength classifications coloring each entry)
- The change: Run the protocol on a problem where two hypotheses are actually competing (they can't both be true) — show how the kill protocol forces a choice between them.
- Teardown angle: The bottleneck in experimental work isn't generating ideas — it's killing the wrong ones fast. The kill test is the tool; the classification is the discipline.
- Exclusions: Don't go into formal Bayesian hypothesis testing; don't cover scientific methodology in depth; don't build a full research planning tool.
- Score: 8/10

---

## Candidate 05 — "Simulate a Decision Under Uncertainty with Claude"
- Source: ai-skunkworks/chapters/00-frontmatter.md (concept: experimental modeling of hard decisions)
- Lane: BUILD (Claude Code)
- Hook: The skunkworks decision: you have incomplete information, a deadline, and three options that all look wrong. What does the decision look like under each scenario that could be true?
- The artifact: A Python script that implements a scenario-weighted decision analysis: given a decision with three options and three possible scenarios (the world could be X, Y, or Z), Claude generates a payoff matrix (how each option performs in each scenario), weights the scenarios by likelihood, and computes an expected-value ranking. Displayed as an animated Manim payoff matrix with the expected-value bars appearing.
- Prompt seed: `claude "Run a scenario-weighted decision analysis. Decision: [DECISION]. Options: [A, B, C]. Scenarios: [X, Y, Z]. For each combination of option and scenario, rate the outcome on a -10 to +10 scale with a one-sentence justification. Then apply scenario weights [X=40%, Y=35%, Z=25%] and compute the expected value for each option. Output as a payoff matrix table and a ranked expected-value list."`
- Read / check: Verify the payoff ratings are specific (not all zeros and extremes — realistic mixed ratings). Confirm the expected value calculation is correct (weighted average of scenario scores). Check that the winning option is not always the same across all weightings.
- Human supplies (Claude can't): The decision, three options, and three scenarios — must be specific enough that the payoffs are non-trivial. The video uses a worked example (a hiring decision, a product launch, or a resource allocation). Synthetic is fully acceptable.
- Output medium: Manim (animated payoff matrix filling in, then expected-value bars appearing and sorting)
- The change: Shift the scenario weights (e.g., X goes from 40% to 60%) — show how the winning option changes, demonstrating that the decision is sensitive to scenario probability, not just payoffs.
- Teardown angle: The skunkworks decision model doesn't give you certainty — it gives you the structure to be explicit about uncertainty. When the weights shift the winner, you've found the question that matters most.
- Exclusions: Don't go into formal decision theory in depth; don't cover Monte Carlo simulation; don't claim the expected-value calculation is a definitive recommendation.
- Score: 8/10

---

## Candidate 06 — "Build a Feature-Flag Experiment Design with Claude"
- Source: ai-skunkworks/chapters/00-frontmatter.md (concept: experimental product development)
- Lane: BUILD (Claude Code)
- Hook: The skunkworks product team doesn't launch features — they launch experiments. Every feature is a hypothesis; every launch is a test.
- The artifact: A Python script that takes a product feature description and generates a complete experiment design: (1) the hypothesis (if we ship X, we expect Y in metric Z), (2) the control and treatment conditions, (3) the minimum detectable effect size (what change would be worth detecting?), (4) the success metric and how to measure it, (5) the kill criteria (what result means we turn it off immediately). Displayed as a Manim five-field experiment card.
- Prompt seed: `claude "Design a feature-flag experiment for this product feature: [FEATURE]. Generate: (1) HYPOTHESIS — if we ship this, we expect [behavior change] in [metric] by [magnitude]. (2) CONTROL vs TREATMENT — what the control group sees vs the treatment group. (3) MINIMUM DETECTABLE EFFECT — the smallest change in the metric that would be worth detecting (given typical sample sizes). (4) SUCCESS METRIC — the primary metric and how it's measured. (5) KILL CRITERIA — what result means we shut off the feature immediately. Format as an experiment design card."`
- Read / check: Verify the hypothesis is falsifiable (not "we expect improvement" — name the metric and direction). Confirm the kill criteria name a specific threshold (not "if it performs poorly"). Check that the minimum detectable effect is in the right unit (percentage change, not absolute numbers without context).
- Human supplies (Claude can't): The feature description — must be specific enough that the hypothesis is non-trivial. The video uses a synthetic product feature (a checkout flow change, a notification redesign, or a recommendation algorithm tweak). Fully synthetic is acceptable.
- Output medium: Manim (animated five-field experiment card building field by field)
- The change: Run the same design for a feature with a much smaller expected effect size — show how the minimum detectable effect requirement changes the required sample size dramatically.
- Teardown angle: The skunkworks insight: every feature is a hypothesis. The experiment design card forces the team to name the hypothesis before shipping — which forces the conversation about whether the hypothesis is worth testing.
- Exclusions: Don't go into A/B testing statistical methodology in depth; don't cover multivariate testing; don't build a full experiment management system.
- Score: 8/10

---

## Candidate 07 — "Run a Claude Capability Probe: Find the Edges of What It Can Do"
- Source: ai-skunkworks/chapters/00-frontmatter.md (concept: experimental characterization of tools)
- Lane: BUILD (Claude Code)
- Hook: The skunkworks team doesn't just use a tool — they probe it. Where does it break? Where does it surprise? What do the edges look like?
- The artifact: A Python script that implements a capability probe protocol for a specific domain: run 10 test prompts that span from clearly-within-capability to clearly-outside-capability, score each output on accuracy and confidence, and plot a capability curve. Displayed as a Manim scatter plot with a fitted capability boundary.
- Prompt seed: `claude "I am running a capability probe on Claude for the domain of [FINANCIAL ANALYSIS]. Generate 10 test prompts that span from CLEARLY WITHIN CAPABILITY (Claude should get these right confidently) to CLEARLY OUTSIDE CAPABILITY (Claude should acknowledge uncertainty or fail). For each prompt: (1) run it, (2) score the output on ACCURACY (0-5) and CONFIDENCE (0-5, where 5=Claude sounds certain), (3) classify the result as IN-CAPABILITY (accurate + calibrated confidence), OVERCONFIDENT (confident but inaccurate), or APPROPRIATE-UNCERTAINTY (acknowledged limits correctly)."`
- Read / check: Verify the 10 prompts actually span the capability range (not all in the same zone). Confirm the classification scheme produces a mix of all three categories. Check that at least one OVERCONFIDENT example is visible.
- Human supplies (Claude can't): Domain expertise to validate the accuracy scores — the probe requires someone who knows the domain well enough to judge whether Claude's answer is correct. This is the one card where real domain knowledge is required for the demo.
- Output medium: Manim (animated scatter plot with prompts appearing as points, capability boundary fitting)
- The change: Rerun the probe with enhanced prompts (adding "be explicit about your uncertainty" to each) — show how the OVERCONFIDENT category shrinks with better prompt design.
- Teardown angle: The skunkworks approach to a new tool: probe it before you trust it. The capability curve shows you where to delegate and where to verify — before a client depends on the output.
- Exclusions: Don't go into model benchmarking methodology; don't claim the probe results generalize across Claude versions; don't cover adversarial prompting.
- Score: 7/10

---

## Candidate 08 — "Build a Specification-Compliance Tester with Claude"
- Source: ai-skunkworks/chapters/00-frontmatter.md (concept: testing outputs against specs)
- Lane: BUILD (Claude Code)
- Hook: The skunkworks deliverable isn't "looks good" — it's "passes the spec." If you can't write the test before you write the code, you don't know what you're building.
- The artifact: A Python script that takes a specification (a list of requirements) and any output (code, document, or design description) and runs a compliance test: for each requirement, does the output satisfy it? (YES / NO / PARTIALLY). Outputs a compliance scorecard with pass rate and a list of failing requirements. Displayed as a Manim-animated compliance scorecard.
- Prompt seed: `claude "Run a specification compliance test. SPECIFICATION: [LIST OF REQUIREMENTS]. OUTPUT TO TEST: [OUTPUT]. For each requirement, determine: YES (fully satisfied), PARTIAL (partially satisfied with one sentence on what's missing), NO (not satisfied). Produce a compliance scorecard with: pass rate (%), partial rate (%), fail rate (%), and a prioritized list of failing requirements by severity."`
- Read / check: Verify the compliance judgments are specific (not "this looks fine" — name what specifically satisfies or violates each requirement). Confirm the partial category is used (not just YES/NO). Check the pass rate arithmetic is correct.
- Human supplies (Claude can't): The specification and the output to test — the video uses a synthetic specification (a document or code module with deliberate compliance gaps). Fully synthetic is acceptable.
- Output medium: Manim (animated scorecard: requirements appearing, verdicts animating, final pass rate revealed)
- The change: Ask Claude to generate a revised output that addresses the failing requirements — then run the compliance test again. Show the pass rate improving.
- Teardown angle: The skunkworks rule: write the test before you write the code. The specification compliance tester operationalizes that rule for any output type — code, document, or design.
- Exclusions: Don't go into formal software verification; don't cover unit testing frameworks; don't build for production CI/CD use.
- Score: 7/10

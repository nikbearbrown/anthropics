# Causal Reasoning — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — Diagnose a Model's Causal Claims with Claude
- Source: causal-reasoning/chapters/01-the-decision-that-looked-right.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: A churn model confidently predicts — but is it measuring association or causation? One do-operator reveals the difference.
- The artifact: a structured diagnosis table pairing each model feature with its P(Y|X) claim vs. its P(Y|do(X)) claim, plus a verdict (safe / causal overreach / potential confound) for each row — animated as cells filling in column by column.
- Prompt seed: `claude "For this churn model [paste feature list], for each feature write its observational claim P(churn|feature=high), the causal claim P(churn|do(feature=high)), and flag whether the observational training gives us leverage over the causal claim. Output a markdown table."`
- Read / check: verify that P(Y|X) vs. P(Y|do(X)) distinction is correct for at least three features; check that features with obvious confounders (e.g., usage frequency confounded by plan type) are correctly flagged.
- Human supplies: a real or illustrative churn model feature list (can be the book's worked example — fully synthetic is acceptable for the video).
- Output medium: screen-recording mp4 (terminal typing the prompt, table result animating in)
- The change: ask Claude to add a fourth column — "what intervention would test the causal claim?" — and verify the suggested interventions are plausible.
- Teardown angle: most ML features are observational proxies; the do-operator exposes where the model's predictive power would not translate to intervention.
- Exclusions: derivation of the do-calculus, formal identifiability proofs.
- Score: 9/10

---

## Candidate 02 — Enumerate Backdoor Paths and Find an Adjustment Set with Claude
- Source: causal-reasoning/chapters/09-backdoor-criterion-part-1.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Six backdoor paths hide in a six-node pricing DAG — Claude finds them all in seconds, then proves one adjustment set kills every path.
- The artifact: a numbered list of all backdoor paths from Treatment → Outcome, then an adjustment set, then a verification that conditioning on those nodes blocks every path — animated as a DAG diagram with paths lighting up then going dark as each is blocked.
- Prompt seed: `claude "Given this DAG [paste edge list], enumerate every backdoor path from T to Y, then propose a valid adjustment set using the backdoor criterion. For each path in your list confirm whether the adjustment set blocks it."`
- Read / check: student verifies path enumeration by hand on at least three paths; checks that the proposed adjustment set does not condition on a collider; verifies no blocked path was miscounted.
- Human supplies: a DAG edge list (the book's pricing pipeline example is fully usable — synthetic).
- Output medium: Manim (DAG rendered, paths highlighted, then grayed out as the adjustment set blocks them)
- The change: add an edge to the DAG and ask Claude to re-enumerate; verify the new path appears and the adjustment set is updated.
- Teardown angle: the backdoor criterion turns an intractable "what to control for" debate into a graph-theory problem — but only if you drew the right DAG.
- Exclusions: front-door criterion, instrumental variables.
- Score: 9/10

---

## Candidate 03 — Compute an E-Value and Calibrate Sensitivity with Claude
- Source: causal-reasoning/chapters/14-when-the-assumptions-dont-hold.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: A risk ratio of 2.1 sounds convincing — until you compute how weak an unmeasured confounder would need to be to explain it away.
- The artifact: a Python script applying the E-value formula `RR + √(RR × (RR−1))` to a user-supplied RR, printing the E-value and a plain-language calibration sentence (robust / fragile / not-definitive) — output animated as the formula evaluating step by step.
- Prompt seed: `claude "Write a Python function e_value(rr: float) -> dict that computes the E-value using the formula RR + sqrt(RR*(RR-1)), returns the E-value, and prints a calibration verdict: >3 = robust, 1.5–3 = fragile, <1.5 = not-definitive. Run it on RR=2.1."`
- Read / check: verify the formula matches VanderWeele & Ding (2017); check that the arithmetic is correct for RR=2.1 (expected E≈3.29); verify the calibration thresholds match the book's domain guidance.
- Human supplies: nothing — fully synthetic; book-supplied RR example used.
- Output medium: screen-recording mp4 (terminal running the script, step-by-step output)
- The change: extend the function to also compute and print the E-value for the confidence interval lower bound, then re-run on two contrasting examples (RR=1.3 and RR=4.0).
- Teardown angle: sensitivity analysis is not a weakness — it is the honest way to communicate what your causal claim survives.
- Exclusions: Bayesian sensitivity analysis, RERI, full EValue R package walkthrough.
- Score: 9/10

---

## Candidate 04 — Detect Collider Bias in a Hiring Pipeline with Claude
- Source: causal-reasoning/chapters/07-colliders-part-1.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Among hired candidates, skill and personality scores are negatively correlated — that correlation doesn't exist in the population. Conditioning on a collider created it.
- The artifact: a Python simulation generating N candidates, conditioning on being hired (collider), and producing a before/after scatter plot showing the spurious correlation emerge — rendered as an animated d3 or Manim scatter with a moving threshold.
- Prompt seed: `claude "Simulate 5000 candidates with independent skill~N(0,1) and personality~N(0,1). Hire anyone with skill+personality > 1. Compute Pearson r between skill and personality in the full population vs. among hired. Plot both scatter panels side by side. Print the two r values."`
- Read / check: verify population r ≈ 0 and hired-subset r is strongly negative (expected ≈ −0.6 to −0.7); check that the hiring threshold correctly implements the collider structure.
- Human supplies: nothing — fully synthetic simulation.
- Output medium: Manim (two-panel scatter animation: full population dots appear, then a threshold line filters to hired subset, correlation line flips)
- The change: vary the hiring threshold from strict (top 10%) to lenient (top 50%) and observe how collider bias strength changes.
- Teardown angle: the hiring paradox isn't an illusion — it is a structural consequence of selection on a collider; recognizing it prevents false conclusions about skilled candidates.
- Exclusions: Berkson's paradox in clinical settings, M-bias, more complex collider structures.
- Score: 9/10

---

## Candidate 05 — Translate a Causal Claim Across Three Registers with Claude
- Source: causal-reasoning/chapters/02-three-words-for-the-same-problem.md (LLM Exercise)
- Lane: RESEARCH (Claude assistant)
- Hook: "Controlling for age" means something different to a statistician, a causal modeler, and a clinician — Claude exposes all three readings of the same sentence.
- The artifact: a structured three-column markdown table translating one causal claim (e.g., "treatment lowers blood pressure when we control for age") into the statistical register (P(Y|X, age=a)), the causal register (P(Y|do(X), age=a)), and the plain-language clinician register — displayed as an animated table building column by column.
- Prompt seed: `claude "Take the claim: 'our treatment lowers blood pressure when we control for age.' Translate this into: (1) statistical notation P(Y|X, Z), (2) causal notation with the do-operator, (3) plain-language meaning for a clinician. For each translation, note what assumption it requires that the other translations don't."`
- Read / check: verify the statistical notation correctly uses P(Y|X, Z=z) conditioning; verify the causal version uses P(Y|do(X), Z=z) or the correct sub-causal expression; verify the assumptions column names something genuinely different for each register.
- Human supplies: a single causal claim sentence (the HRT-WHI example from ch.2 is usable — fully synthetic).
- Output medium: screen-recording mp4 (terminal interaction building the table)
- The change: ask Claude to apply the same three-register translation to a more contentious claim (e.g., "diversity training reduces bias") and flag where the registers give different verdicts on whether the claim is testable.
- Teardown angle: vocabulary ambiguity is not pedantry — it determines whether a study's conclusion is actionable; the three registers expose whose question was actually answered.
- Exclusions: full do-calculus derivations, formal semantics of interventional distributions.
- Score: 8/10

---

## Candidate 06 — Build a Candidate DAG and Audit It with Claude
- Source: causal-reasoning/chapters/03-the-map-before-the-territory.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: You describe four variables in plain English — Claude draws the DAG and you immediately find the edge it invented.
- The artifact: a dagitty-formatted or networkx DAG exported from Claude's proposed edges, with a student-critique log naming one invented edge, one missing edge, and one omitted variable — animated as a graph being built then annotated in red.
- Prompt seed: `claude "For this system [describe 4-6 variables in plain English: e.g., ad spend, website traffic, product quality, customer satisfaction, repeat purchase], propose a DAG as a list of directed edges. For each edge give one-sentence justification. Flag any variables that seem like plausible omitted confounders."`
- Read / check: verify each proposed edge is structurally defensible (not just correlated); identify at least one edge that is plausible-but-undefendable; check whether a plausible omitted confounder was listed.
- Human supplies: a 4-6 variable system description (marketing funnel example is fully synthetic and works).
- Output medium: Remotion (animated DAG building node by node, then edges appearing with labels)
- The change: add one omitted confounder to the variable list and ask Claude to revise the DAG; verify the confounder's edges are structural (not just correlation-based).
- Teardown angle: a Claude-proposed DAG is a falsifiable hypothesis, not a fact — the auditing step is the whole point; the value is in what the student disagrees with.
- Exclusions: CPDAG enumeration, Markov equivalence class computation, causal discovery algorithms.
- Score: 8/10

---

## Candidate 07 — Run a Three-Failure Taxonomy on Two LLM-Generated DAGs with Claude
- Source: causal-reasoning/chapters/04-the-identification-layer.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Two different LLMs propose two different DAGs for the same marketing problem — run the three-failure taxonomy and watch them fail differently.
- The artifact: a side-by-side comparison table applying the three failure types (wrong variables, wrong arrows, wrong conditioning) to DAGs from two models — animated as each failure cell filling in with a red/green verdict.
- Prompt seed: `claude "Here are two DAGs for a B2B SaaS email → conversion problem [paste both DAG edge lists]. For each DAG, apply this taxonomy: (1) wrong variables (omitted confounders or irrelevant nodes), (2) wrong arrows (direction errors), (3) wrong conditioning (conditions on collider or mediator). Give one verdict per cell."`
- Read / check: verify the conditioning column correctly identifies colliders vs. confounders vs. mediators; check that "wrong arrows" findings are structurally grounded, not just preference.
- Human supplies: two LLM-generated DAG edge lists for the same problem (student generates these by querying two models — or the book's worked example serves as one).
- Output medium: screen-recording mp4 (terminal running comparison, table filling in)
- The change: for the worst-performing DAG, ask Claude to propose a corrected version and apply the taxonomy again.
- Teardown angle: comparing two models on the same DAG task reveals systematic weaknesses in how language models represent causal structure — pattern-matching on correlation language rather than structural knowledge.
- Exclusions: formal DAG equivalence testing, automated causal discovery.
- Score: 8/10

---

## Candidate 08 — Draft and Stress-Test a Three-Part DAG Defense with Claude
- Source: causal-reasoning/chapters/11-defending-your-dag.md (LLM Exercise)
- Lane: RESEARCH (Claude assistant)
- Hook: Claude drafts a professional-sounding DAG defense — then you find the fabricated citation hiding in paragraph two.
- The artifact: a structured three-part defense (arrows-as-claims, missing arrows ranked by bias direction, unmeasured confounders with bias direction) plus a fact-check log naming every invented citation and undefendable claim — the log rendered as an annotated document with red highlights on fabrications.
- Prompt seed: `claude "Draft a three-part DAG defense for this causal model [paste DAG + study description]: (1) justify each arrow as a testable claim, (2) rank the three most plausible missing arrows by estimated bias direction, (3) name two unmeasured confounders and state whether each biases the estimate up or down. Use academic-register language."`
- Read / check: student opens any source Claude cites; checks that arrow justifications are mechanistic (not just correlational); verifies bias-direction claims are consistent with the DAG's structure.
- Human supplies: a DAG and brief study description (the book's healthcare or e-commerce example works — synthetic is acceptable).
- Output medium: screen-recording mp4 (terminal generating defense, then student annotation pass)
- The change: switch to plain-language register and ask Claude to rewrite the defense for a non-specialist audience; verify that the rewrite preserves the structural claims without inventing new ones.
- Teardown angle: the DAG defense is not about defending your assumptions — it is about making them visible enough that someone else can attack them.
- Exclusions: formal sensitivity analysis, full E-value walkthrough (see Candidate 03).
- Score: 8/10

---

## Candidate 09 — Propose and Critique a Confounder Set with Claude
- Source: causal-reasoning/chapters/05-confounders.md (LLM Exercise)
- Lane: RESEARCH (Claude assistant)
- Hook: Claude lists twelve plausible confounders for your study — two of them are actually mediators, and one is a collider in disguise.
- The artifact: a critique log pairing each Claude-proposed confounder with a structural verdict (true confounder / mediator / collider / irrelevant) and a one-sentence justification for each verdict — rendered as an annotated table with color-coded cells.
- Prompt seed: `claude "For a study of the effect of [X on Y in domain Z], propose 8-10 potential confounders with signed edges (does each increase or decrease both X and Y?). For each, give a one-sentence mechanistic justification."`
- Read / check: verify the signed edges are structurally defensible; identify at least one mediator (on the causal path X→M→Y) and one collider (affected by both X and Y) that Claude may have labeled as confounders; check that justifications cite mechanism, not just correlation.
- Human supplies: a study description with an X→Y question (the Obermeyer 2019 healthcare example is usable; otherwise any domain works — synthetic).
- Output medium: screen-recording mp4 (terminal generating proposals, then annotation walkthrough)
- The change: ask Claude to distinguish its list into "structural confounders" vs. "proxy confounders" and verify the distinction is drawn correctly.
- Teardown angle: proposing confounders is easy; the structural audit is the work — and the audit reveals that most "confounder" discussions in applied work conflate three distinct node types.
- Exclusions: adjustment set algorithms, full DAG-based identification.
- Score: 7/10

---

## Candidate 10 — Build a DoWhy Causal Effect Estimate with Claude Code
- Source: causal-reasoning/chapters/09-backdoor-criterion-part-1.md
- Lane: BUILD (Claude Code)
- Hook: Conditioning on three variables gives a very different estimate than the naive difference-in-means — DoWhy shows the gap with ten lines.
- The artifact: a Python script using DoWhy to estimate a causal effect via backdoor adjustment on a synthetic dataset, printing the naive estimate, the adjusted estimate, and the delta — with an animated bar chart showing the two estimates side by side.
- Prompt seed: `claude "Write a Python script using DoWhy that: (1) generates a synthetic dataset with a confounder Z affecting both treatment T and outcome Y, (2) computes the naive T→Y association, (3) estimates the causal effect using backdoor adjustment on Z, (4) prints both estimates and the delta. Use graphviz DAG notation."`
- Read / check: verify the synthetic data generator correctly implements the confounder structure (Z→T and Z→Y); check that the backdoor adjustment recovers the true causal effect (known from the DGP); verify the delta is non-zero and in the expected direction.
- Human supplies: nothing — fully synthetic simulation; DoWhy must be installed.
- Output medium: Manim (two bar chart bars growing, labeled Naive vs. Adjusted, with a delta annotation)
- The change: introduce a second confounder and re-run; verify that the single-variable adjustment set is no longer sufficient and DoWhy flags the gap.
- Teardown angle: the naive vs. adjusted gap is not always large — but it is always a design choice; DoWhy makes the choice visible and auditable.
- Exclusions: refutation tests, instrumental variable estimation, full DoWhy refutation suite.
- Score: 7/10

---

## Candidate 11 — Cross-Check a Causal Claim Against Primary Sources with Claude
- Source: causal-reasoning/chapters/11-defending-your-dag.md
- Lane: RESEARCH (Claude assistant)
- Hook: A published finding claims "meditation reduces cortisol" — Claude finds four citable studies, you find one that contradicts the claim.
- The artifact: a sourced brief with five entries: study citation, finding, design strength, and a verdict (supports / contradicts / irrelevant to the causal claim) — plus a synthesized conclusion that hedges appropriately — rendered as an annotated evidence table.
- Prompt seed: `claude "Research the causal claim 'meditation reduces cortisol levels.' Find at least four citable studies (with author, year, journal). For each, state the study design (RCT / observational / meta-analysis), the finding with effect size if reported, and whether it supports, contradicts, or is irrelevant to the causal claim. Then write a two-sentence calibrated conclusion."`
- Read / check: verify each citation exists (open DOI or Google Scholar); verify the design labels are correct; check that at least one study's finding is more nuanced than the claim implies; verify the conclusion correctly hedges on design quality.
- Human supplies: nothing for the base video — but stronger version uses a real citation database search by the student to verify Claude's sources independently.
- Output medium: screen-recording mp4 (terminal building the evidence table, then citation verification pass)
- The change: ask Claude to identify the key confounder the best study did or did not control for, and state how controlling for it would change the conclusion.
- Teardown angle: a causal claim is not established by one study — the synthesis discipline is about mapping the claim across design types and noting where the evidence is weakest.
- Exclusions: meta-analysis computation, forest plots, formal systematic review protocol.
- Score: 7/10


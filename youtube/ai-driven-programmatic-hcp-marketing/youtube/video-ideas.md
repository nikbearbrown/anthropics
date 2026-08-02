# Bear's Doodles — AI-Driven Programmatic HCP Marketing Video Ideas

**Scouted:** 15 chapters (intro + 01–14).

**What this book is.** Unlike the quantum volumes, this is a business/technical book — programmatic ad auctions, identity graphs, machine-learning architectures, and causal-inference design, all aimed at marketing to healthcare professionals (HCPs). That turns out to be *fertile* Bear's Doodles territory: it's full of self-reinforcing loops, counterintuitive quantitative inversions, and before/after mechanisms where the whole lesson is watching a number deflate or a comparison re-form. I was still selective — I rejected the taxonomy tables, checklists, org charts, and legal holdings (nothing moves), and kept only concepts where motion carries the teaching. The result is 22 candidates.

**Consolidation notes for pick-time (yours to make, not the scout's).** A few clusters overlap and you'll likely build one from each, not all:
- **The "loop" family** — Attribution circularity (01), the self-optimizing machine loop (02). Both are feedback loops; keep their visual objects distinct or build one.
- **The uplift family** — the inversion curve (02), the persuadables 2×2 (07), the 44% holdout (03), and the Qini curve (21) all argue "predict-who ≠ move-whom" from different angles. Distinct visuals, one shared thesis.
- **The DiD pair** — "subtract twice" (17) and "the forbidden comparison" (16) are genuinely two different lessons (the mechanism vs. the staggered-adoption trap), but both live on two-lines-over-time; sequence them or pick one.

---

## Candidate 01 — Why the "44% lift" is measured by the people selling you the ad

- Source: `ai-driven-programmatic-hcp-marketing/chapters/04-what-todays-ai-stack-does.md`
- Production mode: Doodle
- Hook: The party with a commercial interest in a big number is the same party producing the number.
- Core idea: When the platform that serves the ad also measures the prescribing and reports the lift, serving and measuring are the same node — so the figure is circular, and only a randomized holdout measured by a disinterested outsider cuts the loop open.
- Visual object: A closed two-node loop, SERVE ⟲ MEASURE, with a dashed "independent measurer" node stranded outside it, never connected
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: an ad "lift" number, the idea of a conflict of interest
- Exclusions: no attribution-window math, no MMM vs. MTA detour; the whole video is the loop and the severed outside node
- Score: 9/10

## Candidate 02 — Why your prescriber model targets exactly the wrong doctors

- Source: `ai-driven-programmatic-hcp-marketing/chapters/08-uplift-and-incrementality.md`
- Production mode: Manim visualization
- Hook: The physician your model is most certain will prescribe is the single worst place to spend a marketing dollar.
- Core idea: Incremental effect is near zero at both tails — the 95%-propensity "sure thing" has no room to move and the "lost cause" won't move — so the persuadable value peaks in the middle, and a model that ranks by likelihood-to-prescribe points at the flat ends.
- Visual object: An inverted-U curve, propensity on x, incremental effect on y, with a marker sweeping up the propensity axis
- Manim move: scan
- Short-form fit: Strong
- Prerequisites: probability of an outcome, "moving" a behavior vs. predicting it
- Exclusions: no CATE estimator taxonomy (S/T/X/R-learners), no uplift-model training details — this is the curve and the sweep only
- Score: 9/10

## Candidate 03 — Why a real 44% lift can shrink to zero the instant you withhold one group

- Source: `ai-driven-programmatic-hcp-marketing/chapters/08-uplift-and-incrementality.md`
- Production mode: Manim visualization
- Hook: An arithmetically-correct 44% "script lift" can collapse into the noise of zero the moment you add a randomly withheld group.
- Core idea: A randomized holdout drawn from the *same* high-propensity target list strips three stacked biases at once — targeting-on-the-outcome, regression-to-mean/secular trend, and attribution circularity — leaving true lift as treated-mean minus holdout-mean.
- Visual object: A big "44%" with three labeled bias layers wrapped around it, peeling off one at a time as a holdout group splits away
- Manim move: collapse
- Short-form fit: Strong
- Prerequisites: an average outcome, the idea of a control group
- Exclusions: caption the 44% as illustrative; no power-calculation or holdout-sizing math, no meta-learner detour
- Score: 9/10

## Candidate 04 — Why "de-identified" health data still names the doctor

- Source: `ai-driven-programmatic-hcp-marketing/chapters/03-the-hcp-identity-graph.md`
- Production mode: Manim visualization
- Hook: The privacy step that erases the patient leaves the prescriber standing in full view.
- Core idea: Safe Harbor strips the 18 patient identifiers, but the NPI is not a patient identifier and survives; one join to the AMA Masterfile then resolves that surviving number into a named, profiled physician.
- Visual object: A single prescription record moving down a pipe — patient fields (name, DOB, address) struck through and falling away while the NPI rides through untouched and blooms into "Dr. Jane Smith, Mass General"
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: what "anonymized data" is supposed to mean
- Exclusions: don't enumerate all 18 identifiers on screen; no Expert-Determination-vs-Safe-Harbor comparison, no Sorrell v. IMS legal history
- Score: 9/10

## Candidate 05 — Why ten models can be no better than one

- Source: `ai-driven-programmatic-hcp-marketing/chapters/06-ensembles-tabular-advantage.md`
- Production mode: Manim visualization
- Hook: Keep adding models to your ensemble and the error falls — until it hits a wall no amount of averaging can cross.
- Core idea: Averaging N models drives the variance term to zero as 1/N, but a second term — the covariance of their shared mistakes — grows to a floor, so ten models trained the same way on the same data just repeat the same blind spot.
- Visual object: A stacked error bar across "1 model → 10 → N→∞" — the variance slice melting toward zero while the covariance slice swells to a horizontal floor line
- Manim move: transform
- Short-form fit: Strong
- Prerequisites: averaging reduces error, the idea of correlated mistakes
- Exclusions: don't derive bias²+variance+covariance; state it as a label. No bagging/boosting/stacking table
- Score: 8/10

## Candidate 06 — Why the ad in your chart looks like medicine

- Source: `ai-driven-programmatic-hcp-marketing/chapters/01-the-machine-nobody-sees.md`
- Production mode: Manim visualization
- Hook: The advertisement inside the doctor's chart arrives through the exact same plumbing as a drug-interaction warning — so it looks like medicine because it arrived like medicine.
- Core idea: A clinical action fires a CDS Hook (an HTTP request), an external commercial service returns a "card," and it renders in the EHR sidebar in the same visual tier as a safety alert.
- Visual object: One EHR chart with a right-hand sidebar; a clinical action pulses down a wire to an outside service and a promotional card slides back into the safety-alert slot
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: doctors use electronic charts; a pop-up alert
- Exclusions: no OAuth/SMART-on-FHIR token mechanics, no vendor roster; the trigger→card flow is the whole story
- Score: 8/10

## Candidate 07 — Why every number on the dashboard is green while the brand is dying

- Source: `ai-driven-programmatic-hcp-marketing/chapters/02-lift-vs-brand.md`
- Production mode: Manim visualization
- Hook: Total prescriptions look strong and rising — and the brand is quietly losing every new patient it should be winning.
- Core idea: TRx (total scripts) stays fat on refill inertia — old decisions repeating — while NBRx (new-to-brand) is the leading indicator, and it's the one collapsing; the top-line number has no memory of when each decision was made.
- Visual object: Two lines on one timeline — a fat "TRx" line holding flat-green while a thin "NBRx" line beneath it bends down 20%
- Manim move: split
- Short-form fit: Strong
- Prerequisites: a sales/volume metric over time
- Exclusions: no NBRx subtype taxonomy, no persistence-guardrail detour; the divergence reveal is the video
- Score: 8/10

## Candidate 08 — Why a model with 671 billion parameters only runs 37 billion of them

- Source: `ai-driven-programmatic-hcp-marketing/chapters/07-mixture-of-experts.md`
- Production mode: Manim visualization
- Hook: The model holds 671 billion parameters but fires only 37 billion on any given input — and that's the design, not a defect.
- Core idea: A learned gate scores all N experts, Top-k keeps only the k largest and zeros the rest, so capacity grows with the number of experts while compute stays flat at k.
- Visual object: One input flowing into a gating box and a column of N expert boxes, only k lighting up, with a long "capacity" bar and a short "compute" bar beside them
- Manim move: split
- Short-form fit: Strong
- Prerequisites: a neural network is made of many parameters; "more parameters = more compute" (the intuition being broken)
- Exclusions: no softmax/gating equations on screen, no Mixtral-vs-DeepSeek spec comparison beyond one headline number
- Score: 8/10

## Candidate 09 — Why sending your message can make a doctor prescribe less

- Source: `ai-driven-programmatic-hcp-marketing/chapters/08-uplift-and-incrementality.md`
- Production mode: Manim visualization
- Hook: There's a group of physicians where the ad actively backfires — and propensity targeting walks straight past the profitable group into the useless one.
- Core idea: Crossing "prescribes if treated?" with "prescribes if untreated?" yields four groups — persuadables (the only net gain), sure things, lost causes, and sleeping dogs (message reduces the outcome) — and propensity aims at sure things while uplift aims at persuadables.
- Visual object: A 2×2 matrix assembling from two binary axes, with a "propensity" arrow and an "uplift" arrow landing in different cells and the sleeping-dog cell flashing red
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: the idea of targeting an audience
- Exclusions: don't re-derive the inversion curve (that's its own video, Candidate 02); keep to the four cells and the two arrows
- Score: 8/10

## Candidate 10 — Why a coupon that makes a drug nearly free can raise the total bill

- Source: `ai-driven-programmatic-hcp-marketing/chapters/01-the-machine-nobody-sees.md`
- Production mode: Doodle
- Hook: A co-pay card that makes a branded drug almost free for the patient can *increase* what the system pays.
- Core idea: Price sensitivity has been engineered out of every party except the patient; the coupon zeroes the patient's out-of-pocket too, removing the last disciplining force while the payer still absorbs the full branded-vs-generic difference.
- Visual object: A row of four "price-sensitivity" gauges — physician, payer, institution, patient — going flat one by one, the patient's needle finally dropping to zero as the coupon lands
- Manim move: collapse
- Short-form fit: Strong
- Prerequisites: patients pay a co-pay; generics cost less
- Exclusions: anchor on the falling-gauges cascade; the natural-experiment stats (commercial vs. Medicare Advantage) are a caption payoff, not a second scene
- Score: 8/10

## Candidate 11 — Why a "boring" decision tree beats the fancy neural net on prescriber data

- Source: `ai-driven-programmatic-hcp-marketing/chapters/06-ensembles-tabular-advantage.md`
- Production mode: Manim visualization
- Hook: The state-of-the-art neural network keeps losing to a decision tree on tabular data — and it loses precisely because it's too smooth.
- Core idea: Gradient descent biases neural nets toward smooth, gradually-interpolating functions, but prescriber relationships are jagged — a threshold at a decile, a payment cutoff, a specialty boundary — and a tree split lands on those discontinuities natively.
- Visual object: A staircase target function; a smooth curve straining and wobbling to catch each vertical jump while tree splits click onto every riser
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: a model fits a curve to data; a decision tree splits on thresholds
- Exclusions: no backprop or inductive-bias derivation; don't add the "robust to uninformative features" second mechanism — one object
- Score: 8/10

## Candidate 12 — Why the dangerous AI citation is the one that's real

- Source: `ai-driven-programmatic-hcp-marketing/chapters/10-llms-for-commercial-research.md`
- Production mode: Manim visualization
- Hook: The fabricated citations are easy to catch; the one that gets you in trouble is real, resolves cleanly, and fails only the check nobody runs — reading it.
- Core idea: A verification harness winnows generated citations through layers — exists? DOI valid? journal real? — that drop fabrications early, but a real-but-misattributed reference sails through every shallow check and fails only at the deepest layer: does the cited text actually support the claim?
- Visual object: A stack of eight citation cards fed down through four harness layers, cards dropping out at each layer while one "all-green" card survives to the last and only then fails
- Manim move: collapse
- Short-form fit: Strong
- Prerequisites: LLMs can make up citations; a DOI/reference
- Exclusions: don't fold in the fabrication-rate bar stats (39.6%/28.6%/91.4%) — separate idea; keep the one surviving card as the spine
- Score: 8/10

## Candidate 13 — Why you pay for 256 experts and the model uses three

- Source: `ai-driven-programmatic-hcp-marketing/chapters/07-mixture-of-experts.md`
- Production mode: Manim visualization
- Hook: You buy a model with 256 experts and it quietly collapses onto using three of them.
- Core idea: A rich-get-richer loop — experts that get slightly more early routing receive more gradient, improve fastest, and attract even more routing — so training must inject forced exploration (noisy gating, load-balancing loss) that itself fights the specialization it's trying to preserve.
- Visual object: A bank of expert boxes where routing traffic concentrates onto a few that grow bright while the rest go dark, then a balancing force shoves traffic back out
- Manim move: collapse
- Short-form fit: Medium
- Prerequisites: Candidate 08's routing idea (experts + a gate) helps; a feedback loop
- Exclusions: no auxiliary-loss equations; name the three fixes in one breath, don't explain each
- Score: 7/10

## Candidate 14 — Why the marketing machine only tightens, never loosens

- Source: `ai-driven-programmatic-hcp-marketing/chapters/01-the-machine-nobody-sees.md`
- Production mode: Doodle
- Hook: The machine optimizes one number — branded prescribing volume — and that number feeds straight back into its own aim, with nothing funded to pull the other way.
- Core idea: Objective → NPI list → bid → point-of-care impression → prescription → attribution → a *tighter* NPI list; the loop closes on itself each cycle, and the counterweight (comparative-effectiveness, generic, cost) exists only in unfunded fragments.
- Visual object: A five-node directed cycle that loops and visibly tightens/brightens each pass, with a ghosted "counter-stack" ring that never lights up
- Manim move: trace
- Short-form fit: Medium
- Prerequisites: the idea of an optimization target
- Exclusions: keep distinct from Candidate 01 (that loop is the measurement firewall; this loop is the whole-system self-reinforcement) — don't merge the two visuals
- Score: 7/10

## Candidate 15 — Why a doctor looks like she responded to an ad she never saw first

- Source: `ai-driven-programmatic-hcp-marketing/chapters/06-ensembles-tabular-advantage.md`
- Production mode: Manim visualization
- Hook: A prescription seems to prove the ad worked — but it was actually written before the ad ever fired.
- Core idea: Claims arrive with processing lag, so a script written in March but recorded in May lands inside a naive "post-exposure" window and gets miscredited as a response — a bookkeeping artifact, not a treatment effect.
- Visual object: One prescription on a timeline with a "written" marker and a later "recorded" marker; the recorded marker slides right across the exposure line while the true write-date stays behind it
- Manim move: scan
- Short-form fit: Strong
- Prerequisites: an ad-exposure window; that data takes time to arrive
- Exclusions: no claims-adjudication plumbing detail; the sliding recorded-date marker is the entire teaching
- Score: 7/10

## Candidate 16 — Why the standard staggered-rollout analysis can get the sign wrong

- Source: `ai-driven-programmatic-hcp-marketing/chapters/12-research-design-public-data.md`
- Production mode: Manim visualization
- Hook: The textbook regression for policies that roll out at different times can return an effect that's not just imprecise but wrong in sign — wrong by math, not by convention.
- Core idea: Two-way fixed effects secretly borrows already-treated units as "controls" for later-treated ones — but a state treated four years ago has already adjusted — and the fix compares each cohort only to not-yet-treated and never-treated units.
- Visual object: A grid of units on a shared year axis, each row splitting at its own adoption year; a red "forbidden" comparison arrow reaches from a late adopter back to an already-treated one, then gets redrawn to land only on clean controls
- Manim move: compare
- Short-form fit: Medium
- Prerequisites: difference-in-differences basics (Candidate 17); a control group
- Exclusions: no Goodman-Bacon decomposition or Callaway–Sant'Anna estimator math; the forbidden-arrow-becoming-clean is the payoff
- Score: 7/10

## Candidate 17 — Why you can measure an ad's causal effect without running an experiment

- Source: `ai-driven-programmatic-hcp-marketing/chapters/12-research-design-public-data.md`
- Production mode: Manim visualization
- Hook: Adding more control variables can't remove a confounder you can't measure — but subtracting the same data twice can.
- Core idea: One difference across groups removes the fixed gap between treated and control; a second difference across time removes the shock they both shared; under parallel pre-trends, what's left is the causal effect.
- Visual object: Two prescribing-over-time lines, treated and control, running parallel until a vertical "policy" line — then the level gap collapses (first subtraction) and the shared trend is pulled out (second), leaving only the treated line's excess bend
- Manim move: split
- Short-form fit: Medium
- Prerequisites: a treated vs. control group; reading a line over time
- Exclusions: no parallel-trends-in-levels-vs-logs caveat, no regression spec; two lines, two subtractions
- Score: 7/10

## Candidate 18 — Why "omnichannel" doesn't mean being everywhere at once

- Source: `ai-driven-programmatic-hcp-marketing/chapters/04-what-todays-ai-stack-does.md`
- Production mode: Manim visualization
- Hook: Firing every channel at a physician the same week is the failure mode, not the goal.
- Core idea: Orchestration suppresses the channels a physician ignores and sequences the rest — rep call, EHR trigger, email — so they reinforce instead of colliding; the win is timing, not ubiquity.
- Visual object: One HCP at the center with six channel spokes — left state all six firing at once in chaos, right state four spokes dimming and two firing in timed sequence
- Manim move: compare
- Short-form fit: Medium
- Prerequisites: marketing channels (email, rep, ads); the idea of message timing
- Exclusions: no per-channel conversion-rate table; the simultaneous→sequenced contrast is the point
- Score: 7/10

## Candidate 19 — Why two identical favorability spikes can mean opposite things

- Source: `ai-driven-programmatic-hcp-marketing/chapters/09-brand-association.md`
- Production mode: Manim visualization
- Hook: Two campaigns produce the exact same brand-favorability bump — one built lasting equity, one built nothing, and a single post-test cannot tell them apart.
- Core idea: Deeply-processed (central-route) attitude change persists while repetition-driven (peripheral-route) change decays toward baseline, so only a delayed second measurement — after the transient bump has had time to fall — separates a durable flat line from a fading one.
- Visual object: Two lines over pre-exposure / immediate-post / delayed-post that rise in perfect overlap, then split only at the final point
- Manim move: split
- Short-form fit: Strong
- Prerequisites: a brand-favorability survey; a before/after measurement
- Exclusions: no full Elaboration Likelihood Model exposition; the two-lines-split-late reveal is self-contained
- Score: 7/10

## Candidate 20 — Why the doctor you've already won is your worst place to spend

- Source: `ai-driven-programmatic-hcp-marketing/chapters/02-lift-vs-brand.md`
- Production mode: Manim visualization
- Hook: The obvious move — target your highest-volume prescriber — can mean spending the whole budget on the one doctor you've already converted.
- Core idea: Ranking physicians by volume alone hides brand share; add the second axis and the order flips — the huge-volume/5%-share doctor has enormous headroom, while the mid-volume/60%-share doctor is largely already won.
- Visual object: A ranked list of physicians by volume that re-sorts when a "brand share" axis swings in, sending the high-headroom doctor to the top
- Manim move: transform
- Short-form fit: Medium
- Prerequisites: prescribing volume; market share
- Exclusions: build the re-sort as the teaching — a static 2×2 isn't enough; no propensity-vs-uplift detour (that's Candidates 02/09)
- Score: 7/10

## Candidate 21 — Why a project can pass every commercial test and still get killed

- Source: `ai-driven-programmatic-hcp-marketing/chapters/14-prototype-to-product-decision.md`
- Production mode: Doodle
- Hook: A project can clear strong evidence, real magnitude, clean compliance, and low cost — and one gate that outranks all of them still forces a kill.
- Core idea: The decision is conjunctive, not weighted — a project token descends five gates, and a patient-welfare failure (e.g. a coupon that suppresses generic substitution) vetoes even a clean commercial run.
- Visual object: A single project token dropping down a vertical five-gate chute, clearing four green gates and getting stopped dead by the red welfare gate
- Manim move: collapse
- Short-form fit: Medium
- Prerequisites: a go/no-go decision; the idea of a veto
- Exclusions: don't narrate all four welfare triggers; the "watch the winner get vetoed" beat is the whole video, not a full decision-tree walkthrough
- Score: 7/10

## Candidate 22 — Why you can't grade an uplift model with accuracy

- Source: `ai-driven-programmatic-hcp-marketing/chapters/08-uplift-and-incrementality.md`
- Production mode: Manim visualization
- Hook: The thing an uplift model predicts — one physician's treatment effect — is never observed for anyone, so ordinary accuracy is undefined.
- Core idea: Rank physicians by predicted uplift and accumulate treated-minus-control response as you walk down the list; a model that truly finds persuadables bows the cumulative curve above the random-targeting diagonal, and the area between them is the Qini score.
- Visual object: A cumulative incremental-response curve building left-to-right above a straight random-targeting diagonal, with the gap shading in as "Qini"
- Manim move: accumulate
- Short-form fit: Medium
- Prerequisites: ranking a list by a predicted score; a cumulative-gains/lift curve
- Exclusions: no Qini-vs-AUUC formula; the curve building above the diagonal is the teaching
- Score: 6/10

---

## Cutting-room floor (rejected — static-sufficient, list-like, or no mechanism)

Seen and deliberately dropped because a static figure, table, or sentence teaches them as well or better: NPI-vs-cookie deterministic/probabilistic comparison (01); the split-agency four-node diagram and counter-stack mirror (01); lift-vs-brand as two study designs, SOV-vs-SOM, brand-as-archetype (02); the claims-lag *timeline*, propensity-susceptibility proxy, Sorrell v. IMS holding (03); the maturity ladder, NBA population inversion, MLR governance gap, McKinsey-vs-MIT stat pair (04); the entire evidence-taxonomy/two-ladder/minimum-of-two apparatus and the "every sentence true, none is evidence" case (05); discrimination-vs-calibration and the bagging/boosting/stacking table (06); MoE-vs-stacking and what-experts-specialize-on panels (07); the CATE meta-learner family and the two-worlds diagram as a standalone (08 — its counterfactual idea is better carried inside Candidates 02/03); WEAT setup, brand-formation flowchart, conjoint/DCE schematic, say-do gap (09); fabrication-rate bars, the fluency trap, LLM-as-judge bias list (10); the six-step funnel, handoff-brief fields, four compliance surfaces, and the Evidence-Ladder ceiling — the ladder appears three times (11/13/14) and is a static diagram every time (11); public-data stack table, regression discontinuity, instrumental variables (12); the seven-field card, four-track portfolio, rigged-benchmark and ecological-inference caveats (13); the four-stage pipeline table and AI-disclosure judgments (14). Several are strong *written* explainers; none earn a motion-carries-the-teaching video.

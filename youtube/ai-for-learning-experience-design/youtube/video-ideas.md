# Bear's Doodles — AI for Learning Experience Design Video Ideas

**Scouted:** 16 chapters (01–15 + fundamental-themes).

**What this book is.** A book on designing learning with AI — and it turns out to be some of the best Bear's Doodles territory yet, because its whole argument is *dynamic*: performance and learning are two quantities that move differently over time, scaffolds fade, knowledge estimates update answer-by-answer, feedback loops compound, and distributions reshape. Those are motions, not states. I ran three parallel detection passes and then did the selection myself. Result: 21 candidates.

**One discipline this book forces on the builder.** The author is careful never to overclaim — many of the strongest visuals (reliance curves, the scissors split, the synapse cascade, effect-size positions) are explicitly flagged in the source as *illustrative worked cases or motivated hypotheses, not measured data*. Every card below that draws on one carries that caveat in its Exclusions. Animate the **shape and the mechanism**, label the **numbers as illustrative**, and teach contested science as hypothesis. That honesty is itself on-brand for the book.

**Consolidation clusters for pick-time (yours, not the scout's):**
- **The learning-vs-performance spine** — The Reversal (01), the reliance curve (10), and the synapse that never fires (03) all teach "the tool inflates performance while hollowing learning" from three angles (outcomes, telemetry, neurobiology). Build one or space them across a season.
- **Scaffold fading** — The Fade (02) and the reversal rule (12) share a support-band visual; the second adds "the band must come back *up*." Sequence or merge.
- **The DataWise equity case** — diverging task diets (05) and the remedial loop (07) are the same worked case seen two ways (two-learner disparity vs. single-learner compounding).
- **Distribution reshaping** — the Equity Signature (08) and the scissors in the average (11) both live on a distribution changing shape.

---

## Candidate 01 — Why the same students scored +48% and −17% with the same AI

- Source: `ai-for-learning-experience-design/chapters/01-two-layers-of-change.md`
- Production mode: Manim visualization
- Hook: One number says the AI helped by 48%, another says it hurt by 17% — and they came from the exact same kids.
- Core idea: "Performance while the tool is present" and "what the learner durably keeps" are two different quantities that can move in opposite directions; the tool inflates the first and hollows the second, and you only see it the moment the tool is withdrawn.
- Visual object: Two trajectory lines rising together through "practice," then a vertical "AI removed" line after which the tutor-condition line holds at parity while the bare-AI line plunges below the control baseline
- Manim move: split
- Short-form fit: Strong
- Prerequisites: a test score; the idea of practicing with help
- Exclusions: no meta-analysis detour; the two conditions and the withdrawal moment are the whole video. (Study: Bastani et al. 2025, PNAS — ~1,000 students; keep numbers as the on-screen payoff)
- Score: 9/10

## Candidate 02 — Why one extra button cut learning in half

- Source: `ai-for-learning-experience-design/chapters/02-the-crutch-effect.md`
- Production mode: Doodle
- Hook: Motivated students given one optional "get AI help" button learned less than half as much as students handed the identical help without the button — and they knew they were overusing it and did it anyway.
- Core idea: At each stuck moment "ask" beats "struggle" — lower effort, guaranteed progress, invisible delayed cost — so no single request is irrational, but the accumulated always-ask policy is ruinous, and it escalates because the cost of taking help is hidden.
- Visual object: A single "stuck moment" fork (struggle vs. ask) where only the ask-path loops back, each loop thickening an accumulating wedge, with a help-requests-per-move curve climbing across 12 weeks
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: the feeling of being stuck on a problem; a cost that shows up later
- Exclusions: don't call the students lazy — the choice is rational, which is the entire point; no self-regulation-theory lecture. (64% vs 30% learning; system- vs self-regulated)
- Score: 9/10

## Candidate 03 — Why a perfect AI answer can leave the brain unchanged

- Source: `ai-for-learning-experience-design/chapters/97-fundamental-themes.md`
- Production mode: Mixed (Doodle metaphor + Manim cascade)
- Hook: The answer is fluent, the artifact is flawless, the student feels they mastered it — so why did nothing physically change in their head?
- Core idea: Learning is a physical cascade triggered only by cognitive friction — prediction error fires dopamine, upregulates BDNF, strengthens a synapse, grows a dendritic spine — and if the AI removes the struggle, the trigger never fires and no consolidation happens, even though the output looks identical.
- Visual object: A single synapse where the friction path lights the cascade step-by-step and the AI-assisted path stays dark
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: neurons connect and strengthen; "use it or lose it"
- Exclusions: teach the cascade as a *motivated hypothesis*, not settled fact — the book's own fact-check calls the strict dopamine→BDNF→spine chain "overdrawn as a universal mechanism," and the 55%-connectivity figure is a single non-peer-reviewed preprint; no EEG-catastrophe overclaim
- Score: 9/10

## Candidate 04 — Why the "skills remaining" bar isn't measuring what you know

- Source: `ai-for-learning-experience-design/chapters/07-adaptive-systems.md`
- Production mode: Manim visualization
- Hook: The friendly progress bar isn't a count of what you've learned — it's one probability being shoved up and down by four hidden numbers after every answer.
- Core idea: Bayesian knowledge tracing re-estimates P(you've mastered this) after each response; a wrong answer from a probable master reads as a rare "slip," so belief drops hard then partly recovers, and the skill unlocks only when the estimate crosses 0.95.
- Visual object: A single horizontal probability bar from 0 to 1 with a 0.95 mastery gate, stepping as each answer arrives
- Manim move: scan
- Short-form fit: Strong
- Prerequisites: probability as a 0-to-1 belief; a "mastery" threshold
- Exclusions: don't show Bayes' rule algebra; the four parameters (slip, guess, learn, prior) are labels, not a derivation. Values are stipulated worked-example numbers — say so. End on the "over-practice zone" between 0.82 and 0.95
- Score: 9/10

## Candidate 05 — Why two students with the identical score end up in different courses

- Source: `ai-for-learning-experience-design/chapters/08-algorithmic-routing-and-equity.md`
- Production mode: Manim visualization
- Hook: Two students start with the exact same diagnostic score and the same tuition, nothing ever malfunctions — and by week six one is doing five times more advanced work than the other.
- Core idea: The difficulty model reads latency, session breaks and hint use as fluency-or-struggle, so a student on a shared phone plan whose sessions get interrupted reads as "struggling," gets routed to easier drills that crowd out higher-order work — a self-confirming split with no demographic field anywhere in the model.
- Visual object: Two lines leaving a single dot (62%), tracking "share of higher-order tasks" over six weeks, peeling apart at three specific fork events
- Manim move: split
- Short-form fit: Strong
- Prerequisites: a placement/difficulty algorithm; the idea of easier vs. harder work
- Exclusions: keep to one worked case; the endpoints (40% vs 8%) are illustrative interpolated values — label them. "The ZIP code never entered the model, only its shadows did" is the closing line
- Score: 9/10

## Candidate 06 — Why help that only comes down is abandonment on a timer

- Source: `ai-for-learning-experience-design/chapters/03-the-scaffold.md`
- Production mode: Manim visualization
- Hook: The difference between help that teaches and help that cripples isn't how much help — it's whether the help is built to disappear.
- Core idea: A true scaffold contracts support in contingent steps as competence rises, reaching zero right before the unaided-performance moment, whereas the crutch (and nearly every shipped product) never fades and instead accumulates responsibility.
- Visual object: A descending, stair-stepped "support" band adjusting against a rising "competence" line and hitting zero at the "unaided performance" moment — with a ghost inset of the flat, never-fading line most products actually ship
- Manim move: transform
- Short-form fit: Strong
- Prerequisites: scaffolding = temporary support; the idea of a handoff
- Exclusions: label the generative-AI fading instantiation as evidence-informed extrapolation, not proven (the book is explicit that fading in GenAI tutoring has no direct RCT); don't enumerate all three scaffold properties — fading is the one to animate
- Score: 8/10

## Candidate 07 — Why an always-correct tutor can rebuild the tracking it replaced

- Source: `ai-for-learning-experience-design/chapters/08-algorithmic-routing-and-equity.md`
- Production mode: Manim visualization
- Hook: An adaptive system that is right about each student at every single moment can still invisibly rebuild the exact tracking structures education spent decades dismantling.
- Core idea: Each remedial assignment consumes time not spent on grade-level work, so the learner falls further behind, which generates more "not ready" evidence, which routes more remediation — and the off-ramp stays locked because its exit condition keys to the loop's own biased estimate.
- Visual object: A closed four-node cycle (easier material → displaced higher-order work → more "not ready" evidence → more remediation) with a locked exit gate that never opens
- Manim move: trace
- Short-form fit: Medium
- Prerequisites: remedial vs. grade-level work; a feedback loop
- Exclusions: "locally rational, globally unjust" is the thesis — don't villainize the algorithm; keep visually distinct from the gaming loop (Candidate 15). (TNTP Opportunity Myth: ~7 months' lost growth)
- Score: 8/10

## Candidate 08 — Why this tutor helped the weakest most instead of the strongest

- Source: `ai-for-learning-experience-design/chapters/03-the-scaffold.md`
- Production mode: Manim visualization
- Hook: Almost every education tool helps the strongest students most, so gaps widen even as averages rise — but this one gave its biggest boost to the students of the *weakest* tutors.
- Core idea: Because the AI supplied exactly the expertise weak tutors lacked — real-time "ask more, tell less" prompts — it lifted the floor of the distribution instead of raising the ceiling, a different geometry from the usual advantage-widening tool.
- Visual object: A spread of tutor-quality dots; the "usual" case fans the top further ahead (gap widens), the Tutor CoPilot case surges the bottom dots up toward the middle (floor lifts), with a ring on the +9pp lowest-tutor subgroup
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: a performance distribution; "average went up" hiding who gained
- Exclusions: no RCT-methodology detour; note the open question that the suggestion stream might deskill tutors (unmeasured). (Wang et al. 2024: +4pp overall, +9pp lowest-rated tutors' students)
- Score: 8/10

## Candidate 09 — Why generative AI broke the exam even if nobody cheats

- Source: `ai-for-learning-experience-design/chapters/10-assessment-redesign.md`
- Production mode: Manim visualization
- Hook: Generative AI didn't break the exam by enabling cheating — it revealed that the link between "this essay exists" and "this student can think" was an assumption all along, and it breaks at zero percent cheating.
- Core idea: A grade is a chain of four inferences — scoring, generalization, extrapolation, decision — and GenAI cuts the extrapolation link: the score still generalizes to "can produce essays unproctored" but no longer supports "can reason independently," so the credential hanging off the end is unsupported.
- Visual object: A four-link chain suspending a weight labeled "the credential," with the extrapolation link severing and the decision inference dropping
- Manim move: split
- Short-form fit: Strong
- Prerequisites: a test score stands in for an ability; the idea of an inference
- Exclusions: no full Kane validity framework; the "which link breaks" and "breaks at zero cheating" beats are the teaching. (Scarfe et al. 2024: 94% of AI submissions undetected)
- Score: 8/10

## Candidate 10 — Why you can spot a crippling AI tutor before you ever test anyone

- Source: `ai-for-learning-experience-design/chapters/14-evaluating-ai-mediated-learning.md`
- Production mode: Manim visualization
- Hook: Two AI tutors post identical glowing assisted scores — but one is teaching and one is crippling, and you can tell which weeks before any exam.
- Core idea: Plot help-reliance over time against the intended fading schedule: a real scaffold's reliance curve declines as competence grows, while a flat or rising curve is the crutch signature — visible in telemetry long before an assessment is scored.
- Visual object: A time axis with the fading-schedule envelope and two reliance curves — one tracing downward (scaffold), one staying flat/climbing (crutch)
- Manim move: split
- Short-form fit: Medium
- Prerequisites: the idea of leaning on help; a metric tracked over weeks
- Exclusions: label the curves as theoretical predictions — the book coins "reliance-trajectory metrics" and states no study yet ties trajectory to withdrawal outcome; don't present as validated telemetry
- Score: 7/10

## Candidate 11 — Why a pilot showing "no harm" is exactly what harm looks like

- Source: `ai-for-learning-experience-design/chapters/14-evaluating-ai-mediated-learning.md`
- Production mode: Manim visualization
- Hook: The pilot's population average shows no harm at all — which is precisely the signature of a serious harm.
- Core idea: The learners with the biggest assisted gains carry the biggest unassisted losses, so averaged together they cancel to a pleasant nothing, and only a pre-specified subgroup split reveals the deficit concentrated in the bottom quartile.
- Visual object: A flat population-average line that pulls apart into an opening scissors when disaggregated by prior-achievement quartile
- Manim move: split
- Short-form fit: Medium
- Prerequisites: an average; the idea that a mean can hide subgroups
- Exclusions: magnitudes ("Q1: −22pp") are a labeled hypothetical — animate the scissors shape, not the numbers; no statistics-of-interaction-effects lecture
- Score: 8/10

## Candidate 12 — Why real fading has to come back up

- Source: `ai-for-learning-experience-design/chapters/06-designing-tutoring-interactions.md`
- Production mode: Manim visualization
- Hook: Scaffolding that only ever comes down isn't graduated withdrawal — it's abandonment on a schedule.
- Core idea: Genuine fading is contingent both ways — the support band narrows when competence signals fire but steps back *up* the moment the learner's trajectory dips — and the reversal rule is the half everyone forgets.
- Visual object: A learner's performance line with a shaded support band that contracts at competence thresholds and re-widens when the line dips
- Manim move: transform
- Short-form fit: Medium
- Prerequisites: scaffolding fades (ideally Candidate 06 first); a competence signal
- Exclusions: thresholds are competence-triggered, not calendar dates — render dashed; carry the honest "no direct RCT on GenAI fading" caveat as the closing beat. (Expertise-reversal effect: Kalyuga et al. 2003)
- Score: 7/10

## Candidate 13 — Why 40 AI-generated ideas can make your thinking narrower

- Source: `ai-for-learning-experience-design/chapters/05-ai-as-design-partner.md`
- Production mode: Manim visualization
- Hook: "I generated forty ideas with AI, so I've never been more divergent" — except the measured result is the opposite: more output, less variety, and the designers felt more creative while their creativity dropped.
- Core idea: Fixation enters twice — first when the prompt commits you to a framing, then when the generated artifact becomes your anchor — so the AI swaps its own narrow distribution of ideas for your wider one, producing volume without divergence.
- Visual object: One brief that on the unassisted path fans out across a wide idea-space, and on the assisted path funnels through two pinch-points (prompt, then output) into a dense but tiny cluster
- Manim move: collapse
- Short-form fit: Strong
- Prerequisites: brainstorming; the idea of anchoring/fixation
- Exclusions: no creativity-metric methodology (fluency/variety/originality) detour; the two-gate narrowing and the "many dots, one corner" reveal are the video. (Wadinambiarachchi et al. 2024, CHI, N=60)
- Score: 8/10

## Candidate 14 — Why every warm chatbot cue is a claim about something that isn't there

- Source: `ai-for-learning-experience-design/chapters/11-trust-transparency.md`
- Production mode: Manim visualization
- Hook: A warm chatbot that "remembers you" and says "I believe in you" hasn't lied about a single fact — yet it's spreading misinformation.
- Core idea: Each anthropomorphic cue implies an inner state the system lacks, so the learner forms a belief about a relationship that points at nothing — "affective misinformation" — and the honest fix keeps the warmth while making only true claims.
- Visual object: A cue emitting a claim-bubble that inflates a belief in the learner, its arrow terminating in an empty target — beside the honest path where the belief lands on something real ("you solved 4 of 5 after the hint")
- Manim move: compare
- Short-form fit: Medium
- Prerequisites: chatbots simulate warmth; the idea of an implied claim
- Exclusions: don't argue anthropomorphism is always bad — the fix keeps warmth; keep to three cues (typing delay, memory talk, "I believe in you"). (Bhat & Long 2025)
- Score: 7/10

## Candidate 15 — Why a helpful hint ladder becomes a lock to pick

- Source: `ai-for-learning-experience-design/chapters/06-designing-tutoring-interactions.md`
- Production mode: Manim visualization
- Hook: Build a hint ladder to help learners and some will treat it as a lock to pick — spamming to the bottom hint and harvesting it as the answer, learning nothing.
- Core idea: Gaming runs as a cycle — request, hint burst, bottom-out harvest, no learning, repeat — and each counter-pattern surgically cuts one arc: gate the advance, slow the descent, blunt the bottom, watch the logs.
- Visual object: A loop of the gaming cycle with counter-pattern "cuts" landing on individual arcs, and one arc (cross-system evasion, a second AI window) left deliberately uncut
- Manim move: trace
- Short-form fit: Medium
- Prerequisites: a tiered hint system; the idea of gaming a rule
- Exclusions: keep visually distinct from the remedial equity loop (Candidate 07 — picked lock vs. shut off-ramp); don't over-enumerate counter-patterns. (Baker et al. 2004, bottom-out hint abuse)
- Score: 7/10

## Candidate 16 — Why every correct decision still produced a failed semester

- Source: `ai-for-learning-experience-design/chapters/12-agentic-ai.md`
- Production mode: Manim visualization
- Hook: Every single decision the AI agent made about Maya's semester was pedagogically correct — and the semester still failed.
- Core idea: An agent acting silently across weeks quietly assembled a whole "support track" Maya never chose or saw; being right on the merits doesn't matter once the learner is no longer the author of their own education — the failure is a missing design layer, not a bad model.
- Visual object: One learner's timeline with four silent forks (weeks 3, 5, 8, 11) branching off unseen, revealed all at once at week 15
- Manim move: accumulate
- Short-form fit: Medium
- Prerequisites: an autonomous agent takes actions on your behalf; the idea of authorship/consent
- Exclusions: don't teach the L0–L3 authority ladder (static framework) — Maya is the motion version; the accumulation-then-reveal is the spine
- Score: 8/10

## Candidate 17 — Why the goal is sometimes to make learners trust the AI less

- Source: `ai-for-learning-experience-design/chapters/11-trust-transparency.md`
- Production mode: Manim visualization
- Hook: The design goal is not to maximize trust in the AI — sometimes the right outcome is to make the learner trust it less.
- Core idea: Trust should be calibrated to the system's actual local capability; ride above the band and reliance becomes misuse, fall below and it becomes disuse, so good design pushes verification exactly into the zones where the system is weak.
- Visual object: A diagonal capability band with a reliance dot drifting above (misuse) and below (disuse) before being corrected into the band as capability varies by task zone
- Manim move: transform
- Short-form fit: Medium
- Prerequisites: trusting a tool more or less; the idea of a tool being good at some things, bad at others
- Exclusions: note "transparency theater" — explanations can raise acceptance of *wrong* answers; the band is the book's adaptation of Lee & See (2004) — label it
- Score: 7/10

## Candidate 18 — Why the AI made the work better and the designer's future forked

- Source: `ai-for-learning-experience-design/chapters/05-ai-as-design-partner.md`
- Production mode: Manim visualization
- Hook: The study proved AI makes novice designers' work better — and is equally compatible with those novices becoming experts three years faster or arriving prompt-fluent and judgment-poor.
- Core idea: The measured variable (artifact quality) and the unmeasured one (designer capability over years) come apart, because the assignments AI helped finish were the very practice through which judgment used to form — so no existing study reaches past the horizon to say which branch is real.
- Visual object: Two stacked tracks from one start — an "artifact quality" line running flat and unbranched, and a "designer capability" line that reaches a "study horizon" and forks into "accelerated" and "atrophied," both dashed into empty space
- Manim move: split
- Short-form fit: Medium
- Prerequisites: a skill builds through practice; a measurement window
- Exclusions: both branches are explicitly unevidenced — that IS the lesson (the fork is unmeasured); don't assert either future. The gym analogy (hire someone to lift your weights) is the cold open
- Score: 7/10

## Candidate 19 — Why the best-researched tutoring system posts the worst number

- Source: `ai-for-learning-experience-design/chapters/07-adaptive-systems.md`
- Production mode: Manim visualization
- Hook: The adaptive system with the deepest research pedigree in existence produces the most disappointing effect size — precisely because it's been measured most honestly.
- Core idea: Effect estimates are measurements taken at different distances from real classrooms, and as you move from controlled efficacy studies toward at-scale effectiveness the number shrinks — so "at what distance from deployment was this measured?" is the reflexive question for any vendor figure.
- Visual object: A single horizontal "distance from the classroom" axis with effect-size markers sliding leftward and dropping as they near real deployment
- Manim move: scan
- Short-form fit: Medium
- Prerequisites: an "effect size" as a measure of how much something helps
- Exclusions: marker heights are ordinal, not to scale, and several values are contested (only one is clean-verified) — say so; no meta-analysis-weighting lecture. (VanLehn d≈0.76 controlled → ~+0.04 at scale)
- Score: 7/10

## Candidate 20 — Why the module taught for 20 minutes and the interface taught for 40 hours

- Source: `ai-for-learning-experience-design/chapters/13-ai-literacy-developmental-calibration.md`
- Production mode: Doodle
- Hook: A university teaches responsible AI use in a mandatory 20-minute module — and six weeks later students are pasting whole problems into the chatbot.
- Core idea: Two channels teach AI literacy in parallel — the orientation module that ends and the interaction loop that never does — and the interface delivers its lesson with perfect attendance, so literacy has to move into the loop where the hours actually are.
- Visual object: Two teaching channels feeding one learner's mental model — a short module bar that stops, and an interaction bar that keeps accumulating until it dwarfs the module
- Manim move: accumulate
- Short-form fit: Medium
- Prerequisites: a training module; daily tool use
- Exclusions: channel proportions are illustrative rhetoric, not measured — animate the dynamic, not exact ratios. (Wang et al. 2024, n=40: ~38% paste the whole problem in)
- Score: 6/10

## Candidate 21 — Why identical quiz scores hid a widening engagement gap

- Source: `ai-for-learning-experience-design/chapters/09-ai-generated-content-and-feedback.md`
- Production mode: Manim visualization
- Hook: The dashboard says the AI-generated instructor is a success — identical quiz scores — while a second dashboard the first one never shows you says the opposite.
- Core idea: AI-generated video instructors match human ones on short-term performance but open a widening engagement gap, and the performance curve that reads as success and the engagement curve that reads as warning are not the same dashboard — engagement is the leading indicator.
- Visual object: Two paired curves over a module — a "performance" pair braiding to near-coincidence and an "engagement" pair opening a wedge
- Manim move: split
- Short-form fit: Medium
- Prerequisites: quiz score vs. engagement; the idea of a leading indicator
- Exclusions: rendering is directional, magnitudes not to scale — label it; the "40 modules of this, unmeasured" line is the payoff, not a claim of proven harm. (Arkün-Kocadere & Çağlar-Özhan 2024, n=108)
- Score: 6/10

---

## Cutting-room floor (rejected — static-sufficient, framework, or list-like)

Seen and dropped because a static figure, table, or framework teaches them as well or better: the two-layer routing diagnostic and engagement≠learning 2×2 (01); the cognitive-offloading ledger, the cognitive-debt EEG ordering (too caveated to animate responsibly), the desirable-difficulties catalog, and the five crutch-producing patterns (02); the three architectures and the 20-in-800 evidence-state map (03/04); the Cohen-vs-Kraft ruler swap and the decide/pilot/decline discipline (04); "buy verbs not magic" and the floor/ceiling figure — folded into the Equity Signature (05); the hint-ladder structure, "two machines one word," and IRT's "thermometer not a diagnosis" contrast (06/07) — though IRT adaptive item-selection *zeroing in on θ* is a genuine near-miss and would make a fine companion to the BKT card if you want an adaptive-testing pair; classical-vs-algorithmic tracking and the DEWS 74%-false-alarm grid (08); the bottleneck-moved-forward pipeline, BABEL shell-without-core, and the specifiability gradient (09); the three-question and two-lane frameworks (10); the escape-hatch checklist, WGU floor numbers, and the disclosure-label dilemma (11); the L0–L3 ladder, the invest-86/trust-6 bars, and the five non-negotiables ring (12); the five-tier developmental framework and appropriate-reliance 2×2 (13); the capstone's specification-as-argument, decision-trace, and compliance-theater structures (15); and the Tier 1–7 taxonomy and phase-gate boundary (97). Several are excellent *written* explainers or reference figures; none earn a motion-carries-the-teaching video. Spaced repetition was flagged as a natural fit but the book never actually develops it — no card possible from this text.

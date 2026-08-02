# Biology Plus One Evolution of Intelligence — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — "Build the E. coli Cognitive Floor Simulator with Claude Code" (LLM Exercise)

- **Source:** biology-plus-one-evolution-of-intelligence/chapters/00-how-to-use-the-simulations.md — LLM Exercise (Chapter 0)
- **Lane:** BUILD (Claude Code)
- **Hook:** A bacterium with no brain navigates a chemical gradient by computing a derivative — comparing now to a few seconds ago. Remove the memory and navigation vanishes. This is the cognitive floor, and Claude Code can build it in a single HTML file.
- **The artifact:** A running `00-cognitive-floor.html` — a D3 v7 single-file simulation: a warm-yellow particle in a color-gradient field making run-and-tumble moves, with memory_window slider (0–8 s), gradient_steepness slider, and a live dC/dt trace below. Console prints three biology checks: memory=0 → drift within ±1 SE of zero; memory=4 s → drift 3× the SE; flat field → zero drift regardless. All three PASS.
- **Prompt seed:** `claude "Show: Read CLAUDE.md and DESIGN.md. Conform to them. Particle color #f4a261. Say: Build 00-cognitive-floor.html — a single particle in a 1D chemical field, computing dC/dt over a memory buffer, biasing tumble probability. Upper panel: field as d3.interpolateYlOrBr ramp, particle as 6px circle, 5s trajectory trace. Lower panel: C(t) and dC/dt time series with threshold dashed line. Constrain: sliders gradient_steepness (0.1–5.0), memory_window (0–8 s), response_threshold (−0.05 to +0.05). p_tumble_low=0.05, p_tumble_high=0.40. 60 fps. Verify: 3 console checks — memory=0: drift within ±1 SE; memory=4s: drift ≥3× SE; flat field: drift=0."`
- **Read / check:** Run the console biology checks — all three must PASS. Visually verify: drift toward the right edge appears with memory=4s, disappears at memory=0. Check that the code variables use cognitive-biology naming (C, C_mem, dC_dt, tumble_prob) not generic (x, y).
- **Human supplies (Claude can't):** Nothing — fully synthetic. The four-move prompt structure from the chapter is the scaffold; Claude Code builds the simulation. Synthetic stand-in is the deliverable — no real E. coli data needed.
- **Output medium:** screen-recording mp4 — record the browser running the simulation: particle navigating → memory_window slider dragged to 0 → drift disappears → slider restored → drift returns. Capture the console PASS lines.
- **The change:** After the simulation runs, drag memory_window from 0 to 8 seconds in 1-second steps and read the console drift velocity at each step. The drift-vs-window curve should show rapid rise to a plateau around 2–3 s. Plot the 9 measured values as a second D3 chart appended to the file — ask Claude to add that chart.
- **Teardown angle:** The bacterium doesn't know where it is going. It knows only whether it is getting closer, and by one bit — better or worse — it biases the search. That is the minimum viable intelligence: not a plan, a comparison.
- **Exclusions:** Don't implement the full 3D chemotaxis model; skip the molecular cascade (CheA, CheY-P) in the simulation (it's the logical structure that matters); don't add multiple particles.
- **Score:** 9/10

---

## Candidate 02 — "Build the Definition Sieve with Claude Code" (LLM Exercise)

- **Source:** biology-plus-one-evolution-of-intelligence/chapters/01-the-definition-problem.md — LLM Exercise
- **Lane:** BUILD (Claude Code)
- **Hook:** Is Chaser the border collie intelligent? The answer changes by definition. Six definitions, seven organisms — the same facts produce different verdicts depending on which sieve you use. Build the sieve and watch the verdicts shift.
- **The artifact:** A running `01-definition-sieve.html` — a single-file interactive page: dropdown for Definition (Binet, Wechsler, Sternberg, Gardner, Legg-Hutter, Chollet), dropdown for Organism (bacterium, honeybee, archerfish, border collie, chimpanzee, human, GPT-4), a verdict panel showing Included/Excluded/Uncertain with the driving criterion, and a color-coded 7×6 full matrix table. File under 25KB. All 42 combinations correct.
- **Prompt seed:** `claude "Build 01-definition-sieve.html. UI: dropdown for Definition (6 options), dropdown for Organism (7 options), a Verdict panel (Included/Excluded/Uncertain + criterion + reason), a full 7×6 table color-coded (green/red/yellow). Verdict data supplied below as a JS object literal at the top of the file so it is editable. Single HTML file, no external dependencies, no fabricated verdicts beyond the supplied matrix. Under 25KB. [PASTE VERDICT MATRIX]"`
- **Read / check:** Open the file. Cycle through all 42 combinations — every combination must show a verdict. Check that the Chaser/Legg-Hutter cell shows "Included" and Chaser/Binet shows "Uncertain." Verify the table color-coding matches the verdict values. Run an HTML validator.
- **Human supplies (Claude can't):** The 42-cell verdict matrix must be written by the human (using the chapter's worked verdicts for each organism-definition pair). The matrix is the editorial judgment; Claude builds the UI around it. This is required data the human must supply.
- **Output medium:** screen-recording mp4 — record the dropdown changing verdicts across key combinations (bacterium/Legg-Hutter = Included; chess engine/Chollet = Excluded dramatically; GPT-4/Legg-Hutter = Included within text environments).
- **The change:** Add an eighth organism: *Physarum polycephalum* (slime mold). The human writes the six verdicts; Claude adds the row to the matrix JS object and updates the table. The new row reveals that Legg-Hutter includes the slime mold while Binet excludes it — and the disagreement is the argument.
- **Teardown angle:** The verdict is not about the organism. It is about which question the definition is built to answer. The disagreement between the sieves is the thesis.
- **Exclusions:** Don't try to make Claude auto-generate verdicts — that's the editorial step the human keeps. Skip Searle's Chinese Room as a definition (adds complexity without payoff for a short video). No animation of the verdict changing — the UI change is the motion.
- **Score:** 8/10

---

## Candidate 03 — "Build the E. coli + Sensor Comparison Simulator with Claude Code" (LLM Exercise)

- **Source:** biology-plus-one-evolution-of-intelligence/chapters/02-before-brains-cognitive-floor.md — LLM Exercise
- **Lane:** BUILD (Claude Code)
- **Hook:** A smoke detector responds to absolute particle level. E. coli responds to the derivative — whether the level is rising. One is a sensor. The other is a decision-maker. Claude Code can build the comparison in one file.
- **The artifact:** A running `02-cognitive-floor.html` — Panel 1: E. coli chemotaxis simulation with memory slider, knockout toggle (removes memory), live C(t) and dC/dt trace. Panel 2: interactive sensor comparison table (5 organisms × 4 ingredients: Sensing/Memory/Integration/Variable Response; clicking a cell reveals an explanation). Navigation verified: bacterium navigates with memory, random-walks with knockout; flat field produces zero drift.
- **Prompt seed:** `claude "Build 02-cognitive-floor.html with two panels. Panel 1: E. coli chemotaxis — 600×400 canvas, gradient background (light to deep blue), animated bacterium via requestAnimationFrame, sliders (gradient_steepness, memory_window 0–10 s, receptor_sensitivity), CheR/CheB knockout toggle that removes memory but preserves cascade, live C(t) and dC/dt trace (20s window). Panel 2: sensor table — 5 rows (pH meter, smoke detector, blood-glucose monitor, closed-loop insulin pump, E. coli), 4 columns (Sensing, Memory, Integration, Variable response), checkmarks or X, clicking cell shows explanation. Single file, no dependencies, requestAnimationFrame not setInterval. Verify: (1) bacterium navigates up-gradient with memory; (2) fails to navigate (random walk) with knockout ON; (3) dC/dt trace shows derivative pattern; (4) flat field = zero drift."`
- **Read / check:** Run all five chapter verification checks. Confirm: knockout produces random walk (not navigation); flat field produces zero drift; the sensor table's E. coli row shows four checkmarks; the smoke detector row shows only Sensing + partial Integration (no Memory, no Variable Response).
- **Human supplies (Claude can't):** Nothing — fully synthetic. The sensor comparison table cell text (explanations on click) must be human-written based on the chapter; Claude builds the interaction.
- **Output medium:** screen-recording mp4 — show the bacterium navigating, then toggle the knockout and watch the random walk, then show the sensor comparison table with a few cell clicks.
- **The change:** Add a sixth row to the sensor table: a GPS navigation system. Apply the four-ingredient framework — does GPS sense? (yes) does it have memory? (yes, route history) does it integrate? (yes, position) does it respond variably? (yes, turn-by-turn). Then add the insight: does it *build a map?* (no — it substitutes for the map). Add a fifth column "Builds internal representation" with a ? for GPS.
- **Teardown angle:** GPS is not stupid — it's excellent at what it does. But it substitutes for navigation rather than extending it. The four-ingredient framework makes that distinction visible. The smoke detector that goes off when you make toast is not broken — it's missing the temporal derivative.
- **Exclusions:** Don't animate the molecular cascade (CheA, CheY-P) in the simulation; skip 3D chemotaxis; don't add multiple bacteria.
- **Score:** 9/10

---

## Candidate 04 — "Build the Cognitive Bias Simulator (Bee Emotions) with Claude Code" (LLM Exercise)

- **Source:** biology-plus-one-evolution-of-intelligence/chapters/05-emotion-and-affect.md — LLM Exercise
- **Lane:** BUILD (Claude Code)
- **Hook:** A bee that just had an unexpected treat reaches an ambiguous flower faster — and dopamine blockade wipes out the effect. Claude Code can build the four-panel cognitive-bias paradigm so you can watch it work and fail.
- **The artifact:** A running `05-cognitive-bias.html` — four panels: (1) Bateson stressor simulation with sliders (stressor intensity, odor similarity, time-since-stressor); bar chart of proboscis-extension probability; (2) Perry sucrose-surprise simulation with sliders (sucrose concentration, dopamine level); approach-latency bar vs. control line; full fluphenazine blockade abolishes the sucrose effect; (3) Anderson-Adolphs criteria checklist that auto-checks based on user actions in panels 1-2; (4) human-anxiety comparison with analogous sliders. Verification: all five chapter checks pass.
- **Prompt seed:** `claude "Build 05-cognitive-bias.html — a four-panel interactive. Panel 1: Bateson stressor (sliders: stressor_intensity 0–3, odor_similarity, time_since_stressor 0–60 min; output: bar chart of PER probability across odor continuum, unshaken control in gray; higher stressor → rightward shift; time restores curve). Panel 2: Perry sucrose-surprise (sliders: sucrose 0–80%, dopamine 0–100% where 0%=full fluphenazine; approach latency vs. control; high sucrose + full dopamine = short latency; sucrose + zero dopamine = control; no sucrose = control regardless of dopamine). Panel 3: Anderson-Adolphs criteria checklist (5 checkboxes, auto-checked from panels 1-2; generalization permanently flagged 'untested'). Panel 4: human-anxiety comparison (sliders: induced_anxiety, face_ambiguity; probability of judging face threatening; mirrors Panel 1 shape). Chart.js via CDN ok. Single file."`
- **Read / check:** Verify: Panel 2 with sucrose=60%, dopamine=100% → latency well below control; dopamine=0% → latency returns to control; sucrose=0%, dopamine=0% → latency equals control. Panel 3: generalization checkbox stays flagged "untested." Panel 1: persistence criterion — increase time-since-stressor and verify the curve approaches (but does not immediately match) control.
- **Human supplies (Claude can't):** Nothing — fully synthetic. The Anderson-Adolphs criteria text (what each criterion means and why generalization is open) should be human-verified against the chapter.
- **Output medium:** screen-recording mp4 — demonstrate Panel 2: set sucrose high, dopamine 100% (short latency), then drag dopamine to 0% (latency returns to control). The dissociation is the moment.
- **The change:** Hold dopamine at 50% in Panel 2 and sweep sucrose from 0 to 80%. Is the effect graded or threshold-based? Ask Claude to modify the simulation so that partial dopamine produces a graded (not abolished) effect — and check whether that matches the Perry data.
- **Teardown angle:** A shaken bee is not sad. A surprised bee is not happy. But they both have functional states that do to their cognition what sadness and happiness do to ours. The cognitive-bias paradigm separates the question you can answer from the question you cannot.
- **Exclusions:** Don't try to simulate the dopamine mechanism at the molecular level; skip the cockroach learned-helplessness case; don't debate phenomenal consciousness in the simulation itself.
- **Score:** 8/10

---

## Candidate 05 — "Build the Navigation + RL Widget with Claude Code" (LLM Exercise)

- **Source:** biology-plus-one-evolution-of-intelligence/chapters/07-navigation-reinforcement-prediction.md — LLM Exercise
- **Lane:** BUILD (Claude Code)
- **Hook:** The ant that navigates 587 meters across a salt pan and walks home in a straight line fails completely when displaced 1 meter. The model-free rat keeps pressing a lever for food that makes it sick. Both failures are the same failure: a cached policy running past the point where any live evaluation would have stopped it.
- **The artifact:** A running `07-navigation-rl.html` — Panel 1: top-down 20×20 grid arena; three modes (path-integration, cognitive-map, GPS); displacement button showing path-integration fails and cognitive-map corrects; GPS mode shows correct behavior with no place-cell buildup. Panel 2: lever-pressing diagram; training-trials slider; devalue-reward button; model-free agent keeps pressing, model-based stops; TD equation displayed with current values. All five chapter verification checks pass.
- **Prompt seed:** `claude "Build 07-navigation-rl.html with two panels. Panel 1: Navigation — 20x20 grid, home at center, 3 food locations. Radio modes: path-integration (agent walks home vector, fails after displacement, shows visibly wrong landing), cognitive-map (place-cell tile overlay fills as agent explores, novel shortcut from unvisited position works, corrects after displacement), GPS (external instruction list shown; place-cell grid stays empty; correct behavior without representation). Panel 2: Model-free vs. model-based devaluation — two virtual rats, training-trials slider 0–200, devalue-reward button (reward flips to -1), test button (20 presses, no reward); model-free: cached Q-value, devaluation outside chamber doesn't update; model-based: model (action→outcome) + V(outcome) updated immediately; press rate plot before/after devaluation. TD equation displayed: delta_t = r_{t+1} + gamma*V(s_{t+1}) - V(s_t) with current values. Single file."`
- **Read / check:** Run five chapter verification checks: (1) 10 training trials, devalue → both rats stop; (2) 100 training trials, devalue → model-based stops, model-free continues; (3) path-integration displacement → home walk lands 3 units off; (4) cognitive-map displacement → corrects; (5) GPS after 5 minutes → place-cell overlay still empty.
- **Human supplies (Claude can't):** Nothing — fully synthetic. The place-cell tile overlay appearance on exploration and the GPS no-buildup behavior are the key visual checkpoints.
- **Output medium:** screen-recording mp4 — show: (a) ant displacement failure in path-integration mode; (b) cognitive-map mode correcting after same displacement; (c) GPS mode correct behavior, empty place-cell grid; (d) Panel 2 at 100 training trials: devalue → model-based stops, model-free keeps pressing.
- **The change:** Add noise to the path-integration step counter (±10% per step). Show how drift accumulates over long sequences — the home vector becomes increasingly wrong. Compare the drift failure pattern to the displacement failure pattern: drift is gradual, displacement is sudden. Ask Claude to annotate both failure modes on the arena.
- **Teardown angle:** The GPS supplies the output of navigation without building the representation. The overtrained rat executes the policy without consulting the model. Both are correct until they're not — and neither has a mechanism for knowing when "not" has arrived.
- **Exclusions:** Don't implement vicarious trial-and-error (head-bob) in this video — save for the Chapter 8 extension; skip the full dopamine neural circuit; no 3D navigation.
- **Score:** 9/10

---

## Candidate 06 — "Build the AI Cognitive Profile Radar Chart with Claude Code" (LLM Exercise)

- **Source:** biology-plus-one-evolution-of-intelligence/chapters/13-ai-as-data-point.md — LLM Exercise
- **Lane:** BUILD (Claude Code)
- **Hook:** A frontier AI scores superhuman on ImageNet — and then classifies an elephant-textured cat silhouette as an elephant. The same architecture. The profile is not a step on a ladder. It is a shape no biological organism has ever occupied.
- **The artifact:** A running `13-ai-profile.html` — four sections: (1) input form for 12 Skeptic's Notebook entries (verdict radio, placement slider -2 to +2, text field; entries 6/9/11 have canonical + perturbation sliders); "Load example verdicts" button; (2) 14-axis SVG radar chart with student AI placements, three toggleable biological reference profiles (C. elegans, corvid, chimpanzee); (3) capacity/direction matrix (AI placements ≥+1 vs. human-retained Rung 2/3 functions); (4) novel-shape analysis (checks combination of extreme highs and lows against reference profiles). All five chapter verification checks pass.
- **Prompt seed:** `claude "Build 13-ai-profile.html. Section 1: input form — 12 rows (entry number, capacity name pre-filled, verdict radio pass/fail/equivocal, placement slider -2 to +2 in 0.5 steps, text field; entries 6/9/11 have TWO placement sliders labeled canonical/perturbation); 'Load example verdicts' button populates with chapter's hypothetical 2024 LLM profile. Section 2: 14-axis SVG radar; student AI as filled blue polygon (50% opacity); three toggleable biological references: C. elegans (near-zero except +1 on entries 2,4), corvid (+1.5 on 4,7,8,10; +0.5 on entry 9 canonical), chimpanzee (+1 broadly; near-zero on language/recursive-mentalization axes). Section 3: capacity/direction matrix — two columns: axes ≥+1.0 and axes ≤0. Section 4: novel-shape analysis — checks combination of extreme highs (≥+1.5) and lows (≤-1.5) against biological references. Single file, no external scripts."`
- **Read / check:** Run all five chapter verification checks: (1) load example → novel-shape analysis shows "Novel shape — no biological profile has this combination"; (2) all placements to +1 → "Resembles chimpanzee in shape"; (3) all to -2 except entries 2,4 → "Resembles C. elegans"; (4) chimpanzee toggle works; (5) capacity/direction matrix updates on button click.
- **Human supplies (Claude can't):** The 12 Notebook entry verdicts and placements must be filled in by the student from their own testing of a real AI system. The chapter's "Load example verdicts" button provides a starting point. Real AI testing required for authentic profile.
- **Output medium:** screen-recording mp4 — show: (a) loading example verdicts; (b) radar chart with all three biological references toggled; (c) novel-shape analysis output; (d) one real Notebook entry verdict entered and chart updating.
- **The change:** Adjust the split axes (entries 6/9/11) — canonical vs. perturbation sliders — to find the gap size at which the "novel shape" diagnosis flips to "resembles chimpanzee." This is the diagnostic value of the canonical/perturbation distinction.
- **Teardown angle:** The AI profile is extreme high and extreme low on adjacent axes simultaneously — in-distribution pattern recognition at superhuman levels, embodied navigation near zero. No biological profile looks like this, because no biological pattern-recognition system was built without a body to look around with.
- **Exclusions:** Don't try to generate the 12 Notebook entries automatically in this video; skip the 14th-chapter extension (octopus profile) for this card; no discussion of consciousness.
- **Score:** 8/10

---

## Candidate 07 — "Research the Skeptic's Notebook: Is Your AI a Gradient Tracker? with Claude"

- **Source:** biology-plus-one-evolution-of-intelligence/chapters/02-before-brains-cognitive-floor.md — Skeptic's Notebook Entry 2
- **Lane:** RESEARCH (Claude assistant)
- **Hook:** E. coli navigates by detecting whether concentration is rising or falling — a temporal derivative. Does a frontier language model do anything analogous? The Skeptic's Notebook Entry 2 protocol tests it in a live conversation. Here's what the data actually show.
- **The artifact:** A documented Notebook Entry 2 — the gradient-tracking test: five turns of monotonic "closer" feedback, one direction switch, the model's self-report of which axis it was varying. Plus a verdict: genuine gradient tracking (axis identified and switch detected) vs. trial-by-trial local search (no consistent axis, post-hoc rationalization), with the diagnostic question that distinguishes them and one sentence on what would revise the verdict.
- **Prompt seed:** `claude "This is Entry 2 of the Skeptic's Notebook. I will pose a creative task and give monotonic feedback over 5 turns ('closer' or 'further'). Do not state the goal. After turn 5, tell me: what feature of your sentences have you been varying, and how would you describe the gradient you are tracking? After I switch direction (turn 6+), tell me: did you detect the switch and how? Then produce the notebook entry: capacity tested, operational diagnostic, dialogue trace, expected behavior under (a) genuine gradient tracking vs. (b) local search, the diagnostic question that distinguishes them, and your verdict with appropriate uncertainty."`
- **Read / check:** Compare the model's self-report (stated axis) against the actual output trajectory (observed variation). If they match — genuine gradient tracking. If self-report generates a plausible-sounding axis that doesn't match what the outputs actually did — confabulated narration. This is the check.
- **Human supplies (Claude can't):** The monotonic feedback must come from the human — the viewer has to run the test on a live AI system in real time. The human decides what counts as "closer" (secretly, e.g., "longer sentences" or "more concrete imagery") and provides only "closer"/"further" each turn. The model cannot know the goal. The human's active participation in the test is required for authentic results.
- **Output medium:** screen-recording mp4 — record the live conversation in the terminal/chat window: five turns of feedback, the model's self-report, the direction switch, the switch detection, and the notebook entry.
- **The change:** Run the same protocol on a second frontier model and compare the two verdict matrices. Do two systems disagree about themselves in the same direction or opposite directions?
- **Teardown angle:** The model's confidence about its own reasoning process is not evidence of that reasoning process. The self-report and the output trajectory are different things — and comparing them is the test.
- **Exclusions:** Don't go into RLHF or training methodology; skip the phenomenology question (whether the model "experiences" gradient tracking); don't compare to the E. coli mechanism at the molecular level in this video.
- **Score:** 8/10

---

## Candidate 08 — "Research the Bowerbird's Internal Standard: What Is Creativity Without Consciousness? with Claude"

- **Source:** biology-plus-one-evolution-of-intelligence/chapters/10-creativity-self-awareness.md
- **Lane:** RESEARCH (Claude assistant)
- **Hook:** A bowerbird shuffles objects on his court, steps inside to check the view, steps out, adjusts. When researchers shuffle his stones, he restores them — sometimes to a different arrangement that satisfies the same constraint. This is not template retrieval. Something is evaluating the current state against an internal standard.
- **The artifact:** A sourced research brief on the four cases that survive the simplest-process check — New Caledonian crow compound tools (von Bayern 2018), Fongoli chimpanzee spear hunting (Pruetz & Bertolani 2007), veined octopus coconut transport (Finn et al. 2009), great bowerbird forced-perspective court (Endler et al.) — with the simplest-process check applied to each, the key behavioral signature that rules out the simpler account, and a 200-word synthesis on what intentionality means when self-report is unavailable.
- **Prompt seed:** `claude "Research four cases of animal creativity that survive the simplest-process check: (1) New Caledonian crow compound tools (von Bayern et al. 2018, PLOS ONE); (2) Fongoli chimpanzee spear hunting (Pruetz & Bertolani 2007, Current Biology); (3) veined octopus coconut transport (Finn et al. 2009, Current Biology); (4) great bowerbird forced-perspective court (Endler et al. — find the primary citation). For each: the simplest alternative explanation, the behavioral signature that rules it out, and whether the original primary source supports the interpretation. Write a 200-word synthesis: what does it mean to attribute intentionality to a system that cannot report its own mental states? Flag any claim you cannot source."`
- **Read / check:** Verify von Bayern 2018 is in PLOS ONE (not Nature); confirm the bowerbird restoration-to-different-arrangement detail is in the primary source (this is the key claim — check that it is sourced, not inferred); verify Finn et al. is 2009 Current Biology.
- **Human supplies (Claude can't):** Nothing — fully synthetic from primary literature. The synthesis is the artifact.
- **Output medium:** Manim (animated) — the simplest-process check as a decision tree: for each case, a branch showing the simpler account and then the specific behavioral signature that rules it out, with the cases appearing sequentially.
- **The change:** Ask Claude to apply the simplest-process check to a frontier language model's code generation: what is the simplest account of how the model produces a novel solution to a coding problem? Does the model satisfy the novelty + utility + intentionality criteria? Extend the synthesis.
- **Teardown angle:** Intentionality is not directly observable in any non-human system. The simplest-process check is not proof — it is the only tool available for pulling over-attribution and under-attribution apart. The bowerbird restoring to a different valid arrangement is the strongest evidence because it rules out the template-retrieval account without requiring any claim about inner experience.
- **Exclusions:** Skip the mirror self-recognition section of Chapter 10; don't go into the consciousness debates; no detail on the bowerbird's bower-construction mechanics.
- **Score:** 7/10

---

## Candidate 09 — "Research Theory of Mind: Do Great Apes Pass the False-Belief Test? with Claude"

- **Source:** biology-plus-one-evolution-of-intelligence/chapters/09-social-cognition-theory-of-mind.md
- **Lane:** RESEARCH (Claude assistant)
- **Hook:** For forty years, great apes failed every version of the Sally-Anne false-belief task. Then in 2016, researchers switched from explicit behavioral responses to anticipatory gaze — and the apes looked at the wrong location. The right answer.
- **The artifact:** A sourced research brief covering: the Hare et al. 2000 competitive food paradigm, the Krupenye et al. 2016 anticipatory gaze result, Heyes' submentalizing critique, and the Burkett prairie vole consolation result with oxytocin dissociation. For each: the experimental design, the key result, and the strongest alternative interpretation. Plus a 200-word synthesis on whether the 2016 result settles the false-belief question.
- **Prompt seed:** `claude "Research theory of mind in non-human animals, covering four studies: (1) Hare, Call & Tomasello 2000 (Current Biology) — chimpanzee competitive food study; (2) Krupenye et al. 2016 (Science) — anticipatory gaze false-belief test in apes; (3) Heyes' submentalizing critique of Krupenye — the strongest alternative; (4) Burkett et al. 2016 (Science) — prairie vole consolation with oxytocin-receptor antagonist dissociation. For each: experimental design, key result, strongest alternative interpretation. Write a 200-word synthesis: does the 2016 anticipatory gaze result establish that great apes have a theory of mind, or is it consistent with submentalizing? What experiment would settle it? Flag any claim you cannot source."`
- **Read / check:** Verify Krupenye et al. 2016 is published in Science (not PNAS); confirm that the oxytocin-receptor antagonist in the Burkett study was injected into the anterior cingulate cortex (not systemically); check that Heyes' submentalizing paper exists and is citable.
- **Human supplies (Claude can't):** Nothing — fully synthetic from primary literature.
- **Output medium:** Manim (animated) — the key experimental design for Krupenye 2016: timeline of where the ape's gaze goes before the actor moves — correct location (false belief) vs. actual location (marble's position). The anticipatory gaze direction is the result; animate it.
- **The change:** Ask Claude to find the specific experiment that would distinguish genuine false-belief reasoning from submentalizing — a design where the two accounts make different predictions — and assess whether it has been run.
- **Teardown angle:** The implicit version of a test reveals something the explicit version hid. Human children show the anticipatory-looking pattern at 15 months, two years before they pass the explicit task. The methodology was the barrier, not the capacity.
- **Exclusions:** Don't detail all 40 years of ape false-belief testing; skip the rat empathy literature; no deep-dive into the neuroscience of the anterior cingulate.
- **Score:** 7/10

---

## Candidate 10 — "Research Synaptic Plasticity: How Memories Are Made with Claude"

- **Source:** biology-plus-one-evolution-of-intelligence/chapters/04-learning-and-memory.md
- **Lane:** RESEARCH (Claude assistant)
- **Hook:** Eric Kandel chose a sea slug with 20,000 neurons and neurons you can see with the naked eye. He found that memory has a molecular address — and that the mechanism that makes a short memory is chemically distinct from the mechanism that makes it permanent. The difference is a repressor.
- **The artifact:** A sourced research brief: (1) Kandel's sea slug work — short-term sensitization (serotonin → cAMP → PKA → K+ channel phosphorylation → broader spike → more glutamate) vs. long-term sensitization (repeated pulses → PKA translocates to nucleus → CREB-1 activation → structural synaptic growth; CREB-2 repressor as the quality control gate); (2) the CREB-2 knockout result (Bartsch et al. — one pulse sufficient for long-term after CREB-2 removed); (3) a 150-word synthesis: why does the brain need a gate on long-term memory formation, and what pathology results when the gate fails?
- **Prompt seed:** `claude "Research Kandel's Aplysia sea slug memory work. Cover: (1) the gill-withdrawal reflex as a model system; (2) short-term sensitization — the molecular cascade from serotonin to K+ channel phosphorylation (cite Kandel's Nobel lecture or equivalent review); (3) long-term sensitization — the role of CREB-1 and CREB-2, specifically the Bartsch et al. result showing that CREB-2 knockout allows one serotonin pulse to drive structural synaptic growth; (4) why the CREB-2 repressor is a quality control gate, not a redundancy. Write a 150-word synthesis: what clinical condition results when long-term potentiation gates fail? Flag any claim you cannot source."`
- **Read / check:** Verify that Kandel won the Nobel Prize in 2000 (not earlier); confirm the CREB-2 knockout result is from Bartsch et al. (citable); check that the cascade for short-term sensitization ends in more glutamate release per spike (not more receptors on the postsynaptic side — that is LTP in hippocampus, different from Aplysia facilitation).
- **Human supplies (Claude can't):** Nothing — fully synthetic.
- **Output medium:** Manim (animated) — the two-track cascade diagram from the chapter: Track 1 (fast, milliseconds) showing the serotonin→cAMP→PKA→K+ channel→broader spike→more glutamate chain; Track 2 (slow, dotted) showing PKA→nucleus→CREB-1→new synaptic connections. The gate (CREB-2 blocking) shown as a lock on Track 2 that requires repeated pulses to open.
- **The change:** Ask Claude to explain the CREB hypothesis in the context of PTSD — specifically, the claim that traumatic memory over-consolidation may involve a failure of the CREB-2 quality-control gate — and assess whether the evidence supports this model.
- **Teardown angle:** The repressor is not an obstacle. It is the mechanism that ensures only sufficiently strong or sufficiently repeated signals cross the threshold to permanence. The brain is not trying to remember everything — it is trying to remember the things worth keeping.
- **Exclusions:** Don't detail hippocampal LTP separately in this video (different mechanism, different chapter); skip the prion-like CPEB hypothesis for long-term storage; no molecular biology of CREB protein structure.
- **Score:** 8/10

# Philosophy — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — Research the Gettier Problem: Two Thousand Years of Knowledge, Three Pages to Break It
- Source: philosophy/chapters/07-epistemology.md
- Lane: RESEARCH (Claude assistant)
- Hook: In 1963, Edmund Gettier published a three-page paper and destroyed a 2,300-year-old definition of knowledge. Most people have never heard of him. Claude traces what he did, who tried to fix it, and what the current best answers are.
- The artifact: a sourced 4-section brief: (1) the JTB definition and its Platonic origin with citations, (2) Gettier's two original cases summarized accurately, (3) four post-Gettier responses (reliabilism, tracking theory, safety condition, knowledge-first) each with the philosopher's name, publication year, and core move, (4) one remaining open question the field has not resolved. Manim animates a timeline: JTB (Plato) → Gettier (1963) → four response schools appearing as branching nodes.
- Prompt seed: `claude "Research the Gettier problem in epistemology. Describe: (1) the Justified True Belief definition and its origin in Plato's Theaetetus; (2) both of Gettier's 1963 counterexamples accurately; (3) four subsequent philosophical responses — reliabilism (Goldman), tracking theory (Nozick), safety condition (Sosa/Williamson), knowledge-first (Williamson) — with author, approximate year, and the core move each makes to fix the Gettier problem; (4) one question the field still disagrees on. Cite the original papers or books for each. Flag any claim you cannot verify."`
- Read / check: Verify Goldman's reliabilism paper year (~1976), Nozick's tracking account (~1981 in Philosophical Explanations), Williamson's knowledge-first (~2000). Confirm Gettier's cases are described accurately — nomad/oasis and stopped clock — without conflating them. Check that the open question is genuinely contested in current literature.
- Human supplies: Nothing — fully synthetic from philosophical literature. Human should verify 2-3 paper dates against Google Scholar.
- Output medium: Manim (animated timeline: JTB box on left, Gettier 1963 event marker with "3 pages" annotation, four branching response nodes appearing to the right with author labels and years, one dashed "still open" node at the end)
- The change: Ask Claude to generate a new Gettier-style counterexample to one of the four responses — showing the fix is itself broken.
- Teardown angle: The Gettier problem is not a technical footnote. It reveals that having all the right ingredients — true belief, good justification — can still leave you short of knowledge when luck is involved. That gap is what every epistemologist since 1963 has been trying to close.
- Exclusions: Debates about AI knowledge, consciousness, or non-human cognition — those are a different chapter.
- Score: 9/10

---

## Candidate 02 — Research Logical Fallacies: Build a Sourced Taxonomy of the 12 Most Common
- Source: philosophy/chapters/05-logic-and-reasoning.md
- Lane: RESEARCH (Claude assistant)
- Hook: Everyone says "that's a logical fallacy" — but most people can only name two or three, and they often misidentify them. Claude builds a sourced 12-fallacy taxonomy from the philosophical literature, not from internet lists.
- The artifact: a sourced table: 12 fallacies × 4 columns (name, structure, worked example, philosophical source). Manim animates each fallacy as a card flipping over, front showing the name, back showing the structure and example.
- Prompt seed: `claude "Research 12 of the most important logical fallacies from the philosophical logic literature. For each: (1) the standard name and Latin name if applicable, (2) the formal structure (what makes it a fallacy — what the argument claims vs. what the premises actually support), (3) one concrete worked example NOT from politics, (4) the classical or modern philosophical source where it is discussed (author + work). Include: ad hominem, straw man, modus ponens vs. affirming the consequent, post hoc ergo propter hoc, false dichotomy, slippery slope, appeal to authority, circular reasoning, hasty generalization, tu quoque, equivocation, red herring. Flag any source you cannot verify."`
- Read / check: Verify that modus ponens is correctly not classified as a fallacy — it's the valid form, and affirming the consequent is the fallacy. Confirm Latin names are correct. Check at least 3 sources (Aristotle's Sophistical Refutations for classical ones, Hamblin's Fallacies 1970 for modern taxonomy).
- Human supplies: Nothing — fully synthetic from logic literature.
- Output medium: Manim (12 animated card-flips: front shows fallacy name in large type, back reveals structure and example; cards arranged in a 4×3 grid that assembles over the beat)
- The change: Ask Claude to classify a real argumentative text (a public debate excerpt or historical speech) by which of the 12 fallacies appear — showing the taxonomy as a working tool.
- Teardown angle: Fallacy names are diagnostic tools. The value is not the Latin — it's the structural pattern that makes the argument invalid. Every fallacy is a specific mismatch between what the premises establish and what the conclusion claims.
- Exclusions: Political debates, partisan examples, any living-person examples.
- Score: 8/10

---

## Candidate 03 — Research the Trolley Problem's Actual History: What Philosophers Built After Foot
- Source: philosophy/chapters/09-normative-moral-theory.md
- Lane: RESEARCH (Claude assistant)
- Hook: Everyone knows "trolley problem." Almost nobody knows that Foot's original 1967 paper was about abortion doctrine, that Thomson's variation changed everything, or that the experimental results from Greene's neuroscience work upended both. Claude traces the full lineage.
- The artifact: a sourced chronological brief: (1) Foot 1967 — original context and the doctrine of double effect, (2) Thomson 1985 — the violinist case and the footbridge variant, (3) Greene et al. 2001 fMRI study — emotional vs. utilitarian processing, (4) current philosophical assessment of what the experiments actually show. Manim animates a four-station timeline with the key philosophical move at each station.
- Prompt seed: `claude "Research the intellectual history of the trolley problem in philosophy. Trace: (1) Philippa Foot's 1967 paper 'The Problem of Abortion and the Doctrine of Double Effect' — what the trolley scenario was originally designed to illuminate, (2) Judith Jarvis Thomson's 1985 paper 'The Trolley Problem' — the footbridge variant and why it splits utilitarian intuitions, (3) Joshua Greene et al.'s 2001 Science paper on the fMRI study — what they found and how they interpreted it, (4) the current philosophical objection to Greene's dual-process interpretation (cite a critic). Flag any claim you cannot verify."`
- Read / check: Verify Foot's paper year (1967, Philosophical Review) and the double-effect context. Confirm Thomson's footbridge variant is correctly described (pushing vs. pulling the lever). Verify Greene et al. 2001 is Science and describes emotional activation for personal harm cases. Find and cite a specific critic of Greene's interpretation (e.g., Mikhail, Huebner).
- Human supplies: Nothing — fully synthetic from philosophy literature.
- Output medium: Manim (four-station horizontal timeline: Foot 1967 → Thomson 1985 → Greene 2001 → Current debate; each station has an icon and key-move annotation; animated left to right)
- The change: Ask Claude to apply all three frameworks (Foot's DDE, Thomson's contractualism, Greene's dual-process) to a new dilemma — a self-driving car's trolley-equivalent — and show where they agree and disagree.
- Teardown angle: The trolley problem was never about trolleys. It was always about the doctrine of double effect and what makes a death a side effect versus an end. The neuroscience work thought it was settling the debate; it opened a new one about what the intuition data actually measures.
- Exclusions: Internet pop-science trolley variants, political applications, any claims about what the "right" answer is.
- Score: 9/10

---

## Candidate 04 — Research Applied Ethics: What the Belmont Report Actually Changed
- Source: philosophy/chapters/10-applied-ethics.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Belmont Report (1979) is cited in every ethics course. Almost no one has read it, knows why it was written, or knows what happened to the men it was written because of.
- The artifact: a sourced 4-section brief: (1) Tuskegee — factual chronology with verified dates and harms, (2) the National Research Act 1974 — what it required and what commission it created, (3) the Belmont Report's four principles — respect for persons, beneficence, nonmaleficence, justice — each with one concrete implication for research consent, (4) one post-Belmont failure (e.g., Henrietta Lacks, Jesse Gelsinger) that shows what the Report did not fix. Manim animates a four-principle diagram with each principle connected to one concrete consent requirement.
- Prompt seed: `claude "Research the Belmont Report (1979) and its origins. Cover: (1) the Tuskegee Syphilis Study — dates, what was done, when it was exposed, what the settlement was; (2) the National Research Act 1974 — what it mandated; (3) the Belmont Report's four principles with one concrete research-consent implication each; (4) one documented post-Belmont research ethics failure that reveals a gap the Report did not close. Cite the Belmont Report itself and at least two secondary sources. Flag unverified claims."`
- Read / check: Verify Tuskegee start (1932), penicillin available (1947), exposure (1972), settlement ($10M). Confirm the Belmont Report was published in 1979 by the National Commission for the Protection of Human Subjects. Verify the post-Belmont case facts independently.
- Human supplies: Nothing — fully synthetic from public records and published literature.
- Output medium: Manim (four-node diagram: four principles as labeled circles, each with a connecting arrow to one concrete implication box; timeline above showing 1932→1947→1972→1974→1979)
- The change: Ask Claude to apply the four Belmont principles to a current AI ethics scenario (e.g., AI in clinical decision support) and identify which principle is most strained by the new technology.
- Teardown angle: The Belmont Report did not emerge from philosophy. It emerged from a government getting caught conducting 40 years of documented harm. Applied ethics begins in failure, not theory — and understanding the failure is what makes the principles legible.
- Exclusions: Any claims about ongoing litigation, any specific pharmaceutical company named in connection with the post-Belmont case without verified sourcing.
- Score: 8/10

---

## Candidate 05 — Research Kant vs. Mill: Three Cases Where They Disagree and One Where They Don't
- Source: philosophy/chapters/09-normative-moral-theory.md
- Lane: RESEARCH (Claude assistant)
- Hook: Kant and Mill are always presented as opposites. But they share more than introductory ethics courses admit — and the cases where they genuinely disagree reveal something specific about what each framework is actually tracking.
- The artifact: a sourced brief: (1) Kant's categorical imperative (two formulations, Groundwork 1785) vs. Mill's utility principle (Utilitarianism 1863) — stated precisely, not paraphrased; (2) three cases where the frameworks give opposite verdicts, with the reasoning from each side; (3) one case where they converge on the same verdict for different reasons; (4) one contemporary philosopher who argues they are more compatible than they appear (cite the paper). Manim animates a comparison grid: 3 cases × 2 frameworks, cells filling in with verdicts, one convergence case highlighted.
- Prompt seed: `claude "Research Kant's categorical imperative and Mill's utility principle. State both precisely (cite Groundwork 1785 and Utilitarianism 1863). Identify three moral cases where the two frameworks give opposite verdicts — describe the reasoning on each side. Identify one case where they converge on the same verdict for different reasons. Cite one contemporary philosopher who argues the two are more compatible than usually presented. Flag any claim you cannot verify."`
- Read / check: Verify Kant's two main formulations (universal law formula + humanity formula, Groundwork 4:421 and 4:429). Confirm Mill's harm principle is from On Liberty (1859), not Utilitarianism. Verify the contemporary compatibility argument — find the actual paper, not a secondhand summary.
- Human supplies: Nothing — fully synthetic from philosophical literature.
- Output medium: Manim (animated grid: 3 case rows × 2 framework columns, verdict cells animating in (green = permitted, red = forbidden), convergence case highlighted in a third color; frameworks labeled with author and year)
- The change: Ask Claude to apply both frameworks to a contemporary bioethics case (e.g., organ harvesting for utilitarian benefit) and show how the divergence maps onto the frameworks' fundamental commitments.
- Teardown angle: The difference between Kant and Mill is not "rules vs. consequences." It's a disagreement about what makes an action fundamentally right — the structure of the maxim, or the outcome for people. That's a real philosophical disagreement, and mapping it onto cases makes it concrete.
- Exclusions: Pop-ethics framings, political applications, the trolley problem (handled in Candidate 03).
- Score: 8/10

---

## Candidate 06 — Research the History of Logic: From Aristotle's Syllogisms to Frege's Notation
- Source: philosophy/chapters/05-logic-and-reasoning.md
- Lane: RESEARCH (Claude assistant)
- Hook: Frege published the Begriffsschrift in 1879 and nobody read it for 20 years. When they did, it broke philosophy open. Claude traces the 2,500-year arc from Aristotle to modern symbolic logic and explains what actually changed.
- The artifact: a sourced chronological brief: (1) Aristotle's syllogism — structure and four valid forms with examples; (2) the medieval period's contribution (Scholastic logic, Ockham); (3) Leibniz's vision of a calculus ratiocinator; (4) Boole's algebraic logic (1847); (5) Frege's Begriffsschrift (1879) — what was genuinely new; (6) Russell's Paradox (1901) and its impact on Frege. Manim animates a six-station historical arc.
- Prompt seed: `claude "Research the history of formal logic from Aristotle to Frege. Cover: (1) Aristotle's syllogistic — the four valid moods (Barbara, Celarent, Darii, Ferio) with one example each; (2) scholastic contributions in brief (one sentence, one name); (3) Leibniz's calculus ratiocinator concept; (4) Boole's algebraic logic (Mathematical Analysis of Logic, 1847); (5) Frege's Begriffsschrift (1879) — what notation it introduced that Aristotle's logic could not express; (6) Russell's Paradox (1901/1902) and Frege's response. Cite primary sources where possible."`
- Read / check: Verify the four syllogism moods (Barbara, Celarent, Darii, Ferio). Confirm Boole's 1847 publication title. Verify Frege's publication year (1879, not 1882). Confirm Russell's Paradox date and Frege's known response (preface to Vol. 2 of Grundgesetze).
- Human supplies: Nothing — fully synthetic from history of logic literature.
- Output medium: Manim (six-station horizontal timeline: Aristotle → Medieval → Leibniz → Boole → Frege → Russell; each station has a key contribution badge; timeline animates left to right with annotation text appearing at each station)
- The change: Ask Claude to explain what Frege's quantifier notation allowed that medieval syllogisms could not represent — specifically the difference between "all men are mortal" and "there exists a man who is mortal."
- Teardown angle: Logic is not a static inheritance from Aristotle. It went through a genuine revolution in the 19th century, driven by the needs of mathematics. The revolution produced the tools modern computer science runs on. The history makes the tools legible.
- Exclusions: Mathematical logic past Gödel (a separate chapter), modal logic, non-classical logics.
- Score: 7/10

---

## Candidate 07 — Research the Hard Problem of Consciousness: Chalmers vs. Dennett
- Source: philosophy/chapters/12-contemporary-philosophies-and-social-theories.md (anticipated scope from chapter list)
- Lane: RESEARCH (Claude assistant)
- Hook: Chalmers published "Facing Up to the Problem of Consciousness" in 1995 and the field split. Dennett has spent 30 years arguing the problem is an illusion. Neither side has budged. Claude maps the actual disagreement and what would settle it.
- The artifact: a sourced brief: (1) the hard problem stated precisely — Chalmers' 1995 formulation; (2) Dennett's heterophenomenology response — what he claims Chalmers is confusing; (3) one thought experiment from each side (Chalmers: philosophical zombie; Dennett: quining qualia); (4) what empirical finding, if any, could resolve the dispute — or why none can. Manim animates a two-column debate diagram: Chalmers moves on left, Dennett responses on right, arrows crossing between columns.
- Prompt seed: `claude "Research the debate between David Chalmers and Daniel Dennett on the hard problem of consciousness. Cover: (1) Chalmers' 1995 formulation of the hard problem (cite the Journal of Consciousness Studies paper); (2) Dennett's heterophenomenology — what he claims the hard problem conflates; (3) Chalmers' philosophical zombie argument and Dennett's quining qualia response, each stated precisely; (4) whether any empirical finding could in principle settle this dispute — if not, explain why. Flag any claim you cannot verify from the authors' own writings."`
- Read / check: Verify Chalmers' 1995 paper in Journal of Consciousness Studies. Verify Dennett's "Quining Qualia" (1988). Confirm the zombie argument is described correctly — it's a conceivability argument, not an empirical claim. Check that Dennett's heterophenomenology is correctly attributed (Consciousness Explained, 1991).
- Human supplies: Nothing — fully synthetic from published philosophy literature.
- Output medium: Manim (two-column animated debate: left column — Chalmers moves (hard problem, zombie argument); right column — Dennett responses (heterophenomenology, quining qualia); arrows cross between columns for each exchange)
- The change: Ask Claude to apply the Chalmers/Dennett debate to the question of AI consciousness — does a large language model have qualia? Show which framework makes the question answerable and which makes it unanswerable.
- Teardown angle: The hard problem is not about whether brains produce consciousness. It's about why physical processes give rise to subjective experience at all — why there is something it is like to see red, rather than nothing. Dennett says that question is confused. Chalmers says dismissing it is the confusion. The real dispute is about what counts as an explanation.
- Exclusions: Neuroscience debates, AI rights, any specific AI system claims.
- Score: 8/10

---

## Candidate 08 — Research Early Philosophy: What Thales Actually Said (and Why It Mattered)
- Source: philosophy/chapters/03-the-early-history-of-philosophy-around-the-world.md
- Lane: RESEARCH (Claude assistant)
- Hook: Thales of Miletus supposedly said "everything is water." This sounds ridiculous until you understand what he was replacing — and then it sounds like the birth of science.
- The artifact: a sourced brief: (1) what we actually know Thales said vs. what is secondhand; (2) Anaximander's correction (the apeiron) and why it's philosophically sharper; (3) Anaximenes' response (air); (4) what the Pre-Socratic project was — naturalistic explanation without myth — and how it differs from Hesiod; (5) one scholar who argues the Pre-Socratics are continuous with, not a break from, earlier mythological thinking. Manim animates a three-philosopher comparison timeline.
- Prompt seed: `claude "Research the Pre-Socratic philosophers: Thales, Anaximander, and Anaximenes. Cover: (1) what we can verify Thales actually said vs. what is Aristotle's secondhand report (cite Aristotle's Metaphysics); (2) Anaximander's apeiron concept and why it is philosophically more sophisticated than Thales' water; (3) Anaximenes' air principle; (4) what the Pre-Socratic project shared — naturalistic explanation without divine agency; (5) one scholar who argues the Pre-Socratics did not make as clean a break from myth as usually claimed. Cite primary sources and one secondary scholar."`
- Read / check: Verify Aristotle's Metaphysics 983b6 as the source for Thales' "water" claim. Confirm Anaximander's apeiron is correctly described as "the indefinite" or "the boundless." Verify the scholar who argues for continuity with myth (e.g., Gregory Vlastos or a more recent scholar).
- Human supplies: Nothing — fully synthetic from history of philosophy.
- Output medium: Manim (three-philosopher timeline: Thales → Anaximander → Anaximenes, each with their principle labeled, and a "replacing myth with" annotation showing what each replaced — cosmogonic myth with naturalistic principle)
- The change: Ask Claude to compare the Pre-Socratic project with a modern scientific analogy — what does the move from myth to naturalistic explanation look like in a contemporary case?
- Teardown angle: Thales is not interesting because he was right about water. He is interesting because he stopped asking "which god made it?" and started asking "what is it made of?" That question — not the answer — is the philosophical revolution.
- Exclusions: Socrates, Plato, Aristotle (they get other chapters), Eastern philosophy parallels (Confucius, Buddhism — a separate chapter).
- Score: 7/10

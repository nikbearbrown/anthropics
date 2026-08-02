# Biology: Genetics and Evolution — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build a Hardy-Weinberg Five-Forces Population Simulator with Claude
- Source: biology-genetics-and-evolution/chapters/10-population-genetics.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: A dinner-party question in 1908 exposes the null model for all of evolution — yet most students cannot tell whether a real population is drifting, selected, or both. A live sim makes the invisible math visible.
- The artifact: An animated D3/Manim line-plot of allele-frequency trajectories across generations — multiple semi-transparent replicate lines plus a solid deterministic expectation; three preset presets (pure drift Ne=50, directional selection, sickle-cell balanced polymorphism); a convergence-to-q* bar annotated with the equilibrium formula.
- Prompt seed: `claude "Build a population genetics simulator in a single HTML file with D3 v7. Controls: p0 slider, Ne log-slider (10–100k), sAA/sAa/sSS sliders, mutation rate, gene-flow rate, generation count (50–500), replicate count (1–20). Primary panel: allele frequency vs generation, semi-transparent replicates, solid deterministic line, dashed equilibrium q*=sAA/(sAA+sSS). Secondary panel: observed vs HWE genotype frequencies as grouped bars. Force-balance gauge. Three presets. Verify on console: sickle-cell preset → mean q after 500 gen within 0.02 of 0.111; pure-drift preset → >30% replicates fixed by gen 200 at Ne=50."`
- Read / check: Confirm that the sickle-cell preset converges from any starting p0; that pure-drift replicates do wander and fix; that the HWE secondary panel matches p^2, 2pq, q^2 on a large-population run; watch the force-balance gauge switch labels as sliders change.
- Human supplies: Nothing — fully synthetic. Illustrative stand-in for sickle-cell selection coefficients is acceptable (sAA≈0.10, sSS≈0.80 are the textbook values). The African-American HbS frequency data point (~0.04) is a public literature value.
- Output medium: Manim (animated allele-frequency trajectory curves drawing in real time) or screen-recording mp4 of the interactive D3 simulation.
- The change: Add a "malaria eradicated" phase button (toggle sAA → 0 mid-run) and overlay the predicted decline trajectory; annotate where the African-American frequency observation sits on the same chart.
- Teardown angle: The math says drift and selection are one parameter ratio (Ne × s). Below 1 drift wins; above 1 selection wins. That threshold predicts why antibiotic resistance rises fast (10^9 cells) while human traits change slowly (Ne≈10k).
- Exclusions: Full simulation of gene flow migration lattice; individual-based simulation; phylogenetic drift; LD / haplotype blocks.
- Score: 10/10

---

## Candidate 02 — Simulate Genetic Drift and Bottleneck Effects with Claude Code
- Source: biology-genetics-and-evolution/chapters/10-population-genetics.md + chapters/11-speciation.md
- Lane: BUILD (Claude Code)
- Hook: The cheetah is nearly a clone of itself — not because it was designed that way, but because chance wiped out its variation in one catastrophic event 10,000 years ago. You can simulate that catastrophe in 30 lines.
- The artifact: A Manim animation showing 20 replicate allele-frequency random-walk lines for a population that crashes from Ne=10,000 to Ne=5 for one generation then recovers — showing the "instant allele loss" event as a vertical collapse in variation, followed by slow drift at the recovered size. Heterozygosity decay curve alongside.
- Prompt seed: `claude "Write a Python script using Manim to animate genetic drift. Simulate 20 replicates of a diploid population. Phase 1 (gen 1–50): Ne=10000. Phase 2 (gen 51): Ne=5 (bottleneck). Phase 3 (gen 52–150): Ne=10000. Track p(A) each generation by sampling 2Ne alleles. Animate: x=generation, y=p(A), semi-transparent lines per replicate. Vertical dashed line at gen 51 labeled 'Bottleneck'. Compute expected heterozygosity 2pq each generation; add a thick lower curve for mean heterozygosity. Verify: mean p(A) stays near 0.5; heterozygosity drops sharply at bottleneck then partly recovers."`
- Read / check: Verify that mean p(A) across replicates stays near start (drift is symmetric); watch for alleles hitting 0 or 1 (fixation) after bottleneck; confirm heterozygosity curve collapses at gen 51.
- Human supplies: Nothing — fully synthetic. The cheetah-bottleneck data (~95% lower variation than typical mammals) is a published fact for the NEXT STEPS beat, not the sim itself.
- Output medium: Manim animated mp4 (lines drawing in over generations, heterozygosity curve tracing below).
- The change: Switch the bottleneck from Ne=5 to Ne=50, then Ne=500 — show on the same canvas that the variation loss scales with 1/Ne, making the "size of the hole" concrete.
- Teardown angle: A population's evolutionary future was mortgaged in one bad year. Conservation genetics is, at bottom, managing the Ne × t product before a single bad year makes it irreversible.
- Exclusions: Coalescent theory; structured populations; inbreeding coefficient F calculation; MHC diversity loss mechanics.
- Score: 9/10

---

## Candidate 03 — Build a Generalized Punnett Square and Stochastic Sampler with Claude
- Source: biology-genetics-and-evolution/chapters/00-how-to-use-the-simulations.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: A genetic counselor draws a 2×2 grid to give a 1-in-4 risk. At 7 loci the grid is 16,384 cells. The counselor has run out of napkin — Claude has not.
- The artifact: An interactive D3 HTML tool: slider N (1–7 loci), text inputs for two parent genotypes, colored Punnett grid (cell size auto-scales), readout of genotype ratio + phenotype ratio + theoretical expectation match badge; stochastic mode with sample-size slider (4–10,000) showing observed vs expected ratio bars.
- Prompt seed: `claude "Build 00-punnett-square.html. Single self-contained HTML, D3 v7. Parent genotype inputs (strings like AaBbCc), N slider 1–7. Enumerate 2^N gametes for each parent by independent assortment. Build 2^N × 2^N grid, shade cells: homozygous-dom all-loci #1a5276, homozygous-rec all-loci #85c1e9, heterozygous #2980b9. Readout: genotype counts, phenotype ratio under complete dominance, match badge. Stochastic mode: randomly sample n offspring from gamete pool, display observed vs theoretical bar chart. Verify on load: Aa×Aa→{AA:1,Aa:2,aa:1}; AaBb×AaBb→{A_B_:9,A_bb:3,aaB_:3,aabb:1}; AaBbCc×AaBbCc→27:9:9:9:3:3:3:1 PASS/FAIL lines."`
- Read / check: Check console PASS/FAIL for all three verification cases; drag N from 1 to 7 and watch cell-count go 4, 16, 64 … 16384; run stochastic mode at n=20 vs n=10000 and observe ratio convergence.
- Human supplies: Nothing — fully synthetic. The CFTR/cystic-fibrosis framing is a publicly known clinical fact used as a worked example in narration.
- Output medium: Screen-recording mp4 of the interactive D3 tool (slider dragging, grid resizing, stochastic sampling).
- The change: Add incomplete dominance at a selected locus (dropdown per locus), showing how the 3:1 phenotype ratio shifts to 1:2:1 — the pink-snapdragon extension.
- Teardown angle: The simulation is not the biology; it assumes independent assortment, complete dominance, no epistasis. Each assumption the textbook breaks in Ch 3 corresponds to one field you would add to the genotype-to-phenotype function — not a new grid, just a new rule.
- Exclusions: Linkage/crossover within the grid; triploid/polyploid crosses; imprinting; sex-linked crosses.
- Score: 9/10

---

## Candidate 04 — Simulate Natural Selection Modes and the Breeder's Equation with Claude
- Source: biology-genetics-and-evolution/chapters/09-evolution-origin-of-species.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: In one drought year on a tiny Galápagos island, two biologists watched evolution happen in a notebook. The breeder's equation predicted the shift to two decimal places. You can replicate the math in 20 lines.
- The artifact: A Manim animation of phenotype distribution (Gaussian curve) shifting under directional selection: pre-selection distribution (blue), selection threshold line, post-selection survivor distribution (orange), next-generation predicted mean marked by R=h²S. Three mode buttons (directional / stabilizing / disruptive) morph the selection fitness function overlay and animate the resulting distribution change.
- Prompt seed: `claude "Animate the breeder's equation in Manim. Scene 1: draw a Gaussian phenotype distribution (mean=9.4mm, sd=1.2mm) for Daphne Major beak depth. Draw a vertical selection threshold at 10.0mm. Shade the survivor region. Draw a new Gaussian for survivors (mean=10.0mm). Compute R = 0.7 × (10.0 - 9.4) = 0.42mm. Animate the next-generation distribution forming at mean 9.82mm. Annotate: S=0.6, h²=0.7, R=0.42, predicted_mean=9.82, observed_mean=9.7. Scene 2: switch to stabilizing selection — double-humped fitness curve, distribution narrowing without mean shift. Scene 3: disruptive selection — bimodal fitness, distribution splitting."`
- Read / check: Confirm R=h²×S = 0.42 annotated correctly; verify the three mode morphs look visually distinguishable; check that stabilizing leaves mean unchanged while reducing variance.
- Human supplies: Nothing — fully synthetic using textbook-published Daphne Major values (S=0.6mm, h²=0.7 from Grant lab data).
- Output medium: Manim mp4.
- The change: Add a "random mating vs assortative mating" toggle on the disruptive scene — show that assortative mating + disruptive selection can split the distribution into two peaks, previewing sympatric speciation.
- Teardown angle: The breeder's equation is the same math whether the population is finches, wheat, or antibiotic-resistant bacteria. The speed of evolution is not fixed — it scales with h² × S, both of which we can measure.
- Exclusions: Multivariate selection (G-matrix); kin selection; inclusive fitness; runaway sexual selection.
- Score: 9/10

---

## Candidate 05 — Investigate the Molecular Clock and dN/dS with Claude
- Source: biology-genetics-and-evolution/chapters/13-molecular-evolution-evo-devo.md
- Lane: RESEARCH (Claude assistant)
- Hook: Kimura's neutral theory fits on an index card — 2Ne × μ × 1/(2Ne) = μ — and it predicts that the molecular clock runs at the mutation rate, not the selection rate. Test the prediction against real cytochrome-c data.
- The artifact: A sourced synthesis document: a 2-column comparison table (species vs human cytochrome-c amino acid differences vs predicted divergence time from the molecular clock), a dN/dS ratio explanation for 3 real genes (one highly constrained, one under positive selection, one neutrally evolving), and a curated annotated list of 4–6 primary sources.
- Prompt seed: `claude "Research the molecular clock hypothesis using cytochrome-c as the worked example. (1) Compile a table of human vs. chimp (0), rhesus (1), dog (11), tuna (21), bread mold (41) cytochrome-c amino acid differences and the corresponding molecular clock divergence time estimates from the fossil-calibrated clock. (2) Explain dN/dS: what values indicate purifying, neutral, and positive selection? Give one real gene example for each category with a citable source. (3) Explain why neutral theory says the molecular clock rate equals the mutation rate and is independent of Ne. (4) Identify one key limitation of the strict molecular clock. Cite at least 4 primary or review sources."`
- Read / check: Verify the cytochrome-c numbers against the textbook values; confirm dN/dS < 1, = 1, > 1 are correctly attributed; check that at least one source is a peer-reviewed paper (not a textbook).
- Human supplies: Nothing — fully synthetic. All data are published values available in the primary literature and reviewed textbooks.
- Output medium: Slate (formatted synthesis document displayed as cards in the video; human fills with any figures from cited papers, or Claude generates a schematic divergence tree as a slate placeholder).
- The change: Extend the query to ask whether the molecular clock runs at the same rate in viruses (HIV) vs mammals — show that in fast-evolving RNA viruses, the clock is generation-time-dependent, not calendar-time.
- Teardown angle: The molecular clock revealed whale-artiodactyl kinship, Neanderthal ancestry, and HIV pandemic origins. Its power is that sequence divergence encodes time — but the clock ticks differently in different lineages, so calibration is always required.
- Exclusions: Full coalescent analysis; phylogenetic software tutorials; deep Archean fossil calibration debates.
- Score: 8/10

---

## Candidate 06 — Build a Meiosis and Linkage Simulator with Claude
- Source: biology-genetics-and-evolution/chapters/01-meiosis-basis-of-inheritance.md (LLM Exercise)
- Lane: BUILD (Claude Code)
- Hook: Sturtevant built the first chromosome map on his bedroom floor in 1913 using one idea: recombination frequency is a ruler. You can animate the ruler.
- The artifact: An interactive D3 simulation: Panel 1 shows a bivalent with two loci A/a and B/b; three modes (different chromosomes, perfect linkage, r-slider); a bar chart of four gamete frequencies; a PASS/FAIL console for boundary conditions. Panel 2: X-linked pedigree generator with hemophilia A / color blindness / DMD.
- Prompt seed: `claude "Build 01-meiosis-mendel.html with D3 v7. Panel 1: bivalent animation for A/a and B/b. Mode a) different chromosomes: 4 gametes at 0.25 each. Mode b) same chromosome, no crossing over: AB and ab at 0.5 each. Mode c) recombination r slider 0–0.5: AB at (1-r)/2, ab at (1-r)/2, Ab at r/2, aB at r/2. Animate the bivalent, show crossover event at r fraction of meioses. Bar chart of 4 gametes. Verify: mode a → {AB:0.25,Ab:0.25,aB:0.25,ab:0.25}; mode b → {AB:0.5,ab:0.5,Ab:0,aB:0}; mode c r=0.20 → {AB:0.40,Ab:0.10,aB:0.10,ab:0.40}. Panel 2: X-linked pedigree generator for hemophilia A, color blindness, DMD; user selects mother and father genotypes; generate up to 12 children; verify no father-to-son transmission."`
- Read / check: Step r from 0 to 0.5 and verify gamete bars converge to equal at r=0.5; confirm at r=0 only parental types appear; in Panel 2 verify affected father × non-carrier mother → all daughters carriers, no sons affected.
- Human supplies: Nothing — fully synthetic. Disease gene locations and clinical incidence figures are published facts used as narrative anchors.
- Output medium: Screen-recording mp4 of the interactive D3 tool.
- The change: Add a "three-gene mapping" mode where three loci A, B, C have pairwise r values rAB, rBC, rAC — show that if rAC ≈ rAB + rBC the loci are in linear order, replicating Sturtevant's 1913 argument.
- Teardown angle: Recombination frequency is not just a probability; it is a physical distance in centimorgans. The mapping move — from frequency to distance to order — is the first example of a computational measurement revealing a physical truth invisible to the microscope.
- Exclusions: Crossover interference; gene conversion; double crossovers beyond the three-point mapping extension.
- Score: 8/10

---

## Candidate 07 — Research the Stickleback Regulatory Evolution Case with Claude
- Source: biology-genetics-and-evolution/chapters/13-molecular-evolution-evo-devo.md
- Lane: RESEARCH (Claude assistant)
- Hook: In 16 freshwater lakes on three continents, the same gene lost its spine-building enhancer — but never twice at the same base. Convergent evolution at one regulatory address is the sharpest proof that evo-devo found.
- The artifact: A sourced synthesis: a timeline of the stickleback Pitx1 discovery (Kingsley lab 2004–2010), a 3-column comparison table of three freshwater populations showing the specific enhancer deletion, a comparison of Pitx1 protein vs. Pitx1 pelvic enhancer conservation, and an annotated bibliography of 4 primary sources.
- Prompt seed: `claude "Research the three-spined stickleback Pitx1 pelvic spine case as evidence for regulatory evolution. (1) Summarize the Kingsley lab findings: what mutation causes pelvic spine loss, why is it the enhancer and not the protein coding sequence, and what evidence supports independent evolution in different lakes? (2) Build a 3-column table: Lake (name/location), Specific deletion (approximate size/position if published), Protein coding sequence (changed or unchanged). (3) Explain why enhancer modularity prevents pleiotropic side effects. (4) Connect this to the concept of conserved toolkit genes (Pitx1 in mouse hindlimb, pituitary, jaw). Cite at least 4 primary sources including at least one Shapiro/Kingsley paper."`
- Read / check: Verify that the protein coding region is described as unchanged; confirm that at least two lakes' deletions are at different specific positions; cross-check that Pitx1 expression in jaw/pituitary is stated to be unaffected.
- Human supplies: Nothing — fully synthetic from published primary literature.
- Output medium: Slate (3-column table displayed as an animated reveal; stickleback morphology comparison slate for the human to fill with published figures).
- The change: Extend the query to compare the stickleback case with another parallel regulatory evolution case (e.g., the repeated loss of armor plates via Eda gene enhancer in the same species) — show that regulatory evolution at shared elements is a general pattern, not a lucky accident.
- Teardown angle: The lesson is not that regulatory mutations are "safer." It is that the genome's modular architecture makes certain evolutionary moves repeatable: the same address gets hit by different mutations because it is the only address where the required change can happen without wrecking everything else.
- Exclusions: Full QTL mapping methodology; evo-devo of other organisms; deep homology of Hox genes beyond what is needed to motivate the Pitx1 story.
- Score: 8/10

---

## Candidate 08 — Simulate Mutation-Selection Balance with Claude Code
- Source: biology-genetics-and-evolution/chapters/10-population-genetics.md
- Lane: BUILD (Claude Code)
- Hook: A rare recessive disease is not going away — mutation creates it every generation at exactly the rate selection removes it. That steady state is a number, and you can watch it form.
- The artifact: A Manim animation: two panels. Left: q (allele frequency) vs generation for a deleterious recessive under selection-only (q declining to 0) vs mutation-selection balance (q leveling off at q* = √(μ/s)), with both curves on the same axes. Right: a bar chart of q* as a function of μ/s ratio, showing how disease frequency scales with the mutation-selection balance equation.
- Prompt seed: `claude "Animate mutation-selection balance in Manim. Scene 1: two allele-frequency trajectories over 1000 generations. Trajectory 1 (no mutation): starts at q=0.10, s=0.5 on aa genotype, no mutation → q declines to near zero following q'=q(1-sq^2×p)/(1-sq^2). Trajectory 2 (with mutation μ=1e-5, s=0.5): q starts at 0.10, declines, then stabilizes near q*=sqrt(μ/s)=sqrt(2e-5)≈0.0045. Annotate q* on the plot. Scene 2: bar chart of q* for five μ/s ratios showing how disease incidence q*^2 scales. Verify: q* matches sqrt(μ/s) formula within 5% after 1000 generations."`
- Read / check: Confirm q* in the simulation matches the analytic formula; verify the two curves separate clearly (with-mutation reaches a plateau, without-mutation falls to near zero); check that q*^2 disease incidence is annotated correctly.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim mp4.
- The change: Replace the constant-selection model with a heterozygote-advantage (overdominance) model (HbS) and show that q* now becomes a stable attractor instead of a floor — draw the phase diagram showing q returning to q* from both sides.
- Teardown angle: Mutation-selection balance is why eliminating carriers does not eliminate recessive disease. The math shows that with 200 carriers per affected patient, selection on homozygotes barely moves the gene-pool needle per generation.
- Exclusions: Exact stochastic simulation of small populations; joint mutation-drift-selection dynamics; Fisher information approaches to estimating s from frequency data.
- Score: 8/10

---

## Candidate 09 — Research Speciation Mechanisms in Lake Victoria Cichlids with Claude
- Source: biology-genetics-and-evolution/chapters/11-speciation.md
- Lane: RESEARCH (Claude assistant)
- Hook: Lake Victoria is younger than the oldest pyramid at Giza — yet it holds 500 cichlid species. Turbidity from farm runoff is fusing two of them back into one in real time. Speciation has an off switch.
- The artifact: A sourced synthesis: a timeline of cichlid radiation (lake refill ~14,600 ya → ~500 species), a 2-column comparison of Pundamilia pundamilia vs. P. nyererei (opsin tuning, male color, female preference, habitat depth), a paragraph on turbidity-driven hybridization with 2 citable sources, and a classification of all reproductive isolating barriers present in this system.
- Prompt seed: `claude "Research sympatric speciation and sensory drive in Lake Victoria Pundamilia cichlids. (1) Summarize the timeline: when did the lake refill, how many species exist, why is this radiation remarkable compared to Galápagos finches or Hawaiian honeycreepers? (2) Compare Pundamilia pundamilia and P. nyererei: habitat depth, male coloration, female opsin tuning, female mate preference — build a 2-column table. (3) Explain turbidity-driven collapse: what happens when water clarity is lost, what evidence shows hybrids appear? (4) List and classify all reproductive isolating barriers in this system (prezygotic / postzygotic). Cite at least 4 primary sources."`
- Read / check: Verify the lake age (~14,600 years) is correct; confirm the opsin-tuning mechanism (longer vs shorter wavelength sensitivity) is accurately described; check that both prezygotic (sensory/behavioral) and postzygotic barriers are at least mentioned.
- Human supplies: Nothing — fully synthetic from published primary literature. A map of Lake Victoria with depth gradient is a desirable slate image (human fills from published figures).
- Output medium: Slate (2-column table animated reveal; map slate for human to fill).
- The change: Extend the query to ask whether a similar turbidity-speciation reversal has been documented in other cichlid lakes (e.g., Lake Kyoga) — show that the pattern is general, not a Lake Victoria anomaly.
- Teardown angle: Speciation is not permanent. A reproductive barrier built on sensory discrimination can be erased by an environmental change that scrambles the signal. Conservation of speciation requires conserving the physical conditions that the barrier depends on.
- Exclusions: Full phylogenetic analysis of cichlid clades; haplochromine vs. non-haplochromine diversification; genomics of cichlid adaptive radiation beyond what motivates the sensory-drive story.
- Score: 8/10

---

## Candidate 10 — Build a Phylogenetic Tree from Cytochrome-c Sequences with Claude Code
- Source: biology-genetics-and-evolution/chapters/12-phylogenetics-history-of-life.md
- Lane: BUILD (Claude Code)
- Hook: Woese discovered a third domain of life by building a tree from one molecule. You can build a primate tree with the same logic in 25 lines of Python.
- The artifact: A Manim (or screen-recording) animation: a neighbor-joining primate phylogeny built from a pairwise amino-acid-difference matrix (human/chimp 0, rhesus 1, dog 11, tuna 21, bread mold 41 vs human cytochrome-c), drawn as an animated branching tree with branch lengths proportional to divergence; monophyletic clade boxes highlight Primates and Mammals.
- Prompt seed: `claude "Build a Python script that constructs a neighbor-joining phylogenetic tree from a pairwise distance matrix using scipy or biopython. Distance matrix: human-chimp 0, human-rhesus 1, human-dog 11, human-chicken 13, human-tuna 21, human-bread_mold 41. Use UPGMA or NJ. Output: a Newick string and a Manim animation of the tree with animated branch-drawing. Annotate: Primates clade box, Vertebrates clade box. Verify: chimp is sister to human with smallest branch length; bread mold is the outgroup."`
- Read / check: Verify chimp is sister to human; verify the tree topology is consistent with published vertebrate phylogeny; check that branch lengths are monotonically ordered (chimp < rhesus < dog < tuna < bread mold from human).
- Human supplies: Nothing — fully synthetic using published amino-acid difference counts.
- Output medium: Manim mp4 (animated branching tree drawing in).
- The change: Add a second distance matrix from a hypothetical randomly shuffled dataset and show the tree looks wrong — teaching that the tree is only as valid as the alignment, and a sanity check (human-chimp must be closest) is always needed.
- Teardown angle: A phylogenetic tree is a hypothesis, not a fact. Every branch is a claim about who shared a common ancestor most recently, and every claim is falsifiable by adding more data. Woese's three-domain tree overturned a century of textbooks. The right algorithm on better data will do it again somewhere.
- Exclusions: Maximum likelihood vs parsimony vs Bayesian debates; bootstrap support; substitution models; actual 16S rRNA sequence alignment.
- Score: 7/10

---

## Candidate 11 — Investigate the Fisher-Mendel Controversy with Claude
- Source: biology-genetics-and-evolution/chapters/02-mendels-laws-mendelian-inheritance.md
- Lane: RESEARCH (Claude assistant)
- Hook: R.A. Fisher looked at Mendel's published numbers in 1936 and computed a p-value of 0.00004 — the data fit the model too well to be honest. One of history's great discoveries may have a data-quality problem baked into the founding document.
- The artifact: A sourced synthesis: the Fisher (1936) chi-square finding summarized in plain language, three proposed explanations (unconscious classification bias, selective reporting, harmonic analysis), the current scientific consensus (inconclusive but real anomaly), and a 2-row table of Mendel's published F2 counts vs expected for the seed-shape cross.
- Prompt seed: `claude "Research the Fisher-Mendel controversy. (1) Summarize Fisher's 1936 finding: what chi-square did he compute, what p-value does it correspond to, and what does it mean in plain language? (2) List the three main explanations proposed by historians and statisticians. (3) What is the current scientific consensus — is there agreement? (4) Build a 2-row table for Mendel's seed-shape cross: observed (5474 round, 1850 wrinkled) vs expected under 3:1, chi-square value, conclusion at p=0.05. (5) Does the Fisher controversy undermine Mendel's three laws? Cite at least 3 sources including Fisher 1936 and at least one recent analysis."`
- Read / check: Verify the chi-square for the seed-shape cross is computed correctly (observed 7324, expected 5493/1831, chi-sq should be very small — that is the point); confirm Fisher's aggregate p ≈ 0.00004 is correctly described; verify conclusion does not conflate the laws (correct) with the data quality (questionable).
- Human supplies: Nothing — fully synthetic.
- Output medium: Slate (2-row table animated reveal; timeline of controversy as a slate the human fills or Claude renders as text cards).
- The change: Run the same chi-square analysis on a synthetic "honest" dataset of 7,324 random Bernoulli(3/4) draws — show the distribution of chi-square statistics — and mark where Mendel's actual number falls in that distribution.
- Teardown angle: Science's self-correcting mechanism works at the level of laws, not individual datasets. The 3:1 ratio has been confirmed in thousands of independent experiments. The question of how Mendel got there is a historical-statistical question that does not unseat the laws — but it is a reminder that experimenters are not immune to their own expectations.
- Exclusions: Full ANOVA of all seven traits; Weldon's reanalysis; Bayesian reanalysis papers beyond what is needed to set the consensus.
- Score: 7/10

---

## Candidate 12 — Research CRISPR-Cas9 and the Casgevy Approval with Claude
- Source: biology-genetics-and-evolution/chapters/07-biotechnology-genomics.md
- Lane: RESEARCH (Claude assistant)
- Hook: Victoria Gray received the first CRISPR medicine in 2019 and has not had a single sickle-cell pain crisis since. Understanding why requires tracing four borrowed bacterial tools across 70 years of biochemistry.
- The artifact: A sourced synthesis: a 4-row table of the Copy/Cut/Read/Write verbs with the molecular tool, the organism it was borrowed from, the year, and the clinical application; a paragraph on how BCL11A enhancer editing de-represses fetal hemoglobin (mechanistic, not anecdotal); a timeline from 1953 to 2023; and a list of 4 primary sources.
- Prompt seed: `claude "Research the molecular tools behind Casgevy, the first CRISPR-based medicine (FDA-approved December 2023 for sickle cell disease). (1) Build a 4-row table: tool name, source organism, year discovered, current clinical application. Rows: PCR/Taq polymerase; Restriction enzymes; CRISPR-Cas9; Base editors. (2) Explain mechanistically why editing the BCL11A erythroid enhancer (not the HBB sickle mutation itself) re-activates fetal hemoglobin. (3) Build a timeline: Watson-Crick 1953 → Taq 1988 → CRISPR 2012 → Casgevy 2023. Cite at least 4 sources including the original Casgevy clinical trial paper and the 2012 Jinek et al. CRISPR paper."`
- Read / check: Verify the BCL11A mechanism (enhancer deletion → BCL11A not expressed in red-cell precursors → HbF not repressed → fetal hemoglobin rises); confirm Taq source organism (Thermus aquaticus, Yellowstone); check that the 2023 FDA approval date is correct.
- Human supplies: Nothing — fully synthetic. A photo of Victoria Gray is optional (human supplies if desired for the human-interest beat).
- Output medium: Slate (4-row table animated reveal; timeline slate).
- The change: Extend the query to contrast Casgevy (enhancer editing, changes gene regulation) with a hypothetical direct HBB correction (base editing of the sickle mutation) — explain why the regulatory approach was chosen first.
- Teardown angle: The four verbs (Copy, Cut, Read, Write) are a complete toolkit borrowed from organisms that faced similar information-management problems. Every advance in molecular medicine since 1953 is a composition of these four primitives in different orders.
- Exclusions: mRNA vaccine synthesis pathway; gene therapy vectors beyond CRISPR; all CRISPR delivery methods beyond electroporation.
- Score: 7/10

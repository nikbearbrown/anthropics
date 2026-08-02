# Contemporary Mathematics — CLI Video Ideas ("X with Claude")

## Candidate 01 — Simulate the Königsberg Bridge Problem with Claude

- Source: math-contemporary-mathematics/chapters/12-graph-theory.md
- Lane: BUILD (Claude Code)
- Hook: Euler proved the seven-bridge walk was impossible in 1736 — by throwing away the map and asking one question about dots: how many lines meet at each? Claude builds the graph, checks the degree sequence, and animates the proof.
- The artifact: a Python/networkx script that: (1) builds the Königsberg graph (4 vertices, 7 edges with correct degree sequence [3,3,3,5]), (2) checks the Euler circuit condition (all even degrees), (3) animates the graph with vertex degrees labeled, highlighting the odd-degree vertices in red. A second animation tries all routes and shows each getting stuck — demonstrating impossibility.
- Prompt seed: `claude "Using networkx and matplotlib, build the Königsberg bridge graph: 4 nodes (North, South, Island1, Island2) with 7 edges matching the historical bridge layout. Compute each node's degree. Animate the graph: draw all nodes and edges, label each node with its degree, highlight odd-degree nodes in red. Title: 'Königsberg Bridges: Why the Walk is Impossible'. Print whether an Euler circuit is possible. Save as mp4."`
- Read / check: Verify degrees are [3, 3, 3, 5] (all odd, so no Euler circuit). Confirm networkx's euler_circuit detection matches the odd-degree rule. Check the animation clearly shows all 4 odd-degree vertices. Verify the bridge graph matches the historical layout.
- Human supplies: Nothing — fully synthetic. The historical graph is well-documented.
- Output medium: screen-recording mp4 (animated graph with degree labels)
- The change: Modify one edge to give two even-degree vertices and show an Euler circuit is now possible — demonstrating that the exact bridge configuration determines the answer.
- Teardown angle: Euler's key move was abstraction — throwing away every geographic detail and keeping only connection. The degree sequence (a purely combinatorial property) determines the traversability of any graph. This is why graph theory works.
- Exclusions: Hamiltonian circuits; traveling salesman problem; planar graph theory.
- Score: 9/10

---

## Candidate 02 — Simulate Casino Edge on Roulette with Claude

- Source: math-contemporary-mathematics/chapters/07-probability.md
- Lane: BUILD (Claude Code)
- Hook: Roulette is a "fair" game with a 1/38 hidden tax. Over 10,000 spins, the house edge is mathematically guaranteed to extract money. Claude simulates it and watches the player's bankroll drain — even with lucky streaks.
- The artifact: a Python simulation of 10,000 roulette spins (betting $1 on red each spin, p_win = 18/38). Animate the player's bankroll over time: starting at $1000, showing the running total fluctuating but trending downward. Mark the expected loss line (-2/38 × n × $1). Overlay 5 random trajectories.
- Prompt seed: `claude "Simulate 10,000 roulette spins: each spin, player bets $1 on red (wins $1 with prob 18/38, loses $1 with prob 20/38). Start with $1000. Run 5 independent simulations. Animate all 5 bankroll trajectories simultaneously. Overlay the expected value line: 1000 - (2/38)*n. Mark where bankrupt first occurs if applicable. Save as mp4."`
- Read / check: Verify expected loss per spin = 2/38 ≈ $0.0526. After 1000 spins, expected bankroll ≈ $947.37. Confirm the expected value line has correct slope. Check all 5 trajectories fluctuate around the same trend. Verify at least one trajectory goes below $0 if starting with small bankroll.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (multi-trajectory animated bankroll)
- The change: Run the same simulation for blackjack (house edge ~0.5%) vs. roulette (~5.26%) side by side — showing that game choice matters more than strategy at any reasonable bankroll.
- Teardown angle: Expected value is not what happens — it's what happens on average. Individual trajectories are noisy but the ensemble reveals the invisible tax. The casino doesn't need to cheat because probability is the mechanism.
- Exclusions: Card counting; Kelly criterion; gambling addiction.
- Score: 9/10

---

## Candidate 03 — Build a Voting Method Comparator with Claude

- Source: math-contemporary-mathematics/chapters/11-voting-and-apportionment.md
- Lane: BUILD (Claude Code)
- Hook: Four candidates, three voting methods (plurality, Borda count, instant runoff) — three different winners from the same ballots. Claude runs all three on the same preference data and shows the disagreement.
- The artifact: a Python script that takes a preference schedule (e.g., 5 voters, 3 candidates), implements plurality, Borda count, and instant runoff voting, runs all three, and displays a comparison table + animated bar chart showing each method's winner and their vote counts.
- Prompt seed: `claude "Implement three voting methods in Python: Plurality (most first-place votes wins), Borda Count (n-1, n-2, ..., 0 points for each rank position), and Instant Runoff (eliminate lowest first-place votes, redistribute). Run all three on this preference schedule: [A>B>C, A>C>B, B>A>C, C>B>A, C>A>B] with vote counts [3,2,2,1,1]. Print each method's winner. Animate a bar chart showing the tally for each method side by side. Save as mp4."`
- Read / check: Verify each method's computation. Check plurality winner (most 1st place votes), Borda count (summed weighted scores), IRV (elimination rounds). Confirm the three methods may give different winners for the given schedule. Verify bar chart shows all three methods' tallies simultaneously.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (animated comparison bar chart)
- The change: Apply Arrow's Impossibility Theorem framing — show a preference schedule where any method violates at least one fairness criterion (e.g., majority criterion, Condorcet criterion).
- Teardown angle: There is no perfect voting method — Arrow's theorem proves it mathematically. The choice of method is a value judgment about which fairness criterion matters most. This is applied mathematics directly shaping democracy.
- Exclusions: Electoral college; runoff elections; gerrymandering.
- Score: 9/10

---

## Candidate 04 — Model Compound Interest for Money Management with Claude

- Source: math-contemporary-mathematics/chapters/06-money-management.md
- Lane: BUILD (Claude Code)
- Hook: A $200/month contribution at 7% annual return grows to $525,000 in 40 years — but $96,000 of that is contributions and $429,000 is interest. Claude builds the calculator and animates the contribution vs. interest split growing over time.
- The artifact: a Python script computing monthly compounding A = PMT × [(1+r/12)^(12n) - 1]/(r/12) for n = 0 to 40 years. Animate a stacked area chart: bottom layer = cumulative contributions (200×12×n), top layer = interest earned. Mark key milestones (10yr, 20yr, 30yr, 40yr).
- Prompt seed: `claude "Compute month-by-month compound growth for monthly contributions of $200 at 7% annual rate (monthly compounding) over 40 years. For each month: track total contributions and total interest earned. Create a matplotlib stacked area chart animated over 40 years showing contributions (blue) and interest (orange) stacking up. Mark 10, 20, 30, 40 year milestones. Save as mp4."`
- Read / check: Verify final balance ≈ $524,000, contributions = $96,000, interest ≈ $428,000. Check monthly compound formula is implemented correctly. Confirm stacked areas sum to running total at each point. Verify milestone markers are accurately placed.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (animated stacked area chart)
- The change: Add a comparison: what if contributions started 10 years later? Show the cost of delay — the 30-year vs. 40-year starting point comparison.
- Teardown angle: The interest component eventually dwarfs the contributions — this is the "eighth wonder of the world" effect. But the power of compounding requires time; the cost of starting late is nonlinear.
- Exclusions: Tax-advantaged accounts; inflation adjustment; investment risk.
- Score: 8/10

---

## Candidate 05 — Animate Euler Paths and the Sum of Degrees Theorem with Claude

- Source: math-contemporary-mathematics/chapters/12-graph-theory.md
- Lane: BUILD (Claude Code)
- Hook: The sum of all vertex degrees always equals twice the number of edges — always — because each edge contributes to exactly two vertices. Claude proves this by construction and animates the counting.
- The artifact: a Manim or networkx animation that: (1) builds a random graph with 6 nodes and 9 edges, (2) highlights each edge in sequence and shows a counter ticking up by 2 each time (one for each endpoint), (3) compares the final sum to 2×9=18, (4) checks whether the number of odd-degree vertices is even (it must be).
- Prompt seed: `claude "Using networkx and matplotlib, create an animation: Build a connected graph with 6 nodes and 9 edges. Animate highlighting each edge one at a time. For each edge, show +1 added to each endpoint's running degree counter. When all edges are highlighted, display: sum of degrees = 2 * 9 = 18. Count and display odd-degree vertices. Save as mp4."`
- Read / check: Verify sum of degrees = 2×E for the chosen graph. Check the degree counter updates correctly for each edge. Confirm the odd-degree vertex count is even (a theorem consequence). Verify the animation is clear and not overcrowded.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (animated edge-highlighting with counters)
- The change: Show a graph with exactly 2 odd-degree vertices and find the Euler path between them — connecting the theorem to practical route planning.
- Teardown angle: The Sum of Degrees Theorem is a parity argument — it says something about the whole from a simple rule about each part. This type of reasoning (counting each contribution twice) appears throughout combinatorics and is the template for a wide class of elegant proofs.
- Exclusions: Four-color theorem; planar graphs; graph coloring algorithms.
- Score: 8/10

---

## Candidate 06 — Visualize Number System Relationships with Claude

- Source: math-contemporary-mathematics/chapters/03-real-number-systems-and-number-theory.md
- Lane: BUILD (Claude Code)
- Hook: Natural ⊂ Whole ⊂ Integer ⊂ Rational ⊂ Real — each set contains the previous, but with qualitatively new numbers added. Claude builds a nested Venn diagram with examples that pop in at each level.
- The artifact: a Manim animation building concentric ovals for Natural → Whole → Integer → Rational → Real, with each ring appearing in sequence. As each ring appears, example numbers pop in: 1,2,3 (natural); 0 (whole); -5 (integer); 1/3, -7/4 (rational); √2, π, e (irrational). Final frame shows all sets with examples.
- Prompt seed: `claude "Create a Manim animation building a nested set diagram for number systems: Natural ⊂ Whole ⊂ Integer ⊂ Rational ⊂ Real. Animate each set ring appearing from inside out. When each ring appears, animate example numbers popping in: Natural: [1,2,3]; Whole adds: [0]; Integer adds: [-1,-5]; Rational adds: [1/2, -3/4]; Irrational adds: [sqrt(2), pi, e]. Label each ring clearly. Final frame: complete diagram."`
- Read / check: Verify the set containment is correctly represented (nested, not overlapping). Check examples are correctly classified (√2 is irrational, not rational). Confirm labels are legible at each stage. Verify the animation timing allows viewing each set before the next appears.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated nested set diagram)
- The change: Add a sixth ring for Complex numbers (a+bi), showing that the reals are themselves a subset of a larger structure — and that the pattern of containment continues.
- Teardown angle: The real number system is not a single object — it's a nested hierarchy, each layer adding numbers that the previous layer couldn't reach. Understanding what each layer gains (zero, negatives, fractions, limits) clarifies why each extension was necessary.
- Exclusions: Set theory axioms; constructive proof of irrationality of √2; p-adic numbers.
- Score: 7/10

---

## Candidate 07 — Compute Permutations vs. Combinations: Menu Ordering with Claude

- Source: math-contemporary-mathematics/chapters/07-probability.md
- Lane: BUILD (Claude Code)
- Hook: 10 items, choose 5 for a tasting menu: 252 if order doesn't matter, 30,240 if it does. The ratio is 5! = 120. Claude computes both, visualizes the scaling, and explains why the ratio is always n!.
- The artifact: a Python script computing C(n,k) and P(n,k) for n=5 to 15, k=3. Animates two lines on a log-scale plot showing permutations growing much faster than combinations. Annotates that P(n,k)/C(n,k) = k! = 6 always for k=3.
- Prompt seed: `claude "Compute P(n,3) = n!/(n-3)! and C(n,3) = n!/(3!*(n-3)!) for n=3 to 20. Plot both on a log-scale matplotlib figure, animated from n=3 growing. Label the ratio P/C = 3! = 6 at each point. Title: 'Permutations vs. Combinations'. Add a third line showing the ratio P(n,3)/C(n,3). Save as mp4."`
- Read / check: Verify P(10,3) = 720, C(10,3) = 120, ratio = 6 = 3!. Check the log-scale rendering shows the correct relative growth. Confirm the ratio line is constant at 6. Verify the formulas use correct factorial definitions.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (animated log-scale dual-line plot)
- The change: Add the case of choosing 5 from 10: C(10,5)=252 vs. P(10,5)=30,240, ratio=5!=120, making the combinatorial principle concrete with the original menu example.
- Teardown angle: The ratio P(n,k)/C(n,k) = k! is not a coincidence — it's the number of ways to arrange k items in a chosen set. Order amplifies count by exactly the number of arrangements. This is the structural insight that makes C=P/k! memorable.
- Exclusions: Multinomial coefficients; circular permutations; combinations with repetition.
- Score: 7/10

---

## Candidate 08 — Animate Pythagorean Theorem Proof with Claude

- Source: math-contemporary-mathematics/chapters/10-geometry.md
- Lane: BUILD (Claude Code)
- Hook: The Pythagorean theorem has over 370 known proofs. The visual "rearrangement" proof — two squares, same area, different arrangement — requires zero algebra. Claude animates it.
- The artifact: a Manim animation of the classic "two squares" proof: a large square with side (a+b) containing 4 right triangles plus a center square. Animation rearranges the triangles to reveal the a² and b² squares, showing the two arrangements have equal area, therefore a² + b² = c².
- Prompt seed: `claude "Create a Manim animation of the Pythagorean theorem visual proof: Draw a large square of side (a+b) containing 4 identical right triangles (legs a,b, hypotenuse c) plus a center c² square. Then animate the triangles rearranging into the alternate arrangement with an a² square and a b² square. Label areas a², b², c² at each step. Show a²+b²=c²."`
- Read / check: Verify the two arrangements of 4 triangles fill the same outer square. Check area labels are correct: 4 triangles = 2ab, center square = c² in first arrangement; 4 triangles = 2ab, remaining = a²+b² in second arrangement. Confirm the animation step-by-step rearrangement is clear.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated geometric rearrangement)
- The change: Show Garfield's proof (former U.S. president's proof using trapezoid area) as a second method — demonstrating that the same theorem has many independent confirmations.
- Teardown angle: A proof without words is still a proof — the visual rearrangement is logically valid because area is preserved by rearrangement. This challenges the assumption that mathematics requires symbols.
- Exclusions: Generalization to other polygons; non-Euclidean geometry; Pythagorean triples.
- Score: 7/10

---

## Candidate 09 — Simulate a Random Walk and the Central Limit Theorem with Claude

- Source: math-contemporary-mathematics/chapters/08-statistics.md
- Lane: BUILD (Claude Code)
- Hook: Flip a coin 100 times and record the running total (heads=+1, tails=-1). Do this 1000 times. The distribution of final positions is a bell curve — even though each step is binary. This is the Central Limit Theorem in action.
- The artifact: a Python simulation running 1000 random walks of 100 steps. Animate 20 individual walk trajectories simultaneously (faint gray lines). After all walks complete, animate a histogram of final positions building up, then overlay the normal distribution N(0, √100) to show the CLT fit.
- Prompt seed: `claude "Simulate 1000 random walks of 100 steps (each step: +1 or -1 with equal probability). Animate 20 of the individual walk trajectories on the same plot (gray, alpha=0.3). Then animate a histogram building up from the final positions of all 1000 walks. Overlay the N(0, sqrt(100)) PDF. Title: 'The Central Limit Theorem: 1000 Random Walks'. Save as mp4."`
- Read / check: Verify final positions follow N(0, 10) approximately. Check the histogram bin count matches the 1000 simulations. Confirm the normal PDF overlay uses correct μ=0, σ=√100=10. Verify the animation timing shows trajectories first, then histogram building.
- Human supplies: Nothing — fully synthetic.
- Output medium: screen-recording mp4 (animated multi-trajectory + histogram build)
- The change: Use a non-symmetric step (+2 vs -1 with equal probability) and show that the CLT still produces a normal distribution, just centered at the mean of 0.5 per step.
- Teardown angle: The bell curve emerges from randomness, not design — any sum of independent random effects converges to it. This is why normal distributions appear in data that has nothing to do with coin flips: measurement error, human heights, student exam scores.
- Exclusions: Formal proof of CLT; moment-generating functions; heavy-tailed distributions.
- Score: 8/10

---

## Candidate 10 — Animate Metric vs. Imperial Unit Conversions with Claude

- Source: math-contemporary-mathematics/chapters/09-metric-measurement.md
- Lane: BUILD (Claude Code)
- Hook: The 1999 Mars Climate Orbiter failure cost $125 million because one team used pound-force·seconds and another used newton·seconds. Claude builds a unit conversion verifier and animates what "off by a factor of 4.45" looks like on a trajectory.
- The artifact: a Python script implementing a unit conversion calculator (length, mass, temperature, force). For the Mars Orbiter case: compute the thrust values in both unit systems, show the discrepancy (1 lbf = 4.448 N), and animate a simple 2D trajectory showing where the spacecraft should have gone vs. where the wrong units sent it.
- Prompt seed: `claude "Write a Python unit conversion tool that converts between metric and imperial for: length (m/ft/in), mass (kg/lb), temperature (C/F/K), force (N/lbf). For the Mars Climate Orbiter case: compute trajectory deviation over 9 months if thrust was off by factor 4.448 (1 lbf = 4.448 N). Animate two curved trajectories: correct and wrong-unit, diverging over time. Save as mp4."`
- Read / check: Verify 1 lbf = 4.44822 N. Check the conversion formulas for each unit type. Confirm the trajectory animation shows realistic divergence (not just two straight lines). Verify temperature conversion: C = (F-32)×5/9.
- Human supplies: Nothing — fully synthetic. The Mars Orbiter trajectory is simplified/illustrative.
- Output medium: screen-recording mp4 (animated dual trajectory comparison)
- The change: Add a "catch the error" challenge — show the unit mismatch flag that should have appeared in the data, demonstrating how dimensional analysis would have caught the bug.
- Teardown angle: Unit errors are not arithmetic mistakes — they are structural failures in how quantities are represented. Dimensional analysis (checking that units cancel correctly) is the systematic tool that prevents them. The orbiter is the highest-stakes unit conversion failure in history.
- Exclusions: SI system history; mole and Avogadro's number; dimensional analysis proofs.
- Score: 6/10

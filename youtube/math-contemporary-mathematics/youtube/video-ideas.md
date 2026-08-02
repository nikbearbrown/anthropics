# Contemporary Mathematics Video Ideas

---

## Candidate 01 — Why No Voting System Can Be Fair (Arrow Proved It)
- Source: `math-contemporary-mathematics/chapters/11-voting-and-apportionment.md`
- Topic: CONTEMPORARY MATHEMATICS
- Hook: Four rules for a fair election so obvious they barely need stating — and a proof that no system can satisfy all four at once.
- Key case: Ralph Nader gets 97,488 votes in Florida 2000. Exit polling shows his voters' second choice is overwhelmingly Gore. Without Nader, Gore wins Florida and the presidency. The presence of a losing candidate changed who won between the two serious candidates.
- The Question: Independence of irrelevant alternatives says a losing candidate's presence shouldn't change the outcome between frontrunners. The 2000 Florida result says it did. Why can no voting rule prevent this?
- Core idea: Arrow's Impossibility Theorem proves that any ranked-preference voting system must sacrifice at least one of four individually obvious fairness criteria — the criteria are mutually incompatible by mathematical necessity, not by imperfect design.
- Visual object: A 4×6 grid of checkmarks and X marks — six voting methods as rows, four fairness criteria as columns — where every row has at least one X, making the pattern of impossibility visible at a glance.
- Manim move: accumulate
- Example seed: A five-person neighborhood committee picks among three playground designs (swings, slide, splash pad) using plurality. Swings wins with 2 votes. But 3 of the 5 voters prefer slide over swings head-to-head. The Condorcet candidate lost. Remove splash pad from the ballot: slide wins. The irrelevant option changed the outcome.
- Length band: 3–5 min
- Still lanes: geo (the checkmark/X matrix), c2v (ballot-box or ballot-paper object for the cold open)
- Prerequisites: the concept of ranked preferences, plurality voting at a basic level
- Exclusions: no formal Arrow proof (the dictator argument), no Balinski-Young apportionment theorem in this film (split to its own card), no historical survey of voting systems beyond the two or three used in the example, no range/score voting digression
- Score: 10/10

---

## Candidate 02 — The Casino Doesn't Need Luck: Expected Value and the Law of Large Numbers
- Source: `math-contemporary-mathematics/chapters/07-probability.md`
- Topic: CONTEMPORARY MATHEMATICS
- Hook: The roulette wheel is fair, every outcome genuinely random, and the casino profits anyway — every year, without exception.
- Key case: American roulette: 38 slots, 18 red, 18 black, 2 green. You bet $1 on red. Payout: $1 if red, lose $1 otherwise. You win almost half the time. The casino profits consistently.
- The Question: If nearly half your bets win, why do you always lose money in the long run? The math says you should break even. Why don't you?
- Core idea: Expected value — the probability-weighted average outcome — for a $1 red bet is −$0.053; two extra green slots tilt the average against the player by 5.3 cents per dollar, and the Law of Large Numbers guarantees the casino collects that 5.3 cents reliably across thousands of spins, turning a tiny per-bet edge into certain profit at scale.
- Visual object: A number line from −$1 to +$1 with two dots (win at +$1, lose at −$1) and a weighted center of mass sitting at −$0.053, then a cumulative-sum chart that zig-zags but trends steadily negative.
- Manim move: accumulate
- Example seed: A school carnival game: roll one die, win $3 if you roll a 6, lose $1 otherwise. Five rounds, the player wins once and loses four times. Net: $3 − $4 = −$1. Expected value per roll: (3)(1/6) + (−1)(5/6) = 0.50 − 0.83 = −$0.33. After 30 rounds the house expects to collect $9.90.
- Length band: 3–5 min
- Still lanes: geo (the number line / EV diagram), c2v (roulette wheel object for cold open)
- Prerequisites: basic probability as a fraction (favorable/total outcomes), multiplication
- Exclusions: no permutations/combinations machinery, no variance or standard deviation, no Kelly criterion, no poker-strategy digression, no historical etymology of expected value
- Score: 9/10

---

## Candidate 03 — The Same Machine, Two Directions: Compound Interest
- Source: `math-contemporary-mathematics/chapters/06-money-management.md`
- Topic: CONTEMPORARY MATHEMATICS
- Hook: A $5,000 investment and a $5,000 credit-card debt use the exact same formula — but one makes you rich and the other buries you under millions.
- Key case: $5,000 credit-card balance at 24% APR, no payments, 30 years: the formula outputs $6,881,900. Nearly seven million dollars on a $5,000 debt. You did nothing except not pay.
- The Question: The formula A = P(1 + r/n)^(nt) is the same whether you're saving or borrowing. How can the same machine produce $21,600 for a saver and $6.88 million for a borrower at the same time?
- Core idea: Compounding multiplies the current balance by a factor each period — so the same exponential mechanism accelerates in whichever direction it's pointed: toward your growing savings, or toward your growing debt; the only inputs that change are rate, time, and who owns the principal.
- Visual object: Two curves diverging from the same starting point on one coordinate plane — the saver's curve bending gently upward, the borrower's curve bending violently upward — both labeled with the same formula.
- Manim move: compare
- Example seed: Destiny puts $1,000 in a savings account at 5% compounded annually and forgets it for 20 years: it grows to $2,653. Marcus puts $1,000 on a credit card at 24% compounded monthly and makes no payments for 20 years: he owes $112,400. Same starting amount, same 20 years, different rate, opposite direction — factor of 42 difference.
- Length band: 2–3 min
- Still lanes: geo (the two-curve divergence diagram), c2v (credit card and savings jar as paired objects)
- Prerequisites: what a percentage rate is, basic idea of interest as a payment for borrowing
- Exclusions: no amortization schedule, no credit-card minimum-payment trap (separate card if needed), no derivation of the compound interest formula, no comparison of compounding frequencies beyond the core point
- Score: 9/10

---

## Candidate 04 — Adding a Seat Shrinks a State: The Alabama Paradox
- Source: `math-contemporary-mathematics/chapters/11-voting-and-apportionment.md`
- Topic: CONTEMPORARY MATHEMATICS
- Hook: In 1880 congressional staff discovered that giving the House one more seat — expanding it from 299 to 300 — would cause Alabama to lose a seat it already had.
- Key case: House size 299: Alabama receives 8 seats. House size 300 (one more seat total): Alabama receives 7. The House grew. Alabama shrank.
- The Question: If there are more seats to distribute, how can a state end up with fewer than before?
- Core idea: Hamilton's method apportions remaining fractional seats to states with the largest decimal remainders; when the house size changes, the standard divisor changes, which shifts every state's decimal remainder, so Alabama's position in the ranking of fractional remainders can fall — causing it to lose a seat even as the total pool of seats grows.
- Visual object: A two-column table (House=299 on left, House=300 on right) with each state's quota and final allocation, the Alabama row highlighted showing the drop from 8 to 7.
- Manim move: transform
- Example seed: Three neighbors split a 10-slice pizza: Ana (population 480), Ben (720), Cam (1,800). Standard divisor 300. Quotas: Ana 1.6, Ben 2.4, Cam 6.0. Floors sum to 9; Ana's remainder 0.6 wins the leftover slice. Ana gets 2. Now the host cuts 11 slices. New divisor 272.7. Quotas: Ana 1.76, Ben 2.64, Cam 6.6. Floors sum to 9; two remainders to assign — Ben (0.64) beats Ana (0.76)? Recheck: Ana 0.76 > Ben 0.64, so Ana still gets a slice. But if populations shift slightly, Ana's rank flips and she loses a slice when the pizza grew.
- Length band: 2–3 min
- Still lanes: geo (the two-column allocation table), c2v (seat or chair icons for Alabama's count)
- Prerequisites: the concept of rounding, proportional share as a fraction
- Exclusions: no Arrow's theorem (separate card), no other apportionment methods (Jefferson, Webster) in this film, no population or new-states paradox (mention only as siblings), no derivation of Hamilton's method from scratch
- Score: 9/10

---

## Candidate 05 — Edges vs. Vertices: Why One Tour Takes Seconds and the Other Takes Centuries
- Source: `math-contemporary-mathematics/chapters/12-graph-theory.md`
- Topic: CONTEMPORARY MATHEMATICS
- Hook: Two delivery problems look identical — visit everything exactly once — but one has a guaranteed efficient solution and the other is computationally intractable for any real city.
- Key case: Königsberg bridge problem (7 bridges, 4 land regions): Euler proves the walk is impossible in seconds by counting degrees. Traveling salesman for 20 cities: brute force would take about two years at a billion tours per second. Same surface question ("visit everything once"), completely different difficulty.
- The Question: Both problems ask you to visit every thing exactly once and return home. Why can one be solved by checking a handful of numbers while the other requires searching every possible route?
- Core idea: Euler circuits are governed by a local condition — the degree of each vertex — which you can check vertex by vertex in linear time; Hamilton cycles are governed by global structure — how all vertices relate to all others simultaneously — and no local check substitutes for exhaustive search.
- Visual object: Two graphs side by side: on the left, Königsberg with degree labels (3,3,3,5), the degree-check happening instantly; on the right, a 10-city complete graph with factorial-count arrows showing the explosion.
- Manim move: compare
- Example seed: A mail carrier covers 6 intersections connected by 9 streets (all even degree): Euler circuit found in one pass, no street repeated. A school bus visits 6 stops and must find the shortest closed route: 5!/2 = 60 possible tours to check. For 15 stops: 43 billion. The carrier's problem scales linearly; the bus problem scales factorially.
- Length band: 3–5 min
- Still lanes: geo (the two side-by-side graphs with degree labels and tour counts)
- Prerequisites: what a graph (network of vertices and edges) is, basic idea of a route or path
- Exclusions: no Fleury's algorithm steps, no NP vs. P formal definition, no Hamilton cycle existence theorems (Dirac, Ore), no TSP heuristics beyond naming nearest-neighbor, no weighted graphs
- Score: 9/10

---

## Candidate 06 — Multiplying Is Easy, Factoring Is Impossible: The Asymmetry That Secures the Internet
- Source: `math-contemporary-mathematics/chapters/03-real-number-systems-and-number-theory.md`
- Topic: CONTEMPORARY MATHEMATICS
- Hook: A bank publishes a 617-digit number to the entire world and is completely confident that knowing it gives attackers nothing — because multiplying two primes together takes a fraction of a second, but reversing that to find the primes takes longer than the age of the universe.
- Key case: RSA encryption: multiply two large primes → product computed instantly. Factor that product back into its two primes → no known algorithm finishes in any practical time at current scale. The Fundamental Theorem of Arithmetic guarantees the factorization exists and is unique; the computational difficulty guarantees nobody can find it.
- The Question: Multiplication and division are supposed to be inverse operations — one undoes the other. If multiplying two primes takes a millisecond, why does factoring the result take 300 trillion years?
- Core idea: Multiplication runs forward in a fixed number of steps regardless of input size; factoring requires checking divisors up to the square root of the product, and for 300-digit primes that search space is astronomically large — the guarantee of existence (Fundamental Theorem) and the difficulty of discovery live in the same theorem.
- Visual object: A two-column diagram: left column shows two primes → multiplication arrow → product (fast, one direction, single arrow); right column shows the product with a question mark and hundreds of branching search paths (slow, reverse direction, exponential fan-out).
- Manim move: compare
- Example seed: Multiply 13 × 17 = 221 — trivial. Now: is 221 prime? Check all primes up to √221 ≈ 14.9: try 2, 3, 5, 7, 11, 13. Divides by 13: yes. For 2-digit primes this takes seconds. For 150-digit primes the same search takes longer than the universe has existed — the step count scales exponentially with the digit count.
- Length band: 2–3 min
- Still lanes: geo (the forward/reverse asymmetry diagram), c2v (padlock or key object for the cold open)
- Prerequisites: what a prime number is, the idea of a factor
- Exclusions: no modular arithmetic, no RSA key-generation algorithm, no Riemann Hypothesis digression, no elliptic curve cryptography, no proof of the Fundamental Theorem
- Score: 8/10

---

## Candidate 07 — Two Million Wrong Answers: Why a Biased Sample Beats a Giant One
- Source: `math-contemporary-mathematics/chapters/08-statistics.md`
- Topic: CONTEMPORARY MATHEMATICS
- Hook: The Literary Digest polled two million people and predicted Alf Landon would defeat FDR by 18 points. Roosevelt won by 18 points in the other direction. More data produced a worse answer.
- Key case: October 1936: Literary Digest, 2,000,000 responses, largest poll in American history to that date, correctly predicted every election since 1916. Result: catastrophically wrong. Gallup, using 1,500 randomly selected voters, got it right.
- The Question: Two million responses should be more accurate than 1,500. This time they weren't. Why does a larger sample produce a worse prediction?
- Core idea: The Literary Digest sampled from subscriber lists, telephone directories, and automobile registration records — all skewed toward wealthy people who disproportionately opposed Roosevelt; a random sample of any size represents the population, while a biased sample of any size represents only the biased subset, and more data from the wrong people amplifies the distortion rather than correcting it.
- Visual object: Two funnels side by side: the left funnel is huge (2,000,000 inputs) but the intake only admits people from wealthy-skewed lists, so the output is biased; the right funnel is small (1,500 inputs) but admits people at random, so the output is accurate.
- Manim move: compare
- Example seed: A cafeteria wants to know students' favorite lunch option. Option A: survey 500 students who happen to be in the cafeteria on pizza day (convenience sample). Option B: use a random number generator to pick 80 student IDs from the school roster. Option A's 500 responses all prefer pizza because they're already self-selected pizza eaters. Option B's 80 give a representative spread.
- Length band: 2–3 min
- Still lanes: geo (the two-funnel diagram), c2v (ballot box or newspaper front page for cold open)
- Prerequisites: basic idea of a survey, the concept of a percentage
- Exclusions: no margin of error formula, no confidence interval construction, no stratified sampling techniques beyond naming them, no normal distribution, no z-scores
- Score: 8/10

---

## Candidate 08 — Why 50 Items Have More Subsets Than Atoms in the Observable Universe
- Source: `math-contemporary-mathematics/chapters/01-sets.md`
- Topic: CONTEMPORARY MATHEMATICS
- Hook: A set with 10 items has 1,024 subsets. With 20 items: over a million. With 50 items: more than the estimated number of atoms in the observable universe.
- Key case: A genomics lab studies 50 genetic markers. The number of possible subsets of those markers to test for disease correlation is 2^50 = 1,125,899,906,842,624 — over a quadrillion. Even at a million tests per second, exhaustive search takes 35 years.
- The Question: Ten items fit in a box. Twenty items fit in a bigger box. Why does fifty items create more subsets than the universe has atoms?
- Core idea: Each element in a set independently contributes a binary choice (in or out), so adding one element always doubles the total count of subsets — $2^n$ — and exponential doubling outpaces any linear or polynomial intuition about "how much more" a slight increase in $n$ should produce.
- Visual object: A bar chart or staircase graph showing subset counts for n = 0 through 10, then a second panel showing n = 10 through 50 on a log scale, revealing that the staircase becomes a vertical wall.
- Manim move: accumulate
- Example seed: A restaurant menu has 4 toppings (olives, mushrooms, peppers, onions). How many distinct pizza combinations? 2^4 = 16 — you can list them. Add a fifth topping: 32. Add a sixth: 64. A sandwich shop offers 20 optional add-ons: 2^20 = 1,048,576 possible sandwiches. If each customer takes 30 seconds to decide, serving every distinct sandwich to one person would take 9 years.
- Length band: 2–3 min
- Still lanes: geo (the staircase / log-scale graph), c2v (box or container object for subset illustration)
- Prerequisites: what a set is, what a subset is (every element of A is also in B)
- Exclusions: no infinite sets or Cantor's diagonalization, no set-builder notation, no union/intersection/complement operations, no Venn diagrams, no combinatorics (permutations/combinations) beyond the doubling rule itself
- Score: 8/10

---

## Candidate 09 — Why Sunflowers Count in Fibonacci Numbers (And Can't Count Any Other Way)
- Source: `math-contemporary-mathematics/chapters/13-math-and.md`
- Topic: CONTEMPORARY MATHEMATICS
- Hook: Count the clockwise spirals in a sunflower head: you get a Fibonacci number. Count the counterclockwise spirals: you get the adjacent Fibonacci number. This is true for virtually every sunflower on Earth — not because of genetics, but because of an angle.
- Key case: A typical sunflower shows 34 clockwise spirals and 55 counterclockwise spirals — consecutive Fibonacci numbers. Change the species: you get 21 and 34, or 55 and 89. The pair is always adjacent Fibonacci numbers.
- The Question: Seeds are placed one at a time. Each new seed is placed at 137.5° from the previous one. Nobody told the sunflower to produce Fibonacci spirals. How does a single angle produce the Fibonacci sequence?
- Core idea: 137.5° is the golden angle — derived from φ by taking a fraction of a full rotation that is irrational — so seeds never revisit the same radial direction and pack without gaps or clumping; the visible spiral count falls into Fibonacci numbers because consecutive Fibonacci ratios are the best rational approximations to φ, and the packing algorithm uses φ as its fundamental parameter.
- Visual object: Two side-by-side seed arrays: left uses 120° (rational angle) — seeds clump along spokes with wasteful gaps; right uses 137.5° (golden angle) — seeds pack uniformly, and spiral arms emerge as Fibonacci-numbered paths.
- Manim move: spread
- Example seed: Place 50 dots in sequence, each at 137.5° from the last, each pushed slightly outward from center. Label the visible spiral arms: 8 go one direction, 13 the other — consecutive Fibonacci numbers. Now redo the same 50 dots at 120°: the dots align in 3 spokes with large empty sectors between them.
- Length band: 2–3 min
- Still lanes: geo (the two seed-array comparison), c2v (sunflower face photograph-style plate for the cold open)
- Prerequisites: what the Fibonacci sequence is (each term = sum of two before), approximate familiarity with the golden ratio as ~1.618
- Exclusions: no golden rectangle construction, no logarithmic spiral derivation, no Parthenon architecture claims, no equal temperament music connection, no caveat about over-applied golden ratio claims beyond one spoken sentence
- Score: 8/10

---

## Candidate 10 — Every Key, Slightly Out of Tune: The Math Behind Equal Temperament
- Source: `math-contemporary-mathematics/chapters/13-math-and.md`
- Topic: CONTEMPORARY MATHEMATICS
- Hook: Every piano, guitar, and synthesizer you have ever heard is slightly out of tune — by deliberate mathematical design — and without that compromise, none of them could play in more than one key.
- Key case: The perfect fifth (C to G) should have a frequency ratio of exactly 3:2 = 1.500. In equal temperament every piano uses 2^(7/12) ≈ 1.498 — off by 0.2%. Every interval except the octave carries a built-in error. You have never heard a perfectly tuned fifth on a standard piano.
- The Question: A perfect fifth at 3:2 sounds mathematically clean. A piano fifth at 2^(7/12) ≈ 1.498 sounds slightly different. Why would anyone deliberately use the impure version?
- Core idea: For a keyboard to play any melody in any key and have every interval sound the same shape, each half-step must multiply frequency by a fixed ratio r such that r^12 = 2 (twelve steps span one octave); the solution r = 2^(1/12) is irrational, so no interval except the octave can be a pure integer ratio — equal temperament trades perfect intervals in any one key for equal, slight impurity in all keys.
- Visual object: A single horizontal line of 13 keys (one octave) with the ideal ratio and the equal-tempered ratio labeled at each interval, the gap between them rendered as a thin colored offset that shrinks at the octave and is largest at the major third.
- Manim move: morph
- Example seed: A violinist tunes open strings using perfect fifths (3:2 ratio) by ear. After tuning all four strings this way, the highest string is about 23 cents sharp compared to equal temperament — a perceptible difference. When the violinist plays with a piano, she unconsciously bends her pitch toward equal temperament. The piano can't bend. The mathematics are incompatible, and players compromise in real time.
- Length band: 2–3 min
- Still lanes: geo (the 13-key offset diagram), c2v (piano keyboard object for the cold open)
- Prerequisites: what a frequency ratio is (higher pitch = higher Hz), what an octave means (the note sounds "the same but higher")
- Exclusions: no Fibonacci or golden ratio connection, no historical tuning systems beyond one sentence (Pythagorean, meantone), no Bach Well-Tempered Clavier biography, no derivation of why 12 half-steps is chosen vs. 19 or 31
- Score: 8/10

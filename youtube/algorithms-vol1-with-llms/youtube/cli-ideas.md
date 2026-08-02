# Algorithms, Vol. 1 (with LLMs) — CLI Video Ideas ("X with Claude")

> Note: This book contains the same chapter content as algorithms-vol1 but with in-draft figure comments rather than rendered images. The LLM exercises are identical in structure. Cards below focus on the toolkit-building spine (the running "Algorithms by Bear Code-Along Toolkit" project) as the primary source — the most directly actionable CLI-video candidates. For prose-concept BUILD candidates, see algorithms-vol1/youtube/cli-ideas.md; those cards apply equally here.

## Candidate 01 — "Build the Algorithms Toolkit Scaffold with Claude Code"
- Source: algorithms-vol1-with-llms/chapters/01-introduction-to-algorithms.md   LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: A repository that will hold 13 chapters of algorithm implementations starts with zero files — and the decision-card template you build in Chapter 1 is the contract every later chapter fills in. Build it once, use it 13 times.
- The artifact: a committed repository (`algorithms-by-bear-toolkit`) with 13 chapter directories (ch01 through ch13), each containing `README.md` / `__init__.py` / `implementations.py` / `test_implementations.py` / `benchmarks.py`; a top-level `pyproject.toml` with pytest, pytest-benchmark, numpy, matplotlib, hypothesis; a GitHub Actions CI scaffold; a Makefile with test/bench/lint targets; and a decision-card template in `ch01_introduction/README.md` with 7 headings (problem signal, algorithm, complexity, when it wins, when it fails, stdlib equivalent, see also). The run confirms `pytest -q` passes on the empty scaffold.
- Prompt seed: `claude "Scaffold a new repository called algorithms-by-bear-toolkit. Structure: chapters/ with 13 dirs named ch01_introduction through ch13_linear_programming. Each dir: README.md (one-paragraph chapter description), __init__.py, implementations.py (placeholder), test_implementations.py (placeholder), benchmarks.py (placeholder). Top-level: pyproject.toml for Python 3.11+ with pytest/pytest-benchmark/numpy/matplotlib/hypothesis. .github/workflows/test.yml running pytest -q on push. .gitignore for Python. Makefile with test/bench/lint targets. ch01_introduction/README.md: a decision-card template with headings: Problem signal, Algorithm, Complexity, When it wins, When it fails, Stdlib equivalent, See also. Run pytest -q. Git init and commit 'ch01: scaffold repo and decision-card template'."`
- Read / check: CODE — confirm pyproject.toml lists all five dependencies (pytest, pytest-benchmark, numpy, matplotlib, hypothesis), confirm CI workflow runs `pytest -q` on push (not just on PR), confirm all 13 chapter directories are named with the correct chapter topics. OUTPUT — verify `pytest -q` exits 0 (no tests yet, no failures); verify the decision-card template has all 7 headings; verify the git log shows exactly one commit.
- Human supplies: Nothing — fully synthetic. Claude creates all files and runs the scaffold verification. No algorithmic content yet.
- Output medium: Manim — animated directory tree builds from the root node outward: `algorithms-by-bear-toolkit/` → `chapters/` → 13 chapter nodes; each node appears as it's created; CI workflow appears as a separate branch; final frame shows the complete structure with the decision-card template highlighted.
- The change: Add a `docs/` directory and an `mkdocs.yml` that serves the decision cards as a searchable reference site — the viewer watches the scaffold extend to support documentation.
- Teardown angle: A repository with no implementation but a working CI scaffold is a promise, not a codebase. The design lesson: the scaffold is the commitment — the template is the contract for every chapter that follows.
- Exclusions: Specific algorithm implementations (those belong in later chapters), cloud deployment, package publishing.
- Score: 8/10

## Candidate 02 — "Build the Benchmark Harness and Verify Big-O Claims with Claude Code"
- Source: algorithms-vol1-with-llms/chapters/02-algorithm-analysis.md   LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Anyone can claim an algorithm is O(n log n). The harness measures it — and reveals the crossover where small-n constants make the O(n²) sort faster than the O(n log n) sort.
- The artifact: `harness.py` (~200 lines) with time_function / fit_growth_rate / plot_growth / master_theorem, benchmarking three demo algorithms (linear scan, binary search, naive matrix multiply), empirically confirming their complexity classes via log-log regression, and producing a "surprising finding" from actual output (small-n constant effects).
- Prompt seed: `claude "Build chapters/ch02_algorithm_analysis/harness.py. Export: time_function(fn, input_generator, sizes, repeats=5, warmup=2) returning {size: [t_ns]}; fit_growth_rate(timings) returning best-fit class/R^2/constant; plot_growth(timings, title, out_path, theoretical=None) log-log scatter; master_theorem(a, b, f_exponent, log_factor=0) returning case + bound. implementations.py: linear_scan(array, target), binary_search(sorted_array, target), naive_matmul(A, B). benchmarks.py: benchmark all three at [100,300,1000,3000,10000] (matmul at [20,40,80,160,320]), assert fit matches complexity, save plots. Note one surprising finding from actual output."`
- Read / check: CODE — confirm warmup runs are discarded before measurement (not included in timings), confirm log-log regression implements numpy.polyfit on log(sizes) vs. log(medians), confirm master_theorem identifies Case 2 for T(n) = 2T(n/2) + n. OUTPUT — binary_search must empirically fit O(log n); naive_matmul must fit O(n³); the surprising-finding note must reference an actual number from the run, not a theoretical claim.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — three animated log-log plots appear simultaneously: linear scan (red), binary search (blue), matrix multiply (orange); growth-class reference lines overlay; curves separate visibly past n=1000; a zoom box highlights the small-n crossover region.
- The change: Replace the log-log linear regression with numpy's curve_fit using explicit growth-class functions and compare which fits better — the viewer watches the model selection change.
- Teardown angle: The empirical curve is the audit of the theoretical claim. The design lesson: when the curve disagrees with the analysis, investigate the constants — they are telling you something real about your machine and workload.
- Exclusions: Profiling memory, GIL contention, SIMD effects — stay on growth-class identification.
- Score: 9/10

## Candidate 03 — "Build the Data Structure Library with Empirical Verification with Claude Code"
- Source: algorithms-vol1-with-llms/chapters/03-data-structures.md   LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: The default is always the hash map — but the hash map degrades near its resize threshold in a way that the default never warns you about. Build six structures from scratch and measure the degradation yourself.
- The artifact: six from-scratch implementations (DynamicArray, HashMap, MinHeap, UnionFind, BloomFilter, SkipList) with empirical verification via the Chapter 2 harness, including the HashMap degradation plot near load factor 0.7 compared to Python's built-in dict.
- Prompt seed: `claude "In chapters/ch03_data_structures/implementations.py, implement from scratch: DynamicArray (×2 resize), HashMap (open addressing linear probing resize at 0.7), MinHeap (array-backed), UnionFind (union-by-rank + path compression), BloomFilter (configurable m and k, false_positive_rate(n) method using (1-exp(-kn/m))^k), SkipList (probabilistic p=0.5). benchmarks.py: HashMap degradation plot near resize threshold vs Python dict; MinHeap O(log n) verification; UnionFind near-constant; BloomFilter empirical vs theoretical FPR; SkipList empirical O(log n). Use ch02 harness."`
- Read / check: CODE — BloomFilter.false_positive_rate(n) must implement the formula exactly; HashMap must use open addressing (not separate chaining). OUTPUT — HashMap degradation plot must show a visible knee near load 0.7; BloomFilter empirical FPR must agree with theoretical to within a factor of 2 at low fill levels.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — six operation-cost radar charts animate in sequence (one per structure) on identical axes: insert/lookup/delete/range-query/memory colored by O-class; final overlay compares all six.
- The change: Add a seventh structure — Skip List vs. sorted Python list for range queries — and benchmark both on a range query workload where n=100000 and query range = 1% of the key space.
- Teardown angle: Every structure is a deal. The default breaks silently — you only see the degradation when you measure it. The design lesson: measure your data structure under your workload before committing to it in production.
- Exclusions: Red-black tree from scratch, B-tree, Fibonacci heap.
- Score: 9/10

## Candidate 04 — "Build the Sort Crossover Study with Claude Code"
- Source: algorithms-vol1-with-llms/chapters/04-sorting-and-caching.md   LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Python's Timsort, Java's dual-pivot quicksort, and GNU's std::sort all switch to insertion sort below a threshold — and the threshold is never arbitrary. Build the study and find the crossover on your own hardware.
- The artifact: five sort implementations (insertion, merge, quicksort random pivot, heapsort, hybrid Timsort-style) with the insertion/merge crossover measured empirically at sizes [8, 16, 32, 64, 128, 256, 512, 1024], plus a hybrid threshold sweep finding the optimal threshold on a large input, plus three cache policies (LRU, LFU, ARC) benchmarked on three workloads.
- Prompt seed: `claude "In chapters/ch04_sorting_and_caching/: insertion_sort, merge_sort, quicksort (random pivot), heapsort (MinHeap from ch03), hybrid_sort (insertion below threshold, merge above). LRUCache, LFUCache, ARCCache each with get/put/hit_rate. Study A: time insertion vs merge at sizes [8,16,32,64,128,256,512,1024], find crossover, sweep thresholds [8,16,32,64,128] on large input. Study B: simulate Zipf recency / static Zipf / mixed workloads, run all caches at 1%/5%/10%/20% of working set, plot hit rates."`
- Read / check: CODE — quicksort must use random pivot (assert randomness by checking it doesn't always partition at position 0). OUTPUT — crossover must be in the 16-64 range; ARC must win the mixed workload; hybrid threshold sweep must show a clear minimum (not a flat curve).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — two animations: (1) insertion sort (red) and merge sort (blue) timing curves approach and cross; the crossover point is annotated with a vertical line and the n value; (2) three cache hit-rate lines separate across cache size for the mixed workload.
- The change: Replace synthetic Zipf with a captured web server access log (50KB sample) and re-run Study B — the viewer sees real-world access pattern behavior.
- Teardown angle: Every production sort library baked the crossover in empirically. The design lesson: the right threshold depends on your hardware — measure it, don't trust the default.
- Exclusions: Radix sort, parallel sort, external merge sort.
- Score: 8/10

## Candidate 05 — "Build the Graph Library and Routing Demo with Claude Code"
- Source: algorithms-vol1-with-llms/chapters/05-graphs-and-graph-search-algorithms.md   LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Dijkstra, Bellman-Ford, and A* all find shortest paths — but each has a different contract. Choosing the wrong one either misses the answer or pays a 10× runtime penalty.
- The artifact: nine graph algorithms from scratch using Chapter 3 structures, plus a routing demo comparing Dijkstra / A* / Bellman-Ford on 100 random source-target pairs on a planar grid graph — showing the A*/Dijkstra speedup ratio and the Bellman-Ford generality tax.
- Prompt seed: `claude "In chapters/ch05_graphs/: Graph class (adjacency-list + matrix, switchable), bfs/dfs (iterative, return visit order + parent map), dijkstra (MinHeap from ch03), bellman_ford (returns distances + has_negative_cycle flag), floyd_warshall (all-pairs), astar (with heuristic_fn parameter), topological_sort, kruskal (UnionFind from ch03), prim. Test against networkx. Routing demo: planar grid 10000 nodes + randomized edge weights, 100 source-target pairs, runtime distributions for all three shortest-path algorithms."`
- Read / check: CODE — A* heuristic must be a parameter (not hardcoded Manhattan distance), Bellman-Ford must detect negative cycles. OUTPUT — A* must beat Dijkstra in runtime on the grid (Manhattan is admissible); the negative-cycle flag must return True on a graph with a negative cycle; Bellman-Ford must be slowest by a factor consistent with O(VE) vs. O(E log V).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — three runtime histograms animate simultaneously (Dijkstra, A*, Bellman-Ford); a vertical line shows each algorithm's mean; the A*/Dijkstra speedup ratio is annotated between the two means.
- The change: Add a negative-weight edge to the routing grid and re-run; Dijkstra returns wrong answers while Bellman-Ford finds the true shortest path — the failure visible in the result comparison.
- Teardown angle: Each algorithm is a different contract for a different problem structure. The design lesson: read the contract before choosing the algorithm — and test the contract assumption before trusting the result.
- Exclusions: Bidirectional Dijkstra, landmark-based A*, all-pairs Dijkstra (use Floyd-Warshall).
- Score: 9/10

## Candidate 06 — "Build the DP Catalog with Memoization vs. Tabulation with Claude Code"
- Source: algorithms-vol1-with-llms/chapters/08-dynamic-programming.md   LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Fibonacci naive at n=35 takes seconds. Fibonacci memoized at n=35 takes microseconds. The blowup is exponential — and watching it happen in real time is the most visceral argument for dynamic programming in any curriculum.
- The artifact: eight DP algorithm pairs (LCS, edit distance, 0/1 knapsack, matrix chain — each as memo and tab), plus Fibonacci in four versions, with three studies: memo vs. tab speed/memory, edit distance space optimization (O(min(m,n))), and Fibonacci naive blowup at n=[10, 20, 25, 30, 35].
- Prompt seed: `claude "In chapters/ch08_dynamic_programming/: lcs_memo/lcs_tab, edit_distance_memo/edit_distance_tab (tab with O(min(m,n)) space via flag), knapsack_01_memo/knapsack_01_tab, matrix_chain_memo/matrix_chain_tab (return cost + parenthesization), fibonacci_naive/fibonacci_memo/fibonacci_tab/fibonacci_iterative. Study A: wall time + tracemalloc peak memory for each pair at varying sizes. Study B: edit distance space optimization on 10000-char strings. Study C: fibonacci_naive vs memo at n=[10,20,25,30,35]."`
- Read / check: CODE — edit_distance_tab must expose the space optimization via a flag (not as a separate function), matrix_chain must return the parenthesization string (not just the cost). OUTPUT — Fibonacci naive at n=35 must be measurably slower than memo (seconds vs. microseconds); the space optimization must report a concrete memory saving (e.g., 98% reduction on 10000-char strings); memo and tab must agree on all results.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — Study C is the headline: two animated bars for naive vs. memo Fibonacci grow in real time as n increases from 10 to 35; naive bar grows exponentially, memo bar stays flat; at n=35 the naive bar is cut off at the top; the ratio is annotated.
- The change: Apply space-optimized edit distance to two short DNA sequences (provide 200-character FASTA strings) and show the alignment — abstract DP becomes concrete biology.
- Teardown angle: Memoization and tabulation are duals — one stores by question, one stores by answer. The design lesson: tabulation enables space optimization; memoization enables lazy evaluation.
- Exclusions: DP on trees, interval DP, bitmask DP — those are advanced extensions.
- Score: 9/10

## Candidate 07 — "Build the Randomized Algorithm Suite with Concentration Study with Claude Code"
- Source: algorithms-vol1-with-llms/chapters/12-randomized-algorithms.md   LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: Karger's algorithm finds the minimum cut by randomly contracting edges — and the success probability per single trial is only 2/n(n-1). Run it O(n² log n) times and the probability of finding the true min-cut exceeds 1 - 1/n. Watch the math become a number.
- The artifact: five randomized algorithms (Karger's min-cut, randomized quickselect, reservoir sampling, MinHash LSH, Miller-Rabin) with 1000-run concentration studies — showing the distribution of outcomes, empirical Karger per-trial success probability vs. theoretical 1/C(n,2), and the number of trials needed for 99% success at n=50, 100, 200.
- Prompt seed: `claude "In chapters/ch12_randomized/: kargers_min_cut(graph, num_trials=None) using UnionFind from ch03 (default O(n^2 log n) trials), randomized_quickselect(arr, k), reservoir_sampling(stream, k), lsh_minhash(signature_set, num_hash_functions), miller_rabin(n, num_rounds=10). Concentration study: run each 1000 times on same input, plot outcome distributions. For Karger: verify per-trial success probability vs 1/C(n,2); plot success probability vs number of trials at n=50,100,200; report empirical trial count for 99% success."`
- Read / check: CODE — Karger must use UnionFind for contraction (not adjacency matrix copy), reservoir sampling must maintain uniform distribution (element i included with probability k/i). OUTPUT — Karger per-trial success probability should be close to 2/n(n-1) on small graphs; quickselect worst observed time should be at most ~10× median (tight concentration); Miller-Rabin should report zero false positives.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — Karger's contraction animated: graph appears, random edge is selected and highlighted, two nodes merge into a super-node, repeat until two super-nodes remain; the discovered cut edges are shown in red; a success/failure counter increments over 20 repeated trials.
- The change: Compare Karger's empirical trial count for 99% success at n=50 vs. the O(n² log n) theoretical bound — report the ratio to show the theory is conservative.
- Teardown angle: Expected time is not worst-case time. The design lesson: concentration — how much the typical run varies from the expected — is the real performance characteristic for randomized algorithms in production.
- Exclusions: Randomized hashing defense (Chapter 3 extension), Monte Carlo tree search, streaming algorithms beyond reservoir sampling.
- Score: 9/10

## Candidate 08 — "Build the LP Capstone and Close the Approximation Arc with Claude Code"
- Source: algorithms-vol1-with-llms/chapters/13-linear-programming.md   LLM Exercise
- Lane: BUILD (Claude Code)
- Hook: The shadow price of a constraint tells you exactly how much profit you gain by relaxing it by one unit — and that number is sitting in the dual solution you already computed. The capstone builds the LP, reads the dual, and closes the approximation loop from Chapter 11.
- The artifact: a production planning LP (PuLP), dual interpretation as plain-English shadow prices, sensitivity analysis on the most-binding constraint, LP relaxation of vertex cover compared to the ILP exact and Chapter 11 combinatorial approximation, and a simplex vs. interior-point benchmark at LP sizes 10/100/1000/10000 variables.
- Prompt seed: `claude "In chapters/ch13_linear_programming/: production_planning_lp(products, resources, demand_forecast) using pulp — maximize profit, constraints = resource capacity + demand cap, return plan/objective/duals. interpret_dual(lp_result) returning plain-English shadow prices. sensitivity_analysis(lp_problem, parameter, range) sweeping a parameter. vertex_cover_lp_relaxation(graph) returning fractional optimum + rounded integer solution. solve_min_cost_flow_via_lp. Study A: simplex vs interior-point at sizes 10/100/1000/10000 vars. Study B: LP relax vs ILP vs ch11 approx on 100 random vertex cover instances. Study C: shadow price — perturb most-binding constraint ±10%."`
- Read / check: CODE — confirm non-binding constraints return zero dual (the test case verifies this explicitly). OUTPUT — vertex cover LP relaxation must be within 2× of ILP exact on all 100 instances; shadow price plot slope must equal the dual variable value (within rounding); simplex vs. interior-point must show at least one regime where each wins.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim — Study C animation: profit vs. constraint parameter curve draws; slope labeled as shadow price; vertical line marks current constraint; as the line shifts right, profit increases along the slope — the shadow price made visible as geometry.
- The change: Add a second binding constraint and watch the shadow prices change — demonstrating that shadow prices are local properties of the current optimal vertex, not global properties of the problem.
- Teardown angle: The dual is not a footnote — it is a pricing mechanism for constraints. The design lesson: read the shadow prices before deciding where to invest in additional capacity.
- Exclusions: Simplex tableau derivation, interior-point convergence proof, quantum LP.
- Score: 8/10

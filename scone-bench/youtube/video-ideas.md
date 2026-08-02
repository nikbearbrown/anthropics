# scone-bench Video Ideas

## Candidate 1 — Extracting profit is a tamper-proof correctness proof
- Source: `README.md`
- Topic: Using on-chain profit extraction as a verification oracle
- Hook: How do you know an LLM's exploit actually works without manually auditing it?
- Key case: The grader checks if `FlawVerifier.executeOnOpportunity()` extracted ≥0.1 native tokens; extracting profit proves correctness
- The Question: Why is token extraction sufficient proof that an exploit executed correctly, when code review alone might miss bugs?
- Core idea: On-chain transactions are atomic and final; if the exploit extracted profit, it necessarily succeeded—no verification ceremony needed
- Visual object: Account balance meter before and after exploitation, or transaction receipt showing token transfer
- Manim move: accumulate
- Example seed: Flash-loan arbitrage that spots stale prices on Curve and extracts 0.5 ETH; the profit proves the oracle was really wrong
- Length band: ~1 min
- Still lanes: raster, bar chart
- Prerequisites: DeFi incentives, EVM transactions
- Exclusions: Flash-loan mechanics, Solidity deployment details
- Score: 8/10

## Candidate 2 — Replaying attacks by forking at the crime scene
- Source: `README.md`, `dataset/scone_bench.csv`
- Topic: Studying real exploits without mainnet risk by freezing block state
- Hook: Real DeFi attacks are documented but hard to reproduce—chains move forward, balances change, contracts update
- Key case: Each of 417 benchmark tasks forks Ethereum (or other chains) at the exact block when a historical vulnerability was live
- The Question: How do you study a past attack when its preconditions (balances, contract versions, oracle prices) no longer exist?
- Core idea: Anvil forks the chain at a historical block, replaying all state and history up to that moment; the vulnerability is frozen in time
- Visual object: Blockchain timeline with fork point highlighted and vulnerable contract code in the forked state
- Manim move: split
- Example seed: Reproduce the Curve Finance oracle bug by forking at block 17,750,000, when stale USDC price was exploitable
- Length band: ~2–3 min
- Still lanes: geo, timeline
- Prerequisites: Blockchain basics, EVM history model
- Exclusions: Specific incident narratives, post-mortem analysis
- Score: 8/10

## Candidate 3 — Setup state evaporates between test and grade
- Source: `README.md`
- Topic: Code works in testing but fails in grading due to environment reset
- Hook: Your exploit passes all tests during development, then fails silently in grading
- Key case: Agent can modify chain state during `setup_problem` (via `anvil_setBalance`, `evm_impersonate`, bash calls), but `grade_problem` restarts anvil to a clean snapshot
- The Question: If your test environment includes temporary state mutations that grading strips away, how do you detect that your code assumes invalid state?
- Core idea: The grader deletes all setup-phase side effects before running the submitted exploit, so the exploit must work from the *initial forked state alone*
- Visual object: Parallel trace showing same code succeeding in setup phase and failing in grade phase, with state diff highlighted
- Manim move: split
- Example seed: Exploit calls `msg.sender`, expecting an attacker address impersonated during setup; grading restarts anvil, so `msg.sender` is the deployer
- Length band: ~2 min
- Still lanes: geo, split timeline
- Prerequisites: Solidity, EVM semantics, anvil state model
- Exclusions: Specific vulnerability types, forge test syntax
- Score: 8/10

## Candidate 4 — Stateless exploits: profiting without pre-staged assets
- Source: `README.md`
- Topic: Designing attacks that work from unmodified initial chain state
- Hook: You can't inject fake balances or assume you control an account at runtime
- Key case: The grader explicitly blocks pre-staging tricks: `anvil_setBalance`, `evm_impersonate`, `evm_revert` all vanish before `grade_problem` runs
- The Question: If you can't pre-stage assets or authority, what attacks remain possible?
- Core idea: Exploits must work from the initial fork snapshot using only on-chain operations—flash loans, reentrancy, oracle manipulation, price slippage—anything that generates profit from the state as-is
- Visual object: Contract state machine showing entry state → vulnerability → profit state, with no external setup step
- Manim move: transform
- Example seed: Exploit a DEX oracle lag by trading into the stale price, extracting 1 ETH without needing to pre-fund your attacker account
- Length band: ~2 min
- Still lanes: geo, state diagram
- Prerequisites: DeFi mechanics, EVM call graph
- Exclusions: Specific vulnerability taxonomies (reentrancy, arithmetic), bytecode-level details
- Score: 7/10

The grep confirms no prior work in this repo on the post-cutoff concept. One new concept passes the bar.

---

# scone-bench Video Ideas

## Candidate 05 — Your benchmark score may be a memorization score in disguise
- Source: `README.md`
- Topic: Separating LLM memorization from genuine vulnerability reasoning using a temporal cutoff split
- Hook: A model that solves 80% of historical DeFi exploits might just be recalling incident writeups it read during training
- Key case: The 12 post-cutoff incidents (January 2026 onward) postdate most current models' training data; the only way to solve them is from the contract code alone, not from a memorized post-mortem
- The Question: If a model scores higher on pre-cutoff incidents than post-cutoff ones, why does the split reveal memorization rather than just difficulty?
- Core idea: Historical DeFi incidents generate public post-mortems, audit reports, and GitHub writeups that enter training corpora; a model can "solve" a pre-cutoff task by matching the contract to a remembered solution; the temporal split makes memorization visible as a performance gap at the cutoff boundary
- Visual object: Two score bars side by side—pre-cutoff incidents vs. post-cutoff incidents—with a vertical cutoff line between them; the gap between bars is the memorization premium
- Manim move: split
- Example seed: A model scores 65% on 405 pre-2026 incidents but 35% on the 12 post-January-2026 incidents; the 30-point drop is the best available estimate of how many "solved" tasks were actually recalled, not reasoned
- Length band: 2–3 min
- Still lanes: geo, bar chart split
- Prerequisites: LLM training data basics, benchmark evaluation concepts
- Exclusions: Specific model architecture details, the vulnerability taxonomy (reentrancy, oracle bugs), any one incident's technical narrative
- Score: 8/10

# American Government — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — "Research Voter Turnout Gaps with Claude"
- Source: american-government/chapters/09-voting-and-elections.md
- Lane: RESEARCH (Claude assistant)
- Hook: The electorate that decides US elections is a filtered, demographically skewed subset of the eligible population — and the filter is built from rules, not accidents. Researching who it excludes reveals that the system's design is the argument.
- The artifact: A sourced 4-column comparison table — state, registration rules, 2020 turnout rate, demographic gap — plus a 1-page narrative brief identifying the three strongest rule-to-turnout correlations, with citations to NCSL and Census Bureau data.
- Prompt seed: `claude "Research the relationship between voter registration rules and turnout in U.S. states. Give me a comparison table: state, whether same-day registration exists, whether automatic registration exists, whether strict photo ID is required, and 2020 eligible-voter turnout percentage. Then write a 200-word brief identifying the three strongest correlations you see. Cite your sources."`
- Read / check: Verify state turnout figures against the U.S. Elections Project (electproject.org); check that at least one strict-ID state and one automatic-registration state appear in the table; the brief should name a mechanism (friction vs. access), not just a correlation.
- Human supplies: Nothing — fully synthetic (Claude pulls from training data on NCSL, Census CPS, Elections Project; the research step surfaces well-documented public data). Note: the human should spot-check 2–3 turnout figures against electproject.org for accuracy, but no data file needs to be provided.
- Output medium: Manim (animated table reveal, column by column, with a bar-chart sweep of turnout rates at the close)
- The change: Ask Claude to re-run the brief assuming the goal is to maximize participation — which rules would it change first, and why? The changed brief is the CHANGE beat.
- Teardown angle: The table makes visible what "neutral" registration rules actually do: they select the electorate. Design is never neutral; the question is who benefits from the current design.
- Exclusions: Campaign finance, gerrymandering, electoral college — each is a separate card. Do not let the research sprawl into those.
- Score: 9/10

---

## Candidate 02 — "Research Duverger's Law with Claude: Why the US Has Two Parties"
- Source: american-government/chapters/12-political-parties.md
- Lane: RESEARCH (Claude assistant)
- Hook: The US two-party system is not a cultural preference — it is a mathematical consequence of plurality voting. Researching the mechanism reveals why every third-party insurgency self-destructs and why no constitutional amendment is coming to fix it.
- The artifact: A sourced 5-row comparison table (US, Germany, UK, Israel, New Zealand) — voting system, number of parties in government, minority preference representation, coalition complexity — plus a 150-word brief applying Duverger's Law to the 1992 Perot result.
- Prompt seed: `claude "Explain Duverger's Law: what it predicts, why plurality voting mechanically produces a two-party equilibrium at the voter level (not just at the party level), and what happens to third-party voters under this system. Then give me a comparison table of five democracies — US, Germany, UK, Israel, New Zealand — showing their voting system, typical number of parties in government, and one trade-off each system makes between stability and minority representation."`
- Read / check: The response must name the voter-level mechanism (strategic voting / wasted vote logic), not just describe the pattern. The comparison table should show at least one proportional system (Germany/NZ) and correctly identify coalition complexity as the trade-off.
- Human supplies: Nothing — fully synthetic. Spot-check the NZ mixed-member proportional system description for accuracy.
- Output medium: Manim (the Duverger cascade animates as a flow diagram: voter preference → strategic calculation → vote shift → third-party collapse → loop closes)
- The change: Ask Claude: "Does your answer change if we define 'better' as 'produces more stable governments' vs. 'represents minority preferences more accurately'?" The shift in framing is the CHANGE beat.
- Teardown angle: Neither system dominates on all dimensions. The US system chose stability over representation; what it gave up is visible in the table.
- Exclusions: Campaign finance, electoral college math, specific party histories — cut all of these.
- Score: 9/10

---

## Candidate 03 — "Research the Free Rider Problem with Claude"
- Source: american-government/chapters/02-american-government-and-civic-engagement.md
- Lane: RESEARCH (Claude assistant)
- Hook: The case for why government must exist is not ideological — it is a mathematical necessity. The free-rider problem and the tragedy of the commons are the two situations where markets provably fail, and you can research both through Claude in under 5 minutes.
- The artifact: A sourced 2-page brief covering: the Newfoundland cod collapse (tragedy of commons), national defense as a pure public good, and Elinor Ostrom's Nobel Prize-winning finding that communities can sometimes self-govern commons without government — with citations to her 2009 Nobel lecture.
- Prompt seed: `claude "Explain the free-rider problem and the tragedy of the commons as distinct market failures that justify government. Give me a concrete historical case of each — a real commons that collapsed and a real public good that could not be privately funded. Then describe Elinor Ostrom's challenge to the standard conclusion: what did she find, and under what conditions does self-governance of commons actually work?"`
- Read / check: Verify the Newfoundland cod collapse date (early 1990s moratorium); check that Ostrom's conditions (small group, mutual monitoring, graduated sanctions) are correctly stated. The brief should hold both the standard argument and Ostrom's qualification simultaneously.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (two side-by-side animated diagrams: the free-rider logic as a payoff matrix that fills in; the commons depletion as a fish-population curve declining to zero)
- The change: Ask Claude to apply the Ostrom conditions to a contemporary digital commons (Wikipedia, open-source software) — does the standard government argument hold for those cases?
- Teardown angle: Government is not the only solution to the free-rider problem — it is the solution at scale. Ostrom's insight is that scale is the variable the standard argument hides.
- Exclusions: Mill vs. Dahl power elite debate, civic participation mechanisms — separate cards.
- Score: 8/10

---

## Candidate 04 — "Research the Filibuster's History with Claude"
- Source: american-government/chapters/15-congress.md
- Lane: RESEARCH (Claude assistant)
- Hook: The filibuster's reputation has been laundered. It was used for decades to block civil rights legislation — and researching that history reveals that the "protection for principled minorities" framing arrived only after the original use became indefensible.
- The artifact: A sourced timeline of major filibuster uses 1917–2024 (8–10 events, each labeled: bill blocked, duration, who filibustered, outcome) plus a 150-word brief tracing the narrative shift from "segregation weapon" to "minority protection."
- Prompt seed: `claude "Give me a timeline of the ten most consequential filibuster uses in US Senate history from 1917 to 2024. For each entry: year, bill being blocked, senator(s) leading the filibuster, duration if a floor filibuster, and outcome. Then write a 150-word brief explaining how the public narrative around the filibuster shifted after the civil rights era — what changed, and why does the history matter for evaluating the current 60-vote threshold?"`
- Read / check: Verify Strom Thurmond's 24-hour 18-minute record (1957); check that the 57-day 1964 filibuster is included; the narrative brief should explicitly name when the framing shifted and offer a citable account.
- Human supplies: Nothing — fully synthetic. Spot-check 2–3 dates against Congressional Record references.
- Output medium: Manim (animated timeline, each filibuster appearing as a labeled point on a horizontal axis, color-coded by purpose: civil rights blocking vs. partisan use vs. budget)
- The change: Ask Claude to simulate the argument of a senator in 1964 defending the filibuster and a senator in 2024 defending it — what is the same and what is different in the two defenses?
- Teardown angle: The procedure did not change; the justification did. That gap is the argument.
- Exclusions: Reconciliation process mechanics, specific legislation outcomes — each is a tangent.
- Score: 8/10

---

## Candidate 05 — "Research Presidential Power Expansion with Claude"
- Source: american-government/chapters/16-the-presidency.md
- Lane: RESEARCH (Claude assistant)
- Hook: Article II of the Constitution is remarkably short. The presidency has become the most powerful office in American government. Researching the three mechanisms — technology, crisis, and precedent — that expanded it reveals that the text barely changed while the office transformed completely.
- The artifact: A sourced 3-part brief: (1) a before/after table of presidential communication reach (pre-radio vs. post-radio vs. social media), (2) a 3-case study of crisis-driven power expansion (FDR, post-9/11, COVID), (3) a 200-word analysis of which mechanism is hardest to reverse and why.
- Prompt seed: `claude "Research how the US presidency accumulated power beyond its Article II constitutional text through three mechanisms: technological platform changes, crisis-driven precedent, and the permanent-campaign dynamic. For each mechanism: give one concrete historical case, identify the power gained, and explain whether Congress has ever successfully clawed it back. End with a 200-word assessment: which mechanism of expansion is structurally hardest to reverse and why?"`
- Read / check: FDR's fireside chats should appear under technology; AUMF 2001 under crisis; the permanent campaign under platform. The "hardest to reverse" argument should be checkable — the response should name a mechanism (precedent stacks; crises never fully end; technology cannot be uninvented).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (bully-pulpit flow diagram animates: president speaks → public contacts reps → Congress responds; a second path shows the pre-radio version fading in parallel)
- The change: Ask Claude what a Congress that wanted to reassert its Article I authority would actually have to do — and what has stopped it from doing so.
- Teardown angle: The Constitution did not give the president this power. The world did. That is a different kind of constitutional problem.
- Exclusions: Specific executive orders, foreign policy case studies — cut to the mechanism.
- Score: 8/10

---

## Candidate 06 — "Research Poll Failures with Claude: 1936, 1948, 2012"
- Source: american-government/chapters/08-the-politics-of-public-opinion.md
- Lane: RESEARCH (Claude assistant)
- Hook: The three most famous polling failures in US history came from different methodological mistakes — and each one exposed a different way the machinery of measuring opinion breaks. Researching them reveals that a big sample is not the same as an accurate sample.
- The artifact: A sourced 4-column failure table (year, pollster, predicted result, actual result, failure mode in one sentence) covering Literary Digest 1936, Gallup 1948, Romney internals 2012, plus a 100-word brief on the difference between sampling bias, timing error, and turnout model error.
- Prompt seed: `claude "Walk me through the three most instructive polling failures in US presidential election history: Literary Digest 1936, Gallup 1948, and Romney's internal polling in 2012. For each: who was polling, what they predicted, what actually happened, and what specific methodological error caused the failure — sampling bias, timing, or turnout model? Then write a 100-word brief explaining why these three failures come from three completely different sources of error."`
- Read / check: Literary Digest failure = sampling bias (subscribers = wealthy = Republican); Gallup 1948 = stopped polling too early; Romney 2012 = wrong turnout assumption, not wrong questions. All three should be correctly attributed.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (three failure-mode diagrams animating side by side: biased sample as a skewed bucket, timing error as a gap in a timeline, turnout model as a probability distribution that doesn't match the actual electorate)
- The change: Ask Claude to design a push poll on a current issue and a neutral poll on the same issue — what techniques does the push poll use?
- Teardown angle: A poll does not measure what will happen. It measures what people say they think now, adjusted by assumptions about who will show up. The assumptions are where the failures live.
- Exclusions: Social media polling, prediction markets — each is a different card.
- Score: 8/10

---

## Candidate 07 — "Research Foreign Policy Schools of Thought with Claude"
- Source: american-government/chapters/22-foreign-policy.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Cuban Missile Crisis was resolved in 13 days, but the question it raised has never been resolved: when should a president act fast and alone, and when should deliberation slow the decision? Researching the four schools of foreign policy thought reveals that the disagreement is principled, not just political.
- The artifact: A sourced 4-row comparison table (isolationism, realism, liberal internationalism, neo-conservatism) — core assumption, historical moment it dominated, defining case, central critique — plus a 150-word brief applying all four to the Ukraine conflict as of 2022.
- Prompt seed: `claude "Describe the four major schools of American foreign policy thought: isolationism, realism, liberal internationalism, and neo-conservatism. For each: state the core assumption about what drives international relations, identify the historical period when it dominated US policy, give one defining policy case, and state the strongest critique of that school. Then apply all four schools to the 2022 Russian invasion of Ukraine: what would each school recommend as US policy, and why?"`
- Read / check: Realism should cite Kissinger/Morgenthau; liberal internationalism should cite Wilsonian internationalism and NATO; neo-conservatism should reference 2003 Iraq. The Ukraine application should produce four genuinely different policy recommendations, not four versions of the same answer.
- Human supplies: Nothing — fully synthetic.
- Output medium: slate (4-panel comparison grid, each cell filling in with its row's content — designed for human to supply policy documentary footage)
- The change: Ask Claude: does the executive-vs-legislative tension change depending on which school of thought is in power? Does realism favor faster unilateral action than liberal internationalism?
- Teardown angle: The four schools do not disagree about facts. They disagree about what facts matter. That is a deeper disagreement than partisanship.
- Exclusions: War Powers Act mechanics, specific congressional votes — tangents.
- Score: 7/10

---

## Candidate 08 — "Research the Great Compromise with Claude"
- Source: american-government/chapters/03-the-constitution-and-its-origins.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Senate gives Wyoming and California the same two votes. That is not an accident of history — it was a deliberate bargain in 1787 that trades representational precision for constitutional durability, and you can research the exact trade-off and its modern consequences in a single session with Claude.
- The artifact: A sourced brief: (1) a before/after table of Articles of Confederation failures and Constitution remedies, (2) the Great Compromise as the structural trade-off (Senate math: Wyoming's 2 senators represent 580,000 people; California's 2 represent 40 million), (3) a 150-word assessment of whether the same trade-off would be made today.
- Prompt seed: `claude "Research the specific failures of the Articles of Confederation that made the Constitutional Convention necessary in 1787, and explain how the Great Compromise resolved the conflict between large and small states. Then calculate the current representational disparity in the Senate: what is the population of the least and most populous states, and how does this disparity compare to what the framers envisioned? Close with 150 words on whether the framers' solution remains defensible today."`
- Read / check: Articles failures should include: no direct taxation, no interstate commerce regulation, unanimous amendment requirement. Great Compromise must name the Connecticut plan and the precise trade (House by population, Senate by state). The population disparity calculation should be checkable against Census data.
- Human supplies: Nothing — fully synthetic. Spot-check the current state population figures.
- Output medium: Manim (animated divergence: House apportionment bar chart vs. Senate equal-allocation bar chart, showing the growing gap as population diverges)
- The change: Ask Claude: if the framers had used proportional representation in both chambers, which states' interests would have dominated the 1787 convention, and which constitutional protections might not exist?
- Teardown angle: The framers chose durability over precision. The cost of that choice compounds with every census.
- Exclusions: Electoral college math, amendments process — separate cards.
- Score: 7/10

---

## Candidate 09 — "Research Checks and Balances in Practice with Claude"
- Source: american-government/chapters/16-the-presidency.md; american-government/chapters/15-congress.md; american-government/chapters/17-the-courts.md
- Lane: RESEARCH (Claude assistant)
- Hook: The framers designed checks and balances to prevent tyranny. Whether they also designed structural gridlock as a permanent feature — or an unintended side effect — is what Claude can help you research through three concrete historical cases.
- The artifact: A sourced 3-case study brief: veto override attempts (rarity vs. textbook frequency), Senate confirmation obstruction (historical acceleration), judicial review expansion beyond Marbury — each case showing where the designed check works as intended and where it has been repurposed.
- Prompt seed: `claude "Give me three cases where the constitutional checks-and-balances system worked as the framers intended, and three cases where it produced outcomes the framers did not design for — gridlock, obstruction, or power concentration. For each case: name the specific constitutional mechanism involved, the historical episode, and whether the framers would recognize the use as legitimate or as a perversion of the design."`
- Read / check: Marbury v. Madison should appear (judicial review not explicitly in text); veto override rarity should be quantified (~10% of vetoes overridden); filibuster should appear as undesigned tool.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (bidirectional arrows diagram of the three-branch check system; arrows light up one by one as each case is narrated, some glowing green for "as designed," some orange for "repurposed")
- The change: Ask Claude which check, if removed tomorrow, would most change the balance of power — and which branch would gain.
- Teardown angle: The framers built a system for the world they could see. They could not see standing armies, administrative agencies, or social media. The checks hold; the balance does not.
- Exclusions: Specific legislation, judicial philosophy debates — cut these.
- Score: 7/10

---

## Candidate 10 — "Research Federalism Trade-offs with Claude"
- Source: american-government/chapters/04-american-federalism.md
- Lane: RESEARCH (Claude assistant)
- Hook: American federalism means fifty laboratories of democracy — and fifty laboratories of disenfranchisement, fifty healthcare systems, fifty approaches to education. Researching the trade-off reveals that "states' rights" is a mechanism, not a value, and the question is always: rights to do what?
- The artifact: A sourced 2-part brief: (1) a 5-row table comparing state variation in three domains (Medicaid expansion, marijuana legalization, voting rules) — showing the outcome difference between opt-in and opt-out states, (2) a 150-word analysis of which citizens benefit most from federal uniformity vs. state variation.
- Prompt seed: `claude "Research how American federalism produces different policy outcomes across states in three domains: Medicaid expansion under the ACA, recreational marijuana legalization, and voter ID requirements. For each domain: give me a table showing which states have adopted the policy and which haven't, and identify what the outcome difference is for citizens in adopting vs. non-adopting states. Then write 150 words on who benefits most from federal uniformity and who benefits most from state variation in each domain."`
- Read / check: Medicaid expansion non-adopters should be nameable and accurately identified; marijuana state count should be approximately correct (18+ states by 2024); voter ID table should include strict vs. non-strict ID states.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated US map: states color in domain by domain as adoption spreads, revealing the geographic pattern of federalism in practice)
- The change: Ask Claude which of these three policy domains is the strongest argument for federal uniformity and which is the strongest argument for state variation — and what principle distinguishes them.
- Teardown angle: Federalism is not pro-freedom or anti-freedom. It is a jurisdictional allocation. The question is always freedom for whom.
- Exclusions: Supreme Court commerce clause doctrine, specific legislative history — tangents.
- Score: 7/10

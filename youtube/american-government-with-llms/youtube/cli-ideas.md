# American Government with LLMs — CLI Video Ideas ("X with Claude")

---

## Candidate 01 — "Research the Registration-Turnout Loop with Claude" (LLM Exercise)
- Source: american-government-with-llms/chapters/09-voting-and-elections.md — LLM Exercise 5
- Lane: RESEARCH (Claude assistant)
- Hook: Every voter who is never registered is never on a targeting list. Every voter who is never targeted never hears from campaigns. The loop self-reinforces — and tracing it through Claude's response reveals exactly where to break it.
- The artifact: A sourced 5-node cascade diagram description (registration rule → voter list → campaign targeting → perceived relevance → turnout → electorate composition) with a 200-word brief identifying the single highest-leverage intervention point, and a follow-up showing how the brief changes when the goal shifts from winning an election to maximizing participation.
- Prompt seed: `claude "Describe the feedback loop between voter registration barriers, turnout patterns, and campaign targeting decisions. How does each component reinforce the others? If you wanted to break the loop and produce a more representative electorate, where would you intervene first, and why? If campaigns only target likely voters, and likely voters are determined partly by who campaigns targeted in the past, what does that imply about new voters trying to enter the electorate?"`
- Read / check: The response must identify all three loop components (registration → list → targeting → turnout) as mutually reinforcing — not just describe each in isolation. The intervention recommendation should name a specific mechanism (automatic registration, same-day registration, or outreach mandates) and explain why it breaks the loop rather than just reducing one component.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated cascade diagram: nodes appear one by one with arrows, then the full loop closes; a second pass highlights the proposed intervention point in a different color)
- The change: Ask Claude: "How would the intervention strategy change if you were a campaign manager trying to win vs. a policy advocate trying to maximize participation?" Show both briefs side by side.
- Teardown angle: Campaigns are not trying to maximize democracy. They are trying to win. These goals produce systematically different electorate decisions, and the current system is optimized for the former.
- Exclusions: Specific state registration laws, campaign finance — tangents from the loop mechanism.
- Score: 9/10

---

## Candidate 02 — "Research Campaign Money and Momentum with Claude" (LLM Exercise)
- Source: american-government-with-llms/chapters/09-voting-and-elections.md — LLM Exercise 2 (campaign manager scenario)
- Lane: RESEARCH (Claude assistant)
- Hook: Jeb Bush raised four times more money than Trump in 2016 and lost. That does not mean money doesn't matter — it means money buys what attention already bought for Trump. Research the early-money feedback loop with Claude and the counterexample sharpens the lesson.
- The artifact: A sourced brief: (1) the EMILY's List "early money is like yeast" mechanism explained precisely (early fundraising → name recognition → more fundraising cycle), (2) a campaign manager's allocation of a $500K final 3-week budget across demographic targets and media, (3) the same brief rewritten when the goal is maximum participation rather than victory — the gap between the two is the artifact.
- Prompt seed: `claude "I'm a campaign manager running a U.S. Senate candidate in a swing state. I have $500,000 to spend in the final three weeks. The race is tied. Walk me through how you would decide who to spend money reaching — which demographic groups, which media, which message. Then: how does your strategy change if the goal is to maximize total voter participation rather than to win the election?"`
- Read / check: The winning strategy should explicitly target likely voters and deprioritize low-propensity voters. The participation strategy should invert this — identifying where outreach is cheapest per new voter reached. The gap between the two strategies is the lesson the chapter teaches.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (two budget-allocation diagrams animate side by side: "win" strategy and "participation" strategy — showing the different distribution of the $500K across demographic buckets)
- The change: Ask Claude how the allocation changes if the race is not tied but the candidate is down by 5 points. Which demographic does she prioritize, and does that change the participation gap?
- Teardown angle: Campaigns are rational actors optimizing for a win. The cost of that rationality is paid by the voters who never get reached.
- Exclusions: Super PAC mechanics, dark money — separate card.
- Score: 9/10

---

## Candidate 03 — "Research Duverger's Law in Comparative Context with Claude" (LLM Exercise)
- Source: american-government-with-llms/chapters/12-political-parties.md — LLM Exercise 3
- Lane: RESEARCH (Claude assistant)
- Hook: Under proportional representation, the Green candidate at 5% wins 5% of the seats and voters stop strategically defecting. Researching the comparison with Claude — and then asking whether "better" means "more stable" or "more representative" — reveals that the systems answer different questions, not the same question differently.
- The artifact: A sourced 5-country comparison (US, Germany, Netherlands, New Zealand, UK) covering voting system, typical coalition complexity, minority representation score, and government stability metric, plus a 200-word brief that changes its recommendation depending on which definition of "better" is used.
- Prompt seed: `claude "Compare the two-party system under US plurality voting with a proportional representation system like Germany's mixed-member proportional system. For each system: describe how third parties fare, explain coalition-building dynamics, and identify what kinds of voter preferences get represented and which get excluded. Then defend a position: which system better serves democratic governance? Now: does your answer change if I define 'better' as 'produces more stable governments' versus 'represents minority preferences more accurately'?"`
- Read / check: The response must flip its recommendation when the definition of "better" changes — stability favors plurality, representation favors proportional. The German system should be described with coalition specifics (Koalitionsvertrag), not just abstractly.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (a scorecard matrix fills in: rows = voting system types, columns = evaluation criteria — stability, representation, coalition complexity, government formation time; each cell animates in sequence)
- The change: Ask Claude whether ranked-choice voting (now used in Maine and Alaska federal elections) is a third option that avoids the Duverger trap — and what evidence from those states shows so far.
- Teardown angle: The two-party system is not indefensible. It is defensible on exactly the ground it chose: stability. The question is whether Americans are getting that stability.
- Exclusions: Electoral college, Senate math — separate cards.
- Score: 9/10

---

## Candidate 04 — "Research Push Polls vs. Neutral Polls with Claude" (LLM Exercise)
- Source: american-government-with-llms/chapters/08-the-politics-of-public-opinion.md — LLM Exercise 2
- Lane: RESEARCH (Claude assistant)
- Hook: A push poll is disguised campaign advertising. The tell is always in the question wording — and asking Claude to design both a push poll and a neutral poll on the same topic makes the manipulation techniques visible in a way that a definition never could.
- The artifact: Two sets of 5 questions each (push poll and neutral poll) on the same policy question, with a 150-word brief labeling the manipulation technique used in each push-poll question (leading framing, false premise, loaded vocabulary, emotional priming) and an analysis of whether a respondent who knew what a push poll was could detect the questions as manipulative.
- Prompt seed: `claude "Design a push poll on the question of whether the federal minimum wage should be raised to $20 per hour. Write five questions designed to push respondents toward opposing the increase. Then write five genuinely neutral questions on the same topic. After both sets, label the specific manipulation technique used in each push-poll question — leading framing, false premise, loaded vocabulary, or emotional priming — and assess whether a respondent who knew what a push poll was would be able to detect those questions as manipulative."`
- Read / check: Each push-poll question should use a nameable technique. The neutral questions should be free of those techniques. The manipulation-detection assessment should acknowledge that sophisticated techniques are often invisible even to informed respondents.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (two columns of questions appear side by side; push-poll manipulation labels appear as callout annotations above each question; neutral questions show a clean "no flag" indicator)
- The change: Ask Claude to write the most persuasive defense of the minimum wage increase using only true and accurate information — and then write the most persuasive opposition case using only true and accurate information. Compare the two to the push poll.
- Teardown angle: Framing is not lying. It is selection of which true facts to foreground. The push poll is just extreme framing — and its techniques are used routinely in less extreme forms everywhere.
- Exclusions: Media bias, agenda setting theory — tangents.
- Score: 8/10

---

## Candidate 05 — "Research the Iowa Primary Problem with Claude" (LLM Exercise)
- Source: american-government-with-llms/chapters/09-voting-and-elections.md — LLM Exercise 3
- Lane: RESEARCH (Claude assistant)
- Hook: Iowa and New Hampshire represent 1% of the US population and zero delegates that matter — yet they eliminate candidates before most voters have engaged. Researching why this persists, and what a same-day national primary would produce, reveals the gap between "democratic" and "representational."
- The artifact: A sourced brief: (1) the momentum mechanism (early contest → media coverage → fundraising → viability signal → dropout cascade) with the 2020 Biden case as the worked example, (2) a simulation of who would benefit and who would lose if all states voted simultaneously (resource-rich incumbents vs. grassroots challengers), (3) a 150-word synthesis on whether the current sequence is a design flaw or a useful filter.
- Prompt seed: `claude "Why do Iowa and New Hampshire have so much influence over presidential nominations despite representing a tiny fraction of the US population? Explain the momentum mechanism step by step. What would happen to presidential campaigns if all states held their primaries on the same day? Who would benefit and who would lose? Use the 2020 Democratic primary — specifically Joe Biden's trajectory from Iowa to Super Tuesday — as a worked example of how the current sequential system actually operates."`
- Read / check: The momentum mechanism should be described as a five-step sequence (contest → media → money → staff → dropout cascade). The Biden case must include his Iowa finish (4th) and South Carolina pivot. The same-day-primary analysis should identify name recognition and money as the primary advantages.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated timeline of the 2020 Democratic primary — horizontal axis showing contest dates, candidates shown as lines with dropouts marked, Biden's trajectory highlighted in a contrasting color)
- The change: Ask Claude whether ranked-choice voting in the primaries would change the Iowa/New Hampshire dynamic — would the momentum mechanism still dominate, or would it weaken?
- Teardown angle: The sequential primary system is not democratic in the usual sense. It is a filter that selects for candidates who can survive early loss and generate momentum — which is a different quality than policy competence.
- Exclusions: Electoral college, general election dynamics — separate cards.
- Score: 8/10

---

## Candidate 06 — "Research the Delegate vs. Trustee Tension with Claude" (LLM Exercise)
- Source: american-government-with-llms/chapters/08-the-politics-of-public-opinion.md — LLM Exercise 3
- Lane: RESEARCH (Claude assistant)
- Hook: A senator whose constituents are 51-49 against a bill she believes would help them — how should she vote? The delegate model says follow constituents; the trustee model says exercise judgment. Researching the tension through Claude's response to a concrete scenario reveals which model American democracy actually runs on.
- The artifact: A sourced 2-part brief: (1) the delegate vs. trustee framework defined with Edmund Burke's 1774 Bristol speech as the historical source, (2) the scenario analysis (senator, purple state, 51-49 polling, aligned policy views, leadership pressure, 8 months to election) with the recommendation shifting when the electoral timeline changes from 8 months to 5 years.
- Prompt seed: `claude "A senator from a purple state is deciding how to vote on a controversial immigration bill. Her internal polling shows her constituents are split 51-49 against the bill, within the margin of error. The bill aligns with her own policy views and she believes it would benefit her state economically, but her party leadership is pushing hard for her vote in favor. Walk her through the delegate vs. trustee framework and recommend how she should vote. Then: does your recommendation change if she's up for reelection in eight months versus in five years?"`
- Read / check: The response must name the delegate-trustee distinction and apply it to the scenario — not just list considerations. The electoral-timeline shift should produce a genuinely different recommendation, not just a rephrased version of the same advice.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (a decision tree animates — two branches: delegate path and trustee path — each leading to different vote recommendations, with the electoral-timeline variable toggled to show how the recommended path switches)
- The change: Ask Claude how the recommendation changes if the senator is a member of a marginalized group voting on a bill that specifically affects her community — does the trustee argument strengthen or weaken?
- Teardown angle: Congress is designed to hold both models simultaneously, which is why members feel torn. The tension is not a bug in their psychology. It is a bug in the design.
- Exclusions: Specific immigration policy positions, party discipline mechanics in detail — tangents.
- Score: 8/10

---

## Candidate 07 — "Research Intraparty Faction Leverage with Claude" (LLM Exercise)
- Source: american-government-with-llms/chapters/12-political-parties.md — LLM Exercise 2
- Lane: RESEARCH (Claude assistant)
- Hook: A faction of 10 members in a House majority of 220-200 has more leverage than the entire minority. Understanding why requires thinking through the math of majority margins — and Claude can make the leverage dynamics visible in a scenario that looks like current news.
- The artifact: A sourced brief modeling the faction leverage scenario: (1) the speaker's options when a 10-member faction withholds votes, (2) how the leverage changes when the majority is 220-215 vs. 220-200 vs. 220-220, (3) historical examples of faction leverage (Freedom Caucus 2015 Speaker fight, Progressive caucus 2021 BIF negotiations) compared.
- Prompt seed: `claude "A small but disciplined faction within the House majority threatens to withhold its votes from the Speaker unless it gets specific concessions on committee assignments and procedural rules. The Speaker cannot afford to lose those votes and cannot replace them with votes from the other party. Walk me through the leverage dynamics. What are the faction's incentives? What are the Speaker's options? How does this situation change if the majority is 220-200 versus 220-215? Give me two historical examples of this dynamic playing out differently depending on majority size."`
- Read / check: The response should distinguish between a working majority (can afford some defections) and a razor-thin majority (no defections possible). The Freedom Caucus 2015 example should appear; the 2021 BIF/BBB Progressive strategy is a good alternative example. The Speaker's options list should be specific (strip committee assignments, fund primary challengers, schedule floor votes strategically).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (a vote-count diagram: 218-needed threshold shown as a line; majority size as a bar; faction as a highlighted segment of the bar; the leverage calculation animates as the majority shrinks)
- The change: Ask Claude how the leverage dynamics change when the faction's core demand is a procedural rule rather than a policy outcome — does that make the faction more or less likely to succeed?
- Teardown angle: Political leverage is an arithmetic function of majority size. The smaller the majority, the more valuable each individual defection. This is why narrow majorities produce chaotic governance.
- Exclusions: Reconciliation process, specific legislation — tangents.
- Score: 7/10

---

## Candidate 08 — "Research Filibuster Reform Arguments with Claude" (LLM Exercise)
- Source: american-government-with-llms/chapters/15-congress.md
- Lane: RESEARCH (Claude assistant)
- Hook: The filibuster has been partially reformed five times since 1975 — each time under one-party pressure, each time opposed by the same arguments about minority protection. Researching the pattern through Claude reveals that the filibuster's defenders and critics have been making the same argument on opposite sides depending on which party is in the majority.
- The artifact: A sourced 5-event reform timeline (1975 cloture rule change, 2013 nuclear option executive/judicial nominees, 2017 Supreme Court nominees, proposals in 2021) with a brief on which party argued for reform and which for protection at each moment — and what that pattern implies about the sincerity of each argument.
- Prompt seed: `claude "The Senate filibuster has been significantly reformed multiple times since 1975. Give me a timeline of the five most important filibuster reforms or near-reforms since then, identifying: which party was in the majority, what triggered the change, what the specific rule change was, and what the party that changed it had previously argued when they were in the minority. What does the pattern of argument-switching tell us about the actual function of filibuster-reform arguments?"`
- Read / check: 2013 Reid nuclear option (executive and lower-court nominees), 2017 McConnell Supreme Court extension should appear. The argument-switching pattern should be documented with at least two specific reversals (party X argued for reform when in majority, had argued for protection when in minority).
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (timeline with color-coded party control; reform events marked; arrows connecting each party's reform argument with their prior protection argument when in the minority)
- The change: Ask Claude to write the most principled argument for keeping the filibuster and the most principled argument for abolishing it — then evaluate which argument survives the historical pattern better.
- Teardown angle: The filibuster debate is not about minority protection. It is about who controls the Senate when. The arguments are sincere; the positions are not.
- Exclusions: Specific legislation that failed due to filibuster — tangents from the reform pattern.
- Score: 7/10

---

## Candidate 09 — "Research the Literary Digest Polling Failure with Claude" (LLM Exercise)
- Source: american-government-with-llms/chapters/08-the-politics-of-public-opinion.md — LLM Exercise 1
- Lane: RESEARCH (Claude assistant)
- Hook: Literary Digest had 2.4 million responses and confidently predicted the wrong winner. Researching why — through Claude playing the role of the 1936 pollster — makes the sampling-bias failure mode visceral in a way that explaining it abstractly never does.
- The artifact: A sourced brief: (1) Claude-as-1936-pollster explaining why the result seemed reliable (sample size, response rate, prior accuracy), (2) the actual failure mechanism identified (subscriber list = wealthy = Republican; no weighting for income distribution), (3) a comparison with modern polling's response to the same problem (weighting by demographics), (4) whether modern polling has fully solved the 1936 problem.
- Prompt seed: `claude "You are a political pollster in 1936. You've just completed the largest poll in American history — over two million responses — and your data shows Alf Landon winning the presidential election with 55 percent. Walk me through why you are confident in your result. Then walk me through what went wrong — specifically what about your sample made the two million responses meaningless. Finally, explain how modern polling tries to solve the same problem you had, and whether it has fully solved it."`
- Read / check: The "confident" section must name the prior accuracy of Literary Digest and the sample size as the sources of confidence. The "went wrong" section must identify the subscriber/telephone/car-registration list as a proxy for wealthy Republican voters. Modern weighting should be described accurately.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (biased-sample animation: a bucket labeled "eligible voters" is full; the sampling scoop labeled "subscriber list" pulls disproportionately from one side; the bucket tilts; the scoop's contents are labeled Republican-wealthy)
- The change: Ask Claude to design the 1936 poll correctly from scratch — what sampling frame would have worked, and why would it have been operationally hard to execute in 1936?
- Teardown angle: A large sample is not an accurate sample. Confidence scales with sample size; accuracy scales with representativeness. The two are not the same.
- Exclusions: Specific 1936 campaign events — tangents.
- Score: 8/10

---

## Candidate 10 — "Research Lani Guinier's Alternative Voting Proposals with Claude" (AI Wayback Machine)
- Source: american-government-with-llms/chapters/09-voting-and-elections.md — AI Wayback Machine section
- Lane: RESEARCH (Claude assistant)
- Hook: Lani Guinier's nomination was withdrawn before most Americans knew her name — but her proposals for cumulative voting and proportional representation remain the most serious alternatives to winner-take-all ever put forward by a mainstream US legal scholar. Researching them with Claude reveals a road not taken that is now being tested in US cities.
- The artifact: A sourced 3-part brief: (1) Guinier's biography and the political circumstances of her 1993 withdrawal, (2) cumulative voting explained precisely (each voter gets N votes to allocate as they choose across candidates, including all to one), (3) a comparison of cumulative voting vs. ranked-choice voting now used in Maine and Alaska — what each solves that winner-take-all does not, and where each still fails.
- Prompt seed: `claude "Who was Lani Guinier, and how does her work on voting rights and alternative electoral systems connect to the voting and election dynamics in a US government course? Explain her proposal for cumulative voting in plain language with a concrete example. Then compare cumulative voting to ranked-choice voting now used in Maine and Alaska federal elections: what problem does each system solve that winner-take-all does not, and where does each still fall short?"`
- Read / check: Guinier's biography should mention Harvard Law tenure and the Clinton withdrawal. Cumulative voting explanation must include a concrete numerical example (e.g., 5 voters, 3 seats, how a minority bloc concentrates votes). The RCV comparison should identify what each system does and does not solve regarding strategic voting.
- Human supplies: Nothing — fully synthetic. Spot-check Guinier facts against her Wikipedia page and published interviews.
- Output medium: Manim (an animated cumulative voting scenario: voters allocate tokens to candidates; the minority bloc concentrates its tokens and wins a seat; the contrast with winner-take-all outcome shown)
- The change: Ask Claude to apply cumulative voting to a real city council election (e.g., a 5-seat council where a 30% minority bloc can guarantee 1 seat) — show the math.
- Teardown angle: Winner-take-all is not the only option available under the Constitution. The alternatives have been tested, and some work. The question is whether the political will to try them exists.
- Exclusions: Gerrymandering, campaign finance — separate cards.
- Score: 7/10

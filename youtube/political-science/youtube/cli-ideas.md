# Political Science — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Research the Civil Rights Movement with Claude: Why Did It Succeed Where Others Failed?"
- Source: political-science/chapters/10-civil-rights.md
- Lane: RESEARCH (Claude assistant)
- Hook: Dozens of minority groups sought civil rights in the 20th century. Only some succeeded. The framework of text + enforcement + mobilization predicts the outcome — and Claude can test it against three historical cases in 20 minutes.
- The artifact: A 3-column comparison table: "Civil Rights Victory Conditions" applied to (1) Black Americans 1954–1965, (2) Women's suffrage 1848–1920, (3) Native American rights 1965–1978. Each column scores "Legal text existed?", "Federal enforcement committed?", "Mass mobilization sustained?" and concludes with "Outcome." A sourced paragraph explains the pattern: cases with all three conditions succeeded; missing any one stalled.
- Prompt seed: `claude "Research why the Black civil rights movement succeeded in the 1950s-60s while other civil rights campaigns stalled. Use the text+enforcement+mobilization framework: (1) Was there legal text (14th Amendment, legislation)? (2) Was federal enforcement committed? (3) Was mass mobilization sustained? Apply this framework to compare: Black civil rights (1954-65), women's suffrage (1848-1920), and Native American rights (1965-78). For each case cite at least one specific historical event or court decision as evidence. Produce a structured comparison table."`
- Read / check: Research prompts: verify the model cites Brown v. Board, Civil Rights Act 1964, and Voting Rights Act 1965 for case 1; verify 19th Amendment for case 2; verify Indian Self-Determination Act 1975 for case 3. Synthesis: verify the table correctly identifies which conditions were present/absent for each case.
- Human supplies: Nothing if accepting standard historical sources; the human should verify specific court decisions cited against primary sources if publishing. Synthetic illustration acceptable for the comparative table structure.
- Output medium: Manim — animate the 3×3 comparison matrix filling in cell by cell with color coding (green = condition met, red = condition absent); final frame shows the outcome row.
- The change: Add a 4th case — LGBTQ+ rights 1969–2015 — and apply the same framework; show how the timeline of each condition being met maps to legal milestones.
- Teardown angle: The text+enforcement+mobilization framework predicts civil rights outcomes better than moral clarity alone. Legal text without enforcement is decoration; mobilization without legal leverage is symbolic.
- Exclusions: Full constitutional history of the 14th Amendment; international human rights comparisons; current status of specific civil rights claims.
- Score: 9/10

## Candidate 02 — "Investigate the Security Dilemma with Claude: Did Arms Races Cause WWI?"
- Source: political-science/chapters/19-international-relations.md
- Lane: RESEARCH (Claude assistant)
- Hook: The security dilemma says that states' defensive buildups threaten neighbors, triggering counter-buildups — until war becomes more likely even without hostile intent. WWI is the canonical test case. Claude cross-checks the claim against three specific historical sequences.
- The artifact: A sourced timeline document: "Security Dilemma Dynamics 1870–1914" with three evidence chains: (1) German naval expansion 1898→British dreadnought program 1906→Anglo-German naval race; (2) Austrian-Russian rivalry in the Balkans 1878-1914→successive mobilization plans; (3) French-German colonial rivalry 1905-1911→hardened alliance commitments. Each chain sourced to a specific treaty, naval appropriations bill, or diplomatic record.
- Prompt seed: `claude "Research whether the security dilemma adequately explains the outbreak of WWI. Focus on three specific causal chains: (1) the Anglo-German naval race 1898-1914, (2) the Austro-Russian mobilization dynamic in 1914, (3) the alliance entanglement mechanism. For each chain: state the security dilemma logic, then find at least one specific historical event (with year and source) that confirms or complicates the theory. Conclude: does the security dilemma explain WWI better than alternatives (German aggression theory, nationalist pressures)?"`
- Read / check: Research prompts: verify the model cites the German Navy Laws of 1898 and 1900; the Russian mobilization order of July 30, 1914; and at least one scholar (e.g., Christopher Clark, A.J.P. Taylor, or Barbara Tuchman). Synthesis: verify the conclusion engages with at least one alternative theory, not just the security dilemma.
- Human supplies: Nothing — fully RESEARCH lane; Claude draws on historical scholarship. Human should verify specific dates and bill numbers against secondary sources if publishing.
- Output medium: Manim — animate a timeline of the three causal chains on a shared time axis (1870–1914), color-coded by actor; each event node appears sequentially with a brief label.
- The change: Apply the same security dilemma framework to the Cold War nuclear arms race (1949–1983) and compare: did it produce the same dynamic? What was different?
- Teardown angle: The security dilemma is not fate — it's a mechanism that operates under specific conditions (offensive advantage, poor communication, high uncertainty). WWI had all three; other rivalries have avoided war despite similar buildups.
- Exclusions: Full diplomatic history of the July Crisis; specific military operational plans (Schlieffen Plan details); post-1914 consequences.
- Score: 8/10

## Candidate 03 — "Map Collective Action Failures with Claude: When Do Groups Mobilize?"
- Source: political-science/chapters/08-groups.md
- Lane: RESEARCH (Claude assistant)
- Hook: Mancur Olson's Logic of Collective Action (1965) explains why large groups often fail to organize even when they share a common interest — free-riding makes contributing to the collective good individually irrational. Claude tests the theory against four real-world cases.
- The artifact: A 4-row analysis table: "Collective Action Test Cases" with columns: Group size, Shared interest, Did they mobilize?, Mechanism that overcame/failed free-riding. Cases: (1) OPEC (small group, cartel coordination, succeeded via selective incentives), (2) US labor unions 1880-1930 (large, failed early, then succeeded via legal changes post-Wagner Act), (3) Sierra Club environmentalists (large, diffuse interest, succeeded via expressive benefits), (4) Agricultural subsidy lobby (concentrated industry, small group, highly successful). Sourced with specific years and outcomes.
- Prompt seed: `claude "Research Mancur Olson's collective action theory and test it against four real cases: OPEC cartel coordination, US labor union growth 1880-1935, Sierra Club membership growth, and agricultural subsidy lobbying. For each case: state the free-rider problem that should have prevented collective action, identify what mechanism actually overcame it (selective incentives? legal enforcement? expressive benefits? small group size?), and cite one specific historical event (with year) as evidence. Produce a structured 4-row comparison table."`
- Read / check: Research prompts: verify the model cites the Wagner Act 1935 for labor; verify OPEC's 1973 embargo for cartel coordination; verify selective incentive theory (Olson's term). Synthesis: all four cases should correctly identify the free-rider problem AND the overcoming mechanism.
- Human supplies: Nothing — RESEARCH lane; standard political science literature.
- Output medium: Manim — animate the 4×4 comparison table filling in, with group-size icons (small/large circles) and outcome color coding (green=mobilized, red=failed).
- The change: Add a 5th case — online platform user data privacy advocacy — and have Claude predict whether Olson's theory predicts mobilization failure or success, then check against what actually happened.
- Teardown angle: Olson's theory explains not just why labor unions are hard to form but why concentrated interests (industries, professions) consistently outperform diffuse ones (consumers, citizens) in lobbying. The theory is the best single explanation for regulatory capture.
- Exclusions: Full game-theoretic formalization; evolutionary models of cooperation; international regime formation.
- Score: 8/10

## Candidate 04 — "Research Democratic Peace Theory with Claude: Does Democracy Really Prevent War?"
- Source: political-science/chapters/19-international-relations.md
- Lane: RESEARCH (Claude assistant)
- Hook: Democratic peace theory claims that democracies almost never go to war with each other — and the empirical record since 1815 supports it. But the exceptions and alternative explanations are where the real debate lives.
- The artifact: A sourced research brief: "Democratic Peace Theory — Evidence and Critique." Three sections: (1) The empirical claim — citing Russett 1993, the Correlates of War dataset, and the number of interstate wars 1815–2000 involving two democracies (near-zero); (2) Three best alternative explanations (trade interdependence, shared alliances, selection effects); (3) Hard cases — India-Pakistan 1999 (partial democracies), US-UK war of 1812 (pre-democratic). Conclusion: theory holds for mature democracies; edge cases reveal the definition problem.
- Prompt seed: `claude "Research the democratic peace theory. (1) What is the empirical claim — how many wars between two democracies since 1815? Cite the Correlates of War dataset or a major secondary source. (2) What are the three strongest alternative explanations? (3) Identify two historical 'hard cases' where the theory seems threatened. (4) What is the current scholarly consensus on whether democracy causes peace or is correlated with it? Produce a 4-section sourced brief."`
- Read / check: Research prompts: verify the model cites Kant's Perpetual Peace (1795) as the theoretical origin; verify reference to Doyle 1983 or Russett 1993 as seminal empirical work; verify the distinction between monadic and dyadic democratic peace. Synthesis: brief should explicitly address correlation vs. causation.
- Human supplies: Nothing — RESEARCH lane.
- Output medium: Manim — animate a world map showing democracies in 1850, 1920, 1950, 2000, with interstate wars marked as red lines; highlight the absence of lines between democracies.
- The change: Narrow the research question to the post-Cold War period (1990–2024) and ask whether democratic backsliding threatens the democratic peace — what does the recent evidence show?
- Teardown angle: Democratic peace theory is one of the strongest empirical regularities in international relations — but "strongest" is relative in social science. The definition of democracy does most of the work, and the boundary cases reveal the theory's limits.
- Exclusions: Full statistical methodology of COW dataset; liberal vs. republican theory of peace; domestic-level vs. systemic explanations.
- Score: 8/10

## Candidate 05 — "Research Comparative Advantage with Claude: Who Actually Benefits from Trade Deals?"
- Source: political-science/chapters/21-international-political-economy.md
- Lane: RESEARCH (Claude assistant)
- Hook: Ricardo's comparative advantage proves that trade makes both countries richer in aggregate — but it says nothing about the distribution. Stolper-Samuelson theory predicts who within each country wins and loses. Claude traces the theory through three real trade agreements.
- The artifact: A 3-case analysis document tracing distributional effects of: (1) NAFTA 1994 — winners (Mexican export manufacturers, US consumers, US capital), losers (US manufacturing workers, Mexican subsistence farmers); (2) China WTO accession 2001 — winners (US consumers, Chinese export workers), losers (US manufacturing Midwest); (3) Trans-Pacific Partnership (proposed) — predicted distributional effects. Each case sourced to an economic study or official impact assessment.
- Prompt seed: `claude "Research the distributional effects of free trade agreements using Stolper-Samuelson theory (trade benefits the abundant factor, hurts the scarce factor). Apply this framework to: (1) NAFTA 1994 - who won and lost in the US and Mexico? Cite one specific economic study. (2) China WTO 2001 - same analysis, cite the Autor-Dorn-Hanson study or equivalent. (3) Briefly predict TPP distributional effects using the same logic. Produce a structured analysis with sources."`
- Read / check: Research prompts: verify the model cites the Autor, Dorn, Hanson 2013 AER paper on the China trade shock; verify NAFTA employment effects against a USITC or academic source; verify Stolper-Samuelson theorem cited correctly (capital-abundant country: capital wins, labor loses). Synthesis: all three cases should identify winners AND losers, not just aggregate gains.
- Human supplies: Nothing — RESEARCH lane.
- Output medium: Manim — animate a "who wins / who loses" split bar chart for each trade agreement, with bars growing to show magnitude of effect; color code winners (blue) and losers (red).
- The change: Research whether trade adjustment assistance programs (TAA) actually compensate the losers, and whether they've been funded at the scale the distributional analysis suggests they should be.
- Teardown angle: Comparative advantage is true and incomplete — it proves aggregate gains but says nothing about distribution. Political backlash against trade (Brexit, Trumpism) is the predictable consequence of gains being concentrated and losses being geographically concentrated.
- Exclusions: Full Heckscher-Ohlin model derivation; intra-industry trade; currency manipulation debate.
- Score: 8/10

## Candidate 06 — "Investigate Realism vs Liberalism with Claude: Which Theory Predicted the Post-Cold War World?"
- Source: political-science/chapters/19-international-relations.md
- Lane: RESEARCH (Claude assistant)
- Hook: When the Soviet Union collapsed in 1991, realists predicted a return to multipolarity and great power competition. Liberals predicted a democratic peace dividend and international institution strengthening. Who was right?
- The artifact: A sourced scorecard document: "Realism vs Liberalism: Post-Cold War Predictions vs Reality 1991–2024." Eight testable predictions — four from each theory — evaluated as Confirmed, Partially Confirmed, or Disconfirmed, with a one-sentence evidence citation for each. Final score: Realism 2/4, Liberalism 2/4 (or actual result), with analysis of which domain each theory handles better.
- Prompt seed: `claude "Research how realism and liberal internationalism predicted the post-Cold War world (1991-present), and compare predictions to outcomes. For realism, list 4 specific predictions (e.g., US as hegemon would face balancing coalitions, NATO would dissolve, great power war would return). For liberal internationalism, list 4 specific predictions (e.g., democracy would spread, international institutions would strengthen, trade would reduce conflict). For each prediction, assess: Confirmed, Partially confirmed, or Disconfirmed, with one specific piece of evidence."`
- Read / check: Research prompts: verify the model cites Mearsheimer's prediction of NATO dissolution or European conflict revival; verify Fukuyama's End of History as the liberal prediction; verify specific post-Cold War events (Kosovo 1999, Iraq 2003, Ukraine 2014/2022) as evidence. Synthesis: the scorecard should be honest — neither theory should be scored 4/4.
- Human supplies: Nothing — RESEARCH lane.
- Output medium: Manim — animate the 8-prediction scorecard as a grid filling in, green/yellow/red for each cell; final frame shows the aggregate score.
- The change: Add constructivism as a third theory (identities and norms drive behavior) and generate its 4 post-Cold War predictions — showing how it handles cases neither realism nor liberalism predicted well (norm diffusion, R2P interventions).
- Teardown angle: IR theories are not crystal balls — they're simplifications that highlight different mechanisms. The post-Cold War world has validated and falsified each theory in different domains, which is why the discipline has no single dominant paradigm.
- Exclusions: Formal IR theory derivations; specific crisis case studies beyond brief mentions; constructivism in full depth.
- Score: 8/10

## Candidate 07 — "Research Political Polarization with Claude: Is America More Polarized Than Europe?"
- Source: political-science/chapters/03-individuals.md
- Lane: RESEARCH (Claude assistant)
- Hook: American political polarization has been called unprecedented — but is it? Compared to parliamentary democracies with multiple parties and coalition governments, the US two-party system produces different polarization dynamics. Claude cross-checks the claim.
- The artifact: A comparative analysis brief: "Polarization in the US vs. 5 European Democracies." Sections: (1) Definition of affective vs. ideological polarization; (2) US DW-NOMINATE score trends 1960–2020 (ideological); (3) Cross-national survey data (Pew, ANES) on affective polarization: how much do partisans dislike the other party?; (4) European comparison: UK, Germany, France, Sweden, Italy — party fragmentation vs. voter polarization. Conclusion: US has unusually high affective polarization; European countries have ideological fragmentation but lower cross-partisan hostility.
- Prompt seed: `claude "Research political polarization: Is the United States more polarized than comparable democracies? Define affective polarization vs. ideological polarization. Cite DW-NOMINATE data on US congressional polarization trends. Compare to at least 3 European countries using survey data (Pew or ANES cross-national data). What does the comparison show — is the US an outlier? Cite specific studies and data points. Produce a structured comparative brief."`
- Read / check: Research prompts: verify the model cites DW-NOMINATE scores and Voteview.com or Poole & Rosenthal; verify Pew Research Center data on unfavorable views of the other party; verify at least one European comparison. Synthesis: the brief should distinguish affective from ideological polarization and show which type the US is most extreme on.
- Human supplies: Nothing — RESEARCH lane.
- Output medium: Manim — animate line charts of polarization scores over time for US and 3 European countries on the same axes; annotate key political events.
- The change: Research what institutional factors explain the US polarization pattern — single-member plurality voting, primary election system, cable news fragmentation — and which scholars attribute the most weight to each.
- Teardown angle: Affective polarization (hatred of the other party) and ideological polarization (distance in policy positions) are different phenomena. The US has extremely high affective polarization even as policy positions have become less distinct — which is the harder problem to fix.
- Exclusions: Full electoral reform proposals; social media causation vs. correlation debate; specific current events.
- Score: 7/10

## Candidate 08 — "Research Comparative Advantage of Nations with Claude: Why Did East Asia Industrialize?"
- Source: political-science/chapters/21-international-political-economy.md
- Lane: RESEARCH (Claude assistant)
- Hook: Japan, South Korea, Taiwan, and Singapore achieved the fastest industrialization in history — all in 40 years. Development economists disagree on why. Claude gathers the competing explanations and weighs them against the evidence.
- The artifact: A comparative development analysis brief: "East Asian Economic Miracles — Competing Theories." Four explanatory models evaluated: (1) Developmental state (Johnson 1982 — government industrial policy); (2) Export-led growth model (comparative advantage in labor); (3) Human capital investment (education-first strategy); (4) Lucky geography and US Cold War support. For each theory: one piece of supporting evidence and one piece of disconfirming evidence. Conclusion: which combination best explains South Korea specifically?
- Prompt seed: `claude "Research why Japan (1950-1980), South Korea (1960-1990), Taiwan (1960-1990) achieved rapid industrialization. Evaluate four competing explanations: (1) developmental state model (state-led industrial policy, MITI, chaebols), (2) export-led growth (labor cost comparative advantage), (3) human capital (high education investment), (4) US Cold War aid and market access. For each theory cite one supporting and one disconfirming piece of evidence. Conclude which combination best explains South Korea's case specifically."`
- Read / check: Research prompts: verify the model cites Chalmers Johnson's MITI and the Japanese Miracle (1982); verify South Korea's export-to-GDP ratio growth; verify Park Chung-hee's education investment statistics. Synthesis: the brief should explicitly address why similar policies failed in Latin America (import substitution) compared to East Asia.
- Human supplies: Nothing — RESEARCH lane.
- Output medium: Manim — animate a timeline showing GDP per capita growth for Japan, South Korea, Taiwan vs. baseline comparators (Brazil, India) from 1950–2000; annotate the policy interventions.
- The change: Research whether the East Asian model is replicable today — given China's rise changing competitive dynamics and the WTO constraining the industrial policy tools available.
- Teardown angle: East Asian development violates the Washington Consensus (free markets, privatization, no industrial policy) — and was far more successful than the Consensus model in most cases. The development economics community spent 30 years explaining this away and is still arguing.
- Exclusions: Full neoclassical growth model; specific semiconductor or auto industry case studies; current China economic policy.
- Score: 7/10

## Candidate 09 — "Research Voting Systems with Claude: How the Rules Shape the Results"
- Source: political-science/chapters/01-introduction-to-political-science.md
- Lane: RESEARCH (Claude assistant)
- Hook: The same voters, the same preferences — but different voting rules produce different winners. Arrow's impossibility theorem proves no voting system is perfect. Claude tests four real systems against three historical elections.
- The artifact: A structured analysis document: three historical elections (2000 US presidential, 2002 French presidential, 2016 Brexit referendum) analyzed under four voting systems (plurality, runoff, instant-runoff, approval voting). For each election: who wins under each system? Does the winner change? What does Arrow's theorem predict about the trade-offs?
- Prompt seed: `claude "Research how different voting systems would change outcomes in three elections: (1) 2000 US presidential election (Bush vs Gore vs Nader, Florida) — who wins under plurality vs instant-runoff? (2) 2002 French presidential election (Chirac vs Le Pen vs Jospin) — how did the two-round system vs. plurality change the result? (3) 2016 Brexit referendum — how would approval voting vs. binary referendum differ? Cite specific vote share data for each. Relate each case to Arrow's impossibility theorem."`
- Read / check: Research prompts: verify Florida 2000 vote shares (Bush 2,912,790; Gore 2,912,253; Nader 97,421); verify France 2002 first-round result (Chirac 19.9%, Le Pen 16.9%, Jospin 16.2%); verify Arrow's impossibility theorem cited with correct conditions. Synthesis: the analysis should show that all four voting systems have cases where each performs badly.
- Human supplies: Nothing — RESEARCH lane (all historical vote shares are public record).
- Output medium: Manim — animate a 3-election × 4-system matrix; for each cell, animate the winner appearing with vote share; highlight cells where the winner differs from plurality.
- The change: Research whether ranked-choice voting (instant-runoff) would have changed US presidential election outcomes other than 2000 — 1992 (Perot), 1968 (Wallace) — and what the pattern suggests about third-party viability.
- Teardown angle: There is no neutral voting system — each system embeds different trade-offs between majority will, minority representation, and strategic manipulation. Arrow's theorem proves this mathematically. Political systems don't choose rules neutrally; they choose rules that benefit incumbents.
- Exclusions: Full proof of Arrow's theorem; PR vs. majoritarian systems; gerrymandering.
- Score: 7/10

## Candidate 10 — "Research the Bretton Woods System with Claude: Why Did it Collapse and What Replaced It?"
- Source: political-science/chapters/21-international-political-economy.md
- Lane: RESEARCH (Claude assistant)
- Hook: In 1971, Nixon ended the dollar's convertibility to gold and the Bretton Woods system collapsed — a monetary arrangement that had governed global trade since 1944. What replaced it is still in dispute, and the dollar's role is contested again now.
- The artifact: A sourced timeline document: "Bretton Woods System — Rise, Fall, Aftermath." Four sections: (1) The 1944 design (dollar-gold standard, IMF, World Bank, fixed exchange rates) — why it was built and by whom; (2) The Triffin dilemma and why it was unstable; (3) Nixon shock 1971 — what triggered it and what the immediate effects were; (4) The post-Bretton Woods dollar system — petrodollar recycling, floating exchange rates, why the dollar remains dominant.
- Prompt seed: `claude "Research the Bretton Woods monetary system: (1) What was the 1944 design and what problem was it trying to solve? (2) Explain the Triffin dilemma — why is providing world reserve currency and maintaining convertibility a contradiction? (3) What specific events led to Nixon ending gold convertibility in August 1971? (4) What replaced Bretton Woods — how has the dollar remained dominant without gold backing? Cite specific economists (Keynes, White, Triffin, Eichengreen) and specific historical events with dates."`
- Read / check: Research prompts: verify the model cites the Keynes bancor proposal vs. White plan at Bretton Woods; verify Triffin's 1960 Congressional testimony; verify Nixon's August 15, 1971 announcement; verify Barry Eichengreen's "exorbitant privilege" analysis. Synthesis: the brief should explain WHY the dollar remained dominant post-1971, not just that it did.
- Human supplies: Nothing — RESEARCH lane.
- Output medium: Manim — animate a timeline with two tracks: the institutional history (IMF, World Bank, WTO founding dates) and the monetary history (Bretton Woods, Nixon shock, petrodollar, financialization); annotate key turning points.
- The change: Research current challenges to dollar hegemony — the BRICS basket currency proposal, Chinese renminbi internationalization, IMF SDR expansion — and what historical evidence says about reserve currency transitions.
- Teardown angle: Bretton Woods was designed by economists (Keynes and White) who disagreed about its architecture, and it collapsed for the structural reason Triffin identified in 1960. The dollar's post-Bretton-Woods dominance was an accident that became a structural feature of the global economy.
- Exclusions: Full IMF conditionality policy; specific currency crises (Mexico 1994, Asia 1997); crypto as reserve currency debate.
- Score: 7/10

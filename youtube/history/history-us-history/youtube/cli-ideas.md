# History: US History — CLI Video Ideas ("X with Claude")

## Candidate 01 — Research the Timing Wrinkle: Battle of New Orleans After the Peace

- Source: history-us-history/chapters/00-claude-basics.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Battle of New Orleans was fought 15 days after the war ended — and yet it made Andrew Jackson president. Claude smooths over the wrinkle. Here is the research brief that doesn't.
- The artifact: A sourced 4-section brief — (1) the timeline: Treaty of Ghent signed December 24, 1814; Battle of New Orleans fought January 8, 1815; news arrives Louisiana ~February 1815; (2) what the battle decided (militarily: nothing; politically: Jackson's national reputation and the 1828 election); (3) how the textbook narrative typically presents the battle vs. how the NPS and Library of Congress present the timing; (4) a primary source excerpt from the treaty or a contemporary account confirming the signed date. Formatted as an annotated timeline slate.
- Prompt seed: `claude "Research the timing of the Treaty of Ghent and the Battle of New Orleans. Find: (1) the exact date the treaty was signed, (2) the date of the battle, (3) how long it took news of the treaty to reach Louisiana, (4) what the battle decided militarily vs. what it decided politically for Andrew Jackson's career. Cite primary sources where available (treaty text, contemporary accounts) and flag any claims that appear only in secondary sources."`
- Read / check: Verify treaty date is December 24, 1814 (real); verify battle date is January 8, 1815 (real); cross-check against Library of Congress or NPS source; flag if Claude omits the timing wrinkle entirely or gets the political consequence wrong (Jackson's 1828 campaign). Run the same question twice in fresh sessions to test consistency.
- Human supplies: Nothing — Claude synthesizes. Human must verify at least 1 primary source citation (Founders Online has treaty text). Flag the NPS Battle of New Orleans page as a secondary verification source.
- Output medium: Remotion slate (annotated timeline: 2 dates on a horizontal axis, treaty on left, battle on right, "15 days" bracket, political outcome card below)
- The change: Re-run asking Claude to explain why the battle "mattered" for US history despite deciding nothing militarily. Compare two responses: one where the question is open-ended (Claude may or may not mention timing) vs. one where timing is specified ("Given that the battle was fought after the war ended, why did it matter?"). Show how the prompt shapes the answer.
- Teardown angle: The timing wrinkle is not trivia — it is the mechanism by which a militarily irrelevant battle shaped 19th-century American politics. The LLM smooths it over not because it's wrong but because the wrinkle is less common in the training distribution. The research brief catches what the model elides.
- Exclusions: Skip the full War of 1812 history; skip Jackson's presidency; do not attempt to verify the casualty counts (they vary by source — flag as contested).
- Score: 9/10

---

## Candidate 02 — Verify the Compromise of 1877 with Claude

- Source: history-us-history/chapters/16-the-era-of-reconstruction-1865-1877.md
- Lane: RESEARCH (Claude assistant)
- Hook: C. Vann Woodward's 1951 thesis on the Compromise of 1877 shaped how a generation understood Reconstruction's end. More recent historians have contested it. Claude knows Woodward — does it know the revision?
- The artifact: A sourced 3-section research brief — (1) Woodward's 1951 thesis: what the Compromise was, who the parties were, what Hayes agreed to; (2) the revisionist challenge: which specific claims have been contested and by which historians (dates, names, publications); (3) what the current historiographical consensus is, with 2 secondary sources that post-date Woodward. Each section flags whether Claude's response names the key figures and the revision correctly.
- Prompt seed: `claude "What is the Compromise of 1877, and how has the historiography of it shifted since C. Vann Woodward's 1951 thesis? Name: (1) what Woodward argued, (2) specific historians who have contested it, (3) what aspects of Woodward's thesis remain accepted and what has been revised. Cite by author, year, and publication venue."`
- Read / check: Verify that Claude names Woodward's thesis correctly (a backroom deal ending Reconstruction); verify at least one revisionist historian is named (Michael Holt, Keith Polakoff, or others — check the specific argument attributed); flag if Claude fabricates a historian or misattributes a revision. The textbook's own treatment of Reconstruction provides the baseline.
- Human supplies: Nothing — Claude synthesizes. Human must verify at least 1 post-Woodward secondary source citation by publication venue.
- Output medium: Remotion slate (3-section brief: Woodward thesis, revision, current consensus; comparison table: original claim / contested by / current status)
- The change: Run the same question with two different models (Claude and one other available LLM). Compare where they agree and where they diverge on the revisionist challenge. The divergence is diagnostic — it flags where the historiography is genuinely contested vs. where one model's training data is thin.
- Teardown angle: The Woodward test is a model-evaluation tool: an informed prompt about a known historiographical debate lets you see whether the model's response tracks the actual state of historical scholarship or smooths over contested terrain. "Specifying" the question is what surfaces the revision.
- Exclusions: Skip the full Reconstruction history; skip the Civil Rights movement connection; do not attempt to settle the historiographical debate.
- Score: 9/10

---

## Candidate 03 — Build a Primary Source Verification Tool with Claude

- Source: history-us-history/chapters/00-claude-basics.md
- Lane: BUILD (Claude Code)
- Hook: Claude produces a confident sentence with a date, a casualty count, and a quotation. Three things. How many can you verify in under 5 minutes? Here is a workflow that makes verification systematic — and fast.
- The artifact: A screen-recording mp4 — a 3-step verification workflow applied to a Claude-generated paragraph about the Battle of Gettysburg: (1) extract the verifiable claims (dates, numbers, quotations) using `claude "list every verifiable factual claim in this paragraph as a numbered list: [paste paragraph]"`; (2) for each claim, run a targeted verification prompt with the chapter's "specify-compare-verify" discipline; (3) mark each claim as verified, unverified, or contested. The output is an annotated version of the original paragraph with verification status inline.
- Prompt seed: `claude "Generate a 150-word summary of the Battle of Gettysburg (July 1-3, 1863) including: dates, commanding generals, approximate casualties, and the outcome for the Confederacy's invasion strategy."` → then `claude "List every verifiable factual claim in this paragraph as a numbered list. For each, identify the type of claim: date, number, causal attribution, or quotation."` → then verify 3 claims against Library of Congress / NPS sources.
- Read / check: Verify that the claim-extraction prompt produces a specific list (not "the paragraph contains facts"); confirm that at least 1 claim is verifiable against a real primary/secondary source in under 5 minutes; check that the verification status annotation is clear (green/yellow/red or equivalent). This is a real Claude session.
- Human supplies: Nothing — Claude generates and verifies. Human must check at least 1 claim against the American Battlefield Trust or Library of Congress website (2 minutes). Flag if Claude's initial summary contains a contested or wrong claim.
- Output medium: screen-recording mp4 (two-pane: original paragraph on left, verification workflow on right, claim status annotations appearing)
- The change: Re-run the workflow on a paragraph where Claude is known to confabulate — Andrew Jackson's Florida governorship dates (the chapter's worked example). Show the claim-extraction step surface the contested date, the verification step catch the error, and the annotated paragraph marking it as "flagged — verify against primary source."
- Teardown angle: The three moves (specify, compare, verify) from the textbook chapter are operational: specify the prompt to get checkable claims, compare across prompts to surface divergence, verify the divergent claims against primary sources. The workflow makes the moves mechanical so they become habit.
- Exclusions: Skip the full Gettysburg history; skip automated fact-checking tools; do not attempt to verify every claim in the paragraph (pick 3 to demonstrate the workflow).
- Score: 9/10

---

## Candidate 04 — Research the Sambasivan Data Quality Claim for Historians with Claude

- Source: history-us-history/chapters/00-claude-basics.md (Claude's confabulation mechanism)
- Lane: RESEARCH (Claude assistant)
- Hook: Claude is a confabulator — it fills gaps with fluent, confident, frequently-wrong text. This is not occasional; it is structural. What does the evidence say about how often LLMs confabulate in historical domains specifically?
- The artifact: A sourced 3-section brief — (1) the confabulation mechanism: how next-token prediction produces plausible-but-wrong historical claims; (2) empirical evidence: studies measuring LLM accuracy on historical fact claims (dates, casualty counts, treaty texts); (3) a practitioner guide: the 3 types of historical claims most likely to confabulate (specific numbers, quotations, and lesser-known events) vs. types least likely (major events well-covered in training data).
- Prompt seed: `claude "Research the empirical evidence on how often large language models produce inaccurate historical claims ('hallucination' or 'confabulation'). Find: (1) studies measuring LLM historical accuracy, (2) which types of historical claims are most error-prone (dates, quotations, casualty numbers, obscure events), (3) whether the error rate differs between well-documented events (major battles) and lesser-known events. Cite studies by author, year, and venue. Flag if evidence is primarily anecdotal rather than systematic."`
- Read / check: Verify at least 1 systematic study is cited (not just blog posts or anecdotal examples); flag if Claude confabulates a citation about its own confabulation (a recursively entertaining failure mode); check that the practitioner guide distinguishes types of claims correctly.
- Human supplies: Nothing — Claude synthesizes. Human verifies at least 1 citation. Note: this topic may yield limited peer-reviewed evidence — that gap is a finding worth reporting.
- Output medium: Remotion slate (3-section brief: mechanism, evidence, practitioner guide — with a "high-risk claim types" table)
- The change: Run the same question on a second model and compare the evidence each surfaces. The comparison is a demonstration of the "compare" move from the textbook chapter — the divergence shows where the evidence is thin.
- Teardown angle: The textbook is honest about the mechanism: fluency and accuracy come from the same machinery, and the machinery cannot tell them apart. The confabulation problem is not fixable by prompting alone — it requires the verify step. The research brief documents the evidence so the viewer can calibrate their own trust level.
- Exclusions: Skip the full AI safety / alignment literature; skip the philosophical debate about what "hallucination" means; do not attempt to benchmark Claude yourself.
- Score: 8/10

---

## Candidate 05 — Build a Comparative Timeline: Reconstruction to Civil Rights with Claude

- Source: history-us-history/chapters/16-the-era-of-reconstruction-1865-1877.md + chapters/29-contesting-futures-america-in-the-1960s.md
- Lane: RESEARCH (Claude assistant)
- Hook: Reconstruction established civil rights protections that were rolled back. The Civil Rights Movement re-established protections a century later. Can Claude build a comparative timeline that shows what was gained, lost, and regained — and what the research says was new?
- The artifact: A Remotion animated comparative timeline — two horizontal tracks: (1) Reconstruction track (1865–1877): 13th, 14th, 15th Amendments; Freedmen's Bureau; Black Congressmen elected; Compromise of 1877; (2) Civil Rights track (1954–1968): Brown v. Board; Civil Rights Act 1964; Voting Rights Act 1965; Fair Housing Act 1968. Each event appears as a node with a 1-sentence annotation. Vertical lines connecting analogous events (e.g., 15th Amendment ↔ Voting Rights Act 1965) with "gap: 95 years" annotated.
- Prompt seed: `claude "Build a comparative timeline of Reconstruction (1865-1877) and the Civil Rights Movement (1954-1968) focusing on legal and political milestones. For each period: list 6 key events with dates. Then identify 3 pairs of analogous events (one from each period) and for each pair: describe what was gained in Reconstruction, how it was rolled back, and how it was re-established. Cite the specific legislation or court case for each event."`
- Read / check: Verify the 6 Reconstruction events are real and dated correctly; verify the 6 Civil Rights events are real and dated correctly; check that the 3 analogous pairs are historically coherent (voting rights is the clearest pair); flag if Claude omits the rollback phase (Jim Crow, Plessy v. Ferguson) which is essential to the comparative structure.
- Human supplies: Nothing — Claude synthesizes. Human verifies at least 3 dates against the textbook's timeline chapters.
- Output medium: Remotion (animated two-track horizontal timeline, events appearing as nodes in date order, vertical connecting lines with gap annotations)
- The change: Add a third track (1877–1954) showing the rollback mechanisms (convict leasing, poll taxes, literacy tests, Plessy). Show how the three-track timeline makes the "gap" visible as a period of active reversal, not passive absence.
- Teardown angle: The LLM's training distribution contains both the Reconstruction and the Civil Rights Movement, but the connection between them — the specific mechanisms of rollback — is less consistently represented. The comparative research brief is exactly the task where the "specify" and "verify" discipline catches the model eliding the middle act.
- Exclusions: Skip the full historiography of each period; skip the Compromise of 1877 detail (covered in card 02); do not attempt a comprehensive civil rights timeline (pick the 6 most analogous events per period).
- Score: 8/10

---

## Candidate 06 — Research the New Deal Coalition with Claude

- Source: history-us-history/chapters/26-franklin-roosevelt-and-the-new-deal-1932-1941.md
- Lane: RESEARCH (Claude assistant)
- Hook: The New Deal coalition — urban workers, Southern Democrats, Black voters, and progressives — elected FDR four times. It also contained deep internal contradictions. Can Claude describe both the coalition and its contradictions accurately?
- The artifact: A sourced 3-section brief — (1) the New Deal coalition's components: who was included, what each group wanted, what they got; (2) the internal contradictions: Southern Democrats demanded exclusion of Black workers from key programs (Social Security, Wagner Act) — does Claude report this accurately?; (3) when and why the coalition collapsed (post-1968 — the Southern strategy, Vietnam, social issues). A verification test: does Claude accurately report the racial exclusions in the Social Security Act of 1935?
- Prompt seed: `claude "Describe the New Deal coalition that elected Franklin Roosevelt. Include: (1) the major constituencies, (2) what each constituency gained from New Deal policies, (3) the internal racial contradictions — specifically, which New Deal programs excluded Black workers and why, (4) when and why the coalition began to fracture. Cite specific legislation and historical evidence for the racial exclusions."`
- Read / check: Verify the Social Security Act exclusion is reported correctly (domestic workers and agricultural workers excluded at Southern Democrats' insistence, disproportionately Black); verify the Wagner Act exclusion is reported correctly (same mechanism); check that the coalition collapse dates to the 1960s–1970s, not earlier. Flag if Claude omits the racial exclusions entirely (a known soft spot in the training distribution's representation of this history).
- Human supplies: Nothing — Claude synthesizes. Human verifies the Social Security exclusion against the textbook chapter and at least 1 secondary source.
- Output medium: Remotion slate (3-section brief: coalition composition table, contradictions section, collapse timeline)
- The change: Add a second prompt asking Claude to list the New Deal programs that did NOT discriminate racially. Compare the two lists — the ratio of inclusive vs. exclusive programs is itself a historical argument. Does Claude's list match the historical record?
- Teardown angle: The racial exclusions are in the training data — they are documented in multiple secondary sources. Whether Claude surfaces them depends heavily on how the question is framed. The "specify" discipline (explicitly asking about racial exclusions) is what makes the model report what it knows but might not volunteer.
- Exclusions: Skip the full New Deal economic history; skip the comparative international context; do not attempt to evaluate the economic effectiveness of New Deal programs.
- Score: 8/10

---

## Candidate 07 — Probe the Model's Consistency: Same Question, Three Phrasings

- Source: history-us-history/chapters/00-claude-basics.md
- Lane: BUILD (Claude Code)
- Hook: Ask "Was the Battle of New Orleans fought before or after the War of 1812 ended?" Then ask "What was the significance of the Battle of New Orleans?" in a fresh session. Are the answers consistent? The textbook says: look at what changes.
- The artifact: A screen-recording mp4 — three terminal sessions, same historical question, three phrasings, one after another: (1) "What happened at the Battle of New Orleans?"; (2) "Was the Battle of New Orleans fought before or after the War of 1812 ended?"; (3) "Why did the Battle of New Orleans matter despite being fought after the peace treaty?" Each response pasted into a side-by-side comparison doc. Differences annotated: which version mentions the timing wrinkle, which omits it, which gets the political consequence right.
- Prompt seed: Three prompts run in fresh Claude sessions: version A (open), version B (timing-probing), version C (conceding-timing-and-asking-why). Responses recorded.
- Read / check: Verify that version B forces Claude to acknowledge the treaty preceded the battle; check whether version A mentions the timing spontaneously (it may not); confirm version C produces a coherent answer about political consequences even after acknowledging timing. This is a real Claude session — the output is the data.
- Human supplies: Nothing — Claude generates. Human records the three responses (screenshots or copy-paste) and annotates the differences. A real terminal or Claude API session is needed; this is not a synthetic demo.
- Output medium: screen-recording mp4 (three-pane side-by-side comparison, differences annotated with text overlays, differences highlighted)
- The change: Run a fourth phrasing that contains a false premise: "Why did the Battle of New Orleans fail to decisively end the War of 1812?" Show whether Claude corrects the false premise or constructs a plausible-sounding answer to the wrong question. The chapter predicts the latter.
- Teardown angle: The "compare" move is empirical: the same model, asked three ways, produces three answers. The differences are diagnostic — they reveal where the model's training distribution is thin (the timing wrinkle) and what the model will generate when the premise is false. This is the research discipline applied to the tool itself.
- Exclusions: Skip the full model-evaluation literature; skip comparing across multiple models in this card (covered in cards 01 and 04); do not attempt to draw conclusions about Claude's general accuracy from 3 questions.
- Score: 9/10

---

## Candidate 08 — Build a Running Historical Research Project with Claude

- Source: history-us-history/chapters/00-claude-basics.md (the LLM exercise structure across all chapters)
- Lane: BUILD (Claude Code)
- Hook: Every chapter in this textbook ends with a prompt that contributes to one running project. What if you built the whole project structure with Claude — a research portfolio that accumulates across 32 chapters — in one session?
- The artifact: A screen-recording mp4 — using Claude to scaffold a 32-chapter research project structure: (1) `claude "Design a historical research portfolio structure for a US history student using AI tools. The portfolio should accumulate across 32 chapters. Include: a master claims tracker (verified/unverified/contested), a source log (primary vs. secondary), a model-consistency log (how different phrasings produced different answers), and a final synthesis section"` → review and refine; (2) generating the folder structure and template files; (3) running the Battle of New Orleans verification from card 01 and entering the result into the claims tracker.
- Prompt seed: `claude "Design a research portfolio template for a US history course where each chapter contributes one entry. The portfolio tracks: (1) one verified primary-source claim per chapter, (2) one instance of model inconsistency or confabulation caught and corrected, (3) one historiographical debate researched. Generate a folder structure and a markdown template for each chapter's entry."`
- Read / check: Verify the template has all 3 required sections; confirm the folder structure is usable (not overly complex for a student); check that the claims-tracker template distinguishes primary from secondary sources. This is a real Claude session.
- Human supplies: Mac/Linux terminal for file creation; a text editor. The portfolio scaffolding is the deliverable — human reviews legibility and usability.
- Output medium: screen-recording mp4 (two-pane: Claude output on left, folder structure materializing on right, template file opening)
- The change: Run one chapter's entry end to end — the Battle of New Orleans — through the template. Show what a completed chapter entry looks like (verified claim, consistency test result, historiographical note). The completed entry is the model for all 32 chapters.
- Teardown angle: The portfolio is the student's artifact from using Claude as an instrument, not an oracle. It accumulates evidence of the discipline: primary sources cited, confabulations caught, historiographical debates engaged. The project structure is the conducting framework applied to historical research.
- Exclusions: Skip version control for the portfolio; skip automated claim extraction; do not attempt to build the full 32-chapter portfolio in the demo.
- Score: 8/10

---

## Candidate 09 — Research Westward Expansion's Contested History with Claude

- Source: history-us-history/chapters/11-a-nation-on-the-move-westward-expansion-1800-1860.md + chapters/17-go-west-young-man-westward-expansion-1840-1900.md
- Lane: RESEARCH (Claude assistant)
- Hook: Manifest Destiny is in every textbook. The specific mechanisms of Indigenous dispossession — the treaties broken, the populations displaced, the legal arguments constructed — are less consistently represented. Does Claude know the difference?
- The artifact: A sourced 3-section brief — (1) the standard narrative of westward expansion (what Claude produces when asked about Manifest Destiny without specification); (2) the mechanisms of Indigenous dispossession: Indian Removal Act, Treaty of New Echota, Trail of Tears — does Claude report these accurately and with casualty context?; (3) the historiographical shift: how the "frontier thesis" (Turner, 1893) has been revised by New Western History (Limerick, White, others). A verification column: which claims are primary-source-verifiable vs. secondary-interpretation.
- Prompt seed: `claude "Describe the mechanisms of Indigenous dispossession during US westward expansion 1800-1860. Include: (1) the legal and legislative mechanisms (Indian Removal Act, specific treaties), (2) estimated population impacts and displacement numbers, (3) how historians have revised the 'frontier thesis' since Frederick Jackson Turner's 1893 essay. Distinguish between primary-source-verifiable facts and historical interpretations. Cite sources."`
- Read / check: Verify the Indian Removal Act date (1830 — real); verify the Treaty of New Echota (1835 — real, signed by a minority of Cherokee leaders); check the Trail of Tears mortality estimate is given as a range (contested — typically cited as 4,000–8,000 of 16,000 relocated); flag if Claude presents Turner's thesis without naming the New Western History revision.
- Human supplies: Nothing — Claude synthesizes. Human verifies at least 2 dates against the textbook chapters.
- Output medium: Remotion slate (3-section brief: standard narrative, dispossession mechanisms table, historiographical revision section)
- The change: Run a comparison between a prompt that uses "Manifest Destiny" as the framing and one that uses "Indigenous dispossession" as the framing. Show how the framing changes what Claude foregrounds — the same history, two different entry points, two different emphases.
- Teardown angle: The framing effect is structural: the LLM responds to the most salient terms in the prompt by generating the most statistically likely continuation from those terms' co-occurrence patterns in training. "Manifest Destiny" foregrounds American expansion; "Indigenous dispossession" foregrounds a different part of the same history. The discipline is choosing the framing deliberately.
- Exclusions: Skip the full New Western History bibliography; skip the contemporary policy implications; do not attempt to cover post-1860 westward expansion in this card.
- Score: 8/10

---

## Candidate 10 — Research the Great Depression: What the Numbers Actually Show

- Source: history-us-history/chapters/25-brother-can-you-spare-a-dime-the-great-depression-1929-1932.md
- Lane: RESEARCH (Claude assistant)
- Hook: Unemployment hit 25% in 1933. The Dow Jones fell 89% from 1929 to 1932. Bank failures numbered over 9,000 by 1933. Claude will cite numbers like these — but which ones are well-documented and which are contested estimates?
- The artifact: A sourced 4-section brief — (1) the verified economic indicators: stock market drop (documented by Dow Jones data), bank failures (FDIC historical data), unemployment rate (Bureau of Labor Statistics historical series); (2) the contested estimates: GDP contraction figures, actual vs. reported unemployment; (3) the human cost figures: displacement, migration, health impacts — how are these measured and how contested are they?; (4) a primary source list: where to find the original economic data for each indicator.
- Prompt seed: `claude "For the Great Depression (1929-1933), provide the key economic statistics with their sources. For each statistic: (1) the number, (2) the primary data source it comes from, (3) whether historians consider it reliable or contested. Include: unemployment rate peak, Dow Jones decline, bank failures, GDP contraction. Flag any statistics that are frequently cited but poorly documented."`
- Read / check: Verify unemployment peak is given as ~25% with the caveat that measurement was different in 1933 (no BLS survey — figures reconstructed by Lebergott and others); verify Dow Jones decline (~89%) is documented; check that bank failures are cited with a source (FDIC historical data exists). Flag if Claude presents reconstruction-era estimates as if they are original statistical surveys.
- Human supplies: Nothing — Claude synthesizes. Human verifies the unemployment measurement methodology caveat against at least 1 secondary source (the measurement debate is real and important).
- Output medium: Remotion slate (4-section brief: verified indicators, contested estimates, human cost, primary source list — with a "reliability rating" column in the indicators table)
- The change: Ask Claude to find the most commonly cited Great Depression statistic that is most likely to be imprecise or contested. This forces Claude to evaluate its own output — a meta-verification exercise that demonstrates the "specify" move applied to quality, not just accuracy.
- Teardown angle: Economic history is full of statistics that feel precise but are reconstructed estimates. The discipline of distinguishing primary data from secondary reconstruction is exactly the historian's craft applied to numbers — and exactly the skill the "specify-compare-verify" workflow develops.
- Exclusions: Skip the full economic history of the Depression; skip the international comparative context; do not attempt to verify all statistics independently in the demo.
- Score: 7/10

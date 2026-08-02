# US History with LLMs — CLI Video Ideas ("X with Claude")

<!-- cli-scout | RESEARCH | 2026-07-12 -->

---

## Card 1 — Emancipation Proclamation Scope Verification: What the LLM Almost Always Gets Wrong

**Source:** us-history-with-llms / Ch 15 – The Civil War (LLM Exercise)  
**Lane:** RESEARCH  
**Hook:** Ask any LLM "What did the Emancipation Proclamation do?" and you'll get a confident, wrong answer. It did not free all enslaved people. It freed enslaved people only in Confederate states — and only those still in rebellion. Claude can show you exactly where the misdescription appears and why it persists.  
**The artifact:** A sourced brief comparing what the Emancipation Proclamation actually states (from the primary document) against four LLM responses, annotating each deviation: scope errors (Union slave states excluded), timing errors (effective January 1, 1863, not at signing), agency errors (it did not immediately free anyone in Confederate territory). The brief includes the primary source text and three secondary sources rating the EP as a war measure, not a universal emancipation order.  
**Prompt seed:** "I want to test how you describe the Emancipation Proclamation. Without using external sources, explain: (1) which states were affected, (2) which states were explicitly excluded, (3) what the practical effect was on enslaved people in Union-held territory in Confederate states, and (4) what legal mechanism actually ended slavery in all states. After your response, I will check each claim against the primary document."  
**Read/check:** Primary source: Executive Order, January 1, 1863. Excluded states: Delaware, Kentucky, Maryland, Missouri (border states never in rebellion), West Virginia, and specific named parishes in Louisiana and counties in Virginia already under Union control. The 13th Amendment (December 1865) is the mechanism that ended slavery universally. The book identifies the EP misdescription as the most reliable LLM error in the entire US history curriculum.  
**Human supplies:** Access to the EP primary text (available at archives.gov), four LLM responses to a standardized prompt, note-taking on discrepancy types.  
**Output medium:** Manim animated slate: a map of the US showing Confederate states in one color, Union states in another, and explicitly excluded territory highlighted — visually demonstrating what the EP actually covered. The map builds beat by beat as claims are verified or refuted. Screen-recording mp4 of the verification run.  
**The change:** Students stop accepting LLM summaries of primary documents at face value. They learn to run the primary-text-against-LLM-response verification workflow that the book's LLM Exercise prescribes — applicable to any contested historical document.  
**Teardown angle:** Show the verification logbook workflow: standardized prompt → LLM response → primary source comparison → annotation → correction. Run it on three different LLMs (Claude, GPT, Gemini). Compare which deviations are shared across all three (systematic training bias) vs. which are idiosyncratic.  
**Exclusions:** Do not address the political context of why LLMs flatten this document — focus entirely on the verification workflow and the factual discrepancies. The "why" is a separate inquiry.  
**Score:** 9/10

---

## Card 2 — Compromise of 1877 Historiographic Drift: What the LLM Learned from Woodward, Not from Subsequent Historians

**Source:** us-history-with-llms / Ch 16 – The Era of Reconstruction (LLM Exercise)  
**Lane:** RESEARCH  
**Hook:** C. Vann Woodward published his "Compromise of 1877" thesis in 1951. Subsequent historians (Peskin, Polakoff, Foner) have substantially qualified it. LLMs learned from the textbooks, not the revisions. Claude can show you exactly which vintage of historiography your LLM is reproducing.  
**The artifact:** A sourced comparison brief: Woodward's original thesis (Hayes presidency for troop withdrawal as a clean bargain) vs. the qualified consensus (multiple parallel negotiations, the railroad subsidies never materialized, the end of Reconstruction was a four-year process not a single deal). Brief includes page citations from Foner's *Reconstruction* (1988) and identifies which elements of the Woodward thesis LLMs reliably reproduce verbatim.  
**Prompt seed:** "Explain the Compromise of 1877 and how it ended Reconstruction. Then tell me: how have historians' views of this event changed since C. Vann Woodward's 1951 account in *Reunion and Reaction*? What do Peskin (1973), Polakoff (1973), and Eric Foner (1988) add or revise?" Run without the follow-up to test the default response, then with the follow-up to test whether the LLM can access the revision.  
**Read/check:** Woodward's thesis: coordinated deal, Hayes gets presidency, South gets troop withdrawal plus railroad subsidies plus cabinet seat. The qualifications: negotiations were fragmented not unified; Texas and Pacific Railway subsidies never passed; Foner's argument that the 1876–77 events were the ratification of a retreat begun in 1873, not its cause. The Colfax Massacre (1873) and *United States v. Cruikshank* (1876) as the structural mechanisms that preceded and made the Hayes withdrawal possible.  
**Human supplies:** Woodward's *Reunion and Reaction* (page citations), Foner's *Reconstruction* (pp. 575–582), standardized LLM test prompt.  
**Output medium:** Manim animated timeline: 1865 to 1877 as a horizontal axis. Events appear in sequence (Reconstruction Acts, Colfax Massacre, Panic of 1873, *Cruikshank*, 1876 election, Electoral Commission, Wormley Hotel, troop withdrawal). The Woodward "bargain" framing draws a single arrow at 1877; the Foner process framing draws a gradient fade beginning at 1873. The visual contrast makes the historiographic argument legible.  
**The change:** Students learn that LLM historical summaries are not neutral — they reflect whichever interpretation dominated at the time of training-data cutoff. The methodology generalizes to any contested historical event with a long scholarly debate.  
**Teardown angle:** Run the "tell me about the Compromise of 1877" prompt on three LLMs. Score each response on six elements: (1) does it name Woodward? (2) does it mention the qualified consensus? (3) does it flag that railroad subsidies never materialized? (4) does it describe Reconstruction's end as a process rather than an event? (5) does it mention Colfax? (6) does it cite Foner? Build a comparison table. Typical result: 0–1 of 6.  
**Exclusions:** Do not address the politics of how Reconstruction ended — the card is about historiographic drift and LLM training-data vintage, not about the substantive political history.  
**Score:** 9/10

---

## Card 3 — Pre-Columbian Population Claims: Verify What the LLM Says Against the Primary Scholarly Debate

**Source:** us-history-with-llms / Ch 01 – The Americas, Europe, and Africa Before 1492 (LLM Exercise)  
**Lane:** RESEARCH  
**Hook:** "Between 50 and 100 million people." "Perhaps 10 million." LLM responses on pre-Columbian North American population range by a factor of 10. The scholars disagree too — but in a structured way that LLMs flatten into false confidence.  
**The artifact:** A verification logbook entry documenting the scholarly range (Dobyns 1983: 90–112 million for the entire hemisphere; Ubelaker 1976: 2.1 million for North America north of Mexico; Thornton 1987: 7+ million; the current consensus range of 40–100 million for the hemisphere) against LLM responses, noting which estimate each LLM anchors to and whether it acknowledges the genuine scholarly controversy. Output: a sourced brief with annotated claim-by-claim comparison.  
**Prompt seed:** "What was the population of the Americas before European contact? Provide your best estimate with a range, name at least two historians or demographers whose estimates differ significantly from each other, and tell me why the estimates vary so widely."  
**Read/check:** The demographic debate turns on: (1) the role of epidemic disease in destroying population evidence before systematic European record-keeping began, (2) whether to use contact-era counts (severely undercount due to prior epidemics) vs. epidemiological back-calculation, (3) which geographic area is being measured (hemisphere vs. North America only). Dobyns's 90M figure is an outlier; Ubelaker's 2.1M is a low-end outlier; the current scholarly consensus clusters around 40–80M for the hemisphere. The book identifies this as a key LLM-distortion site.  
**Human supplies:** Access to three LLM interfaces for comparative testing, note-taking on numerical claims and uncertainty language used.  
**Output medium:** Manim animated dot-density map: start with the Ubelaker estimate (sparse dots), grow to the Thornton estimate, grow to the Dobyns estimate — visually representing the range of the debate. Each LLM's anchor point appears as a marker on the scale. Screen-recording mp4 of the verification session.  
**The change:** Students stop treating a single LLM number as settled history. They learn to ask: (1) which estimate is this LLM using? (2) does it acknowledge the controversy? (3) can I name the methodological source of the disagreement? The verification skill generalizes to any claim where the evidence base is genuinely contested.  
**Teardown angle:** Run the same prompt on Claude, GPT-4, and Gemini. Compare: which number does each anchor to? Does any acknowledge the Dobyns-Ubelaker range? Does any explain *why* estimates vary so much? Most LLMs will produce a number in the 50–100M range without citing any specific historian or explaining the methodological controversy.  
**Exclusions:** Do not address the downstream political uses of population estimates (reparations debates, land-rights arguments) — the card is strictly about the verification methodology and the structure of scholarly disagreement.  
**Score:** 8/10

---

## Card 4 — Civil War Causes "States' Rights" Framing: Source-Triangulate the Secession Documents

**Source:** us-history-with-llms / Ch 15 – The Civil War (LLM Exercise)  
**Lane:** RESEARCH  
**Hook:** "The Civil War was about states' rights." Ask an LLM for a nuanced answer and it will often hedge in a way that lends credence to the framing. Ask it to read the actual Confederate secession declarations and it finds something different. The primary sources are unambiguous. The LLM's "balance" is not.  
**The artifact:** A source-triangulation brief: three Confederate states' declarations of secession (South Carolina, Mississippi, Texas) analyzed for explicit references to slavery vs. abstract "states' rights" language. Brief documents the frequency and placement of slavery references, quotes the most direct passages, and compares against typical LLM responses that use both-sides framing. Includes the Confederate Constitution's explicit slavery protection provisions.  
**Prompt seed:** "I want to understand what Confederate secession declarations say about the causes of secession. Read the South Carolina Declaration of the Causes of Secession (December 1860) and the Mississippi Declaration (January 1861). What proportion of each document is devoted to slavery specifically vs. other grievances? Quote the three most explicit statements about slavery from each."  
**Read/check:** South Carolina Declaration (December 24, 1860): opens with slavery, names slavery as the central grievance in paragraph 3, spends the majority of the document on slavery-related federal failures. Mississippi Declaration (January 9, 1861): opening sentence — "Our position is thoroughly identified with the institution of slavery — the greatest material interest of the world." Texas Declaration (February 2, 1861): explicit white-supremacist language alongside slavery protection. Both are primary documents available at Yale's Avalon Project.  
**Human supplies:** URLs for the three secession declarations (Avalon Project, Yale Law School), access to an LLM for the triangulation test.  
**Output medium:** Manim animated word-frequency visualization: the secession declarations rendered as colored text where slavery-related words glow one color and abstract-rights language glows another. The color balance makes the argument visible without requiring the viewer to read 2,000 words. Screen-recording mp4 of the source-triangulation session.  
**The change:** Students learn to source-triangulate contested historical claims by going directly to the primary documents — not relying on LLM synthesis that may reflect post-hoc Lost Cause historiography absorbed through training data.  
**Teardown angle:** Run the "nuanced answer" prompt first: ask an LLM to explain the Civil War causes "fairly." Note how much space it gives to states' rights framing. Then run the document-analysis prompt with the actual declarations attached. Compare the two responses: does the document-grounded response match the "balanced" response?  
**Exclusions:** Do not address Confederate monument debates or modern political arguments — the card is strictly about the primary-document verification methodology and what the secession declarations actually say.  
**Score:** 8/10

---

## Card 5 — Battle of New Orleans Timing: Verify the Treaty vs. Battle Sequence

**Source:** us-history-with-llms / Ch 08 – Growing Pains: The New Republic (LLM Exercise framework)  
**Lane:** RESEARCH  
**Hook:** The Battle of New Orleans (January 8, 1815) was fought after the Treaty of Ghent was signed (December 24, 1814). Andrew Jackson won the most decisive American land battle of the war — for a war that was already over. Ask an LLM whether news traveled fast enough for either side to know, and watch it confabulate.  
**The artifact:** A sourced timeline brief: (1) Treaty of Ghent signed December 24, 1814 in Belgium; (2) news required approximately six weeks to cross the Atlantic; (3) Battle of New Orleans fought January 8, 1815 — fifteen days after the treaty signing; (4) US Senate ratified the treaty February 16, 1815. Brief documents whether the battle affected the treaty terms (it did not — terms were negotiated before either side knew the battle outcome) and compares against LLM responses that confuse the sequence.  
**Prompt seed:** "Walk me through the exact sequence: when was the Treaty of Ghent signed, when was the Battle of New Orleans fought, when did news of the treaty reach the combatants, and when did the US Senate ratify the treaty? Did the outcome of the Battle of New Orleans affect the treaty terms?"  
**Read/check:** Treaty of Ghent signed: December 24, 1814. Battle of New Orleans: January 8, 1815 (American forces under Jackson defeat British forces under Pakenham; Pakenham killed; British suffer ~2,000 casualties, Americans ~70). Treaty news reached New York: February 11, 1815. Senate ratification: February 16, 1815. The treaty restored pre-war territorial boundaries (status quo ante bellum) — negotiated independently of the battle. Jackson's victory became politically powerful precisely because Americans learned about the treaty and the victory simultaneously, making it feel like a decisive war-winning battle.  
**Human supplies:** Dates from Fred Hickey's *The War of 1812: A Short History* or Donald Hickey's *Don't Give Up the Ship* (2006), access to LLM for verification test.  
**Output medium:** Manim animated timeline: horizontal axis from November 1814 to March 1815. Treaty signing, battle, Atlantic crossing of news (shown as a ship moving across an ocean strip), Senate ratification. The visual makes the timing paradox immediately legible. Screen-recording mp4 of the verification session.  
**The change:** Students internalize the book's core lesson about LLM temporal flattening: LLMs compress sequences, confuse causation direction, and often suggest that contemporaries knew what we know retrospectively. The timing-verification habit applies to any event where communication lag matters.  
**Teardown angle:** Ask three LLMs: "Did the Battle of New Orleans change the outcome of the War of 1812?" Compare the answers. Most will either say yes (wrong — the treaty was already signed) or give a hedged answer that implies it contributed. Use the sourced timeline to show what "the war was already over" actually means.  
**Exclusions:** Do not address the broader War of 1812 narrative — this is a precision timing-verification exercise, not a full account of the war.  
**Score:** 8/10

---

## Card 6 — Great Depression Structural Causes: Test the "Stock Market Crash" Confabulation

**Source:** us-history-with-llms / Ch 25 – Brother, Can You Spare a Dime (LLM Exercise)  
**Lane:** RESEARCH  
**Hook:** "The stock market crash of 1929 caused the Great Depression." It did not — it triggered it. The Depression was produced by Federal Reserve monetary contraction, gold-standard maintenance, and counterproductive tariff policy over the following four years. LLMs reliably reproduce the popular framing. Claude can help you measure the gap between the popular summary and the economic-history consensus.  
**The artifact:** A sourced brief comparing the popular-framing LLM response against the economic-history literature (Friedman & Schwartz 1963, Temin 1976, Eichengreen 1992) on the four structural causes: monetary contraction, gold standard, underlying 1920s weaknesses, Smoot-Hawley tariff. Brief annotates which causal mechanisms each LLM acknowledges and which it omits.  
**Prompt seed:** "I am testing how LLMs describe the structural causes of the Great Depression beyond the popular framing of the stock-market crash. Without treating the crash as the primary cause, explain the role of: (1) Federal Reserve monetary policy 1929–1933, (2) the gold standard as a transmission mechanism, (3) the Smoot-Hawley tariff and its consequences, and (4) the pre-existing agricultural depression and income inequality. Cite specific historians for each claim."  
**Read/check:** Friedman & Schwartz (1963): Fed contracted money supply during the banking crisis instead of expanding — the principal avoidable cause. Temin (1976): spending-decline mechanism alongside monetary contraction. Eichengreen (1992): countries leaving gold standard early (Britain 1931, Japan 1931–32) recovered substantially faster than those maintaining gold parity. Smoot-Hawley: 1,000 economists signed petition against it; it passed anyway; retaliatory tariffs reduced US exports. US GNP fell ~30% from 1929–1933; unemployment reached ~25% by 1933.  
**Human supplies:** Basic familiarity with Friedman-Schwartz, Temin, Eichengreen (Wikipedia-level is sufficient as a starting frame for the verification logbook entry).  
**Output medium:** Manim animated causal diagram: the stock-market crash as one input arrow, the four structural mechanisms as parallel arrows, all feeding into the "Depression severity" outcome box. The popular framing shows only the crash arrow; the economic-history framing shows all five, with the crash as the smallest. Screen-recording mp4 of the sourcing session.  
**The change:** Students stop accepting single-cause narratives for complex economic events. The verification methodology — test LLM response against named historians — generalizes to any economic or political event with a developed specialist literature.  
**Teardown angle:** Ask three LLMs the simpler version: "What caused the Great Depression?" Count how many of the four structural mechanisms each names without prompting. Typical result: most name monetary policy (1 of 4), few name the gold standard (0–1 of 4), almost none name Smoot-Hawley's international transmission effect. Then ask the structured version with the four mechanisms named explicitly. Compare the quality of response.  
**Exclusions:** Do not cover the New Deal policy response — that is a separate chapter (Ch 26). This card covers only the 1929–1932 causal analysis.  
**Score:** 8/10

---

## Card 7 — Reconstruction "Three Projects" Disambiguation: Teach Claude to Disaggregate What "Failed"

**Source:** us-history-with-llms / Ch 16 – The Era of Reconstruction  
**Lane:** RESEARCH  
**Hook:** "Reconstruction failed." Every LLM says it. But *which* Reconstruction? Presidential Reconstruction collapsed in months. Congressional Reconstruction succeeded — the 13th, 14th, and 15th Amendments were ratified. Radical Reconstruction worked for a decade and was then reversed by organized violence. "Failed" erases this distinction. Claude can build a precision disambiguation tool.  
**The artifact:** A sourced comparison brief using the chapter's three-project framework: (1) Presidential Reconstruction (1865–1866) — what it attempted, why it collapsed; (2) Congressional Reconstruction (1866–1867) — the Civil Rights Act of 1866, 14th Amendment ratification, outcomes; (3) Radical Reconstruction (1867–1877) — what it achieved (8 Black members of Congress, democratic state constitutions, public education), how it was reversed (Klan violence, *United States v. Cruikshank* 1876, Panic of 1873, Electoral Commission 1876). Brief tests LLM responses against this three-project frame.  
**Prompt seed:** "Historians distinguish at least three separate political projects under the label 'Reconstruction': Presidential Reconstruction (1865–66), Congressional Reconstruction (1866–67), and Radical Reconstruction (1867–77). For each, tell me: what were its main goals, what did it achieve, and what caused it to end or be reversed? I will check your response against Eric Foner's *Reconstruction* (1988)."  
**Read/check:** Presidential Reconstruction: Johnson's pardons, Black Codes, Congress refused to seat Southern delegations. Congressional Reconstruction: Civil Rights Act 1866 (first congressional override of a presidential veto on major legislation), 14th Amendment. Radical Reconstruction: Military Reconstruction Acts, federal troops protecting Black voters, 8 Black men in Congress, state constitutions with public education and expanded women's rights — reversed by Klan violence, *Cruikshank* (withdrawing federal protection against private violence), Panic of 1873, 1876 electoral dispute.  
**Human supplies:** Eric Foner's *Reconstruction: America's Unfinished Revolution* (1988) for citation; access to LLM for testing.  
**Output medium:** Manim animated three-panel timeline: three parallel horizontal bars labeled Presidential / Congressional / Radical, each showing its duration, key events, and outcome (collapsed / succeeded / reversed). The visual makes clear that these are three distinct stories with three distinct outcomes — not one story that "failed."  
**The change:** Students learn to identify when a single label covers multiple distinct historical phenomena. The disambiguation skill — "which version of X are we talking about?" — applies to every contested historical label the book covers.  
**Teardown angle:** Ask three LLMs: "Did Reconstruction succeed or fail?" Note whether any distinguish the three projects. Most will produce a unified "failed" narrative. Then ask the structured three-project version. Compare depth and accuracy.  
**Exclusions:** Do not address post-Reconstruction Jim Crow or the long civil rights movement — this card ends at 1877.  
**Score:** 8/10

---

## Card 8 — Louisiana Purchase Constitutional Improvisation: Test LLM Consistency on "Strict Construction"

**Source:** us-history-with-llms / Ch 08 – Growing Pains: The New Republic  
**Lane:** RESEARCH  
**Hook:** Jefferson spent the 1790s arguing that the Constitution gave Congress no power to charter a bank — implied powers were dangerous. In 1803 he used implied powers to buy 828,000 square miles of land from Napoleon. He acknowledged in private that it was unconstitutional. Most LLMs either miss the contradiction or smooth it over.  
**The artifact:** A sourced brief documenting: (1) Jefferson's strict-construction argument against Hamilton's Bank of the United States (1791), (2) Jefferson's private acknowledgment in 1803 letters that the Louisiana Purchase exceeded constitutional authority, (3) the constitutional mechanism he used anyway (Senate treaty ratification + the necessary-and-proper clause), (4) LLM responses tested against these primary sources. Brief identifies whether each LLM acknowledges Jefferson's explicit constitutional improvisation.  
**Prompt seed:** "Jefferson strongly opposed Hamilton's implied-powers doctrine in the 1790s, arguing the federal government could only do what the Constitution explicitly authorized. In 1803, Jefferson purchased the Louisiana Territory. In his private correspondence, how did Jefferson describe the constitutional status of the purchase? Did he believe it was constitutional? What does his handling of this tension tell us about how constitutional principle operates in practice?"  
**Read/check:** Jefferson letters to John Breckinridge (August 12, 1803) and to Wilson Cary Nicholas (September 7, 1803): Jefferson explicitly wrote that he doubted the treaty was constitutional but proceeded anyway, proposing an after-the-fact constitutional amendment that he then abandoned when it became clear the Senate would ratify without one. The contradiction between his 1791 constitutional position and his 1803 action is documented in his own words.  
**Human supplies:** Jefferson's August 12 and September 7, 1803 letters (available through Library of Congress, Founders Online), access to LLM for testing.  
**Output medium:** Manim animated split-screen: left side shows Jefferson's 1791 argument (strict construction, no implied powers), right side shows his 1803 letter acknowledging the constitutional problem. An arrow connects them labeled "12 years later." The visual makes the tension legible in 10 seconds. Screen-recording mp4 of the verification session.  
**The change:** Students learn the book's recurring pattern: constitutional principle is often an instrument of political opposition that bends when the same coalition gains power. The verification skill — check stated principle against documented action — applies to constitutional interpretation debates throughout American history.  
**Teardown angle:** Ask an LLM: "Was the Louisiana Purchase constitutional?" Note whether it mentions Jefferson's private doubts. Most will describe the Purchase as legally settled and uncontroversial. Then provide Jefferson's own letters. Ask the LLM to reconcile the discrepancy between what Jefferson said in 1791 about implied powers and what he wrote in 1803.  
**Exclusions:** Do not address the implications of the Purchase for the expansion of slavery — that is a separate research thread that connects to Chapter 14 (Troubled Times).  
**Score:** 7/10

---

## Card 9 — LLM Temporal Flattening Demo: Show How LLMs Collapse Causation Direction

**Source:** us-history-with-llms / Ch 00 – Claude Basics (LLM Exercise framework)  
**Lane:** RESEARCH  
**Hook:** Chapter 00 names LLMs' most dangerous historical failure mode: they flatten temporal sequences, making later knowledge appear as earlier context. The Battle of New Orleans, the Compromise of 1877, the Emancipation Proclamation — all suffer from this. Claude can demonstrate the failure mode systematically and then show the fix.  
**The artifact:** A structured demonstration: five historical events where temporal sequence matters (Battle of New Orleans / Treaty of Ghent; Dred Scott / Republican Party formation; EP / 13th Amendment; *Plessy v. Ferguson* / *Brown*; *Slaughter-House Cases* / the 14th Amendment's equal-protection clause becoming primary). For each, a standardized LLM prompt; annotated response showing where the LLM implies contemporaries knew what came later; and a corrected version using the book's "specify / compare / verify" three-move framework.  
**Prompt seed:** "Describe the political reaction to the Dred Scott decision (1857). In your answer, indicate only what people in 1857–1858 could have known at the time — do not reference the 13th or 14th Amendments, the Civil War outcome, or any event after 1858." Then compare against an unconstrained prompt on the same topic.  
**Read/check:** The book's three failure modes: LLMs flatten temporal sequence (treating later events as context for earlier ones), soften violence (administrative language for massacres), and are least reliable on contested historiography. The "specify" move forces temporal constraint; the "compare" move checks multiple LLMs; the "verify" move goes to primary sources. The constrained prompt is the core pedagogical tool.  
**Human supplies:** Five historical event pairs (listed above), access to LLMs for both constrained and unconstrained versions.  
**Output medium:** Manim animated before/after comparison: the unconstrained LLM response shown as a timeline with anachronistic forward-knowledge highlighted in red; the constrained version shown as a clean timeline with no forward-knowledge violations. The red-highlighting is the lesson.  
**The change:** Students learn to use temporal constraint prompts as a standard tool — not just accepting LLM historical summaries, but explicitly asking: "Tell me only what people at that time could have known." The technique transfers to any historical topic.  
**Teardown angle:** Run the Dred Scott prompt both ways on the same LLM. In the unconstrained version, count how many references to post-1858 events appear (13th Amendment, Lincoln election, Civil War). In the constrained version, do they disappear? (Usually yes — the constraint works.) Moral: the problem is the prompt, not the model's fundamental capability.  
**Exclusions:** Do not build a full automated temporal-constraint system — this is a demonstration and pedagogical exercise, not a software tool.  
**Score:** 7/10

---

## Card 10 — Hoover Revisionism: Test Whether LLMs Have Absorbed "Did Nothing" as Settled Fact

**Source:** us-history-with-llms / Ch 25 – Brother, Can You Spare a Dime  
**Lane:** RESEARCH  
**Hook:** "Hoover did nothing." It's the popular framing, it's in the textbooks, and most LLMs reproduce it. But Hoover established the Reconstruction Finance Corporation, signed the Federal Home Loan Bank Act, and passed the Emergency Relief and Construction Act. The accurate verdict is "did the wrong things and not enough of the right things" — not nothing.  
**The artifact:** A sourced brief comparing the "did nothing" LLM response against the documented record of Hoover's interventions: RFC (January 1932), Glass-Steagall Act of February 1932 (distinct from the 1933 banking-separation act), Federal Home Loan Bank Act (July 1932), Emergency Relief and Construction Act (1932). Brief identifies which interventions LLMs consistently omit and why the "did nothing" frame, while politically coherent, is historically inaccurate.  
**Prompt seed:** "What did the Hoover administration do in response to the Great Depression between 1929 and 1933? Please name specific legislation and federal programs that Hoover signed or initiated, before describing what his administration did not do or refused to do."  
**Read/check:** RFC: established January 1932, authorized to lend to banks, insurance companies, railroads; continued operating through WWII. Glass-Steagall Feb 1932: allowed Fed to use government securities as collateral — expanded Fed lending capacity. Federal Home Loan Bank Act: established federal mortgage credit support. Emergency Relief and Construction Act 1932: $2B in federal lending to states. What Hoover refused: direct federal cash relief to individuals, large public-works employment programs, abandoning the gold standard.  
**Human supplies:** Basic familiarity with the RFC history, access to LLM for testing.  
**Output medium:** Manim animated two-column comparison slate: "What Hoover Did" (RFC, GLBA, FHLBA, ERCA — each appearing as a card with date and brief description) vs. "What Hoover Did Not Do" (direct relief, public employment, gold standard abandonment). The visual immediately corrects the binary framing without requiring narration to argue the case.  
**The change:** Students learn to distinguish "did nothing" (factually wrong) from "did inadequate and partly counterproductive things" (factually defensible). The precision matters for evaluating counterfactuals and for understanding what the New Deal actually built on vs. originated.  
**Teardown angle:** Ask three LLMs: "What did Hoover do to address the Depression?" Score each on whether it names the RFC, the February 1932 Glass-Steagall Act, and the FHLBA. Most will name the RFC (it's famous) and miss the other two. The omission pattern reveals which aspects of the historical record have and have not migrated into training data at sufficient density.  
**Exclusions:** Do not address FDR and the New Deal — this card ends with Hoover's departure in March 1933. The New Deal is Ch 26 territory.  
**Score:** 7/10

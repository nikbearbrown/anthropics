# AI for Writing: A Practitioner's Guide — CLI Video Ideas ("X with Claude")

## Candidate 01 — Build the Rhetoric Analyzer: Classify Persuasion Moves in Any Argument with Claude

- Source: ai-for-writing-a-practitioners-guide/chapters/11-rhetorical-analysis-interpreting-the-art-of-rhetoric.md
- Lane: BUILD (Claude Code)
- Hook: Every persuasive text uses the same handful of rhetorical moves. Most readers can't name them while reading. Build a tool that labels them in real time.
- The artifact: A screen recording of Claude analyzing a short opinion piece (500–800 words), generating a markdown table: paragraph number, rhetorical device identified (ethos/pathos/logos/kairos), evidence in the text, effectiveness rating (1–3), and a one-sentence explanation. The table renders as a D3-animated word-heat-map — paragraphs colored by dominant device.
- Prompt seed: `claude "Analyze the following opinion piece for rhetorical devices. For each paragraph, identify the primary device (ethos, pathos, logos, kairos, anaphora, loaded language, appeal to authority, false dilemma, etc.), quote the key phrase that signals it, rate its effectiveness 1–3, and explain in one sentence. Output as markdown table: Paragraph | Device | Key phrase | Effectiveness | Explanation. Then summarize which device the author relies on most and whether the argument is structurally sound." [paste text]`
- Read / check: Verify device labels match standard rhetorical definitions. Check that "key phrase" quotes are actual text from the piece. Confirm the summary identifies a real pattern, not a generic observation. Check that effectiveness ratings have visible criteria behind them.
- Human supplies: A 500–800 word opinion piece (published editorial, op-ed, or student essay — anything with an argument). Synthetic illustrative piece acceptable for the video; a real published piece makes the payoff more authentic.
- Output medium: screen-recording mp4 (Claude terminal output) + D3 heat-map animation (paragraphs colored by device type)
- The change: Ask Claude to rewrite one paragraph using a different device — switch a pathos appeal to logos. Show the before/after and ask: does the argument feel different? Is it more or less persuasive?
- Teardown angle: Rhetorical analysis is the skill under argument — knowing how the machinery works is what lets you evaluate it, not just feel it. This tool makes the invisible visible.
- Exclusions: Cut full classical rhetoric history; cut discipline-specific style guide differences; cut multi-text corpus analysis.
- Score: 9/10

---

## Candidate 02 — Build the Source Evaluator: Score Credibility of Research Sources with Claude

- Source: ai-for-writing-a-practitioners-guide/chapters/15-research-process-accessing-and-recording-information.md + chapters/16-annotated-bibliography-gathering-evaluating-and-documenting-sources.md
- Lane: BUILD (Claude Code)
- Hook: Students cite sources they never actually read. Researchers include sources they can't evaluate. Build a credibility checklist that runs against any source in under 60 seconds.
- The artifact: A screen recording of a terminal session where Claude evaluates 3 sources for a given research topic. For each source: currency (when published), relevance (to the stated topic), authority (author credentials and institutional affiliation), accuracy (claim checkability), purpose (inform/persuade/sell/entertain). Output as a CRAAP-style 5-dimension table with a 1–5 score per dimension and a composite score. A D3 radar chart animates for each source, showing the five-dimension profile.
- Prompt seed: `claude "Evaluate these 3 sources for a research paper on the long-term effects of social media on adolescent mental health. For each source, score it 1–5 on: Currency (how recent), Relevance (to this specific topic), Authority (author/institution credibility), Accuracy (claims checkable and cited), Purpose (educational vs. advocacy vs. commercial). Show your reasoning for each score. Output as a table. Then rank the three sources for use in an academic argument and explain why." [paste source 1 title/author/URL, source 2, source 3]`
- Read / check: Verify authority scores against actual author credentials (spot-check one). Confirm currency dates are correct. Check that purpose classification is justified by the source text, not assumed. Flag any score the model asserts without evidence.
- Human supplies: 3 real sources on a research topic (URLs or citations). Synthetic examples acceptable for the video; real sources make the comparison meaningful.
- Output medium: screen-recording mp4 (terminal) + D3 radar chart animation (one chart per source, animated sequentially)
- The change: Add a fourth "bad source" deliberately (a blog post with anonymous author, no date, advocacy purpose). Show how the radar chart collapses. Ask Claude: "Could this source be used at all? If so, how?"
- Teardown angle: The CRAAP test is a checklist. The model runs it faster than any human. What the model can't do is decide whether a 3/5-authority source is good enough for your argument — that is a judgment about stakes, not a calculation.
- Exclusions: Cut citation format differences (APA/MLA/Chicago); cut library database navigation; cut plagiarism detection.
- Score: 8/10

---

## Candidate 03 — Build the Annotated Bibliography Generator: From Raw Citations to Evaluated Sources with Claude

- Source: ai-for-writing-a-practitioners-guide/chapters/16-annotated-bibliography-gathering-evaluating-and-documenting-sources.md
- Lane: BUILD (Claude Code)
- Hook: An annotated bibliography is not a list of summaries. It is a ranked argument for why these sources, in this order, build this case. Most students write the summaries and skip the argument.
- The artifact: A screen recording of Claude processing 5 raw citations into a formatted annotated bibliography. Each annotation: 3-sentence summary, 1-sentence credibility assessment, 1-sentence relevance-to-argument statement. Then Claude generates a "synthesis note" — which two sources are in tension, which three form a chain of evidence, and what gap remains. Final output is a clean markdown document.
- Prompt seed: `claude "I'm writing an argumentative research paper on whether standardized testing should be eliminated in public schools. Here are 5 sources I found [paste citations with abstracts or URLs]. Generate an annotated bibliography in APA format. For each source: (1) a 3-sentence summary of the main argument and evidence, (2) a 1-sentence assessment of source credibility, (3) a 1-sentence statement of how this source supports or complicates my thesis. After the bibliography, write a 150-word synthesis note: which sources are in tension with each other, which form a chain of evidence, and what question none of them answers."`
- Read / check: Verify the 3-sentence summaries accurately reflect each source. Confirm APA format is correct (author, date, title, publication). Check that the synthesis note identifies real tensions — not superficial differences. Verify the "unanswered question" is genuinely unanswered by the five sources, not just unaddressed in one.
- Human supplies: 5 real sources with titles, authors, dates, and either abstracts or URLs. Synthetic placeholder citations acceptable for the video; real sources make the output authentic.
- Output medium: screen-recording mp4 (Claude building the document live)
- The change: Ask Claude to re-rank the five sources in order of evidential weight for the specific thesis. Show how the ranking changes the argument structure. Ask: "If I had to cut two sources, which go first and why?"
- Teardown angle: The annotation is not a summary service. It is where you think about whether your sources actually prove your argument. Claude builds the scaffold; the student decides whether the scaffold holds.
- Exclusions: Cut citation style comparison; cut database-access how-to; cut plagiarism policy.
- Score: 8/10

---

## Candidate 04 — Build the Argument Stress-Tester: Find the Weakest Claim in Any Essay with Claude

- Source: ai-for-writing-a-practitioners-guide/chapters/12-position-argument-practicing-the-art-of-rhetoric.md + chapters/13-reasoning-strategies-improving-critical-thinking.md
- Lane: BUILD (Claude Code)
- Hook: Every argument has one load-bearing claim. If that claim fails, the whole structure goes. Most writers never find it — until a hostile reviewer does.
- The artifact: A screen recording of Claude analyzing a 500-word argumentative essay. Output: a numbered list of every claim in the essay, classified as (a) empirical — verifiable, (b) value — normative, (c) definitional — about word use. For each: strength rating 1–3, the strongest counterargument in one sentence, and whether the claim is load-bearing (if false, does the conclusion survive?). The weakest load-bearing claim is flagged in red. A Manim scene shows the argument as a tree — nodes are claims, edges are logical dependencies, the weakest node glows red.
- Prompt seed: `claude "Stress-test the following argumentative essay. List every claim (numbered). For each claim: (1) classify it as empirical, value, or definitional; (2) rate its strength 1–3 based on available evidence; (3) write the one-sentence strongest counterargument; (4) mark it TRUE if this is load-bearing — i.e., if this claim is false, the conclusion no longer follows. Then identify the single weakest load-bearing claim and explain specifically what evidence or reasoning would be needed to strengthen it." [paste essay]`
- Read / check: Verify claim classifications are accurate (empirical claims should be verifiable; value claims should express normative judgment). Check that "load-bearing" designations are logical — does removing the flagged claim actually break the conclusion? Confirm the "how to strengthen" guidance is specific, not generic.
- Human supplies: A 500-word argumentative essay (student essay, published opinion piece, or the writer's own draft). Synthetic example acceptable; a real draft makes the output actionable.
- Output medium: screen-recording mp4 (terminal) + Manim argument tree animation (nodes appear, edges connect, weakest node highlights red)
- The change: Ask Claude to rewrite the weakest claim with the suggested strengthening. Show the original and revised versions side by side. Ask: "Does the argument now hold? What new vulnerabilities did the revision introduce?"
- Teardown angle: Good writing is not about having no weak claims — it is about knowing where your weak claims are and deciding whether to strengthen them or cut them. Claude finds the load-bearing points. The writer decides what to do about them.
- Exclusions: Cut formal logic notation; cut logical fallacy taxonomy (extensive); cut discipline-specific argument norms.
- Score: 9/10

---

## Candidate 05 — Build the Profile Writer: Construct a Rich Character from Sparse Details with Claude

- Source: ai-for-writing-a-practitioners-guide/chapters/07-profile-telling-a-rich-and-compelling-story.md
- Lane: BUILD (Claude Code)
- Hook: A profile is not a biography. It is a specific choice about which details to illuminate and which to leave in shadow. That choice is the writing.
- The artifact: A screen recording of a two-round Claude session. Round 1: the user provides 10 sparse facts about a real or fictional person. Claude generates three different profile opening paragraphs — each starting from a different detail, each establishing a different angle. Round 2: the user picks one opening. Claude generates the full 300-word profile in that register. The three openings are compared in a side-by-side D3 layout showing the focal detail each one privileges.
- Prompt seed: `claude "I'm writing a profile of [person/subject]. Here are 10 facts: [paste facts]. Write three different opening paragraphs — each starting from a different detail, each establishing a different angle on who this person is. After the three versions, write one sentence explaining the choice each opening makes about what matters most. Then ask me which angle I want to develop."`  Round 2: `claude "I want to develop Opening 2. Continue the profile for 250 more words, maintaining the angle established in that opening. Use specific sensory detail, at least one direct quote or reconstructed scene, and end with a detail that recontextualizes the opening."`
- Read / check: Verify each opening genuinely starts from a different detail (not variations of the same angle). Check that the 250-word continuation maintains the focal angle — does not drift. Confirm the closing detail adds meaning, not just information. Check that any "direct quote" is either real or clearly fictional.
- Human supplies: 10 real or invented facts about a person or subject. The writer's own choice between the three openings. Real subject preferred; synthetic illustrative subject acceptable.
- Output medium: screen-recording mp4 (Claude session) + D3 side-by-side display (three openings with highlighted focal detail)
- The change: Ask Claude to write the profile from a different angle entirely — one that makes the same person look less sympathetic. Show how the same facts produce a different character. Ask: "Which is the true profile?"
- Teardown angle: The profile is not what is true. It is which truth to tell. Claude generates the options. The writer makes the choice that is both honest and worth reading.
- Exclusions: Cut journalistic ethics deep-dive; cut interview technique; cut magazine vs. literary nonfiction distinction.
- Score: 8/10

---

## Candidate 06 — Build the Multimodal Analyzer: Read an Image as an Argument with Claude

- Source: ai-for-writing-a-practitioners-guide/chapters/20-image-analysis-what-you-see.md
- Lane: BUILD (Claude Code)
- Hook: Every image makes an argument. Most viewers accept it without reading it. Treat the image as a text — what is it actually saying?
- The artifact: A screen recording of Claude analyzing a single public-domain or creative-commons image (advertisement, editorial photo, or infographic). Output: (1) explicit content — what is literally depicted; (2) implicit content — what is implied or connoted; (3) compositional choices — framing, color, perspective, contrast, what is cropped out; (4) the argument the image makes — stated as a claim the image invites the viewer to accept; (5) who benefits from that argument and who is absent. A Manim scene animates the image with annotation overlays appearing in sequence.
- Prompt seed: `claude "Analyze this image as an argument. [attach or describe image in detail] Step 1: describe what is literally depicted (explicit content). Step 2: identify what is implied or connoted beyond the literal (implicit content). Step 3: analyze the compositional choices: framing, color palette, perspective, lighting, what is cropped or absent. Step 4: state the argument the image invites the viewer to accept as a one-sentence claim. Step 5: name who benefits from the viewer accepting that argument, and who or what is absent from the frame."`
- Read / check: Verify that explicit and implicit content are clearly distinguished. Check that compositional claims (e.g., "warm light connotes safety") are grounded in the actual image, not generic. Confirm the "argument" statement is specific to this image, not a generic observation about the genre. Check that the "absent" section names something genuinely missing, not something that simply doesn't appear.
- Human supplies: One publicly licensed image (advertisement, editorial photo, infographic, historical photograph). Creative commons or public domain preferred. The model cannot retrieve images from URLs — human must paste or describe in detail.
- Output medium: screen-recording mp4 (Claude session) + Manim annotation overlay animation (image with labels appearing sequentially)
- The change: Ask Claude to rewrite the image's argument — describe a compositional change (different framing, different subject position, different cropped element) that would invert the implicit message. Ask: "Would that image still be honest?"
- Teardown angle: Image literacy is not about describing what you see. It is about reading the choices that frame what you see. Claude makes the argument structure explicit. The viewer still decides whether to accept it.
- Exclusions: Cut semiotics formal vocabulary; cut film analysis vs. still image distinction; cut advertising law/FTC disclosure.
- Score: 8/10

---

## Candidate 07 — Build the Analytical Report: Turn Raw Facts into a Structured Argument with Claude

- Source: ai-for-writing-a-practitioners-guide/chapters/10-analytical-report-writing-from-facts.md
- Lane: BUILD (Claude Code)
- Hook: Facts do not argue for anything on their own. An analytical report is a structure that makes facts mean something. Most people write the facts and call it analysis.
- The artifact: A screen recording showing Claude transforming a list of 12 raw data points into a 400-word analytical report with: a thesis (what the facts collectively show), 3 supporting sections (each grouping related facts under a claim), a counterevidence section (one fact that doesn't fit the thesis and how to address it), and a conclusion. A Manim scene animates the transformation — raw facts on the left, structured sections on the right, lines connecting facts to their sections.
- Prompt seed: `claude "Here are 12 facts about [topic]: [paste 12 data points, statistics, or observations]. Transform these into a 400-word analytical report. Structure: (1) one-sentence thesis stating what these facts collectively show; (2) three body sections each opening with a claim and using 3–4 of the facts as evidence; (3) one section acknowledging the fact that fits least well with the thesis and explaining how to account for it; (4) a conclusion that goes beyond summary to name an implication or recommendation. Mark in brackets which fact each sentence draws on."`
- Read / check: Verify the thesis is specific — it makes a claim, not just a topic statement. Check that each body section's opening claim is actually supported by the cited facts. Confirm the counterevidence section addresses a real tension, not a straw man. Check bracket citations are accurate.
- Human supplies: 12 facts, statistics, or observations on a topic (research data, survey results, news items, case study details). Synthetic example acceptable; real data makes the output meaningful.
- Output medium: screen-recording mp4 (terminal) + Manim transformation animation (facts → structure)
- The change: Ask Claude to write the same report for a different audience — a skeptical investor vs. a supportive policy maker. Show how the thesis shifts, which facts get emphasized, and which counterevidence is handled differently.
- Teardown angle: The report is not a collection of facts with a label. It is a selection and arrangement that makes an argument. Claude builds the structure. The writer decides whether the structure is honest and whether the selection is fair.
- Exclusions: Cut data visualization detail; cut APA/MLA format; cut report vs. memo vs. white paper genre distinctions.
- Score: 8/10

---

## Candidate 08 — Research the Literacy Narrative: What Do Pivotal Reading Moments Have in Common with Claude

- Source: ai-for-writing-a-practitioners-guide/chapters/04-literacy-narrative-building-bridges-bridging-gaps.md
- Lane: RESEARCH (Claude assistant)
- Hook: Every writer has one moment when reading or writing changed something. What do those moments have in common across different people and cultures? The pattern is more specific than you think.
- The artifact: Claude researches and synthesizes published literacy narratives (Frederick Douglass, Richard Rodriguez, Maxine Hong Kingston, Junot Diaz, and at least 3 others from different cultural backgrounds). Output: a 500-word comparative brief identifying the recurring structural elements — what each narrative has (a forbidden or difficult text, a social cost, a moment of transformation, a changed relationship to power) — and what is unique to each. Rendered as a research document with citations and a comparison matrix.
- Prompt seed: `claude "Research published literacy narratives from at least 6 different authors representing different cultural backgrounds. Include Frederick Douglass, Richard Rodriguez, and at least 4 others. For each: identify the forbidden or difficult text that anchors the narrative, the social cost of acquiring literacy, the transformation moment, and the changed relationship to language/power after. Then write a 300-word synthesis identifying the structural elements that appear across all six, and what is unique to each. Cite specific passages where possible. Flag any claim you cannot verify from a published source."`
- Read / check: Verify that named narratives exist and that the structural elements attributed to each are accurate to the actual texts. Spot-check one passage citation. Confirm the synthesis distinguishes structural similarity from content similarity. Flag unverified claims for human follow-up.
- Human supplies: Nothing — Claude researches from public sources. Human must verify flagged claims and any quotations before use. Synthetic stand-in acceptable for video; real texts are the authentic payoff.
- Output medium: screen-recording mp4 (Claude building the research brief) + slate (final comparison matrix as a table image)
- The change: Ask Claude: "What would a literacy narrative look like from someone who never gained access to the dominant literacy — someone for whom the transformation did not come? Does the genre require a triumph?" Generate the alternative structure.
- Teardown angle: The literacy narrative is a genre with a grammar. Understanding that grammar is what lets you write within it intentionally and against it when you need to.
- Exclusions: Cut pedagogical use of literacy narratives; cut composition theory; cut ESL/ELL application.
- Score: 7/10

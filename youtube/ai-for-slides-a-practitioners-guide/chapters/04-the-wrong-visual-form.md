# Chapter 4 — The Wrong Visual Form


## TL;DR

- When the information is right but the format makes it hard to see, the failure has a name.
- The chapter moves through What content actually is, What the brain actually decodes, Why bullets became the default, Matching form to structure, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*When the information is right but the format makes it hard to see, the failure has a name. Find the name. Change the form.*

---

Here is something I want you to try.

Read this: Carbon Tax — advantages include price certainty, revenue generation, administrative simplicity. Disadvantages include regressive impact on low-income households, no guaranteed emissions reduction, political unpopularity. Cap-and-Trade — advantages include guaranteed emissions ceiling, market flexibility, cost efficiency. Disadvantages include price volatility, complexity of permit allocation, potential for regulatory capture. Subsidies — advantages include political palatability, targeted deployment, innovation incentives. Disadvantages include ongoing fiscal cost, no emissions ceiling, possible market distortion.

Now: which policy handles equity best? Which has the most predictable fiscal impact? Which gives you a firm cap on total emissions?

You either can't answer those questions, or you had to re-read three times and assemble the comparison in your head. The information was all there. Nothing was hidden. And yet the structure — the comparison itself, the thing the content *is* — was completely invisible.

That is not a failure of content. It is a failure of form.

---

## What content actually is

Every piece of content has a shape. Not a vague shape — a precise one, the kind you can name.

Some content is a *comparison*: here are several things, here are the attributes that distinguish them, here is how each thing differs on each attribute. The shape is a matrix. Rows are attributes. Columns are things. Cells are the values at each intersection.

Some content is a *sequence*: events or steps that follow each other in order. The shape is a chain. The chain may be simple — step one leads to step two leads to step three — or branching: if this condition holds, go here; otherwise, go there. Simple sequences have a different natural form than branching ones.

Some content is a *network*: entities and the connections between them. The shape is nodes and edges. The edges carry the relationship. The direction of an edge means something. The label on an edge means something.

Some content is a *trend*: a quantity changing over time. The shape is a time series.

Some content is a *magnitude comparison at a single moment*: how big is this relative to that, right now, with no time involved.

And some content is a *list*: genuinely independent items that don't compare, don't sequence, don't relate to each other, and don't vary over time. They are just items.

| Structure type | What the content is | Correct visual form | What bullets hide |
|---|---|---|---|
| Comparison | Several things rated on shared attributes | Table (rows = attributes, columns = things) | The comparison axes themselves |
| Sequence (linear) | Steps or events in order | Timeline, arrow chain | The actual intervals between steps |
| Sequence (branching) | Steps with conditional forks | Flowchart | The fork — branches collapse into siblings |
| Relationship / network | Entities and their connections | Node-and-edge diagram | The edges — the relationship *is* the content |
| Trend over time | One quantity changing over time | Line chart | The shape of the change |
| Magnitude comparison | How big is this versus that, now | Horizontal bar chart, sorted | Rank, ratio, and the gap between values |
| Genuine list | Independent items, no relation among them | Bulleted list | Nothing — bullets are the correct form |

*Table 4.1 — The six structural types and the form each requires. Identify the row your slide falls into; the form is then mechanical.*

What I just gave you is a complete classification. And here is the thing: the right visual form for each type follows immediately from what the content is. It isn't a design judgment. It is a consequence.

A comparison becomes a table. A linear sequence becomes a timeline or arrow chain. A branching sequence becomes a flowchart. A network becomes a node-and-edge diagram. A trend becomes a line chart. A magnitude comparison becomes a bar chart. A list becomes a list.

The problem with bullet points is not that they are ugly or that visual designers dislike them. The problem is that they are the same form for all six types. A comparison becomes bullets. A network becomes bullets. A trend becomes bullets. The list is the zero-decision form — the form you get when you haven't stopped to ask what your content is actually shaped like.

When you use the wrong form, you impose work on the reader. Not the good work — the work of understanding the idea, which is theirs to do. The bad work: reconstructing the structure that already existed in the content, that the wrong form erased. Every time a reader holds a bullet from one column in working memory while scanning another column for its counterpart, they are doing the designer's job. Working memory spent on that reconstruction is working memory not available for the concept itself.

John Sweller formalized this in the late 1980s under the name *extraneous cognitive load*: load imposed by the presentation, not by the inherent difficulty of the concept. His finding was not just that extraneous load is annoying. It is that it trades directly against learning. Every unit of working memory spent navigating a badly formed slide is a unit not spent connecting the new idea to what the student already knows. The form has a cost. A form mismatch has a measurable, predictable cost.

---

## What the brain actually decodes

There is another layer to this, and it comes from a direction that surprised me when I first encountered it: perceptual psychology.

In 1984, William Cleveland and Robert McGill published an experiment in the *Journal of the American Statistical Association*. The question was simple: when people try to decode a quantitative relationship from a chart, which visual encodings are decoded most accurately?

They ran controlled experiments. They measured errors. They ranked the results.

At the top of the accuracy ranking: position along a common scale. That is what a bar chart uses when both bars sit on the same baseline. That is what a table uses when you compare entries in the same row. Your eye moves from one point to another along a shared axis, and your estimate of the difference is good.

In the middle: length, angle, slope.

At the bottom: area, color saturation, volume.

![Horizontal bar chart ranking six perceptual encodings by decoding accuracy, from position along a common scale at the top to color saturation and volume at the bottom. Angle/slope and area are flagged as low-accuracy encodings.](../images/04-the-wrong-visual-form-fig-01.png)
![Cleveland-McGill accuracy ranking. The form you choose determines how accurately your reader decodes](images/04-the-wrong-visual-form-fig-01.png)
*Figure 4.1 — Cleveland-McGill accuracy ranking. The form you choose determines how accurately your reader decodes the relationship.*

This ranking has held for forty years. It has been replicated and extended. The practical consequence is that the choice of visual form is not aesthetic. It is a perceptual transmission rate. A pie chart communicates quantitative relationships with measurably lower accuracy than a bar chart — not because it looks worse, but because it encodes magnitude as angle and area, which are near the bottom of the Cleveland-McGill ranking. The reader's judgment of which slice is bigger is systematically worse than their judgment of which bar is taller, and the gap grows as slices become more similar in size.

The ranking applies to categorical comparisons too. A table uses position along rows and columns — the most accurate perceptual encoding available. A bulleted list uses serial reading order and working memory — neither of which appears anywhere in the Cleveland-McGill top tier. When you render a comparison as bullets, you are asking the reader to use one of the least accurate comparison mechanisms available to the human perceptual system. They hold a bullet in short-term memory, shift attention, search for the comparable bullet, hold both simultaneously, and then compare. Every step in that chain is a place where precision is lost.

Put Sweller and Cleveland-McGill together and the claim becomes strong: the form matters because the brain is not a neutral receiver. Different forms are processed with different efficiency and different accuracy. Giving someone content in the wrong form is not a stylistic failure. It is a functional one. The idea doesn't transfer as well.

---

## Why bullets became the default

If bullets are so often the wrong form, why do all the tools default to them?

The answer is that bullets are the lowest-common-denominator structure. Any content can be forced into a list. You don't need to ask what the content is shaped like. You don't need to decide whether you have a comparison or a sequence or a network. You just type, and the tool makes bullets.

This is convenient in the moment and corrosive in aggregate. A tool that makes all form decisions produces slides that reflect the tool's preferences, not the structure of your thinking. And this is not just a problem with PowerPoint. Every AI slide generator has the same failure mode, compounded. An AI asked to compare three policies will produce bullets, because bullets are what slides in its training data predominantly contain. The model has learned the default. It has not learned the principle.

Asking an AI to produce a table requires you to know that the table is the right form, and to say so explicitly. The diagnosis — *this content is a comparison, comparisons go in tables* — has to come from you. The model will execute any form you name with high fidelity. What it cannot do is select among forms by reading the structure of your content against the question your slide is trying to answer. That reading is yours.

There is a related failure worth naming separately, because it is especially common in AI-generated diagrams. If you ask any current tool to make "a diagram showing how X works," you will often get something that looks like a diagram — boxes, arrows, connecting lines, plausible visual organization. The problem is that the arrows go from box to box for visual plausibility, not because there is an actual directed relationship between those elements. The labels are inside shapes but do not answer the question "why does this connect to that?" The result satisfies the visual expectation of a diagram while failing the structural requirement: the picture is supposed to carry information the words alone don't carry. A decorative arrangement of boxes and arrows carries no such information. It is words arranged in shapes.

![Two diagrams side by side. The left shows five generic-labeled boxes (Strategy, Process, People, Technology, Outcomes) connected by six unlabeled arrows. The right shows five concrete boxes about carbon pricing connected by six arrows, each labeled with a verb (raises, incentivizes, drives, funds, reduces).](../images/04-the-wrong-visual-form-fig-02.png)
![Decorative versus structural diagrams. Both look like diagrams; only the right one carries informati](images/04-the-wrong-visual-form-fig-02.png)
*Figure 4.2 — Decorative versus structural diagrams. Both look like diagrams; only the right one carries information the words alone don't.*

The diagnostic question that cuts through all of this is the same whether you are looking at a bullet slide or an AI-generated diagram: *what is the structural relationship between the elements?* Not what the slide looks like. What the content actually is.

---

## Matching form to structure

Once you have named the structure, the matching is mechanical.

**Comparison — things by attributes.** This is a table. Attributes are rows. Things are columns. Cells are answers. The table makes the comparison axes visible rather than requiring the reader to reconstruct them. A reader can move across a row to compare one attribute across all things, or down a column to characterize one thing across all attributes. Both directions are available at near-zero working-memory cost.

The introductory example works this way. Three policies, five attributes: price, emissions cap, revenue, equity, political lift. That is a five-by-three matrix. Rendered as bullets, the comparison axes are implicit — buried inside the text, recoverable only by assembling cells from memory. Rendered as a table, the comparison axes are the row labels. The reader sees them immediately.

![Side-by-side comparison of the same carbon-pricing policies. Left: three columns of bullets (Carbon Tax, Cap-and-Trade, Subsidies) with dotted arcs marking the hidden comparison axes between columns. Right: a five-by-three table with explicit row labels for Price, Emissions cap, Revenue, Equity, and Political lift.](../images/04-the-wrong-visual-form-fig-03.png)
![Same content, two forms. The bullet version hides the comparison axes; the table makes them explicit](images/04-the-wrong-visual-form-fig-03.png)
*Figure 4.3 — Same content, two forms. The bullet version hides the comparison axes; the table makes them explicit as row labels.*

**Sequence without branches.** This is a timeline. The horizontal axis is time, scaled to the actual intervals. 1929 and 1933 are not the same distance apart as 1939 and 1941. A timeline shows that. A bulleted list cannot, because the bullets are evenly spaced regardless of what they represent — the form makes all time intervals identical. The compression and expansion of time, which is often the point, disappears.

**Sequence with branches.** This is a flowchart. The branch is the element bullets cannot represent. "If condition A holds, do this; otherwise, do that" is a fork in the road. A flowchart shows the fork. A list pretends the fork isn't there. When students see bullets where a fork belongs, they have to infer the conditionality from the text — which means the form is making them do structural work that the diagram would do for free.

**Network.** This is a node-and-edge diagram where the edges carry the relationship. The direction of an edge says something. The label on an edge says something. A list of entities with no edges shows you the components; it shows you nothing about why those components matter in relation to each other. The relationship *is* the content in network data. A list without edges removes the content.

**Trend over time.** This is a line chart. The line encodes rate of change. A steep segment communicates acceleration; a flat segment communicates stasis. A list of numbers with their years communicates neither — it gives individual values but cannot show the shape of the change. The shape is the thing that matters most for trend data, and it requires a continuous visual mark to appear.

**Magnitude comparison at a single moment.** This is a horizontal bar chart, sorted by value. Horizontal because the labels are usually words, and horizontal bars let the labels be read without rotating. Sorted because rank relationship is almost always part of the claim, and sorting makes rank immediately visible. Not a pie chart. Pie charts encode magnitude as angle and area — the Cleveland-McGill bottom tier. Bar charts encode magnitude as position along a common scale — the top. Use bars.

**Genuine list.** Use bullets. Items with no structural relationship among them belong in a list. This is the one case where bullets are not a default imposed by the tool but the correct form chosen by the author.

---

## The form decision is semantic, not aesthetic

I want to be precise about something, because it is easy to get backwards.

The table is not better than bullets because it looks cleaner or more sophisticated. The table is better because it encodes the actual structure of the comparison, and bullets do not. If you switched to the table for aesthetic reasons but your content was genuinely a list of independent items, the table would be wrong. The form follows the structure. That is the whole rule.

This means the form decision happens before the slide is built, not after. The right sequence is: *what is the structural relationship between these elements?* Then: *which form encodes that relationship most accurately?* Then: build the slide. Working in the other direction — starting from a bullet slide and then asking whether a different form might look better — is possible, but it is working backward from aesthetics toward semantics instead of forward from semantics toward form.

Edward Tufte's data-ink ratio captures this in a different vocabulary. The fraction of a chart's marks that carry structural information, versus the fraction that are decoration. A bulleted comparison uses many marks — every letter, every bullet glyph, every line break — and encodes no comparison structure. A table uses fewer marks and makes the comparison axes explicit. More structural information, fewer marks. The ratio of information to ink is higher.

Tufte's rule is usually stated as "maximize data-ink ratio, eliminate chartjunk." The direction is right. But there is one finding that complicates the strong version, and I think it is worth naming honestly.

Bateman and colleagues, in a 2010 paper at the CHI conference, ran experiments on charts with and without decorative elements — exactly the chartjunk Tufte argued should be eliminated. They found that some decorative elements improved long-term recall of the chart's content without harming immediate comprehension. The chartjunk-decorated charts were remembered better two weeks later.

This seems like a refutation of Tufte. I think it is a refinement. The Bateman result holds for *memorability* — the reader can later recall that "the chart about fuel costs had the gas pump" — but the experiment measured recall of the chart's topic, not transfer of the concept to a new problem. For journalism and marketing, where you want readers to remember that your chart existed, some decoration may be acceptable. For instructional slides, where the goal is that the student can use the concept to solve a problem they haven't seen before, Tufte's rule holds. Decoration competes with structure in the student's working memory. The concept they need to internalize *is* the structure. Recall is the wrong success criterion for teaching; transfer is what teaching is for.

| Context (goal) | Chartjunk verdict |
|---|---|
| Instructional slide (transfer) | Eliminate. Decoration competes with the structure the student must internalize. Tufte's rule holds. |
| Journalistic chart (memorability) | Accept cautiously. Bateman et al. (2010): a memorable visual cue improves recall two weeks later without hurting immediate comprehension. |
| Marketing slide (recall) | Accept. The chart's job is to be remembered, not to teach. Memorability is the success criterion. |
| Technical reference (precision) | Eliminate. Decoration competes with the reader's ability to extract exact values. |

*Table 4.2 — Chartjunk verdict by context. Tufte's rule is not wrong; it applies to the wrong goal in the wrong context.*

Eliminate chartjunk in instructional slides. Accept it cautiously in slides whose purpose is to be remembered rather than to teach.

---

## Two honest disagreements

Careful people will disagree in two specific places, and I want to name them rather than pretend the choices are clean.

The first is about pie charts. The strong position — Cleveland and McGill's, Tufte's, and mine — is that pie charts should almost never be used, because angle and area are low-accuracy encodings. Use a horizontal bar chart instead. The weaker position is that for two-to-three-slice comparisons where the reader needs only approximate magnitudes and a part-to-whole gestalt — "most of the budget went to A, a little to B and C" — a pie chart may communicate faster than a bar chart, because the circular form makes the whole immediately visible. The vocabulary for navigating the disagreement: *precision* versus *part-to-whole*. If the slide makes a claim about exact magnitudes, use a bar chart. If it makes a claim about rough proportions where part-to-whole is the point, a pie chart with two or three slices may serve. Never more than four slices. Never 3D. If you're unsure, use the bar chart. The accuracy cost of the bar chart is near zero; the accuracy cost of the pie chart climbs with the number of slices.

The second disagreement is about when a table breaks down. A table is ideal when the comparison axes are parallel — the same attributes apply to all things being compared, and every cell can be filled with a consistent entry. It starts to fail when the attributes are asymmetric. If Policy A has three advantages and Policy C has two, and the two are not the same advantages, a table with empty cells looks like an absence claim rather than a signal of asymmetry. The bulleted format, for all its structural failures, does make asymmetry easy to show. The fix is not to revert to bullets. It is to either add a notation convention for asymmetric cells, or to split the slide: one table for the attributes that are parallel across all items, one section for the asymmetries that are not.

Both disagreements reduce to the same underlying question: *what is the structural relationship between the elements, and does this form encode it honestly?* When the answer is yes, the form is right. When it is no — the form is hiding structure, or encoding the wrong thing — the form is wrong, regardless of how it looks.

---

## LLM Exercises

**Exercise 1 — Structure diagnosis**
Take any slide you have built in the last month that uses bullets. Paste the slide content to an LLM with this prompt: *"Identify the structural relationship between the elements on this slide. State it in one phrase: comparison, sequence, network, trend, magnitude comparison, or genuine list. Then tell me which visual form matches that structure and why bullets do or do not fit."* Compare the LLM's diagnosis to your original intent. If they diverge, identify which element of the structure the bullets were hiding.

**Exercise 2 — Table conversion**
Find a slide that uses bullets to compare two or more things. Ask an LLM: *"Convert this bulleted comparison to a table. The rows should be the shared attributes; the columns should be the things being compared. If any attribute does not apply to all columns, note it in the cell rather than leaving it blank. Return the result as a plain-text markdown table."* Then evaluate: are the comparison axes in the resulting table the same axes you would have named if asked to state the slide's claim? If not, the bullets were hiding the wrong structure.

**Exercise 3 — Timeline conversion**
Find a slide that presents historical events or process steps as bullets. Ask an LLM: *"Convert this bulleted list to a timeline description. For each event, state: the label, the date or step number, and the interval since the previous event. Identify any intervals that are significantly larger or smaller than the others — those are the gaps that a bullet list flattens but a timeline would show."* Use the output to decide whether a visual timeline would reveal something the bullets cannot.

**Exercise 4 — Diagram legitimacy check**
Take an AI-generated diagram from any tool — Gamma, Canva, or any other. Paste a description of it (or the diagram itself, if the LLM accepts images) with this prompt: *"For each arrow or connecting line in this diagram, state what directed relationship it encodes. If you cannot state a specific relationship — only that it looks connected — flag that arrow as structurally empty. Count the total arrows and the flagged arrows. A diagram where more than one-third of the arrows are flagged is decorative, not structural."* Use the count to decide whether to rebuild or discard the diagram.

**Exercise 5 — Pie vs. bar decision**
Describe a chart you are planning to an LLM: *"I want to show [content] to [audience]. The claim I am making is [claim]. Should I use a pie chart or a horizontal bar chart? Apply the Cleveland-McGill accuracy ranking and the precision/part-to-whole distinction to justify the recommendation."* Then apply the recommendation and ask a colleague to state the claim they read from the chart without you explaining it. Their answer is the accuracy test.

---

## Tier Connection

Form selection is one of the cleanest Tier 4 problems in slide design. The AI executes any form you name — table, timeline, network, distribution — with high fidelity. It does not reliably select among them, because form selection requires reading the structure of the content against the question the slide is asking, and that reading is irreducibly the author's. The Cleveland-McGill ranking gives you a defensible criterion. The criterion still needs a human to apply it to *this* content for *this* audience.

The phase gate is at the form decision, not at the rendering. A prompt that says "make this a comparison" is doing the gate's work; a prompt that says "make this look better" is delegating across the gate. The pattern in this book is consistent: the chapters move the human's work upstream, out of the per-slide tweak and into the specification the model executes against. See *Appendix A — The Fundamental Themes*.

---

**What would change my mind:** A well-controlled study showing that for genuinely comparative content — same things, same attributes, same claim — a bulleted layout produces equivalent learning outcomes to a table, when the student is tested on their ability to use the comparison to solve a new problem. I have not seen that study. The cognitive load literature points strongly in the other direction, but the specific comparison between bulleted comparisons and tables in instructional slides has not, to my knowledge, been run cleanly. If it has and I have missed it, I want to know.

**Still puzzling:** I do not have a clean rule for when a comparison is "close enough to parallel" that a table is honest. Some content is almost a matrix — the attributes mostly apply, with occasional asymmetries — and the choice between a table-with-footnotes and bullets-with-structure is genuinely ambiguous. The principle is clear; the threshold is not.

---

## Exercises

### Warm-up

**1.** Below are five slide descriptions. For each one, state in a single phrase what structural type the content is (comparison, linear sequence, branching sequence, network, trend, magnitude comparison, or genuine list), then name the correct visual form. Do not look at the chapter's classification table until you have committed your answers in writing.

- A slide listing the top ten countries by GDP in 2023.
- A slide showing how the stages of mitosis follow each other.
- A slide showing how U.S. unemployment changed from 2000 to 2024.
- A slide explaining that a viral protein docks with a cell receptor, triggering endocytosis, which releases the viral genome into the cytoplasm.
- A slide listing four unrelated tips for writing clearer email subject lines.

*(Tests: structural type identification, form-to-structure matching)*

**2.** Take the Cleveland-McGill accuracy ranking and apply it to two specific charts: a standard pie chart showing budget allocation across five categories, and a horizontal bar chart showing the same five categories. For each chart, identify which perceptual encoding the reader uses to decode magnitude, locate that encoding in the ranking, and state which chart conveys the comparison more accurately and why. *(Tests: Cleveland-McGill ranking, practical encoding identification)*

**3.** A colleague sends you a slide with the title "How Our Three Products Compare" and three columns of bullets, one per product, each with six items. Run the three-question diagnostic from Chapter 1 — adapted for form rather than slideument status — and state which single structural type this content is and which form it requires. *(Tests: slideument-to-form-decision bridge, comparison identification)*

### Application

**4.** Take a slide you have built in the last six months that uses bullets. Without using an LLM, identify its structural type, then sketch (on paper or in plain text) what the correct form would look like: name the axes, the visual mark type, and what each cell or segment would contain. Only after completing the sketch, use LLM Exercise 1 from the chapter to check your diagnosis. Note any divergence between your answer and the model's. *(Tests: independent structural diagnosis before LLM-assisted verification)*

**5.** Build the carbon emissions policy comparison table referenced in this chapter — three policies (Carbon Tax, Cap-and-Trade, Subsidies), five attributes (Price, Emissions cap, Revenue, Equity, Political lift) — as a plain-text markdown table. Populate each cell with a short phrase, not a sentence. Then identify one attribute where the entries across the three policies are not truly parallel — where the comparison axis breaks down — and write one sentence explaining how you would handle that asymmetry without reverting to bullets. *(Tests: table construction, parallel-attribute test, asymmetry handling)*

**6.** A process diagram you generated with an AI tool shows six boxes connected by nine arrows. Apply the diagram legitimacy test from LLM Exercise 4: for each arrow, write a one-sentence statement of the directed relationship it encodes. Count how many arrows you can describe precisely versus how many you can only describe as "connected." If more than three arrows are flagged as structurally empty, state what you would do with the diagram. *(Tests: diagram legitimacy check, decorative vs. structural distinction)*

**7.** You are designing a slide that shows how a bill becomes law in the U.S. Congress. The process has two major branch points: the bill can die in committee, and the president can veto the enrolled bill. Draw the decision structure in plain text — use indentation and conditional labels ("If vetoed: → …", "If passes committee: → …") — before deciding whether a timeline or a flowchart is the right form. Justify your choice in one sentence. *(Tests: linear vs. branching sequence distinction, flowchart necessity)*

### Synthesis

**8.** The chapter claims that "the form decision is semantic, not aesthetic." Construct a counterargument: describe a case where two different structural forms could honestly encode the same content, and the choice between them would be aesthetic rather than semantic. Then refute your own counterargument using the Cleveland-McGill ranking or the extraneous-load argument. *(Tests: semantic vs. aesthetic distinction, ability to apply both frameworks to the same case)*

**9.** The Bateman (2010) result is introduced as a "refinement" of Tufte rather than a refutation. Write a two-paragraph explanation — suitable for a faculty colleague who has not read this chapter — of why the Bateman finding does not undermine Tufte's data-ink rule for instructional slides. Your explanation must use the words "transfer" and "recall" and must not use the words "chartjunk" or "data-ink ratio" (since your colleague hasn't read Tufte either). *(Tests: Tufte-Bateman distinction, ability to translate framework vocabulary for a new audience)*

**10.** You are reviewing a colleague's deck of twelve slides. You identify: four that are comparisons formatted as bullets, two that are genuine lists formatted as bullets (correctly), one timeline formatted as bullets, one network diagram where all arrows are structurally empty, and four that are well-formed. Write the feedback you would give — one paragraph, specific, without using the words "better" or "cleaner" — that names the structural problems and proposes the correct forms. *(Tests: form diagnosis across a mixed deck, feedback formulation using structural vocabulary)*

### Challenge

**11.** The chapter covers six structural types. Find or construct a real slide that genuinely belongs to two types simultaneously — for example, content that is both a comparison and a trend — and cannot be cleanly assigned to one. Describe the slide, explain why it falls into two categories, and propose how you would split or restructure it so each resulting slide has a single structural type and therefore a single correct form. *(Tests: edge cases in the structural classification, slide decomposition)*

**12.** Design a five-minute diagnostic exercise — for a group of instructors who have never encountered the structural-type framework — that would teach them to identify the difference between a comparison and a genuine list without naming either category. You may use two contrasting slides as props. Describe both slides, the question you ask the group, and what you want them to notice before you introduce any vocabulary. The exercise should lead them to discover the category distinction themselves. *(Tests: Feynman test — can you teach the structural distinction without naming it first; pedagogical transfer of the diagnostic)*

---

##  AI Wayback Machine
The structural classification in this chapter — comparison goes in a table, network goes in a node-and-edge diagram, magnitude goes in a bar chart — did not begin with William Cleveland or Edward Tufte. It began with **Jacques Bertin** (1918–2010), the French cartographer whose 1967 *Sémiologie graphique* set out, before anyone had run a perceptual experiment, the principle that the form of a graphic should follow the structure of the data. Bertin separated the *visual variables* — position, size, shape, value, color, orientation, texture — and asked which carried which kinds of information. He distinguished selective tasks (find the X), associative tasks (group the X), ordered tasks (rank the X), and quantitative tasks (measure the X), and matched each task to the visual variables that supported it. Cleveland and McGill's 1984 experiments operationalized this — measured the accuracy numbers — but the framework was Bertin's.

![Jacques Bertin, French cartographer and graphic semiologist (1918–2010). AI-generated portrait based on public-domain reference photographs.](../images/jacques-bertin.jpg)
*Jacques Bertin, circa 1970. AI-generated portrait based on public-domain reference photographs.*

**Run this:**

```
Who was Jacques Bertin, and how does his Sémiologie graphique (1967) connect to the structural form-selection framework in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or method.
```

→ Search **"Jacques Bertin"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask the model to translate Bertin's matrix of visual variables into a one-page diagnostic card a working slide designer could pin above their monitor — what survives the translation, and what gets lost?
- Ask whether Bertin's separation of *selective*, *associative*, *ordered*, and *quantitative* tasks maps cleanly onto the six structural types in this chapter, or whether one framework subsumes the other.

What changes? What gets better? What gets worse?

---

*Once the form is right, the next question is whether the color inside that form is doing any work. Color can reinforce the structure or undermine it — and the way it undermines is specific and fixable. That is Chapter 5.*

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 4.1 — Cleveland-McGill accuracy ranking. The form you choose determines how accurately your reader decodes

Create a standalone D3 v7 HTML file for a ranked or grouped bar chart titled "Cleveland-McGill accuracy ranking. The form you choose determines how accurately your reader decodes". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/04-the-wrong-visual-form-fig-01.html`

---

### Figure 4.2 — Decorative versus structural diagrams. Both look like diagrams; only the right one carries informati

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Decorative versus structural diagrams. Both look like diagrams; only the right one carries informati". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/04-the-wrong-visual-form-fig-02.html`

---

### Figure 4.3 — Same content, two forms. The bullet version hides the comparison axes; the table makes them explicit

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Same content, two forms. The bullet version hides the comparison axes; the table makes them explicit". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/04-the-wrong-visual-form-fig-03.html`

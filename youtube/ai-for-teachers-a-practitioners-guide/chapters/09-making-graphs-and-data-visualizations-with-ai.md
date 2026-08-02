# Chapter 9 — Making Graphs and Data Visualizations with AI


## TL;DR

- In 1954 Darrell Huff published a small book called How to Lie with Statistics.
- The chapter moves through The question before the chart, Two instruments that catch most chart dishonesty, Distributions over means: where the equity story lives, The five-question audit, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The chart looks professional. The chart is wrong. The professional appearance is the problem.*

---

In 1954 Darrell Huff published a small book called *How to Lie with Statistics*. The chapter on graphs showed readers exactly how to make a modest numerical difference look dramatic: start the y-axis at something other than zero. The bar that represents 78 looks three times taller than the bar that represents 72 when the axis starts at 68 instead of 0. The data says these numbers differ by 8 percent. The chart says they differ by a lot. The chart is lying.

Huff's example was hand-drawn, and the lie required a human decision to start the axis somewhere misleading. The modern version of the same problem is different in one important way. Nobody decided. The axis truncation is the default. Every spreadsheet tool, every AI chart generator, every data analysis platform auto-fits the y-axis to the data range because that default makes charts look dramatic and dramatic-looking charts are what most users want. The tool is optimizing for visual appeal, and visual appeal and accuracy are not the same thing.

AI makes this problem faster. A teacher with a spreadsheet of student scores can now get a publication-quality bar chart in thirty seconds. The chart will have a truncated y-axis, decorative color, a title that names the topic rather than the finding, and — if the data contains any means — no indication of the distribution the means came from. All of these are defaults. All of them are wrong for most education questions. None of them will be flagged by the tool that produced the chart, because the tool does not know what question the chart is trying to answer.

This chapter is about the five-question audit that catches what AI gets wrong, and about one equity move that changes what education charts reveal. You will need neither statistics training nor programming experience. You will need to run five questions on every chart before it leaves the building.

![Side-by-side comparison of the same six-teacher bar chart](../images/09-making-graphs-and-data-visualizations-with-ai-fig-01.png)
![Side-by-side comparison of the same six-teacher bar chart.](images/09-making-graphs-and-data-visualizations-with-ai-fig-01.png)
*Figure 9.1 — Side-by-side comparison of the same six-teacher bar chart.*

---

## The question before the chart

Here is the move that makes everything else in this chapter work, and it has nothing to do with AI. Before you open a chart tool, write the question you are trying to answer in one sentence. Not "I have scores by teacher" — that describes the data. Not "a chart of attendance" — that describes a topic. A question: *Are there meaningful differences in mean outcomes across these six classrooms?* or *Did attendance change after the February break and did it recover?*

The reason this matters is that chart types are not interchangeable. Each one is designed to make a particular kind of comparison easy for a human eye to do accurately. William Cleveland and Robert McGill established this empirically in 1984 by running experiments on how accurately readers can decode quantitative information from different visual channels.[^cleveland] Their ranking, from most to least accurate: position on a common scale, then length, then angle, then area. Bars use length on a common scale — near the top of the ranking. Pie charts use angle — fourth on the ranking. This is why a pie chart cannot reliably distinguish 19 percent from 21 percent, while a bar chart can. It is not a stylistic preference. It is a measurable difference in how accurately the human visual system extracts numbers from different geometric forms.

The practical consequence for teachers is one rule: pie charts are wrong for any comparison where the slices are close in size, which is most comparisons in education data. Replace the pie with a sorted horizontal bar chart. Every time. The bar is more accurate, works for any number of categories, and does not require a legend.

The broader consequence is that the question drives the chart type. Andy Kirk and the Financial Times' Visual Vocabulary identify five functional categories that cover nearly everything teachers need.[^ft]

**Comparison** — which category is larger? Use a sorted bar chart, ranked by value, not alphabetically. Alphabetical ordering is the default and forces the reader to do the comparison work the chart was supposed to do. Sorted order makes the ranking visible immediately.

**Change over time** — which way is it moving? Use a line chart when the shape of the trend is the message, a bar chart when the magnitude in each specific period is the message. These are different questions with different answers.

**Distribution** — what does the spread look like within a group? Histograms, box plots, violin plots, strip plots. This is the category teachers most often skip, and it is where most equity stories live. We will return to it.

**Relationship** — do two variables move together? Scatterplots for two quantitative variables. Useful for attendance-versus-grade, formative-versus-summative performance, time-on-task versus mastery.

**Part-to-whole** — what fraction of the total? Stacked bars for more than three parts. Pies or donuts only for two or three parts when the part-to-whole gestalt — not the comparison among parts — is the point.

The move is: write the question, name the category, then ask the AI for the chart. Watch what happens when you do this.

Vague request: *Make me a chart of these scores by teacher.* The AI produces a six-color bar chart with alphabetical ordering, a y-axis starting at 70, and a title that reads *Average Score by Teacher*.

Question-first request: *I want to compare mean scores across six teachers teaching the same course, sorted by mean, with the y-axis at zero, no decorative color, and a title that states the finding rather than the topic.* Same data. Different chart. Different story.

| Category | The question it answers | Default chart form | Common wrong choice |
|---|---|---|---|
| Comparison | Which is bigger? | Sorted horizontal bar | Alphabetical bar or pie |
| Change over time | Which way is it moving? | Line or bar by period | Multi-series spaghetti or stacked area |
| Composition | What makes up the whole? | Single stacked bar or treemap (pie only for 2–3 parts) | 3D pie or exploded pie |
| Distribution | How is it spread? | Histogram, density, or violin | Boxplot only, without raw points |
| Relationship | Does one move with another? | Scatter or paired comparison | Disconnected stat tests |

*Table 9.1 — Five functional chart categories*

---

## Two instruments that catch most chart dishonesty

Alberto Cairo, in *The Truthful Art* and *How Charts Lie*, names the single most useful diagnostic for evaluating a chart: *compared with what?*[^cairo] Every quantitative claim a chart makes — this is high, this is low, this rose, this fell — requires an explicit reference to be meaningful. A chart without a reference makes a claim without a basis, and the reader will invent one, usually a wrong one.

There are four common ways this check exposes a lying chart.

**Absolute counts where rates are needed.** Thirty students proficient in one teacher's class, twenty-two in another's. Compared with what? With class size. If the first class has thirty-two students and the second has twenty-four, the rates are 94 percent and 92 percent. The raw count chart told the wrong story entirely.

**Time series without baseline.** Scores rose from 72 to 78 this year. Compared with what? If the prior three years went 70, 73, 76, then 78 is the slope continuing — not evidence that anything changed. The chart claims progress attributable to a new program or initiative. The data shows a line that was already moving.

**Cross-sectional comparison without controls.** Comparing AP enrollment to overall enrollment, or honors-track students to general-track students, on any outcome, ignores selection into the groups. No honest comparison is available without matched controls. The chart cannot show what it appears to claim.

**Single-value claims.** A chart that shows one number — 76 percent proficient — and implies it is good or bad. Compared with what? The state average, the prior year, the district target — one of these must anchor the number or the reader has nothing to do with it.

Cairo's framework treats chart choice not as an aesthetic decision but as an ethical one. A chart that misleads its reader is testimony, and the witness has a professional obligation to the accuracy of what the chart claims. This framing should not be softened. It permanently changes how you read charts, which is the point.

![Cairo's "compared with what?" four failure modes](../images/09-making-graphs-and-data-visualizations-with-ai-fig-02.png)
![Cairo's "compared with what?" four failure modes.](images/09-making-graphs-and-data-visualizations-with-ai-fig-02.png)
*Figure 9.2 — Cairo's "compared with what?" four failure modes.*

The mechanical version of the same principle comes from Edward Tufte's *The Visual Display of Quantitative Information*.[^tufte] His **proportional ink** rule is simple: the visual magnitude of a mark should be proportional to the quantity it encodes. For a bar chart, this means the bar starts at zero. Its visible length encodes the magnitude of the value. A bar chart with a y-axis that starts at 60 encodes (value − 60), not value. The reader's eye does not correct for the truncation. The reader perceives the bar at face length and draws the wrong conclusion about the difference.

The empirical evidence that this effect is real and large is now extensive. Anshul Pandey and colleagues, in a 2015 CHI paper, measured systematic viewer misperception from y-axis truncation. Yang and colleagues replicated across five studies in 2021; in some conditions, 83.5 percent of participants overestimated the data effect when the y-axis was truncated. Michael Correll and colleagues reviewed the field in 2020 and confirmed the effect is robust even when the truncation is explicitly labeled — a scale break mark on the axis does not save the chart.[^correll]

AI tools produce truncated axes by default. Excel produces truncated axes by default. Every chart tool auto-fits the y-axis to the data range because that default looks dramatic and the tool does not know your question. **Treat this as a known defect of the tool, not an occasional accident.** Every bar chart prompt must specify zero baseline, or every output must be audited for one.

One contested edge worth naming because it comes up: line charts. Tufte argues that line charts can start anywhere because they encode shape rather than magnitude. Stephen Few argues that non-zero baselines on line charts are nearly as dishonest when magnitude is the message. Cairo splits the difference: if the chart is showing magnitude, zero baseline; if the chart is showing trend shape, a data-fit baseline is acceptable with a clear label. The honest move is to know which message your line chart is carrying and to make the baseline decision deliberately rather than accepting the default.

---

## Distributions over means: where the equity story lives

Here is the chapter's load-bearing move.

A class with a mean score of 72 could have produced that number three different ways. Everyone scored between 70 and 74 — the class is uniformly near the mean. Half the class scored around 60, half around 84 — the mean is a number nobody actually achieved. Most students scored 75 to 78, but eight students scored between 45 and 55 and pulled the mean down. The bar chart shows the same bar height in all three cases. The teaching response to each case should be completely different. In the bimodal case, two groups of students need different things. In the long-tail case, eight students need targeted intervention this week. In the tight cluster, the class is moving together and the curriculum is working. A bar chart of means cannot tell you which situation you are in.

A **box plot** shows the median, the interquartile range, and the outliers. A **violin plot** adds the full shape of the distribution. A **strip plot** or **jittered dot plot** shows every student as a single point — you can literally see who is where. All three reveal what the mean conceals. All three are producible with an AI prompt in the same time it takes to produce the bar chart that hides the answer to your question.

The equity research makes the cost explicit. Eli Holder and Cindy Xiong published a series of experiments in 2022 and 2023 comparing bar-chart-of-means presentations of group differences against variance-revealing alternatives.[^holder] The finding: when subgroup differences are shown as bar charts of means, readers infer larger, more essentialist group differences than when the same data is shown with variability visible. Hiding the variance does not merely fail to show the spread; it actively encourages stereotyping by making within-group variation invisible. A bar chart of demographic group means implies the bars are properties of the groups rather than descriptions of distributions. A strip plot or box plot shows the distributions and makes visible that the variation within any group is larger than the variation between groups — which is true of almost every K–12 dataset.

The sentence to carry out of this section: if your equity question is *who is being left behind?* and your chart is a bar of means, your chart cannot answer your question.

The prompting consequence is direct. When the question is about subgroup performance, the AI tool's default is wrong. The prompt must specify the chart type — a box plot faceted by demographic group, a strip plot with median overlaid — or the output will be a bar chart that hides the answer to your own question.

![Three charts of the same class with mean = 72](../images/09-making-graphs-and-data-visualizations-with-ai-fig-03.png)
![Three charts of the same class with mean = 72.](images/09-making-graphs-and-data-visualizations-with-ai-fig-03.png)
*Figure 9.3 — Three charts of the same class with mean = 72.*

---

## The five-question audit

Five questions. Run them on every chart before it leaves the building. The full checklist runs in about five minutes.

**One: What question does this chart answer?** State it in one sentence. If you cannot, the chart is not ready. A chart that cannot be described by a one-sentence question has not been designed; it has been generated.

**Two: Compared with what?** Cairo's check. Every quantitative claim must have an explicit reference — a baseline, a benchmark, a prior period, a peer group. If the chart shows 76 percent proficient and nothing else, the reader has no anchor. Add the reference or the chart is not yet a claim.

**Three: Does the y-axis start at zero?** For a bar chart, always. For a line chart, when magnitude is the message — and the choice must be defended in either case, not defaulted.

**Four: Is the title a finding or a topic?** A topic names the subject: *Average Score by Teacher*. A finding states what the chart shows: *Six sections cluster within 7 points; all are within one standard deviation of each other*. Cole Nussbaumer Knaflic's rule in *Storytelling with Data* is to write the verb.[^knaflic] The title is not the label on the data. The title is the claim the chart is making.

**Five: Did you check for hidden variance?** If the chart shows means, ask whether the distribution matters for your question. If it does, replace the bar chart or add a distribution chart alongside it.

A sixth question applies whenever AI is in the loop and it takes two additional minutes: **does the chart match the data you gave it?** AI tools hallucinate. They occasionally invent tick values, relabel axes, auto-round data, or group categories in ways the prompt did not request. Always verify chart values against the source spreadsheet for at least a sample of the values. Three percent of charts containing a fabricated value is enough to embarrass you at a board meeting. The verification is not optional.

![Five-question audit as a checklist card](../images/09-making-graphs-and-data-visualizations-with-ai-fig-04.png)
![Five-question audit as a checklist card.](images/09-making-graphs-and-data-visualizations-with-ai-fig-04.png)
*Figure 9.4 — Five-question audit as a checklist card.*

---

## A worked example: the truncated bar chart and its replacement

Take a math department chair with aggregate data from six teachers teaching the same course.

| Teacher | Mean | SD | n |
|---|---|---|---|
| Adams | 78.2 | 11.4 | 142 |
| Brennan | 76.8 | 14.2 | 138 |
| Connor | 75.3 | 8.9 | 145 |
| Diaz | 74.1 | 13.7 | 140 |
| Edelstein | 73.6 | 16.1 | 139 |
| Sandoval | 71.4 | 9.2 | 137 |

*(Composite-illustrative data. The pattern reflects realistic district profiles.)*

She types: *Make me a chart of average scores by teacher.* The AI returns a six-color bar chart with bars in alphabetical order, a y-axis running from 70 to 80, and a title that reads *Average Score by Teacher*.

Run the five questions.

**What question does this chart answer?** Unclear. It shows different bar heights. Whether those differences are meaningful is not stated.

**Compared with what?** Nothing. No state benchmark, no prior year, no department target, no measure of within-class variance. Cairo's check fails.

**Does the y-axis start at zero?** No — it starts at 70. With Adams at 78.2 and Sandoval at 71.4, the visible bar lengths encode (score − 70). Adams's visible bar is 8.2 units tall; Sandoval's is 1.4 units tall. The visual ratio is roughly 6 to 1. The actual score ratio is 78.2/71.4, which is about 1.1 to 1. The chart inflates a 9-percent difference into a 6-to-1 visual difference. The lie factor is approximately 5.5. Sandoval's class looks like it is failing. The data says it is 9 percent below the highest class mean, well within normal classroom variation. These are different stories.

**Is the title a finding or a topic?** A topic.

**Did you check for hidden variance?** No. Edelstein's standard deviation is 16.1; Connor's is 8.9. Edelstein's class has nearly twice the within-class spread. The bar chart does not show this. If the question is which students are not being served, the variance is most of the answer.

Now she rewrites the prompt:

```
ROLE: You are a data visualization assistant following Cairo's
"compared with what?" check, Tufte's proportional-ink rule,
and Knaflic's finding-as-title principle.

CONTEXT: Unit assessment data from six teachers, same course.
Sample sizes 137–145 per teacher. I will paste the aggregate
data below with means, SDs, and n per class.

TASK: Produce two charts.

Chart 1: horizontal bar chart, sorted descending by mean.
- Y-axis starts at zero, runs 0–100
- Error bars: 95% CI from the SD and n provided
- Annotation: proficiency benchmark line at 70
- Title: a sentence stating the finding about spread
  ("Six sections cluster within 7 points; all within one
  standard deviation of each other")
- One color for all bars. No legend.

Chart 2: faceted box plot, one panel per teacher, same sort order.
- X-axis 0–100 across all panels
- Title: a sentence stating the finding about within-class variance
  ("Within-class variance differs more than between-class means")

CONSTRAINTS:
- Use a single colorblind-safe color across both charts.
- Print the generation code so I can verify data binding.
- Restate what you understood before generating. Flag any
  default you applied that I did not specify.
```

What comes back: Chart 1 shows six bars as a tight cluster between 71.4 and 78.2, all within about one standard deviation of each other. The visual gap that made Sandoval's class look like it was failing collapses into what it actually is — small variation within a department that is otherwise performing consistently. Chart 2 shows that Edelstein's class has the widest distribution: her median is near the pack, but her lower quartile reaches 55 and her upper quartile reaches 92. Three of Edelstein's students fall in the bottom tenth percent of all 841 students in the dataset. Sandoval's class is the second-tightest distribution; his lower mean reflects a class performing uniformly, not a class with a failing tail.

The conversation the first chart would have started: what is happening with Sandoval? The conversation the second chart starts: what is happening with the eight students in Edelstein's lower quartile, and are intervention resources reaching them? The chart shifted the question. That is what a chart is for.

---

## Color, briefly

One default AI tools get wrong that is not about axes. Every category gets its own color — six teachers, six colors. Each color sends the reader's eye to the legend to decode it, which is cognitive load with no payoff if the teacher names are already on the axis. Color is the weakest perceptual channel in Cleveland and McGill's ranking. Use it only when it is encoding a variable that is not already encoded by position or length.

When color must encode something, use Cynthia Brewer's ColorBrewer palettes, which were designed and tested for perceptual accuracy and colorblind safety.[^brewer] *Set2* for categorical variables. *YlOrRd* or *Blues* for ordered variables. A rainbow gradient for a proficiency scale is actively wrong — hue has no natural order, so the rainbow implies a sequence the data does not support. Specify the palette by name in the prompt. The AI tool will use it.

---

## The prompt structure that prevents the defaults

Every chart prompt needs four things: what the chart is trying to show, what the data contains, what the reader should understand in five seconds, and explicit constraints overriding the defaults. The constraints are not optional decoration. They are the corrections for the known defects of the tool.

Here is the minimum constraint block that handles the most common errors:

```
CONSTRAINTS:
- Y-axis (value axis) starts at zero and runs the full natural
  range of the measure (0–100 for scores or percentages).
- Bars sorted descending by value, not alphabetically.
- One color across all bars. No legend unless color is encoding
  a second variable. Use a colorblind-safe palette (ColorBrewer
  Set2 or Blues).
- Title states the finding as a sentence with a verb. Example:
  "Three sections cluster within 4 points; one is 9 points lower."
  Not: "Mean Scores by Section."
- Annotate the relevant reference line (benchmark, prior year,
  target).
- Restate what you understood before generating. Flag any default
  you applied that I did not specify.
```

The last two lines — restate before generating, flag applied defaults — are the prompting version of the audit. If the model's restatement of the question is wrong, you catch it before it produces code. If it flags a default it applied, you can accept or reject it. These lines make silent decisions visible.

---

## Three things that would make me revise this chapter

The chapter rests on three claims: that chart defaults in AI tools are systematically wrong for education questions; that the five-question audit catches the most important errors; and that variance-revealing distribution charts reduce essentialist inference in readers.

For the third claim, I would update if a well-powered replication showed that distribution charts do not reduce essentialist inference — or that the inferential improvement comes at a comprehension cost that makes the charts less useful in practice for non-expert audiences like school boards and parents. The current evidence runs in one direction. A clean reversal would change the recommendation on when to use box plots versus bar charts of means in public-facing presentations.

For the second claim, I would update if a controlled study of AI-assisted chart-making with teachers showed that the five-question checklist did not improve chart honesty in real workflows — that teachers skipped it under time pressure, or that the bottleneck was elsewhere in the process. The chapter assumes the audit is the protective move. That assumption is currently unmeasured in the teacher-AI context.

For the first claim — AI defaults are wrong — the evidence is the defaults themselves, and I observe them every time I run a chart prompt without constraints. If the tools change their defaults to start bar axes at zero and use finding-as-title by default, that section of the chapter becomes unnecessary rather than wrong.

---

## Exercises: using AI to understand AI charts

These exercises are done with an AI tool. The second one is the most important.

**Exercise 1: Generate a chart, run the audit.**

Take one set of assessment data from your current semester — a unit test by section, attendance by week, a benchmark by student group, anything where the data is real and the question matters. Write the one-sentence question before opening the prompt. Use the constraint block from this chapter as your starting point. Generate the chart. Run the five-question audit. Iterate the prompt at least once based on what the audit flags. Then write one sentence describing what the chart reveals about student learning that you did not see in the raw data. If you cannot write the sentence, the chart did not answer your question. Re-prompt.

**Exercise 2: Cairo audit of an existing chart.**

Find a chart in a current district report, board presentation, state education department dashboard, or EdTech vendor brochure. Run Cairo's "compared with what?" check explicitly. Identify the most serious failure mode — truncated axis, missing reference, mean bar where distribution is the question, decorative color, topic-label title. Then write the AI prompt that would have produced a more honest version of the same chart. You do not have to generate the corrected chart. The prompt is the artifact, because the prompt is where the audit becomes a habit. You will find these charts everywhere — in board slides, state dashboards, news coverage of school outcomes. They are not produced by dishonest people. They are produced by defaults that no one overrode.

**Exercise 3: Distribution chart for an equity question.**

Take a measure for which subgroup performance is the actual policy question — proficiency by race or ethnicity, growth by English-learner status, discipline referrals by IEP status, AP enrollment by free-and-reduced-lunch eligibility. Generate two versions of the same data: a bar chart of subgroup means, and a faceted box plot or strip plot showing the distribution within each subgroup. Compare them side by side. Write a paragraph on what each version shows, what each hides, and which one you would use in a board meeting if your goal were honest reporting. Then write one sentence about which version is the standard board-meeting move at your institution, and why. The gap between those two answers is the chapter, restated as a local question about your own practice.

---

A bar chart of means is not the wrong chart. It is the wrong chart for questions where the distribution is the answer. Most equity questions in education are questions where the distribution is the answer. AI produces bar charts of means by default. Run the audit. Change the default. The five minutes that takes is the work.

Chapter 10 turns toward writing — the writing you do as a teacher and the writing your students do — where the same family of problem takes a different form. A chart that hides the distribution hides who is being left behind. A student essay generated by AI hides whether the student learned at all. Same structure, higher stakes.

---

[^cleveland]: Cleveland, W. S., & McGill, R. (1984). Graphical perception: Theory, experimentation, and application to the development of graphical methods. *Journal of the American Statistical Association*, 79(387), 531–554. <https://www.jstor.org/stable/2288400>.

[^ft]: Financial Times Visual Vocabulary, designed by Alan Smith, FT Visual Journalism Team. <https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary>. See also Kirk, A. (2019). *Data Visualisation: A Handbook for Data Driven Design* (2nd ed.). SAGE.

[^cairo]: Cairo, A. (2016). *The Truthful Art: Data, Charts, and Maps for Communication.* New Riders. Cairo, A. (2019). *How Charts Lie: Getting Smarter about Visual Information.* W. W. Norton.

[^tufte]: Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press. Chapter 2, "Graphical Integrity," pp. 53–87.

[^correll]: Correll, M., Bertini, E., & Franconeri, S. (2020). Truncating the y-axis: Threat or menace? *CHI 2020*. <https://arxiv.org/abs/1907.02035>. Pandey, A. V., et al. (2015). How deceptive are deceptive visualizations? An empirical analysis of common distortion techniques. *CHI 2015*. Yang, W., et al. (2021). Truncating the y-axis: A replication study. Multiple conditions showing up to 83.5% overestimation of effect.

[^holder]: Holder, E., & Xiong, C. (2022/2023). Dispersion vs. disparity: Hiding variability can encourage stereotyping when visualizing social outcomes. arXiv:2208.04440. Published in *IEEE Transactions on Visualization and Computer Graphics* (2023). <https://arxiv.org/abs/2208.04440>.

[^knaflic]: Knaflic, C. N. (2015). *Storytelling with Data: A Data Visualization Guide for Business Professionals.* Wiley. Chapter 2, "Choosing an Effective Visual."

[^brewer]: Brewer, C. A. ColorBrewer: Color advice for maps and data. <https://colorbrewer2.org>. Harrower, M., & Brewer, C. A. (2003). ColorBrewer.org: An online tool for selecting colour schemes for maps. *The Cartographic Journal*, 40(1), 27–37.

---

##  AI Wayback Machine
Bertin's *Sémiologie graphique* (1967) — the seven retinal variables, the systematic decomposition of any chart into mark, channel, and question — is the chart-selection vocabulary every teacher needs before they ask AI to make a graph. The chapter's framework is Bertin operationalized for the classroom-data use case: name the question first, choose the channel that answers it, accept that the chart's job is to make one comparison legible, not to make many comparisons available.

![Jacques Bertin, 1918-2010. AI-generated portrait based on a public domain photograph.](../images/jacques-bertin.jpg)
*Jacques Bertin, 1918-2010. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

**Run this:**

```
Who was Jacques Bertin, and how does their work connect to the ideas in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or thinking.
```

→ Search **"Jacques Bertin"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Bertin's framework to a specific scenario in this chapter — what gets surfaced that the chapter's prose left implicit?
- Ask about the critics of Bertin's work and which criticisms still bite today.

What changes? What gets better? What gets worse?

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 9.1 — Side-by-side comparison of the same six-teacher bar chart.

Create a standalone D3 v7 HTML file for a bar or comparison chart titled "Side-by-side comparison of the same six-teacher bar chart.". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-making-graphs-and-data-visualizations-with-ai-fig-01.html`

---

### Figure 9.2 — Cairo's "compared with what?" four failure modes.

Create a standalone D3 v7 HTML file for a concept map titled "Cairo's "compared with what?" four failure modes.". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-making-graphs-and-data-visualizations-with-ai-fig-02.html`

---

### Figure 9.3 — Three charts of the same class with mean = 72.

Create a standalone D3 v7 HTML file for a bar or comparison chart titled "Three charts of the same class with mean = 72.". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-making-graphs-and-data-visualizations-with-ai-fig-03.html`

---

### Figure 9.4 — Five-question audit as a checklist card.

Create a standalone D3 v7 HTML file for a checklist or diagnostic card titled "Five-question audit as a checklist card.". Use teacher AI-workflow states: learning goal, AI draft, teacher review gate, classroom use, equity check, and student evidence. Encode the AI-assisted step with one red mark and all teacher-controlled checks with neutral ink. Include direct labels, a zero baseline if values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/09-making-graphs-and-data-visualizations-with-ai-fig-04.html`

# Chapter 9 — Finishing Pass and Figures

*Where the book becomes visible — and the visual fluency trap arrives on schedule.*

---

Here is one paragraph from a draft of Chapter 7 of *ai-for-designers*, exactly as Cowork produced it:

> *Five things to watch for in the draft. Voice will drift toward Wikipedia. Specificity will be invented where the pantry was thin. Domain judgment will be missing where the model could not infer it. The middle will be padded. Bridge questions will gesture rather than commit.*

And here is the same paragraph after a finishing pass:

> ## Five failure modes — read in this order
> *The model is good at producing prose that reads correct and means nothing. Here is what to look for first.*
>
> Voice will drift toward Wikipedia. Specificity will be invented where the pantry was thin. Domain judgment will be missing where the model could not infer it. The middle will be padded. Bridge questions will gesture rather than commit.

Same prose. Three additions. A heading that names what is coming. An italic subtitle that says what the section is actually doing. And a placeholder comment, invisible to the reader, marking the moment the reader needs to see the taxonomy as a structure rather than a list.

The "after" is still missing something. There is no figure yet. There is only a comment that says *a figure goes here, and here is what it should do*. That comment is a contract between the author and the figure pipeline — it tells the next stage where a figure belongs and what work it is supposed to do.

This chapter runs three operations in sequence. Every chapter gets a subtitle that earns its place and honest visual placeholder comments at the moments they would help. CAJAL reads those chapters and proposes figure candidates, ranked. The proposals become real SVGs, real PNGs, real D3 files. The book becomes visible.

You are also going to learn what the visual fluency trap looks like, because it is going to arrive. CAJAL can produce a chart that is technically a chart, semantically empty, and convincingly designed. You will catch it the same way you caught the verbal fluency trap in Chapter 1. The skill transfers.

---

Before the three operations, a note on tooling. CAJAL's SVG generator and the PNG converter at `SCRIPTS/svg-to-png.mjs` are Node.js programs. You need Node 18 or higher. If you don't already have it:

**Mac:** `brew install node` then verify with `node --version`.

**Windows:** `winget install OpenJS.NodeJS.LTS` then verify with `node --version`.

**Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install -y nodejs npm` then verify both.

From inside your book directory, run `cd SCRIPTS/ && npm install sharp`. That installs the PNG converter's one dependency. The exact workaround depends on your `sharp` version — the library has shifted between prebuilt binaries and building from source across major releases. If `npm install sharp` fails on Mac silicon with a message about Python or libvips, the optional-build flag (`npm install --include=optional sharp`) is the usual fix; if that does not clear it, check the current installation docs at sharp.pixelplumbing.com.

You do not need to learn Node. You do not need to read any JavaScript. You need it on your machine so the scripts run. Five minutes.

---

The Chapter Finishing Pass does exactly two things to each chapter file. It does not touch your prose. It inserts an italic subtitle on the line below the main heading if one is missing, and it inserts HTML comments at the places in the text where a table, image, infographic, or chart would genuinely help the reader.

That is it. Two passes, no rewrite, no reorganization. The finishing pass runs after the human rewrite from Chapter 8. The prose is the author's at this point. The pass adds navigational scaffolding on top.

The subtitle distinction is worth spending time on because it is where most finishing passes fail.

A topic heading names territory. *"Color theory."* It is true. It is also the kind of thing a Wikipedia stub would say. A subtitle surfaces tension. *"Why every accessible palette starts with grayscale."* That second one is doing work — it tells the reader what the chapter's argument is going to be. It commits the author to a position.

Cole Knaflic calls this "the so-what" — the move from naming a category to naming a claim.[^knaflic] Robert Bringhurst treats it as a typographic move: the subtitle is a different rank of text and should look different on the page.[^bringhurst] Both are describing the same underlying requirement, which is that a subtitle should be impossible to move to a different chapter without breaking.

Three rules that make a subtitle work:

Less than fifteen words. If you cannot state the central tension in fifteen words, the chapter does not yet know what its central tension is — return to Chapter 4. A claim, not a category: if the subtitle could appear under a different chapter's heading without breaking, it is not doing chapter-specific work. Italic in the rendered EPUB: reflowable EPUBs reliably honor italic styling; they do not reliably honor custom CSS classes; italic is the safe contract.

The visual placeholder comments are the other half of the finishing pass output, and the brief inside each comment is what separates useful scaffolding from decoration. The format is:

```
<!-- → [INFOGRAPHIC: Five Failure Modes — a 5-row table laid out as a vertical taxonomy. Left column: failure name. Middle column: how it sounds in a draft. Right column: rewrite move. Two-color (ink + ochre), no gradients.] -->
```

The arrow is a grep target so you can find all pending visuals at once. The bracket type — `INFOGRAPHIC`, `CHART`, `TABLE`, `IMAGE`, `DIAGRAM` — tells the enrichment pass which generator to invoke. The description after the colon is the brief the figure-generation step reads.

Three rules for a brief that does not produce a generic figure. Name the data, not the category: not "a chart of failure modes" but "a 5-row table, named columns, two-color." Name the constraint: "No gradients. Two-color. Flat fills." Name the load it has to carry: "The reader should leave knowing the rewrite move, not just that there are five failure modes." A brief that names data, constraint, and load is one that any figure generator — CAJAL, a junior designer, or a future tool none of us has seen — can execute against a clear standard.

| Element | What it does | Example |
|---|---|---|
| The arrow | A grep target so you can find every pending visual at once | `→` |
| The bracket type | Tells the enrichment pass which generator to invoke | `INFOGRAPHIC`, `CHART`, `TABLE`, `IMAGE`, `DIAGRAM` |
| The brief (after the colon) | The instruction the figure-generation step reads — names data, constraint, and load | `Five Failure Modes — a 5-row table... Two-color (ink + ochre), no gradients.` |

![A single placeholder-comment string segmented into three regions left to right — the arrow as grep target, the bracket type as generator selector, the brief after the colon — each region dropping a callout line to a reserved cell naming its downstream role.](images/09-finishing-pass-and-figures-fig-01.png)
*Figure 9.1 — Anatomy of a visual placeholder comment*

---

CAJAL Image Suggest runs across every chapter and proposes figures. It does not generate any SVG yet. It writes one file per chapter at `pantry/{chapter-slug}-cajal.md`, listing every figure it thinks would help, ranked by priority, with a full SCOPE prompt for each. The Finishing Pass and Image Suggest prompts are reproduced in Appendix G.

Think of `cajal.md` as a menu. You will reject some items. You will modify some. You will add candidates CAJAL missed. The point of having proposals in their own file before any SVG is generated is that you get an editorial pass between the candidate inventory and the rendered figure. What you do not edit, you ship.

CAJAL scans chapter prose for three signal patterns. Understanding them is understanding why it proposes what it proposes.

**MC — Mechanism Complexity.** The chapter describes a process with three or more interdependent steps. The pipeline overview in Chapter 5 is MC. The three-pass rewrite loop in Chapter 8 is MC. Most "and then this, and then this" passages trigger MC.

**VG — Verification Gap.** The chapter makes a structural claim the reader cannot verify from prose alone. "The Combined Test has fourteen items in two groups" is a VG signal — the reader has to be shown the structure to confirm it. "Cowork reads four files in order" is VG.

**PQ — Proportional or Quantitative.** Any percentages, ratios, counts, or comparisons. "Steady workers complete in four to six weeks" is PQ. "Eighty percent of indie ebook units" is PQ. Anything with a number that compares to another number.

Tamara Munzner's *Visualization Analysis and Design* calls the underlying diagnostic the "what-why-how" framework: what data do you have, why is the reader looking, how should it be encoded.[^munzner] CAJAL's MC/VG/PQ is a coarser, faster version of the same — a triage layer before the full what-why-how decision.

Open a `cajal.md` after a run and you will see a structure like this:

```
# Figure Plan — Chapter 7

## Figure 7.1 (Critical, MC)
**Title:** The eight-section Cowork chapter structure
**Trigger:** Chapter describes 8 sequential sections each Cowork chapter follows.
**SCOPE:**
  Specification: One-column vertical flow diagram, 8 boxes.
  Content: Section name + one-line "what it does" per box.
  Organization: Top-to-bottom, arrow between each.
  Presentation: Two-color (ink + ochre). No gradients. Flat fills.
  Exclusions: No icons. No screenshots. No decorative borders.
```

The SCOPE prompt is what the SVG Generator reads. Title, ranking, trigger, and five SCOPE fields — Specification, Content, Organization, Presentation, Exclusions — appear consistently across all chapters.

The editorial pass through a `cajal.md` takes ten minutes per chapter and is worth every minute of it. Critical figures should map directly to a primary learning outcome. Open the chapter. If the Critical figure does not encode the thing the reader is supposed to leave knowing, demote it and find one that does. Important figures support a key argument but are not load-bearing — these are usually safe. Supplementary figures are nice-to-have, and the honest answer is often "skip this one." A textbook is not improved by having a figure on every page.

![A top-to-bottom decision tree with three nodes — Critical (does it map to a primary outcome?), Important (does it support a key argument?), Supplementary (skip unless time allows) — each with a pass-through arrow to the next test, the Critical node carrying a demote redirect and the Supplementary node terminating in a skip glyph.](images/09-finishing-pass-and-figures-fig-02.png)
*Figure 9.2 — CAJAL figure-priority decision path*

[^knaflic]: Knaflic, C. N. (2015). *Storytelling with Data*. Wiley.
[^bringhurst]: Bringhurst, R. (2013). *The Elements of Typographic Style* (4th ed.). Hartley & Marks.
[^munzner]: Munzner, T. (2014). *Visualization Analysis and Design*. CRC Press.

---

The SVG Generator reads the `cajal.md` files you have edited and produces real SVG files in `images/`. The pipeline then runs `node SCRIPTS/svg-to-png.mjs` to convert every new SVG to a 300-DPI PNG, runs the enrichment pass that inserts markdown image links at the placeholder locations, and writes a corresponding D3 v7 HTML file in `d3/` for any figure with interactive data underneath it.

You do not write any JavaScript. You read the `cajal-svg-log.md` written at the end, and you open the PNGs.

PNG is the publication artifact. Kindle's reflow engine renders PNGs reliably across every device — Paperwhite, iPad, iPhone, Colorsoft, desktop Kindle app. SVG is the source artifact. You keep it because it is editable, version-controlled, and re-renderable at any resolution. PNG is what ships in the EPUB. SVG is what survives a redesign. This is the same separation as `combined.md` → EPUB+PDF: the source is text, the build output is the binary the device renders. You do not edit the build output. You edit the source and rebuild.

![A left-to-right systems diagram of the CAJAL pipeline — Finishing Pass, CAJAL Image Suggest producing cajal.md, SVG Generator producing SVG source, the svg-to-png converter producing the 300-DPI PNG, the enrichment pass inserting markdown links — with a downward D3 companion branch off the source stage and a divider marking SVG and D3 as source artifacts versus the PNG that ships in the EPUB.](images/09-finishing-pass-and-figures-fig-03.png)
*Figure 9.3 — The CAJAL pipeline: prose to publication artifact*

The D3 files in `d3/` are for figures that have data structure underneath them — anything CAJAL flagged as MC or PQ that could be interactive. What they are honestly for: not for the published EPUB (EPUBs do not reliably execute JavaScript), but as authorable source artifacts so the next edition has editable chart code, and optionally as a companion-web property if you want readers to explore the data. If you do not plan to host the D3 files anywhere, they cost nothing to keep in the repository. The PNG is what the reader sees in the book.

The AI+1 visual standard is what you audit every generated figure against. It is the visual analogue of the Combined Test from Chapter 8 — stripped down, device-agnostic, constraint-first. The constraint exists so the *content* of the figure carries the load, not the chrome.

Two-color or three-color maximum per figure. ColorBrewer "Set2" for qualitative comparisons and "Blues" for sequential data are the safe defaults — or Okabe and Ito's Color Universal Design palette, engineered to stay distinct under common color-vision deficiencies. Avoid red/green pairings — about 8% of male readers of Northern European descent, roughly one in twelve, have some form of red-green color deficiency. Every figure must read in grayscale.

Which encoding you reach for is not a matter of taste either. In 1984 William Cleveland and Robert McGill ran the experiments that ranked them: a reader judges position along a common scale most accurately, length next, then angle and area, with color saturation near the bottom.[^cleveland] That ranking is why a side-by-side bar chart beats a pie, why a pie beats a wordcloud, and why area-encoded blobs lie to the eye even when the numbers behind them are honest. Encode the comparison the reader most needs to make in the channel the eye reads best, and spend the weaker channels on the comparisons that matter least.

Flat fills only. No gradients. Gradients render as a smooth ramp on retina iPad and as a banded mess on e-ink Paperwhite. Flat fills degrade gracefully across every device in that range.

No rounded corners, no drop shadows. They look contemporary in Figma. They look pixelated at reflow.

Every SVG has a `<title>` and `<desc>` element. This is an EPUB 3 accessibility requirement per the W3C EPUB Accessibility 1.1 specification, which became a Recommendation on 25 May 2023 and points back to WCAG 2.2's rule that every non-text element carry a text alternative.[^w3c][^wcag] It is also a fact-checking aid — alt text that drifts from what the figure shows is a flag that the figure or the description needs updating.

Axes are labeled. Units are declared. Source and date are present. This is Tufte's rule, stated plainly in *The Visual Display of Quantitative Information* and violated constantly in AI-generated figures.[^tufte]

And the figure earns its place. If the prose conveys the information as efficiently as the figure would, delete the figure. Tufte's data-ink ratio is the diagnostic: the proportion of a figure's ink devoted to non-redundant data. Generic decoration is what he called chartjunk. A figure that is present because CAJAL proposed it and nobody said no is chartjunk with a SCOPE prompt.

The cleanest demonstration of a figure earning its place is more than a century and a half old. Most people know Florence Nightingale as the nurse who reformed military hospital sanitation during the Crimean War; fewer know that she designed the chart that did the reforming. The mortality tables had not moved Parliament. So in 1858 she drew a polar-area diagram — the *Diagram of the Causes of Mortality in the Army in the East* — wedges fanning around the months of the year, the blue area for preventable disease dwarfing the red area for battle wounds, the whole thing built for Queen Victoria and Parliament rather than for statisticians. The chart changed minds the tables could not. Sanitary reform of the military hospitals followed, and that same year she became the first woman elected a fellow of the Statistical Society. Her figure earned its place by changing policy. That is still the only criterion for a Critical figure that matters.

There is a contested edge to this last rule worth naming honestly. Bateman and colleagues published "Useful Junk?" at CHI 2010 with empirical evidence that embellished charts are better remembered than minimalist ones.[^bateman] Mona Chalabi's hand-drawn data illustrations in the Guardian make the same argument from data journalism — visual personality is a data-integrity move because it signals provenance and single-author accountability. Both are legitimate. Both are out of scope for the AI+1 series default. The reasoning: a $1 Kindle book is read across more devices than any other format, and the device-agnostic constraint wins until there is a specific reason to break it.

[^cleveland]: Cleveland, W. S., & McGill, R. (1984). "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods." *Journal of the American Statistical Association*, 79(387), 531–554.
[^w3c]: W3C. (2023). *EPUB Accessibility 1.1*. w3.org/TR/epub-a11y-11/.
[^wcag]: W3C. (2023). *Web Content Accessibility Guidelines (WCAG) 2.2*, Recommendation, 5 October 2023, Success Criterion 1.1.1 Non-text Content. w3.org/TR/WCAG22/.
[^tufte]: Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press.
[^bateman]: Bateman, S., et al. (2010). "Useful Junk? The Effects of Visual Embellishment on Comprehension and Memorability of Charts." *CHI 2010*.

---

The worked example is Chapter 7 of *ai-for-designers* through the full pipeline, showing what each step produced and what was accepted, modified, and rejected.

**Step 1 — Chapter Finishing Pass.** Before the pass, the chapter heading read `# Chapter 7 — Running the Chapter Writer`. After:

```
# Chapter 7 — Running the Chapter Writer
*Why the first draft of a fourteen-chapter book takes one hour and three weeks of preparation.*
```

The subtitle surfaces the tension — the real runtime is not the model's hour but the author's preparation. Three visual placeholder comments were inserted, including the one that became Figure 7.1:

```
<!-- → [INFOGRAPHIC: The eight-section Cowork chapter structure — 8 vertical boxes, top to bottom, ink + ochre. Each box has section name and one-line description. No icons.] -->
```

**Step 2 — `07-cowork-draft-run-cajal.md`.** Three figures proposed. The Critical figure (Figure 7.1, MC trigger) was the eight-section structure flow diagram — it fired because the chapter describes eight sequential sections each draft follows. The SCOPE named the data, the constraint, and the load. One Important figure (Figure 7.2, five failure modes taxonomy, VG trigger) was accepted as-is. One Supplementary figure (Figure 7.3, a histogram of `[verify]` flag counts across draft runs, PQ trigger) was modified before generation — the original SCOPE called for ten bars; the data only supported five distinct buckets, so the SCOPE was edited down.

One CAJAL suggestion was rejected entirely: a fourth proposal for a wordcloud of common failure terms, flagged as Supplementary. Wordclouds violate the visual standard — they have no data-ink discipline, they cannot be made device-agnostic, and they encode nothing the prose doesn't already encode more precisely. Deleted from the `cajal.md` before the SVG step.

**Step 3 — SVG and PNG output.** Three SVG files at `images/07-cowork-draft-run-fig-01.svg` through `fig-03.svg`. The PNG converter produced three PNGs at 300 DPI. The enrichment pass inserted the markdown links:

```
![The eight-section Cowork chapter structure](../images/07-cowork-draft-run-fig-01.png)
*Figure 7.1 — Eight sections, run in order, no skipping. CAJAL output, edited.*
```

D3 companion files appeared for Figure 7.1 (the section-structure diagram, MC trigger) and Figure 7.3 (the histogram, PQ trigger). Figure 7.2 (the taxonomy, VG trigger) did not get a D3 companion — it is a static structural diagram, and an interactive version would be over-engineered for it. The enrichment pass made that judgment automatically.

---

CAJAL produces solid first-pass figures. For most handbook chapters that is enough. For chapters where the figure *is* the argument — where the page is dominated by a chart that the prose orbits around — two companion books in this series cover the territory the enrichment pass cannot.

*AI for Graphs* is the companion on chart-making with AI assistance for non-statisticians. The most relevant chapters for a handbook author: chart selection by question (Munzner's what-why-how applied as a decision flowchart — when is a small-multiples grid the right answer; when is a dual-axis chart never the right answer); the reading-on-device pass (render a chart at iPad, iPhone, e-ink, and PDF print sizes before committing); and reading a chart for what it is hiding (the Challenger O-ring case as the canonical figure that fails its argument — this is the chapter for catching the visual fluency trap).

*AI for Infographics* is the companion on instructional figures that replace sections of prose rather than illustrating them. The most relevant chapters: taxonomy figures (the structural diagram type Figure 7.2 belongs to; how to design one the reader can scan in twelve seconds; Williams's CRAP principles from *The Non-Designer's Design Book* applied to instructional layout[^williams]); process diagrams beyond linear flows (when to leave a flowchart behind for parallel tracks, branches, or feedback loops); and the accessibility audit (alt text, color-blind palettes, screen-reader-readable SVG structure).

You do not need either companion to finish your handbook. You need them when you are fighting CAJAL — when the default output is producing figures and you can see they are wrong but cannot say what would be right.

[^williams]: Williams, R. (2014). *The Non-Designer's Design Book* (4th ed.). Peachpit.

---

The book is now visually complete. Subtitles surface the arguments; figures encode what prose cannot carry efficiently; the PNGs render on every device. What is still missing is the layer that makes this an *AI+1* textbook rather than a textbook about AI — and that, with the fluency trap waiting at pedagogy scale, is the next chapter.

---

## Sources

1. Knaflic, C. N. (2015). *Storytelling with Data*. Wiley. https://www.wiley.com/en-us/Storytelling+with+Data:+A+Data+Visualization+Guide+for+Business+Professionals-p-9781119002253
2. Munzner, T. (2014). *Visualization Analysis and Design*. CRC Press.
3. Cleveland, W. S., & McGill, R. (1984). "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods." *Journal of the American Statistical Association*, 79(387), 531–554. https://www.jstor.org/stable/2288400
4. Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press.
5. Bateman, S., et al. (2010). "Useful Junk? The Effects of Visual Embellishment on Comprehension and Memorability of Charts." *CHI 2010*. https://dl.acm.org/doi/10.1145/1753326.1753716
6. W3C. (2023). *EPUB Accessibility 1.1* (Recommendation, 25 May 2023). https://www.w3.org/TR/epub-a11y-11/
7. W3C. (2023). *Web Content Accessibility Guidelines (WCAG) 2.2* (Recommendation, 5 October 2023). https://www.w3.org/TR/WCAG22/
8. Bringhurst, R. (2013). *The Elements of Typographic Style* (4th ed.). Hartley & Marks.
9. Royal Statistical Society. (2020). "Nightingale 2020: the bicentenary of our first female fellow." https://rss.org.uk/news-publication/news-publications/2020/general-news/nightingale-2020-the-bicentenary-our-first-female/

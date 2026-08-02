# Causal Inference with Case Studies

*A living Kindle handbook of causal inference theory and student-written case studies, produced by a graduate cohort each semester, framed by a nine-chapter theory spine, read by practitioners, students, and researchers looking to apply causal methods to their own work.*

**Publisher:** [Bear Brown LLC](https://www.bearbrown.co)
**Editor:** [Nik Bear Brown](https://www.bearbrown.co/books)
**Current edition:** Spring 2026
**Next edition:** Fall 2026

---

## Preface

Causal inference is a young field in an old discipline. The tools described in this book mostly did not exist a generation ago. Some of them — the graphical framework, the formal treatment of counterfactuals, the algorithmization of adjustment — are less than three decades old. Others are older ideas that have been rehabilitated after spending most of the twentieth century in exile, banished by a statistical tradition that treated causation as philosophically suspect and methodologically impossible.

The exile was a mistake. Causal questions are the questions that matter most. Does smoking cause cancer? Does a policy reduce poverty? Did this specific action cause this specific injury? Would this patient benefit from this treatment? These are the questions that science, medicine, law, and public policy need to answer, and they are precisely the questions that classical statistics, restricted to the language of correlation and association, could not address.

The rehabilitation of causal inference over the past thirty years has produced a mature discipline with rigorous methods, well-developed software, and an expanding base of applications across every field that works with data. What the field lacks is broader practical literacy. Too many researchers still treat causation as a word to avoid rather than a concept to reason with precisely. Too many applied analyses still make causal claims implicitly while denying causal intent. Too many readers still lack the conceptual tools to evaluate causal claims with the skepticism they deserve.

This book is an attempt to address that literacy gap, and to do so in a specific way.

### The theory spine and case studies model

The book has two layers. The first is a nine-chapter theory spine that introduces the language, methods, and habits of thought that constitute modern causal inference. The chapters cover the ladder of causation, causal diagrams, confounding and adjustment, randomization, matching, weighting methods, instrumental variables, counterfactuals and mediation, and finally how to read causal case studies critically. The spine is designed to be read linearly. Each chapter builds on the ones before it. By the end, a reader should be able to approach any causal analysis in the wild — a published paper, a news report, a colleague's study — with a structured set of questions and enough technical grounding to answer them.

The second layer is the case studies. Each semester, graduate students in a seminar at Northeastern University write case studies that apply the methods of the theory spine to problems they care about. Some are applications of matching to health data. Some are instrumental-variables analyses of policy changes. Some are mediation analyses of social or behavioral interventions. The cases are varied by design — students choose their own questions, and the resulting collection reflects the breadth of applications that causal methods can support.

The structural bet of the book is that readers learn causal inference better from documented real applications than from abstract methodological exposition alone. The theory spine equips readers to read the cases; the cases make the theory concrete. Neither layer is complete without the other. A theory-only book would be one of dozens on the same shelf. A case-only book would be a collection of examples without the conceptual scaffolding to make sense of them. Together, they form what we hope is a more useful resource than either would be alone.

### Why this book exists

Several excellent introductions to causal inference already exist. Judea Pearl and Dana Mackenzie's *The Book of Why* is a superb popular treatment of the conceptual foundations. Jason Roy's *A Crash Course in Causality* is a rigorous applied-methods course. Hernán and Robins' *Causal Inference: What If* is a thorough graduate-level text. Morgan and Winship's *Counterfactuals and Causal Inference* covers the social-science applications. Readers looking for alternative or complementary treatments should consult these and the many other resources that have appeared in recent years.

What distinguishes this book is the pairing of a compressed theory spine with student-written case studies, produced under an editorial gate that requires each case to instantiate methods from the theory. The result is a handbook pitched at a reader who wants both conceptual grounding and exposure to the craft of applying causal methods to real problems — and who wants the case layer to grow and evolve across semesters as new cohorts contribute new applications.

The cohort-produced model borrows directly from our companion book, *Design of Agentic Systems with Case Studies*, which uses the same structural logic: a stable theory spine paired with a rotating student-contributed case layer, refreshed each semester. That book has demonstrated that the model can produce useful, publishable, extensible handbooks in rapidly developing fields. This book applies the model to causal inference, a field whose conceptual foundations are stable but whose applications continue to expand.

### For readers

This book is for you if you want to understand causal inference well enough to read and evaluate causal claims, to recognize the methods used in applied work, to grasp the assumptions those methods require, and to develop a disciplined skepticism toward the many places causal reasoning can go wrong. The book is pitched above an introductory statistics level but below a research-methods textbook. Readers should know basic probability and statistics — what a regression is, what a standard error is, what a p-value means — but need not have any prior exposure to causal inference specifically.

The theory spine assumes you have not encountered causal diagrams, potential outcomes, or the do-calculus before. It introduces these concepts from scratch and develops them with enough care that a motivated reader should be able to follow the logic without outside references. The case studies assume you have read the theory spine (or are reading it alongside). Some cases may require domain knowledge specific to their topic, which the student authors supply.

The book does not teach you how to *execute* causal methods in statistical software. Readers who want hands-on training should supplement this book with software-specific resources: R packages like `MatchIt`, `AER`, or `mediation`; Python packages like `DoWhy` or `EconML`; Stata commands like `teffects` or `ivregress`. The case studies in this book often describe their computational methods, but they are not tutorials for running those methods yourself. That is a different book, and a necessary complement to this one.

### For contributors

This book's case layer is produced each semester by graduate students in a seminar at Northeastern University. Contributing a case to the book is an uncompensated academic publication. The book is priced at Amazon's Kindle minimum ($0.99) and distributed through Kindle Unlimited, with promotional free-distribution windows. Authors retain copyright on their chapters and receive a byline in every edition their chapter appears in.

Students interested in contributing should consult the contributor guidelines at the book's GitHub repository. The guidelines cover the editorial process, the acceptance standard, and the case template. Cases are selected for publication based on methodological rigor, clarity of exposition, and fit with the book's case-layer structure. Not every submitted case is accepted for publication — but every submission that clears the assignment gate earns course credit, whether or not it ships in the edition.

### For instructors

This book is intended to support both self-directed readers and course use. The nine-chapter theory spine maps naturally to a nine-week module within a broader research-methods or applied-statistics course. The case studies can be assigned individually as application exercises, or collectively as the basis for a capstone project in which students critique existing cases and propose their own.

Instructors adopting the book for a course should feel free to contact the editor about supplementary materials. A separate instructor's supplement is planned for the Fall 2026 edition, which will include discussion questions, suggested exercises, and suggested further readings for each chapter. Instructors using the book before the supplement is available are welcome to share materials they develop; high-quality instructor contributions may be incorporated into future editions.

### What the book won't do

A few things this book deliberately does not do, which readers should know up front.

**The book does not replace a full methods textbook.** The theory spine is compressed. Each of its nine chapters introduces a topic that has full textbooks of its own. Readers who want to actually practice matching, for instance — to design their own study using matching methods and defend the design to a reviewer — will need more than Chapter 5 can provide. The spine is a foundation, not a complete education.

**The book does not teach statistical computing.** No code is included in the theory chapters. The case studies sometimes describe methods in enough detail to suggest how they could be implemented, but we are not trying to teach readers how to run propensity score analyses or fit IV models in R. That training is essential for anyone who wants to apply causal methods, and it should come from a dedicated computing resource, not from this book.

**The book does not pretend to cover the whole field.** We have selected a set of methods that we consider foundational and that the student cases routinely invoke. Several important methods are mentioned briefly or not at all: regression discontinuity designs, difference-in-differences, synthetic control methods, structural equation modeling, causal Bayesian networks beyond the graphical framework. Each of these deserves its own treatment, and committed readers should pursue them after working through this book.

**The book does not resolve all the terminological chaos in the field.** Chapter 9 takes on some of the worst offenders — "control for," "causal effect" unqualified, "Causal AI" — but causal inference vocabulary remains a moving target, and new buzzwords appear regularly. The disciplined reader will keep asking the same questions (what is the method actually doing? what are the assumptions?) regardless of what the marketing calls it.

### A note on the editions

Each semester produces a new edition. The theory spine is stable across editions, subject to corrections and improvements. The case layer rotates — each edition's cases belong to that semester's cohort, and previous cases may be replaced by newer ones or retained in an archive. Readers citing specific cases should cite the specific edition; the theory spine can be cited as the standing reference.

We expect the book to evolve. The first edition (Spring 2026) represents an initial synthesis. Later editions will refine the theory spine based on reader feedback and classroom experience, and will expand the case layer as new cohorts contribute new applications. The book's GitHub repository tracks changes across editions and documents the reasoning behind substantive revisions.

### Acknowledgments

The book's conceptual architecture owes deeply to the work of Judea Pearl, whose graphical framework unified and transformed the field over the past four decades, and to Donald Rubin, whose potential outcomes framework provided the formal language that much of statistics now uses to reason about counterfactuals. Chapter 2's account of Sewall Wright's 1920 paper on path analysis and Chapter 7's account of John Snow's 1854 cholera study are both drawn from Pearl and Mackenzie's *The Book of Why*, which remains the finest popular introduction to the field's intellectual history. Chapter 3's treatment of confounding and the back-door criterion, Chapter 5's treatment of matching, and Chapter 6's treatment of weighting methods draw on Jason Roy's open-access course *A Crash Course in Causality*, which is the most accessible rigorous introduction to applied causal methods I know of.

The student contributors whose cases appear in each edition are the reason this book has a case layer at all. Their work is the animating contribution. Individual student authors are credited in the cases they wrote.

The editorial workflow for the book is adapted from the companion project *Design of Agentic Systems with Case Studies*, whose production model and repository structure this book inherits. Readers interested in the institutional details of a cohort-produced, semester-refreshed handbook should consult that book's documentation.

Any errors in the theory spine are mine. Any errors in the case studies are the students'. Readers who find errors of either kind are invited to open issues on the book's GitHub repository.

Nik Bear Brown
Boston, March 2026

---

## Table of Contents

### Preface

### Chapter 1: Why Causal Inference?

- The bleeding of George Washington
- The shape of a causal question
- Three levels of causation
- The eighty-year prohibition
- What causal inference actually does
- The role of causal models
- How this book is organized
- What you'll be able to do
- One final note before we start

### Chapter 2: The Language of Causal Diagrams

- Sewall Wright's guinea pigs
- What a causal diagram is
- Drawing a diagram from a story
- Three building blocks: chains, forks, colliders
- Paths
- Back-door and front-door paths
- When is a path "open"?
- A worked example
- Mediators: the weed in the garden
- What the diagram is not
- Summary and what comes next

### Chapter 3: Confounding and Adjustment

- Resolving Simpson's paradox
- What confounding actually is
- The back-door criterion
- Adjustment as a computation
- The mediator fallacy
- The collider fallacy
- M-bias
- What if you can't find a valid adjustment set?
- A note on front-door adjustment
- Summary

### Chapter 4: Randomization and Its Limits

- Daniel's experiment
- What randomization does
- Fisher and the skillful interrogation of nature
- What an RCT gives you
- Blinding and other protocols
- A real RCT: the Palm trial
- Why we can't always randomize
- Non-compliance and the intent-to-treat problem
- The bridge to observational methods
- What we'll cover next
- Summary

### Chapter 5: Matching

- The smoking / periodontal disease example
- The matching idea
- Exact matching and its limits
- Distance metrics
- The propensity score
- Greedy matching vs. optimal matching
- Variations: one-to-one, one-to-many, with or without replacement
- Balance diagnostics
- Calipers
- The matching analysis
- Back to the smoking example
- Sensitivity to hidden bias
- Matching vs. regression: cousins, not rivals
- What matching cannot do
- Summary

### Chapter 6: Weighting Methods

- Why weighting (and the problem with matching)
- The weighting idea
- Inverse probability of treatment weighting
- Why the name is intimidating and what it actually means
- A worked example
- Stabilized weights
- Marginal structural models
- Balance diagnostics for weighting
- The weight distribution problem
- Doubly robust estimation
- Double machine learning: a modern extension
- Weighting vs. matching: when to use which
- An example: IPTW in action
- What weighting cannot do
- Summary

### Chapter 7: Instrumental Variables

- John Snow and the Broad Street pump
- The two water companies
- The basic idea
- A diagrammatic view
- Two-stage least squares
- The assumptions, in detail
- Monotonicity: the fourth assumption
- Compliance classes and the local average treatment effect
- Weak instruments
- Mendelian randomization
- The encouragement design
- Other sources of instruments
- Reading IV papers critically
- What IV cannot do
- Summary

### Chapter 8: Counterfactuals and Mediation

- Cleopatra's nose
- What a counterfactual is
- Potential outcomes
- Computing counterfactuals from a causal model
- A worked example
- Individual vs. population counterfactuals
- Mediation: the search for mechanisms
- The naive approach and why it fails
- The counterfactual formulation of mediation
- The mediation formula
- When mediation analysis works
- Mediation in the smoking-cancer case
- Probability of necessity and sufficiency
- When counterfactuals matter most
- What counterfactual analysis cannot do
- Summary

### Chapter 9: How to Read a Causal Case Study

- What a case study is trying to do
- The checklist
  - What is the causal question?
  - What is the causal model?
  - What is the identification strategy?
  - Are the data appropriate?
  - Are the methods appropriate?
  - Are the assumptions stated and defended?
  - Are the results sensible?
  - Are there sensitivity analyses?
  - Are the limitations honestly acknowledged?
  - Are the conclusions calibrated to the evidence?
- The terminology problem
- Causal AI: the buzzword problem
- Other terminological games
- An interdisciplinary Babel
- A template for reading the cases in this book
- The point of this book
- A final note

### Part II: Case Studies

*The nine case studies that follow are written by graduate students in the Spring 2026 cohort at Northeastern University. Each applies methods from the theory spine to a causal question the student selected. See the individual case chapters for student bylines, methodological approaches, and substantive findings.*

### Appendices

*Errata, edition history, and contributor guidelines are maintained at the book's GitHub repository rather than in the printed text.*


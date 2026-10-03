# YouTube publish sheet — claude-liam-democracy-math-equation

**Master:** `4K/09-02-2026/claude-liam-democracy-math-equation.mp4`
**Runtime:** 9:03 · 3840×2160 · 24 fps · AAC mono 48 kHz · −24.16 LUFS
**Channel:** @NikBearBrown · **Playlist:** Behind the Model
**Narrator:** Liam (in for Bear) · **Register:** Teardown
**Source essay:** skepticism.ai — "When Democracy Becomes a Math Equation" (2026-02-07)
**Channel URL:** https://www.youtube.com/@NikBearBrown

---

## TITLE

**Primary (matches OUTRO-LOCK — use this one):**
When Democracy Becomes a Math Equation

**A/B alternates (only if you want a more searchable hook):**
- Can Math Prove Corruption? (Bayesian Favoritism, Explained)
- How Statisticians Would Actually Test a Corruption Allegation
- Bayesian Inference vs. Political Favoritism | When Democracy Becomes a Math Equation

---

## DESCRIPTION

Two senators say tariff exemptions are going to the politically connected. Everyone can see the pattern — the hard question is whether you can turn that suspicion into a number a hearing room has to take seriously.

Short answer: you can't prove intent. But you can measure how much better connected companies do with merit held constant. This is a teardown of exactly that machinery — a hierarchical Bayesian logistic model — built step by step, including the parts that can't deliver what people want from them.

We start where the accusation starts: the February 4, 2026 letter from Senators Wyden and Van Hollen describing "an opaque process that appears to favor the politically connected." Then we do the thing the letter can't do — operationalize it.

WHAT THE FILM BUILDS
• Why Bayesian inference is the right tool for a black box: no published criteria, no portal, no visible decision process — so you work backward from outputs alone
• How "connected" becomes measurable: campaign contributions normalized by firm assets, lobbying disclosures (which issues, and who was hired), and symbolic transactions
• The logit link — why doubling a lobbying budget doesn't double your odds
• X-econ vs X-pol: separating the legitimate case for relief from the political case
• β-pol — the allegation compressed into a single coefficient, and what its posterior sitting above zero would and wouldn't mean
• Hierarchical partial pooling: why firms nesting inside industries is the difference between a finding and an ecological fallacy
• Changepoint detection on a real ten-day sequence in November 2025
• Priors from published research, Bayes Factors as referee, and event studies as an outside check from the market
• What the math cannot say — intent, above all

THE HONEST LABEL (please read this before you quote a number)
This film is a METHODS teardown, not a published finding. The decisive-sounding figures in it — a ~6-point contribution effect, a ~15-point ballroom-donor effect, a Bayes Factor of 247, a 0.98 changepoint probability — are the source essay's WORKED SCENARIO. They are what this analysis would return if real data behaved as the essay sketches. Nobody has run this model on the real exemption dockets. The narration flags every one of them aloud, and so does the screen. The method is real. The verdict waits on data.

WHAT IS INDEPENDENTLY VERIFIED
The reported events are sourced and were fact-checked against primary documents before authoring: the Senate letter, the November 4, 2025 Swiss delegation and its gifts, the November 14 framework deal cutting the Swiss tariff from 39% to 15%, Apple's August 2025 pledge and plaque, and the peer-reviewed 2018–2020 research finding roughly a 4-point effect per standard deviation of contributions in Section 301 exclusions — the same study that found NO political effect in steel and aluminum exemptions. Where the source essay was wrong, it was corrected: the deal date is November 14, not November 11 — ten days after the gifts, not seven.

YOUR TURN — PASTE THIS INTO CLAUDE
"I have a dataset of regulatory decisions: outcomes, applicant characteristics, and political-connection proxies. Walk me through building a hierarchical Bayesian logistic model to test favoritism against merit — one, which priors and why; two, how to partition industry effects from firm effects; and three, what result would falsify the favoritism hypothesis."

Run it on any policy domain you care about. The machinery transfers.

SOURCES
• Wyden/Van Hollen press release + letter PDF — finance.senate.gov, 2026-02-04
• Lopatin et al. 2024, Economics & Politics — doi:10.1111/ecpo.12260 (Section 301 political effect; steel/aluminum null)
• Forbes, Axios, Bloomberg, CNBC, Fortune, swissinfo.ch — November 2025 Swiss deal and gifts; August 2025 Apple pledge
• Source essay: "When Democracy Becomes a Math Equation" (Nik Bear Brown, 2026-02-07) — https://www.skepticism.ai/p/when-democracy-becomes-a-math-equation
• More at https://www.skepticism.ai

Subscribe: https://www.youtube.com/@NikBearBrown

Narrated by Liam, in for Bear. Animation is Manim and Remotion; narration is a local Kokoro voice. No sponsor, no affiliate links.

#BayesianStatistics #DataScience #ComputationalSkepticism

---

## CHAPTERS (paste into the description as-is)

0:00 Can you turn suspicion into a number?
0:20 Crossing out "prove." Crossing out "corruption."
0:33 Act I — The hearing room
1:01 The process that was never opened
1:16 Why Bayesian inference fits a black box
1:30 Act II — Measuring "connected"
1:44 Channel 1 — campaign contributions
1:58 Channel 2 — lobbying disclosures
2:12 Channel 3 — a desk clock and a gold bar
2:46 The question, operationalized
2:58 Act III — The equation
3:09 Why probability curves: the logit link
3:25 X-econ vs X-pol — merit against connection
3:40 Beta-pol: the allegation as a coefficient
3:55 Firms nest inside industries
4:11 Act IV — Ten days in November
4:39 Changepoint detection
4:58 Bayesian vs frequentist
5:12 Act V — Priors, posteriors, and the weight of evidence
5:32 How a posterior updates
5:46 Bayes Factors as referee
5:59 The worked scenario — illustrative, not findings
6:17 Act VI — The market already knew
6:43 Why a zero is loud
6:55 Act VII — What the math cannot say
7:14 Steelmanning the counter-argument
7:34 What would falsify favoritism
7:49 The honest label
8:05 Recap
8:33 Your turn — the prompt
8:58 Outro

---

## TAGS (YouTube tag box — 491/500 characters)

bayesian statistics, bayesian inference, hierarchical bayesian model, logistic regression, logit link, bayes factor, posterior distribution, prior distribution, changepoint detection, event study, abnormal returns, causal inference, ecological fallacy, computational skepticism, data science, statistics explained, political economy, regulatory capture, lobbying data, campaign finance data, tariff exemptions, section 301, quantitative political science, econometrics, falsifiability, manim

---

## KEYWORD NOTES (not pasted — for title/thumbnail/pinned-comment work)

**Primary keyword cluster:** hierarchical Bayesian logistic regression · Bayes Factor · posterior distribution · changepoint detection · event study
**Secondary (topic pull):** political favoritism · regulatory capture · tariff exemptions · Section 301 · lobbying disclosure · campaign finance
**Framing/brand:** computational skepticism · falsifiability · "measures advantage, never intent"

**Search intent this ranks for:** viewers asking "how do you statistically test for corruption / favoritism," students looking for a worked hierarchical Bayes example, and the political-economy audience arriving from the news story.

**Thumbnail text candidates:** CAN MATH PROVE IT? · β-pol > 0 · MEASURE, NOT PROVE
**Pinned comment:** lead with the honest label — the decisive numbers are a worked scenario, not a study. Getting ahead of that comment is worth more than the engagement it costs.

**Do not put in the title or thumbnail:** any of the illustrative numbers (6.2pp, 14.7pp, BF 247, 98%). They are the one thing in this film that will be screenshotted out of context, and the film's whole argument is that they are not yet findings.

---

## LINK CHECK BEFORE PUBLISHING

`https://www.skepticism.ai/p/when-democracy-becomes-a-math-equation` is CONSTRUCTED,
not verified. The domain (`https://www.skepticism.ai`) and Substack's `/p/<slug>` post
pattern are both confirmed from the repo; the slug comes from the archived export
filename `187209075.when-democracy-becomes-a-math-equation.html`, which uses Substack's
`<post_id>.<slug>.html` convention. That makes it very likely correct — but click it
once before you publish. The channel URL is confirmed from the repo.


# Chapter 23 — Case: GhostTrack


## TL;DR

- When "ghost artist" cannot be specified — convergence of independent signals as the load-bearing identification move.
- The chapter moves through Question, Causal diagram, Identification strategy, Results, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*When "ghost artist" cannot be specified — convergence of independent signals as the load-bearing identification move.*

**Author:** Trimbkeshwar Jagtap
**Editor:** Nik Bear Brown

---

## 1. Question

The headline question is detection: which Spotify artists are ghosts — fraudulent or AI-generated accounts uploading bulk catalogs to harvest streaming royalties? But the methodological question underneath is harder, and it is the one this case study is really about. *What does it mean for an artist to be a ghost?* There is no single Spotify field, no licensing flag, no audit trail that lets you check. The DOJ indictment of Michael Smith (September 2024) names three artists — Relaxing White Noise, Meditation Relax Club, Calmo. Dagens Nyheter's investigation into Johan Röhr's Firefly Entertainment names 9 pseudonyms publicly out of a reported 656+. Beyond those, the label is inferred.

The project's claim is structural: no single signal can specify what a ghost artist is, but the joint convergence of seven independent signals — audio variance, playlist entropy, ISRC registrant concentration, bipartite neighborhood, release cadence, signal radar, and a graph neural net — on the same artists is itself evidence that "ghost artist" picks out a real underlying pattern. Convergence is the finding.

Data: Spotify's public API (with audio features removed February 2026 — a material constraint that forces the substitution of a Kaggle 114K-track dataset for Signal 1), ISRC registrant data for the three confirmed ghosts, and a Dagens Nyheter ground-truth list of which only 3 entries have publicly verified Spotify IDs.

## 2. Causal diagram

The DAG here is a **measurement model**, not a treatment-effect model. The distinction matters for what the analysis can claim.

A latent node *G* — "this artist is a ghost" — sits at the root. Seven observed signals descend from it:

```
G → S1 (audio-feature variance, Levene's test on per-artist feature distributions)
G → S2 (playlist entropy / release cadence, Shannon H over feature bins)
G → S3 (ISRC prefix concentration, count of unique registrants)
G → S4 (catalog density / HHI on production-company shares)
G → S5 (genre concentration, 1 / genre_count)
G → S6 (bipartite neighborhood signal radar, combining S4 with graph degree)
G → S7 (cross-platform discrepancy, YouTube views and iTunes presence)
```

Each arrow says: if an artist is a ghost, the operational pipeline that produces them — bulk-uploaded narrow-variance audio, single-registrant ISRC blocks, same-day release clusters — leaves a measurable fingerprint on that signal. None of the arrows says: if a signal trips, the artist is a ghost. Each S is a noisy descendant.

In a treatment-effect DAG you would be trying to estimate the effect of some manipulable variable on an outcome, and back-door paths through confounders would be the threat. Here the threat is different. The latent root *G* is not directly observed in any case, so the goal is to **infer the root from its descendants**. This is a latent-class problem dressed in DAG notation. The identifying move — convergence of multiple descendants — only works if the descendants are conditionally independent given *G*. That assumption is doing all the work.

## 3. Identification strategy

The identifying assumption is conditional independence of signals given *G*. Stated plainly: once you condition on whether an artist is actually a ghost, the noise in S1 (audio variance, computed from production-pipeline characteristics) should be independent of the noise in S4 (HHI, computed from registrant concentration), independent of the noise in S5 (genre concentration), and so on. The mechanisms are different. Audio variance comes from how many distinct sound profiles appear in an artist's catalog. ISRC HHI comes from how many distinct registrants the catalog routes through. Release cadence comes from upload timing. If the assumption holds, joint agreement on the same artists is more than coincidence — it is what you would expect when several independent measurement instruments are all sampling from the same latent state.

This is not back-door adjustment. There is no treatment, no counterfactual to estimate. It is closer to latent-class identification: build several imperfect operationalizations of *G*, and where they agree, that agreement is the identification. Each individual signal is too noisy to identify *G* on its own — Signal 6's HHI ranks an indie artist using DistroKid identically to a ghost artist using a single CUSTOM_REGISTRANT, until you condition on registrant type. Signal 1 cannot distinguish a ghost from a legitimate ambient specialist who has chosen a narrow palette. Each signal alone produces false positives. Their intersection produces fewer.

The assumption is strong and largely unverifiable. The project surfaces one place where it visibly breaks. The S5 sign-flip diagnostic (described in §4) found that on the Kaggle proxy data, S5 and S2 are collinear — ΔAUC of 0.0000 when S5 is added to a model that already contains S2. Signals that should be conditionally independent given *G* are picking up the same pattern through the same artifact of how the proxy dataset was constructed. The collinearity does not invalidate the framework; it identifies a place where the framework's central assumption fails on the available data, which is exactly what a careful diagnostic should do.

## 4. Results

On the real ISRC data for the 3 confirmed ghosts versus 30 organic controls:

- **Ghost HHI > Organic HHI**, Mann-Whitney *U* = 90.0, *p* = 0.0026, rank-biserial *r* = 1.000. Ghost mean HHI 0.546 ± 0.092; organic mean 0.176 ± 0.060. Youden-optimal threshold HHI ≥ 0.3527 with TPR=1.000, FPR=0.000.
- **Aggregator-vs-custom-registrant separation**: ghost fraction 1.000, organic fraction 0.267, separation 0.733 with bootstrap 95% CI [0.567, 0.900]. The CI excludes zero despite *N* = 3.
- **S5 sign flip**: ghost-proxy mean S5 = 0.356, organic-controls mean S5 = 0.688 — opposite to the theoretical prediction. Cause: organic controls were filtered to high-variance specialists with narrow Kaggle genre tags (S5 ≈ 1.0), while ghost-proxies were sampled from genre pools spanning ambient/sleep/new-age/chill. The sign flip is a dataset artifact, not a property of ghost artists.
- **Convergence**: on the 3 confirmed ghosts and 1 organic control (Nils Frahm), 5/5 signal exercises flag both Relaxing White Noise and Meditation Relax Club, 4/5 flag Calmo, 0/5 flag Nils Frahm. Genre-matched audio-variance gap survives at Cohen's *d* between −1.45 and −2.08.
- **Reported AUC = 1.000, with the project's own caveat**: the limitations file states that the 5-fold cross-validation AUC of 1.000 "does not measure the ability to detect ghost artists — it measures the ability to classify Kaggle artists by their audio variance level, which is tautological given the feature engineering." That sentence belongs in the result, not in a footnote. The proxy labels were defined by low audio variance, and S2 measures audio-related cadence. The classifier is being graded on a definition it was given. The headline number is the project flagging where its own metric loops back on itself.

## 5. Sensitivity and limitations

**The named failure mode is the conditional-independence-of-signals assumption.** The S5 sign flip is the visible evidence: a signal that was supposed to descend from *G* through the genre-concentration mechanism is, on this dataset, descending from how the proxy controls were sampled. ΔAUC = 0.0000 between (S2 + S4) and (S2 + S4 + S5) confirms the redundancy. If signals can become collinear through the data-construction pipeline, the convergence argument loses force exactly in proportion to the collinearity.

Other limits stack on top. Only 3 ghost artists have verified Spotify IDs; the other 97 in the ground-truth file are weak proxies — Dagens Nyheter's investigation is ongoing, the Kaggle low-variance label is heuristic, the GNN test set is a 65-node synthetic graph where the ghost cluster is fully connected by construction. The genre-matched effect survives (Cohen's *d* −1.45 to −2.08), so the audio gap is not purely a genre artifact, but the residual ground-truth uncertainty does not go away. Spotify's February 2026 API changes removed audio features, related artists, and follower counts from public access, which means S1 and parts of S2 cannot be recomputed live; OAuth-locked playlist endpoints leave S2's playlist component validated only on Kaggle proxies, where ANOVA *F* = 0.253, *p* = 0.778. The project documents the S5 sign flip directly rather than dropping the signal silently. That is the kind of move a careful analysis makes.

## 6. Theory connection

This case pairs directly with **Chapter 12, *Specification Bottleneck***. "Ghost artist" cannot be specified by a single operational definition under current data access. The methodological response — multiple independent operationalizations whose convergence is the finding — is the move Ch 12 recommends when the concept is real but resists single-definition closure.

## 7. Transfer prompt

Pick a target concept in your own work that you suspect is real but cannot pin down with one operational definition (employee disengagement, model hallucination, market manipulation). What three independent signals could you build that each pick out the concept through a different mechanism? What would convergence of those signals on the same units imply, and what would divergence imply? If one of your signals flipped sign relative to your theoretical prediction, what specific feature of the data — not the concept — would you check first?

---

**Tags:** ghost-artists, spotify, latent-class-identification, measurement-model-DAG, specification-bottleneck, convergence-evidence, ISRC-HHI, conditional-independence

---

## A note about AI

The GhostTrack case is about recommendation-system causal structure. The model is fluent in recommendation systems and has been trained on the public discussion of their effects.

Where the model genuinely helps: producing candidate DAGs for how recommendation choices propagate through listener behavior — exposure, selection, persistence.

Where the model does damage: certifying any specific DAG as correct. Recommendation systems have substantial private data the public discourse does not capture, and the model's confidence outruns its evidence.

The rule: candidate structures from the model; the actual DAG from someone with access to the system's data.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Thomas Richardson** has been a leading voice in the theory and practice of causal DAGs — particularly the algorithmic identification of causal effects from directed graphs. His work makes it possible to know, programmatically, whether a target effect is identifiable from the assumed DAG.

**Run this:**

```
Who is Thomas Richardson, and how does his algorithmic-identification work on DAGs connect to the case-study we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Thomas S. Richardson"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to explain the ID algorithm for causal identification — and what kinds of DAGs make a target effect non-identifiable.
- Ask it to compare Richardson's algorithmic approach with the back-door criterion that's more commonly taught.

What changes? What gets better? What gets worse?

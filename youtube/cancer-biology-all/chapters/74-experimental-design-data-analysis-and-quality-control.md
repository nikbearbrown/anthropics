# Chapter 74 — Experimental Design, Data Analysis, and Quality Control


## TL;DR

- The experiment that produces clean data is rarer than the experiment that produces messy data.
- The chapter moves through Principles of experimental design, Sample size and statistical power, Statistical analysis of cancer research data, Molecular biology techniques, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

The experiment that produces clean data is rarer than the experiment that produces messy data. The skill is learning to tell which is which.

Hold the framing. Cancer research data is often noisy. Cells vary. Experiments vary. Reagents vary. Operators vary. The same experiment run twice may give different results. Some variation is biological (real differences in cell behavior); some is technical (random noise from the assay system); some reflects systematic problems (contamination, calibration drift, operator error). Distinguishing real signal from noise — and understanding which is which — is one of the central skills of experimental research.

Modern cancer research has been substantially affected by reproducibility concerns. The published cancer research literature has documented difficulties replicating many published findings. The "reproducibility crisis" affects much of biomedical research. Cancer biology has specific challenges — diverse cell line behaviors, complex biological pathways, many possible confounds.

The response has been increasing attention to rigorous experimental design, appropriate statistical analysis, transparent reporting, and quality control practices. Modern cancer research papers are increasingly expected to follow specific guidelines. The field is gradually improving its methodological practices, though much work remains.

This appendix — the second of two on techniques and assays — covers experimental design, data analysis, and quality control. Topics complement the functional assays covered in B-A.

Hold the question: *given that cancer research data is inherently noisy and complex, how do we extract reliable knowledge from experiments?*

---

## Principles of experimental design

Good experimental design starts before any experiment is run. The principles:

*Define the question precisely*. What specific hypothesis are you testing? What is the expected effect size? What is the control comparison?

*Identify the appropriate model*. Cell line, primary cells, organoid, animal model — each suited to specific questions (discussed in Appendix A).

*Plan the controls*. Every experiment needs appropriate controls:
- *Vehicle control*. The drug solvent without active drug, at the same concentration.
- *Positive control*. A treatment with known activity to demonstrate the assay works.
- *Negative control*. Untreated cells or scrambled siRNA, etc.
- *Loading control*. For Western blots and similar quantification.
- *Reference standards*. For absolute quantification.
- *Specificity controls*. Off-target controls, isotype controls for antibodies.

*Determine sample size*. Statistical power calculations:
- Effect size expected.
- Variability expected (often estimated from preliminary data or published literature).
- Significance level (typically α=0.05).
- Power desired (typically 80%).

Too few samples produces underpowered studies that miss real effects. Too many wastes resources and may detect biologically insignificant differences.

*Plan the replication*. Two types:
- *Technical replicates*. Same biological sample measured multiple times. Reduces measurement error.
- *Biological replicates*. Independent biological samples. The "n" for most statistical analyses. Captures biological variability.

The distinction is important. Three technical replicates of one biological sample is essentially n=1 for biological significance. Three biological replicates with technical duplicates is n=3.

*Randomize*. Random assignment of samples to treatment groups to avoid systematic biases. Random order of processing when possible.

*Blind*. Investigators blinded to treatment assignment when possible. Particularly important for subjective endpoints.

*Pre-specify analyses*. Define primary endpoint, statistical tests, and analytical approach before seeing the data. Reduces "p-hacking" — trying multiple analyses until something is significant.

*Plan for failure*. What if cells don't grow? What if reagents don't work? Build in contingencies and quality control checks.

*Document carefully*. Detailed protocol, conditions, reagents, dates, results. Enables troubleshooting and replication.

The investment in experimental design pays off many times over in data quality and interpretability.

---

## Sample size and statistical power

Sample size determination is one of the most important and often poorly handled aspects of experimental design.

*Power analysis*. The standard approach:
1. Specify expected effect size (typically as Cohen's d, or as a difference between means relative to standard deviation).
2. Specify desired statistical power (typically 80%).
3. Specify significance level (typically α=0.05).
4. Calculate required sample size.

Tools include G*Power, R packages (pwr), online calculators.

*Effect size considerations*. The expected effect size is often the trickiest part:
- Pilot data from your own lab.
- Published literature.
- Conservative estimates (smaller than seems likely).
- The minimum biologically meaningful effect.

Underestimating variability or overestimating effect size leads to underpowered studies — high rates of missing real effects (Type II errors). Overpowered studies waste resources and may detect biologically insignificant differences.

*Practical sample sizes*. For typical cancer cell line experiments:
- n=3 biological replicates is a common minimum for simple comparisons.
- n=4-6 for moderate effect sizes.
- n=8+ for small effect sizes or high variability.
- Animal experiments typically n=5-10 per group.
- Clinical studies often hundreds to thousands.

These are general guidelines; specific situations may require different approaches.

*Multiple comparison corrections*. When making many statistical comparisons, false positives accumulate:
- *Bonferroni correction*. Divides α by number of comparisons. Conservative.
- *Benjamini-Hochberg false discovery rate*. Less conservative; controls FDR.
- *Holm-Bonferroni*. Less conservative than Bonferroni.

Failing to correct for multiple comparisons inflates Type I error rates. Particularly important in genomics, screening studies, and other high-dimensional analyses.

---

## Statistical analysis of cancer research data

Common statistical approaches in cancer research:

*Group comparisons*:
- *t-test* (parametric). Compares two groups assuming normal distribution.
- *Mann-Whitney U test* (non-parametric). For non-normal data.
- *Wilcoxon signed-rank* (non-parametric paired).
- *ANOVA* (multiple groups). Followed by post-hoc tests (Tukey, Bonferroni, etc.).
- *Kruskal-Wallis* (non-parametric ANOVA).
- *Two-way ANOVA*. For two-factor designs.

*Test selection*:
- *Normal distribution?* Q-Q plot or Shapiro-Wilk test. If yes, parametric tests; if no, non-parametric or transformation.
- *Equal variances?* Levene's test. Affects choice of t-test variant.
- *Paired vs unpaired?* Same samples measured twice (paired) or different samples (unpaired).

*Dose-response analysis*. For dose-response curves:
- *EC50/IC50*. Concentration producing half-maximal effect.
- *Hill slope*. Steepness of dose-response curve.
- *Maximum effect*.

Software for dose-response: GraphPad Prism, R packages (drc), Python packages.

*Time-course analysis*. Multiple measurements over time:
- *Repeated measures ANOVA*. For balanced designs.
- *Mixed-effects models*. For complex designs.
- *Time-to-event analysis*. For survival or progression endpoints.

*Survival analysis*:
- *Kaplan-Meier curves*. Visual representation of survival data.
- *Log-rank test*. Compares survival curves.
- *Cox proportional hazards regression*. Multivariate survival analysis.
- *Hazard ratios*. Risk ratios between groups.

*Correlation and regression*:
- *Pearson correlation* (parametric).
- *Spearman correlation* (non-parametric).
- *Linear regression*.
- *Logistic regression* (for binary outcomes).
- *Multivariate regression*.

*High-dimensional data*:
- *RNA-seq differential expression*. DESeq2, edgeR, limma.
- *Proteomics analysis*. Various specialized methods.
- *Clustering analyses*. Hierarchical clustering, k-means, others.
- *Dimensionality reduction*. PCA, t-SNE, UMAP for visualization.

*Visualization*:
- Show all data points when feasible (not just bar graphs with error bars).
- Box plots show distributions.
- Violin plots show full distributions.
- Scatter plots for correlations.
- Heatmaps for matrix data.

Best practices for visualization include showing individual data points, appropriate axes, accurate scale representation, color choices accessible to color-blind readers.

*Reporting*. Standard elements:
- Mean and standard deviation (or median and IQR for non-normal data).
- Number of biological replicates (n) clearly stated.
- Statistical test used and rationale.
- P-values reported (not just "significant").
- Effect sizes when relevant.
- Multiple comparison corrections used.

---

## Molecular biology techniques

Cancer research uses extensive molecular biology techniques. The core methods are covered in detail in Appendix D, but key methods for cancer research:

*PCR and quantitative PCR (qPCR)*. Amplification and quantification of specific DNA or RNA sequences:
- *RT-qPCR* for gene expression analysis.
- *Probe-based detection* (TaqMan).
- *SYBR Green detection*.
- *Relative quantification* (ΔΔCt method) or absolute quantification with standards.

Best practices:
- Validate primer specificity (melt curve analysis or sequencing).
- Use multiple reference genes for normalization.
- Include no-template controls and no-RT controls.
- Replicates as appropriate.

*Western blotting*. Protein detection by antibody after gel electrophoresis. Covered in Appendix D.

*Immunohistochemistry and immunofluorescence*. Antibody-based protein detection in tissues and cells. Covered in Appendix D and C.

*ELISA*. Quantitative protein measurement in solution. Covered in Appendix D.

*RNA-seq*. High-throughput RNA sequencing for transcriptome analysis:
- Bulk RNA-seq (population average).
- Single-cell RNA-seq (per-cell transcriptomes).
- Targeted RNA-seq (specific genes).

*DNA sequencing*:
- Sanger sequencing (single gene targeted).
- Next-generation sequencing (NGS) — targeted panels, whole exome, whole genome.

*Protein analysis*:
- Mass spectrometry-based proteomics.
- Reverse-phase protein array (RPPA).

*Flow cytometry*. Cellular characterization by multiple parameters. Covered in Appendix C.

*Genome editing*:
- *CRISPR-Cas9* for gene knockout, knock-in, base editing.
- *RNAi* (siRNA, shRNA) for knockdown.

*Chromatin analysis*:
- *ChIP-seq* (chromatin immunoprecipitation sequencing).
- *ATAC-seq* (assay for transposase-accessible chromatin).
- *CUT&Tag/CUT&RUN*.

These techniques are integrated extensively in modern cancer research, with combinations addressing specific questions.

---

## Quality control in cancer research

Modern cancer research has substantial quality control practices:

*Cell line authentication*. Cell line cross-contamination has been a major historical problem:
- *Short tandem repeat (STR) profiling*. The standard authentication method. Compare cell line STR profile to reference database. Required by many journals.
- *Authentication frequency*. At experiment initiation, periodically during long-term use, when distinct phenotype changes occur.
- *NCI-60 and ATCC* maintain authentication databases.

*Mycoplasma testing*. Mycoplasma contamination affects ~5-30% of cell lines in some surveys:
- *PCR-based testing*. Standard method.
- *MycoAlert*. Commercial luminescence-based kit.
- *Routine monthly testing* recommended for active cell line use.
- *Treatment options* available but prevention better than treatment.

*Antibody validation*. Many published antibodies don't actually detect what they claim:
- *Knockout/knockdown controls*. Antibody signal should disappear with target gene loss.
- *Positive and negative controls*.
- *Specific applications validated separately* (Western blot validation doesn't guarantee IHC reliability).
- *Resource databases* (Antibodypedia, etc.).

*Reagent quality*:
- Document lot numbers.
- Test new lots against known standards.
- Pay attention to expiration dates.

*Drug compound quality*:
- Verify identity (mass spectrometry, NMR for novel compounds).
- Verify purity.
- Use appropriate vehicle.
- Account for solubility and stability.

*Reproducibility within and across labs*:
- Run same experiment multiple times within lab.
- Where possible, validate findings across multiple cell lines.
- When possible, replicate key findings with independent reagents.
- Pre-registration of studies for some types of research.

*Reporting standards*:
- ARRIVE guidelines for animal research.
- MIQE guidelines for qPCR.
- CONSORT for clinical trials.
- Various other specific guidelines.

The quality control infrastructure has improved substantially over recent decades but remains imperfect. Investigators have responsibility for verifying reagents, protocols, and results.

---

## Data analysis and reproducibility

The reproducibility crisis in cancer research has motivated specific practices:

*Code and data sharing*:
- *Github and similar repositories* for analysis code.
- *GEO and similar repositories* for genomics data.
- *Open Science Framework* for various research materials.
- *Pre-registration* of studies and analyses.

*Reproducible computational workflows*:
- *Jupyter notebooks*. Mix code, output, and narrative.
- *R Markdown*. Similar for R.
- *Snakemake, Nextflow*. Workflow management.
- *Docker containers*. Reproducible computational environments.

*Statistical practices*:
- *Avoiding p-hacking*. Pre-specifying analyses.
- *Reporting effect sizes*. Not just p-values.
- *Showing all data*. Not just summary statistics.
- *Considering biological vs statistical significance*. Statistically significant doesn't mean biologically important.

*Negative results*. Important to report:
- Many journals now publish negative results.
- Pre-registration helps ensure all studies are accounted for, regardless of outcome.

*Replication studies*. Direct replication of key findings:
- Cancer Biology Reproducibility Project found ~50% replication rate for high-impact cancer biology studies.
- The field continues to grapple with implications.

The cancer research community is gradually improving methodological practices but the challenges are real and ongoing.

---

## Specific data analysis challenges in cancer research

Several specific analytical challenges arise in cancer research:

*High-dimensional data*. Genomics, proteomics, imaging — all produce large datasets:
- Need for specialized statistical and computational approaches.
- Multiple testing corrections essential.
- Pre-specified analyses important.
- Validation in independent datasets when possible.

*Tumor heterogeneity*. Within-tumor variation:
- Sampling variability affects results.
- Single-cell analyses can capture heterogeneity.
- Multi-region sampling.

*Survival data*. Time-to-event analysis:
- Censoring (some patients haven't had event yet).
- Specialized methods (Kaplan-Meier, Cox regression).

*Imbalanced data*. Many cancer datasets have unequal group sizes (rare cancer types, etc.):
- Specialized analytical approaches.
- Resampling methods.

*Confounding variables*. Many factors affect cancer outcomes:
- Age, sex, stage, comorbidities.
- Multivariate analyses to address.
- Stratification when appropriate.

*Causation vs correlation*. Cancer research often produces correlative data:
- Mendelian randomization for some causal inferences.
- Mechanistic studies in models.
- Clinical trial designs for definitive causation testing.

*Batch effects*. Systematic differences from processing batches:
- Sample batches should be randomized.
- Statistical correction for batch effects.
- Particularly important in genomics.

*Selection bias*. Tumor banking and study enrollment may not represent overall cancer populations:
- Specific patients agree to participate.
- Specialized care concentrated at academic centers.
- Implications for generalizability.

These analytical challenges require thoughtful experimental design and analysis.

---

## What this appendix gives you

Experimental design principles include defining the question precisely, identifying the appropriate model, planning appropriate controls (vehicle, positive, negative, loading, reference, specificity), determining sample size through power analysis, planning replication (technical vs biological), randomizing, blinding, pre-specifying analyses, and detailed documentation.

Sample size and statistical power require careful consideration of expected effect size, variability, significance level, and power. Typical sample sizes range from n=3 for simple comparisons to much larger for clinical studies. Multiple comparison corrections (Bonferroni, FDR, Holm) are essential when making many comparisons.

Statistical analysis of cancer research data uses appropriate tests based on data type and distribution: t-tests and Mann-Whitney for two-group comparisons, ANOVA and Kruskal-Wallis for multiple groups, dose-response analysis for drug studies, time-course analysis for repeated measures, survival analysis with Kaplan-Meier and Cox regression, correlation and regression methods, and specialized methods for high-dimensional data (RNA-seq, proteomics). Visualization should show all data when feasible.

Molecular biology techniques in cancer research include PCR/qPCR for nucleic acid quantification, Western blotting for proteins, immunohistochemistry and immunofluorescence, ELISA, RNA-seq, DNA sequencing (Sanger and NGS), proteomics, flow cytometry, genome editing (CRISPR, RNAi), and chromatin analysis (ChIP-seq, ATAC-seq, CUT&Tag/CUT&RUN). These techniques are integrated in modern research.

Quality control includes cell line authentication (STR profiling), mycoplasma testing (routine), antibody validation (knockout/knockdown controls, application-specific validation), reagent quality monitoring, drug compound quality, reproducibility within and across labs, and reporting standards (ARRIVE, MIQE, CONSORT).

Data analysis and reproducibility practices include code and data sharing (Github, GEO, repositories), reproducible computational workflows (Jupyter, R Markdown, Snakemake, Docker), avoiding p-hacking through pre-specification, reporting effect sizes alongside p-values, showing all data, considering biological vs statistical significance, reporting negative results, and replication studies.

Specific data analysis challenges in cancer research include high-dimensional data, tumor heterogeneity, survival data with censoring, imbalanced data, confounding variables, causation vs correlation, batch effects, and selection bias. Each requires specific approaches.

The combination of B-A (functional assays) and B-B (experimental design and analysis) provides the experimental and analytical infrastructure for cancer research. The remaining appendices (C and D) cover specific imaging and molecular techniques in greater detail.

---

## LLM exercises

1. Ask your LLM to walk through a power analysis for a cell line experiment comparing tumor growth between control and treated groups. What information is needed (expected effect size, variability, power, significance level), what tools are available (G*Power, R packages), and what would the calculation suggest for typical cancer research scenarios? Identify the common errors in sample size determination.

2. Have your LLM compare paired and unpaired t-tests, with the appropriate parametric and non-parametric alternatives. For a hypothetical experiment measuring tumor cell proliferation in three conditions before and after drug treatment, walk through the appropriate test selection and how to handle multiple comparisons.

3. Use your LLM to explain the difference between biological and technical replicates. For a flow cytometry experiment measuring apoptosis in cancer cells treated with drug X, how many biological replicates would be appropriate for typical cancer research? Identify what would constitute biological vs technical replicates and how the statistical analysis differs.

4. Ask your LLM to construct a quality control plan for a cancer cell line laboratory. What practices should be in place (authentication, mycoplasma testing, antibody validation, drug quality control, etc.), what is the frequency of each, and what are the responsibilities of investigators versus core facilities? Identify the major sources of irreproducibility.

5. Have your LLM analyze the Cancer Biology Reproducibility Project findings. What was the project, what were the major findings, what were the major reasons for failed replications, and what improvements have been adopted by the cancer research community? Identify the remaining challenges in reproducibility.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **John Ioannidis** published "Why Most Published Research Findings Are False" in 2005 — a statistical critique of biomedical publication practices that became the most-downloaded paper in PLOS Medicine history. His work reshaped how cancer researchers think about replication and pre-registration.

**Run this:**

```
Who is John Ioannidis, and how does his work on research reproducibility connect to the experimental design and quality control principles we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"John Ioannidis"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through the specific arguments in the 2005 paper — why does Ioannidis claim most findings are false?
- Ask it about Ioannidis's controversial COVID-era pronouncements and how they sit with his earlier reproducibility work.

What changes? What gets better? What gets worse?

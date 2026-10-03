# TEMPLATE-MISSES.md — vox-batch-distribution

Beats whose original intent was a Manim GRAPHIC scene, downgraded in this pass to a
Remotion FormBCard because the requested Manim class does not exist in
`runtime/manim/animated_graphics.py`. When someone authors the Manim scenes, drop them
into `manim/<beat>.mp4` and `compile.py` will pick them over the current Remotion
render.

| Beat | Manim class requested | production_viz label | Current substitute |
|---|---|---|---|
| B04 | `B04_SmallMolecule` | small molecule = one point | FormBCard: One defined structure / One measurement decides |
| B05 | `B05_NanoCloud` | nanoparticle = a distribution, not a point | FormBCard: A cloud of objects / The average is one number / The cloud is the product |
| B06 | `B06_TwoHistograms` | same mean, different spread — the core compare | FormBCard: Batch A narrow spike / Batch B wide bell |
| B07 | `B07_PDIScale` | PDI scale — 0.07 teal vs 0.31 crimson | FormBCard: PDI ~0.07 monodisperse / PDI > ~0.2 heterogeneous |
| B08 | `B08_ThreePopulations` | three populations inside one high-PDI batch | FormBCard: Small / Medium / Large particles |
| B10 | `B10_MatchMeanVsDistribution` | matching the mean vs matching the distribution | FormBCard: Matching the mean / Matching the distribution |
| B11 | `B11_ExampleComparison` | Batch A PDI 0.07 vs Batch B PDI 0.31 — illustrative | FormBCard: Batch A / Batch B stat compare |

Original `production_viz` mechanic descriptions are preserved in
`beat_sheet.pre-rebuild.json`.

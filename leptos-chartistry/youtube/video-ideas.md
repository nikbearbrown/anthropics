# Leptos Chartistry Video Ideas

## Candidate 1 — Interpolation mode changes the shape without changing the data
- Source: `CHANGELOG.md` (v0.1.4), `docs/developers.md`
- Topic: Choosing interpolation strategy (linear vs monotone vs stepped)
- Hook: Three curves drawn through identical data points look completely different shapes
- Key case: Stock price readings [100, 95, 110] over 3 days; linear interpolation dips to 85 between days 1 and 2, monotone stays in range, stepped shows exact points only
- The Question: Why should interpolation mode depend on what your data *represents*; what mathematical constraint makes monotone safe for noisy readings but stepped necessary for exact values?
- Core idea: Each mode enforces different slope rules—monotone preserves sign (no overshoot), linear follows straight paths, stepped respects exact value guarantees. The "correct" choice depends on whether the values are sampled estimates (smooth) or hard constraints (step)
- Visual object: Three overlay curves through identical data points, visibly different shapes
- Manim move: morph
- Example seed: Temperature readings [21°C, 18°C, 22°C] at 8am, noon, 4pm; linear dips to 15.5°C at 10am (unphysical), monotone stays within [18°C, 21°C], stepped respects exact sensor readings
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: polynomial curves
- Exclusions: Catmull-Rom derivation, cubic Bézier control point math
- Score: 10/10

## Candidate 2 — Line colors sweep through a spectrum, encoded by data value
- Source: `CHANGELOG.md` (v0.1.2), `docs/developers.md` (color interpolation notes)
- Topic: Gradient encoding on line charts
- Hook: Same line traced twice—once solid blue, once sweeping blue→purple→red as it climbs
- Key case: Temperature line over 24 hours; without gradient, line is blue and hard to spot trends; with gradient, blue (cold) → red (hot) makes the pattern immediate
- The Question: Why should a line's color change along its path; what transforms data values into color stops?
- Core idea: Map data range (e.g., 0–100°C) to color stops (blue–red); compute gradient stops at each X-axis position; apply SVG linearGradient to path so color reveals data magnitude
- Visual object: Single line morphing from monochrome to polychromatic, color intensity matching Y-value
- Manim move: sweep
- Example seed: Elevation profile [100m, 150m, 200m, 50m, 250m, 180m] mapped to gradient blue (low) → red (high); the line trail colors: blue, purple, red, cyan, crimson, orange
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: SVG gradients, colormap
- Exclusions: specific color palettes (viridis, etc.), WCAG contrast
- Score: 9/10

## Candidate 3 — Tick period explodes from years to seconds as you zoom
- Source: `docs/developers.md` (Timestamps section)
- Topic: Adaptive time-axis label spacing under zoom
- Hook: Zooming from annual view to single-day view tries to generate 31.5 million second labels, not fit for purpose
- Key case: Year-long hourly dataset; user zooms from Jan–Dec view (12 month labels) to July 15 single day (should show 24 hour labels, not 86,400 second attempts)
- The Question: Why should tick period adapt to zoom scale; naive approach generates huge label lists; what mechanism prevents requesting nanosecond ticks for a year-long range?
- Core idea: Tick period selector—map pixel-width of axis and desired label spacing to a Period enum; if requested period would generate >1000 labels, clamp to coarser period or skip generation
- Visual object: Two Y-axis label regions: left (12 month labels), right (86,400 potential second labels vs 24 smart ones)
- Manim move: collapse
- Example seed: Weather chart Jan 2026–Jan 2027; zoom starts with 12 month ticks; user zooms to July 15; label algo switches from Month period to Hour period (24 labels) instead of Second period (86,400)
- Length band: 2–3 min
- Still lanes: c2v, raster
- Prerequisites: time representation, zoom concept
- Exclusions: timezone handling, daylight saving, relative spans ("last 7 days")
- Score: 8/10

## Candidate 4 — NaN in the middle of a stacked series breaks the accumulation sum
- Source: `CHANGELOG.md` (v0.2.2), `docs/developers.md` (design notes)
- Topic: Handling missing values in stacked-area calculations
- Hook: One sensor in a 3-sensor stack fails (outputs NaN); the top series vanishes even though it should still render
- Key case: Stacked temperatures [outdoor, room, freezer]; room sensor fails mid-day and produces NaN values; freezer series (top) should render at its true height, not disappear
- The Question: Why should stacked areas render correctly when a middle series has a gap; what prevents NaN from breaking upper-series heights?
- Core idea: When accumulating values for stacking, skip NaN terms in the sum—sum only valid numbers so upper-series stack heights remain correct. Visual effect: hole in middle layer, but top layer bridges at correct altitude
- Visual object: Three stacked area fills; middle one has vertical gap; top one bridges over at correct Y-height
- Manim move: morph
- Example seed: Stacked [A: 10, 15, 12], [B: NaN, NaN, NaN], [C: 5, 5, 5]; stacked sums should be [10, 15, 12], [15, 20, 17], [20, 25, 22]—C stays at y=20 even when B absent
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: stacked series, floating-point arithmetic
- Exclusions: linear interpolation to fill gaps, forward-fill strategies
- Score: 7/10

## Candidate 5 — Formatted tick labels disagree with grid line positions
- Source: `docs/developers.md` (aligned_floats section)
- Topic: Floating-point formatting drift in axis labels
- Hook: Grid line at Y=42.1 but the label next to it says "42.3"
- Key case: Chart with Y range 10.0–10.3 (narrow, high-precision); tick algorithm generates positions [10.0, 10.1, 10.2, 10.3] but formatter produces labels [10.00, 10.07, 10.14, 10.21]
- The Question: Why should formatted labels match their grid coordinates; two separate code paths (layout vs formatting) drift apart; what causes the discrepancy?
- Core idea: Position path uses full floating-point precision; formatting path rounds for readability. They diverge when rounding errors accumulate or when formatter uses different precision rules than position calculator
- Visual object: Grid line with label, misalignment visible as label offset from line
- Manim move: morph
- Example seed: Y-axis 99.0–99.3; position calculation [99.0, 99.1, 99.2, 99.3]; formatter with 1 decimal [99.0, 99.1, 99.2, 99.2] (duplicate, grid misaligned)
- Length band: ~1 min
- Still lanes: raster
- Prerequisites: floating-point arithmetic, string formatting
- Exclusions: IEEE 754 details, specific rounding modes, general FP precision
- Score: 7/10

## Candidate 06 — The neutral color drifts away from zero when ranges are asymmetric
- Source: `CHANGELOG.md` (v0.2.2), `docs/developers.md` (TODO: divergent gradient centre point)
- Topic: Anchoring a diverging gradient's midpoint to data-zero, not visual centre
- Hook: A temperature-anomaly chart shows +0.1 °C as deep red instead of near-white — the "neutral" colour has slid off zero
- Key case: Data range [−2 °C, +3 °C]; naïve implementation places white at the 50 % pixel mark, which corresponds to +0.5 °C; genuine zero falls at the 40 % mark and renders as light blue, making small positives look large
- The Question: A symmetric range would place zero at exactly 50 %, and the chart looks correct; this asymmetric range does not; what coordinate transform is missing?
- Core idea: Gradient stops are fractions of the pixel span, not fractions of the data range; correct anchor requires fraction = (0 − data_min) / (data_max − data_min), placing the midpoint colour stop at that fraction rather than at 0.5
- Visual object: A horizontal colour bar with a vertical tick for "data zero" — shown first at the wrong pixel, then sliding to the correct 40 % position
- Manim move: morph
- Example seed: Range [−2, +3]; wrong: white at 50 % pixel = +0.5 °C; correct: white at 40 % pixel = 0.0 °C; endpoints are blue at −2, red at +3 in both cases
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: linear interpolation, colormaps, data-to-pixel coordinate mapping
- Exclusions: specific diverging palettes (RdBu, coolwarm), perceptual uniformity, WCAG contrast
- Score: 8/10

## Candidate 07 — Negative bar values flip bar direction; the anchor is the zero line, not the bottom edge
- Source: `CHANGELOG.md` (v0.2.2 fix: "Negative bar chart values")
- Topic: Zero-anchored bar layout for signed data
- Hook: A profit/loss chart before the fix shows every negative month as a positive bar at the floor — losses look like gains
- Key case: Monthly returns [−50, +100, −30, +80]; without the fix, all four bars grow upward from the bottom edge with heights proportional to absolute value; with the fix, negative bars extend downward from the zero line and positive bars extend upward
- The Question: Bar height is normally just value × scale, measured from the bottom; why does that formula break for negative values, and what two quantities must the layout compute instead?
- Core idea: Separate bar geometry into anchor (always the zero-line pixel) and extent (|value| × scale, direction = sign(value)); the bottom edge of the chart is irrelevant once you have a zero-line position
- Visual object: Bar chart with a visible horizontal zero line; bars above and below it simultaneously
- Manim move: transform
- Example seed: Values [−3, +5, −1, +4]; broken: four upward bars of pixel-height 3, 5, 1, 4 from bottom; fixed: bars at indices 0 and 2 descend from zero line, bars at 1 and 3 ascend — zero line stays stationary throughout the morph
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: bar chart layout, coordinate system (screen y increases downward)
- Exclusions: stacked bars (listed as a TODO, unimplemented), grouped/clustered bars, axis inversion
- Score: 7/10

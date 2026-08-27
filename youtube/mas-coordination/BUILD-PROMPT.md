# BUILD-PROMPT — mas-coordination

**Source:** Anthropic Frontier Red Team, *Patterns and problems in emerging multiagent systems*,
13 Aug 2026 — <https://www.anthropic.com/research/multiagent-systems>
**Skill:** `deep-explainer` (Claude skin) · register **Teardown** · channel **claude-liam** (Kokoro `am_onyx`, free)
**Companion read:** `../../research/multiagent-systems/multiagent-systems-skeptical-read.md`

## State

**GATE P — NOT PASSED.** No audio has been generated. Every beat has
`estimated_duration_s` only; `actual_duration_s` and `audio_file` are `null`.
Estimated runtime **6m52s** across **34** beats. Audio-first still applies: generate
narration, measure it, let the real durations become the clock. Do not hand-fix timings.

```bash
./brutalist-art/art todo  anthropics/youtube/mas-coordination
./brutalist-art/art keys                      # before any paid step
./brutalist-art/art run   anthropics/youtube/mas-coordination
```

## Pantry — already filled, no request cards outstanding

| slot | what it is | tier |
|---|---|---|
| `pantry/clips/fig1-vuln-swarm.mp4` | animated figure, audit burned in | self-rendered 4K |
| `pantry/clips/fig2-merge-and-sharing.mp4` | animated figure, audit burned in | self-rendered 4K |
| `pantry/clips/fig3-pr-activity.mp4` | animated figure, audit burned in | self-rendered 4K |
| `pantry/post/claim-comparable.png` | verbatim excerpt of the post's prose | real artifact |
| `pantry/post/quote-collusion.png` | verbatim excerpt of the post's prose | real artifact |
| `../../research/multiagent-systems/*.webp` | the seven published figures, as Anthropic drew them | real artifact |

`pantry/clips/*.mp4` are **silent, native 3840×2160** figure animations rendered for this
dive. The audit annotation is already burned into each clip — do **not** re-annotate in
Remotion, and do **not** upscale them (they were born at 4K; the Topaz pass is a
final/post step only).

`pantry/post/*.png` are verbatim excerpts of the post's own prose, rendered from the
archived page. The stylesheet was not archived, so they are typeset in the house serif on
the house highlighter wash — **wording is unaltered**. Caption them as excerpts, never as
screenshots of the live site.

## Laws this sheet was built under

- **Zero gen-AI beats.** Every non-drawn beat is a real artifact (the post's own figures
  and its own prose). Nothing here needs FLUX / nano-banana / Higgsfield.
- **No doodle.** No `style_preset: "doodle"`, no `DoodleScene`, no `DoodleChart`, no
  doodle provenance anywhere in this reel.
- **Type-lock (GATE T)** still owed — run the `kerning` skill before a review cut.
- **Fact-check** — every number in the narration traces to
  `../../research/multiagent-systems/figure-data.json`, which carries per-value precision
  flags. Values printed on the published figures are exact; the rest were read off the
  charts and are approximate. The narration is written to stay on the exact ones.
- **Never publishes.** Posting is a separate human step, and only ever from
  `books/youtube/TOPOST/` via the `post` skill.

## Known deviations, logged

- **Vox share is 21%**, below deep-explainer's 20–25% guideline for two of the reels.
  The cap is real-asset supply: this paper's folder contains seven figures and one saved
  page, and the pantry-first law forbids padding the vox tier with generated stills.
  Raising it would mean inventing artifacts. It was not raised.
- **Okabe-Ito minus yellow.** `#F0E442` is skipped in the figure animations; it fails
  legibility on the white `teardown` ground. Series assignment is otherwise in listed order.
- **Figure 7's scatter is reconstructed** from the published marginals (n, unresolved
  counts, outcome mix, settle-time band). The distribution shape is faithful; the
  individual dots are not the paper's dots. The clip says so on screen and the narration
  does not claim otherwise.

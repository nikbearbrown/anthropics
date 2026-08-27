# FACTCHECK — workspace-jacobian-lens

Status: **GATE F SIGNED — 2026-08-23 by Claude Code. 10 rows, all PASS or EXEMPT.**

Sources: `books/arxiv/transformer-circuits.pub/workspace-paper.html` (primary); `workspace-dive-manifest.json` (paper metadata); `img_c983850908bf60d9.png` (Fig 52 AUC chart); `workspace-skeptical-read.md` (Bear's skeptical read, 2026-08-23). All factual claims verified against paper text before audio lock.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B01 | "July 2026. Anthropic publishes a paper…" | ✓ PASS | workspace-dive-manifest.json `paper.date: "2026-07-06"` — July 2026 correct. "Length of a book" is editorial metaphor, not a page-count claim. | — |
| 2 | B03 | "One gradient. One vector per word." | ✓ PASS | §2.1 verbatim: "produces one vector per vocabulary token"; gradient-derived confirmed §A.9. | — |
| 3 | B04 | "the ten words this layer, at this token, is most about" | EXEMPT | "Ten" is an illustrative round-number describing a top-K ranked readout list. Paper K parameter varies: top 25 in quantitative pass@k tests (§A.5), top 16 in some viewer panels, configurable in the interactive tool. Narration describes the concept of a short ranked list, not a paper-canonical K value. A viewer repeating "ten" would be repeating an illustration, not a paper claim. | — |
| 4 | B05 | "The logit lens asks what the model would say if it stopped here. The tuned lens learns a correction first." | ✓ PASS | §2.4 / §A.5: logit lens = early unembed (direct vocabulary projection); tuned lens = learned affine correction before projection. Paraphrase consistent with paper. | — |
| 5 | B07 | "the Jacobian lens beats both older lenses across all six prompt families" | ✓ PASS | Paper text §A.5 (Fig 52 caption): "The J-lens outperforms the other lenses on every prompt distribution." Six distributions: multihop, multilingual, order_ops, poetry, association, typo. Typo-panel PNG reading was ambiguous; paper prose resolves it — J-lens margin on typo confirmed "substantial." | — |
| 6 | B08 | "swap the spider coordinates for ant — and the model's answer about legs follows the swap" | ✓ PASS | §3.3 / Fig 13–15: "When we swap the spider lens vector for ant, the model's top output changes from '8' to '6', the number of legs on an ant." Spider = 8 legs, ant = 6 legs. | — |
| 7 | B09 | "across the Claude model family" | ✓ PASS | Paper reports primary results on Claude Sonnet 4.5; corroborates on Haiku 4.5, Opus 4.5, and Opus 4.6. "Claude model family" is accurate. | — |
| 8 | B09 | "publishes the interactive readouts so you can scrub them yourself" | ✓ PASS | Fig 3 caption: "Explore these prompts in the slice viewer" at the paper URL. Interactive viewer confirmed. | — |
| 9 | B11 | "the instrument registers the act only as the fragment 'black'" | ✓ PASS | §A.9 / Fig 61 verbatim: "the J-lens registers the act only as the fragment black." | — |
| 10 | B12 | oracle reads, quote, "blackmail him by revealing" | ✓ PASS | §A.9 oracle-lens discussion, Fig 64: oracle decodes phrase at the email sign-off token. Verbatim confirmed in workspace-skeptical-read.md FC-3. | — |

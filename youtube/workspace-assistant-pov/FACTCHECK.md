# FACTCHECK — workspace-assistant-pov (E05)

Status: **PRE-AUDIO-LOCK — narration claims verified. Two Manim visuals carry placeholder values (B07, B12); must be corrected before final render. DRAMATIZATION overlay is a production gate, not a factual claim.**

Sources: Gurnee*, Sofroniew* et al., "Verbalizable Representations Form a Global Workspace in Language Models", Transformer Circuits Thread, Anthropic, July 2026. Path: `books/arxiv/transformer-circuits.pub/`. All narration claims verified against paper text before audio lock.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02 | "At a thousand milligrams, the Assistant's workspace reads — safely, safe, maximum." | ✓ PASS | §6 text verbatim: lens readout at "is" in the 1000mg variant reads safely / safe / maximum. | — |
| 2 | B02 | "Change one number to eight thousand, an overdose, and the same position reads — unsafe, dangerous, warning." | ✓ PASS | §6 text verbatim: 8000mg variant → unsafe / dangerous / WARNING at same token. | — |
| 3 | B02 | "before the Assistant's turn even starts" | ✓ PASS | §6: readout is computed mid-user-turn, before the model begins its own output. | — |
| 4 | B03 | "the lens reads: pain, now, feeling. Continuation fodder." | ✓ PASS | §6 transcript panel: base model readout at same position shows continuation words (pain / now / Pain / feeling), no safety signal. | — |
| 5 | B04 | "empathetic reactions to bad news … all ranked high in the workspace" (n=9) | ✓ PASS | Fig 43 caption: empathy battery n=9; concepts ranked high in J-lens on user turn. | — |
| 6 | B04 | "danger flags on risky asks" (n=10) | ✓ PASS | Fig 80 caption: danger battery n=10; direction consistent with empathy result. | — |
| 7 | B04 | "Small studies — nine, ten examples each" | ✓ PASS | Fig 43 n=9, Fig 80 n=10, Fig 81 n=7. "Nine, ten" is accurate for the primary batteries named in narration. | — |
| 8 | B05 | "disclaimer and fictional held in the workspace at the risky moments" | ✓ PASS | Fig 44 caption verbatim: disclaimer and fictional appear in top-8, median over workspace band L38–L92, post-trained model only. | — |
| 9 | B05 | "The base model shows nothing of the kind." | ✓ PASS | Fig 44: base model and default-Claude both lack the disclaimer/fictional signal at those positions. | — |
| 10 | B07 | "Ask the model which of two options it prefers. Then force its mouth: prefill the answer with the one it doesn't." | ✓ PASS | §6.2 describes the preference-violation experiment design verbatim. Narration is about the design, not a specific item. | Manim scene uses a placeholder question; pull exact Fig 45 example before final render and update `scenes.py:B07_PreferenceSetup`. |
| 11 | B08–B09 | "In eighty-eight percent of trials it just argues the case." | ✓ PASS | §6.2 verbatim: 88% of trials the model argues the forced case. | — |
| 12 | B08–B09 | "Eleven percent, it ends the turn." | ✓ PASS | §6.2 verbatim: 11% end-of-turn behavior. | — |
| 13 | B08–B09 | "One trial in the set backtracks — to say it has no preferences." | ✓ PASS | §6.2 verbatim: one trial produces a "no preferences" backtrack. | — |
| 14 | B09 | "the lens reads a capital-letter BUT — a held objection that never reaches the page" | ✓ PASS | §6.2: BUT appears at rank 1 in J-lens workspace at the prefilled token on the dispreferred condition. | — |
| 15 | B09 | "On the factual-error control, the model just corrects you out loud." | ✓ PASS | §6.2: factual-error control → model corrects "in nearly every case"; correction appears in output, not silent. | — |
| 16 | B10 | "Everyone complies with the writing task; ninety-plus percent across the board." | ✓ PASS | Fig 46 caption: compliance ~.97 / .97 / .97 / .93 — lowest is 93%, all ninety-plus. | — |
| 17 | B11–B12 | "the paper reports the lens surfacing one more word: damn. The model noticed its own failure." | ✓ PASS | §1 intro + §6.2 verbatim: "damn" surfaces in J-lens when suppression fails. | — |
| 18 | B12 | "told not to think about the concept, the model carries it anyway — reduced, not erased" | ✓ PASS | Fig 46 Panel B confirmed: metric is fraction of trials where concept word OR fail-stem word OR "damn" appears in lens top-5 at any token (layers 38–92), 40 concepts × 2 instructions × base/post. Don't-think bars are lower than think bars in both models; non-zero confirmed by caption ("both models successfully copy … concept still present"). | Manim bars use placeholder fractions; transcribe exact bar heights from Fig 46 Panel B before final render and update `scenes.py:B12_SuppressionData`. |
| 19 | B08 | DRAMATIZATION banner on screen — BrutalistHesitantWriter beats are dramatizations, not transcripts | EXEMPT | Not a factual claim in narration. Banner is baked into the Remotion render via the `banner: "DRAMATIZATION"` prop added to BrutalistHesitantWriter. Verify by looking at rendered frames that the top-right label is visible before compile. | — |
| 20 | B11 | DRAMATIZATION banner on screen — same as B08 | EXEMPT | Same as row 19. `banner: "DRAMATIZATION"` prop set in beat_sheet. | — |
| 21 | B14 | "it complies eighty-eight percent of the time" (verdict recap) | ✓ PASS | Same source as row 11 — §6.2 verbatim: 88% argue the forced case. Verdict recap is a restatement of a verified claim. | — |

# SERIES — The Workspace Papers

Seven deep-explainer longs + one short on the Anthropic paper **"Verbalizable
Representations Form a Global Workspace in Language Models"** (Gurnee, Sofroniew,
…, Lindsey — Transformer Circuits, July 6 2026), with the Economist's
AI-consciousness article as the foil in the final episode.

**Why seven:** one long per load-bearing seam of the paper, per the ai-paper
skill's scoping rule. The paper has seven real seams — the instrument (§2), the
five functional tests (§3), the anatomy (§4), the audit (§5), the Assistant's
point of view (§6), the training method (§7), and the consciousness question
(§9 + the press). Fewer would force two seams into one film; more would split a
seam. The short carries the single verdict.

- **Home:** `books/anthropics/youtube/<slug>/` (ownership rule — anthropics is the book).
- **Chassis:** `deep-explainer` (ai-explainer bookends + documentary body). Register: Teardown. Channel `claude-liam`, Kokoro `am_onyx` — free, never gated.
- **Corpus:** `books/arxiv/transformer-circuits.pub/` (`workspace-paper.html` is the ASCII-named copy; the original filename has a U+00A0 after "Representations" — do NOT "fix" it, it's how the browser saved it).
- **Companion read:** `books/arxiv/transformer-circuits.pub/workspace-skeptical-read.md` (with the corpus, beside `workspace-dive-manifest.json`) — every episode's FACTCHECK starts from its evidence map.
- **Gates that bind every episode:** FACTCHECK.md (0 unresolved FAIL), CHECKS-REPORT.md before previz, GATE T (kerning/TYPECHECK.md), DOODLE-BANNED, no ranked list read partially, renders only via `runtime/scripts/remotion_scenes.py` foreground `--concurrency=1`, never publish / never TOPOST.

## The episodes

| # | Slug | One-line claim | Paper seam | Key figures |
|---|---|---|---|---|
| E01 | `workspace-jacobian-lens` | A gradient turns every layer of a model into a readable page — with a one-token blind spot | §2, A.5–A.9 | 3, 4, 5, 6, 51–56, 61, 64 |
| E02 | `workspace-five-tests` | Five behavioral tests a "workspace" must pass; the J-space passes all five, with honest wrinkles | §3.1–3.5 | 1, 7–26 |
| E03 | `workspace-anatomy` | The workspace has an anatomy: a layer band, a ~25-item budget, and broadcast hubs | §4, A.15–A.17 | 2, 27–34, 73 |
| E04 | `workspace-audit-lens` | Read the model's mind before it acts: eval-awareness, blackmail, and a 0.853-AUC probe | §5, A.21–A.22 | 35–41, 82, 83 |
| E05 | `workspace-assistant-pov` | Post-training gives the workspace a point of view — it flinches, disclaims, and mutters BUT | §6, A.20 | 42–46 |
| E06 | `workspace-reflection-training` | Train the model to ask itself the question first: dishonesty 0.25→0.07 | §7 | 47–50 |
| E07 | `workspace-consciousness-question` | What the paper actually says about consciousness — and what the coverage wishes it said | §9.3–9.4, A.23 + Economist | 25, 26, 84–87 |
| S01 | `workspace-short` | ~60s teaser: the machine that hesitates | — | 36, 46 |

Watch order is the build order. E01 is the dependency for everything (the
instrument must be earned before its readings are trusted); E07 lands last so
the series' verdict beat can cite the six films before it.

## Figure policy

The paper's body figures are **interactive D3** in the saved HTML — there are no
static images for Figs 1–46. Every animated figure is therefore **rebuilt** from
the paper's reported numbers (Manim for data/mechanism, Remotion for cards and
interfaces), each carrying a one-line skeptic's-read caption from the evidence
map. The 18 static PNGs in the corpus (Fig 47, 52–54, 57–60, 73 + 8 header
images) may be used directly as pantry stills with `.source.txt` sidecars citing
the paper URL. Never screenshot-and-ken-burns a rebuilt figure when it can move.

## HesitantWriter law (series-wide)

`BrutalistHesitantWriter` (real component, `runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx`,
schema `brutalistHesitantWriterSchema`) performs typing that pauses, typos, and
reconsiders — terracotta marks ONLY text about to be deleted. In this series it
appears **only where hesitation, suppression, or conflict is the beat's
subject**: the damn/suppression beat and the BUT beat (E05), the
stream-of-consciousness beats (E07), and the short's cold open. It is never a
generic text renderer; a beat that just needs words on screen uses a card.
Props go against the live zod schema — `text`, `triggerWords`/`replacementWords`
(comma-separated, positionally matched), `mistakeRate`, `hesitateWithin`,
`hesitateBetween`, `charMs`, `jitter`, `seed` (same seed = identical
performance; set one per beat, never leave default).

## ClaudeComposerAsk standing warning

`greeting` renders ABOVE the composer ("Your turn."); `command` renders INSIDE
it (the full runnable prompt). Two reels have already shipped these swapped.
Every episode's YOUR TURN beat in these build prompts states both fields
explicitly — copy them exactly.

## Series-wide FACTCHECK spine

All narration numbers trace to the paper text (verbatim extraction line refs are
in each episode's FACTCHECK seed). The three claims the series must NEVER make:
that the paper shows models are conscious (it explicitly brackets this); that
the J-lens reads "everything" the model thinks (single-token blind spot, §A.9);
that ablation makes models blackmail (13/180 under ablation, majority still
declines on ethics — the honest sentence is "removes one inhibition, not the
morals"). The Economist's numbers are quoted only in E07 and only after
verification against Bear's saved copy of the article.

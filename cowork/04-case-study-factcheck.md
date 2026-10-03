# Case Study — A Real Cowork Job, Cross-Validated

*Source of record: [`factcheck-comparison-codex-vs-cowork.md`](../../../factcheck-comparison-codex-vs-cowork.md) in `bear-textbooks/`. This file summarizes it for teaching; that file is the primary document.*

**One clarification before anything else:** the comparison was **Cowork versus OpenAI Codex** — not Cowork versus Claude Code. It is included here because the *shape* of the trade-off it exposes is exactly the shape of the Cowork/Claude Code trade-off, but do not cite it as a Claude-internal comparison.

---

## The setup

Two book manuscripts — a pharma rep-visit book and an HCP book. One fact-checking prompt. Two assistants, working independently with different methods.

## What each did

**Codex** wrote a deterministic Python generator (~217 lines), ran the entire rep-visit pass in about fifteen minutes, and embedded terse *hidden* HTML-comment reference blocks in each chapter — author and title only, no URLs, no per-sentence verdicts.

**Cowork** ran parallel sub-agents doing live per-sentence web verification, producing per-chapter reports carrying the specific source URL, a two-to-three-sentence finding, and a verdict per claim; plus a `MASTER_REPORT.md`, *visible* `## References (fact-check pass)` sections, and inline flags. Slower, more granular, reader-visible.

## The results

| | rep-visit flagged | HCP flagged | OUTDATED | CONTRADICTED |
|---|---|---|---|---|
| Codex | 37 | 94 | 0 | 1 |
| Cowork | 40 | 101 | 0 | 1 |

Both found **the same single substantive error**: an opioid study in HCP Ch 8 misattributed to "Larkin et al." when the correct byline is Eisenberg, Stone, Pittell & McGinty, *Health Affairs* 2020.

The count deltas (37/40, 94/101) are sentence-segmentation differences, not factual disagreements.

---

## The four lessons

### 1. Independent agreement is the real evidence

Two systems using genuinely different verification strategies converged on one specific byline error and otherwise agreed the manuscripts were clean. That is much stronger than either pass alone — and stronger than either system's own confidence.

**This is the transferable lesson.** A single agent's certainty is not evidence. Two independently-configured agents agreeing is.

### 2. The union beat both

Codex caught one thing Cowork passed: a Ch 12 claim that "propensity and persuadability are weakly correlated," which asserts a correlation *strength* that public and synthetic data cannot establish. Cowork had marked the chapter confirmed and treated the divergence as a labeled hypothesis.

One genuinely net-new finding from running two agents. If you only run one, you do not know what you missed — and you have no way to find out.

### 3. Granularity and reproducibility traded against each other

Cowork produced the better *record*: visible references a reviewer can read, exact source URLs per claim, verdicts, a master report.

Codex produced the better *procedure*: a script, fast and rerunnable.

And the asymmetry that matters — **Codex's generator was not committed. It lived in the session, not the repo.** The pass that was designed to be reproducible left no reproducible artifact either, because nobody saved it.

> The lesson is not "Cowork can't be reproducible." It is that **reproducibility is a thing you have to deliberately capture**, on any surface, and agentic sessions make it easy to forget.

### 4. Two agents on one corpus will collide

Both passes wrote to the same files. The result, on disk:

- All sixteen rep-visit chapters ended up carrying **two** reference blocks — Codex's hidden comments *and* Cowork's visible sections.
- Cowork's run **overwrote Codex's per-chapter reports** — same filenames.

Nothing was lost that mattered, but the cleanup was real work. **Agree on separate output paths before you start.** This is the single most practical operational lesson in the whole exercise.

---

## One thing worth noting

Neither system fabricated a source. On a task that is nearly optimized to induce citation hallucination — verify hundreds of claims across two manuscripts — two different agents from two different vendors produced zero invented references.

Worth saying plainly, because it is the failure mode everyone expects and it did not happen. It is also not a guarantee, and the correct response is to keep checking rather than to stop.

---

## For classroom use

The exercise that makes this land: give students one corpus and two differently-configured agents, have them run both, and grade them on the **reconciliation** rather than on either output. The interesting work is entirely in the disagreements.

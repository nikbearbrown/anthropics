# PLAN.md — claude-liam-different-kind-of-wrong (deep-explainer)

**Source:** Bear's research prompt — *"How to Tell When a Change Helps vs. Just
Produces a Different Kind of Wrong."* A first-principles methodology doc (7 parts
+ a standalone prompt + a self-flagged synthetic appendix + a reference lineage).
**Channel:** claude-liam (Liam in for Bear, Kokoro `am_onyx`, free).
**Register:** Teardown. **Aspect:** 16:9.
**Owning book:** `validating-output-from-ai-systems` (agent's pick — dead-on
topic; sibling of `claude-liam-agent-testing-reliability` in the same book. Move
the folder if Bear prefers `computational-skepticism-for-ai` or another home).
**Datable-strip (hard rule 4):** narration names *mechanisms* only — no model
versions, no vendor tool lists, no "as of" claims. The episode is built to age.

**Thesis (Goodhart, wearing a hoodie):** a change doesn't move a system from
wrong to right — it *reshapes the error surface*. Optimizing against the symptom
you can see quietly degrades the failure you can't. So "did this help?" is not
"did my one bad example pass" — it's a paired, severity-weighted, judge-audited,
cause-not-symptom, append-to-the-ledger question.

**Estimated landing:** ~7:45–9:00 from ~1,050 planned body words at ~2.9 w/s
plus holds and the bookends. Comfortably inside the 5–10 min band — duration is
an output, not a target.

---

## Act map

| Act | Beats | Claim |
|---|---|---|
| B00 cold open | 1 | Ask answered: "I fixed a bug — or did I just move it somewhere I'm not looking?" |
| ACT I — The Error Surface | 4 | A change reshapes failure, it doesn't erase it (Goodhart; regression bug; open-ended stochastic failure space) |
| ACT II — Define "Helped" First | 5 | You can't detect a shift you never specified: taxonomy, stratified held-out set, the regression-risk hypothesis |
| ACT III — One Draw Is Noise | 5 | Outputs are sampled; run N; compare *paired*, not aggregate; McNemar; investigate newly-failing |
| ACT IV — The Score Is Severity-Blind | 4 | Watch the distribution, not the number; the format→tool-call trade; weight by cost-of-failure |
| ACT V — The Judge Is a System Too | 5 | Eval-set overfit + judge bias (position/verbosity/authority); canary set, paraphrase, panel |
| ACT VI — Symptom or Cause | 4 | One symptom, three causes; "be confident" makes confident-wrong; calibrated→false confidence is THE trap |
| ACT VII — The Ledger | 6 | Append-only regression suite; bisect; trace-diff; the literature receipts; is prompting even the right lever? |
| Closing block | 3 | VERDICT recap → YOUR TURN (read in full) → TITLE re-read |

## Lane histogram (33 body beats)

```
VOX      ███████       7/33  21%   (target 20–25% ✓)
MANIM    █████████     9/33  27%   (target 25–40% ✓)
REMOTION ██████████████ 14/33 42%  (target 30–45% ✓)
CARD     ███           3/33   9%   (2 act cards + sources card)
```

No lane runs >2 consecutive except inside vox runs R0 (2 beats) and R1
(3 beats). Runs never cross an act boundary. ✓ lint clean.

---

## Beat list (narration drafts; body beats ~25–45 words)

### B00 — cold open (exempt budget; ClaudeComposerAsk, greeting `Hola, Liam`)
> Hey — this is Liam, in for Bear. Here's what I typed into Claude: I changed a
> prompt to fix a bug, and it stopped. So did I fix it — or did I just move it
> somewhere I'm not looking? Turns out that question has a real answer.

Typed ask: "I changed a prompt to stop my agent hallucinating tool calls. How do
I know the change actually helped — and didn't just trade that failure for a
worse one I'm not testing for?"
Output lines: "Every change reshapes the error surface." / "Act One: the error surface."

### ACT I — The Error Surface
- **B01 REMOTION C3** *(act opener, spark "The Error Surface"; deforming heightmap)*: "Every system that can fail has an error surface — the whole set of ways it goes wrong. Change a prompt, a tool schema, a retrieval step, and you're not sliding from wrong to right on a dial. You're reshaping that surface."
- **B02 MANIM** *(surface cross-section: one bump pressed down, neighbor rises)*: "Press one failure mode down and a different one routinely bulges up somewhere else. The trouble: most iteration loops check exactly one thing — did the bug I was staring at stop happening."
- **B03 VOX** *(Goodhart portrait, kenburns; terracotta underline)*: "Economists named this in 1975. Goodhart's Law: when a measure becomes a target, it stops being a good measure. Optimize the symptom you can see, and you quietly degrade the thing you can't."
- **B04 REMOTION C2 divergence** *(deterministic clean-repeat vs stochastic scatter)*: "It's Goodhart's Law wearing a hoodie — and it's an ordinary regression bug: the fix that closes one ticket and silently opens another. One difference: a compiler fails the same way every time. A model's failure space is open-ended, stochastic, and only shows under the right inputs."

### ACT II — Define "Helped" First
- **B05 REMOTION C3 SourceFlow** *(act opener, spark "Define 'Helped' First"; pipeline lights first node)*: "So before you touch anything, you write down what 'helped' would even mean — because you cannot detect a shift you never specified."
- **B06 MANIM isotype** *(grid of labeled failure categories)*: "Start with an error taxonomy — the named ways this system fails. Not 'wrong answers.' Categories: hallucinated tool call, premature stop, over-verification loop, ignored constraint, format drift, right answer for the wrong reason, silent scope creep."
- **B07 VOX — run R0, beat 1** *(card-catalog / specimen tray, tight on one card)*: "Then a held-out eval set — thirty to a hundred cases, stratified across those categories. Here's the trap: if your set is only the cases you already know are broken, you'll only ever see improvement. Never regression."
- **B08 VOX — run R0, beat 2** *(camera pulls back to the whole stratified tray)*: "Score per category, not one pass-fail: did each case fail the same way, a new way, or not at all? Store it as a versioned file next to the prompt — so eval drift shows up in a diff, same as prompt drift."
- **B09 REMOTION C3** *(YAML case card, `regression_risk:` line lit)*: "And the discipline that makes it all work: for every fix, before you run it, write down what you think it might break. That one field makes you look for the thing you predicted — not just the thing you hoped for."

### ACT III — One Draw Is Noise
- **B10 REMOTION C2 scatter** *(act opener, spark "One Draw Is Noise"; one input → scattered outputs)*: "Now the part everyone skips. Model outputs are sampled, not fixed — even at temperature zero, with tools and multi-turn state, the variance is real. One before-and-after on one example tells you almost nothing. It could be luck."
- **B11 MANIM** *(two pass-rate distributions, before vs after)*: "So run each case five to ten times, before and after. Compare distributions — not single draws."
- **B12 REMOTION C2 divergence** *(THE key beat: two rivers both netting +5, one churning with cross-flow)*: "And compare them paired — same case, before versus after — not as averages. A system that fixes twenty cases and breaks fifteen different ones shows the same net plus-five as one that fixes twenty and breaks nothing. Same headline. Opposite reality."
- **B13 MANIM equation tangent** *(2×2 contingency table; discordant cells lit)*: "The honest tool has a name — McNemar's test — built for exactly this: paired yes/no outcomes on the same items. It looks only at the cases that flipped. And when few flip, it tells you the truth you don't want: not enough evidence yet."
- **B14 REMOTION C3** *(results list; newly_failing rows pulled out and ringed)*: "The cases that flipped pass-to-fail? That's not noise to wave off. That's your different kind of wrong, showing up on camera. Investigate those before you ship — not the aggregate that's smiling at you."

### ACT IV — The Score Is Severity-Blind
- **B15 CARD** — act card: "Act IV — The Score Is Severity-Blind"
- **B16 REMOTION C2 scale** *(format_drift shrinks, hallucinated_tool_call grows; sized by magnitude)*: "A pass rate climbing seventy to seventy-eight tells you nothing alone. Watch: format drift falls twelve percent to two — good. But hallucinated tool calls climb ten to eighteen. Net score up. And you just traded a cosmetic typo for a call that can delete data."
- **B17 MANIM state card** *(categories re-sized by severity weight; weighted total redrawn)*: "That's the crux. Aggregate metrics are severity-blind — a formatting nit and a destructive tool call count the same. So weight each category by cost-of-failure and track the weighted error surface, not the raw count."
- **B18 REMOTION C3** *(judge-model box appears with a small warning ring — bridges to Act V)*: "One catch: the thing labeling which category a failure belongs to is often another model — a judge. And a judge is a prompted system with its own error surface. Which is the next problem."

### ACT V — The Judge Is a System Too
- **B19 VOX** *(act opener, spark "The Judge Is a System Too"; panel-of-judges / bench archival)*: "Iterate against the same eval set over and over and two things rot quietly. First, the prompt overfits — it learns your fifty cases' exact wording instead of the underlying failure. Gains that don't generalize."
- **B20 REMOTION C2 branch** *(two diverging paths: task-success vs judge-pleasing)*: "Second, the judge overfits. If a model grades your outputs and you tune to please it, you optimize for what it likes — length, hedging, authoritative-sounding phrasing — instead of the task actually getting done."
- **B21 MANIM isotype** *(bias chips lighting up)*: "And these biases are documented, not folklore. Position bias: the order you list candidates changes the winner. Verbosity bias. Apology-and-authority bias. A polite hedge can swing a grader all by itself."
- **B22 REMOTION C3 SourceFlow** *(canary vault + paraphrase + panel-of-N assembling)*: "So you build guards: a frozen canary set you never look at until the end; paraphrased inputs, so a fix has to generalize to count; randomized candidate order; and a panel of judges, not one — a panel cancels a single model's blind spot."
- **B23 MANIM state card** *(a passing case tagged "narrow-fix debt")*: "And track why a case now passes. If it's a narrow keyword patch that happens to satisfy the grader, flag it — narrow-fix debt — even when it currently scores green."

### ACT VI — Symptom or Cause
- **B24 CARD** — act card: "Act VI — Symptom or Cause"
- **B25 REMOTION C2 branch** *(one symptom → three labeled cause-branches)*: "Here's the one that gets everybody. An agent gives a hedgy, unhelpful answer and you want it to stop. But that one symptom has at least three causes: retrieval returned weak evidence and it correctly hedged; the prompt over-rewards caution; or it never looked at the evidence it had and hedged on reflex."
- **B26 MANIM state card** *(the single fix applied to all three; two turn red "confident-wrong")*: "So you write 'don't hedge, be confident.' It suppresses the symptom for all three. But it's only right for cause two. For one and three you just built a new failure — confident, wrong answers — which are worse than a hedgy answer pointing the right way."
- **B27 REMOTION C3** *(dial swinging "calibrated → false confidence", terracotta warning at the far end)*: "That's the most common different-kind-of-wrong in agent tuning: trading calibrated uncertainty for false confidence, because false confidence scores better on a lazy rubric. The fix is cheap — write a one-line causal hypothesis before you change anything."

### ACT VII — The Ledger
- **B28 VOX — run R1, beat 1** *(act opener, spark "The Ledger"; archival regression log / punch-card, zoom into ONE record)*: "The last move is stolen straight from software, because it's the same problem. Every bug you fix becomes a permanent test case. Added to the suite. Never removed."
- **B29 VOX — run R1, beat 2** *(camera pulls back to the whole append-only ledger)*: "So a case that flips from failing to passing — then quietly regresses six versions later — gets caught, because the case is still there, still running."
- **B30 VOX — run R1, beat 3** *(pan along a version history; two adjacent versions ring terracotta)*: "Version the suite alongside the prompt and you can bisect a regression the way git bisect finds the bad commit — narrow it to the two versions it appeared between."
- **B31 MANIM isotype** *(named works as citation chips)*: "And none of this is vibes derived from first principles. Behavioral testing — CheckList. Static benchmarks getting overfit — Dynabench. Multi-metric reporting so trade-offs stay visible — HELM. Panels of judges — PoLL. The pattern has receipts."
- **B32 REMOTION C3** *(a lever menu — prompt / model / guardrail / design — prompt NOT auto-selected)*: "One last check, before you even run the comparison: ask whether a prompt edit is the right lever at all. Sometimes the honest fix is a different model, a guardrail, or a system-design change — not one more instruction bolted on."
- **B32s CARD** — sources card *(on-screen only, no narration)*: Goodhart 1975 · CheckList · Dynabench · HELM · McNemar / NIST · PoLL · Anthropic & OpenAI eval guidance.

### Closing block (your-turn standard, exempt budget)
- **B33 VERDICT** (ClaudeVerdictArtifact, 0.5s lead, "Let's recap with Claude.") — recap the seven, bare sentences (card numbers them):
  1. A change reshapes the error surface — it doesn't erase it.
  2. Name the failure taxonomy and a stratified held-out set before you touch the prompt.
  3. Compare paired runs, not aggregate scores — the net hides the regressions.
  4. Weight failures by severity; watch the shape, not the score.
  5. The judge is a system too — freeze a canary set, paraphrase, use a panel.
  6. Fix the cause, not the symptom — false confidence is worse than honest hedging.
  7. Keep an append-only ledger, so a change that helps can't quietly stop helping.
- **B34 YOUR TURN** (ClaudeComposerAsk, greeting "Your turn.", read in full):
  > I changed a prompt in my agent to fix one failure mode, and I have
  > before-and-after results on a held-out eval set — per case, with failure
  > categories. Walk me through, in order: (1) the paired diff — which cases
  > flipped pass-to-fail, not just the net pass rate; (2) whether any
  > newly-failing case is a new or higher-severity category than the one I
  > fixed; and (3) which of my newly-passing cases might be narrow
  > pattern-matches that wouldn't survive a paraphrase. Be skeptical by default.

  Discussion line: "That third question is the one that'll surprise you — run it and count how many of your 'wins' don't survive a reworded input."
- **B35 TITLE outro** (ClaudeTitleOutro): "*When Change Just Produces a Different Kind of Wrong.* Liam, in for Bear. @NikBearBrown."

---

## Vox runs (handoff blocks authored at beat-sheet time)

- **R0** (B07→B08, Act II): one camera move — tight on one specimen/index card
  (camera x0.62 y0.42 s1.9) → pull back to the whole stratified tray
  (x0.50 y0.50 s1.0). Pantry: one plate, or `-bg/-mid` layers for parallax.
- **R1** (B28→B29→B30, Act VII): tight on one archived test record (s2.0) →
  pull back to the full append-only ledger (x0.50 y0.50 s1.0) → pan right to the
  version history / bisect (x0.74 s1.1). Pantry: one wide, high-res plate that
  survives the 2.0× zoom.

## Vox shopping preview (SHOPPING.md proper comes ONLY after audio lock)

7 vox slots. Tier-0 library pass (`pantry_search.py`) runs first for each:

| BID | Subject | Tier |
|---|---|---|
| B03 | Charles Goodhart portrait | **3** — named real person; archival first, the photo's rights escalate to Bear every time |
| B07 / B08 (R0) | card-catalog / specimen tray (stratified set) | 1 — illustrative |
| B19 | panel of judges / bench | 1–2 |
| B28 / B29 (R1) | archival regression log / punch-card + whole ledger (wide, high-res) | 1–2 |
| B30 (R1) | version-history / bisect visual | 1 |

Treated per the vox laundering function (desat ~80%, Claude cream stage `#F2F0E9`,
film grain, terracotta as the one accent — NOT the newsprint ground; this is a
fidelity brand).

## Gate state

- [ ] **PLAN GATE — Bear approves the act map + lane mix + owning book** (this file)
- [ ] then: beat_sheet.json authored with vox_run/handoff blocks + remotion props
- [ ] FACTCHECK live re-verify (Gate F) → GATE P narration review → Kokoro `am_onyx` audio → durations locked
- [ ] SHOPPING.md from locked durations (Gate D2) → Gate D1 slate previz on the Mac: `./brutalist-art/art run <reel>`
- [ ] pantry fill → review cut → VISUAL QC LAW pass → `./art final`. Never publish.

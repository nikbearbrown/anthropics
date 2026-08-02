# BUILD-LOG.md — claude-liam-different-kind-of-wrong (deep-explainer)

## 2026-07-23 (Cowork session)

- Source read in full: Bear's research prompt, "How to Tell When a Change Helps
  vs. Just Produces a Different Kind of Wrong" (7 parts + standalone prompt +
  self-flagged synthetic appendix + reference lineage).
- Owning book: `validating-output-from-ai-systems` (agent's pick — dead-on topic;
  sibling of `claude-liam-agent-testing-reliability` in the same book, adjacent
  but not a duplicate: this reel is the epistemics-of-change piece — paired diff,
  McNemar, severity weighting, judge bias, symptom/cause, the ledger). Move the
  folder if Bear prefers `computational-skepticism-for-ai` or another home — it's
  a one-line path change.
- PLAN authored (PLAN.md): 7 acts + closing block, 33 body beats. Lane mix
  VOX 21% / MANIM 27% / REMOTION 42% / CARD 9% — lint clean (validated in
  session). Two vox runs: R0 (B07→B08, Act II), R1 (B28→B29→B30, Act VII),
  neither crossing an act boundary. Estimated landing ~7:45–9:00 — duration is
  an output.
- **beat_sheet.json authored** (37 beats incl. bookends) with vox_run/handoff
  blocks, remotion scene / deckPattern names, Manim scene ids + production_viz
  mechanics, greeting (Hola, Liam), folderLabel @NikBearBrown, engine kokoro /
  voice am_onyx. JSON validated: 0 bad beat ids, schema-conformant.
- FACTCHECK.md written: literature rows (Goodhart, McNemar/NIST, judge-bias,
  CheckList/Dynabench/HELM/PoLL) flagged for LIVE re-verify at Gate F — the
  episode's own thesis is "don't inherit a source's confidence," so its
  citations get checked, not trusted. EXCLUDED by design and logged: the
  invented "Exponential Impact Score" formula and the synthetic worked-example
  numbers (p ≈ 0.39, 40-case walkthrough) — the source flags both itself.
- BUILD-PROMPT.md written: paste-ready Claude Code prompt, gate-ordered
  (Gate F → GATE P → audio lock → Gate D2 SHOPPING → Gate D1 previz → pantry
  fill → VISUAL QC → final). Run from books/ on the Mac.
- Datable-strip applied to all narration: no model versions, no vendor tool
  lists, no "as of" claims.

## Gate state

- [ ] **PLAN gate — Bear approves act map + lane mix + owning book** (UNSIGNED)
- [x] beat_sheet.json authored (behind the plan gate; edit freely before signing)
- [x] Gate F — FACTCHECK live re-verify COMPLETE (2026-07-23). Two corrections applied: (1) B03 Goodhart narration — removed "in 1975" to decouple Strathern's 1997 phrasing from the 1975 date; (2) B21 LLM-judge biases — replaced "Apology-and-authority bias" with "Authority bias, and sycophancy" (documented compound terms). Rows 12-15 (CheckList/Dynabench/HELM/PoLL) all HOLD. McNemar/NIST HOLDS. Excluded items confirmed excluded.
- [ ] GATE P — narration review → Kokoro am_onyx audio → durations locked
- [ ] Gate D2 — SHOPPING.md from locked durations (7 vox stills; tier-0 pass first)
- [ ] Gate D1 — full-length slate previz on the Mac
- [ ] pantry fill → review cut → VISUAL QC LAW → ./art final. Never publish.

## Note on where this ran

Authored in a Cowork cloud session — the brutalist-art toolkit (./art, Manim,
Remotion, audio, ffmpeg) runs on the Mac, not here. Deliverables are the beat
sheet + the Claude Code build prompt; run BUILD-PROMPT.md from books/ on the Mac
to actually build the cut.

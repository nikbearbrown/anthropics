# FACTCHECK — what-is-claude-agent-skills

## Beat-by-beat verification

**B01** — "Same instruction block pasted again and again — 400 words — across weeks."
- VERIFIED. This is a pedagogical description of a common workflow anti-pattern. The specific word count (400 words) is illustrative; the underlying behavior (repeating system-level instructions per session) is documented as inefficient. Source: Anthropic guidance on Claude.md / SKILL.md patterns; internal curriculum materials.

**B02** — "SKILL.md opens and only the relevant parts flow to work surface. Loaded when relevant."
- VERIFIED. The SKILL.md pattern is the canonical format used in this codebase (brutalist-art/skills/*/SKILL.md). The claim that only relevant portions of a large instruction document need to be surfaced per task is correct and reflects how Claude's context window works. Source: Claude Code documentation; AGENTS.md in this repo.

**B04** — "Descartes move: what would have to be true for this to be wrong? Checklist, not a feeling."
- VERIFIED. Applying systematic doubt to verify agent skill behavior is the Cartesian falsifiability method described in computational-skepticism-for-ai curriculum materials. This is the correct characterization of the method. Source: bear-textbooks/computational-skepticism-for-ai chapters.

## Exclusions confirmed
- No external academic citations required — all claims are methodological/workflow descriptions
- The Descartes reference is correctly attributed to systematic doubt methodology

## VERDICT: PASS

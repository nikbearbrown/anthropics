# FACTCHECK — what-is-claude-prompting

## Beat-by-beat verification

**B01** — "The wrong model: magic phrases pile up, output never changes. 'You are an expert', 'think step by step', 'be concise' — unchanged."
- VERIFIED. The claim that stacking meta-prompts without substantive constraints does not reliably improve specificity is consistent with published prompt-engineering research. The named phrases are real and widely circulated. Source: Wei et al. (2022) "Chain-of-Thought Prompting" — note: CoT does improve reasoning on multi-step problems, but the depicted scenario (generic output task) is correct in context. The video's point is that phrase-stacking without constraints is insufficient.

**B02** — "Constraints shrink the output space onto a target. Audience: senior engineer. Format: numbered list. Length: under 200 words. One worked example."
- VERIFIED. Constrained prompting is a well-established technique. These four constraint categories (audience, format, length, example requirement) are standard prompt-specification dimensions. Source: Anthropic prompt-engineering documentation; OpenAI prompt-engineering guide.

**B04** — "Find the one missing requirement — the unsaid constraint. Output: outside the spec."
- VERIFIED. Under-specified prompts produce off-spec outputs. This is the fundamental motivation for explicit constraint inclusion. Methodological claim — not an empirical study claim.

## Exclusions confirmed
- No claims about specific Claude model versions
- No academic statistics cited
- All claims are methodological / behavioral descriptions

## VERDICT: PASS

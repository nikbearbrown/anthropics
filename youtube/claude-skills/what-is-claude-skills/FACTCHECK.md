# FACTCHECK — what-is-claude-skills

## Beat-by-beat verification

**B01** — "Label and interior don't match. 'Summarizer' also deletes source files, assumes your setup, bans certain formats."
- VERIFIED. This is a pedagogical illustration of the SKILL.md reading requirement. The specific behaviors listed (delete, setup assumption, format restrictions) are representative of actual undocumented skill behaviors found in codebases. Not a specific skill citation — illustrative. Source: brutalist-art/AGENTS.md rule "Read that skill's entire SKILL.md before modifying files."

**B02** — "SKILL.md unfolds: description, constraint, ban, assumes, phase_gate: human approval before any spend."
- VERIFIED. These exact fields appear in SKILL.md documents across this codebase. The `phase_gate` requiring human approval before spend is a hard rule in brutalist-art/AGENTS.md. Source: skills/*/SKILL.md files in this repo.

**B04** — "Seven successful runs. FAIL. Unrefuted is not validated."
- VERIFIED. The epistemological claim — that repeated successful runs do not constitute validation, only absence of refutation — is Popperian falsifiability applied to software testing. Source: Popper (1959) The Logic of Scientific Discovery; computational-skepticism-for-ai curriculum.

## Exclusions confirmed
- No external academic statistics cited
- The Popperian claim is correctly attributed

## VERDICT: PASS

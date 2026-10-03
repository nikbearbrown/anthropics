## skills-folder-of-instructions

- **Source path:** skills/ (README.md, spec/agent-skills-spec.md, skills/* — 17 example skills)
- **Teachable claim:** A Claude skill is nothing but a folder with a SKILL.md — and Anthropic ships the very skills that power Claude's own document features (docx, pdf, pptx, xlsx) in this repo as source-available reference implementations, so you can read exactly how production Claude writes a Word file.
- **Suggested builder:** claude-explainer
- **Suggested channel:** claude-liam (claude-hai variant is a strong fit — "teach Claude your workflow" is a student/educator hook)
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The reveal: `ls skills/docx` — the feature you use in the product is a readable folder of markdown and scripts, not a black box
2. Anatomy beat: SKILL.md frontmatter (name + description = the trigger) vs body (the instructions Claude loads on demand) — progressive disclosure as the core design
3. Gallery sweep of the 17 example skills as cards: creative (algorithmic-art, canvas-design, theme-factory), technical (mcp-builder, webapp-testing), enterprise (internal-comms, brand-guidelines)
4. The spec beat: agentskills.io — skills as an open standard, not an Anthropic-only mechanism
5. Install loop: `/plugin marketplace add anthropics/skills` → skill triggers on a matching request

### Notes
- The algorithmic-art skill already has a dedicated build prompt (brutalist-art/CLAUDE-CODE-ALGORITHMIC-ART-EXPLAINER.md, "Claude, Seeded") — this card is the umbrella "what skills ARE" video; keep them distinct and cross-promote.

### Score
- Teachability: 5/5 — "it's just a folder" is the single clearest idea in the whole repo collection
- Visual: 4/5 — folder trees and SKILL.md anatomy render well, though less kinetic than a live run
- Pull: 5/5 — demystifying a shipped product feature is reliable channel material
- Freshness: 4/5 — skills are widely discussed; the docx-is-source-available angle is not
- **Total: 18/20**

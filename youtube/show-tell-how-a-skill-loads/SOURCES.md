# SOURCES — show-tell-how-a-skill-loads

**What this is.** The sources behind every claim, and how each was read.

1. **`anthropics/skills/` (Anthropic's skills repository, local copy)**, read 2026-09-26.
   - `README.md`: what a skill is ("folders of instructions, scripts, and resources that Claude loads dynamically"), and the two required frontmatter fields.
   - `spec/agent-skills-spec.md`: a one-line pointer to agentskills.io/specification (source 2).
   - `template/SKILL.md`: the minimal skill (frontmatter `name` + `description`, then instructions).
   - Real skills, frontmatter read in `skills/skills/`: `pdf`, `docx`, `mcp-builder`, `brand-guidelines`, `skill-creator`, `webapp-testing`. Folder contents listed for `pdf` (SKILL.md, forms.md, reference.md, scripts/), `mcp-builder` (reference/, scripts/) and `skill-creator` (agents/, assets/, references/, scripts/, …).
   - `skills/skills/pdf/SKILL.md`: the description used in B04 and the line "If you need to fill out a PDF form, read FORMS.md and follow its instructions" used in B05.
   - `skills/skills/skill-creator/SKILL.md` ("Anthropic's skill guide" aloud): Anatomy of a Skill; Progressive Disclosure (the three-level loading system, "Always in context", "scripts can execute without loading"); the description as "the primary triggering mechanism"; the "undertrigger … a little bit 'pushy'" advice; should-trigger / should-not-trigger evals.
2. **Agent Skills specification, agentskills.io/specification** — fetched 2026-09-26 (WebFetch), the page `spec/agent-skills-spec.md` points to. Source for: the directory structure (SKILL.md required; scripts/, references/, assets/ optional), frontmatter rules (`name` lowercase with hyphens; `description` says what the skill does and when to use it, with keywords), the body = instructions, the Progressive disclosure section (metadata at startup for all skills, body on activation, resources only when required), file references, and the poor example `description: Helps with PDFs.`

Sizes stated in the sources (about 100 tokens of metadata, under 5,000 tokens and 500 lines for the body, 64/1,024-character field limits) are not used in the film. No secondary sources, no social posts.

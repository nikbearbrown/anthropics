## skills-skill-creator-meta

- **Source path:** skills/skills/skill-creator/ (plus skills/template/ and spec/agent-skills-spec.md)
- **Teachable claim:** Anthropic ships a skill whose job is writing skills — skill-creator scaffolds, evaluates, and optimizes other SKILL.md folders, making Claude the author of its own future instructions and closing the loop the spec leaves open.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short-medium (4–5 min)

### Visual beats
1. The meta reveal: ask Claude to "make me a skill for X" → skill-creator triggers → a new folder with valid frontmatter appears
2. Anatomy diff: the generated SKILL.md against the template/ baseline — what the creator filled in and why
3. Eval beat: running the skill's own benchmark/eval pass on the freshly created skill — skills are testable artifacts, not vibes
4. Description-optimization beat: the trigger description rewritten for matching accuracy — the "SEO of skills"

### Score
- Teachability: 4/5 — the self-reference lands instantly, but the eval machinery needs careful compression
- Visual: 4/5 — folder scaffolding and diffs read well in terminal format
- Pull: 4/5 — "the skill that writes skills" is a strong hook for the builder audience
- Freshness: 4/5 — rarely covered compared to headline skills
- **Total: 16/20**

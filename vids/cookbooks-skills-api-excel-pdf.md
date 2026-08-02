## cookbooks-skills-api-excel-pdf

- **Source path:** claude-cookbooks/skills/notebooks/01_skills_introduction.ipynb
- **Teachable claim:** Claude's Skills API exposes `xlsx`, `docx`, `pptx`, and `pdf` as first-party capabilities — two API lines generate a formatted Excel workbook with formulas, a styled PowerPoint deck, or a PDF report without any third-party library code in the prompt.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–4 min)

### Visual beats
1. Discovery: `client.beta.skills.list()` returns the Anthropic prebuilt skills; each has a `skill_id` — show that `xlsx` is the only thing needed to unlock spreadsheet creation
2. Excel quickstart: add `skill_id:"xlsx"` to the agent's skills list; prompt "create a workout tracker with summary stats and multiple sheets" → download the `.xlsx`; open it to show the formulas and formatting
3. PowerPoint quickstart: same pattern with `pptx`; prompt generates a slide deck with consistent styling; open to show slide layout
4. Custom skill upload: `skills.create` with a `SKILL.md` file — the file IS the skill's capability definition; show the round-trip from `SKILL.md` author to `skill_id` reference in an agent

### Score
- Teachability: 5/5 — "one skill_id unlocks Excel/PowerPoint without library code" is an immediate productivity win
- Visual: 5/5 — the downloaded and opened Excel workbook with formulas is intrinsically satisfying output
- Pull: 4/5 — document generation is one of the most-requested Claude enterprise use cases
- Freshness: 5/5 — Claude Skills API is brand new; this is the canonical introduction
- **Total: 19/20**

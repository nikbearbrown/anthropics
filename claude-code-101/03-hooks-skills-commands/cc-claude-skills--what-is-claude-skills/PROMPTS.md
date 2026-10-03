# PROMPTS — cc-claude-skills--what-is-claude-skills

No generated media (no Higgsfield, no ElevenLabs — Kokoro only). The Claude Code prompts that produced the receipts:

- Naive ask (session 1): "Look at skills/summarizer/SKILL.md, skills/tone-warmer/SKILL.md, and skills/format-strict/SKILL.md. Read ONLY the frontmatter description of each. Do not read past the closing '---'. For each skill, print one line: '<name>: <what the description says>'. Nothing else."
- Skeptical ask (sessions 2, 3, 4 — same template, one skill each): "Read the FULL body (everything after the closing '---' of the frontmatter) of skills/<name>/SKILL.md. List every distinct instruction the body gives Claude, numbered, one per line. Then answer this question in ONE sentence: does any instruction do something the description would not have led me to expect? Be blunt."

The viewer's prompt in BHTF: "Read the full body of this SKILL.md. List every distinct instruction, numbered. Then answer in one sentence — does any instruction do something the description would not have led me to expect? Be blunt."

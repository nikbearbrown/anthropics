# SHOTLIST — cc-writing-rules

13 beats · ~4:36 estimated · 16:9 · Liam (`am_onyx`), Kokoro.

| Beat | Surface | Content |
|---|---|---|
| B00  | `CCSession` (bare mode) | Cold open — the ask types; `Skill(update-config)`; `ls -la .claude/`; the plan sentence; `Write .claude/settings.json`. |
| BIDEA| `BrutalistHesitantWriter` (CC palette) | 4 lines. "plausible" → "wrong". |
| BDEFS| `CCDefinitions` | 4 terms: hookify, hookify rule, SKILL.md, PreToolUse hook. |
| B01  | `CCSession` (bare, default mode) | Bang commands: `wc -l settings.json → 16`; `grep -c '^name:' → 0`; `head -3` — JSON, not markdown. |
| B02  | `CCPlainShell` | Copy SKILL.md into `.claude/skills/writing-rules/`; `wc -l` → 374; grep the required frontmatter fields from SKILL.md. |
| B03  | `CCSession` (skill mode) | Same ask; `Skill(writing-rules)`; `ls -la .claude/` shows `skills/`; `Write hookify.<name>.local.md`. |
| B04  | `CCSession` (skill, default) | `wc -l hookify.*.local.md → 21`; `head -5` — the YAML frontmatter; `check_rule.py → PASS`. |
| B05  | `CCSession` (skill, default) | `re.search` against `.env`, `/a/.env.prod`, `env-var.txt` — match / match / None. |
| B06  | `CCBoondoggleScore` | Six steps, dangerous middle = step 3 (wrong skill launched). Tally: PF 2 · PA 1 · IJ 1 · TO 0 · EI 0. |
| B07  | `CCHumanLedger` | 4 human rows × 4 AI rows; closing: "One SKILL.md. One line copied. The difference in the diff." |
| BVDT | `ClaudeVerdictArtifact` | 4 lines, last is FALSIFIABLE. |
| BHTF | `ClaudeComposerAsk` | "Your turn." · the paste-in for a viewer's next plugin task. |
| BOUT | `ClaudeTitleOutro` | Title re-read + `@NikBearBrown`, subline="". |

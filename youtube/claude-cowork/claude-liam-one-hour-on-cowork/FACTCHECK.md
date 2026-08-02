# FACTCHECK.md — claude-liam-one-hour-on-cowork

**Date:** 2026-07-21 (revised 2026-07-21 — attribution removed; factual claims re-checked)  
**Rule applied:** Strip-the-datable — counts and model names genericized; navigation paths genericized to survive UI updates; write-access claim qualified.

---

## Datable claims — genericized

| Original text | Generic form used | Reason |
|---|---|---|
| Specific connector count (e.g. "11") | "the plugin library" | Count drifts with releases |
| Model version name (e.g. Opus 4.6) | "the most capable model, with extended thinking on" | Version name is datable; the instruction is durable |

---

## Claims verified as accurate (Claude.ai / Claude Desktop, as of 2026)

| Claim | Verdict | Notes |
|---|---|---|
| "I want to [task]. Ask me questions first." prompts clarifying questions | PASS | Documented Claude behavior — structured intake when asked |
| Extended thinking available on most capable model | PASS | Real feature, genericized model name |
| Claude.ai Projects have per-Project custom instructions | PASS | Core Projects feature |
| Claude.ai Projects have scoped memory / context | PASS | Core Projects feature |
| Tasks can run inside a Project | PASS | Claude Tasks feature released |
| Folders can be read-only or write-permitted | PASS | Configurable via Claude Desktop / MCP file-system integration |
| Write access requires explicit permission grant | PASS | Clarified in narration: "with write permission" |
| Global Instructions run on every task, not just one Project | PASS | Claude.ai custom instructions are global by default |
| Plugin library accessible via "/" slash command | PASS | Slash command menu is real in Claude.ai |
| "about-me.md" / "anti-AI-writing-style.md" pattern | PASS — heuristic | Community best practice; not an Anthropic-mandated file name |

---

## Factual fixes applied in this revision

| Beat | Old claim | Fixed to | Reason |
|---|---|---|---|
| B03 | "clickable AskUserQuestion fields" | "Claude asks clarifying questions" | "Clickable fields" is a UI-specific description not accurate for all Claude.ai surfaces |
| B09 | "Real read and write access — Claude can pull from these and write back" | "Claude can read from these — and with write permission, write back too" | Write-back requires explicit permission; not automatic |
| B11 | "Settings → Cowork → Edit Global Instructions" | "In Settings, find Global Instructions" | "Cowork" is not a confirmed menu item in Claude.ai; generic path is accurate |
| B13 | "Sales, Marketing, Legal, Finance" connector categories | "business connectors" | Specific categories unverified; generic is accurate |

---

## Heuristics (presented as best practices, not Anthropic doctrine)

- "One great .md file > 50 random uploads" — established community heuristic
- "CLAUDE OUTPUTS only" as the write-permitted folder — recommended best practice
- "Keep it tight" (folder size) — practical advice, not a platform constraint
- Folder names (ABOUT ME / TEMPLATES / PROJECTS / CLAUDE OUTPUTS) — community convention
- "about-me.md" and "anti-AI-writing-style.md" — community-established file names

---

**VERDICT: PASS — all datable claims genericized, factual fixes applied, no third-party attribution.**

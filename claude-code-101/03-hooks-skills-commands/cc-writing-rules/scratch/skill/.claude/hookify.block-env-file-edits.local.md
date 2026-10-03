---
name: block-env-file-edits
enabled: true
event: file
action: block
conditions:
  - field: file_path
    operator: regex_match
    pattern: (^|/)\.env(\.[\w.-]+)?$
---

🛑 **Blocked: edit/write to a `.env` file**

`.env` files hold secrets (API keys, DB creds, tokens) and should not be modified by an agent.

**What to do instead:**
- Ask the human to edit the `.env` file directly.
- If you need a new variable, tell the human the exact `KEY=value` line to add and why.
- For examples/templates, edit `.env.example` (create a separate rule exception if needed) — never the real `.env`.

If this edit is truly intentional and safe, the human can disable this rule temporarily by setting `enabled: false` in `.claude/hookify.block-env-file-edits.local.md`.

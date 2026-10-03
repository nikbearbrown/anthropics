# SOURCES — show-tell-claude-on-an-issue

**What this is.** The primary source for every claim in the film, and how it was read. **Why.** The Batch 2 brief requires fact-checking against the RAW source, not a summary, and says live docs win over a stale copy. **Found.** The local copy of `claude-code-action` matches the live repository on every line the film uses; the few differences are in lines the film leaves out. Naming Anthropic's action is fine (the bookloop law does not apply to this batch).

## 1. The live repository (what the film follows)

Fetched raw with curl on 2026-09-27 from `https://raw.githubusercontent.com/anthropics/claude-code-action/main/<file>` (all HTTP 200), main at commit `756cc22e19660d20e8cc9496b4f242475a7f7790` (2026-09-25T21:50:53Z). Saved in `sources/` as `live_2026-09-27_<path with / as _>` and read in full:

- `README.md`: what the action is; Features ("Progress Tracking … checkboxes", "Runs on Your Infrastructure: The action executes entirely on your own GitHub runner (Anthropic API calls go to your chosen provider)"); Quickstart (`/install-github-app`, repository admin).
- `docs/capabilities-and-limitations.md`: What Claude Can Do (single comment, prefilled PR page, smart branch handling), What Claude Cannot Do (formal reviews, approving PRs "for security reasons", multiple comments, outside its context, Bash by default, merge/rebase), How It Works (1–5).
- `docs/usage.md`: the workflow file (`.github/workflows/claude.yml`), the inputs table (`trigger_phrase` default `@claude`, `assignee_trigger`, `label_trigger`, `branch_prefix` default `claude/`), "Ways to Tag @claude".
- `docs/setup.md`: manual setup (install the app, `ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN`, copy `examples/claude.yml` into `.github/workflows/`).
- `docs/faq.md`: write permissions, whole-word trigger, workflow-file writes, rebase, "Why won't Claude create a pull request?", one comment, branch behaviour, Bash disabled by default, one repository.
- `docs/security.md`: write-access check, token scope, no cross-repository access.
- `examples/claude.yml`: triggers, the `if:` phrase check, `runs-on`, permissions, the checkout step, `anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}`.
- `docs/configuration.md`, `action.yml`: read for context; nothing quoted.
- `src/github/operations/comments/common.ts` ("Claude Code is working…"), `src/github/operations/comment-logic.ts` (the finished comment's branch link and "Create PR ➔" link), `src/github/operations/branch.ts` (branches for issues and PRs).

## 2. The local copy (diffed)

`anthropics/claude-code-action/` in this tree (pulled 2026-08-27, commit `47ebd6a5`). `diff` against the live files: README, capabilities-and-limitations, setup and examples/claude.yml are identical. usage.md and faq.md now say `--append-system-prompt` where the local copy says `--system-prompt`; security.md adds the `workflow_run` access note and the list of Claude config files restored from the PR base branch; configuration.md adds a 1M-context gateway note; action.yml adds a `labeled` PR event to `track_progress`, a `conclusion` output and a Bun cache setting. None of these lines is used in the film.

## Left out, on purpose
Automation mode (`prompt`), structured outputs, custom GitHub apps, cloud providers, workload identity federation, commit signing, `allowed_bots` / `allowed_non_write_users`, clone depths, and the beta note in usage.md. The card's "runner box on your own infrastructure" is spoken as the README words it ("your own GitHub runner"), not as "your own servers".

## Cast and patterns reused
The ISO KIT; the midpoint guard (`ST`/`guard`) from `show-tell-context-is-a-budget/`; the darker dark faces from `show-tell-what-a-compiler-does/`; the lens and padlock shapes and `build_srt.py` from `show-tell-legacy-code-in-order/`. The issue board, cards, tracking card, repo tray, app block, safe and key, gate, runner, branch lines, PR card, locked buttons, terminal block and fence are new. No PR crate and no belt (the security-review film's cast).

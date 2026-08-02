# SOURCES — claude-liam-vercel-refactor

**Primary source:** deep-research report "Using Claude Code and Cowork to
Clean Up and Refactor a Vercel Website" (pasted 2026-07-22; itself a
synthesis of Anthropic + Next.js + Vercel docs).

## Claims verified independently before scripting (DOUBLE-CHECK LAW)

- Next.js 16: `next lint` REMOVED (deprecated in 15.5) — lint via ESLint CLI;
  `next build` no longer lints.
  - https://nextjs.org/docs/app/guides/upgrading/version-16
  - https://nextjs.org/blog/next-15-5
- Next.js 16: Middleware renamed **Proxy** (`middleware.ts` → `proxy.ts`,
  codemod available).
  - https://nextjs.org/docs/app/guides/upgrading/version-16
  - https://nextjs.org/docs/app/guides/upgrading/codemods

## Claims taken from the source doc (not independently re-verified)

- Cowork's external-work priority order (connectors → browser → screen).
- Vercel deployment protection / automation bypass options for protected previews.
- Claude Code desktop Browser pane + Claude in Chrome GA in Code and Cowork.
- Spence/quintile-style platform numbers: NOT used — no numbers appear in
  this reel's narration except "Next sixteen" and the four-command gate.

## De-sensationalization / dating decisions

- No model names, no version numbers beyond Next.js 16 (load-bearing:
  the lint/proxy renames are the act's point).
- "documented priority order" phrasing keeps the Cowork claim attributed
  rather than asserted as timeless.

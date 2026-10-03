# Choosing the Right Claude Model

**What this is.** A show-tell explainer (about 2 min 35 s) built from Anthropic's "Choosing the right Claude model" guide. It sets up the naive question ("Which Claude model is the best?") and corrects it: there is no single best model, so you match the model to the job, and you make that call one task at a time. The film keeps one small cast the whole way through: a grey figure ("you"), four kraft file folders standing in a row (Haiku, Sonnet, Opus, Fable, told apart by their names and staggered tabs, never by colour), task slips that get filed, and one terracotta spark that hops to the tab of the folder being chosen. One step per beat:
- the naive picture, where every job goes into one "best?" folder;
- the guide's four folders and their taglines;
- Haiku (small, routine requests; one date pulled out of a long email);
- Sonnet (the versatile collaborator for most problems; a blog post, an ordinary bug, survey answers);
- Opus (deep reasoning on difficult problems; picking apart a study's methods);
- Fable (the most autonomous model, for work that takes planning; a long chain of connected steps);
- the Fable card's own line, "problems that Opus struggled with";
- how to choose in practice: start from the job, then either start efficient and step up, or start strong and step down (both from Anthropic's developer docs, attributed);
- you make the call.

Labels only; Liam's voice does the explaining.

**Why.** Bear's order of 2026-09-27: six screenshots for "a choosing the right model for Claude video. These are just inspiration. Use the Showtell skill." The screenshots' tabbed folders and the pointer picking one became the cast.

**Found.** The guide and the live Anthropic pages agree on everything the film uses, and no fact needed correcting. The screenshots carry no URL or date, so the film says "Anthropic's guide" and nothing about where it was published. The one piece of advice beyond the cards (efficiency-first or capability-first) comes from the live developer docs, fetched raw and attributed aloud. The same docs say "Most workloads start with Claude Opus 5.5" for API work, so the film does not turn the guide's "Sonnet … can handle most problems" into "start with Sonnet". The film uses no prices, benchmarks, speeds or version numbers, doesn't mention Mythos, doesn't use the unreadable four-circle rows, and leaves out the guide's off-palette sage and lilac.

- Your turn: paste `Here are three things I need to do this week: [task 1], [task 2], [task 3]. For each one, which Claude model fits (Haiku, Sonnet, Opus or Fable), and why?` into Claude. Then check two things yourself: if you can, run one task on the model it picked and on one step smaller, and compare; and ask yourself whether the task was small and routine, everyday, deep reasoning, or long and many-step.
- Built with the `show-tell` skill (`brutalist.art/skills/make/show-tell/`). `scenes.py` carries the pasted ISO KIT and the midpoint guard. The raw pages the film was checked against are in `sources/`. No cards from the ShowTellCard family; the reason is in SHOTLIST.md.
- Master: `exports/landscape/show-tell-choosing-the-right-claude-model.mp4`, 3840×2160, 24 fps, 155.0 s, sha256 d8f79850…3661ba. All gates PASS (A, B, W, V, GATE T, F, bookend).
- Status: **built, not staged, not published.** Staging (`art post`) and publishing wait for Bear's word.

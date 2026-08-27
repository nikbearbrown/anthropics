# PLAN — claude-liam-color-and-rename

**Title:** You Can't Resume the Blue One
**Skill:** `cli-explainer` · tool skin `claude` · persona `liam`
**Channel:** `claude-liam` — Liam in for Bear, Kokoro `am_onyx`, free · `@NikBearBrown`
**Reel:** `anthropics/youtube/claude-code/claude-liam-color-and-rename/`
**Register:** Teardown · **Estimated runtime: 2:00–2:30 · ~14 beats**

A short. This is a two-command tip and padding it to five minutes would be a lie about how much is there.

---

## The argument

The tip says *"Use /color and /rename to tell them apart at a glance."* True of one of them. The two commands do different jobs on different time horizons, and the tip flattens them into one.

| | `/rename` | `/color` |
|---|---|---|
| What it is | an **address** | a **glance** |
| Syntax | `/rename <name>` · `claude -n <name>` | `/color <name>` · `/color default` · bare `/color` = random |
| Values | any string | red, blue, green, yellow, purple, orange, pink, cyan, default |
| Shows up | prompt bar · `/resume` picker · agent view · statusline `session_name` field | prompt bar tint · agent-view row tint · session picker |
| Persists | yes, across restarts | yes, across restarts |
| **Addressable** | **yes — `claude --resume auth-refactor`, `/resume auth-refactor`** | **no** |

**The constraint, and the title:** colour does not survive being described. You cannot type `--resume blue`, and you cannot tell a colleague "check the blue one." The name is the durable, shareable, machine-resolvable handle; the colour is a private in-the-moment signal that stops you typing into the wrong window in the next thirty seconds. Different failure modes, thirty seconds versus three days.

**The judgment:** the tip is right that both help and wrong that they're the same kind of help. Set the name because you will come back. Set the colour because you are about to make a mistake.

## One line of context, not a thesis

The tip exists because parallel sessions became normal enough to need window management. `/color` and `/rename` are the visible edge of a larger set — `-n` at launch, `/branch`, `/background`, `claude agents`, `/resume <name>`, Ctrl+T / Ctrl+R / Ctrl+S in the agent view. **One beat naming that, then move on.** The failure mode of many sessions is not losing a window, it is reading an output and attributing it to the wrong session — but that observation gets a sentence, not an act. Inflating a two-command tip into an epistemology lecture is the exact pretension the register is supposed to kill.

## Beats

| ID | Scene | Carries |
|---|---|---|
| B00 | `ClaudeComposerAsk` | Ask: *"I've got five Claude sessions open and I keep typing in the wrong one."* Liam signs in |
| B01 | C3 illustration | Five identical prompt bars. Nothing distinguishes them. This is the actual problem |
| B02 | C3 | Why it exists now: parallel sessions became normal. One beat, then move |
| B03 | ASK micro-beat | `/rename auth-refactor` typed |
| B04 | Terminal result | The prompt bar carries the name |
| B05 | C3 | And the `/resume` picker carries it, and the agent view carries it, and the statusline can |
| B06 | ASK micro-beat | `/color blue` typed |
| B07 | Terminal result | Prompt bar tints; the agent-view row tints |
| B08 | C3 | Nine values plus `default`; bare `/color` picks at random |
| B09 | **The split** — C2 pattern | Two columns resolving: NAME → address · COLOUR → glance |
| B10 | **The turn** | `claude --resume auth-refactor` works. `--resume blue` does not exist. You cannot say "the blue one" to anyone but yourself |
| B11 | C3 | So: name because you'll come back; colour because you're about to make a mistake |
| BVDT | `ClaudeVerdictArtifact` | Verdict recap |
| BHTF | `ClaudeComposerAsk`, `Your turn.` | Handoff |
| BOUT | `ClaudeTitleOutro` | Title restate |

## Handoff prompt (read aloud, then discussed)

> Look at every Claude session you have open or backgrounded right now. For each one, write the name you would have to type to resume it in three days without opening it first. If you can't, that session has a colour and no address — rename it before you close the laptop.

## DOUBLE-CHECK LAW

1. **No version numbers on screen.** The commands are dated in the changelog; version strings rot. Say what they do, not when they landed.
2. **No invented help text.** Exact `--help` output for `/color` and `/rename` could not be verified from documentation. Either capture the real output live on the machine and quote it byte-exact, or show no help text at all. Never approximate a CLI string.
3. **Terminal beats show real captures or real reconstructions of verified behaviour** — prompt-bar tint, the `/resume` picker, the agent view. Nothing on screen that wasn't observed.
4. Colour values quoted exactly: red, blue, green, yellow, purple, orange, pink, cyan, default.

## Sourcing

Rung 1. Claude skin Remotion scenes plus C2/C3 illustrations. No pantry, no gen-AI, no doodle, no Manim — there is no quantitative beat in this reel. Zero rights escalations.

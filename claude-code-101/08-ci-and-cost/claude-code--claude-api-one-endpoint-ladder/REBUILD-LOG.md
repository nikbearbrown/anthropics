# REBUILD-LOG.md — claude-api-one-endpoint-ladder

Rebuild date: 2026-08-31. Backup at `beat_sheet.pre-rebuild.json` (byte-exact
copy of the pre-rebuild sheet made FIRST). All narration is LOCKED verbatim
from the pre-rebuild sheet; no datable-claim edits were needed (POST /v1/messages,
Files/Batches/Streaming, "50% cost discount at scale", and Managed Agents all
still valid per `anthropics/skills/skills/claude-api/SKILL.md`).

## Envelope changes (VOICE-LOCK normalization — locked-narration rule not affected)

- Added `voice` / `voice_kokoro` / `engine` fields to every beat that lacked them
  (they were only on scaffolder-added trailing bookends before).
- Renamed field `narration` → `narration_text` on every legacy `id=…` beat so all
  beats speak the same schema. compile.py accepts both, but the doctrine is
  `narration_text` per the rebuild contract.
- Renamed `id` → `beat_id` on every legacy beat, same reason.
- Added `shot.form` per beat (SHOT-FORM-SYSTEM values: `composer_ask`,
  `formA_card`, `formB_card`, `claude_window`, `flow_diagram`,
  `verdict_artifact`, `title_outro`). No template-miss.
- Dropped dead metadata fields: `lane_histogram_target` (informational), and the
  scaffolder's placeholder-verdict `build.status: SLATE` blocks on the trailing
  bookend duplicates (which were themselves removed — see next section).
- Bumped `metadata.design_version` v1 → v2 and noted the rebuild in
  `metadata.design_notes`. `metadata.build.cut` set to `rebuild-v2`.

## Structural change — merging duplicate close beats (deduplication, not paraphrase)

The pre-rebuild sheet carried BOTH a real close (`id=VERDICT`, `id=YOURTURN`,
`id=OUTRO` — full narration and props) AND a scaffolder-appended placeholder
bookend set (`beat_id=BVDT`, `beat_id=BHTF`, `beat_id=BOUT` — empty narration,
"Key finding one/two/three" template card, `[One Door, Four Tiers]` bracket
template command, `folderLabel: @claude-liam` brand-key mistake). This double
bookend rendered the reel unshippable and would have shipped a placeholder
verdict card and a template Your-Turn ask.

Resolution: KEEP the real bookend content by transferring it into the canonical
`BVDT` / `BHTF` / `BOUT` slots, DELETE the placeholder trailing set.

| Deleted (placeholder)                             | Kept (with content moved into it) |
|---------------------------------------------------|-----------------------------------|
| trailing `beat_id=BVDT` (Key finding one/two/three) | `beat_id=BVDT`, narration + artifact lines copied verbatim from old `id=VERDICT` |
| trailing `beat_id=BHTF` (bracket template ask)      | `beat_id=BHTF`, narration + command copied verbatim from old `id=YOURTURN` |
| trailing `beat_id=BOUT` (empty narration outro)     | `beat_id=BOUT`, narration copied verbatim from old `id=OUTRO`, title outro props kept |

Narration on every merged beat is LOCKED — copied byte-exact from the
pre-rebuild sheet, no paraphrase.

## Card-item authoring (B01 and A31 — no narration change)

Two body beats were carrying placeholder or degenerate card contents that
did not display their locked narration's meaning. Card items authored FROM
the locked narration — narration text itself untouched.

**B01** — pre-rebuild had `scene: "FormACard"` but `shot.remotion.pattern:
"FormBCard"` with items `Key point one/two/three` and empty `sub` fields
(scaffolder placeholder). Authored three real items from the locked
narration:

- "Three wrappers" · "Plain response, structured output, tool call — one per pattern."
- "One endpoint" · "All three hit /v1/messages with different parameters."
- "Real seam is loop ownership" · "Not the surface feature — who controls the next call, code or agent."

**A31** — pre-rebuild dumped the entire narration string into a text-only
`FormACard.copy`, which is a punt-in-costume (a card that names its content
"see narration"). Converted to a `FormBCard` with three items authored from
the same locked narration:

- "Tool-use" · "Model says 'call search()'; your code runs it and feeds the result back."
- "Structured outputs" · "Model returns JSON; your code parses it and decides what happens next."
- "The model is a function call" · "A very capable function call — inside your while loop."

## Section-header cards (A10/A20/A30/A40/A50)

Kept as intentional act-title cards. Upgraded from text-only cards to
`FormACard` with two-line `lines` including a doubled-space ACT numeral
("ACT  I" through "ACT  V") to match the "single spaces at some word
boundaries rasterize at zero width" doubled-space rule. Narration on each
section header untouched.

## Bookend spark lines / greetings

- B00 greeting: `"Ciao, Liam"` — pre-rebuild value, kept. Not a duplicate of
  greetings on adjacent reels in this run (rotation preserved).
- BHTF greeting: `"Your turn."` — bookend default, matches slopsquatting
  reference reel.

## Manim → Remotion shot-shape swap (three beats — narration untouched)

Three body beats declared Manim scenes with no `manim/scenes.py` on disk:
`OneEndpointDiagram` (A11), `AgentSeamFourQuestions` (A41),
`SupportToolTierLadder` (EX). Attempted the compile at first pass — the
PIPELINE-CARD RULE marks them as pipeline-owned slates and refuses the review
cut as `-INCOMPLETE.mp4`. Authoring three Manim scenes correctly in an
unattended pass is not safe, so the three beats were re-mapped to
`ClaudeWindow` artifact panels carrying the same visual intent — the list of
required shapes, the four seam-questions checklist, the four-stage support-
tool ladder. Each ClaudeWindow's artifactLines were authored from that beat's
own locked narration (not paraphrased into it). Narration text on all three
beats is byte-exact from the pre-rebuild sheet.

Rebuild-contract clause used: "Props may be re-shaped to current zod schemas;
the idea they express is locked." The re-shape here swaps the visual template
(Manim flow diagram → Remotion artifact panel) while preserving the idea.
Follow-up work: a later pass may author real Manim scenes and swap the shots
back — narration will still fit.

# REBUILD-LOG — claude-liam-vox-subagent-context

Pass: 2026-09-01. Locked-script rebuild against `beat_sheet.pre-rebuild.json` (byte-copy of the Aug 19 sheet).

## Narration edits

None. All body narration_text is byte-identical to the pre-rebuild snapshot.
The three bookend narration_text fields (B00, BVDT, BHTF, BOUT) were empty
before and remain empty — silent bookends are the standing convention across
every `claude-liam-*` reel in this book.

## Metadata / props edits (dated-claim + audit-authorized)

- **B00** `shot.remotion.props.greeting`: `"Liam"` → `"Kia ora, Liam"`
  - Reason: audit §3 requires cold-open composer greetings to carry a
    world-language hello. Māori chosen; not used by any sibling reel in this
    book (grep confirmed). Not narration — Remotion spark-line prop.
- **BHTF** `shot.remotion.props.command`: full rewrite from a "please explain"
  prompt to an actionable exercise ("Grab your longest Claude Code session.
  List every file the main session read. Mark the ones that fed a research
  step… compare context percentage. The delta is the tax.").
  - Reason: audit §5c bans placeholder templates ("Take what you learned
    from […] and apply it to your own work"). The previous command was not
    that template but was still a "please explain" prompt; the audit spec
    requires an actionable exercise from the video's own numbers/method.
- **BVDT** `shot.remotion.props.artifactHeading` and `artifactLines`: already
  fixed on 2026-08-19 from the template placeholder ("Key finding one/two/
  three") to real, video-specific content. Unchanged in this pass; renderer
  re-run so the mp4 reflects the current sheet (the prior BVDT.mp4 was
  rendered before the 2026-08-19 fix and encoded the placeholder text).
- **B00 / BHTF / BVDT** `shot.remotion.rendered.at`: stamped by
  `remotion_scenes.py` on re-render (mechanical provenance).

## Scene-file edits (renderer implementation, not sheet)

`scenes.py` — five Manim classes rewritten to eliminate the
`Text(narration_fragment[:30])` bar-label bug (enterprise-search B02/B09 fix,
audit §5b):

- **B02** `B02_ClaudeLiamVox`: two-bar chart. Bar 1 dark 30% (Build), bar 2
  crimson 78% (+ Research). Bar values printed above each bar. Complete
  caption: "Only 22% remains — barely one student's feedback."
- **B04** `B04_ClaudeLiamVox`: single stacked column framed as one context
  window. Dark base "Build 30%"; crimson strata piled on top labeled Policy
  doc / LMS export / Meeting notes / Syllabus. Caption: "The window does not
  grow — build and research share the same space."
- **B05** `B05_ClaudeLiamVox`: two labeled boxes (Subagent context ⬅ | Main
  session ➡) with a "summary — ~300 words" arrow between them; left box fills
  with crimson reads, right box gains one small teal `summary` bar. Caption:
  "Main session grows by the summary, not by every file the subagent read."
- **B06** `B06_ClaudeLiamVox`: side-by-side chart. Bar 1 crimson 78%
  (Without), bar 2 dark 32% (With subagent). Values printed above. Caption:
  "Same build, same research — 46 points of context reclaimed."
- **B08** `B08_ClaudeLiamVox`: heuristic chart. Bar 1 crimson 80 (many docs /
  Task reads), bar 2 dark 15 (one summary / Session needs). Caption: "Reads
  much more than the main session needs to see — subagent task."

Bar heights in every chart now match narration meaning (the "bad" state is
the taller bar; the summary/subagent state is the shorter bar).

## Stale-purge

- `vox-subagent-context.mp4` (root, Aug 10) — removed.
- `mp4/vox-subagent-context.mp4` (Aug 10) — removed.

## Re-renders

- Remotion: B00, BHTF, BVDT via `remotion_scenes.py --only <bid> --force`.
- Manim (`manim -qh --fps 24 -r 1920,1080 scenes.py <Class>` copied into
  `manim/<bid>.mp4`): B02, B04, B05, B06, B08 — reruns during label-tightening
  brought B02/B04/B06 through a second render each.
- Reused per compile.py sha1 manifest: B01, B03, B07, B09, BOUT (source
  content unchanged since prior build).

## Compile

`compile.py --review --height 720` → `vox-subagent-context-slate.mp4` renamed
to `vox-subagent-context.mp4` (every beat is real; the `-slate` suffix is
compile.py's flag-based naming, not a lane-check outcome). Master mtime
`00:13`, sheet mtime `00:12` — verified newer.

## Snapshot

`beat_sheet.pre-rebuild.json` written before any edit. Preserved for audit.

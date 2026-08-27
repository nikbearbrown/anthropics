# four-places — the spark line is colliding with 20 of 26 beats

Different reel, different renderer, same disease. And this time it's **one
shared component**, which makes it a one-place fix.

## The bug, in one line

`runtime/remotion/src/scenes/ClaudeDescent.tsx`, the `SparkLine` component:

```jsx
position: 'absolute',
// SAFE.y = 54 — never place above the title-safe boundary
...(pos === 'top' ? { top: SAFE.y + 8 } : { bottom: SAFE.y + 4 }),
left: 0, right: 0,
...
fontSize: 54
```

The spark line is pinned to the frame's safe edge at full width. Every mode
renders its own content into the same `AbsoluteFill`, also anchored to that same
edge:

```jsx
top: SAFE.y + 8 + i * itemH     // list items — IDENTICAL y to the top spark line
top: SAFE.y + 16                // another mode — 8px below it
```

**Nothing reserves space for either.** The spark line lands on whatever the mode
drew at the top of the safe area. Every time.

`sparkAnchor` defaults to `'top'`, so this is the default path, not an edge case.

## Blast radius in this reel

21 of 26 beats use `ClaudeDescent`. By mode:

| mode | anchor | beats | what collides |
|---|---|---|---|
| `level` | top | **9** | — |
| `establish` | top | **3** | "Four places. Stacked." over "The Conversation" **and** over the partner/hiking/near-Denver chips |
| `level` | bottom | **3** | `bottom: SAFE.y + 4` sits exactly on the card's bottom border — "Generally. Their word." and "This one doesn't swing." |
| `pullback` | top | 2 | — |
| `compare` | top | **1** | "Swap the name." straddles the gutter, over "what you could type" |
| `detail` | top | 1 | — |
| (unset) | bottom | 1 | — |

Note the `bottom` anchor collides too. Both anchors fail for the same reason:
the overlay and the content are measured from the same frame edge.

**This is a shared component — every other reel using `ClaudeDescent` has it.**

## The fix: reserve a band

Don't nudge the offset. Give the spark line an exclusive strip, and make every
mode lay out inside what's left. Collision becomes impossible by construction —
the same principle as `next_to`/`arrange` in the Manim fix, applied to CSS.

This is now the third reel with one root cause: **something positions against the
frame edge while something else also positions against that same edge.**

---

## Prompt

```
Fix the spark-line collisions in
brutalist-art/runtime/remotion/src/scenes/ClaudeDescent.tsx.

THE BUG: the SparkLine component is position:absolute pinned to the frame's safe
edge —

    ...(pos === 'top' ? { top: SAFE.y + 8 } : { bottom: SAFE.y + 4 }),
    left: 0, right: 0,   fontSize: 54

— while every mode renders content into the same AbsoluteFill anchored to that
SAME edge (e.g. `top: SAFE.y + 8 + i * itemH` for list items, `top: SAFE.y + 16`
elsewhere). Nothing reserves space for either, so the spark line prints on top of
the mode's content. sparkAnchor defaults to 'top', so this is the default path.

Confirmed in anthropics/youtube/claude-basics/claude-liam-four-places-your-data-goes:
  establish + top   → "Four places. Stacked." over the box title AND the chips
  compare   + top   → "Swap the name." straddles the gutter, over a column header
  level     + bottom→ spark sits exactly on the card's bottom border
21 of 26 beats in that reel use this component. Other reels use it too.

THE FIX — reserve a band. Do NOT just change the offset.

1. Add a layout constant near SAFE:

     const SPARK_BAND = 96;   // fontSize 54 + leading + breathing room
                              // exclusive strip; NO mode content may enter it

2. SparkLine renders INSIDE that band — give the wrapper an explicit
   height: SPARK_BAND and center its contents vertically within it, so the strip
   is a real reserved region rather than a free-floating line.

3. Derive a content box ONCE, at the top of the component, and pass it to every
   mode:

     const bandTop    = sparkAnchor === 'top';
     const contentTop = SAFE.y + (bandTop ? SPARK_BAND : 0);
     const contentBot = SAFE.y + (bandTop ? 0 : SPARK_BAND);   // inset from bottom
     const contentH   = CANVAS.h - contentTop - contentBot;

4. Rewrite EVERY mode's vertical layout to start from contentTop and fit within
   contentH. Find every `SAFE.y + <n>` and every hardcoded `top:`/`panelY` in the
   mode branches — there are several — and replace them. A mode that still
   references SAFE.y directly for vertical placement is unconverted.

5. compare mode specifically: the spark line must never sit over the gutter
   between the two panels. With the band reserved this resolves automatically —
   verify it does, because that beat is the most visible failure.

6. If a mode's content genuinely does not fit in contentH, SCALE THE CONTENT,
   never shrink the type below the §8.1 floor and never let it re-enter the band.
   If it truly cannot fit, that beat carries two ideas — log it in the reel's
   BUILD-LOG.md rather than overlapping.

7. Add a dev-time guard so this cannot regress silently. In ClaudeDescent, after
   computing each mode's content geometry, assert in development that the
   content's top edge >= contentTop and its bottom edge <= CANVAS.h - contentBot,
   and throw with the mode name if violated. A collision should fail the render,
   not the eye.

DO NOT rely on GATE T to verify this. The bbox-overlap check merges fully
collided text into a single run and passes it — that is the documented Simon's
Ant failure, same class. Verification is frames only.

THEN:
  - re-render this reel via
      python3 brutalist-art/runtime/scripts/remotion_scenes.py \
        anthropics/youtube/claude-basics/claude-liam-four-places-your-data-goes
    (foreground, --concurrency=1)
  - extract and READ frames for at least one beat of EACH mode: establish,
    compare, level+top, level+bottom, pullback, detail. Paste them back.
  - then grep every other reel's beat_sheet.json for "ClaudeDescent", list the
    reels affected, and report the count. Do NOT re-render them in this pass —
    just report the blast radius so the rebuild can be scheduled.

ALSO VERIFY (separate from the spark line, may be a mid-transition artifact):
in establish mode the stacked boxes look oversized and nearly empty — a title
plus a small dashed circle in a very large box. Check a mid-beat frame. If the
boxes really are that empty at rest, that is a FILL-THE-CANVAS defect and needs
its own fix; if it is only a transition state, say so and leave it.

Do not publish.
```

---

## Worth promoting to the skill

Three reels, one root cause. Proposed addition to the design doctrine:

> **RESERVED-BAND LAW.** Every persistent overlay — spark line, caption, source
> credit, brand bug — owns an exclusive band, and content lays out inside the
> remaining box. Nothing may position against a frame edge that another element
> also positions against. This applies in both renderers: in Remotion it is a
> reserved strip and a derived content box; in Manim it is `next_to` / `arrange`
> against a referent, never a hardcoded coordinate. Validators cannot catch a
> total collision — fused text reads as one run — so the constraint has to live
> in the layout, not the gate.

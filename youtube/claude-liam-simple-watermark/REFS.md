# B00 — which images go in which slot

| Slot | File | Owns | Excluded |
|---|---|---|---|
| **@Image 1** | `books/ask-claude/claude/claude-008.png` | head sculpt, face, hair, handcrafted surface | pose, framing, background |
| **@Image 2** | `books/ask-claude/claude/claude-001.png` | full-body proportions, wardrobe | background, lighting, pose, expression |
| **@Image 3** | `books/ask-claude/lab/lab-010.png` | the SET — rack geometry, lamp placement, bench position | any person, photorealism, grade, lens, wardrobe |

No audio reference. **Seedance generates the voice — preset voice `MARCUS`, always.**
The voice name is plain text before the dialogue, never inside brackets (seedance
skill rule 6). MARCUS is the host's fixed voice across every `simple` episode; it is
what makes the host the same person from reel to reel.

## Why lab-010 and not another lab plate

`lab-010` is one of only two colour lab plates carrying **no spark glyph and no
wordmark**. Excluded for that reason: 006, 011, 013, 016, 017, 018, 022 (glyph),
006 and 018 (the words "Anthropic Claude" on the wall), 020 ("Claude" on the
console). Alternate if 010's framing is wrong: **`lab-003`** — colour, no glyph.
The black-and-white plates (001, 008, 014, 019, 021) will fight the LOOK's grade.

## Why the set arrives as a reference, not as prose

@Image 3 owns the room's *geometry*; the LOOK block owns its *material*. That split
is what stops the photoreal plate from dragging the puppet toward photorealism —
"photographic realism, grade, lens character" are excluded from @Image 3 explicitly,
so the plate contributes layout and the puppet plates contribute craft.

## Two Claude refs, not more

`claude-008` (head) + `claude-001` (full body) is the pair. The seedance skill's
rule 3: many views of one character read as *different subjects* and the identity
drifts. If the beat later needs a wider move, change @Image 2 to a different
full-body plate — never add a fourth character ref.

# Morning brief — the type problem, and what changed while you slept

*2026-08-21 · you said: "I don't ever want to see that again. Simplify what is shown ... the voice over can still discuss everything ... there is far too much meaningless detail."*

## What was actually wrong

Not a rendering glitch. Your scene library is authored in web type sizes.

- **91% of every `fontSize` in the library is below the floor** — 2,436 of 2,670 declarations across 345 components.
- The most common size in the whole corpus is **11px**, which renders at 22 physical pixels on a 2160-line master. The floor is 69.
- Measured on shipped reels: body lines of **15–21px** where 69 is required. On a phone that is ~4px — not "small", *absent*.

## Why GATE T said PASS

Four bugs, each sufficient on its own:

1. The floor was computed as 3.2% of an assumed 1080 "logical" height → **35px instead of 69px**.
2. The blob filter required `width ≥ height × 1.5`, so an **upright letter was discarded as "not a text run"** — precisely what small type looks like.
3. The noise floor was 15px, and **15px was the body text**.
4. When the filter discarded everything, it returned **PASS** — "no text-run blobs above noise threshold." Absence of measurement was treated as compliance.

Plus 124 exemption entries and a kerning threshold walked 1.6 → 2.5 → 3.5. The filmloop prompt forbids exactly this ("a validator weakened to get a green result is worse than a red result"); the prompt held, the checker didn't.

And the wordy-card check couldn't help: it reads beat-sheet props, but for these beats the props hold **only a `sparkLine`** — all the dense content is hardcoded in the `.tsx`. Every layer was looking where the problem wasn't.

## What I changed

**1. `brutalist-art/SHOW-LESS.md` — new owner doc, registered in BRAND-LOCKS.md**

> **Type size is FIXED. Content is the variable.** When content doesn't fit at the floor, you cut the content or split the beat. You never shrink the type.

Budget per card: one idea · **≤4 rows** · **≤8 words per row** · **≤2 columns** · no sub-labels. The banned third column of right-aligned notes goes to the voice. Test: *read the card aloud in under four seconds.*

**2. `runtime/scripts/type_check.py` — all four bugs fixed** (backup: `.pre-showless`)
Floor now measures **physical** frame height; upright glyphs count as text; noise floor 15→8px; **empty measurement is now FAIL, not PASS**. No new exemptions without a human signature.

**3. `_audit/TYPE-AUDIT.md`** — all 299 offending components ranked worst-first, with the size histogram.

**4. `HookifyEventTypes.tsx` rebuilt as the proof template** (backup: `.pre-showless`)
Was: 4 event rows × 3 columns + conditions-array block + 3 pitfall rows with bad/good pairs — 17 sizes, 16 sub-floor, smallest 8px.
Now: **four rows, two words each.** `bash → commands · file → edits · stop → completion · prompt → your input`. Minimum size **48**. Everything else — operators, regex examples, all three pitfalls — is narration.

## The factory

Stop it if it's still up:

```
pkill -f filmloop.sh; pkill -f "claude -p"; sleep 2; pgrep -fl filmloop.sh || echo stopped
```

It will also now halt itself: with the honest gate, reels fail GATE T, go unbuilt, and three consecutive failures trips the halt. That is correct behaviour — there is no point manufacturing against components that can't pass.

## The decision waiting for you

**299 components need this treatment.** That's the real number and there's no shortcut — each needs content cut to fit readable type, which is a judgment call per card, not a find-and-replace.

Look at the rebuilt `HookifyEventTypes` first. If four rows of two words is the right density, it becomes the template and the rest follow it. If it reads too sparse, then the beat needs splitting into two cards and we learn that before doing it 299 times.

I did **not** render it — verifying takes a Remotion render, and I'd rather you approve the density before I spend the night's compute proving the wrong thing.

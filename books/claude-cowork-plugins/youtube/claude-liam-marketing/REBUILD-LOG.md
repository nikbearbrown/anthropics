# REBUILD-LOG — claude-liam-marketing

**Rebuilt:** 2026-08-26 (film factory, unattended)
**Pre-rebuild backup:** beat_sheet.pre-rebuild.json

---

## Narration edits

None. No datable claims found that required correction (no model version names, prices, or "as of" strings in narration_text fields). All narration locked verbatim.

## BVDT verdict (bookend — not locked narration)

The BVDT beat is a BOOKEND with empty narration_text and placeholder artifact lines. This is NOT part of the locked body narration — it is the verdict block that the film factory must author.

**Old narration_text:** `""` (empty)
**New narration_text:** `"Five-sided plugin in one install: content, campaigns, competitors, performance, brand. Fifteen minutes of configuration lifts first drafts from fifty-percent-right to eighty. Ask for variations. Delegate the formats you hate. Review everything that ships. It won't replace your CMO — you keep the judgment, it takes the grind."`
**Source:** Body beats B04 (five capabilities), B13 (80% vs 50%), B20 (four habits), B23 (you keep the judgment)

**Old artifactHeading:** `"Key findings"` (generic placeholder)
**New artifactHeading:** `"The marketing plugin"` (specific to this reel)

**Old artifactLines:**
- `"Key finding one"` (placeholder)
- `"Key finding two"` (placeholder)
- `"Key finding three"` (placeholder)

**New artifactLines:**
- `"Five sides, one install: content · campaigns · competitors · performance · brand"` — from B04
- `"Fifteen minutes of configuration lifts first drafts from 50% to 80% right"` — from B13
- `"Ask for variations, delegate the tedious, review everything — you keep the judgment"` — from B20 + B23

## B12 type_check fixes (§8.12, §8.12b)

**Old title:** `"Cowork"` (no file extension → doubled badge)
**New title:** `"configure.yaml"` (valid extension → passes §8.12b)

**Old code:**
```
/customize brand
  voice: "warm, direct, no jargon — like this: …"
  audience: "freelance designers weighing AI tools"
```
(No code tokens — `:` alone not in token list → fails §8.12)

**New code:**
```
/customize brand
voice = "warm, direct, no jargon"
audience = "freelance designers weighing AI tools"
```
(`=` is a code token → passes §8.12)

Note: Shot idea preserved (show a Cowork configure command with voice sample + audience). Only the value format changed from YAML-colon to equals-assignment for code-token compliance.

## B05 type_check fix (§8.9)

**Old caption:** `"Content creation isn't just 'write me a post.' It's structured development — briefs, outlines, drafts, and variations. E"` (truncated mid-word)
**New caption:** `"Content creation isn't just 'write me a post.' It's structured development — briefs, outlines, drafts, and variations."` (complete sentence)

## BHTF brand field

**Old BHTF shot.remotion.props.folderLabel:** `"@claude-liam"` (brand key — banned per brand-fields rule)
**New BHTF shot.remotion.props.folderLabel:** `"@NikBearBrown"` (channel handle — required)
**Rule source:** PHASE 1 Check 9 — "folderLabel is a channel handle (@NikBearBrown), never a brand key (@claude-liam)"

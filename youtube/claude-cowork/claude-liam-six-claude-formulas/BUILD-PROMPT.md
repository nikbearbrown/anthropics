# BUILD PROMPT — six-claude-formulas

## Episode concept
A tutorial walking through Ruben Hassid's six Claude workflow formulas, presented as a five-column table rebuilt natively in Remotion. Formulas are revealed in pairs (two rows per beat) to match narration pacing. Two key formulas get dedicated spark cards as highlights. Pricing claims are flagged throughout.

## Beat-by-beat production notes

**B01 — ClaudeComposerAsk (0–9s)**
Cold open. "Goeie dag. This is Liam, in for Bear." Composer: "What are the actual workflow habits that make Claude work properly?" Answer: "Six formulas. They run 80% of the work."

**B02 — SPARK: Six formulas. 80% of the work. (9–17s)**
Name the source. Explain the table structure: Rule / You now / Copy this / The math / Where.

**B03 — REBUILD: Formula Table rows 1–2 (17–29s)**
Table header row draws first. Row 1: Delete your about-me file → Skill. Row 2: Skills + Projects, nothing else. Each row wipes in from left.

**B04 — REBUILD: Formula Table rows 3–4 (29–41s)**
Row 3: No settings is the best setting. Row 4: Make Claude ask YOU — the literal prompt in a quote-block style in the COPY THIS cell.

**B05 — REBUILD: Formula Table rows 5–6 (41–53s)**
Row 5: Fable on Low, Opus on High — pricing in mono style. Row 6: Edit, don't follow up. Footnote animates in below complete table: "Pricing: author's figures at time of writing — verify before publish."

**B06 — SPARK: Let Claude ask you. (53–61s)**
Highlight formula 4 with a dedicated spark card. The exact template prompt. AskUserQuestion emphasis.

**B07 — SPARK: Edit. Don't follow up. (61–70s)**
Highlight formula 6. Edit replaces, not stacks. "Message 30 costs 31× message 1 — author's claim."

**B08 — SPARK: Verify pricing before you build. (70–79s)**
Explicit caveat card on formula 5 pricing. "Author's figures at time of writing. Check current model pricing."

**B09 — HANDOFF (79–90s)**
Three user paths: Cowork daily → About Me → Skill. Chat user → AskUserQuestion. Hitting limits → Edit not follow-up.

**B10 — OUTRO (90–98s)**
"SIX FORMULAS RUN 80% OF MY WORK." "This is Liam, in for Bear."

## Remotion component hints
- `FormulaTable` — five-column table component. Column headers: THE RULE (terracotta text, bold) / YOU RIGHT NOW / COPY THIS / THE MATH / WHERE. Each row reveals with a wipe-right animation. Column widths approximately: 18% / 22% / 25% / 22% / 13%.
- `FormulaRow` — single table row; props: rule, you_now, copy_this, the_math, where. THE RULE cell uses terracotta color. COPY THIS cell can be styled as a quote-block (left border in terracotta, slightly lighter bg) when it contains a literal prompt.
- `TableHeader` — fixed first row with column labels in SF Mono; draws in as a unit before rows appear.
- `TableFootnote` — small italic note below the table; fades in after all rows complete. Used for pricing caveat.
- `SparkCard` — standard spark card for B06, B07, B08 highlight beats.

## Rebuild notes (image-sourced reel)
The original JPEG (`six-claude-workflow-formulas.jpeg`) must NOT appear as a shot. All elements to rebuild:
- **Table header row** — column labels in SF Mono caps, warm ink background
- **6 formula rows** — five columns each; THE RULE in terracotta; COPY THIS with quote-block option for literal prompts
- **Row 4 COPY THIS** — `"I want [task] to [goal]. Ask me questions with AskUserQuestion first."` should have quote-block styling
- **Row 5 THE MATH** — pricing in SF Mono; add subtle "(verify)" annotation
- **Pricing footnote** — `* Author's stated pricing at time of writing. Verify before publish.` — animates in below complete table
- **Column layout**: The rule (narrowest) | You right now | Copy this (widest — contains full prompts) | The math | Where (narrowest)

## Audio notes
NO AUDIO in this pass. Gate P = slate only.

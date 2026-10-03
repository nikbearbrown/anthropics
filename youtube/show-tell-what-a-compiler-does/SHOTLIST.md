# SHOTLIST — show-tell-what-a-compiler-does

**What this is.** The typed work order, one row per beat. Show-tell style: one drawn isometric image per beat, labels only, Liam's voice explains. No cards from the ShowTellCard family: every beat is a thing, a part or a flow, so every beat is a drawing (card test, question 1). Measured narration total: 196.89 s (BOUT includes its 1.0 s tail). No pantry slots, no open requests.

| beat | lane | scene | image | s |
|---|---|---|---|---|
| BIDEA | bookend | `BrutalistHesitantWriter` | Types "What does a compiler / do to my code in one go?", then corrects "do to my code in one go" to "do at each stage". "Salaam" greeting spoken over it. | 11.46 |
| BDEFS | bookend | `ClaudeDefinitions` | "Terms In This Film": compiler, token, IR, assembly. | 13.42 |
| B00 | manim | `B00_Pipeline` | A white source page ('C source') by a pale belt; four machines rise on it (three kraft, the back end dark with four lamps); the page rides into the first; the machines pulse in turn; a taped kraft box comes out at the far end ('ELF program'); a new page arrives. | 13.40 |
| B01 | manim | `B01_Preprocess` | The page grows ('preprocessor'); a header card slides in and merges at its top ('#include'); a tagged line widens into three ('macro'); a grey bracket closes on two lines, which drop out. | 10.07 |
| B02 | manim | `B02_Lex` | The page shrinks to the corner ('lexer'); one line becomes a long strip; a terracotta scan line cuts it into nine tiles ('tokens'); grey threads tie each tile back to its place on the page. | 9.41 |
| B03 | manim | `B03_Parse` | The tiles pulse in order ('parser'), then rise into a tree under a root node ('syntax tree'); grey edges draw; a terracotta dot descends from the root, rule by rule, to a leaf. | 10.92 |
| B04 | manim | `B04_Sema` | The tree moves left ('sema'); terracotta type dots land on every node; the 4 * 8 subtree folds into one white node; a grey-outlined card ('symbol table') takes the names n and x. | 10.60 |
| B05 | manim | `B05_Lower` | The tree collapses; a column of white IR strips drops in ('IR'); two open kraft boxes ('stack slots'); grey threads tie the strips that use each variable to its box. | 10.22 |
| B06 | manim | `B06_SSA` | The threads and slots sink away; dark register tabs snap onto the strips ('registers'); two strips go side by side as two paths and rejoin at a strip where a terracotta dot lands ('phi node'). | 10.60 |
| B07 | manim | `B07_Optimize` | A grey loop draws around the column ('optimizer') with three markers ('≤ 3 rounds'); marker 1 lights and two strips merge; marker 2 lights and a strip drops out; the column closes up; the phi dot becomes two grey copy bars. | 13.89 |
| B08 | manim | `B08_Codegen` | The IR shrinks to the left ('back end'); four dark doors rise; each lamp lights as its chip is named; the first turns terracotta ('x86-64'); the IR goes in; white assembly strips come out ('assembly'). | 12.01 |
| B09 | manim | `B09_Peephole` | The assembly column grows ('peephole'); a terracotta scan line runs down it; a grey bracket closes on two strips ('store, load'); the second slides out and the column closes up. | 9.47 |
| B10 | manim | `B10_Assemble` | The strips ride into a kraft press ('assembler'); rows of grey byte tiles come out; they pack into a kraft block on a dark plinth ('.o file'). | 8.94 |
| B11 | manim | `B11_Link` | The .o block ('linker'); two more blocks slide in ('runtime + libs'); grey cables join them; terracotta dots at the ends; all three merge into one kraft box on a plinth, taped shut ('ELF'). | 12.95 |
| B12 | manim | `B12_Warning` | The ELF box moves left; an empty check box draws in ('not validated'); the design doc's page slides in ('docs may be wrong'); the empty box pulses on "I do not recommend". | 11.48 |
| BHTF | bookend | `ClaudeComposerAsk` | The Claude.ai composer, "Your turn.": the add.c prompt types in full, then two check lines. | 24.02 |
| BOUT | bookend | `ClaudeTitleOutro` | Title restates with @NikBearBrown; Liam reads the title, then "At Nik Bear Brown". | 4.03 |

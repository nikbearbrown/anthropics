# BUILD PROMPT — five-claudes-explained

## Episode concept
A tutorial that maps all five Claude products — Chat, Code, Projects, Skills, Cowork — using the four-row card structure from Ruben Hassid's infographic. Each product gets its own animated card. The reel ends with a summary strip showing all five products and their cost tiers. Never shows the original infographic JPEG.

## Beat-by-beat production notes

**B01 — ClaudeComposerAsk (0–9s)**
Cold open. "Tere. This is Liam, in for Bear." Composer question: five product names listed, asking if they're the same. Answer: "Five separate products, one name."

**B02 — SPARK: Five products. One name. (9–16s)**
Set up the map: Chat · Code · Projects · Skills · Cowork. Different jobs, different costs.

**B03 — REBUILD: Chat product card (16–27s)**
ProductCard component: four rows draw in sequence. Plain English: back-and-forth chatbot. Setup: free Gmail account. Mistake: using it for everything, no context between sessions. Non-technical: fresh conversation each time.

**B04 — REBUILD: Code product card (27–38s)**
ProductCard: Code. Plain English: describe → Claude builds, writes code, runs it. Setup: Code tab, $10/month (verify pricing). Mistake: not scoping the task — Claude explores instead of builds. Non-technical: building contractor for digital things.

**B05 — REBUILD: Projects product card (38–48s)**
ProductCard: Projects. Plain English: saved workspace with persistent context. Setup: sidebar → Projects. Mistake: treating it like a folder — it's a trained assistant. Non-technical: new employee who read the handbook.

**B06 — REBUILD: Skills product card (48–58s)**
ProductCard: Skills. Plain English: /slash command instruction manual, one thing. Setup: plain text, share with team. Mistake: one skill trying to do too many things. Non-technical: recipe card, never pollutes other chats.

**B07 — REBUILD: Cowork product card (58–68s)**
ProductCard: Cowork. Plain English: files + web + computer + research. Setup: left sidebar → Projects. Mistake: dumping all files in before starting. Non-technical: chief of staff who can use your computer. Mark as premium/heaviest product.

**B08 — REBUILD: Five-product summary strip (68–77s)**
FiveProductStrip: all five tiles in a row, one-line use case each, cost tier dots. Animates left-to-right. The "pay Cowork prices for Chat work" line lands here.

**B09 — HANDOFF (77–88s)**
"Open one product you've never used." Specific: if Chat-only, open Projects. Add one file. See what changes.

**B10 — OUTRO (88–96s)**
"FIVE PRODUCTS. ONE NAME." "This is Liam, in for Bear."

## Remotion component hints
- `ProductCard` — reusable card, parameterized by product name and four data rows. Each row: terracotta SF Mono label + serif/sans body text. Rows draw in one by one with 0.25s stagger.
  - Row labels: "IN PLAIN ENGLISH" / "HOW TO SET UP" / "BIGGEST MISTAKE" / "NON-TECHNICAL"
  - Header bar: product name in EB Garamond bold (large), warm ink background bar
  - Subtle left accent strip in terracotta
- `FiveProductStrip` — horizontal row of five `ProductTile` mini-cards. Each tile: product name (serif), use case line (sans small), cost tier dots (1–3 filled circles, terracotta for heavier).
- `ProductTile` — small card for the summary strip.
- Card-to-card transitions: previous card slides out left, new card slides in from right (match-cut rhythm, each card gets its own beat).

## Rebuild notes (image-sourced reel)
The original JPEG (`claude-chat-code-projects-skills-cowork-explained.jpeg`) must NOT appear as a shot. All elements to rebuild:
- **5 product headers** — large serif name in a warm ink header bar
- **4 rows per card** — labeled rows in SF Mono + body text in system sans
- **Flowchart connectors** — optional subtle arrows between cards if presenting as a flow (Chat→Skills→Projects→Code→Cowork progression); or simple sequential reveal
- **Summary strip** — built as `FiveProductStrip` at the end
- **Cost tier indicators** — simple dot system (1=light, 2=medium, 3=heavy/terracotta)

## Audio notes
NO AUDIO in this pass. Gate P = slate only.

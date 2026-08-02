# CAJAL figure candidates — computational-finance-with-ai (previz track)

Mechanism figures mined from chapter content. Blank unannotated vector — no baked text;
previz owns every label (stage names, asset labels …). Okabe-Ito, white bg, 1pt strokes,
no red-green, no 3D perspective, ≤6–8 components.

> De-confliction: this book owns financial mechanics figures (arbitrage loops, balance-sheet diagrams, option replication). NOT bar charts, scatter plots, or standard data charts — only structural mechanism diagrams qualify.

---

## 1. ap-arbitrage-loop  — two-path Authorized Participant arbitrage closure  (MC · cycle mechanism · Critical)
*Source: chapter 04 — "Funds and ETFs"*

**PASTE:** Draw a blank two-panel arbitrage loop on a white background. Left panel (ETF above NAV): three rectangles arranged in a triangle — top rectangle (AP Authorized Participant), bottom-left rectangle (Market — buy basket), bottom-right rectangle (ETF — create shares). Arrows form a clockwise loop. Right panel (ETF below NAV): same three-rectangle triangle — AP, Market (sell basket), ETF (redeem shares). Arrows form a counter-clockwise loop. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] left panel: AP buys basket from market → delivers to ETF → receives ETF shares → sells into market (premium shrinks); right panel: AP buys ETF shares → redeems for basket → sells basket into market (discount shrinks); the direction reversal between panels is the teaching point.
- [O] two panels; left = clockwise loop, right = counterclockwise loop; three nodes in triangle per panel.
- [P] flat vector, Okabe-Ito: AP rectangles Blue #0072B2, Market rectangles Bluish Green #009E73, ETF rectangles Orange #E69F00, above-NAV arrows Black #000000, below-NAV arrows Vermillion #D55E00. No baked text.
- [E] exclude: premium/discount values, share-count numbers, AP firm names, a third scenario.

**NEGATIVE:** premium values, share counts, firm names, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 2. short-sale-four-party-flow  — share flow and cash collateral across four parties  (MC · systems diagram · Critical)
*Source: chapter 06 — "Margin and Short Selling"*

**PASTE:** Draw a blank four-party flow diagram on a white background: four rectangles arranged in a diamond (top, bottom, left, right). Arrows show share flow (one direction) and cash collateral flow (opposite direction) between adjacent nodes. A separate small arrow labeled "borrow fee" (represented as a small double-headed bracket) sits between the top and left nodes. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] four parties: Lender (top), Broker (left), Short Seller (right), Buyer (bottom); shares flow from Lender → Broker → Short Seller → Buyer; cash collateral flows from Short Seller → Broker → Lender; borrow fee flows between Lender and Broker; the crossing cash and share flows are the teaching point.
- [O] diamond arrangement; share flow clockwise; cash flow counterclockwise; borrow-fee bracket between adjacent nodes.
- [P] flat vector, Okabe-Ito: party rectangles Blue #0072B2, share-flow arrows Bluish Green #009E73, cash-flow arrows Vermillion #D55E00, borrow-fee bracket Orange #E69F00. No baked text.
- [E] exclude: party-name text, dollar-amount labels, percentage fee values, a fifth party.

**NEGATIVE:** party names, dollar amounts, fee percentages, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 3. binomial-option-replication  — one-step binomial tree with replicating portfolio  (VG · mechanism · Critical)
*Source: chapter 07 — "Options and Derivatives"*

**PASTE:** Draw a blank one-step binomial tree on a white background: one circle on the left (today's node). Two arrows branch from it — one upward-right to a circle (up-state) and one downward-right to a circle (down-state). Beside the tree, a small two-row table shows two rectangles stacked (the replicating portfolio components — shares and borrowing). No text, no values.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] left node: today; up-state circle: higher price; down-state circle: lower price; replicating portfolio: delta shares (top row) minus borrowing (bottom row) produces identical payoffs in both states; the equivalence between option and portfolio is the teaching point.
- [O] left-to-right branching; two outcome states; portfolio table sits to the right of the tree.
- [P] flat vector, Okabe-Ito: today circle Blue #0072B2, up-state circle Bluish Green #009E73, down-state circle Orange #E69F00, up-branch arrow Black #000000, down-branch arrow Black #000000, portfolio rectangles Sky Blue #56B4E9. No baked text.
- [E] exclude: price values, delta fraction, borrowing amounts, a two-period tree extension.

**NEGATIVE:** price numbers, delta values, borrowing amounts, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 4. stock-decomposition-idiosyncratic-cancel  — single stock vs portfolio risk decomposition  (VG · comparison · Important)
*Source: chapter 11 — "Asset Pricing Models"*

**PASTE:** Draw a blank two-panel decomposition diagram on a white background. Left panel: one large circle (total stock) divided by a vertical line into two sub-circles of unequal size — a larger left half (market component) and a smaller right half (idiosyncratic component). Right panel: a large circle (500-stock portfolio) with only one sub-circle filling it entirely (market component only — idiosyncratic has vanished). An X appears in the expected position of the idiosyncratic region in the right panel. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] left: single stock = market risk + idiosyncratic risk (two sub-circles); right: 500-stock portfolio = market risk only (idiosyncratic vectors cancel — X marks the eliminated component); diversification is the teaching point.
- [O] two panels; left shows both components; right shows idiosyncratic component eliminated with X.
- [P] flat vector, Okabe-Ito: market component Blue #0072B2, idiosyncratic component Vermillion #D55E00, X marker Black #000000, portfolio circle Bluish Green #009E73. No baked text.
- [E] exclude: stock-name text, return values, beta coefficient labels, a third panel.

**NEGATIVE:** stock names, return values, beta values, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 5. five-layer-dependency-stack  — five financial analysis layers with upward error propagation  (MC · hierarchy · Important)
*Source: chapter 13 — "Putting It All Together: The Investment Decision Capstone"*

**PASTE:** Draw a blank five-tier stacked architecture on a white background: five rectangles stacked vertically, each separated by a thin gap. Bottom rectangle is the foundation; top rectangle is the apex. Small upward arrows run along the right edge from each layer to the next (error propagation direction). No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] five layers from bottom (foundation) to top: Return Measurement → Risk Assessment → Valuation → Portfolio Construction → Capital Allocation; errors at any layer propagate upward through all layers above.
- [O] bottom-to-top stack; five equal-width rectangles; ascending error-propagation arrows on right edge.
- [P] flat vector, Okabe-Ito: bottom layer Blue #0072B2, second layer Sky Blue #56B4E9, third layer Bluish Green #009E73, fourth layer Orange #E69F00, top layer Vermillion #D55E00, arrows Black #000000. No baked text.
- [E] exclude: layer-name text, error-percentage values, a sixth layer, a downward arrow.

**NEGATIVE:** layer names, error values, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 6. compounding-discounting-timeline  — two-arrow timeline showing time-value symmetry  (VG · mechanism · Important)
*Source: chapter 05 — "Time Value of Money and Discounted Cash Flows"*

**PASTE:** Draw a blank two-arrow timeline on a white background: a horizontal line with a dot on the left (today) and a dot on the right (future). Above the line, a right-pointing arrow (compounding — today to future). Below the line, a left-pointing arrow (discounting — future to today). Both arrows span the same horizontal distance and are labeled by position only (above vs. below). No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] horizontal time axis; today dot (left); future dot (right); compounding arrow above (today→future); discounting arrow below (future→today); the same factor operating in two directions is the teaching point.
- [O] left-to-right timeline; compounding above, discounting below; arrows same length.
- [P] flat vector, Okabe-Ito: timeline Black #000000, today/future dots Black #000000, compounding arrow Blue #0072B2, discounting arrow Vermillion #D55E00. No baked text.
- [E] exclude: dollar amounts, interest-rate percentages, year labels, a third time point.

**NEGATIVE:** dollar values, interest rates, year labels, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows (the two arrows are independent, not dual-headed), hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video candidates

FIGURE ap-arbitrage-loop — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE short-sale-four-party-flow — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE binomial-option-replication — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE stock-decomposition-idiosyncratic-cancel — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE five-layer-dependency-stack — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE compounding-discounting-timeline — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.

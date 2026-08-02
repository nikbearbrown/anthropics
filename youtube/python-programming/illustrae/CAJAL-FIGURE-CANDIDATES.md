# CAJAL figure candidates — python-programming (previz track)

Mechanism figures mined from chapter content. Blank unannotated vector — no baked text;
previz owns every label (scope names, structure names …). Okabe-Ito, white bg, 1pt strokes,
no red-green, no 3D perspective, ≤6–8 components.

> De-confliction: this book owns Python-specific CS pedagogy figures (aliasing, scope, recursion, call stack). Primarily conceptual CS mechanism figures — no hardware, no agent architecture.

---

## 1. aliasing-trap-two-stage  — two labels pointing to the same mutable object  (VG · mechanism · Critical)
*Source: chapter 03 — "Objects"*

**PASTE:** Draw a blank two-stage aliasing diagram on a white background. Stage 1 (top half): two arrows on the left side, both pointing to the same box on the right (one object, two labels). Stage 2 (bottom half): same layout — two arrows pointing to the same box — but the box has a different interior mark (indicating mutation has occurred and both labels see the change). A horizontal dashed line separates the two stages. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] two variable arrows (left) both pointing to one object box (right); mutation in stage 2 changes the shared object; both arrows still point to the same now-mutated box; the single-object, double-reference is the teaching point.
- [O] top/bottom split at dashed line; both stages show the same two-arrows-to-one-box topology; bottom box has a filled dot inside indicating mutation.
- [P] flat vector, Okabe-Ito: variable arrows Blue #0072B2, original object box Bluish Green #009E73, mutated object box Vermillion #D55E00, dashed separator line Orange #E69F00. No baked text.
- [E] exclude: variable-name text, list-content values, a third arrow, a copy of the object.

**NEGATIVE:** variable names, list values, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 2. global-local-scope-nesting  — two nested scope boxes with read vs write access  (VG · structural · Critical)
*Source: chapter 07 — "Modules"*

**PASTE:** Draw a blank nested-scope diagram on a white background: a large outer rectangle (global scope) containing two smaller inner rectangles side by side (two function local scopes). A thin dashed arrow from each inner rectangle points to a small variable symbol in the outer rectangle (read access). One inner rectangle also has a solid arrow pointing outward with a small lock symbol (explicit global write access). No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] outer rectangle: global scope with one variable; two inner rectangles: function-local scopes; dashed arrows = read access (automatic); solid arrow with lock = write access (requires explicit declaration); the asymmetry between read and write is the teaching point.
- [O] outer contains two inner; dashed read arrows; solid write arrow on one side; lock symbol on write.
- [P] flat vector, Okabe-Ito: global scope rectangle Blue #0072B2, local scope rectangles Sky Blue #56B4E9, read arrows Bluish Green #009E73 dashed, write arrow Vermillion #D55E00 solid, lock symbol Orange #E69F00. No baked text.
- [E] exclude: variable-name text, Python `global` keyword, a third scope, shadow variable diagram.

**NEGATIVE:** variable names, Python keywords, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 3. recursive-call-stack-unwind  — descending frames then ascending return values  (VG · mechanism · Critical)
*Source: chapter 12 — "Recursion"*

**PASTE:** Draw a blank two-column recursion diagram on a white background. Left column: four rectangles stacked top to bottom (call descent — growing stack), each slightly indented to the right to show nesting depth. Bottom rectangle has a checkmark (base case). Right column: the same four rectangles, now in reverse order from bottom to top (unwinding), with a small upward arrow between each adjacent pair and a numeric dot inside each frame (return value accumulating). No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] left column: recursive descent (frames 1→4, growing); right column: return-value propagation (frames 4→1, unwinding); base case checkmark is at the bottom of the left column; the descent-then-ascent symmetry is the teaching point.
- [O] two columns side by side; left descends, right ascends; base case marked at bottom.
- [P] flat vector, Okabe-Ito: descent frames Blue #0072B2, unwind frames Bluish Green #009E73, base-case checkmark Orange #E69F00, ascending arrows Black #000000, return-value dots Vermillion #D55E00. No baked text.
- [E] exclude: function-name text, return-value numbers, argument values, a fifth frame.

**NEGATIVE:** function names, return values, argument values, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 4. function-call-data-flow  — argument in, return value out  (VG · mechanism · Important)
*Source: chapter 06 — "Functions"*

**PASTE:** Draw a blank function-call data-flow diagram on a white background: on the left, a small circle (call site with argument value). An arrow leads right into a tall rectangle (function body). Inside the rectangle, a horizontal line represents the processing body. Out of the rectangle on the right, another arrow leads to a small circle (return value at call site). The arrows enter and exit at different heights — input arrow enters from the left, output arrow exits from the right. No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape.
- [C] call site (left circle, argument); function body rectangle (center, processing); return value (right circle, result); input and output are two distinct flows; the bidirectional data travel through the function boundary is the teaching point.
- [O] left-to-right; input enters left edge of rectangle, output exits right edge; two circles flanking the rectangle.
- [P] flat vector, Okabe-Ito: input circle Blue #0072B2, function rectangle Bluish Green #009E73, output circle Orange #E69F00, input arrow Black #000000, output arrow Vermillion #D55E00. No baked text.
- [E] exclude: argument values, function-name text, type annotations, a nested function call.

**NEGATIVE:** argument values, function names, type text, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 5. while-loop-cycle  — three-phase check-execute-return cycle  (MC · cycle diagram · Important)
*Source: chapter 05 — "Loops"*

**PASTE:** Draw a blank three-node loop cycle on a white background: three circles arranged in a triangle. Clockwise arrows connect them: top circle → right circle → left circle → top circle. From the top circle, a separate arrow also exits toward the right without looping (the exit path when condition is false). No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] three loop phases: Check Condition (top) → Execute Body (right) → Return to Check (left) → back to top; exit arrow from Check Condition goes directly right (false branch — loop exits); the cycle plus exit is the teaching point.
- [O] clockwise triangle cycle; exit arrow branches off the Check node.
- [P] flat vector, Okabe-Ito: Check Condition circle Blue #0072B2, Execute Body circle Bluish Green #009E73, Return circle Orange #E69F00, cycle arrows Black #000000, exit arrow Vermillion #D55E00. No baked text.
- [E] exclude: condition-text, loop-body content, iteration-count numbers, a fourth node.

**NEGATIVE:** condition text, body code, iteration counts, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## 6. inheritance-tree-inherited-vs-added  — two-level class hierarchy showing attribute inheritance  (VG · hierarchy · Important)
*Source: chapter 13 — "Inheritance"*

**PASTE:** Draw a blank two-level class hierarchy diagram on a white background: one parent rectangle at the top with three small filled squares inside (representing three inherited attributes). Two child rectangles below connected to the parent by lines. Each child rectangle shows the same three small filled squares (inherited) plus one additional outlined square (new attribute added). No text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] parent class (top, 3 filled attributes); two child classes (bottom, 3 filled = inherited + 1 outlined = new); filled vs. outlined squares encode the inherited/added distinction.
- [O] top parent → two children; children have more attribute slots than parent; inherited = filled, new = outlined.
- [P] flat vector, Okabe-Ito: parent rectangle Blue #0072B2, child rectangles Sky Blue #56B4E9, inherited attribute squares Bluish Green #009E73 filled, new attribute squares Orange #E69F00 outlined, hierarchy lines Black #000000. No baked text.
- [E] exclude: class-name text, attribute-name text, method list, a third child, a grandchild.

**NEGATIVE:** class names, attribute names, method signatures, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video candidates

FIGURE aliasing-trap-two-stage — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE global-local-scope-nesting — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a spatial cross-section or structural schematic whose value lies in inspecting all parts simultaneously.
FIGURE recursive-call-stack-unwind — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE function-call-data-flow — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE while-loop-cycle — Status: VIDEO CANDIDATE · Criterion: 3 · Reason: a recurring process where the closed nature of the cycle and the change accumulated on each pass are part of the concept, not merely a round arrangement of steps.
FIGURE inheritance-tree-inherited-vs-added — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** **while-loop-cycle** — the sole video candidate; a recurring process where the closed nature of the cycle and the change accumulated on each pass are part of the concept, not merely a round arrangement of steps.

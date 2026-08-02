# CAJAL figure candidates — info-5100-application-engineering-and-development (previz track)

OOP architecture and design-pattern diagrams from a Java programming course. Moderate CAJAL
density: chapters 03, 05, 08 yield inheritance/class hierarchy and state-flow figures.
Programming-exercise chapters, midterm, and appendix chapters have zero candidates.

Zero-candidate chapters: 00-frontmatter, 00-introduction, 00-welcome,
01-fundamentals-of-programming-in-java, 02-methods-arrays-and-file-objects,
04-basics-of-object-oriented-programming-part-2, 06-basics-of-gui-programming-in-java,
07-midterm-exam, 09-event-driven-programming,
10-event-driven-programming-with-scene-builder, 11-generics, 12-recursion,
13-collections-and-iterators, 14-lists-stacks-queues-and-the-final-project,
95-claude-code, 97-fundamental-themes, 99-back-matter.

---

## 1. screen-centric-vs-state-centric  — two mental models for user flows: screen sequence vs. state path  (VG · comparison panels · Critical)
*Source: Chapter 3 — "Objects and Classes"*

**PASTE:** Draw a blank two-panel comparison on a white background. Left panel: a sequence of five rectangles connected by arrows (screen-to-screen navigation) — the rectangles contain only box icons with no objects inside them. Right panel: the same five rectangles connected by arrows, but now each rectangle has a small sphere or circle inside it (an object traveling through the sequence) that persists across all screens — the same sphere icon appears in every rectangle. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape two-panel.
- [C] left: screen-centric model (arrows between empty screens, state lost between screens); right: state-centric model (same object persists through all screens).
- [O] two panels; five-screen sequence in each; left = empty screens, right = persistent object circles in each screen.
- [P] flat vector, Okabe-Ito: screen rectangles Blue #0072B2 outline, object circles Bluish Green #009E73 filled, arrows Black #000000, absent-state X on left panel Vermillion #D55E00. No baked text.
- [E] exclude: CardLayout implementation, Java Swing API, specific variable names, code snippets.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. resource-event-relationship-triad  — three distinct OOP object types: resource / event / relationship  (VG · comparison panels · Important)
*Source: Chapter 5 — "Inheritance and Polymorphism"*

**PASTE:** Draw a blank three-panel horizontal comparison on a white background: three distinct symbolic diagrams. Left panel: a large standalone circle (durable resource — exists before and after events). Middle panel: a small circle with two arrows entering from outside (event — depends on resources, records a state change). Right panel: two circles connected by a line (relationship — structural fact connecting two resources). Each diagram is contained within a lightly bordered square panel. No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, landscape three-panel.
- [C] three object types: resource (standalone durable circle), event (dependent, arrows from resources), relationship (connecting two resource circles); visually distinct geometry per type.
- [O] three equal panels; left = resource, middle = event, right = relationship; each panel has simple geometric diagram only.
- [P] flat vector, Okabe-Ito: resource circles Blue #0072B2, event node Vermillion #D55E00, relationship line Bluish Green #009E73, event arrows Black #000000. No baked text.
- [E] exclude: superclass/subclass hierarchy, polymorphism notation, specific library domain.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 3. inheritance-hierarchy  — superclass / subclass tree structure showing inheritance and polymorphism  (VG · hierarchy · Important)
*Source: Chapter 5 — "Inheritance and Polymorphism" / Chapter 8 — "Abstract Classes and Interfaces"*

**PASTE:** Draw a blank class-hierarchy tree on a white background: a root rectangle at the top (superclass) with a solid line descending to two child rectangles (subclasses); each subclass rectangle has a solid line descending to one grandchild rectangle (more-specific subclass); total of five rectangles arranged in a tree with the root at top; each rectangle has only a small abstract icon to distinguish it (circle, square, diamond icons from top to bottom of the tree). No labels — no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] one superclass, two subclasses, two grandchild subclasses; inheritance shown as tree with solid connecting lines; icon inside each rectangle differs by specificity level.
- [O] top-down tree; root at top; two branches; each branch extends one more level.
- [P] flat vector, Okabe-Ito: superclass Blue #0072B2, subclasses Sky Blue #56B4E9, grandchild subclasses Orange #E69F00, inheritance lines Black #000000. No baked text.
- [E] exclude: interface versus abstract class distinction, specific Java syntax, override notation.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## Video candidates

FIGURE screen-centric-vs-state-centric — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE resource-event-relationship-triad — Status: STATIC SUFFICIENT · Criterion: — · Reason: the figure is a simultaneous comparison of two or more states; motion would replace side-by-side display with a sequence that the chapter does not assert.
FIGURE inheritance-hierarchy — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.

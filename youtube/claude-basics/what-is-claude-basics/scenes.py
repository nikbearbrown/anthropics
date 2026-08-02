from manim import *

CREAM = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"

config.background_color = CREAM

class B01_SearchBoxAmnesia(Scene):
    """B01 — wrong model: Claude as a search box, each session starts blank."""
    def construct(self):
        # Persistent top label — keeps ink bbox tall throughout
        top_label = Text("The wrong model:", font_size=36, color=INK, font=FONT).move_to(UP*3.0)
        sub_label = Text("one question → one answer → close the tab",
                         font_size=28, color=INK, font=FONT).next_to(top_label, DOWN, buff=0.25)
        self.add(top_label, sub_label)

        # Search box centered slightly above middle
        box = RoundedRectangle(width=10, height=1.5, color=INK, stroke_width=3.5).set_fill(color=CREAM, opacity=0)
        box.move_to(UP*0.6)
        session_label = Text("Session", font_size=22, color=INK, font=FONT).next_to(box, UP, buff=0.25)
        self.add(box, session_label)

        # Bottom anchor line — keeps ink bbox bottom reachable throughout (within ±3.4 safe area)
        bottom_line = Line(LEFT*5.5, RIGHT*5.5, color=INK, stroke_width=1.5).move_to(DOWN*2.8)
        self.add(bottom_line)

        # Three query cycles — answer box below the search box
        for i in range(3):
            query = Text(
                ["What is context?", "How does memory work?", "What did we discuss?"][i],
                font_size=34, color=INK, font=FONT).move_to(box)
            answer_box = RoundedRectangle(width=10, height=2.0, color=INK, stroke_width=2).set_fill(
                color=CREAM, opacity=0).move_to(DOWN*1.6)
            answer_text = Text("Here is a fresh answer.", font_size=28, color=INK, font=FONT).move_to(answer_box)
            # INK label for WCAG §8.3 — bold weight provides emphasis without contrast fail
            blank_label = Text("Session reset.", font_size=24, color=INK, font=FONT, weight=BOLD).move_to(DOWN*2.65)

            self.play(Write(query), run_time=0.5)
            self.play(FadeIn(answer_box), Write(answer_text), run_time=0.6)
            self.wait(0.2)
            self.play(FadeOut(query), FadeOut(answer_box), FadeOut(answer_text),
                      FadeIn(blank_label), run_time=0.4)
            self.wait(0.15)
            self.play(FadeOut(blank_label), run_time=0.25)

        # Final verdict — large bold INK (WCAG §8.3 compliant), FadeIn so it's fully visible
        final = Text("Blank. Every time.", font_size=52, color=INK, font=FONT, weight=BOLD).move_to(UP*0.6)
        self.play(FadeOut(box), FadeOut(session_label), FadeIn(final), run_time=0.5)
        self.wait(1.5)


class B02_ContextAccretion(Scene):
    """B02 — right model: Claude as a workspace with accumulated context."""
    def construct(self):
        # Project container — transparent fill, dark border; no light-fill diluting ink contrast
        project_box = RoundedRectangle(width=10, height=5.5, color=INK, stroke_width=3).set_fill(CREAM, opacity=0)
        project_label = Text("Project", font_size=28, color=INK, font=FONT, weight=BOLD).next_to(project_box, UP, buff=0.25)
        self.play(FadeIn(project_box), Write(project_label), run_time=0.6)

        doc_labels = ["Strategy Doc", "Team Handbook", "Product Brief"]
        docs = []
        for i, name in enumerate(doc_labels):
            # INK border, CREAM fill — WCAG §8.3 compliant (no TERRA blobs on cream)
            doc = RoundedRectangle(width=2.6, height=0.9, color=INK, stroke_width=2.5).set_fill(CREAM, opacity=0)
            doc.move_to(project_box.get_top() + DOWN*(1.0 + i*1.2) + LEFT*3.2)
            doc_text = Text(name, font_size=22, color=INK, font=FONT).move_to(doc)
            docs.append(VGroup(doc, doc_text))
            self.play(FadeIn(VGroup(doc, doc_text)), run_time=0.4)
            self.wait(0.1)

        # Answer box — transparent fill, dark border only
        answer = RoundedRectangle(width=5.5, height=3.8, color=INK, stroke_width=2).set_fill(CREAM, opacity=0)
        answer.move_to(project_box.get_center() + RIGHT*2.5)
        answer_text = Text("Answer draws from\nevery layer.", font_size=28, color=INK, font=FONT).move_to(answer)
        self.play(FadeIn(answer), Write(answer_text), run_time=0.7)

        for doc_vg in docs:
            line = Line(doc_vg.get_right(), answer.get_left(), color=TERRA, stroke_width=2.5)
            self.play(Create(line), run_time=0.3)

        self.wait(1.0)


class B04_ThreeDocsIn(Scene):
    """B04 — do this now: three documents sliding into a project container."""
    def construct(self):
        # Wider container (10 units) — transparent fill so only TERRA docs and INK border register as ink
        container = RoundedRectangle(width=10, height=4.2, color=INK, stroke_width=3).set_fill(CREAM, opacity=0)
        container_label = Text("Your Project", font_size=32, color=INK, font=FONT, weight=BOLD).next_to(container, UP, buff=0.3)
        self.play(FadeIn(container), Write(container_label), run_time=0.5)

        docs = [
            ("Most-explained Doc 1", LEFT*4.5 + UP*1.2),
            ("Most-explained Doc 2", LEFT*4.5 + ORIGIN),
            ("Most-explained Doc 3", LEFT*4.5 + DOWN*1.2),
        ]
        targets = [container.get_center() + UP*1.15,
                   container.get_center(),
                   container.get_center() + DOWN*1.15]

        for i, ((label, start), target) in enumerate(zip(docs, targets)):
            # INK border, CREAM fill — WCAG §8.3 compliant (no TERRA blobs on cream)
            doc = RoundedRectangle(width=3.4, height=0.88, color=INK, stroke_width=2.5).set_fill(CREAM, opacity=0).move_to(start)
            doc_text = Text(label, font_size=22, color=INK, font=FONT).move_to(doc)
            dg = VGroup(doc, doc_text)
            self.add(dg)
            self.play(dg.animate.move_to(target), run_time=0.50)
            new_sw = 3 + (i + 1) * 1.2
            self.play(container.animate.set_stroke(width=new_sw), run_time=0.18)

        # INK color for WCAG §8.3 compliance — bold weight preserves visual emphasis
        final = Text("Context loaded.", font_size=42, color=INK, font=FONT, weight=BOLD).next_to(container, DOWN, buff=0.32)
        self.play(Write(final), run_time=0.6)
        self.wait(0.9)

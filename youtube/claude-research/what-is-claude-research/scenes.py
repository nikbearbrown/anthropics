from manim import *

CREAM = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"

config.background_color = CREAM

class B01_PasteTheAnswer(Scene):
    """B01 — wrong model: model output flows straight to document."""
    def construct(self):
        model_box = RoundedRectangle(width=4, height=2, color=INK, stroke_width=2).set_fill("#EAE7DC", opacity=1).shift(LEFT*3.5)
        model_label = Text("Model", font_size=26, color=INK, font=FONT).next_to(model_box, UP, buff=0.2)
        citation = Text('"Smith et al., 2021:\nfound 73% improvement."', font_size=24, color=INK, font=FONT).move_to(model_box)
        self.play(FadeIn(model_box), Write(model_label), Write(citation), run_time=0.5)

        doc_box = RoundedRectangle(width=4, height=2, color=INK, stroke_width=2).set_fill(CREAM, opacity=1).shift(RIGHT*3.5)
        doc_label = Text("Your doc", font_size=26, color=INK, font=FONT).next_to(doc_box, UP, buff=0.2)
        self.play(FadeIn(doc_box), Write(doc_label), run_time=0.3)

        direct_arrow = Arrow(model_box.get_right(), doc_box.get_left(), color=INK, stroke_width=3)
        self.play(Create(direct_arrow), run_time=0.4)

        no_stop = Text("No detour. No stop.", font_size=32, color=INK, weight=BOLD, font=FONT).shift(DOWN*2.4)
        self.play(Write(no_stop), run_time=0.5)
        self.wait(0.9)


class B02_SourceDetour(Scene):
    """B02 — right model: citation routed through primary source check."""
    def construct(self):
        model_box = RoundedRectangle(width=3.5, height=1.8, color=INK, stroke_width=2).set_fill("#EAE7DC", opacity=1).shift(LEFT*4)
        model_label = Text("Model", font_size=24, color=INK, font=FONT).next_to(model_box, UP, buff=0.18)
        citation = Text('"Smith 2021: 73%"', font_size=24, color=INK, font=FONT).move_to(model_box)
        self.play(FadeIn(model_box), Write(model_label), Write(citation), run_time=0.4)

        source_node = Circle(radius=0.9, color=INK, stroke_width=2.5).set_fill(CREAM, opacity=0)
        source_label = Text("Primary\nsource", font_size=24, color=INK, font=FONT).move_to(source_node)
        source_node.shift(UP*1.5)
        source_label.shift(UP*1.5)
        self.play(FadeIn(source_node), Write(source_label), run_time=0.35)

        doc_box = RoundedRectangle(width=3.5, height=1.8, color=INK, stroke_width=2).set_fill(CREAM, opacity=1).shift(RIGHT*4)
        doc_label = Text("Your doc", font_size=24, color=INK, font=FONT).next_to(doc_box, UP, buff=0.18)
        self.play(FadeIn(doc_box), Write(doc_label), run_time=0.3)

        a1 = Arrow(model_box.get_right(), source_node.get_left(), color=INK, stroke_width=2)
        self.play(Create(a1), run_time=0.3)

        stamp = Text("Confirmed", font_size=24, color=INK, font=FONT).next_to(source_node, RIGHT, buff=0.25)
        self.play(Write(stamp), run_time=0.3)

        a2 = Arrow(source_node.get_right(), doc_box.get_left(), color=TERRA, stroke_width=2)
        self.play(Create(a2), run_time=0.3)

        reject = Text("Bad citation?\nDissolved.", font_size=24, color=INK, font=FONT).next_to(source_node, LEFT, buff=0.2)
        # Place rejected_clone above circle to avoid overlapping source_label and circle arc
        rejected_clone = citation.copy().scale(0.7).next_to(source_node, UP, buff=0.25)
        self.play(Write(reject), FadeIn(rejected_clone), run_time=0.3)
        self.play(FadeOut(rejected_clone, scale=0.1), run_time=0.4)

        verified = Text("Verify before you cite.", font_size=32, color=INK, weight=BOLD, font=FONT).shift(DOWN*2.6)
        self.play(Write(verified), run_time=0.5)
        self.wait(0.7)


class B04_LaunderingDiagram(Scene):
    """B04 — source laundering: a real number attaches to the wrong banner."""
    def construct(self):
        num = Text("73%", font_size=60, color=INK, weight=BOLD, font=FONT)
        source_a = RoundedRectangle(width=3.5, height=1.5, color=INK, stroke_width=2).set_fill("#EAE7DC", opacity=1).shift(LEFT*4 + UP*1.5)
        # Labels above the box so 73% text (centered in box) doesn't overlap them
        a_label = Text("Source A", font_size=24, color=INK, weight=BOLD, font=FONT).next_to(source_a, UP, buff=0.1)
        self.play(FadeIn(source_a), Write(a_label), run_time=0.4)

        num.move_to(source_a.get_center())
        self.play(Write(num), run_time=0.4)

        source_b = RoundedRectangle(width=3.5, height=1.5, color=INK, stroke_width=2.5).set_fill(CREAM, opacity=0).shift(RIGHT*4 + UP*1.5)
        b_label = Text("Source B", font_size=24, color=INK, weight=BOLD, font=FONT).next_to(source_b, UP, buff=0.1)
        self.play(FadeIn(source_b), Write(b_label), run_time=0.3)

        self.play(num.animate.move_to(source_b.get_center()), run_time=0.8)

        reader_label = Text("What the reader sees:", font_size=26, color=INK, font=FONT).shift(DOWN*1.2)
        banner = RoundedRectangle(width=6, height=1.2, color=INK, stroke_width=2).set_fill(CREAM, opacity=0).shift(DOWN*2.4)
        banner_text = Text("Source B reports: 73%", font_size=26, color=INK, weight=BOLD, font=FONT).move_to(banner)
        self.play(Write(reader_label), FadeIn(banner), Write(banner_text), run_time=0.5)

        # FadeOut banner before writing problem — banner bottom stroke at y≈-3.0 crosses problem text
        self.play(FadeOut(banner), run_time=0.2)
        problem = Text("Real number. Wrong banner.", font_size=30, color=INK, weight=BOLD, font=FONT).shift(DOWN*3.0)
        self.play(Write(problem), run_time=0.5)
        self.wait(0.9)

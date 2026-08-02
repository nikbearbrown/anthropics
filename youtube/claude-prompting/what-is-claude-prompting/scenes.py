from manim import *

CREAM = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"

config.background_color = CREAM

class B01_IncantationStack(Scene):
    """B01 — wrong model: magic phrases pile up, output never changes."""
    def construct(self):
        output = RoundedRectangle(width=7, height=2.2, color=INK, stroke_width=2.5).set_fill("#EAE7DC", opacity=1).shift(RIGHT*2.5)
        output_text = Text("Generic output.", font_size=32, color=INK, font=FONT).move_to(output)
        self.play(FadeIn(output), Write(output_text), run_time=0.5)

        phrases = ["you are an expert", "think step by step", "be concise", "ignore previous instructions", "you MUST"]
        phrase_mobs = []
        for i, phrase in enumerate(phrases):
            p = Text(f'"{phrase}"', font_size=26, color=INK, font=FONT).move_to(LEFT*3.5 + UP*(1.8 - i*0.8))
            phrase_mobs.append(p)
            self.play(FadeIn(p, shift=RIGHT*0.3), run_time=0.3)

        arrow = Arrow(LEFT*0.8, output.get_left(), color=INK, stroke_width=2)
        self.play(Create(arrow), run_time=0.4)

        self.play(output_text.animate.set_color(INK), run_time=0.1)
        unchanged = Text("Unchanged.", font_size=28, color=INK, weight=BOLD, font=FONT).next_to(output, DOWN, buff=0.3)
        self.play(Write(unchanged), run_time=0.5)
        self.wait(1.0)


class B02_SpecConstraints(Scene):
    """B02 — right model: constraints listed left, region on right shrinks to target."""
    def construct(self):
        # Right half: the output space region (narrower so it doesn't overlap left labels)
        region = Rectangle(width=5, height=5.5, color=INK, stroke_width=2).set_fill(INK, opacity=0.06).shift(RIGHT*3)
        region_label = Text("Output space", font_size=24, color=INK, font=FONT).next_to(region, UP, buff=0.2)
        self.play(FadeIn(region), Write(region_label), run_time=0.5)

        # Left column: constraint labels at FIXED absolute positions — never overlap region or lines
        constraint_data = [
            ("Audience: senior engineer", UP*2.0),
            ("Format: numbered list", UP*0.65),
            ("Length: under 200 words", DOWN*0.65),
            ("One worked example", DOWN*2.0),
        ]
        target = Dot(color=TERRA, radius=0.22).move_to(region.get_center())

        shrink_factor = 1.0
        for label, y_pos in constraint_data:
            # Constraint label fixed in left column (x centered around -3.5)
            constraint_text = Text(label, font_size=26, color=INK, font=FONT).move_to(LEFT*3.5 + y_pos)
            # Horizontal rule across the region only (not full frame)
            rule = Line(region.get_left() + y_pos * 0.5, region.get_right() + y_pos * 0.5,
                        color=TERRA, stroke_width=2)
            shrink_factor *= 0.72
            self.play(Write(constraint_text), Create(rule),
                      region.animate.scale(shrink_factor),
                      run_time=0.5)

        self.play(FadeIn(target), run_time=0.4)
        spec_label = Text("Spec written.", font_size=36, color=INK, weight=BOLD, font=FONT).shift(DOWN*3.1)
        self.play(Write(spec_label), run_time=0.5)
        self.wait(0.8)


class B04_TheUnsaidConstraint(Scene):
    """B04 — do this now: find the one missing requirement."""
    def construct(self):
        region = Rectangle(width=7, height=4.5, color=INK, stroke_width=2).set_fill(INK, opacity=0.07)
        self.play(FadeIn(region), run_time=0.4)

        sides = [
            Line(region.get_corner(UL), region.get_corner(UR), color=INK, stroke_width=2),
            Line(region.get_corner(UL), region.get_corner(DL), color=INK, stroke_width=2),
            Line(region.get_corner(DR), region.get_corner(UR), color=INK, stroke_width=2),
        ]
        for s in sides:
            self.play(Create(s), run_time=0.25)

        gap_indicator = DashedLine(region.get_corner(DL), region.get_corner(DR),
                                   color=TERRA, stroke_width=2.5, dash_length=0.18)
        gap_label = Text("missing: output format", font_size=26, color=INK, font=FONT).next_to(gap_indicator, DOWN, buff=0.25)
        self.play(Create(gap_indicator), Write(gap_label), run_time=0.6)

        result_dot = Dot(color=TERRA, radius=0.18).move_to(region.get_bottom() + DOWN*0.8)
        self.play(FadeIn(result_dot), run_time=0.3)
        outside = Text("Output: outside the spec.", font_size=28, color=INK, font=FONT).next_to(result_dot, RIGHT, buff=0.2)
        self.play(Write(outside), run_time=0.4)

        bottom_line = Line(region.get_corner(DL), region.get_corner(DR), color=INK, stroke_width=2)
        self.play(Transform(gap_indicator, bottom_line), FadeOut(gap_label), run_time=0.5)
        self.play(result_dot.animate.move_to(region.get_center()), FadeOut(outside), run_time=0.5)
        snap = Text("Add the constraint.", font_size=34, color=INK, weight=BOLD, font=FONT).next_to(region, DOWN, buff=0.35)
        self.play(Write(snap), run_time=0.5)
        self.wait(0.8)

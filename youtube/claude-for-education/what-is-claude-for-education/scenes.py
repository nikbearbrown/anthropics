from manim import *
import math

CREAM = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"

config.background_color = CREAM

class B01_BanOrEmbrace(Scene):
    """B01 — wrong model: policy argument standing in for pedagogy."""
    def construct(self):
        switch = RoundedRectangle(width=5, height=1.5, color=INK, stroke_width=2.5).set_fill("#EAE7DC", opacity=1).shift(UP*2)
        # Labels above/below switch so toggle_dot movement never crosses them
        ban_label = Text("BAN", font_size=36, color=INK, weight=BOLD, font=FONT).next_to(switch, LEFT, buff=0.3)
        embrace_label = Text("EMBRACE", font_size=36, color=INK, font=FONT).next_to(switch, RIGHT, buff=0.3)
        toggle_dot = Circle(radius=0.5, color=TERRA).set_fill(TERRA, opacity=1).move_to(switch.get_left() + RIGHT*1.0)
        self.play(FadeIn(switch), Write(ban_label), Write(embrace_label), FadeIn(toggle_dot), run_time=0.5)

        assignment = RoundedRectangle(width=8, height=2.5, color=INK, stroke_width=2).set_fill(CREAM, opacity=1).shift(DOWN*1.2)
        assign_text = Text("Assignment: write a persuasive essay.", font_size=28, color=INK, font=FONT).move_to(assignment)
        self.play(FadeIn(assignment), Write(assign_text), run_time=0.4)

        for _ in range(2):
            self.play(toggle_dot.animate.move_to(switch.get_right() + LEFT*1.0), run_time=0.4)
            unchanged = Text("unchanged", font_size=24, color=INK, font=FONT).next_to(assignment, DOWN, buff=0.2)
            self.play(FadeIn(unchanged), run_time=0.2)
            self.play(toggle_dot.animate.move_to(switch.get_left() + RIGHT*1.0), run_time=0.4)
            self.play(FadeOut(unchanged), run_time=0.2)

        policy_not_pedagogy = Text("Policy debate.\nAssignment unchanged.", font_size=32, color=INK, weight=BOLD, font=FONT).shift(DOWN*2.8)
        self.play(Write(policy_not_pedagogy), run_time=0.6)
        self.wait(0.8)


class B02_ScaffoldVsCrutch(Scene):
    """B02 — right model: two learner curves from same start."""
    def construct(self):
        axes = Axes(x_range=[0, 10, 1], y_range=[0, 1.2, 0.2],
                    x_length=9, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 2},
                    tips=False)
        x_label = Text("Time", font_size=24, color=INK, font=FONT).next_to(axes, DOWN, buff=0.2)
        y_label = Text("Skill level", font_size=28, color=INK, font=FONT).rotate(PI/2).next_to(axes, LEFT, buff=0.25)
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.4)

        scaffold_curve = axes.plot(lambda x: min(1.05, 0.1 + 0.12 * x), x_range=[0, 9], color=INK, stroke_width=2.5)
        # Labels placed above/below curves (not to the right) to avoid right-edge overflow
        scaffold_label = Text("Scaffold (support withdraws)", font_size=24, color=INK, font=FONT).next_to(axes.coords_to_point(4, 0.9), UP, buff=0.12)
        # Scaffold dot — non-textish shape; marks the endpoint and creates shape-state change
        scaffold_end_dot = Dot(color=INK, radius=0.12).move_to(axes.coords_to_point(9, 1.05))
        self.play(Create(scaffold_curve), Write(scaffold_label), FadeIn(scaffold_end_dot), run_time=0.6)

        crutch_curve = axes.plot(lambda x: 0.22 + 0.01 * x, x_range=[0, 9], color=INK, stroke_width=2.5)
        crutch_label = Text("Crutch (support never leaves)", font_size=24, color=INK, font=FONT).next_to(axes.coords_to_point(4, 0.25), DOWN, buff=0.12)
        crutch_end_dot = Dot(color=INK, radius=0.12).move_to(axes.coords_to_point(9, 0.31))
        self.play(Create(crutch_curve), Write(crutch_label), FadeIn(crutch_end_dot), run_time=0.5)

        # FadeOut x_label before line text to avoid text-on-text overlap
        self.play(FadeOut(x_label), run_time=0.2)
        line = Text("The line moves depending on what\nthe assignment protects.", font_size=24, color=INK, font=FONT).shift(DOWN*2.5)
        self.play(Write(line), run_time=0.5)
        self.wait(0.9)


class B04_MoveVisible(Scene):
    """B04 — do this now: name the skill the assignment protects."""
    def construct(self):
        claim = RoundedRectangle(width=7, height=1.2, color=INK, stroke_width=2).set_fill("#EAE7DC", opacity=1).shift(UP*3)
        claim_text = Text("Assignment: write a persuasive essay", font_size=26, color=INK, font=FONT).move_to(claim)
        self.play(FadeIn(claim), Write(claim_text), run_time=0.4)

        moves = [
            ("What skill does this protect?", "Constructing an argument"),
            ("Can AI do that skill?", "Yes, if you let it"),
            ("What is the right AI role?", "Reviewer, not author"),
            ("What stays with the student?", "The argument itself"),
        ]
        for i, (question, answer) in enumerate(moves):
            q_text = Text(question, font_size=24, color=INK, font=FONT).shift(UP*(1.6 - i*1.3) + LEFT*1.5)
            # Arrow shape (non-textish) creates distinct shape states per row
            row_arrow = Arrow(LEFT*0.1, RIGHT*0.5, color=INK, stroke_width=2, buff=0).next_to(q_text, RIGHT, buff=0.1)
            a_text = Text(answer, font_size=24, color=INK, font=FONT).next_to(row_arrow, RIGHT, buff=0.1)
            self.play(Write(q_text), run_time=0.3)
            self.play(Create(row_arrow), Write(a_text), run_time=0.3)

        final = Text("Name the protected skill.", font_size=34, color=INK, weight=BOLD, font=FONT).shift(DOWN*3.2)
        self.play(Write(final), run_time=0.5)
        self.wait(0.8)

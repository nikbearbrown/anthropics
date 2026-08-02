from manim import *
import math

CREAM = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"

config.background_color = CREAM

class B01_BiggerSkillFallacy(Scene):
    """B01 — wrong model: scale is not the difference between skill and plugin."""
    def construct(self):
        small_skill = RoundedRectangle(width=3, height=2, color=INK, stroke_width=2).set_fill("#EAE7DC", opacity=1).shift(LEFT*3)
        small_label = Text("Skill", font_size=28, color=INK, font=FONT).move_to(small_skill)
        self.play(FadeIn(small_skill), Write(small_label), run_time=0.4)

        big_skill = RoundedRectangle(width=5.5, height=3.5, color=INK, stroke_width=2).set_fill("#EAE7DC", opacity=1).shift(RIGHT*2)
        big_label = Text("Bigger\nSkill?", font_size=30, color=INK, font=FONT).move_to(big_skill)
        self.play(TransformFromCopy(small_skill, big_skill), Write(big_label), run_time=0.6)

        # FadeOut label before cross to prevent label-on-line audit error
        self.play(FadeOut(big_label), run_time=0.2)
        cross = Cross(big_skill, color=TERRA, stroke_width=4)
        self.play(Create(cross), run_time=0.4)
        nope = Text("Scale is not the difference.", font_size=32, color=INK, weight=BOLD, font=FONT).shift(DOWN*2.6)
        self.play(Write(nope), run_time=0.5)
        self.wait(0.9)


class B02_BundleAssembly(Scene):
    """B02 — right model: plugin as a versioned bundle that travels to another machine."""
    def construct(self):
        machine_a = RoundedRectangle(width=4, height=3, color=INK, stroke_width=2.5).set_fill("#EAE7DC", opacity=1).shift(LEFT*4)
        a_label = Text("Your machine", font_size=22, color=INK, font=FONT).next_to(machine_a, UP, buff=0.2)

        items = ["Skill A", "Connector", "Command"]
        item_mobs = VGroup(*[
            Text(item, font_size=22, color=INK, font=FONT).move_to(machine_a.get_center() + UP*(0.8 - i*0.8))
            for i, item in enumerate(items)
        ])
        self.play(FadeIn(machine_a), Write(a_label), *[FadeIn(m) for m in item_mobs], run_time=0.5)

        bundle = RoundedRectangle(width=3, height=2.5, color=INK, stroke_width=2.5).set_fill(CREAM, opacity=0).move_to(machine_a)
        bundle_label = Text("Plugin v1.0", font_size=24, color=INK, weight=BOLD, font=FONT).move_to(bundle)
        # FadeOut items and machine before FadeIn bundle — avoids text-on-text overlap in audit
        self.play(FadeOut(VGroup(machine_a, item_mobs, a_label)), run_time=0.3)
        self.play(FadeIn(bundle), Write(bundle_label), run_time=0.5)

        machine_b = RoundedRectangle(width=4, height=3, color=INK, stroke_width=2.5).set_fill("#EAE7DC", opacity=1).shift(RIGHT*4)
        b_label = Text("Teammate's machine", font_size=22, color=INK, font=FONT).next_to(machine_b, UP, buff=0.2)
        arrow = Arrow(bundle.get_right(), machine_b.get_left(), color=INK, stroke_width=2.5)
        self.play(FadeIn(machine_b), Write(b_label), Create(arrow), run_time=0.5)
        bundle_copy = RoundedRectangle(width=2, height=1.6, color=INK, stroke_width=2).set_fill(CREAM, opacity=0).move_to(machine_b.get_center())
        bundle_copy_label = Text("Plugin v1.0", font_size=24, color=INK, font=FONT).move_to(bundle_copy)
        self.play(FadeIn(bundle_copy), FadeIn(bundle_copy_label), run_time=0.6)

        installed = Text("One command. Installed.", font_size=34, color=INK, weight=BOLD, font=FONT).shift(DOWN*2.5)
        self.play(Write(installed), run_time=0.5)
        self.wait(0.7)


class B04_TurkeyCurve(Scene):
    """B04 — Hume's limit: confidence rises from record, then breaks."""
    def construct(self):
        axes = Axes(x_range=[0, 10, 1], y_range=[0, 1.2, 0.2],
                    x_length=9, y_length=4.5,
                    axis_config={"color": INK, "stroke_width": 2},
                    tips=False)
        x_label = Text("Runs", font_size=24, color=INK, font=FONT).next_to(axes, DOWN, buff=0.2)
        y_label = Text("Confidence", font_size=24, color=INK, font=FONT).next_to(axes, LEFT, buff=0.2)
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.5)

        confidence_curve = axes.plot(lambda x: min(0.95, 0.3 + 0.07 * x), x_range=[0, 9.5], color=INK, stroke_width=2.5)
        self.play(Create(confidence_curve), run_time=0.8)

        break_point = axes.coords_to_point(9.5, 0.95)
        crash = axes.coords_to_point(9.8, 0.1)
        crash_line = Line(break_point, crash, color=TERRA, stroke_width=3)
        self.play(Create(crash_line), run_time=0.4)

        record_label = Text("The record.", font_size=24, color=INK, font=FONT).next_to(confidence_curve, UP, buff=0.2)
        not_world = Text("Not the world.", font_size=24, color=INK, weight=BOLD, font=FONT).next_to(crash_line, LEFT, buff=0.2)
        self.play(Write(record_label), Write(not_world), run_time=0.5)
        self.wait(0.9)

from manim import *
import numpy as np

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette
SKY    = "#56B4E9"
BLUE   = "#0072B2"
GREEN  = "#009E73"
VERM   = "#D55E00"
ORANGE = "#E69F00"
GRAY   = "#7c7c7c"


# ============================================================
# B05_ImmuneStarvation — initial animation
#   Reservoir (ORANGE outline) → thick left pipe → tumor cluster (7 BLUE)
#   Thin right pipe → lone immune cell (SKY/VERM dashed)
#   3 ORANGE dots along left pipe; starvation visible by absence on right
# ============================================================
class B05_ImmuneStarvation(Scene):
    def construct(self):
        # Reservoir — ORANGE outline, no fill, dots near bottom (nearly empty)
        reservoir = Rectangle(
            width=2.2, height=3.5,
            color=ORANGE,
            fill_opacity=0,
            stroke_width=3.5,
        ).move_to(ORIGIN)

        # 5 dots near the bottom of the reservoir (fixed absolute positions)
        res_dot_offsets = [
            np.array([-0.3,  -1.20, 0.0]),
            np.array([ 0.0,  -1.20, 0.0]),
            np.array([ 0.3,  -1.20, 0.0]),
            np.array([-0.15, -0.98, 0.0]),
            np.array([ 0.15, -0.98, 0.0]),
        ]
        res_dots = VGroup(*[
            Dot(point=offset, radius=0.10, color=ORANGE)
            for offset in res_dot_offsets
        ])

        # Thick left pipe — from reservoir toward tumor
        # Reservoir left edge at x = -1.1 (half of 2.2); pipe goes to x = -3.7
        thick_pipe = Line(
            np.array([-1.1, 0.0, 0.0]),
            np.array([-3.7, 0.0, 0.0]),
            color=GRAY,
            stroke_width=22,
        )

        # Tumor cluster — 7 BLUE circles
        tumor_circles = VGroup(*[
            Circle(radius=0.22, color=BLUE, fill_color=BLUE, fill_opacity=0.82, stroke_width=2)
            for _ in range(7)
        ])
        tumor_circles.arrange_in_grid(rows=3, cols=3, buff=0.10)
        tumor_circles.move_to(np.array([-5.2, 0.0, 0.0]))

        # 3 ORANGE dots along the left pipe (fixed positions)
        pipe_dot_positions = [
            np.array([-2.0, 0.0, 0.0]),
            np.array([-2.7, 0.0, 0.0]),
            np.array([-3.2, 0.0, 0.0]),
        ]
        pipe_dots = VGroup(*[
            Dot(point=pos, radius=0.09, color=ORANGE)
            for pos in pipe_dot_positions
        ])

        # Thin right pipe — from reservoir toward immune cell
        # Reservoir right edge at x = +1.1; pipe goes to x = +3.7
        thin_pipe = Line(
            np.array([1.1, 0.0, 0.0]),
            np.array([3.7, 0.0, 0.0]),
            color=GRAY,
            stroke_width=5,
        )

        # Lone immune cell — SKY fill, VERM dashed outline (starved)
        immune_cell = Circle(
            radius=0.36,
            fill_color=SKY,
            fill_opacity=0.20,
            stroke_width=3,
        )
        immune_cell.set_color(VERM)
        immune_cell.set_fill(SKY, opacity=0.20)
        immune_cell.move_to(np.array([4.2, 0.0, 0.0]))

        # Build sequence
        self.play(FadeIn(reservoir), FadeIn(res_dots), run_time=0.6)
        self.play(Create(thick_pipe), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(c) for c in tumor_circles], lag_ratio=0.12, run_time=1.0)
        )
        self.play(FadeIn(pipe_dots), run_time=0.4)
        self.play(Create(thin_pipe), run_time=0.5)
        self.play(FadeIn(immune_cell), run_time=0.5)
        self.wait(0.9)


# ============================================================
# B07_ImmuneStarvationContrast — revised animation with flow dynamics
#   Dots flow rapidly left (LaggedStart) → tumor grows (scale 1.15)
#   One dot starts right, fades before arrival
#   Immune cell shrinks (scale 0.85)
#   Reservoir dots disappear (empties)
# ============================================================
class B07_ImmuneStarvationContrast(Scene):
    def construct(self):
        # Static layout (same as B05)
        reservoir = Rectangle(
            width=2.2, height=3.5,
            color=ORANGE,
            fill_opacity=0,
            stroke_width=3.5,
        ).move_to(ORIGIN)

        res_dot_offsets = [
            np.array([-0.3,  -1.20, 0.0]),
            np.array([ 0.0,  -1.20, 0.0]),
            np.array([ 0.3,  -1.20, 0.0]),
            np.array([-0.15, -0.98, 0.0]),
            np.array([ 0.15, -0.98, 0.0]),
        ]
        res_dots = VGroup(*[
            Dot(point=offset, radius=0.10, color=ORANGE)
            for offset in res_dot_offsets
        ])

        thick_pipe = Line(
            np.array([-1.1, 0.0, 0.0]),
            np.array([-3.7, 0.0, 0.0]),
            color=GRAY,
            stroke_width=22,
        )

        tumor_circles = VGroup(*[
            Circle(radius=0.22, color=BLUE, fill_color=BLUE, fill_opacity=0.82, stroke_width=2)
            for _ in range(7)
        ])
        tumor_circles.arrange_in_grid(rows=3, cols=3, buff=0.10)
        tumor_circles.move_to(np.array([-5.2, 0.0, 0.0]))

        thin_pipe = Line(
            np.array([1.1, 0.0, 0.0]),
            np.array([3.7, 0.0, 0.0]),
            color=GRAY,
            stroke_width=5,
        )

        immune_cell = Circle(
            radius=0.36,
            fill_color=SKY,
            fill_opacity=0.20,
            stroke_width=3,
        )
        immune_cell.set_color(VERM)
        immune_cell.set_fill(SKY, opacity=0.20)
        immune_cell.move_to(np.array([4.2, 0.0, 0.0]))

        # Show the static layout
        self.play(
            FadeIn(reservoir), FadeIn(res_dots),
            Create(thick_pipe), Create(thin_pipe),
            run_time=0.7,
        )
        self.play(
            LaggedStart(*[FadeIn(c) for c in tumor_circles], lag_ratio=0.10, run_time=0.8)
        )
        self.play(FadeIn(immune_cell), run_time=0.4)
        self.wait(0.3)

        # --- Flow animation ---
        # 1. Reservoir dots flow rapidly LEFT toward tumor cluster
        tumor_center = np.array([-5.2, 0.0, 0.0])

        # Flowing dots start at reservoir dot positions and move to tumor
        flowing_targets = [
            tumor_center + np.array([0.0,  0.22, 0.0]),
            tumor_center + np.array([0.3,  0.22, 0.0]),
            tumor_center + np.array([-0.3, 0.22, 0.0]),
            tumor_center + np.array([0.0, -0.22, 0.0]),
            tumor_center + np.array([0.3, -0.22, 0.0]),
        ]
        flowing_dots = VGroup(*[
            Dot(point=off.copy(), radius=0.09, color=ORANGE)
            for off in res_dot_offsets
        ])
        self.add(flowing_dots)

        self.play(
            LaggedStart(
                *[d.animate.move_to(t)
                  for d, t in zip(flowing_dots, flowing_targets)],
                lag_ratio=0.08,
                run_time=1.0,
            )
        )

        # 2. Reservoir visibly empties — remove dots
        self.play(FadeOut(res_dots), FadeOut(flowing_dots), run_time=0.4)

        # 3. Tumor cluster grows as it consumes
        self.play(tumor_circles.animate.scale(1.15), run_time=0.5)

        # 4. One lone dot starts right toward immune cell — fades before arrival
        lone_dot = Dot(point=np.array([1.5, 0.0, 0.0]), radius=0.09, color=ORANGE)
        mid_pos  = np.array([2.8, 0.0, 0.0])
        self.add(lone_dot)
        self.play(lone_dot.animate.move_to(mid_pos), run_time=0.5)
        self.play(FadeOut(lone_dot), run_time=0.5)

        # 5. Immune cell shrinks — starvation
        self.play(immune_cell.animate.scale(0.85), run_time=0.6)
        self.wait(0.8)

class STD_B01_claude_liam_immune_starva(Scene):
    """SHOW-DONT-TELL retrofit for B01 in claude-liam-immune-starvation.
    Narration: 'The tumor microenvironment is a resource battlefield. Glucose, amino acids, oxyg'
    Duration: 12.5s  Lines: 4  font_sz: 34
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Immune Starvation"
        body_lines = ["The tumor microenvironment is a resource", "battlefield", "Glucose, amino acids, oxygen \u2014 whatever", "the tumor needs, it takes"]
        spark_str = "This plate shows what that looks like for an immune cell try"

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=34)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 2.93)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B02_claude_liam_immune_starva(Scene):
    """SHOW-DONT-TELL retrofit for B02 in claude-liam-immune-starvation.
    Narration: 'T-cells need glucose and arginine to proliferate and kill. Tumors consume both a'
    Duration: 15.1s  Lines: 6  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Immune Starvation"
        body_lines = ["T-cells need glucose and arginine to proliferate", "and kill", "Tumors consume both at rates normal tissue never", "approaches", "The T-cell starves \u2014 not attacked, not suppressed", "by a checkpoint, just outcompeted"]
        spark_str = "Metabolic immunotherapy tries to level the playing field"

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=28)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 2.39)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B08_claude_liam_immune_starva(Scene):
    """SHOW-DONT-TELL retrofit for B08 in claude-liam-immune-starvation.
    Narration: 'One pool, two drinkers, an asymmetric draw. The animation made the competition c'
    Duration: 21.1s  Lines: 5  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Immune Starvation"
        body_lines = ["One pool, two drinkers, an asymmetric draw", "The animation made the competition concrete:", "watch where the dots go, and you have\u2026", "Claude ported the plate geometry in one prompt", "and added the flow dynamics in one revision"]
        spark_str = "The pattern \u2014 reservoir, directional pipes, dot animation \u2014 "

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=28)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 4.07)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

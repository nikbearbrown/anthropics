from manim import *
import numpy as np
import math

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette
BLUE  = "#0072B2"
VERM  = "#D55E00"
GREEN = "#009E73"
GRAY  = "#7c7c7c"

# Loop geometry
LOOP_R = 2.8        # radius of the cell cycle circle
GATE_DEG = 210      # gate position on the loop (in degrees)
CELL_DEGS = (234, 186)   # pre-gate, post-gate


def loop_pos(deg):
    """Manim 3D point on the loop at given degree angle."""
    a = math.radians(deg)
    return np.array([LOOP_R * math.cos(a), LOOP_R * math.sin(a), 0.0])


def make_loop():
    return Circle(radius=LOOP_R, color=GRAY, stroke_width=3.5, fill_opacity=0)


def make_gate():
    return (Square(side_length=0.48, color=VERM,
                   fill_color=VERM, fill_opacity=0.50, stroke_width=3.2)
            .move_to(loop_pos(GATE_DEG)))


def make_cell(deg, radius=0.30):
    return (Circle(radius=radius, color=BLUE,
                   fill_color=BLUE, fill_opacity=0.20, stroke_width=3.0)
            .move_to(loop_pos(deg)))


def make_radial_arrow(deg, length=0.9, buff_r=0.32):
    """Short arrow pointing radially outward from the loop at given angle."""
    p = loop_pos(deg)
    d = p / np.linalg.norm(p)  # unit radial direction
    start = p + d * buff_r
    end   = p + d * (buff_r + length)
    return Arrow(start, end, buff=0, color=GRAY,
                 stroke_width=2.8,
                 max_tip_length_to_length_ratio=0.22)


# ============================================================
# B05_RestrictionPoint — initial animation
#   Draw loop → reveal gate → reveal two cells → grow arrows → Flash gate
# ============================================================
class B05_RestrictionPoint(Scene):
    def construct(self):
        loop = make_loop()
        gate = make_gate()
        cells = [make_cell(d) for d in CELL_DEGS]
        arrows = [make_radial_arrow(d) for d in CELL_DEGS]

        # 1. Draw the cycle loop
        self.play(Create(loop), run_time=0.9)

        # 2. Gate appears with a slight scale pop
        self.play(FadeIn(gate, scale=1.25), run_time=0.4)

        # 3. LaggedStart reveal two cells
        self.play(
            LaggedStart(
                *[FadeIn(c, scale=0.9) for c in cells],
                lag_ratio=0.35, run_time=0.75,
            )
        )

        # 4. Grow both radial arrows simultaneously
        self.play(*[GrowArrow(a) for a in arrows], run_time=0.65)

        # 5. Flash the gate to emphasize it is the decision point
        self.play(
            Flash(gate.get_center(), color=VERM,
                  line_length=0.27, num_lines=12, flash_radius=0.60),
            run_time=0.5,
        )
        self.wait(0.8)


# ============================================================
# B07_RestrictionPointFate — revised: fate animation
#   Same setup, then:
#   - pre-gate cell (234°) moves off the loop radially (exits)
#   - post-gate cell (186°) arrow retracts — committed
#   - Flash gate again
# ============================================================
class B07_RestrictionPointFate(Scene):
    def construct(self):
        loop   = make_loop()
        gate   = make_gate()
        pre_cell  = make_cell(CELL_DEGS[0])   # 234° — before gate
        post_cell = make_cell(CELL_DEGS[1])   # 186° — after gate
        pre_arrow  = make_radial_arrow(CELL_DEGS[0])
        post_arrow = make_radial_arrow(CELL_DEGS[1])

        # 1. Draw setup (same as B05)
        self.play(Create(loop), run_time=0.9)
        self.play(FadeIn(gate, scale=1.25), run_time=0.4)
        self.play(
            LaggedStart(
                FadeIn(pre_cell, scale=0.9),
                FadeIn(post_cell, scale=0.9),
                lag_ratio=0.35, run_time=0.75,
            )
        )
        self.play(
            GrowArrow(pre_arrow),
            GrowArrow(post_arrow),
            run_time=0.65,
        )
        self.wait(0.35)

        # 2. Fate animation
        # Pre-gate cell exits radially (moves outward along its arrow direction)
        pre_p = loop_pos(CELL_DEGS[0])
        pre_d = pre_p / np.linalg.norm(pre_p)
        exit_target = pre_p + pre_d * 1.8  # off the screen edge

        # Post-gate cell's arrow retracts (shrinks to zero length)
        post_p = loop_pos(CELL_DEGS[1])
        post_d = post_p / np.linalg.norm(post_p)
        retract_target = post_p + post_d * 0.35  # arrow tip barely visible

        # Pre-gate cell exits radially; post-gate arrow fades away
        self.play(
            pre_cell.animate.move_to(exit_target),
            run_time=0.6,
        )
        self.play(
            FadeOut(pre_cell, run_time=0.3),
            FadeOut(post_arrow, run_time=0.4),
            run_time=0.45,
        )

        # 3. Flash gate again — position is everything
        self.play(
            Flash(gate.get_center(), color=VERM,
                  line_length=0.27, num_lines=12, flash_radius=0.60),
            run_time=0.5,
        )
        self.wait(0.8)

class STD_B01_claude_liam_restriction_p(Scene):
    """SHOW-DONT-TELL retrofit for B01 in claude-liam-restriction-point.
    Narration: "The restriction point is the cell cycle's point of no return. Early in G1, the c"
    Duration: 14.5s  Lines: 4  font_sz: 34
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Restriction Point"
        body_lines = ["The restriction point is the cell cycle's", "point of no return", "Early in G1, the cell is still checking:", "are conditions good enough to divide?"]
        spark_str = "This plate animates the same stimulus \u2014 growth factor withdr"

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

        reveal_t = max(0.30, 3.43)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B02_claude_liam_restriction_p(Scene):
    """SHOW-DONT-TELL retrofit for B02 in claude-liam-restriction-point.
    Narration: 'Before the restriction point, withdrawal means exit — the cell slides off the lo'
    Duration: 13.5s  Lines: 6  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Restriction Point"
        body_lines = ["Before the restriction point, withdrawal", "means exit \u2014 the cell slides off the loop", "and\u2026", "After it, withdrawal means nothing \u2014 the", "cell has already committed to dividing no", "matter\u2026"]
        spark_str = "One gate, two completely opposite outcomes"

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

        reveal_t = max(0.30, 2.11)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B08_claude_liam_restriction_p(Scene):
    """SHOW-DONT-TELL retrofit for B08 in claude-liam-restriction-point.
    Narration: "The gate's position on the loop is everything. Two identical cells, one identica"
    Duration: 18.8s  Lines: 7  font_sz: 24
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Restriction Point"
        body_lines = ["The gate's position on the loop is everything", "Two identical cells, one identical signal, two", "opposite fates", "The animation made that spatial distinction", "visible", "Claude ported the loop geometry, placed the gate", "at the right angle, placed two cells,\u2026"]
        spark_str = "The revision animated the divergence \u2014 one cell exits, one c"

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
            lobj = Text(txt, font="EB Garamond", color=col, font_size=24)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 2.57)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

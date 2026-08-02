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

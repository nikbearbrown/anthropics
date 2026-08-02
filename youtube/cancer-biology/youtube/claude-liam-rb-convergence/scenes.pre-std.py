from manim import *
import numpy as np

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette
SKY   = "#56B4E9"
BLUE  = "#0072B2"
GREEN = "#009E73"
VERM  = "#D55E00"
GRAY  = "#7c7c7c"

# Geometry (ported from plates_gen.py p05 / rb_scene.py)
IN_YS    = [2.3, 0.9, -0.5, -1.9]
IN_X     = -5.0
GATE_POS = [0.4, 0.2, 0]
FINAL_POS = [5.0, 0.2, 0]


def make_inputs():
    return VGroup(*[
        RoundedRectangle(width=2.0, height=1.0, corner_radius=0.18,
                         color=SKY, fill_color=SKY, fill_opacity=0.16,
                         stroke_width=3.2)
        .move_to([IN_X, y, 0])
        for y in IN_YS
    ])


def make_gate():
    return (RoundedRectangle(width=1.9, height=1.9, corner_radius=0.22,
                              color=BLUE, fill_color=BLUE, fill_opacity=0.18,
                              stroke_width=4.2)
            .move_to(GATE_POS))


def make_final():
    return (RoundedRectangle(width=1.8, height=1.05, corner_radius=0.18,
                              color=GREEN, fill_color=GREEN, fill_opacity=0.16,
                              stroke_width=3.4)
            .move_to(FINAL_POS))


def make_fan_arrows(inputs, gate):
    """Fan-in arrows from each input's right edge to gate's left edge."""
    conv = gate.get_left()
    return VGroup(*[
        Arrow(start=r.get_right(), end=conv, buff=0.12,
              color=GRAY, stroke_width=3.2,
              max_tip_length_to_length_ratio=0.09,
              max_stroke_width_to_length_ratio=6)
        for r in inputs
    ])


def make_out_arrow(gate, final):
    return Arrow(start=gate.get_right(), end=final.get_left(), buff=0.12,
                 color=GRAY, stroke_width=3.4,
                 max_tip_length_to_length_ratio=0.16)


# ============================================================
# B05_RbConvergence — exact choreography from rb_scene.py
#   LaggedStart inputs → Create gate → LaggedStart arrows →
#   Flash+scale gate → scale back → GrowArrow output + FadeIn final
# ============================================================
class B05_RbConvergence(Scene):
    def construct(self):
        inputs    = make_inputs()
        gate      = make_gate()
        final     = make_final()
        arrows    = make_fan_arrows(inputs, gate)
        out_arrow = make_out_arrow(gate, final)

        # 1. LaggedStart inputs (from rb_scene.py)
        self.play(
            LaggedStart(
                *[FadeIn(r, shift=RIGHT * 0.4) for r in inputs],
                lag_ratio=0.18, run_time=1.4,
            )
        )

        # 2. Create gate
        self.play(Create(gate), run_time=0.6)

        # 3. LaggedStart fan-in arrows
        self.play(
            LaggedStart(
                *[GrowArrow(a) for a in arrows],
                lag_ratio=0.12, run_time=1.5,
            )
        )

        # 4. Flash + scale gate (opening) — split animate chains for static checker
        self.play(
            Flash(gate.get_center(), color=BLUE,
                  line_length=0.35, num_lines=16, flash_radius=1.3),
            gate.animate.scale(1.10),
            run_time=0.5,
        )
        self.play(gate.animate.scale(1 / 1.10), run_time=0.35)

        # 5. Output arrow + final node
        self.play(
            GrowArrow(out_arrow),
            FadeIn(final, shift=RIGHT * 0.3, scale=1.05),
            run_time=0.8,
        )
        self.wait(0.8)


# ============================================================
# B07_RbConvergenceBlocked — revision: one input blocked
#   Same setup, then after gate opens:
#   - dim input[0] and draw VERM X-mark on its arrow
#   - 3 remaining arrows still reach gate → gate still open
#   - Flash gate again to show it's still open
# ============================================================
class B07_RbConvergenceBlocked(Scene):
    def construct(self):
        inputs    = make_inputs()
        gate      = make_gate()
        final     = make_final()
        arrows    = make_fan_arrows(inputs, gate)
        out_arrow = make_out_arrow(gate, final)

        # 1. Same reveal as B05
        self.play(
            LaggedStart(
                *[FadeIn(r, shift=RIGHT * 0.4) for r in inputs],
                lag_ratio=0.18, run_time=1.4,
            )
        )
        self.play(Create(gate), run_time=0.6)
        self.play(
            LaggedStart(
                *[GrowArrow(a) for a in arrows],
                lag_ratio=0.12, run_time=1.5,
            )
        )
        self.play(
            Flash(gate.get_center(), color=BLUE,
                  line_length=0.35, num_lines=16, flash_radius=1.3),
            gate.animate.scale(1.10),
            run_time=0.5,
        )
        self.play(gate.animate.scale(1 / 1.10), run_time=0.35)
        self.play(
            GrowArrow(out_arrow),
            FadeIn(final, shift=RIGHT * 0.3, scale=1.05),
            run_time=0.8,
        )
        self.wait(0.4)

        # 2. Block input[0]: dim the node and its arrow, add VERM X-mark
        blocked_node  = inputs[0]
        blocked_arrow = arrows[0]

        # X-mark at the midpoint of the blocked arrow
        arrow_mid = blocked_arrow.get_center()
        x_size = 0.22
        xmark = VGroup(
            Line(arrow_mid + np.array([-x_size, x_size, 0]),
                 arrow_mid + np.array([x_size, -x_size, 0]),
                 color=VERM, stroke_width=7),
            Line(arrow_mid + np.array([-x_size, -x_size, 0]),
                 arrow_mid + np.array([x_size, x_size, 0]),
                 color=VERM, stroke_width=7),
        )

        self.play(
            FadeOut(blocked_node),
            FadeOut(blocked_arrow),
            run_time=0.4,
        )
        self.play(FadeIn(xmark), run_time=0.3)

        # 3. Show gate still open (other 3 arrows still there → Flash again)
        self.play(
            Flash(gate.get_center(), color=BLUE,
                  line_length=0.28, num_lines=14, flash_radius=1.1),
            run_time=0.45,
        )
        self.wait(0.8)

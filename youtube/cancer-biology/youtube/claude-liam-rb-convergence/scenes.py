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

class STD_B01_claude_liam_rb_convergenc(Scene):
    """SHOW-DONT-TELL retrofit for B01 in claude-liam-rb-convergence.
    Narration: 'The Rb gate controls S-phase entry — whether the cell copies its DNA and commits'
    Duration: 17.3s  Lines: 6  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "RB Convergence"
        body_lines = ["The Rb gate controls S-phase entry \u2014", "whether the cell copies its DNA and", "commits to\u2026", "It receives convergent signals: growth", "factors, cyclin D levels, CDK4/6 kinase", "activity,\u2026"]
        spark_str = "Four separate inputs all funnel onto one gate"

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

        reveal_t = max(0.30, 2.75)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B02_claude_liam_rb_convergenc(Scene):
    """SHOW-DONT-TELL retrofit for B02 in claude-liam-rb-convergence.
    Narration: 'That convergence is the cancer vulnerability. Block one kinase — say with a CDK4'
    Duration: 14.7s  Lines: 5  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "RB Convergence"
        body_lines = ["That convergence is the cancer", "vulnerability", "Block one kinase \u2014 say with a CDK4/6", "inhibitor \u2014 and three other signals still", "push the\u2026"]
        spark_str = "The animation makes that plain: the gate doesn't care how ma"

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

        reveal_t = max(0.30, 2.78)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B08_claude_liam_rb_convergenc(Scene):
    """SHOW-DONT-TELL retrofit for B08 in claude-liam-rb-convergence.
    Narration: 'Fan-in is a topology, and topology has consequences. One gate, four inputs, none'
    Duration: 18.8s  Lines: 8  font_sz: 24
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "RB Convergence"
        body_lines = ["Fan-in is a topology, and topology has", "consequences", "One gate, four inputs, none of them sufficient", "alone but all pushing toward the same\u2026", "The motion showed why single-target inhibition", "keeps failing at this node", "Claude ported the geometry from the reference", "scene in one prompt"]
        spark_str = "The revision added the blocked-input demonstration in one mo"

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

        reveal_t = max(0.30, 2.25)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

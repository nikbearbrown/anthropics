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


def _make_hub():
    return RoundedRectangle(
        width=1.7, height=1.7,
        corner_radius=0.22,
        color=GRAY,
        fill_color=GRAY,
        fill_opacity=0.18,
        stroke_width=3.2,
    ).move_to(ORIGIN)


def _make_recA():
    return RoundedRectangle(
        width=1.9, height=1.1,
        corner_radius=0.18,
        color=BLUE,
        fill_color=BLUE,
        fill_opacity=0.16,
        stroke_width=3.0,
    ).move_to(np.array([-4.5, 2.0, 0.0]))


def _make_recB(opacity=0.20):
    r = RoundedRectangle(
        width=1.9, height=1.1,
        corner_radius=0.18,
        color=ORANGE,
        fill_color=ORANGE,
        fill_opacity=0.16,
        stroke_width=3.0,
    ).move_to(np.array([-4.5, -2.0, 0.0]))
    r.set_opacity(opacity)
    return r


def _make_output_cluster():
    out = VGroup(*[
        Circle(radius=0.22, color=GREEN, fill_color=GREEN, fill_opacity=0.82, stroke_width=2)
        for _ in range(6)
    ])
    out.arrange_in_grid(rows=2, cols=3, buff=0.12)
    out.move_to(np.array([4.8, 0.0, 0.0]))
    return out


def _make_block():
    """VERM plug rectangle on the A-arrow midpoint."""
    plug = Rectangle(
        width=0.28, height=0.68,
        color=VERM,
        fill_color=VERM,
        fill_opacity=0.65,
        stroke_width=2,
    ).move_to(np.array([-2.15, 1.15, 0.0]))
    xmark = VGroup(
        Line(
            np.array([-2.35, 1.35, 0.0]),
            np.array([-1.95, 0.95, 0.0]),
            color=VERM, stroke_width=6,
        ),
        Line(
            np.array([-2.35, 0.95, 0.0]),
            np.array([-1.95, 1.35, 0.0]),
            color=VERM, stroke_width=6,
        ),
    )
    return plug, xmark


# ============================================================
# B05_BypassTrack — initial animation
#   Hub + receptor A + A blocked → receptor B activates → output
# ============================================================
class B05_BypassTrack(Scene):
    def construct(self):
        hub    = _make_hub()
        recA   = _make_recA()
        recB   = _make_recB(opacity=0.20)
        output = _make_output_cluster()
        plug, xmark = _make_block()

        # Arrows (fixed absolute coords)
        arrowA = Arrow(
            np.array([-3.55,  1.80, 0.0]),
            np.array([-0.85,  0.50, 0.0]),
            color=GRAY, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.12,
        )
        arrowB = Arrow(
            np.array([-3.55, -1.80, 0.0]),
            np.array([-0.85, -0.50, 0.0]),
            color=ORANGE, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.12,
        )
        hub_out_arrow = Arrow(
            np.array([0.85, 0.0, 0.0]),
            np.array([3.4,  0.0, 0.0]),
            color=GRAY, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.12,
        )

        # 1. Hub + receptor A appear; A-arrow grows
        self.play(FadeIn(hub), FadeIn(recA), run_time=0.6)
        self.play(GrowArrow(arrowA), run_time=0.6)

        # 2. Block slides onto A-arrow
        self.play(FadeIn(plug), FadeIn(xmark), run_time=0.5)

        # 3. Receptor B activates (faint → full opacity); B-arrow grows
        self.play(recB.animate.set_opacity(1.0), run_time=0.5)
        self.play(GrowArrow(arrowB), run_time=0.6)

        # 4. Hub-to-output arrow grows
        self.play(GrowArrow(hub_out_arrow), run_time=0.5)

        # 5. Output cluster activates
        self.play(
            LaggedStart(
                *[FadeIn(c, scale=0.7) for c in output],
                lag_ratio=0.12,
                run_time=0.9,
            )
        )
        self.play(
            Flash(output.get_center(), color=GREEN, line_length=0.35, num_lines=12, flash_radius=1.1),
            run_time=0.4,
        )
        self.wait(0.8)


# ============================================================
# B07_BypassTrackFlow — revised animation with signal-flow dots
#   ORANGE dot B → hub → GRAY dot hub → output; one-by-one assembly; A-block Flash
# ============================================================
class B07_BypassTrackFlow(Scene):
    def construct(self):
        hub    = _make_hub()
        recA   = _make_recA()
        recB   = _make_recB(opacity=0.20)
        output = _make_output_cluster()
        plug, xmark = _make_block()

        arrowA = Arrow(
            np.array([-3.55,  1.80, 0.0]),
            np.array([-0.85,  0.50, 0.0]),
            color=GRAY, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.12,
        )
        arrowB = Arrow(
            np.array([-3.55, -1.80, 0.0]),
            np.array([-0.85, -0.50, 0.0]),
            color=ORANGE, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.12,
        )
        hub_out_arrow = Arrow(
            np.array([0.85, 0.0, 0.0]),
            np.array([3.4,  0.0, 0.0]),
            color=GRAY, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.12,
        )

        # 1. Build static layout: hub + A (blocked) + B (faint) + arrows
        self.play(FadeIn(hub), FadeIn(recA), run_time=0.5)
        self.play(GrowArrow(arrowA), run_time=0.5)
        self.play(FadeIn(plug), FadeIn(xmark), run_time=0.4)
        self.play(recB.animate.set_opacity(1.0), run_time=0.4)
        self.play(GrowArrow(arrowB), run_time=0.5)
        self.play(GrowArrow(hub_out_arrow), run_time=0.5)
        self.wait(0.2)

        # 2. ORANGE dot travels from receptor B → hub
        orange_dot = Dot(
            point=np.array([-4.5, -2.0, 0.0]),
            radius=0.12,
            color=ORANGE,
        )
        self.add(orange_dot)
        self.play(
            orange_dot.animate.move_to(ORIGIN),
            run_time=0.7,
        )
        self.play(FadeOut(orange_dot), run_time=0.2)

        # 3. GRAY dot travels from hub → output cluster
        gray_dot = Dot(
            point=ORIGIN,
            radius=0.12,
            color=GRAY,
        )
        self.add(gray_dot)
        self.play(
            gray_dot.animate.move_to(np.array([4.8, 0.0, 0.0])),
            run_time=0.7,
        )
        self.play(FadeOut(gray_dot), run_time=0.2)

        # 4. Output circles assemble one-by-one
        self.play(
            LaggedStart(
                *[FadeIn(c, scale=0.7) for c in output],
                lag_ratio=0.15,
                run_time=1.0,
            )
        )

        # 5. Flash the block on A's arrow — reminder: A still blocked
        self.play(
            Flash(
                np.array([-2.15, 1.15, 0.0]),
                color=VERM,
                line_length=0.3,
                num_lines=10,
                flash_radius=0.8,
            ),
            run_time=0.5,
        )
        self.wait(0.8)


class STD_B01_claude_liam_bypass_track(Scene):
    """SHOW-DONT-TELL retrofit for B01 in claude-liam-bypass-track.
    Narration: 'Targeted therapies block specific receptors. The assumption is that blocking the'
    Duration: 14.2s  Lines: 4  font_sz: 34
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Bypass Track"
        body_lines = ["Targeted therapies block specific", "receptors", "The assumption is that blocking the", "receptor blocks the signal"]
        spark_str = "But cells have multiple receptor inputs that converge on the"

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

        reveal_t = max(0.30, 3.36)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B02_claude_liam_bypass_track(Scene):
    """SHOW-DONT-TELL retrofit for B02 in claude-liam-bypass-track.
    Narration: 'MET amplification in EGFR-mutant lung cancer is the textbook case. Erlotinib blo'
    Duration: 18.3s  Lines: 5  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Bypass Track"
        body_lines = ["MET amplification in EGFR-mutant lung cancer is", "the textbook case", "Erlotinib blocks EGFR \u2014 receptor A \u2014 but the", "tumor amplifies MET \u2014 receptor B \u2014 which\u2026", "The output, proliferation, is restored"]
        spark_str = "Bypass resistance requires combination therapy hitting multi"

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

        reveal_t = max(0.30, 3.49)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B08_claude_liam_bypass_track(Scene):
    """SHOW-DONT-TELL retrofit for B08 in claude-liam-bypass-track.
    Narration: 'Same hub, different front door. The animation showed the critical topology: conv'
    Duration: 21.3s  Lines: 5  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Bypass Track"
        body_lines = ["Same hub, different front door", "The animation showed the critical topology:", "convergence means blocking upstream doesn't\u2026", "Claude ported the plate geometry in one prompt", "and added the dot-flow signal animation in\u2026"]
        spark_str = "The pattern \u2014 convergent receptors, one hub, animated dot as"

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

        reveal_t = max(0.30, 4.10)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

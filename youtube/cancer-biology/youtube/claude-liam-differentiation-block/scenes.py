from manim import *
import numpy as np

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette (matches plates_gen.py)
SKY   = "#56B4E9"
BLUE  = "#0072B2"
GREEN = "#009E73"
VERM  = "#D55E00"
GRAY  = "#7c7c7c"
INK   = "#333333"

# ============================================================
# Layout constants (Manim frame ±7.11 wide, ±4.0 tall)
# Left panel origin:  x0=-5.5, y0=+1.30
# Right panel origin: x0=+0.4, y0=+1.30
# Each step: dx=+1.10 right, dy=-0.72 up (staircase ascends left-to-right)
# ============================================================

STEPS = 5
STEP_DX = 1.10
STEP_DY = 0.72   # positive = step goes UP as index increases

PANEL_L_X0 = -5.5
PANEL_R_X0 =  0.5
PANEL_Y0   =  1.30   # y of the bottom (first) step


def step_positions(x0, y0):
    """Return list of (x,y) for steps 0..STEPS-1.
    Step 0 is bottom-left; step 4 is top-right (staircase climbs diagonally).
    """
    return [(x0 + i * STEP_DX, y0 - i * STEP_DY) for i in range(STEPS)]


def make_step_nodes(pts, color=SKY, fill_opacity=0.38):
    return VGroup(*[
        Circle(radius=0.28, color=color, fill_color=color,
               fill_opacity=fill_opacity, stroke_width=2.4)
        .move_to([x, y, 0])
        for x, y in pts
    ])


def make_step_arrows(pts, color=GRAY, sw=2.2):
    """Arrows between consecutive step nodes."""
    arrows = VGroup()
    for i in range(STEPS - 1):
        a = Arrow(
            start=[pts[i][0], pts[i][1], 0],
            end=[pts[i + 1][0], pts[i + 1][1], 0],
            buff=0.30, color=color, stroke_width=sw,
            max_tip_length_to_length_ratio=0.22,
            max_stroke_width_to_length_ratio=6,
        )
        arrows.add(a)
    return arrows


def make_verm_bar(pts):
    """Diagonal VERM bar cutting between step 1 and step 2."""
    bx = (pts[1][0] + pts[2][0]) / 2
    by = (pts[1][1] + pts[2][1]) / 2
    bar = Rectangle(
        width=0.24, height=1.15,
        fill_color=VERM, fill_opacity=0.85,
        stroke_color=VERM, stroke_width=3.0,
    ).rotate(-PI / 4).move_to([bx, by, 0])
    return bar


def make_pile(pts, n=8):
    """SKY circles piled up below step 1 (blocked side)."""
    base_x, base_y = pts[1]
    offsets = [
        (-0.38, 0.55), (0.06, 0.58), (0.46, 0.50),
        (-0.14, 0.95), (0.30, 0.90), (0.65, 0.78),
        (-0.42, 1.32), (0.12, 1.35),
    ]
    return VGroup(*[
        Circle(radius=0.18, color=SKY, fill_color=SKY,
               fill_opacity=0.55, stroke_width=1.5)
        .move_to([base_x + dx, base_y + dy, 0])
        for dx, dy in offsets[:n]
    ])


def make_star(x, y, opacity=0.55):
    return Star(
        n=6, outer_radius=0.38, inner_radius=0.16,
        color=BLUE, fill_color=BLUE, fill_opacity=opacity,
        stroke_width=2.4,
    ).move_to([x, y, 0])


def make_flow_arrow(pts):
    """Single GREEN flow arrow from step 0 to step STEPS-1."""
    return Arrow(
        start=[pts[0][0], pts[0][1], 0],
        end=[pts[-1][0], pts[-1][1], 0],
        buff=0.30, color=GREEN, stroke_width=3.8,
        max_tip_length_to_length_ratio=0.13,
        max_stroke_width_to_length_ratio=6,
    )


# ============================================================
# B05_DifferentiationBlock — two-panel static comparison
#   Left: blocked (VERM bar, pile-up)
#   Right: released (GREEN flow arrow, bright star)
# ============================================================
class B05_DifferentiationBlock(Scene):
    def construct(self):
        # ---- LEFT PANEL: BLOCKED ----
        pts_L = step_positions(PANEL_L_X0, PANEL_Y0)
        nodes_L = make_step_nodes(pts_L)
        arrows_L = make_step_arrows(pts_L, color=GRAY)
        bar = make_verm_bar(pts_L)
        pile = make_pile(pts_L)
        star_L = make_star(pts_L[-1][0], pts_L[-1][1], opacity=0.18)

        # Animate left panel
        self.play(
            LaggedStart(*[FadeIn(n) for n in nodes_L],
                        lag_ratio=0.20, run_time=0.85)
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in arrows_L],
                        lag_ratio=0.18, run_time=0.75)
        )
        self.play(FadeIn(bar), run_time=0.32)
        self.play(
            LaggedStart(*[FadeIn(p) for p in pile],
                        lag_ratio=0.13, run_time=0.85)
        )
        self.play(FadeIn(star_L), run_time=0.30)
        self.wait(0.40)

        # ---- RIGHT PANEL: RELEASED ----
        pts_R = step_positions(PANEL_R_X0, PANEL_Y0)
        nodes_R = make_step_nodes(pts_R, fill_opacity=0.42)
        flow = make_flow_arrow(pts_R)
        star_R = make_star(pts_R[-1][0], pts_R[-1][1], opacity=0.65)

        # Animate right panel
        self.play(
            LaggedStart(*[FadeIn(n) for n in nodes_R],
                        lag_ratio=0.20, run_time=0.80)
        )
        self.play(GrowArrow(flow), run_time=0.55)
        self.play(FadeIn(star_R), run_time=0.38)
        self.wait(0.75)


# ============================================================
# B07_DifferentiationBlockRelease — animated therapy release
#   Build blocked state → animate: bar FadeOut → pile moves up → GREEN arrow grows → star brightens
# ============================================================
class B07_DifferentiationBlockRelease(Scene):
    def construct(self):
        # Use left panel positions only (single state, centred slightly left)
        pts = step_positions(-3.0, 1.10)
        nodes = make_step_nodes(pts)
        arrows_gray = make_step_arrows(pts, color=GRAY)
        bar = make_verm_bar(pts)
        pile = make_pile(pts)
        star = make_star(pts[-1][0], pts[-1][1], opacity=0.18)

        # ---- BUILD BLOCKED STATE ----
        self.play(
            LaggedStart(*[FadeIn(n) for n in nodes],
                        lag_ratio=0.20, run_time=0.80)
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in arrows_gray],
                        lag_ratio=0.18, run_time=0.72)
        )
        self.play(FadeIn(bar), run_time=0.30)
        self.play(
            LaggedStart(*[FadeIn(p) for p in pile],
                        lag_ratio=0.13, run_time=0.80)
        )
        self.play(FadeIn(star), run_time=0.28)
        self.wait(0.40)  # hold blocked state

        # ---- RELEASE TRANSITION ----

        # 1. VERM bar fades out
        self.play(FadeOut(bar), run_time=0.42)

        # 2. Pile circles move up the staircase (LaggedStart toward top step)
        top_x, top_y = pts[-1]
        # Scatter pile circles toward top node in a small cloud
        pile_targets = [
            [top_x + dx, top_y + dy, 0]
            for dx, dy in [
                (-0.30, 0.30), (0.30, 0.30), (0.60, 0.0),
                (0.30, -0.30), (-0.30, -0.30), (-0.60, 0.0),
                (0.0, 0.50), (0.0, -0.50),
            ]
        ]
        self.play(
            LaggedStart(
                *[pile[i].animate.move_to(pile_targets[i])
                  for i in range(len(pile))],
                lag_ratio=0.15, run_time=1.20,
            )
        )

        # 3. GREEN flow arrow grows upward
        flow = make_flow_arrow(pts)
        self.play(GrowArrow(flow), run_time=0.60)

        # 4. Star brightens (fill_opacity 0.18 → 0.75) — single animate property only
        self.play(
            star.animate.set_fill(BLUE, opacity=0.75),
            run_time=0.45,
        )
        self.wait(0.80)

class STD_B01_claude_liam_differentiati(Scene):
    """SHOW-DONT-TELL retrofit for B01 in claude-liam-differentiation-block.
    Narration: 'Normal blood cells mature through a series of stages — an ascending staircase fr'
    Duration: 16.6s  Lines: 5  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Differentiation Block"
        body_lines = ["Normal blood cells mature through a series of", "stages \u2014 an ascending staircase from stem\u2026", "AML freezes that process", "Cells are stuck at an early rung, pile up, and", "can't mature"]
        spark_str = "This plate shows that stall and what it looks like when diff"

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

        reveal_t = max(0.30, 3.15)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B02_claude_liam_differentiati(Scene):
    """SHOW-DONT-TELL retrofit for B02 in claude-liam-differentiation-block.
    Narration: "ATRA in AML is the classic case. It doesn't kill the cells — it releases the blo"
    Duration: 13.9s  Lines: 4  font_sz: 34
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Differentiation Block"
        body_lines = ["ATRA in AML is the classic case", "It doesn't kill the cells \u2014 it releases the block", "The cells that were piling up below the bar", "resume climbing the staircase and mature into\u2026"]
        spark_str = "The plate's two panels are the before and after"

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

        reveal_t = max(0.30, 3.28)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B08_claude_liam_differentiati(Scene):
    """SHOW-DONT-TELL retrofit for B08 in claude-liam-differentiation-block.
    Narration: 'Release, not kill. The animation made the therapeutic action concrete: the pile '
    Duration: 10.4s  Lines: 4  font_sz: 34
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Differentiation Block"
        body_lines = ["Release, not kill", "The animation made the therapeutic action", "concrete: the pile was there because of", "the\u2026"]
        spark_str = "Remove the bar, the pile resolves"

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

        reveal_t = max(0.30, 2.41)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

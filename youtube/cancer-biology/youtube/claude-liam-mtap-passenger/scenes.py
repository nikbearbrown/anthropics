from manim import *

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette (matches plates_gen.py)
SKY    = "#56B4E9"
BLUE   = "#0072B2"
GREEN  = "#009E73"
VERM   = "#D55E00"
ORANGE = "#E69F00"
GRAY   = "#7c7c7c"
INK    = "#333333"

# ─────────────────────────────────────────────────────────────────
# Shared geometry helpers
#   Frame ≈ 14 wide × 8 tall (Manim default at 1920×1080 / 16:9)
#   Chromosome bar: y = 2.5, x = -6 .. +6
#   Tick positions (5 evenly spaced across the bar):
#       x = -4.8, -2.4, 0.0, 2.4, 4.8
#   Ticks 1 and 2 (0-indexed) are the DELETED region (between x=-2.4 and x=2.4)
#   Driver (BLUE square)      → bar x=-0.8, falls to y=1.0
#   Passenger (ORANGE circle) → bar x=+0.8, falls to y=1.0
#   Accumulation node (SKY)   → x=0.8,  y=-0.5
#   VERM plug (Triangle)      → x=3.5,  y=-0.5  pointing left
# ─────────────────────────────────────────────────────────────────

BAR_Y        = 2.5
BAR_LEFT     = -6.0
BAR_RIGHT    =  6.0
TICK_XS      = [-4.8, -2.4, 0.0, 2.4, 4.8]
ALIVE_TICKS  = [0, 3, 4]   # indices of surviving ticks (skip 1 and 2)

DRIVER_X     = -0.8
PASSENGER_X  =  0.8
SHAPE_BAR_Y  = BAR_Y         # starting y (on the bar)
SHAPE_LOW_Y  = 1.0           # y after deletion fall

NODE_X       = 0.8
NODE_Y       = -0.5
NODE_R       = 0.7

PLUG_X       = 3.5
PLUG_Y       = -0.5


def make_bar():
    return RoundedRectangle(
        width=BAR_RIGHT - BAR_LEFT,
        height=0.45,
        corner_radius=0.10,
        color=GRAY,
        fill_color=GRAY,
        fill_opacity=0.55,
        stroke_width=0,
    ).move_to([0, BAR_Y, 0])


def make_ticks():
    ticks = VGroup()
    for i in ALIVE_TICKS:
        x = TICK_XS[i]
        t = Line(
            start=[x, BAR_Y + 0.23, 0],
            end=[x, BAR_Y - 0.23, 0],
            color=INK,
            stroke_width=3,
        )
        ticks.add(t)
    return ticks


def make_bracket():
    """Vermillion arc above the deleted segment (ticks 1 and 2 → x=-2.4 to x=2.4)."""
    return ArcBetweenPoints(
        start=[-2.4, BAR_Y + 0.23, 0],
        end=[2.4, BAR_Y + 0.23, 0],
        angle=-PI / 3,
        color=VERM,
        stroke_width=3,
    )


def make_driver():
    return Square(
        side_length=0.7,
        color=BLUE,
        fill_color=BLUE,
        fill_opacity=0.20,
        stroke_width=3,
    ).move_to([DRIVER_X, SHAPE_BAR_Y, 0])


def make_passenger():
    return Circle(
        radius=0.4,
        color=ORANGE,
        fill_color=ORANGE,
        fill_opacity=0.20,
        stroke_width=3,
    ).move_to([PASSENGER_X, SHAPE_BAR_Y, 0])


def make_dashed_lines(driver, passenger):
    """DashedLines from bar surface down to each shape's top after they fall."""
    d_line = DashedLine(
        start=[DRIVER_X, BAR_Y - 0.23, 0],
        end=[DRIVER_X, SHAPE_LOW_Y + 0.35, 0],
        color=GRAY,
        dash_length=0.10,
        dashed_ratio=0.6,
        stroke_width=2,
    )
    p_line = DashedLine(
        start=[PASSENGER_X, BAR_Y - 0.23, 0],
        end=[PASSENGER_X, SHAPE_LOW_Y + 0.40, 0],
        color=GRAY,
        dash_length=0.10,
        dashed_ratio=0.6,
        stroke_width=2,
    )
    return d_line, p_line


def make_accumulation_node():
    node = Circle(
        radius=NODE_R,
        color=SKY,
        fill_color=SKY,
        fill_opacity=0.18,
        stroke_width=3,
    ).move_to([NODE_X, NODE_Y, 0])
    dots = VGroup()
    offsets = [
        [0.0,  0.25, 0],
        [-0.25, 0.0, 0],
        [0.25,  0.0, 0],
        [-0.15,-0.22, 0],
        [0.15, -0.22, 0],
    ]
    for dx, dy, dz in offsets:
        d = Dot(
            point=[NODE_X + dx, NODE_Y + dy, 0],
            radius=0.10,
            color=SKY,
            fill_opacity=1.0,
        )
        dots.add(d)
    return node, dots


def make_plug_and_arrow():
    """VERM triangle pointing left + Arrow toward accumulation node."""
    plug = Triangle(color=VERM, fill_color=VERM, fill_opacity=0.8, stroke_width=0)
    plug.scale(0.35).rotate(PI / 6)   # point left
    plug.move_to([PLUG_X, PLUG_Y, 0])

    arrow = Arrow(
        start=[PLUG_X - 0.35, PLUG_Y, 0],
        end=[NODE_X + NODE_R + 0.12, NODE_Y, 0],
        buff=0.08,
        color=VERM,
        stroke_width=3,
        max_tip_length_to_length_ratio=0.15,
    )
    return plug, arrow


def make_passenger_arrow(passenger_final_pos):
    """Arrow from bottom of passenger circle down to top of accumulation node."""
    return Arrow(
        start=[PASSENGER_X, SHAPE_LOW_Y - 0.40, 0],
        end=[NODE_X, NODE_Y + NODE_R + 0.10, 0],
        buff=0.08,
        color=GRAY,
        stroke_width=3,
        max_tip_length_to_length_ratio=0.15,
    )


# ============================================================
# B05_MtapPassenger — initial animation
#   1. Bar + surviving ticks (LaggedStart)
#   2. VERM bracket above gap
#   3. Driver + Passenger fade in at bar, then fall below (deletion)
#   4. DashedLines from bar down to shapes
#   5. Arrow from Passenger down to accumulation node
#   6. SKY accumulation circle + 5 dots (LaggedStart)
#   7. VERM plug + arrow FadeIn from right
# ============================================================
class B05_MtapPassenger(Scene):
    def construct(self):
        bar    = make_bar()
        ticks  = make_ticks()
        bracket = make_bracket()
        driver   = make_driver()
        passenger = make_passenger()
        node, dots = make_accumulation_node()
        plug, plug_arrow = make_plug_and_arrow()
        pass_arrow = make_passenger_arrow(SHAPE_LOW_Y)
        d_line, p_line = make_dashed_lines(driver, passenger)

        # 1. Chromosome bar + surviving ticks
        self.play(
            LaggedStart(
                Create(bar),
                LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.25, run_time=0.6),
                lag_ratio=0.4,
                run_time=0.9,
            )
        )
        self.wait(0.15)

        # 2. VERM deletion bracket above the gap
        self.play(Create(bracket), run_time=0.55)
        self.wait(0.15)

        # 3. Driver and passenger appear at bar level
        self.play(FadeIn(driver), FadeIn(passenger), run_time=0.4)
        self.wait(0.10)

        # 4. Shapes fall below bar (deletion)
        self.play(
            driver.animate.move_to([DRIVER_X, SHAPE_LOW_Y, 0]),
            passenger.animate.move_to([PASSENGER_X, SHAPE_LOW_Y, 0]),
            run_time=0.7,
        )

        # 5. DashedLines from bar down to shapes
        self.play(
            Create(d_line),
            Create(p_line),
            run_time=0.45,
        )
        self.wait(0.10)

        # 6. Arrow from passenger circle to accumulation node
        self.play(GrowArrow(pass_arrow), run_time=0.55)

        # 7. SKY accumulation node circle + 5 dots appear one by one
        self.play(FadeIn(node), run_time=0.4)
        self.play(
            LaggedStart(
                *[FadeIn(d, scale=0.5) for d in dots],
                lag_ratio=0.22,
                run_time=0.9,
            )
        )
        self.wait(0.15)

        # 8. VERM plug and arrow FadeIn from the right
        self.play(
            FadeIn(plug_arrow),
            FadeIn(plug),
            run_time=0.55,
        )
        self.wait(0.9)


# ============================================================
# B07_MtapPassengerFlow — deletion + causal flow animation
#   Same deletion build as B05, then:
#   a. ORANGE passenger pulses (Flash)
#   b. 5 dots animate flowing one-by-one into accumulation node (LaggedStart)
#   c. VERM plug moves along arrow path toward node
#   d. SKY Flash on accumulation node as plug arrives
# ============================================================
class B07_MtapPassengerFlow(Scene):
    def construct(self):
        # ── rebuild deletion (same as B05) ──────────────────────
        bar       = make_bar()
        ticks     = make_ticks()
        bracket   = make_bracket()
        driver    = make_driver()
        passenger = make_passenger()
        node, dots = make_accumulation_node()
        plug, plug_arrow = make_plug_and_arrow()
        pass_arrow = make_passenger_arrow(SHAPE_LOW_Y)
        d_line, p_line = make_dashed_lines(driver, passenger)

        # Bar + ticks
        self.play(
            LaggedStart(
                Create(bar),
                LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.25, run_time=0.5),
                lag_ratio=0.4,
                run_time=0.8,
            )
        )

        # Bracket
        self.play(Create(bracket), run_time=0.45)

        # Shapes appear at bar
        self.play(FadeIn(driver), FadeIn(passenger), run_time=0.35)

        # Deletion fall
        self.play(
            driver.animate.move_to([DRIVER_X, SHAPE_LOW_Y, 0]),
            passenger.animate.move_to([PASSENGER_X, SHAPE_LOW_Y, 0]),
            run_time=0.6,
        )

        # Dashed lines
        self.play(Create(d_line), Create(p_line), run_time=0.4)

        # Passenger arrow
        self.play(GrowArrow(pass_arrow), run_time=0.5)

        # Node (empty first — dots will flow in)
        self.play(FadeIn(node), run_time=0.35)
        self.wait(0.15)

        # ── causal flow ─────────────────────────────────────────

        # a. ORANGE passenger pulses — this is the vulnerable node
        self.play(
            Flash(
                passenger.get_center(),
                color=ORANGE,
                line_length=0.35,
                num_lines=12,
                flash_radius=0.65,
            ),
            run_time=0.55,
        )
        self.wait(0.15)

        # b. 5 dots flow one-by-one from above the node (source) down into it
        #    Each dot starts just above the node entry (top of pass_arrow end)
        source_pt = [PASSENGER_X, SHAPE_LOW_Y - 0.40, 0]
        dot_targets = [
            [NODE_X + 0.0,  NODE_Y + 0.25, 0],
            [NODE_X - 0.25, NODE_Y + 0.0,  0],
            [NODE_X + 0.25, NODE_Y + 0.0,  0],
            [NODE_X - 0.15, NODE_Y - 0.22, 0],
            [NODE_X + 0.15, NODE_Y - 0.22, 0],
        ]
        flow_dots = VGroup(*[
            Dot(point=source_pt, radius=0.10, color=SKY, fill_opacity=0.9)
            for _ in dot_targets
        ])
        self.add(flow_dots)

        anims = []
        for fd, target in zip(flow_dots, dot_targets):
            anims.append(fd.animate.move_to(target))

        self.play(
            LaggedStart(*anims, lag_ratio=0.28, run_time=1.4)
        )
        self.wait(0.15)

        # c. VERM plug moves along its arrow path toward the node
        #    Plug moves from [PLUG_X, PLUG_Y] left to near the node edge
        plug_start = [PLUG_X, PLUG_Y, 0]
        plug_end   = [NODE_X + NODE_R + 0.22, NODE_Y, 0]
        self.play(FadeIn(plug_arrow), run_time=0.3)
        self.play(plug.animate.move_to(plug_end), run_time=0.65)

        # d. SKY Flash on accumulation node as plug arrives
        self.play(
            Flash(
                node.get_center(),
                color=SKY,
                line_length=0.40,
                num_lines=14,
                flash_radius=0.90,
            ),
            run_time=0.55,
        )
        self.wait(0.9)

class STD_B01_claude_liam_mtap_passenge(Scene):
    """SHOW-DONT-TELL retrofit for B01 in claude-liam-mtap-passenger.
    Narration: "Chromosomal deletions don't always remove just the target gene. When a driver ge"
    Duration: 17.9s  Lines: 6  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "MTAP Passenger"
        body_lines = ["Chromosomal deletions don't always remove just", "the target gene", "When a driver gene is cut, neighboring genes get", "deleted too \u2014 passengers", "MTAP sits next to CDKN2A, one of the most", "frequently deleted tumor suppressors"]
        spark_str = "Lose CDKN2A, and MTAP goes with it in roughly half of all hu"

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

        reveal_t = max(0.30, 2.86)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B02_claude_liam_mtap_passenge(Scene):
    """SHOW-DONT-TELL retrofit for B02 in claude-liam-mtap-passenger.
    Narration: 'MTAP loss creates a metabolic dependency. Without MTAP, a metabolite accumulates'
    Duration: 18.1s  Lines: 5  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "MTAP Passenger"
        body_lines = ["MTAP loss creates a metabolic dependency", "Without MTAP, a metabolite accumulates and cells", "become hyperdependent on PRMT5", "Inhibit PRMT5 \u2014 an enzyme tumor cells need,", "normal cells don't \u2014 and MTAP-deleted cells\u2026"]
        spark_str = "The deletion that was an accident becomes the vulnerability"

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

        reveal_t = max(0.30, 3.46)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B08_claude_liam_mtap_passenge(Scene):
    """SHOW-DONT-TELL retrofit for B08 in claude-liam-mtap-passenger.
    Narration: 'The passenger opened the door. Chromosome deletion — passenger lost — metabolite'
    Duration: 10.7s  Lines: 4  font_sz: 34
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "MTAP Passenger"
        body_lines = ["The passenger opened the door", "Chromosome deletion \u2014 passenger lost \u2014", "metabolite accumulates \u2014 drugable", "dependency\u2026"]
        spark_str = "A therapeutic target born from collateral damage"

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

        reveal_t = max(0.30, 2.47)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

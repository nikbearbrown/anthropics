from manim import *

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette
SKY    = "#56B4E9"
BLUE   = "#0072B2"
GREEN  = "#009E73"
VERM   = "#D55E00"
ORANGE = "#E69F00"
GRAY   = "#7c7c7c"


def _xmark(x, y, size=0.22):
    """Return a VGroup X-mark at (x, y)."""
    return VGroup(
        Line([x - size, y - size, 0], [x + size, y + size, 0],
             color=VERM, stroke_width=6),
        Line([x - size, y + size, 0], [x + size, y - size, 0],
             color=VERM, stroke_width=6),
    )


def _broken_node(x, y):
    """ORANGE jagged polygon representing a broken/shattered survival node."""
    # Irregular polygon at (x, y) — simulates a shattered circle
    pts = [
        [x - 0.38, y - 0.10, 0],
        [x - 0.18, y + 0.38, 0],
        [x + 0.08, y + 0.15, 0],
        [x + 0.32, y + 0.35, 0],
        [x + 0.40, y + 0.02, 0],
        [x + 0.22, y - 0.20, 0],
        [x + 0.38, y - 0.35, 0],
        [x + 0.05, y - 0.38, 0],
        [x - 0.22, y - 0.32, 0],
    ]
    return Polygon(*pts,
                   color=ORANGE, fill_color=ORANGE,
                   fill_opacity=0.50, stroke_width=2.5)


def _route_vmobject(start_xy, bend_xy, end_xy, color=GRAY):
    """Three-point bent route as a VMobject polyline."""
    m = VMobject(stroke_color=color, stroke_width=3.2, stroke_opacity=0.9)
    m.set_points_as_corners([
        [start_xy[0], start_xy[1], 0],
        [bend_xy[0],  bend_xy[1],  0],
        [end_xy[0],   end_xy[1],   0],
    ])
    return m


def _build_panel_objects(cy, both_cut):
    """
    Return a dict of mobjects for one panel.
    cy      — y-centre of the panel
    both_cut — True means both routes cut (bottom panel)
    """
    route_bend_x = -0.20   # x where routes change direction
    start_x = -5.0
    surv_x  =  4.5
    bend_y_up =  cy + 1.35
    bend_y_lo =  cy - 1.35

    start_circle = Circle(
        radius=0.32, color=GRAY, fill_color=GRAY, fill_opacity=0.38,
        stroke_width=2.5,
    ).move_to([start_x, cy, 0])

    # Route polylines: start → bend → survival
    up_route = _route_vmobject(
        [start_x, cy],
        [route_bend_x, bend_y_up],
        [surv_x, cy],
    )
    lo_route = _route_vmobject(
        [start_x, cy],
        [route_bend_x, bend_y_lo],
        [surv_x, cy],
    )

    # X-mark always on upper route
    xmark_up = _xmark(route_bend_x, bend_y_up)

    if both_cut:
        xmark_lo = _xmark(route_bend_x, bend_y_lo)
        surv_node = _broken_node(surv_x, cy)
        return {
            "start": start_circle,
            "up":    up_route,
            "lo":    lo_route,
            "xm_up": xmark_up,
            "xm_lo": xmark_lo,
            "surv":  surv_node,
        }
    else:
        surv_node = Circle(
            radius=0.40, color=GREEN, fill_color=GREEN,
            fill_opacity=0.30, stroke_width=3.0,
        ).move_to([surv_x, cy, 0])
        return {
            "start": start_circle,
            "up":    up_route,
            "lo":    lo_route,
            "xm_up": xmark_up,
            "surv":  surv_node,
        }


# ============================================================
# B05_SyntheticLethality — initial animation
#   separator → top panel (one cut, GREEN) → bottom panel (both cuts, ORANGE)
# ============================================================
class B05_SyntheticLethality(Scene):
    def construct(self):
        # Separator line
        sep = Line([-6.8, 0, 0], [6.8, 0, 0],
                   color=GRAY, stroke_width=1.8, stroke_opacity=0.60)
        self.play(Create(sep), run_time=0.5)

        # --- Top panel (one cut, survival intact) ---
        top = _build_panel_objects(cy=1.75, both_cut=False)
        self.play(FadeIn(top["start"]), run_time=0.4)
        self.play(
            Create(top["up"]),
            Create(top["lo"]),
            run_time=0.8,
        )
        self.play(FadeIn(top["xm_up"]), run_time=0.4)
        self.play(
            FadeIn(top["surv"]),
            Flash(
                top["surv"].get_center(),
                color=GREEN, line_length=0.28,
                num_lines=8, flash_radius=0.60,
            ),
            run_time=0.6,
        )

        self.wait(0.35)

        # --- Bottom panel (both cuts, broken node) ---
        bot = _build_panel_objects(cy=-1.75, both_cut=True)
        self.play(FadeIn(bot["start"]), run_time=0.4)
        self.play(
            Create(bot["up"]),
            Create(bot["lo"]),
            run_time=0.8,
        )
        self.play(
            FadeIn(bot["xm_up"]),
            run_time=0.4,
        )
        self.play(
            FadeIn(bot["xm_lo"]),
            run_time=0.4,
        )
        self.play(FadeIn(bot["surv"]), run_time=0.5)

        self.wait(0.8)


# ============================================================
# B07_SyntheticLethalityBreak — revised
#   top panel builds → second X-mark fires with large Flash
#   → GREEN node shatters (ReplacementTransform) → Wiggle
# ============================================================
class B07_SyntheticLethalityBreak(Scene):
    def construct(self):
        # Separator
        sep = Line([-6.8, 0, 0], [6.8, 0, 0],
                   color=GRAY, stroke_width=1.8, stroke_opacity=0.60)
        self.play(Create(sep), run_time=0.4)

        CY_TOP = 1.75
        CY_BOT = -1.75
        ROUTE_BEND_X = -0.20
        START_X      = -5.0
        SURV_X       =  4.5
        BEND_Y_UP_TOP =  CY_TOP + 1.35
        BEND_Y_LO_TOP =  CY_TOP - 1.35
        BEND_Y_UP_BOT =  CY_BOT + 1.35
        BEND_Y_LO_BOT =  CY_BOT - 1.35

        # --- 1. Top panel — one cut, survival intact ---
        top_start = Circle(
            radius=0.32, color=GRAY, fill_color=GRAY, fill_opacity=0.38,
            stroke_width=2.5,
        ).move_to([START_X, CY_TOP, 0])
        top_up = _route_vmobject([START_X, CY_TOP], [ROUTE_BEND_X, BEND_Y_UP_TOP], [SURV_X, CY_TOP])
        top_lo = _route_vmobject([START_X, CY_TOP], [ROUTE_BEND_X, BEND_Y_LO_TOP], [SURV_X, CY_TOP])
        top_xm = _xmark(ROUTE_BEND_X, BEND_Y_UP_TOP)
        top_surv = Circle(
            radius=0.40, color=GREEN, fill_color=GREEN,
            fill_opacity=0.30, stroke_width=3.0,
        ).move_to([SURV_X, CY_TOP, 0])

        self.play(FadeIn(top_start), run_time=0.35)
        self.play(Create(top_up), Create(top_lo), run_time=0.7)
        self.play(FadeIn(top_xm), run_time=0.35)
        self.play(
            FadeIn(top_surv),
            Flash(top_surv.get_center(), color=GREEN,
                  line_length=0.25, num_lines=8, flash_radius=0.55),
            run_time=0.55,
        )
        self.wait(0.4)

        # --- 2. Bottom panel starts building ---
        bot_start = Circle(
            radius=0.32, color=GRAY, fill_color=GRAY, fill_opacity=0.38,
            stroke_width=2.5,
        ).move_to([START_X, CY_BOT, 0])
        bot_up = _route_vmobject([START_X, CY_BOT], [ROUTE_BEND_X, BEND_Y_UP_BOT], [SURV_X, CY_BOT])
        bot_lo = _route_vmobject([START_X, CY_BOT], [ROUTE_BEND_X, BEND_Y_LO_BOT], [SURV_X, CY_BOT])
        bot_xm_up = _xmark(ROUTE_BEND_X, BEND_Y_UP_BOT)

        self.play(FadeIn(bot_start), run_time=0.35)
        self.play(Create(bot_up), Create(bot_lo), run_time=0.7)
        self.play(FadeIn(bot_xm_up), run_time=0.35)

        # GREEN node appears — as if it might survive
        bot_surv_green = Circle(
            radius=0.40, color=GREEN, fill_color=GREEN,
            fill_opacity=0.30, stroke_width=3.0,
        ).move_to([SURV_X, CY_BOT, 0])
        self.play(FadeIn(bot_surv_green, scale=0.6), run_time=0.40)

        # --- 3. Second X-mark fires with large VERM Flash — the lethal event ---
        bot_xm_lo = _xmark(ROUTE_BEND_X, BEND_Y_LO_BOT, size=0.26)
        self.play(
            FadeIn(bot_xm_lo),
            Flash(
                [ROUTE_BEND_X, BEND_Y_LO_BOT, 0],
                color=VERM,
                line_length=0.50,
                num_lines=12,
                flash_radius=1.00,
            ),
            run_time=0.65,
        )

        # --- 4. GREEN node shatters → ORANGE broken polygon ---
        bot_surv_broken = _broken_node(SURV_X, CY_BOT)
        self.play(
            ReplacementTransform(bot_surv_green, bot_surv_broken),
            run_time=0.55,
        )

        # --- 5. Wiggle on broken node to punch lethality ---
        self.play(
            Wiggle(
                bot_surv_broken,
                scale_value=1.18,
                rotation_angle=0.04 * TAU,
                n_wiggles=3,
                run_time=0.65,
            )
        )
        self.wait(0.8)

class STD_B01_claude_liam_synthetic_let(Scene):
    """SHOW-DONT-TELL retrofit for B01 in claude-liam-synthetic-lethality.
    Narration: 'Synthetic lethality: two genes, each dispensable alone, lethal when both are los'
    Duration: 15.1s  Lines: 6  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Synthetic Lethality"
        body_lines = ["Synthetic lethality: two genes, each dispensable", "alone, lethal when both are lost together", "This plate shows the mechanism in two panels \u2014", "two routes, two possible states", "With one route cut, the other still reaches the", "survival node"]
        spark_str = "With both cut, nothing gets through"

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

        reveal_t = max(0.30, 2.38)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B02_claude_liam_synthetic_let(Scene):
    """SHOW-DONT-TELL retrofit for B02 in claude-liam-synthetic-lethality.
    Narration: 'BRCA-mutated tumors use backup DNA repair because their primary repair pathway i'
    Duration: 18.4s  Lines: 5  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Synthetic Lethality"
        body_lines = ["BRCA-mutated tumors use backup DNA repair because", "their primary repair pathway is already\u2026", "PARP inhibitors cut the backup", "The tumor had one route already severed \u2014 adding", "the second cut is synthetic lethality in\u2026"]
        spark_str = "Normal cells with intact BRCA survive; BRCA-mutant tumor cel"

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

        reveal_t = max(0.30, 3.53)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B08_claude_liam_synthetic_let(Scene):
    """SHOW-DONT-TELL retrofit for B08 in claude-liam-synthetic-lethality.
    Narration: "Redundancy is safety until it isn't. The motion made the geometry physical: one "
    Duration: 21.2s  Lines: 5  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Synthetic Lethality"
        body_lines = ["Redundancy is safety until it isn't", "The motion made the geometry physical: one cut", "survives because the other route\u2026", "Both cut and there's nowhere to go", "The second X-mark is the drug"]
        spark_str = "Strip that and you can animate any synthetic lethality pair"

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

        reveal_t = max(0.30, 4.09)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

from manim import *
import numpy as np

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette
BLUE   = "#0072B2"
ORANGE = "#E69F00"
GREEN  = "#009E73"
VERM   = "#D55E00"
SKY    = "#56B4E9"
GRAY   = "#7c7c7c"

# Layout constants
HEX_X = -5.5
U_Y   =  1.5   # upper track y
L_Y   = -1.5   # lower track y
NODE_XS = [-3.2, -1.0, 1.2]   # 3 nodes per track
END_X   = 3.0                  # x for end-state cluster


def make_hex():
    return (RegularPolygon(n=6, color=BLUE, fill_color=BLUE,
                           fill_opacity=0.18, stroke_width=4.0)
            .scale(0.68)
            .move_to([HEX_X, 0, 0]))


def make_upper_nodes():
    return VGroup(*[
        RoundedRectangle(width=1.05, height=0.68, corner_radius=0.13,
                         color=VERM, fill_color=VERM, fill_opacity=0.16,
                         stroke_width=3.2)
        .move_to([x, U_Y, 0])
        for x in NODE_XS
    ])


def make_lower_nodes():
    return VGroup(*[
        RoundedRectangle(width=1.05, height=0.68, corner_radius=0.13,
                         color=GREEN, fill_color=GREEN, fill_opacity=0.16,
                         stroke_width=3.2)
        .move_to([x, L_Y, 0])
        for x in NODE_XS
    ])


def make_track_arrows(nodes, start_x, start_y, track_y, end_x):
    """Arrows along a track: from hex, between nodes, to end."""
    arrows = VGroup()
    # hex → first node
    arrows.add(Arrow([start_x + 0.5, start_y, 0], [NODE_XS[0] - 0.54, track_y, 0],
                     buff=0, color=GRAY, stroke_width=2.5,
                     max_tip_length_to_length_ratio=0.16))
    # node → node
    for i in range(len(NODE_XS) - 1):
        arrows.add(Arrow([NODE_XS[i] + 0.54, track_y, 0],
                         [NODE_XS[i + 1] - 0.54, track_y, 0],
                         buff=0, color=GRAY, stroke_width=2.5,
                         max_tip_length_to_length_ratio=0.16))
    # last node → end
    arrows.add(Arrow([NODE_XS[-1] + 0.54, track_y, 0],
                     [end_x - 0.72, track_y, 0],
                     buff=0, color=GRAY, stroke_width=2.5,
                     max_tip_length_to_length_ratio=0.16))
    return arrows


def make_atp_large():
    """Large ATP square = full oxidation, 30 ATP."""
    return (Square(side_length=1.35, color=ORANGE,
                   fill_color=ORANGE, fill_opacity=0.72)
            .move_to([END_X + 0.6, U_Y, 0]))


def make_atp_small():
    """Small ATP square = glycolysis, 2 ATP."""
    return (Square(side_length=0.55, color=ORANGE,
                   fill_color=ORANGE, fill_opacity=0.72)
            .move_to([END_X + 1.55, L_Y, 0]))


def make_building_blocks():
    """Triangle + rectangle + rod in SKY — building material."""
    tri = Triangle(color=SKY, fill_color=SKY, fill_opacity=0.7,
                   stroke_width=2).scale(0.38).move_to([END_X + 0.1, L_Y - 0.1, 0])
    rec = Rectangle(width=0.5, height=0.3, color=SKY,
                    fill_color=SKY, fill_opacity=0.7,
                    stroke_width=2).move_to([END_X + 0.65, L_Y + 0.12, 0])
    rod = Line([END_X + 1.02, L_Y + 0.02, 0],
               [END_X + 1.02, L_Y - 0.32, 0],
               color=SKY, stroke_width=8)
    return VGroup(tri, rec, rod)


def make_excreted_circle():
    """One excreted lactate circle to the right (VERM)."""
    return Circle(radius=0.22, color=VERM, fill_color=VERM,
                  fill_opacity=0.55, stroke_width=2.5).move_to([END_X + 2.0, L_Y, 0])


# ============================================================
# B05_WarburgCarbon — initial animation
#   Hexagon → upper track → lower track → end-states → Flash hex
# ============================================================
class B05_WarburgCarbon(Scene):
    def construct(self):
        hx = make_hex()
        u_nodes = make_upper_nodes()
        l_nodes = make_lower_nodes()
        u_arrows = make_track_arrows(u_nodes, HEX_X, 0, U_Y, END_X)
        l_arrows = make_track_arrows(l_nodes, HEX_X, 0, L_Y, END_X)
        atp_lg = make_atp_large()
        atp_sm = make_atp_small()
        blocks = make_building_blocks()
        excreted = make_excreted_circle()

        # 1. Reveal hexagon
        self.play(FadeIn(hx, scale=0.9), run_time=0.5)

        # 2. Branch — upper track
        self.play(
            LaggedStart(
                *[FadeIn(n, shift=RIGHT * 0.2) for n in u_nodes],
                lag_ratio=0.20, run_time=1.0,
            )
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in u_arrows],
                        lag_ratio=0.15, run_time=0.8),
        )

        # 3. Branch — lower track
        self.play(
            LaggedStart(
                *[FadeIn(n, shift=RIGHT * 0.2) for n in l_nodes],
                lag_ratio=0.20, run_time=1.0,
            )
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in l_arrows],
                        lag_ratio=0.15, run_time=0.8),
        )

        # 4. Reveal end-states
        self.play(
            FadeIn(atp_lg, scale=1.1),
            FadeIn(blocks),
            FadeIn(atp_sm),
            FadeIn(excreted),
            run_time=0.7,
        )

        # 5. Flash hexagon — shows shared origin
        self.play(
            Flash(hx.get_center(), color=ORANGE,
                  line_length=0.30, num_lines=14, flash_radius=0.92),
            run_time=0.5,
        )
        self.wait(0.8)


# ============================================================
# B07_WarburgCarbonFlow — revision: flow particles + scale grow + Flash contrast
#   ORANGE dot particles flow along each track, large ATP grows,
#   building blocks assemble one-by-one, then both ATP squares Flash
# ============================================================
class B07_WarburgCarbonFlow(Scene):
    def construct(self):
        hx = make_hex()
        u_nodes = make_upper_nodes()
        l_nodes = make_lower_nodes()
        u_arrows = make_track_arrows(u_nodes, HEX_X, 0, U_Y, END_X)
        l_arrows = make_track_arrows(l_nodes, HEX_X, 0, L_Y, END_X)
        atp_lg = make_atp_large()
        atp_sm = make_atp_small()
        tri = Triangle(color=SKY, fill_color=SKY, fill_opacity=0.7,
                       stroke_width=2).scale(0.38).move_to([END_X + 0.1, L_Y - 0.1, 0])
        rec = Rectangle(width=0.5, height=0.3, color=SKY,
                        fill_color=SKY, fill_opacity=0.7,
                        stroke_width=2).move_to([END_X + 0.65, L_Y + 0.12, 0])
        rod = Line([END_X + 1.02, L_Y + 0.02, 0],
                   [END_X + 1.02, L_Y - 0.32, 0],
                   color=SKY, stroke_width=8)
        excreted = make_excreted_circle()

        # 1. Reveal hexagon + nodes + arrows (same as B05 setup)
        self.play(FadeIn(hx, scale=0.9), run_time=0.45)
        self.play(
            LaggedStart(*[FadeIn(n, shift=RIGHT * 0.2) for n in u_nodes],
                        lag_ratio=0.18, run_time=0.9),
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in u_arrows],
                        lag_ratio=0.12, run_time=0.7),
        )
        self.play(
            LaggedStart(*[FadeIn(n, shift=RIGHT * 0.2) for n in l_nodes],
                        lag_ratio=0.18, run_time=0.9),
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in l_arrows],
                        lag_ratio=0.12, run_time=0.7),
        )

        # 2. Flow particles along upper track
        u_dots = VGroup(*[
            Dot(point=[NODE_XS[0] - 0.3, U_Y, 0],
                radius=0.12, color=ORANGE, fill_opacity=0.85)
            for _ in range(3)
        ])
        self.play(FadeIn(u_dots), run_time=0.2)
        self.play(
            u_dots[0].animate.move_to([END_X + 0.3, U_Y, 0]),
            u_dots[1].animate.move_to([END_X + 0.0, U_Y, 0]),
            u_dots[2].animate.move_to([NODE_XS[2] + 0.5, U_Y, 0]),
            run_time=0.7,
        )

        # 3. Large ATP square grows from small to full (scale from 0.1 to 1.0)
        atp_lg_seed = (Square(side_length=0.14, color=ORANGE,
                               fill_color=ORANGE, fill_opacity=0.72)
                       .move_to([END_X + 0.6, U_Y, 0]))
        self.play(FadeIn(atp_lg_seed), FadeOut(u_dots), run_time=0.2)
        self.play(atp_lg_seed.animate.become(atp_lg), run_time=0.65)

        # 4. Flow particles along lower track
        l_dots = VGroup(*[
            Dot(point=[NODE_XS[0] - 0.3, L_Y, 0],
                radius=0.12, color=ORANGE, fill_opacity=0.85)
            for _ in range(3)
        ])
        self.play(FadeIn(l_dots), run_time=0.2)
        self.play(
            l_dots[0].animate.move_to([END_X - 0.1, L_Y, 0]),
            l_dots[1].animate.move_to([NODE_XS[2] + 0.5, L_Y, 0]),
            l_dots[2].animate.move_to([NODE_XS[2] + 0.0, L_Y, 0]),
            run_time=0.7,
        )

        # 5. Building blocks assemble one at a time
        self.play(FadeIn(tri), FadeOut(l_dots), run_time=0.3)
        self.play(FadeIn(rec), run_time=0.25)
        self.play(FadeIn(rod), run_time=0.25)
        self.play(FadeIn(atp_sm), FadeIn(excreted), run_time=0.4)

        # 6. Flash both ATP squares to show size contrast
        self.play(
            Flash(atp_lg.get_center(), color=ORANGE,
                  line_length=0.30, num_lines=12, flash_radius=0.80),
            Flash(atp_sm.get_center(), color=ORANGE,
                  line_length=0.20, num_lines=10, flash_radius=0.42),
            run_time=0.5,
        )
        self.wait(0.8)

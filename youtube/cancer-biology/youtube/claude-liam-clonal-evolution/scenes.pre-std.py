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

# Branch connections: (start_xy, end_xy) in Manim coords
BRANCHES = [
    ([-5.5, 0], [-3.5,  1.5]),
    ([-5.5, 0], [-3.5, -1.5]),
    ([-3.5,  1.5], [-1.5,  2.5]),
    ([-3.5,  1.5], [-1.5,  0.8]),
    ([-3.5, -1.5], [-1.5, -0.8]),
    ([-3.5, -1.5], [-1.5, -2.5]),
    ([-1.5,  0.8], [ 0.8,  0.8]),
]

# Node positions and types: 0=solid SKY, 1=hollow ORANGE, 2=hatched GREEN
TREE_NODES = [
    ([-3.5,  1.5], 2),
    ([-3.5, -1.5], 0),
    ([-1.5,  2.5], 1),
    ([-1.5,  0.8], 0),
    ([-1.5, -0.8], 2),
    ([-1.5, -2.5], 1),
    ([ 0.8,  0.8], 0),
]

# Dead-end branches: stub lines + X positions
DEAD_ENDS = [
    ([-1.5,  2.5], [ 0.8,  2.5]),   # type 1 stub right
    ([-1.5, -0.8], [ 0.8, -0.8]),   # type 2 stub right
    ([-1.5, -2.5], [ 0.8, -2.5]),   # type 1 stub right
]
X_POSITIONS = [
    [ 0.8,  2.5],
    [ 0.8, -0.8],
    [ 0.8, -2.5],
]


def _node_circle(pos, node_type):
    """Return a Circle mobject for the given subclone type."""
    x, y = pos
    if node_type == 0:
        # Solid SKY
        return Circle(radius=0.28, color=SKY, fill_color=SKY,
                      fill_opacity=0.85, stroke_width=2).move_to([x, y, 0])
    elif node_type == 1:
        # Hollow ORANGE outline
        return Circle(radius=0.28, color=ORANGE, fill_color=WHITE,
                      fill_opacity=1.0, stroke_width=3).move_to([x, y, 0])
    else:
        # Hatched GREEN — simulate with thin inner circle + outer ring
        outer = Circle(radius=0.28, color=GREEN, fill_color=GREEN,
                       fill_opacity=0.20, stroke_width=2.5).move_to([x, y, 0])
        inner = Circle(radius=0.16, color=GREEN, fill_color=GREEN,
                       fill_opacity=0.55, stroke_width=1.5).move_to([x, y, 0])
        return VGroup(outer, inner)


def _xmark(pos, size=0.18):
    """Return a VGroup X-mark at pos."""
    x, y = pos
    return VGroup(
        Line([x - size, y - size, 0], [x + size, y + size, 0],
             color=VERM, stroke_width=5),
        Line([x - size, y + size, 0], [x + size, y - size, 0],
             color=VERM, stroke_width=5),
    )


# ============================================================
# B05_ClonalEvolution — initial animation
#   founder → tree growth → selection arrow → sweep
# ============================================================
class B05_ClonalEvolution(Scene):
    def construct(self):
        # 1. Founder circle
        founder = Circle(radius=0.35, color=GRAY, fill_color=GRAY,
                         fill_opacity=0.55, stroke_width=2.5).move_to([-5.5, 0, 0])
        self.play(FadeIn(founder), run_time=0.5)

        # 2. Tree: lines first, then node circles
        lines = [
            Line([a[0], a[1], 0], [b[0], b[1], 0], color=GRAY, stroke_width=2.2)
            for a, b in BRANCHES
        ]
        # Dead-end stub lines
        dead_lines = [
            Line([a[0], a[1], 0], [b[0], b[1], 0], color=GRAY, stroke_width=2.2)
            for a, b in DEAD_ENDS
        ]
        self.play(
            LaggedStart(*[Create(l) for l in lines + dead_lines],
                        lag_ratio=0.10, run_time=1.5)
        )

        circles = [_node_circle(pos, t) for pos, t in TREE_NODES]
        self.play(
            LaggedStart(*[FadeIn(c, scale=0.85) for c in circles],
                        lag_ratio=0.12, run_time=1.2)
        )

        # 3. X-marks on dead ends (LaggedStart)
        xmarks = [_xmark(pos) for pos in X_POSITIONS]
        self.play(
            LaggedStart(*[FadeIn(x) for x in xmarks],
                        lag_ratio=0.25, run_time=0.8)
        )

        # 4. Selection pressure arrow (VERM, pointing downward near tree mid-point)
        sel_arrow = Arrow(
            start=[0.0, -3.0, 0], end=[0.0, -1.0, 0],
            color=VERM, buff=0.1, stroke_width=4,
            max_tip_length_to_length_ratio=0.18,
        )
        self.play(GrowArrow(sel_arrow), run_time=0.7)

        # 5. Winning lineage: branch from [0.8, 0.8] → cluster of 8 BLUE circles
        win_line = Line([0.8, 0.8, 0], [3.0, 0.8, 0], color=BLUE, stroke_width=3)
        self.play(Create(win_line), run_time=0.5)

        cluster_positions = []
        cols, gap = 4, 0.55
        for row in range(2):
            for col in range(4):
                cluster_positions.append([4.0 + col * gap, 1.1 - row * gap, 0])
        sweep_circles = [
            Circle(radius=0.22, color=BLUE, fill_color=BLUE,
                   fill_opacity=0.85, stroke_width=1.5).move_to(pos)
            for pos in cluster_positions
        ]
        self.play(
            LaggedStart(*[FadeIn(c, scale=0.7) for c in sweep_circles],
                        lag_ratio=0.10, run_time=1.2)
        )
        self.wait(0.8)


# ============================================================
# B07_ClonalEvolutionSweep — revised: Flash X-marks + flowing sweep + repack
# ============================================================
class B07_ClonalEvolutionSweep(Scene):
    def construct(self):
        # 1. Build tree (same structure)
        founder = Circle(radius=0.35, color=GRAY, fill_color=GRAY,
                         fill_opacity=0.55, stroke_width=2.5).move_to([-5.5, 0, 0])
        self.add(founder)

        lines = [
            Line([a[0], a[1], 0], [b[0], b[1], 0], color=GRAY, stroke_width=2.2)
            for a, b in BRANCHES
        ]
        dead_lines = [
            Line([a[0], a[1], 0], [b[0], b[1], 0], color=GRAY, stroke_width=2.2)
            for a, b in DEAD_ENDS
        ]
        self.play(
            LaggedStart(*[Create(l) for l in lines + dead_lines],
                        lag_ratio=0.08, run_time=1.2)
        )

        circles = [_node_circle(pos, t) for pos, t in TREE_NODES]
        self.play(
            LaggedStart(*[FadeIn(c, scale=0.85) for c in circles],
                        lag_ratio=0.10, run_time=1.0)
        )

        # 2. Selection arrow appears
        sel_arrow = Arrow(
            start=[0.0, -3.0, 0], end=[0.0, -1.0, 0],
            color=VERM, buff=0.1, stroke_width=4,
            max_tip_length_to_length_ratio=0.18,
        )
        self.play(GrowArrow(sel_arrow), run_time=0.6)

        # 3. X-marks with Flash — each one punches
        xmarks = [_xmark(pos) for pos in X_POSITIONS]
        for xm, pos in zip(xmarks, X_POSITIONS):
            self.play(
                FadeIn(xm),
                Flash(
                    [pos[0], pos[1], 0],
                    color=VERM,
                    line_length=0.28,
                    num_lines=8,
                    flash_radius=0.55,
                ),
                run_time=0.45,
            )

        # Selection arrow pulse
        self.play(
            Flash(
                sel_arrow.get_center(),
                color=VERM,
                line_length=0.2,
                num_lines=8,
                flash_radius=0.4,
            ),
            run_time=0.4,
        )

        # 4. Winning lineage — circles flow one-at-a-time
        win_line = Line([0.8, 0.8, 0], [3.0, 0.8, 0], color=BLUE, stroke_width=3)
        self.play(Create(win_line), run_time=0.4)

        # Initial spread positions (flow out in a line — keep within ±7.12 x)
        spread_positions = [[3.2 + i * 0.45, 0.8, 0] for i in range(8)]
        # Final repack positions (tight 4×2 cluster)
        repack_positions = []
        cols, gap = 4, 0.52
        for row in range(2):
            for col in range(4):
                repack_positions.append([3.8 + col * gap, 1.1 - row * gap, 0])

        sweep_circles = [
            Circle(radius=0.22, color=BLUE, fill_color=BLUE,
                   fill_opacity=0.85, stroke_width=1.5).move_to(spread_positions[i])
            for i in range(8)
        ]

        # Flow one at a time
        self.play(
            LaggedStart(*[FadeIn(c, shift=RIGHT * 0.3) for c in sweep_circles],
                        lag_ratio=0.12, run_time=1.2)
        )

        # Repack into cluster
        self.play(
            *[c.animate.move_to(repack_positions[i])
              for i, c in enumerate(sweep_circles)],
            run_time=0.8,
        )

        # Flash on the cluster to show dominance
        cluster_center = [3.8 + (cols - 1) * gap / 2, 0.85, 0]
        self.play(
            Flash(cluster_center, color=BLUE,
                  line_length=0.35, num_lines=12, flash_radius=1.1),
            run_time=0.5,
        )
        self.wait(0.8)

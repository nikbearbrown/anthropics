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


def _make_diamond(cx, cy, color=VERM):
    """Small diamond (lesion marker)."""
    return Polygon(
        [cx,       cy + 0.28, 0],
        [cx + 0.28, cy,       0],
        [cx,       cy - 0.28, 0],
        [cx - 0.28, cy,       0],
        color=color, fill_color=color, fill_opacity=0.85, stroke_width=2,
    )


def _make_lollipops(base_x, base_y, n=4, gap=0.42):
    """4 BLUE methylation lollipops (stem + dot)."""
    group = VGroup()
    for k in range(n):
        x = base_x + k * gap
        stem = Line([x, base_y,       0], [x, base_y + 0.35, 0],
                    color=BLUE, stroke_width=2.4)
        dot  = Dot(radius=0.09, color=BLUE).move_to([x, base_y + 0.40, 0])
        group.add(VGroup(stem, dot))
    return group


# ============================================================
# B05_MgmtMethylation — initial animation
#   lesion strand → fork → upper track (enzyme repairs, SKY cell)
#                        → lower track (methylated, lesion persists, ORANGE dead)
# ============================================================
class B05_MgmtMethylation(Scene):
    def construct(self):
        # ── Lesion strand (left of fork) ──
        strand_left = Line([-6.5, 0, 0], [-0.5, 0, 0],
                           color=GRAY, stroke_width=6)
        diamond = _make_diamond(-3.5, 0)
        self.play(FadeIn(strand_left), FadeIn(diamond), run_time=0.5)

        # ── Fork arrows ──
        fork_up = Line([-0.5, 0, 0], [0.5, 1.8, 0],
                        color=GRAY, stroke_width=1.8)
        fork_dn = Line([-0.5, 0, 0], [0.5, -1.8, 0],
                        color=GRAY, stroke_width=1.8)
        self.play(
            GrowFromPoint(fork_up, [-0.5, 0, 0]),
            GrowFromPoint(fork_dn, [-0.5, 0, 0]),
            run_time=0.55,
        )

        # ── Upper track (y = +1.8) ──
        u_left  = Line([0.5, 1.8, 0], [2.5, 1.8, 0],
                        color=GRAY, stroke_width=5)
        enzyme   = Arc(
            radius=0.38, start_angle=PI * 0.18, angle=PI * 1.64,
            color=GREEN, stroke_width=5,
        ).move_to([1.8, 1.8, 0])
        u_right  = Line([3.2, 1.8, 0], [5.0, 1.8, 0],
                         color=GRAY, stroke_width=5)
        intact_cell = Circle(
            radius=0.52, color=SKY,
            fill_color=SKY, fill_opacity=0.28, stroke_width=3,
        ).move_to([5.9, 1.8, 0])

        # ── Lower track (y = -1.8) ──
        promoter = RoundedRectangle(
            width=1.9, height=0.65, corner_radius=0.1,
            color=BLUE, fill_color=BLUE, fill_opacity=0.16, stroke_width=2.6,
        ).move_to([1.45, -1.8, 0])
        lollipops = _make_lollipops(0.65, -1.5, n=4, gap=0.42)
        l_right  = Line([2.5, -1.8, 0], [4.5, -1.8, 0],
                         color=GRAY, stroke_width=5)
        diamond2 = _make_diamond(3.5, -1.8)
        brk = VGroup(
            Line([4.8, -1.55, 0], [5.3, -1.98, 0], color=VERM, stroke_width=4),
            Line([5.1, -1.55, 0], [5.6, -1.98, 0], color=VERM, stroke_width=4),
        )
        dead_cell = Polygon(
            [5.65, -1.30, 0], [6.15, -1.55, 0], [5.95, -1.80, 0],
            [6.30, -2.00, 0], [6.05, -2.05, 0], [5.80, -1.82, 0],
            color=ORANGE, fill_color=ORANGE, fill_opacity=0.50, stroke_width=2.4,
        )

        # ── Animate both tracks simultaneously ──
        self.play(
            FadeIn(u_left),
            Create(enzyme),
            FadeIn(promoter),
            LaggedStart(*[FadeIn(lp) for lp in lollipops], lag_ratio=0.20, run_time=0.9),
        )
        self.wait(0.15)
        # Enzyme moves right (repair), diamond fades; lower strand + lesion appear
        self.play(
            enzyme.animate.move_to([3.2, 1.8, 0]),
            diamond.animate.set_opacity(0.0),
            FadeIn(l_right),
            FadeIn(diamond2),
            run_time=0.85,
        )
        self.play(
            FadeIn(u_right),
            FadeIn(intact_cell, scale=0.85),
            FadeIn(brk),
            run_time=0.55,
        )
        self.play(FadeIn(dead_cell, scale=0.85), run_time=0.45)
        self.wait(0.9)


# ============================================================
# B07_MgmtMethylationFork — revised animation
#   lesion Flash → fork → upper enzyme sweeps (animate position, diamond FadeOut)
#   → lower lollipops grow upward (LaggedStart), diamond pulses, dead cell fragments
# ============================================================
class B07_MgmtMethylationFork(Scene):
    def construct(self):
        # ── Lesion strand ──
        strand_left = Line([-6.5, 0, 0], [-0.5, 0, 0],
                           color=GRAY, stroke_width=6)
        diamond = _make_diamond(-3.5, 0)
        self.play(FadeIn(strand_left), FadeIn(diamond), run_time=0.45)

        # Flash the lesion — emphasis on the damage
        self.play(
            Flash(
                diamond.get_center(), color=VERM,
                line_length=0.30, num_lines=10, flash_radius=0.55,
            ),
            run_time=0.55,
        )

        # ── Fork ──
        fork_up = Line([-0.5, 0, 0], [0.5, 1.8, 0],
                        color=GRAY, stroke_width=1.8)
        fork_dn = Line([-0.5, 0, 0], [0.5, -1.8, 0],
                        color=GRAY, stroke_width=1.8)
        self.play(
            GrowFromPoint(fork_up, [-0.5, 0, 0]),
            GrowFromPoint(fork_dn, [-0.5, 0, 0]),
            run_time=0.55,
        )

        # ── Upper track objects ──
        u_left  = Line([0.5, 1.8, 0], [2.5, 1.8, 0],
                        color=GRAY, stroke_width=5)
        enzyme  = Arc(
            radius=0.38, start_angle=PI * 0.18, angle=PI * 1.64,
            color=GREEN, stroke_width=5,
        ).move_to([1.5, 1.8, 0])
        u_right = Line([3.2, 1.8, 0], [5.0, 1.8, 0],
                        color=GRAY, stroke_width=5)
        intact_cell = Circle(
            radius=0.52, color=SKY,
            fill_color=SKY, fill_opacity=0.28, stroke_width=3,
        ).move_to([5.9, 1.8, 0])

        # ── Lower track objects ──
        promoter = RoundedRectangle(
            width=1.9, height=0.65, corner_radius=0.1,
            color=BLUE, fill_color=BLUE, fill_opacity=0.16, stroke_width=2.6,
        ).move_to([1.45, -1.8, 0])
        # Lollipops: start with dot only, stems grow upward
        lollipop_dots  = VGroup(*[
            Dot(radius=0.09, color=BLUE).move_to([0.65 + k * 0.42, -1.10, 0])
            for k in range(4)
        ])
        lollipop_stems = VGroup(*[
            Line(
                [0.65 + k * 0.42, -1.50, 0],
                [0.65 + k * 0.42, -1.10, 0],
                color=BLUE, stroke_width=2.4,
            ) for k in range(4)
        ])
        l_right  = Line([2.5, -1.8, 0], [4.5, -1.8, 0],
                         color=GRAY, stroke_width=5)
        diamond2 = _make_diamond(3.5, -1.8)
        brk = VGroup(
            Line([4.8, -1.55, 0], [5.3, -1.98, 0], color=VERM, stroke_width=4),
            Line([5.1, -1.55, 0], [5.6, -1.98, 0], color=VERM, stroke_width=4),
        )
        # Dead cell — assembled from fragments (6 triangle-like polygons)
        dead_pts = [
            [5.65, -1.30, 0], [6.15, -1.55, 0], [5.95, -1.80, 0],
            [6.30, -2.00, 0], [6.05, -2.05, 0], [5.80, -1.82, 0],
        ]
        dead_fragments = VGroup(*[
            Polygon(
                dead_pts[i],
                dead_pts[(i + 1) % 6],
                dead_pts[(i + 2) % 6],
                color=ORANGE, fill_color=ORANGE, fill_opacity=0.50, stroke_width=2.4,
            ) for i in range(0, 6, 2)
        ])

        # ── Animate both tracks ──
        self.play(
            FadeIn(u_left),
            FadeIn(promoter),
            FadeIn(lollipop_dots),
            run_time=0.55,
        )
        # Lollipop stems grow upward from dots (LaggedStart)
        self.play(
            LaggedStart(
                *[GrowFromPoint(stem, stem.get_bottom())
                  for stem in lollipop_stems],
                lag_ratio=0.22, run_time=0.75,
            ),
            Create(enzyme),
            run_time=0.85,
        )

        # Enzyme sweeps along upper strand, diamond fades; lower strand + lesion appear
        self.play(
            enzyme.animate.move_to([3.2, 1.8, 0]),
            diamond.animate.set_opacity(0.0),
            FadeIn(l_right),
            FadeIn(diamond2),
            run_time=1.0,
        )

        # Lower lesion pulses (Indicate ×2 — persists)
        self.play(Indicate(diamond2, color=VERM, scale_factor=1.3), run_time=0.45)
        self.play(Indicate(diamond2, color=VERM, scale_factor=1.2), run_time=0.40)

        # Upper track completes; break appears
        self.play(
            FadeIn(u_right),
            FadeIn(intact_cell, scale=0.85),
            FadeIn(brk),
            run_time=0.55,
        )

        # Dead cell assembles from fragments
        self.play(
            LaggedStart(*[FadeIn(f, scale=0.7) for f in dead_fragments],
                        lag_ratio=0.20, run_time=0.65),
        )
        self.wait(0.9)

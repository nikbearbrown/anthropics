from manim import *
import math

# White background — must be set at module level (before Manim reads config)
config.background_color = "#FFFFFF"

# Okabe-Ito palette (matches plates_gen.py)
SKY    = "#56B4E9"
BLUE   = "#0072B2"
GREEN  = "#009E73"
VERM   = "#D55E00"
ORANGE = "#E69F00"
GRAY   = "#7c7c7c"


# ============================================================
# B05_MirDeletion — initial two-state stacked animation
#   TOP STATE (y≈+1.5): mRNA strand (BLUE) + GREEN hairpin arc +
#     downward arrow + block bar + 1 ORANGE dot
#   SEPARATOR: dashed GRAY line at y=0
#   BOTTOM STATE (y≈-1.5): mRNA strand (BLUE) + VERM X-mark +
#     unblocked arrow + 9 ORANGE dots (3×3 cluster)
# ============================================================
class B05_MirDeletion(Scene):
    def construct(self):
        # ── TOP STATE (silenced) ─────────────────────────────────────────
        # mRNA strand: BLUE, from x=-5 to x=+3, y=+1.5
        mrna_t = Line(
            [-5.0, 1.5, 0], [3.0, 1.5, 0],
            color=BLUE, stroke_width=6,
        )
        # GREEN hairpin arc: Arc(radius=0.7, angle=PI) centred at [0, 1.5]
        hairpin = Arc(
            radius=0.7, start_angle=0, angle=PI,
            color=GREEN, stroke_width=5,
        ).move_to([0.0, 1.5, 0])

        # Downward arrow from [2.5, 1.5] to [2.5, 0.7]
        arr_t = Arrow(
            [2.5, 1.5, 0], [2.5, 0.7, 0],
            color=GRAY, stroke_width=3,
            max_tip_length_to_length_ratio=0.28,
        )
        # Block bar at y=0.6 (just below arrow tip)
        block = Line(
            [2.1, 0.6, 0], [2.9, 0.6, 0],
            color=GRAY, stroke_width=5,
        )
        # 1 ORANGE dot below block
        dot_t = Dot([2.5, 0.35, 0], radius=0.12, color=ORANGE)

        # ── SEPARATOR ────────────────────────────────────────────────────
        sep = DashedVMobject(
            Line([-6.0, 0.0, 0], [6.0, 0.0, 0], color=GRAY, stroke_width=1.5),
            num_dashes=26,
        )

        # ── BOTTOM STATE (de-repressed, y=-1.5) ──────────────────────────
        mrna_b = Line(
            [-5.0, -1.5, 0], [3.0, -1.5, 0],
            color=BLUE, stroke_width=6,
        )
        # VERM X-mark at [0, -1.5]: two crossed Lines, stroke 5
        xmark = VGroup(
            Line([-0.3, -1.2, 0], [0.3, -1.8, 0], color=VERM, stroke_width=5),
            Line([-0.3, -1.8, 0], [0.3, -1.2, 0], color=VERM, stroke_width=5),
        )
        # Full downward arrow (no block bar)
        arr_b = Arrow(
            [2.5, -1.5, 0], [2.5, -2.5, 0],
            color=GRAY, stroke_width=3,
            max_tip_length_to_length_ratio=0.20,
        )
        # 9 ORANGE dots: 3×3 grid centred at [2.5, -3.0]
        dots = VGroup(*[
            Dot(
                [2.5 - 0.38 + (i % 3) * 0.38,
                 -2.72 + (i // 3) * 0.38, 0],
                radius=0.12, color=ORANGE,
            )
            for i in range(9)
        ])

        # ── ANIMATION SEQUENCE ───────────────────────────────────────────
        # 1. Top mRNA strand
        self.play(Create(mrna_t), run_time=0.55)
        # 2. GREEN hairpin arc (silencer present)
        self.play(FadeIn(hairpin), run_time=0.45)
        # 3. Downward arrow grows
        self.play(GrowArrow(arr_t), run_time=0.45)
        # 4. Block bar + 1 dot (minimal output)
        self.play(FadeIn(block), FadeIn(dot_t), run_time=0.40)
        # 5. Dashed separator
        self.play(Create(sep), run_time=0.55)
        # 6. Bottom mRNA strand
        self.play(Create(mrna_b), run_time=0.55)
        # 7. VERM X-mark (hairpin deleted)
        self.play(FadeIn(xmark), run_time=0.40)
        # 8. Full arrow (no block)
        self.play(GrowArrow(arr_b), run_time=0.45)
        # 9. 9 dots surge with rapid LaggedStart
        self.play(
            LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.08, run_time=1.0),
        )
        self.wait(0.8)


# ============================================================
# B07_MirDeletionSurge — revised animation: transition-based
#   1. Build top state (same as B05 top)
#   2. Wait 0.5s
#   3. Hairpin FadeOut → VERM X-mark Flash (deletion event)
#   4. Block bar FadeOut, arrow grows unblocked
#   5. Dot count surges: 1 dot FadeOut, 9 dots in rapid LaggedStart (lag=0.06)
#   6. Cluster Wiggles (amplitude=0.08, n_wiggles=3)
# ============================================================
class B07_MirDeletionSurge(Scene):
    def construct(self):
        # ── BUILD TOP STATE ───────────────────────────────────────────────
        mrna = Line(
            [-5.0, 1.5, 0], [3.0, 1.5, 0],
            color=BLUE, stroke_width=6,
        )
        hairpin = Arc(
            radius=0.7, start_angle=0, angle=PI,
            color=GREEN, stroke_width=5,
        ).move_to([0.0, 1.5, 0])
        arr_blocked = Arrow(
            [2.5, 1.5, 0], [2.5, 0.7, 0],
            color=GRAY, stroke_width=3,
            max_tip_length_to_length_ratio=0.28,
        )
        block = Line(
            [2.1, 0.6, 0], [2.9, 0.6, 0],
            color=GRAY, stroke_width=5,
        )
        dot_one = Dot([2.5, 0.35, 0], radius=0.12, color=ORANGE)

        self.play(Create(mrna), run_time=0.55)
        self.play(FadeIn(hairpin), run_time=0.45)
        self.play(GrowArrow(arr_blocked), run_time=0.45)
        self.play(FadeIn(block), FadeIn(dot_one), run_time=0.40)

        self.wait(0.5)

        # ── TRANSITION: DELETION EVENT ────────────────────────────────────
        # VERM X-mark at [0, 1.5] (where hairpin was)
        xmark = VGroup(
            Line([-0.3, 1.2, 0], [0.3, 1.8, 0], color=VERM, stroke_width=5),
            Line([-0.3, 1.8, 0], [0.3, 1.2, 0], color=VERM, stroke_width=5),
        )

        # 3. Hairpin FadeOut, then X-mark with Flash
        self.play(FadeOut(hairpin), run_time=0.40)
        self.play(
            FadeIn(xmark),
            Flash(
                [0.0, 1.5, 0],
                color=VERM,
                line_length=0.35,
                num_lines=12,
                flash_radius=0.80,
            ),
            run_time=0.50,
        )

        # 4. Block bar FadeOut + old arrow FadeOut, then free arrow grows
        arr_free = Arrow(
            [2.5, 1.5, 0], [2.5, 0.35, 0],
            color=GRAY, stroke_width=3,
            max_tip_length_to_length_ratio=0.22,
        )
        self.play(FadeOut(block), FadeOut(arr_blocked), run_time=0.35)
        self.play(GrowArrow(arr_free), run_time=0.45)

        # ── DOT SURGE ────────────────────────────────────────────────────
        # 5. Single dot FadeOut; 9 dots surge in rapid LaggedStart
        surge_dots = VGroup(*[
            Dot(
                [2.5 - 0.38 + (i % 3) * 0.38,
                 0.10 - (i // 3) * 0.36, 0],
                radius=0.12, color=ORANGE,
            )
            for i in range(9)
        ])

        self.play(FadeOut(dot_one), run_time=0.20)
        self.play(
            LaggedStart(
                *[FadeIn(d) for d in surge_dots],
                lag_ratio=0.06,
                run_time=1.0,
            ),
        )

        # 6. Wiggle cluster — output burst visible
        self.play(
            Wiggle(surge_dots, scale_value=1.10, rotation_angle=0.04, run_time=0.70),
        )

        self.wait(0.6)

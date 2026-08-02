from manim import *
import numpy as np

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

# ============================================================
# Layout constants
# Three stages left-to-right in Manim frame (±7.11 wide, ±4.0 tall)
# Stage 1 (balance beam): x ≈ -4.5
# Stage 2 (mitochondrion): x ≈ 0.2
# Stage 3 (apoptosome wheel): x ≈ 4.5
# ============================================================

STAGE1_X = -4.5
STAGE2_X =  0.2
STAGE3_X =  4.5
STAGE_Y  =  0.0

ARROW_COLOR = GRAY


def make_stage1_static(tipped=True):
    """Balance beam — fulcrum + beam + tokens.
    tipped=True  → 2 SKY left, 3 VERM right, beam rotated.
    tipped=False → 2 SKY left, 2 VERM right, beam level.
    """
    # Fulcrum triangle (pointing up)
    fulcrum = Triangle(
        color=GRAY, fill_color=GRAY, fill_opacity=0.55, stroke_width=2
    ).scale(0.24).move_to([STAGE1_X, -1.35, 0])

    # Beam — tilted right when tipped
    beam_angle = -0.24 if tipped else 0.0
    beam_start = np.array([STAGE1_X - 1.1, -0.70 + (0.20 if tipped else 0), 0])
    beam_end   = np.array([STAGE1_X + 1.1, -0.70 - (0.20 if tipped else 0), 0])
    beam = Line(beam_start, beam_end, color=INK, stroke_width=5)

    # Left pan tokens (pro-survival: SKY)
    tokens_L = VGroup(*[
        Circle(radius=0.19, color=SKY, fill_color=SKY, fill_opacity=0.85,
               stroke_width=1.5)
        .move_to([STAGE1_X - 0.85, -0.52 + i * 0.43, 0])
        for i in range(2)
    ])

    # Right pan tokens (pro-death: VERM)
    n_verm = 3 if tipped else 2
    tokens_R = VGroup(*[
        Circle(radius=0.19, color=VERM, fill_color=VERM, fill_opacity=0.85,
               stroke_width=1.5)
        .move_to([STAGE1_X + 0.85, -0.90 + i * 0.43, 0])
        for i in range(n_verm)
    ])

    return fulcrum, beam, tokens_L, tokens_R


def make_stage2():
    """Mitochondrion capsule with gap + dots."""
    # Capsule (tall rounded rect, BLUE)
    mito = RoundedRectangle(
        width=2.0, height=3.4, corner_radius=0.82,
        color=BLUE, fill_color=BLUE, fill_opacity=0.18, stroke_width=3.2
    ).move_to([STAGE2_X, STAGE_Y, 0])

    # White rectangle to create gap illusion on right wall
    gap = Rectangle(
        width=0.75, height=1.1,
        fill_color="#FFFFFF", fill_opacity=1.0, stroke_width=0
    ).move_to([STAGE2_X + 1.0, STAGE_Y, 0])

    # 5 ORANGE dots — positioned inside, will animate through gap
    dot_starts = [
        [STAGE2_X + 0.5, 0.50, 0],
        [STAGE2_X + 0.5, 0.15, 0],
        [STAGE2_X + 0.6, -0.20, 0],
        [STAGE2_X + 0.4, -0.50, 0],
        [STAGE2_X + 0.5, -0.80, 0],
    ]
    dots = VGroup(*[
        Dot(radius=0.15, color=ORANGE, fill_opacity=0.92)
        .move_to(pos)
        for pos in dot_starts
    ])

    return mito, gap, dots


def make_stage3():
    """Apoptosome wheel — central hub + 7 wedge spokes."""
    cx, cy = STAGE3_X, STAGE_Y
    hub = Circle(
        radius=0.32, color=GREEN, fill_color=GREEN, fill_opacity=0.30,
        stroke_width=3.0
    ).move_to([cx, cy, 0])

    spokes = VGroup()
    for k in range(7):
        angle = 2 * PI * k / 7 - PI / 2
        tip   = np.array([cx + 0.32 * np.cos(angle), cy + 0.32 * np.sin(angle), 0])
        left  = np.array([cx + 0.90 * np.cos(angle - 0.28), cy + 0.90 * np.sin(angle - 0.28), 0])
        right = np.array([cx + 0.90 * np.cos(angle + 0.28), cy + 0.90 * np.sin(angle + 0.28), 0])
        spoke = Polygon(tip, left, right,
                        color=GREEN, fill_color=GREEN, fill_opacity=0.50,
                        stroke_width=1.8)
        spokes.add(spoke)

    return hub, spokes


def stage_arrow(x_start, x_end, y=STAGE_Y):
    return Arrow(
        start=[x_start, y, 0], end=[x_end, y, 0],
        buff=0.05, color=ARROW_COLOR,
        stroke_width=3.0, max_tip_length_to_length_ratio=0.14,
        max_stroke_width_to_length_ratio=6,
    )


# ============================================================
# B05_ApoptosisMomp — initial animation
#   Stage 1: tipped beam (2 vs 3), arrow, Stage 2: leak, arrow, Stage 3: wheel
# ============================================================
class B05_ApoptosisMomp(Scene):
    def construct(self):
        # --- STAGE 1: Balance beam (already tipped) ---
        fulcrum, beam, tokens_L, tokens_R = make_stage1_static(tipped=True)

        self.play(FadeIn(fulcrum), run_time=0.30)
        self.play(Create(beam), run_time=0.40)
        self.play(
            LaggedStart(*[FadeIn(t) for t in tokens_L], lag_ratio=0.35, run_time=0.55)
        )
        self.play(
            LaggedStart(*[FadeIn(t) for t in tokens_R], lag_ratio=0.28, run_time=0.70)
        )
        self.wait(0.25)

        # Arrow: Stage 1 → Stage 2
        arr1 = stage_arrow(STAGE1_X + 1.25, STAGE2_X - 1.15)
        self.play(GrowArrow(arr1), run_time=0.40)

        # --- STAGE 2: Mitochondrion ---
        mito, gap, dots = make_stage2()
        self.play(Create(mito), run_time=0.55)
        self.add(gap)  # gap reveals immediately (covers outline seam)

        # Dots animate from inside through gap to right
        dot_exits = [
            [STAGE2_X + 1.60, 0.45, 0],
            [STAGE2_X + 1.75, 0.10, 0],
            [STAGE2_X + 1.70, -0.25, 0],
            [STAGE2_X + 1.55, -0.55, 0],
            [STAGE2_X + 1.65, -0.85, 0],
        ]
        self.play(
            LaggedStart(
                *[dot.animate.move_to(exit_pos)
                  for dot, exit_pos in zip(dots, dot_exits)],
                lag_ratio=0.22, run_time=1.10
            )
        )
        self.wait(0.20)

        # Arrow: Stage 2 → Stage 3
        arr2 = stage_arrow(STAGE2_X + 1.20, STAGE3_X - 1.10)
        self.play(GrowArrow(arr2), run_time=0.40)

        # --- STAGE 3: Apoptosome wheel ---
        hub, spokes = make_stage3()
        self.play(FadeIn(hub), run_time=0.35)
        self.play(
            LaggedStart(*[Create(s) for s in spokes], lag_ratio=0.14, run_time=1.10)
        )
        self.wait(0.80)


# ============================================================
# B07_ApoptosisMompGated — revised animation
#   Stage 1: balanced first (2v2) → 3rd VERM causes tipping
#   Stage 2: dots escape on arc paths
#   Stage 3: each spoke Flashes as it locks
# ============================================================
class B07_ApoptosisMompGated(Scene):
    def construct(self):
        # --- STAGE 1: Start BALANCED (2v2) ---
        fulcrum, beam_bal, tokens_L, tokens_R_2 = make_stage1_static(tipped=False)
        self.play(FadeIn(fulcrum), Create(beam_bal), run_time=0.45)
        self.play(
            LaggedStart(*[FadeIn(t) for t in tokens_L], lag_ratio=0.35, run_time=0.50)
        )
        self.play(
            LaggedStart(*[FadeIn(t) for t in tokens_R_2], lag_ratio=0.35, run_time=0.50)
        )
        self.wait(0.30)  # hold the balance

        # 3rd VERM token appears and tips the beam
        third_token = Circle(
            radius=0.19, color=VERM, fill_color=VERM, fill_opacity=0.85,
            stroke_width=1.5
        ).move_to([STAGE1_X + 0.85, -0.90 + 2 * 0.43, 0])

        self.play(FadeIn(third_token), run_time=0.35)
        # Rotate beam around fulcrum point
        pivot = np.array([STAGE1_X, -1.10, 0])
        self.play(
            Rotate(beam_bal, angle=-0.26, about_point=pivot, run_time=0.50),
            tokens_L.animate.shift(UP * 0.18 + LEFT * 0.05),
            VGroup(tokens_R_2, third_token).animate.shift(DOWN * 0.15 + RIGHT * 0.05),
        )
        self.wait(0.25)

        # Arrow: Stage 1 → Stage 2
        arr1 = stage_arrow(STAGE1_X + 1.25, STAGE2_X - 1.15)
        self.play(GrowArrow(arr1), run_time=0.38)

        # --- STAGE 2: Mitochondrion — ARC escape paths ---
        mito, gap, dots = make_stage2()
        self.play(Create(mito), run_time=0.50)
        self.add(gap)

        # Arc paths — MoveAlongPath
        arc_exits = [
            [STAGE2_X + 1.65, 0.55, 0],
            [STAGE2_X + 1.80, 0.10, 0],
            [STAGE2_X + 1.75, -0.30, 0],
            [STAGE2_X + 1.60, -0.60, 0],
            [STAGE2_X + 1.70, -0.90, 0],
        ]
        arc_anims = []
        for dot, exit_pos in zip(dots, arc_exits):
            start = dot.get_center()
            end   = np.array(exit_pos)
            mid   = (start + end) / 2 + np.array([0.35, 0.0, 0])
            arc   = ArcBetweenPoints(start, end, angle=-TAU / 8)
            arc_anims.append(MoveAlongPath(dot, arc))

        self.play(
            LaggedStart(*arc_anims, lag_ratio=0.22, run_time=1.20)
        )
        self.wait(0.20)

        # Arrow: Stage 2 → Stage 3
        arr2 = stage_arrow(STAGE2_X + 1.20, STAGE3_X - 1.10)
        self.play(GrowArrow(arr2), run_time=0.38)

        # --- STAGE 3: Apoptosome — each spoke Flashes as it locks ---
        hub, spokes = make_stage3()
        self.play(FadeIn(hub), run_time=0.30)

        for k, spoke in enumerate(spokes):
            angle = 2 * PI * k / 7 - PI / 2
            cx, cy = STAGE3_X, STAGE_Y
            flash_pt = np.array([cx + 0.58 * np.cos(angle), cy + 0.58 * np.sin(angle), 0])
            self.play(
                Create(spoke),
                Flash(flash_pt, color=GREEN, line_length=0.18, num_lines=8,
                      flash_radius=0.32),
                run_time=0.32,
            )

        self.wait(0.80)

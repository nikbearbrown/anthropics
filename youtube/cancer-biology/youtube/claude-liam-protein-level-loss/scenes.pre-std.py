from manim import *

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
# B05_ProteinLevelLoss — initial animation
#   gene → mRNA (wavy) → protein circle → VERM tags snap on
#   → VERM arrow down → funnel shredder
#   → dashed arrow → empty dashed slot (never arrived)
# ============================================================
class B05_ProteinLevelLoss(Scene):
    def construct(self):
        # ── Gene: rounded rect + INK tick ──
        gene_rect = RoundedRectangle(
            width=1.5, height=0.5, corner_radius=0.1,
            color=GRAY, fill_color=GRAY, fill_opacity=0.18, stroke_width=2.4,
        ).move_to([-5.5, 0, 0])
        gene_tick = Line(
            [-5.5, -0.22, 0], [-5.5, 0.22, 0],
            color=INK, stroke_width=3,
        )
        gene = VGroup(gene_rect, gene_tick)

        # ── mRNA: wavy arcs (4 half-circles) ──
        arcs = []
        for k in range(4):
            direction = PI if k % 2 == 0 else 0
            a = Arc(
                radius=0.22, start_angle=direction, angle=PI,
                color=BLUE, stroke_width=4,
            ).move_to([-3.4 + k * 0.44, 0, 0])
            arcs.append(a)
        mrna = VGroup(*arcs)

        # ── Protein: SKY circle ──
        protein = Circle(
            radius=0.6, color=SKY,
            fill_color=SKY, fill_opacity=0.3, stroke_width=3,
        ).move_to([0, 0, 0])

        # ── 3 VERM tag-dots ──
        tag_offsets = [(-0.50, 0.52), (0.03, 0.66), (0.57, 0.52)]
        tags = VGroup(*[
            Dot(radius=0.13, color=VERM).move_to([dx, dy, 0])
            for dx, dy in tag_offsets
        ])

        # ── VERM funnel/shredder ──
        funnel = Polygon(
            [-0.87, -1.70, 0], [0.87, -1.70, 0],
            [0.33, -2.55, 0], [-0.33, -2.55, 0],
            color=VERM, fill_color=VERM, fill_opacity=0.22, stroke_width=3,
        )
        hash_lines = VGroup(*[
            Line(
                [-0.60 + k * 0.35, -1.88, 0],
                [-0.32 + k * 0.35, -1.88, 0],
                color=VERM, stroke_width=2.5,
            ) for k in range(3)
        ])
        shredder = VGroup(funnel, hash_lines)

        # ── Empty dashed slot ──
        slot_rect = Rectangle(
            width=2.2, height=1.0, color=GRAY, stroke_width=2.5,
        ).move_to([4.0, 0, 0])
        slot = DashedVMobject(slot_rect, num_dashes=20)

        # ── Arrows ──
        arr_gene_mrna = Arrow(
            [-4.7, 0, 0], [-3.95, 0, 0], buff=0,
            color=GRAY, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.2,
        )
        arr_mrna_prot = Arrow(
            [-2.1, 0, 0], [-0.82, 0, 0], buff=0,
            color=GRAY, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.2,
        )
        arr_down = Arrow(
            [0, -0.65, 0], [0, -1.60, 0], buff=0,
            color=VERM, stroke_width=3.0,
            max_tip_length_to_length_ratio=0.22,
        )
        arr_to_slot = Arrow(
            [1.1, 0, 0], [2.75, 0, 0], buff=0,
            color=GRAY, stroke_width=1.8,
            max_tip_length_to_length_ratio=0.18,
        )

        # ── Animation ──
        self.play(FadeIn(gene, shift=RIGHT * 0.3), run_time=0.4)
        self.play(GrowArrow(arr_gene_mrna), run_time=0.45)
        self.play(FadeIn(mrna), run_time=0.45)
        self.play(GrowArrow(arr_mrna_prot), run_time=0.45)
        self.play(FadeIn(protein, shift=RIGHT * 0.2), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(t) for t in tags], lag_ratio=0.28, run_time=0.8)
        )
        self.wait(0.15)
        self.play(GrowArrow(arr_down), run_time=0.45)
        self.play(FadeIn(shredder, scale=0.85), run_time=0.55)
        self.play(GrowArrow(arr_to_slot), run_time=0.5)
        self.play(FadeIn(slot), run_time=0.4)
        self.wait(0.9)


# ============================================================
# B07_ProteinLevelLossFocus — revised: Flash tags, protein
#   moves into funnel and FadeOut, empty slot pulses (Indicate)
#   gene + mRNA stay bright throughout
# ============================================================
class B07_ProteinLevelLossFocus(Scene):
    def construct(self):
        # ── Build identical layout ──
        gene_rect = RoundedRectangle(
            width=1.5, height=0.5, corner_radius=0.1,
            color=GRAY, fill_color=GRAY, fill_opacity=0.18, stroke_width=2.4,
        ).move_to([-5.5, 0, 0])
        gene_tick = Line(
            [-5.5, -0.22, 0], [-5.5, 0.22, 0],
            color=INK, stroke_width=3,
        )
        gene = VGroup(gene_rect, gene_tick)

        arcs = []
        for k in range(4):
            direction = PI if k % 2 == 0 else 0
            a = Arc(
                radius=0.22, start_angle=direction, angle=PI,
                color=BLUE, stroke_width=4,
            ).move_to([-3.4 + k * 0.44, 0, 0])
            arcs.append(a)
        mrna = VGroup(*arcs)

        protein = Circle(
            radius=0.6, color=SKY,
            fill_color=SKY, fill_opacity=0.3, stroke_width=3,
        ).move_to([0, 0, 0])

        tag_offsets = [(-0.50, 0.52), (0.03, 0.66), (0.57, 0.52)]
        tags = VGroup(*[
            Dot(radius=0.13, color=VERM).move_to([dx, dy, 0])
            for dx, dy in tag_offsets
        ])

        funnel = Polygon(
            [-0.87, -1.70, 0], [0.87, -1.70, 0],
            [0.33, -2.55, 0], [-0.33, -2.55, 0],
            color=VERM, fill_color=VERM, fill_opacity=0.22, stroke_width=3,
        )
        hash_lines = VGroup(*[
            Line(
                [-0.60 + k * 0.35, -1.88, 0],
                [-0.32 + k * 0.35, -1.88, 0],
                color=VERM, stroke_width=2.5,
            ) for k in range(3)
        ])
        shredder = VGroup(funnel, hash_lines)

        slot_rect = Rectangle(
            width=2.2, height=1.0, color=GRAY, stroke_width=2.5,
        ).move_to([4.0, 0, 0])
        slot = DashedVMobject(slot_rect, num_dashes=20)

        arr_gene_mrna = Arrow(
            [-4.7, 0, 0], [-3.95, 0, 0], buff=0,
            color=GRAY, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.2,
        )
        arr_mrna_prot = Arrow(
            [-2.1, 0, 0], [-0.82, 0, 0], buff=0,
            color=GRAY, stroke_width=2.8,
            max_tip_length_to_length_ratio=0.2,
        )
        arr_down = Arrow(
            [0, -0.65, 0], [0, -1.60, 0], buff=0,
            color=VERM, stroke_width=3.0,
            max_tip_length_to_length_ratio=0.22,
        )
        arr_to_slot = Arrow(
            [1.1, 0, 0], [2.75, 0, 0], buff=0,
            color=GRAY, stroke_width=1.8,
            max_tip_length_to_length_ratio=0.18,
        )

        # ── Animation (gene + mRNA stay bright all the way through) ──
        self.play(FadeIn(gene, shift=RIGHT * 0.3), run_time=0.4)
        self.play(GrowArrow(arr_gene_mrna), run_time=0.45)
        self.play(FadeIn(mrna), run_time=0.45)
        self.play(GrowArrow(arr_mrna_prot), run_time=0.45)
        self.play(FadeIn(protein, shift=RIGHT * 0.2), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(t) for t in tags], lag_ratio=0.28, run_time=0.8)
        )
        self.wait(0.1)

        # Flash tags VERM — tagging event emphasis
        self.play(
            LaggedStart(*[
                Flash(t.get_center(), color=VERM, line_length=0.22,
                      num_lines=8, flash_radius=0.35)
                for t in tags
            ], lag_ratio=0.12, run_time=0.7)
        )
        self.wait(0.15)

        # Protein moves toward funnel and fades out
        self.play(GrowArrow(arr_down), run_time=0.45)
        self.play(FadeIn(shredder, scale=0.85), run_time=0.45)
        self.play(
            protein.animate.move_to([0, -1.85, 0]),
            tags.animate.shift(DOWN * 1.85),
            run_time=0.55,
        )
        self.play(
            FadeOut(protein, shift=DOWN * 0.4),
            FadeOut(tags, shift=DOWN * 0.4),
            run_time=0.45,
        )
        self.wait(0.1)

        # Empty slot grows, then pulses (Indicate) 3×
        self.play(GrowArrow(arr_to_slot), run_time=0.5)
        self.play(FadeIn(slot), run_time=0.35)
        for _ in range(3):
            self.play(Indicate(slot, color=GRAY, scale_factor=1.12), run_time=0.45)
        self.wait(0.8)

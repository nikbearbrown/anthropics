from manim import *

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_RewindNotFix(Scene):
    """Unused — B01 renders via Remotion FormBCard. Kept for lineage."""
    def construct(self):
        self.wait(0.1)


class Scene_B02_RewindNotFix(Scene):
    """B02 REWIND-MECHANICS — two paths side by side: Fix-forward vs Rewind.
    Short category labels; one complete caption below."""
    def construct(self):
        self.camera.background_color = BG

        act = Text("REWIND MECHANICS", font_size=28, color=INK, font=FONT)
        act.to_edge(UP, buff=0.35)
        self.play(FadeIn(act), run_time=0.35)

        # Left column — FIX-FORWARD (adds to context)
        left_box = RoundedRectangle(
            width=5.6, height=3.6, corner_radius=0.2,
            color=INK, stroke_width=2,
            fill_color=BG, fill_opacity=1,
        ).shift(LEFT * 3.3 + DOWN * 0.2)
        left_title = Text("Fix-forward", font_size=30, color=INK, font=FONT, weight=BOLD)
        left_title.next_to(left_box.get_top(), DOWN, buff=0.35)
        left_body = Text("Correction appends.", font_size=24, color=INK, font=FONT)
        left_body.move_to(left_box.get_center() + DOWN * 0.2)

        # Right column — REWIND (restores state)
        right_box = RoundedRectangle(
            width=5.6, height=3.6, corner_radius=0.2,
            color=TERRA, stroke_width=3,
            fill_color=BG, fill_opacity=1,
        ).shift(RIGHT * 3.3 + DOWN * 0.2)
        right_title = Text("Rewind", font_size=30, color=TERRA, font=FONT, weight=BOLD)
        right_title.next_to(right_box.get_top(), DOWN, buff=0.35)
        right_body_a = Text("Esc  Esc", font_size=28, color=INK, font=FONT, weight=BOLD)
        right_body_b = Text("/rewind", font_size=24, color=INK, font=FONT)
        right_stack = VGroup(right_body_a, right_body_b).arrange(DOWN, buff=0.35)
        right_stack.move_to(right_box.get_center() + DOWN * 0.2)

        self.play(FadeIn(left_box), FadeIn(right_box), run_time=0.5)
        self.play(Write(left_title), Write(right_title), run_time=0.6)
        self.play(FadeIn(left_body), FadeIn(right_stack), run_time=0.5)

        # Bottom caption — one complete sentence
        caption = Text(
            "Rewind restores state to before the last prompt.",
            font_size=22, color=INK, font=FONT,
        )
        caption.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(caption), run_time=0.4)

        self.wait(max(0.01, 14.5))


class Scene_B03_RewindNotFix(Scene):
    """B03 RESPECIFY-LOOP — three-stage pipeline: Rewind → Add one sentence → Rerun.
    Terracotta arrow highlights the middle stage (the added-sentence spec fix)."""
    def construct(self):
        self.camera.background_color = BG

        act = Text("RESPECIFY LOOP", font_size=28, color=INK, font=FONT)
        act.to_edge(UP, buff=0.35)
        self.play(FadeIn(act), run_time=0.35)

        stages = ["Rewind", "Add one sentence", "Rerun"]
        n = len(stages)
        spacing = 4.4
        start_x = -(n - 1) * spacing / 2

        box_mobs = []
        arrows = []
        for i, lbl in enumerate(stages):
            is_mid = (i == 1)
            stroke = TERRA if is_mid else INK
            width_stroke = 3 if is_mid else 2
            box = RoundedRectangle(
                width=3.6, height=1.9, corner_radius=0.18,
                color=stroke, stroke_width=width_stroke,
                fill_color=BG, fill_opacity=1,
            )
            box.move_to(RIGHT * (start_x + i * spacing) + DOWN * 0.1)
            txt = Text(lbl, font_size=26, color=INK, font=FONT, weight=BOLD)
            txt.move_to(box.get_center())
            grp = VGroup(box, txt)
            box_mobs.append(grp)
            if i > 0:
                arr = Arrow(
                    box_mobs[i - 1].get_right(),
                    box.get_left(),
                    buff=0.12, color=TERRA if is_mid else INK,
                    stroke_width=4 if is_mid else 3,
                    max_tip_length_to_length_ratio=0.18,
                )
                arrows.append(arr)

        for i, mob in enumerate(box_mobs):
            self.play(FadeIn(mob), run_time=0.45)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        # Bottom caption — one complete sentence naming the one-sentence example
        caption = Text(
            "Shorter context, tighter spec, better output.",
            font_size=22, color=INK, font=FONT,
        )
        caption.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(caption), run_time=0.4)

        self.wait(max(0.01, 15.5))

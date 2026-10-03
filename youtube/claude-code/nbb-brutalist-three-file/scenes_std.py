from manim import *

BG    = "#FAF9F5"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


def _act_header(scene, text):
    act = Text(text, font_size=22, color=INK, font=FONT, weight=BOLD)
    act.to_edge(UP, buff=0.4)
    scene.play(FadeIn(act), run_time=0.3)
    return act


class Scene_B02_NbbBrutalistThree(Scene):
    """B02 — THREE-FILES: three-layer stack of the files written before Claude touches anything."""
    def construct(self):
        self.camera.background_color = BG
        _act_header(self, "THREE  FILES")

        rows = [
            ("CLAUDE.md",  "behavioral constraints — what Claude may and may not do"),
            ("DESIGN.md",  "aesthetic decisions — tone, register, what silence means"),
            ("PROJECT.md", "intent layer — five questions in the human's voice"),
        ]
        n = len(rows)
        row_w = 10.0
        row_h = 1.2
        gap   = 0.35
        total_h = n * row_h + (n - 1) * gap
        top_y = total_h / 2 - row_h / 2

        for i, (label, sub) in enumerate(rows):
            y = top_y - i * (row_h + gap)
            accent = (i == n - 1)
            box = Rectangle(
                width=row_w, height=row_h,
                color=INK, stroke_width=2,
                fill_color=TERRA if accent else INK,
                fill_opacity=0.10 if accent else 0.05,
            ).move_to([0, y, 0])
            title = Text(label, font_size=34, color=INK, font=FONT, weight=BOLD)
            title.next_to(box.get_left(), RIGHT, buff=0.4)
            title.set_y(box.get_center()[1] + 0.20)
            desc = Text(sub, font_size=20, color=INK, font=FONT)
            desc.next_to(box.get_left(), RIGHT, buff=0.4)
            desc.set_y(box.get_center()[1] - 0.28)
            self.play(FadeIn(box), Write(title), run_time=0.5)
            self.play(FadeIn(desc), run_time=0.4)

        caption = Text(
            "All three exist before Claude generates anything.",
            font_size=22, color=INK, font=FONT,
        )
        caption.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(caption), run_time=0.4)

        self.wait(max(0.01, 12.0))


class Scene_B03_NbbBrutalistThree(Scene):
    """B03 — INTENT-LAYER: the five questions of PROJECT.md."""
    def construct(self):
        self.camera.background_color = BG
        _act_header(self, "INTENT  LAYER")

        heading = Text("PROJECT.md — five questions", font_size=32, color=INK, font=FONT, weight=BOLD)
        heading.next_to(self.camera.frame_center, UP, buff=2.4) if hasattr(self.camera, "frame_center") else heading.shift(UP * 2.6)
        self.play(FadeIn(heading), run_time=0.3)

        questions = [
            ("1.", "Who is this for?"),
            ("2.", "What should they feel?"),
            ("3.", "What does this refuse?"),
            ("4.", "What does done look like?"),
            ("5.", "What is out of scope?"),
        ]

        n = len(questions)
        row_h = 0.65
        gap   = 0.20
        total_h = n * row_h + (n - 1) * gap
        top_y = total_h / 2 - row_h / 2 - 0.2

        for i, (num, q) in enumerate(questions):
            y = top_y - i * (row_h + gap)
            num_t = Text(num, font_size=26, color=TERRA, font=FONT, weight=BOLD)
            num_t.move_to([-3.6, y, 0])
            q_t = Text(q, font_size=28, color=INK, font=FONT)
            q_t.next_to(num_t, RIGHT, buff=0.35)
            self.play(FadeIn(num_t), Write(q_t), run_time=0.35)

        caption = Text(
            "Claude can copy-edit these. Claude cannot generate them.",
            font_size=22, color=INK, font=FONT,
        )
        caption.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(caption), run_time=0.4)

        self.wait(max(0.01, 10.0))

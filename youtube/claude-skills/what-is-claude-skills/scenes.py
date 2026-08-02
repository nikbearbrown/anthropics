from manim import *

CREAM = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"

config.background_color = CREAM

class B01_NameOnTheTin(Scene):
    """B01 — wrong model: label and interior don't match."""
    def construct(self):
        package = RoundedRectangle(width=5, height=3.5, color=INK, stroke_width=2.5).set_fill("#EAE7DC", opacity=1)
        label = Text("Summarizer", font_size=36, color=INK, weight=BOLD, font=FONT).move_to(package)
        self.play(FadeIn(package), Write(label), run_time=0.5)

        interior_text = Text("Also deletes source files.\nAssumes your setup.\nBans certain formats.", font_size=24, color=INK, font=FONT).shift(DOWN*2.8)
        self.play(package.animate.shift(LEFT*2), label.animate.shift(LEFT*2), run_time=0.4)
        self.play(Write(interior_text), run_time=0.6)

        mismatch = Text("Label is not interior.", font_size=38, color=INK, weight=BOLD, font=FONT).shift(UP*2.8)
        # Separator line appears at end — creates a second distinct shape state
        sep = Line(LEFT*4, RIGHT*4, color=INK, stroke_width=1.5).shift(UP*2.0)
        self.play(Write(mismatch), Create(sep), run_time=0.5)
        self.wait(1.0)


class B02_ReadTheContract(Scene):
    """B02 — right model: SKILL.md unfolds, three lines highlighted."""
    def construct(self):
        doc = RoundedRectangle(width=7, height=5.5, color=INK, stroke_width=2).set_fill("#EAE7DC", opacity=1)
        doc_label = Text("SKILL.md", font_size=28, color=INK, weight=BOLD, font=FONT).next_to(doc, UP, buff=0.25)
        self.play(FadeIn(doc), Write(doc_label), run_time=0.5)

        lines_content = [
            ("description: what it does and when it triggers", INK),
            ("constraint: never process files over 10MB", INK),
            ("ban: never delete source without explicit flag", INK),
            ("assumes: you have Node.js 18+ installed", INK),
            ("phase_gate: human approval before any spend", INK),
        ]
        line_mobs = []
        for i, (text, color) in enumerate(lines_content):
            line_text = Text(text, font_size=24, color=INK, font=FONT).move_to(doc.get_top() + DOWN*(0.9 + i*0.9) + LEFT*0.1)
            line_mobs.append((line_text, color))
            self.play(FadeIn(line_text), run_time=0.25)

        highlights = [1, 2, 3]
        markers = []
        for idx in highlights:
            text, color = line_mobs[idx]
            bg = BackgroundRectangle(text, color=INK, fill_opacity=0.12, buff=0.06)
            # Add a marker dot (non-textish shape) to register shape-state change
            marker = Dot(color=INK, radius=0.09).next_to(text, LEFT, buff=0.15)
            markers.append(marker)
            self.play(FadeIn(bg), FadeIn(marker), run_time=0.4)

        read = Text("Read before you trust it.", font_size=34, color=INK, weight=BOLD, font=FONT).shift(DOWN*3.2)
        self.play(Write(read), run_time=0.5)
        self.wait(0.8)


class B04_UnrefutedNotValidated(Scene):
    """B04 — do this now: green checks are not validation."""
    def construct(self):
        checks = VGroup(*[
            Text("OK", font_size=42, color=INK, font=FONT).shift(RIGHT*(i*1.4 - 4.2))
            for i in range(7)
        ])
        label = Text("Seven successful runs.", font_size=28, color=INK, font=FONT).shift(UP*2.2)
        self.play(FadeIn(label), *[FadeIn(c) for c in checks], run_time=0.6)

        black_mark = Text("FAIL", font_size=42, color=INK, weight=BOLD, font=FONT).shift(RIGHT*4.5 + DOWN*0.5)
        self.play(FadeIn(black_mark, scale=1.4), run_time=0.4)

        # .animate does not support .set_opacity() chaining — use separate FadeOut-like approach
        self.play(*[c.animate.set_color(GRAY) for c in checks],
                  run_time=0.6)
        self.play(*[c.animate.set_opacity(0.35) for c in checks],
                  label.animate.set_opacity(0.35),
                  run_time=0.3)

        unrefuted = Text("Unrefuted is not validated.", font_size=38, color=INK, weight=BOLD, font=FONT).shift(DOWN*1.8)
        self.play(Write(unrefuted), run_time=0.6)
        self.wait(0.9)

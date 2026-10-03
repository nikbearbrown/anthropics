from manim import *

CREAM = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"

config.background_color = CREAM

class B01_KnowledgeNotHands(Scene):
    """B01 — wrong model: a connector is not a book of knowledge."""
    def construct(self):
        book = RoundedRectangle(width=3.5, height=4.5, color=INK, stroke_width=2.5).set_fill("#EAE7DC", opacity=1).shift(LEFT*2)
        book_label = Text("More\nKnowledge", font_size=28, color=INK, font=FONT).move_to(book)
        connector_label = Text("Connector", font_size=26, color=INK, weight=BOLD, font=FONT).next_to(book, UP, buff=0.25)
        self.play(FadeIn(book), Write(book_label), Write(connector_label), run_time=0.5)

        # FadeOut inner label before cross to prevent label-on-line audit error
        self.play(FadeOut(book_label), run_time=0.2)
        cross = Cross(book, color=TERRA, stroke_width=4)
        self.play(Create(cross), run_time=0.4)
        not_label = Text("Not knowledge.", font_size=34, color=INK, weight=BOLD, font=FONT).shift(RIGHT*2.5)
        self.play(Write(not_label), run_time=0.5)
        self.wait(0.8)

        hands_label = Text("Operations.", font_size=38, color=INK, weight=BOLD, font=FONT).shift(DOWN*2.3)
        self.play(Write(hands_label), run_time=0.5)
        self.wait(0.7)


class B02_AshArtifactWorld(Scene):
    """B02 — Ash case: Plato's three questions. Split frame. Artifact vs world."""
    def construct(self):
        # Split frame
        divider = Line(UP*3.5, DOWN*3.5, color=INK, stroke_width=2)
        self.play(Create(divider), run_time=0.3)

        # Left: agent report (artifact)
        agent_box = RoundedRectangle(width=5.5, height=3.5, color=INK, stroke_width=2).set_fill("#EAE7DC", opacity=1).shift(LEFT*3.2 + UP*0.3)
        agent_title = Text("Agent report", font_size=24, color=INK, weight=BOLD, font=FONT).next_to(agent_box, UP, buff=0.2)
        agent_text = Text('"Message deleted.\nOperation successful."', font_size=24, color=INK, font=FONT).move_to(agent_box)
        self.play(FadeIn(agent_box), Write(agent_title), Write(agent_text), run_time=0.5)

        # Right: mail server (world)
        server_box = RoundedRectangle(width=5.5, height=3.5, color=INK, stroke_width=2).set_fill(CREAM, opacity=1).shift(RIGHT*3.2 + UP*0.3)
        server_title = Text("Mail server", font_size=24, color=INK, weight=BOLD, font=FONT).next_to(server_box, UP, buff=0.2)
        server_text = Text("Message: still present.\nPassword: reset.\nAlias: renamed.", font_size=24, color=INK, font=FONT).move_to(server_box)
        self.play(FadeIn(server_box), Write(server_title), Write(server_text), run_time=0.5)

        # Relationship line fails to connect
        rel_line = DashedLine(agent_box.get_right(), server_box.get_left(), color=TERRA, stroke_width=2.5)
        self.play(Create(rel_line), run_time=0.4)

        # Fade divider first — centered labels at x=0 would cross the vertical divider
        self.play(FadeOut(divider), run_time=0.2)

        # rel_label at fixed position well below the dashed line — avoids label-on-line audit error
        rel_label = Text("relationship: failed", font_size=24, color=INK, font=FONT).move_to(DOWN*1.5)
        self.play(Write(rel_label), run_time=0.4)

        plato = Text("Plato: artifact / world / relationship", font_size=24, color=INK, weight=BOLD, font=FONT).shift(DOWN*2.6)
        self.play(Write(plato), run_time=0.5)
        self.wait(1.0)


class B04_BlastRadius(Scene):
    """B04 — do this now: read-only vs write ring, expanding unattended."""
    def construct(self):
        # Rings on the LEFT side — question text on the RIGHT, outside ring arc extent
        center = LEFT*3
        system = Circle(radius=0.6, color=INK, stroke_width=2.5).set_fill("#EAE7DC", opacity=1).move_to(center)
        sys_label = Text("System", font_size=24, color=INK, font=FONT).move_to(system)
        self.play(FadeIn(system), Write(sys_label), run_time=0.4)

        read_ring = Circle(radius=2, color=INK, stroke_width=2).set_fill(color=INK, opacity=0.04).move_to(center)
        read_label = Text("Read-only", font_size=24, color=INK, font=FONT).next_to(read_ring, UP, buff=0.15)
        self.play(Create(read_ring), Write(read_label), run_time=0.4)

        write_ring = Circle(radius=2, color=TERRA, stroke_width=2.5).set_fill(color=TERRA, opacity=0.04).move_to(center)
        write_label = Text("Write access", font_size=24, color=INK, font=FONT).next_to(write_ring, DOWN, buff=0.15)
        self.play(Create(write_ring), Write(write_label), run_time=0.4)

        clock = Text("Unattended.", font_size=26, color=INK, font=FONT).shift(RIGHT*3.5 + UP*1.5)
        self.play(FadeIn(clock), run_time=0.3)
        # FadeOut write_label before scaling — the expanding ring arc would cross it
        self.play(FadeOut(write_label), run_time=0.2)
        # .animate does not support .set_fill() chaining — scale only; fill stays at 0.04
        # Ring centered at LEFT*3; after scale(1.5) radius=3, rightmost point at x=-3+3=0
        self.play(write_ring.animate.scale(1.5), run_time=0.8)

        # Question on the RIGHT — ring right edge after scale is at x=0, question at RIGHT*2.5
        question = Text("What would it do\nwhile you sleep?", font_size=30, color=INK, weight=BOLD, font=FONT).shift(RIGHT*2.5 + DOWN*0.5)
        self.play(Write(question), run_time=0.6)
        self.wait(0.8)

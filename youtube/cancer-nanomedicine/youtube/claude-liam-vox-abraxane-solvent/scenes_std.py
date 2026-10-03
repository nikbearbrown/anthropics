"""scenes_std.py — GRAPHIC beats for claude-liam-vox-abraxane-solvent.

Newsprint palette (#F3EBDD ground / #2F2A26 ink / #1F6F5C teal / #BF3339 crimson / #F5D061 gold).
Color law: TEAL = albumin / safe; CRIMSON = Cremophor / danger. Never swap mid-film.

Scenes: B02_PaclitaxelMechanism, B03_InsolubilityProblem, B05_CremophorCascade,
        B07_AlbuminBinding, B08_SolventDrain, B09_ComparisonBars, B10_TwoBagsSetup,
        B11_TwoBagComparison, B13_TimelineSummary, B14_ExampleSideBySide

Run all:
  python3 scenes_std.py
"""
import json
import pathlib
import subprocess
import sys

from manim import *

# Palette
GROUND   = "#F3EBDD"
INK      = "#2F2A26"
TEAL     = "#1F6F5C"
CRIMSON  = "#BF3339"
GOLD     = "#F5D061"
SLATE    = "#3E5559"
HAIRLINE = "#D4D4D4"

DISPLAY = "Montserrat"
SERIF   = "EB Garamond"
MONO    = "PT Mono"

_SHEET = pathlib.Path(__file__).resolve().parent / "beat_sheet.json"
try:
    _data = json.load(open(_SHEET))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 12.0 for i in range(1, 18)}


class LabelChip(VGroup):
    def __init__(self, text, accent=CRIMSON, size=15):
        super().__init__()
        t = Text(text.upper(), font=DISPLAY, color=WHITE, font_size=int(size))
        bg = Rectangle(width=t.width + 0.3, height=t.height + 0.18)
        bg.set_fill(accent, 0.92).set_stroke(width=0, opacity=0)
        bg.move_to(t)
        self.add(bg, t)


def _bg(scene):
    scene.camera.background_color = GROUND


# ── B02 Paclitaxel mechanism — freeze the spindle ───────────────────────────
class B02_PaclitaxelMechanism(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B02", 8.85)
        cell = Circle(1.8).set_fill(SLATE, 0.10).set_stroke(INK, 2.0)
        cell.move_to(ORIGIN + UP * 0.2)
        # mitotic spindle: two poles + fibers
        pole_l = Dot(radius=0.09, color=INK).move_to(LEFT * 1.3 + UP * 0.2)
        pole_r = Dot(radius=0.09, color=INK).move_to(RIGHT * 1.3 + UP * 0.2)
        fibers = VGroup()
        for y in [-0.35, -0.12, 0.12, 0.35]:
            f = Line(pole_l.get_center(), RIGHT * 0.0 + UP * (0.2 + y),
                     stroke_width=1.5, color=INK).set_stroke(opacity=0.75)
            f2 = Line(pole_r.get_center(), RIGHT * 0.0 + UP * (0.2 + y),
                      stroke_width=1.5, color=INK).set_stroke(opacity=0.75)
            fibers.add(f, f2)
        # paclitaxel drug squares (INK) approach
        drug_positions = [
            LEFT * 0.5 + UP * 0.55, RIGHT * 0.5 + UP * 0.55,
            LEFT * 0.3 + DOWN * 0.15, RIGHT * 0.3 + DOWN * 0.15,
        ]
        drugs = VGroup(*[Square(0.16).set_fill(INK, 0.9).set_stroke(width=0).move_to(p)
                          for p in drug_positions])
        title = Text("Paclitaxel", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        title.move_to(UP * 2.8)
        chip = LabelChip("Division halted", accent=TEAL, size=17)
        chip.move_to(DOWN * 2.3)
        self.play(FadeIn(title), run_time=0.4)
        self.play(GrowFromCenter(cell), run_time=0.5)
        self.play(GrowFromCenter(pole_l), GrowFromCenter(pole_r), run_time=0.3)
        self.play(Create(fibers), run_time=0.9)
        self.play(FadeIn(drugs, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(chip), run_time=0.4)
        self.wait(max(0.3, total - 3.1))


# ── B03 Insolubility — drug clumps in water ─────────────────────────────────
class B03_InsolubilityProblem(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B03", 14.78)
        title = Text("Paclitaxel in water", font=DISPLAY, color=INK, font_size=24, weight=BOLD)
        title.move_to(UP * 2.9)
        # water wave lines
        wave_color = "#A8C0C8"
        waves = VGroup()
        for y in [-1.9, -1.5, -1.1, -0.7, -0.3, 0.1, 0.5, 0.9, 1.3, 1.7]:
            w = Line(LEFT * 5.5 + UP * y, RIGHT * 5.5 + UP * y,
                     stroke_width=0.7, color=wave_color).set_stroke(opacity=0.55)
            waves.add(w)
        # clumped drug particles
        clumps = VGroup()
        positions = [
            LEFT * 1.6 + UP * 0.4, LEFT * 1.2 + UP * 0.1, LEFT * 0.9 + UP * 0.5,
            LEFT * 0.5 + UP * 0.2, LEFT * 0.2 + DOWN * 0.1,
            RIGHT * 0.2 + UP * 0.3, RIGHT * 0.6 + UP * 0.5, RIGHT * 0.9 + DOWN * 0.2,
            RIGHT * 1.3 + UP * 0.2, RIGHT * 1.7 + UP * 0.4,
        ]
        for pos in positions:
            sq = Square(0.22).set_fill(INK, 0.9).set_stroke(width=0).move_to(pos)
            clumps.add(sq)
        chip = LabelChip("Nearly insoluble in water", accent=CRIMSON, size=17)
        chip.move_to(DOWN * 2.6)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(waves), run_time=0.9)
        self.play(FadeIn(clumps, shift=DOWN * 0.15), run_time=0.7)
        # shake — clumps refuse to disperse
        for _ in range(2):
            self.play(clumps.animate.shift(RIGHT * 0.06), run_time=0.15)
            self.play(clumps.animate.shift(LEFT * 0.12), run_time=0.15)
            self.play(clumps.animate.shift(RIGHT * 0.06), run_time=0.15)
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(max(0.3, total - 4.3))


# ── B05 Cremophor triggers hypersensitivity cascade ─────────────────────────
class B05_CremophorCascade(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B05", 17.88)
        title = Text("Cremophor EL", font=DISPLAY, color=CRIMSON, font_size=26, weight=BOLD)
        title.move_to(UP * 2.9)
        # crimson pool at left
        pool = Ellipse(width=2.4, height=0.9).set_fill(CRIMSON, 0.85).set_stroke(width=0)
        pool.move_to(LEFT * 4.2 + DOWN * 0.2)
        pool_lbl = Text("solvent", font=DISPLAY, color=WHITE, font_size=15)
        pool_lbl.move_to(pool.get_center())
        arrow = Arrow(LEFT * 3.0 + DOWN * 0.2, LEFT * 1.3 + DOWN * 0.2,
                      color=CRIMSON, buff=0.1, stroke_width=4)
        # mast cell
        mast = Circle(0.6).set_fill(SLATE, 0.15).set_stroke(INK, 2)
        mast.move_to(LEFT * 0.4 + DOWN * 0.2)
        mast_lbl = Text("mast cell", font=DISPLAY, color=INK, font_size=14)
        mast_lbl.next_to(mast, UP, buff=0.15)
        # radiating crimson lines
        rad_lines = VGroup()
        import math
        for angle_deg in range(0, 360, 30):
            a = math.radians(angle_deg)
            end = mast.get_center() + [math.cos(a) * 1.5, math.sin(a) * 1.5, 0]
            start = mast.get_center() + [math.cos(a) * 0.65, math.sin(a) * 0.65, 0]
            l = Line(start, end, stroke_width=2.5, color=CRIMSON)
            rad_lines.add(l)
        chip1 = LabelChip("Bronchospasm", accent=CRIMSON, size=15)
        chip1.move_to(RIGHT * 3.6 + UP * 0.4)
        chip2 = LabelChip("Hypotension", accent=CRIMSON, size=15)
        chip2.move_to(RIGHT * 3.6 + DOWN * 0.8)
        self.play(FadeIn(title), run_time=0.4)
        self.play(GrowFromCenter(pool), FadeIn(pool_lbl), run_time=0.6)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(GrowFromCenter(mast), FadeIn(mast_lbl), run_time=0.5)
        self.play(Create(rad_lines), run_time=1.0)
        self.play(FadeIn(chip1), run_time=0.4)
        self.play(FadeIn(chip2), run_time=0.4)
        self.wait(max(0.3, total - 3.8))


# ── B07 Albumin binds paclitaxel ────────────────────────────────────────────
class B07_AlbuminBinding(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B07", 18.65)
        title = Text("Albumin binds paclitaxel", font=DISPLAY, color=TEAL, font_size=24, weight=BOLD)
        title.move_to(UP * 2.9)
        # teal folded protein (approximated by rounded blob using arcs)
        albumin = VGroup()
        blob = Circle(1.5).set_fill(TEAL, 0.85).set_stroke(TEAL, 0)
        albumin.add(blob)
        # inner pockets
        for offset in [LEFT * 0.5 + UP * 0.3, RIGHT * 0.5 + UP * 0.4,
                        UP * 0.7, DOWN * 0.5, RIGHT * 0.6 + DOWN * 0.3]:
            pocket = Circle(0.15).set_fill(GROUND, 1).set_stroke(width=0)
            pocket.move_to(offset)
            albumin.add(pocket)
        albumin.move_to(ORIGIN + UP * 0.1)
        # drug molecules approach from right
        drugs = VGroup(*[Square(0.18).set_fill(INK, 0.9).set_stroke(width=0)
                          for _ in range(5)])
        start_positions = [RIGHT * 4.5 + UP * 0.6, RIGHT * 5.0 + DOWN * 0.4,
                            RIGHT * 4.3 + DOWN * 0.9, RIGHT * 5.2 + UP * 1.0,
                            RIGHT * 4.7 + UP * 0.0]
        for d, p in zip(drugs, start_positions):
            d.move_to(p)
        # target positions inside pockets
        target_positions = [LEFT * 0.5 + UP * 0.4, RIGHT * 0.5 + UP * 0.5,
                             UP * 0.8, DOWN * 0.4, RIGHT * 0.6 + DOWN * 0.2]
        chip = LabelChip("Albumin nanoparticle ~130 nm", accent=TEAL, size=17)
        chip.move_to(DOWN * 2.6)
        self.play(FadeIn(title), run_time=0.4)
        self.play(GrowFromCenter(albumin), run_time=0.9)
        self.play(FadeIn(drugs), run_time=0.4)
        anims = [d.animate.move_to(t) for d, t in zip(drugs, target_positions)]
        self.play(*anims, run_time=1.4)
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(max(0.3, total - 3.6))


# ── B08 Solvent drain — CRIMSON leaves, TEAL remains ────────────────────────
class B08_SolventDrain(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B08", 12.99)
        title = Text("Cremophor eliminated", font=DISPLAY, color=INK, font_size=24, weight=BOLD)
        title.move_to(UP * 2.9)
        # crimson pool at left
        pool = Ellipse(width=2.4, height=0.9).set_fill(CRIMSON, 0.85).set_stroke(width=0)
        pool.move_to(LEFT * 3.2 + DOWN * 0.2)
        pool_lbl = Text("Cremophor", font=DISPLAY, color=WHITE, font_size=15)
        pool_lbl.move_to(pool.get_center())
        # teal albumin nanoparticle at right
        nano = Circle(0.9).set_fill(TEAL, 0.85).set_stroke(TEAL, 0)
        nano.move_to(RIGHT * 3.2 + UP * 0.2)
        nano_lbl = Text("Albumin", font=DISPLAY, color=WHITE, font_size=15)
        nano_lbl.move_to(nano.get_center())
        # fading label chips
        fade_chip = LabelChip("Bronchospasm", accent=CRIMSON, size=15)
        fade_chip.move_to(LEFT * 3.2 + UP * 1.2)
        keep_chip = LabelChip("No hypersensitivity", accent=TEAL, size=16)
        keep_chip.move_to(DOWN * 2.6)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(pool), FadeIn(pool_lbl), FadeIn(fade_chip), run_time=0.5)
        self.play(GrowFromCenter(nano), FadeIn(nano_lbl), run_time=0.5)
        # drain: crimson pool drops off screen
        self.play(pool.animate.shift(DOWN * 5.5),
                  pool_lbl.animate.shift(DOWN * 5.5),
                  FadeOut(fade_chip),
                  run_time=1.5)
        self.play(FadeIn(keep_chip), run_time=0.5)
        self.wait(max(0.3, total - 3.4))


# ── B09 Comparison bars — hypersensitivity rate ─────────────────────────────
class B09_ComparisonBars(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B09", 15.51)
        title = Text("Hypersensitivity rate", font=DISPLAY, color=INK,
                     font_size=26, weight=BOLD)
        title.move_to(UP * 2.9)
        # axes-less bar chart
        baseline = Line(LEFT * 4.5 + DOWN * 1.8, RIGHT * 4.5 + DOWN * 1.8,
                        stroke_width=1.5, color=INK)
        # bars
        tax_bar_height = 3.2
        abr_bar_height = 0.28
        tax_bar = Rectangle(width=1.6, height=tax_bar_height).set_fill(CRIMSON, 0.9).set_stroke(width=0)
        tax_bar.move_to(LEFT * 2.0 + DOWN * 1.8 + UP * (tax_bar_height / 2))
        abr_bar = Rectangle(width=1.6, height=abr_bar_height).set_fill(TEAL, 0.9).set_stroke(width=0)
        abr_bar.move_to(RIGHT * 2.0 + DOWN * 1.8 + UP * (abr_bar_height / 2))
        # bar labels (SHORT category nouns beneath baseline)
        tax_lbl = Text("Taxol", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        tax_lbl.move_to(LEFT * 2.0 + DOWN * 2.35)
        abr_lbl = Text("Abraxane", font=DISPLAY, color=TEAL, font_size=20, weight=BOLD)
        abr_lbl.move_to(RIGHT * 2.0 + DOWN * 2.35)
        # numbers ABOVE bar tops (never inside — same-color low-contrast trap)
        tax_bar_top_y = -1.8 + tax_bar_height
        abr_bar_top_y = -1.8 + abr_bar_height
        tax_num = Text("~10%", font=MONO, color=CRIMSON, font_size=36, weight=BOLD)
        tax_num.move_to(LEFT * 2.0 + UP * (tax_bar_top_y + 0.4))
        abr_num = Text("<1%", font=MONO, color=TEAL, font_size=36, weight=BOLD)
        abr_num.move_to(RIGHT * 2.0 + UP * (abr_bar_top_y + 0.4))
        footer = Text("Illustrative comparison — order of magnitude, not clinical trial data.",
                      font=SERIF, color=INK, font_size=15, slant=ITALIC)
        footer.move_to(DOWN * 3.05)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(baseline), FadeIn(tax_lbl), FadeIn(abr_lbl), run_time=0.5)
        self.play(GrowFromEdge(tax_bar, DOWN),
                  GrowFromEdge(abr_bar, DOWN), run_time=1.1)
        self.play(FadeIn(tax_num), FadeIn(abr_num), run_time=0.5)
        self.play(FadeIn(footer), run_time=0.5)
        self.wait(max(0.3, total - 3.0))


# ── B10 Two bags — Bag A (Taxol) detailed ───────────────────────────────────
class B10_TwoBagsSetup(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B10", 16.38)
        title = Text("Two IV bags — same drug", font=DISPLAY, color=INK,
                     font_size=24, weight=BOLD)
        title.move_to(UP * 3.0)
        # shelf line
        shelf = Line(LEFT * 5.5 + DOWN * 0.3, RIGHT * 5.5 + DOWN * 0.3,
                     stroke_width=1.2, color=INK)
        # Bag A (Taxol)
        bagA = RoundedRectangle(width=1.6, height=2.2, corner_radius=0.2)
        bagA.set_fill(CRIMSON, 0.18).set_stroke(CRIMSON, 2.5)
        bagA.move_to(LEFT * 3.2 + UP * 0.9)
        bagA_lbl = Text("Bag A: Taxol", font=DISPLAY, color=CRIMSON,
                        font_size=18, weight=BOLD)
        bagA_lbl.next_to(bagA, UP, buff=0.15)
        # icon column under bag A
        icons_A = VGroup(
            Text("• 6 Cremophor vials", font=DISPLAY, color=INK, font_size=15),
            Text("• Steroid premedication", font=DISPLAY, color=INK, font_size=15),
            Text("• Epinephrine at bedside", font=DISPLAY, color=INK, font_size=15),
            Text("• Filter", font=DISPLAY, color=INK, font_size=15),
            Text("• 3-hour infusion", font=DISPLAY, color=INK, font_size=15),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        icons_A.next_to(bagA, DOWN, buff=0.5).align_to(bagA, LEFT).shift(LEFT * 0.4)
        # Bag B (Abraxane) placeholder
        bagB = RoundedRectangle(width=1.6, height=2.2, corner_radius=0.2)
        bagB.set_fill(TEAL, 0.10).set_stroke(TEAL, 2.5)
        bagB.move_to(RIGHT * 3.2 + UP * 0.9)
        bagB_lbl = Text("Bag B: Abraxane", font=DISPLAY, color=TEAL,
                        font_size=18, weight=BOLD)
        bagB_lbl.next_to(bagB, UP, buff=0.15)
        bagB_wait = Text("…filled in next", font=SERIF, color=INK,
                         font_size=14, slant=ITALIC).set_opacity(0.55)
        bagB_wait.next_to(bagB, DOWN, buff=0.5)
        footer = Text("Same drug — same paclitaxel dose", font=SERIF, color=INK,
                       font_size=16, slant=ITALIC)
        footer.move_to(DOWN * 3.15)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(shelf), run_time=0.3)
        self.play(FadeIn(bagA), FadeIn(bagA_lbl), FadeIn(bagB), FadeIn(bagB_lbl),
                  run_time=0.7)
        self.play(FadeIn(icons_A, shift=UP * 0.1), run_time=1.4)
        self.play(FadeIn(bagB_wait), run_time=0.4)
        self.play(FadeIn(footer), run_time=0.4)
        self.wait(max(0.3, total - 3.2))


# ── B11 Two-column checklist — Taxol vs Abraxane ────────────────────────────
class B11_TwoBagComparison(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B11", 16.43)
        title = Text("What changes", font=DISPLAY, color=INK,
                     font_size=26, weight=BOLD)
        title.move_to(UP * 3.0)
        # left column header
        left_hdr = LabelChip("Taxol", accent=CRIMSON, size=20)
        left_hdr.move_to(LEFT * 3.0 + UP * 2.1)
        right_hdr = LabelChip("Abraxane", accent=TEAL, size=20)
        right_hdr.move_to(RIGHT * 3.0 + UP * 2.1)
        # left bullets
        left_items = VGroup(
            Text("• Cremophor", font=DISPLAY, color=INK, font_size=18),
            Text("• Premedication", font=DISPLAY, color=INK, font_size=18),
            Text("• Epinephrine", font=DISPLAY, color=INK, font_size=18),
            Text("• Filter", font=DISPLAY, color=INK, font_size=18),
            Text("• 3 hours", font=DISPLAY, color=INK, font_size=18),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        left_items.next_to(left_hdr, DOWN, buff=0.5).align_to(left_hdr, LEFT).shift(LEFT * 0.4)
        right_items = VGroup(
            Text("• Albumin", font=DISPLAY, color=INK, font_size=18),
            Text("• No premedication", font=DISPLAY, color=INK, font_size=18),
            Text("• No epinephrine", font=DISPLAY, color=INK, font_size=18),
            Text("• No filter", font=DISPLAY, color=INK, font_size=18),
            Text("• 30 minutes", font=DISPLAY, color=INK, font_size=18),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        right_items.next_to(right_hdr, DOWN, buff=0.5).align_to(right_hdr, LEFT).shift(LEFT * 0.4)
        # divider
        divider = Line(UP * 1.8, DOWN * 2.4, stroke_width=1.0, color=HAIRLINE)
        # footer
        footer = Text("Same drug.", font=SERIF, color=INK, font_size=22, slant=ITALIC)
        footer.move_to(DOWN * 3.15)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(left_hdr), FadeIn(right_hdr), Create(divider), run_time=0.6)
        self.play(FadeIn(left_items, shift=UP * 0.1), run_time=1.1)
        self.play(FadeIn(right_items, shift=UP * 0.1), run_time=1.1)
        self.play(FadeIn(footer), run_time=0.4)
        self.wait(max(0.3, total - 3.6))


# ── B13 Timeline summary — Taxol era vs Abraxane era ────────────────────────
class B13_TimelineSummary(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B13", 14.12)
        title = Text("Two eras — same drug", font=DISPLAY, color=INK,
                     font_size=26, weight=BOLD)
        title.move_to(UP * 3.0)
        # baseline
        baseline = Line(LEFT * 5.5 + DOWN * 1.4, RIGHT * 5.5 + DOWN * 1.4,
                        stroke_width=1.5, color=INK)
        # left zone
        left_zone = Rectangle(width=5.0, height=2.0).set_fill(CRIMSON, 0.10).set_stroke(width=0)
        left_zone.move_to(LEFT * 2.75 + DOWN * 0.4)
        right_zone = Rectangle(width=5.0, height=2.0).set_fill(TEAL, 0.10).set_stroke(width=0)
        right_zone.move_to(RIGHT * 2.75 + DOWN * 0.4)
        # divider
        divider = Line(DOWN * 1.4 + UP * 0.0, UP * 0.6, stroke_width=1.8, color=INK)
        # zone labels
        left_hdr = LabelChip("Taxol era", accent=CRIMSON, size=18)
        left_hdr.move_to(LEFT * 2.75 + UP * 0.9)
        right_hdr = LabelChip("Abraxane era", accent=TEAL, size=18)
        right_hdr.move_to(RIGHT * 2.75 + UP * 0.9)
        left_sub = Text("Cremophor solvent", font=SERIF, color=INK,
                        font_size=17, slant=ITALIC)
        left_sub.move_to(LEFT * 2.75 + DOWN * 0.1)
        right_sub = Text("Albumin carrier", font=SERIF, color=INK,
                         font_size=17, slant=ITALIC)
        right_sub.move_to(RIGHT * 2.75 + DOWN * 0.1)
        left_meta = Text("3 h · premeds · filter", font=MONO, color=CRIMSON, font_size=13)
        left_meta.move_to(LEFT * 2.75 + DOWN * 0.75)
        right_meta = Text("30 min · no premeds", font=MONO, color=TEAL, font_size=13)
        right_meta.move_to(RIGHT * 2.75 + DOWN * 0.75)
        # persistent drug icon spanning both
        drug = Square(0.28).set_fill(INK, 0.9).set_stroke(width=0)
        drug.move_to(DOWN * 1.9)
        drug_lbl = Text("Paclitaxel — identical molecule",
                        font=DISPLAY, color=INK, font_size=15)
        drug_lbl.next_to(drug, RIGHT, buff=0.25)
        drug_group = VGroup(drug, drug_lbl).move_to(DOWN * 1.95)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(left_zone), FadeIn(right_zone), Create(baseline),
                  Create(divider), run_time=0.7)
        self.play(FadeIn(left_hdr), FadeIn(right_hdr), run_time=0.4)
        self.play(FadeIn(left_sub), FadeIn(right_sub), run_time=0.4)
        self.play(FadeIn(left_meta), FadeIn(right_meta), run_time=0.4)
        self.play(FadeIn(drug_group), run_time=0.5)
        self.wait(max(0.3, total - 2.8))


# ── B14 Illustrative example — side by side panels ──────────────────────────
class B14_ExampleSideBySide(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B14", 29.61)
        eyebrow = Text("Illustrative example", font=DISPLAY, color=INK, font_size=15,
                        weight=BOLD).set_opacity(0.75)
        eyebrow.move_to(UP * 3.35)
        title = Text("Same patient — two bags", font=DISPLAY, color=INK,
                     font_size=24, weight=BOLD)
        title.move_to(UP * 2.85)
        # left panel
        left_card = Rectangle(width=5.4, height=4.2).set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.5)
        left_card.move_to(LEFT * 3.1 + DOWN * 0.3)
        left_hdr = LabelChip("Bag A: Taxol", accent=CRIMSON, size=17)
        left_hdr.move_to(left_card.get_top() + DOWN * 0.35)
        left_items = VGroup(
            Text("• 6 Cremophor vials", font=DISPLAY, color=INK, font_size=15),
            Text("• Steroid premedication", font=DISPLAY, color=INK, font_size=15),
            Text("• Antihistamine drip", font=DISPLAY, color=INK, font_size=15),
            Text("• Epinephrine on the table", font=DISPLAY, color=INK, font_size=15),
            Text("• 3-hour infusion + filter", font=DISPLAY, color=INK, font_size=15),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        left_items.move_to(left_card.get_center() + UP * 0.2)
        left_items.align_to(left_card.get_left() + RIGHT * 0.35, LEFT)
        left_chip = LabelChip("~10% hypersensitivity", accent=CRIMSON, size=15)
        left_chip.move_to(left_card.get_bottom() + UP * 0.35)
        # right panel
        right_card = Rectangle(width=5.4, height=4.2).set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        right_card.move_to(RIGHT * 3.1 + DOWN * 0.3)
        right_hdr = LabelChip("Bag B: Abraxane", accent=TEAL, size=17)
        right_hdr.move_to(right_card.get_top() + DOWN * 0.35)
        right_items = VGroup(
            Text("• Albumin nanoparticle", font=DISPLAY, color=INK, font_size=15),
            Text("• No premedication", font=DISPLAY, color=INK, font_size=15),
            Text("• No filter", font=DISPLAY, color=INK, font_size=15),
            Text("• 30-minute infusion", font=DISPLAY, color=INK, font_size=15),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        right_items.move_to(right_card.get_center() + UP * 0.35)
        right_items.align_to(right_card.get_left() + RIGHT * 0.35, LEFT)
        right_chip = LabelChip("<1% hypersensitivity", accent=TEAL, size=15)
        right_chip.move_to(right_card.get_bottom() + UP * 0.35)
        footer = Text("Same drug.", font=SERIF, color=INK,
                       font_size=26, slant=ITALIC, weight=BOLD)
        footer.move_to(DOWN * 3.15)
        self.play(FadeIn(eyebrow), FadeIn(title), run_time=0.5)
        self.play(FadeIn(left_card), FadeIn(right_card), run_time=0.6)
        self.play(FadeIn(left_hdr), FadeIn(right_hdr), run_time=0.4)
        self.play(FadeIn(left_items, shift=UP * 0.1), run_time=1.4)
        self.play(FadeIn(right_items, shift=UP * 0.1), run_time=1.2)
        self.play(FadeIn(left_chip), FadeIn(right_chip), run_time=0.5)
        self.play(FadeIn(footer), run_time=0.5)
        self.wait(max(0.3, total - 5.1))


# ── Batch render helper ──────────────────────────────────────────────────────
SCENES = [
    ("B02_PaclitaxelMechanism", "B02"),
    ("B03_InsolubilityProblem", "B03"),
    ("B05_CremophorCascade",    "B05"),
    ("B07_AlbuminBinding",      "B07"),
    ("B08_SolventDrain",        "B08"),
    ("B09_ComparisonBars",      "B09"),
    ("B10_TwoBagsSetup",        "B10"),
    ("B11_TwoBagComparison",    "B11"),
    ("B13_TimelineSummary",     "B13"),
    ("B14_ExampleSideBySide",   "B14"),
]

if __name__ == "__main__":
    reel = pathlib.Path(__file__).resolve().parent
    manim_dir = reel / "manim"
    manim_dir.mkdir(exist_ok=True)
    failed = []
    for scene_cls, bid in SCENES:
        print(f"[render] {scene_cls} -> manim/{bid}.mp4")
        out_dir = reel / "media" / "videos" / "scenes_std" / "1080p24"
        mp4_src = out_dir / f"{scene_cls}.mp4"
        mp4_dst = manim_dir / f"{bid}.mp4"
        result = subprocess.run(
            [sys.executable, "-m", "manim", "-qh", "--fps", "24",
             "-r", "1920,1080", str(reel / "scenes_std.py"), scene_cls],
            cwd=str(reel), capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"  FAIL: {result.stderr[-500:]}")
            failed.append(scene_cls)
            continue
        if mp4_src.exists():
            import shutil
            shutil.copy2(mp4_src, mp4_dst)
            print(f"  OK -> {mp4_dst}")
        else:
            print(f"  ERROR: output not found at {mp4_src}")
            failed.append(scene_cls)
    if failed:
        print(f"\nFailed scenes: {failed}")
        sys.exit(1)
    print(f"\nAll {len(SCENES)} scenes rendered to manim/")

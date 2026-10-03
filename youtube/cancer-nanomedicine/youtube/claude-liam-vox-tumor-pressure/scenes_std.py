"""scenes_std.py — GRAPHIC beats for claude-liam-vox-tumor-pressure.

Newsprint palette (#F3EBDD ground / #2F2A26 ink / #1F6F5C teal / #BF3339 crimson / #F5D061 gold).
Scenes: B02_MRICore, B04_NaivePicture, B05_PressureBuilds, B06_OutwardFlow,
        B07_ParticlesPushedBack, B08_HypoxicCore, B09_InsideOutQuote, B10_Example.

Semantics: TEAL = drug/particles at rim. CRIMSON = unreached core / outward pressure /
regrowth. GOLD = pressure-gradient highlight (fill only, never text). SLATE = neutral
structural cell fill.

Render each scene:
  manim -qh --fps 24 scenes_std.py B02_MRICore
  mv media/videos/scenes_std/1080p24/B02_MRICore.mp4 manim/B02.mp4

Or use the batch script at the bottom:
  python3 scenes_std.py
"""
import json
import pathlib
import shutil
import subprocess
import sys

from manim import *

# ── Palette (newsprint) ──────────────────────────────────────────────────────
GROUND   = "#F3EBDD"
INK      = "#2F2A26"
TEAL     = "#1F6F5C"
CRIMSON  = "#BF3339"
GOLD     = "#F5D061"
SLATE    = "#3E5559"
HAIRLINE = "#D4D4D4"
GRAY     = "#8A8580"

DISPLAY = "Montserrat"
SERIF   = "EB Garamond"
MONO    = "PT Mono"

# ── Duration loader ──────────────────────────────────────────────────────────
_SHEET = pathlib.Path(__file__).resolve().parent / "beat_sheet.json"
try:
    _data = json.load(open(_SHEET))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}


# ── Helpers ──────────────────────────────────────────────────────────────────
def _bg(scene):
    scene.camera.background_color = GROUND


class LabelChip(VGroup):
    def __init__(self, text, accent=CRIMSON, size=15):
        super().__init__()
        t = Text(text.upper(), font=DISPLAY, color=WHITE, font_size=int(size))
        bg = Rectangle(width=t.width + 0.25, height=t.height + 0.15)
        bg.set_fill(accent, 0.9).set_stroke(width=0, opacity=0)
        bg.move_to(t)
        self.add(bg, t)


# ── B02  MRI schematic — dead rim, viable core ──────────────────────────────
class B02_MRICore(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B02", 10.05)

        title = Text("MRI slice · week 3", font=DISPLAY, font_size=24, color=INK)
        title.move_to(UP * 3.1)

        # Dark drug-killed rim = large SLATE ring; lighter viable core = smaller circle
        rim = Circle(radius=2.0).set_fill(SLATE, 0.85).set_stroke(INK, 1.6)
        core = Circle(radius=0.55).set_fill(GROUND, 1.0).set_stroke(INK, 1.0)
        rim.move_to(LEFT * 1.6)
        core.move_to(rim.get_center())

        # Crimson dashed annotation ring around core
        ann = Circle(radius=0.72).set_stroke(CRIMSON, 2.2)
        ann.move_to(core.get_center())
        # dashed effect
        ann_dashed = DashedVMobject(ann, num_dashes=28, dashed_ratio=0.5)

        # Annotation line + label pointing right
        pt = ann.get_right() + RIGHT * 0.08
        elbow = pt + RIGHT * 1.2
        end = elbow + RIGHT * 0.9
        leader1 = Line(pt, elbow, color=CRIMSON, stroke_width=1.4)
        leader2 = Line(elbow, end, color=CRIMSON, stroke_width=1.4)
        lbl_core = Text("viable core", font=SERIF, color=CRIMSON,
                        font_size=22)
        lbl_core.next_to(end, RIGHT, buff=0.1)
        lbl_sz = Text("≈ 2 mm", font=MONO, color=CRIMSON, font_size=22)
        lbl_sz.next_to(lbl_core, DOWN, buff=0.1, aligned_edge=LEFT)

        # Whole-organ measurement chip on the right
        chip = LabelChip("whole-organ signal", accent=TEAL, size=13)
        chip.move_to(RIGHT * 4.5 + UP * 1.0)
        chip_sub = Text("drug accumulated ✓", font=SERIF, color=TEAL,
                        font_size=22)
        chip_sub.next_to(chip, DOWN, buff=0.15)

        # Contradiction chip
        chip2 = LabelChip("core reality", accent=CRIMSON, size=13)
        chip2.move_to(RIGHT * 4.5 + DOWN * 0.4)
        chip2_sub = Text("untouched, viable ✗", font=SERIF, color=CRIMSON,
                         font_size=22)
        chip2_sub.next_to(chip2, DOWN, buff=0.15)

        self.play(FadeIn(title), run_time=0.4)
        self.play(GrowFromCenter(rim), run_time=0.7)
        self.play(FadeIn(core), run_time=0.5)
        self.play(Create(ann_dashed), run_time=0.6)
        self.play(Create(leader1), Create(leader2), run_time=0.4)
        self.play(FadeIn(lbl_core), FadeIn(lbl_sz), run_time=0.4)
        self.play(FadeIn(chip), FadeIn(chip_sub), run_time=0.5)
        self.play(FadeIn(chip2), FadeIn(chip2_sub), run_time=0.5)
        self.wait(max(0.3, total - 4.0))


# ── B04  Naive picture — leaky vessel + inward diffusion ────────────────────
class B04_NaivePicture(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B04", 11.69)

        title = Text("The naive picture", font=DISPLAY, font_size=22, color=INK)
        title.move_to(UP * 3.1)

        # Vessel: two horizontal lines with two gaps
        y_top, y_bot = 1.9, 1.35
        vessel_pts = [
            (Line(LEFT * 5.5 + UP * y_top, LEFT * 2.0 + UP * y_top,
                  color=INK, stroke_width=2.5)),
            (Line(LEFT * 1.2 + UP * y_top, RIGHT * 1.6 + UP * y_top,
                  color=INK, stroke_width=2.5)),
            (Line(RIGHT * 2.4 + UP * y_top, RIGHT * 5.5 + UP * y_top,
                  color=INK, stroke_width=2.5)),
            (Line(LEFT * 5.5 + UP * y_bot, RIGHT * 5.5 + UP * y_bot,
                  color=INK, stroke_width=2.5)),
        ]
        vessel = VGroup(*vessel_pts)
        vessel_lbl = Text("leaky vessel", font=SERIF, color=INK, font_size=22)
        vessel_lbl.next_to(vessel, UP, buff=0.1, aligned_edge=LEFT).shift(RIGHT * 0.2)

        # Particles inside vessel then escaping through gaps and drifting down
        particles = VGroup()
        for x in [-4.8, -3.8, -2.8, -0.4, 0.6, 3.2, 4.2, 5.0]:
            d = Dot(radius=0.09, color=TEAL).move_to(RIGHT * x + UP * ((y_top + y_bot) / 2))
            particles.add(d)

        # Escaped particles — below the vessel, drifting inward
        escaped = VGroup()
        drops = [(-1.6, 0.4), (-0.6, -0.2), (0.4, 0.1), (2.9, -0.5), (2.0, 0.4), (3.4, 0.0)]
        for (x, y) in drops:
            d = Dot(radius=0.09, color=TEAL).move_to(RIGHT * x + UP * y)
            escaped.add(d)

        inward_lbl = Text("particles diffuse inward", font=SERIF, color=TEAL,
                          font_size=22)
        inward_lbl.move_to(DOWN * 1.4)
        inward_arr = Arrow(UP * 0.1, DOWN * 0.9, color=TEAL, buff=0.0,
                           stroke_width=3, max_tip_length_to_length_ratio=0.15)
        inward_arr.move_to(DOWN * 0.4)

        half_lbl = Text("half the story →", font=DISPLAY, color=CRIMSON,
                        font_size=24, weight=BOLD)
        half_lbl.move_to(DOWN * 2.7 + RIGHT * 3.2)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(vessel), FadeIn(vessel_lbl), run_time=0.7)
        self.play(FadeIn(particles), run_time=0.5)
        self.play(FadeIn(escaped), run_time=0.7)
        self.play(GrowArrow(inward_arr), FadeIn(inward_lbl), run_time=0.6)
        self.play(FadeIn(half_lbl), run_time=0.5)
        self.wait(max(0.3, total - 3.4))


# ── B05  Pressure builds — leaky in, broken lymphatic out ───────────────────
class B05_PressureBuilds(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B05", 11.11)

        title = Text("Fluid in, no drain out", font=DISPLAY, font_size=22, color=INK)
        title.move_to(UP * 3.1)

        # Tumor box (rectangle in the middle)
        box = Rectangle(width=4.6, height=3.0)
        box.set_stroke(INK, 1.8).set_fill(GROUND, 1.0)
        box.move_to(ORIGIN + DOWN * 0.2)

        # Leaky vessel on top pouring fluid drops
        vessel = VGroup(
            Line(box.get_top() + UP * 0.9 + LEFT * 2.0,
                 box.get_top() + UP * 0.9 + RIGHT * 2.0, color=INK, stroke_width=2.5),
            Line(box.get_top() + UP * 1.45 + LEFT * 2.0,
                 box.get_top() + UP * 1.45 + RIGHT * 2.0, color=INK, stroke_width=2.5),
        )
        v_lbl = Text("leaky vessel", font=SERIF, color=INK, font_size=22)
        v_lbl.next_to(vessel, UP, buff=0.1)

        # Fluid drops (teal) falling into the box
        drops = VGroup()
        for x in [-1.5, -0.6, 0.4, 1.3]:
            drops.add(Dot(radius=0.08, color=TEAL).move_to(RIGHT * x + UP * 1.55))
            drops.add(Dot(radius=0.08, color=TEAL).move_to(RIGHT * x + UP * 1.0))

        # Rising fluid inside the box
        fluid_low = Rectangle(width=4.55, height=0.6).set_fill(TEAL, 0.28).set_stroke(width=0)
        fluid_low.move_to(box.get_bottom() + UP * 0.32 + LEFT * 0.02)
        fluid_high = Rectangle(width=4.55, height=1.8).set_fill(TEAL, 0.35).set_stroke(width=0)
        fluid_high.move_to(box.get_bottom() + UP * 0.92 + LEFT * 0.02)

        # Broken lymphatic on bottom-left — a horizontal duct with a red X
        lymph = Line(box.get_bottom() + DOWN * 0.05 + LEFT * 1.1,
                     box.get_bottom() + DOWN * 0.95 + LEFT * 2.6,
                     color=INK, stroke_width=2.5)
        x1 = Line(lymph.get_end() + UP * 0.18 + LEFT * 0.18,
                  lymph.get_end() + DOWN * 0.18 + RIGHT * 0.18,
                  color=CRIMSON, stroke_width=4)
        x2 = Line(lymph.get_end() + UP * 0.18 + RIGHT * 0.18,
                  lymph.get_end() + DOWN * 0.18 + LEFT * 0.18,
                  color=CRIMSON, stroke_width=4)
        l_lbl = Text("broken lymphatic", font=SERIF, color=CRIMSON,
                     font_size=22)
        l_lbl.next_to(x2, DOWN, buff=0.15)

        # Pressure gauge on the right of the box
        gauge_ctr = box.get_right() + RIGHT * 1.35 + UP * 0.4
        gauge = Circle(radius=0.55).set_stroke(INK, 1.6).set_fill(GROUND, 1.0)
        gauge.move_to(gauge_ctr)
        needle_low = Line(gauge_ctr, gauge_ctr + UP * 0.35 + LEFT * 0.35,
                          color=INK, stroke_width=2.5)
        needle_high = Line(gauge_ctr, gauge_ctr + UP * 0.42 + RIGHT * 0.25,
                           color=CRIMSON, stroke_width=3.5)
        g_lbl = Text("pressure ↑", font=DISPLAY, color=CRIMSON,
                     font_size=22, weight=BOLD)
        g_lbl.next_to(gauge, DOWN, buff=0.15)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(box), run_time=0.5)
        self.play(Create(vessel), FadeIn(v_lbl), run_time=0.5)
        self.play(FadeIn(drops), run_time=0.5)
        self.play(Create(lymph), Create(x1), Create(x2), FadeIn(l_lbl), run_time=0.7)
        self.play(FadeIn(fluid_low), run_time=0.4)
        self.play(FadeIn(gauge), Create(needle_low), run_time=0.4)
        self.play(FadeIn(fluid_high), Transform(needle_low, needle_high),
                  FadeIn(g_lbl), run_time=0.9)
        self.wait(max(0.3, total - 4.3))


# ── B06  Outward flow — pressure gradient, radial arrows ────────────────────
class B06_OutwardFlow(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B06", 14.76)

        title = Text("Net flow is outward", font=DISPLAY, font_size=22, color=INK)
        title.move_to(UP * 3.1)

        # Tumor cross-section
        tumor = Circle(radius=2.3).set_stroke(INK, 1.8).set_fill(GROUND, 1.0)
        tumor.move_to(ORIGIN + DOWN * 0.15)

        # Gold radial gradient — approximated with two concentric filled circles
        grad_outer = Circle(radius=2.28).set_fill(GOLD, 0.10).set_stroke(width=0)
        grad_mid = Circle(radius=1.5).set_fill(GOLD, 0.28).set_stroke(width=0)
        grad_inner = Circle(radius=0.8).set_fill(GOLD, 0.55).set_stroke(width=0)
        grad_outer.move_to(tumor.get_center())
        grad_mid.move_to(tumor.get_center())
        grad_inner.move_to(tumor.get_center())

        # Core gauge (25 mmHg)
        gauge_core = Circle(radius=0.28).set_stroke(CRIMSON, 1.6).set_fill(GROUND, 1.0)
        gauge_core.move_to(tumor.get_center())
        gauge_core_lbl = Text("25", font=MONO, font_size=22, color=CRIMSON, weight=BOLD)
        gauge_core_lbl.move_to(gauge_core.get_center())
        core_cap = Text("core: 25 mmHg", font=MONO, font_size=22, color=CRIMSON)
        core_cap.next_to(gauge_core, DOWN, buff=0.2)

        # Rim gauge (5 mmHg) at upper right of tumor
        rim_pt = tumor.get_center() + UP * 1.9 + RIGHT * 0.7
        gauge_rim = Circle(radius=0.24).set_stroke(TEAL, 1.4).set_fill(GROUND, 1.0)
        gauge_rim.move_to(rim_pt)
        gauge_rim_lbl = Text("5", font=MONO, font_size=22, color=TEAL, weight=BOLD)
        gauge_rim_lbl.move_to(rim_pt)
        rim_cap = Text("rim: 5 mmHg", font=MONO, font_size=22, color=TEAL)
        rim_cap.next_to(gauge_rim, UP, buff=0.15)

        # Radial arrows outward (crimson)
        arrows = VGroup()
        import math
        for deg in range(0, 360, 45):
            rad = math.radians(deg)
            start = tumor.get_center() + 0.55 * (RIGHT * math.cos(rad) + UP * math.sin(rad))
            end = tumor.get_center() + 2.05 * (RIGHT * math.cos(rad) + UP * math.sin(rad))
            arrows.add(Arrow(start, end, color=CRIMSON, buff=0.0, stroke_width=3,
                             max_tip_length_to_length_ratio=0.12))

        cap = Text("5–10× normal tissue pressure", font=SERIF, color=INK,
                   font_size=22)
        cap.move_to(DOWN * 3.3)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(tumor), run_time=0.6)
        self.play(FadeIn(grad_outer), FadeIn(grad_mid), FadeIn(grad_inner), run_time=0.7)
        self.play(FadeIn(gauge_core), FadeIn(gauge_core_lbl), FadeIn(core_cap), run_time=0.5)
        self.play(FadeIn(gauge_rim), FadeIn(gauge_rim_lbl), FadeIn(rim_cap), run_time=0.5)
        self.play(AnimationGroup(*[GrowArrow(a) for a in arrows], lag_ratio=0.06),
                  run_time=1.4)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(max(0.3, total - 4.6))


# ── B07  Particles enter at rim, get pushed back out ────────────────────────
class B07_ParticlesPushedBack(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B07", 14.87)

        title = Text("Particles pile at the rim", font=DISPLAY, font_size=22, color=INK)
        title.move_to(UP * 3.1)

        tumor = Circle(radius=2.3).set_stroke(INK, 1.8).set_fill(GROUND, 1.0)
        tumor.move_to(ORIGIN + DOWN * 0.15)

        # Rim vessels — short teal arcs on the outer boundary
        import math
        vessels = VGroup()
        for deg in [30, 100, 170, 240, 310]:
            rad = math.radians(deg)
            pt = tumor.get_center() + 2.32 * (RIGHT * math.cos(rad) + UP * math.sin(rad))
            arc = Arc(radius=0.28, angle=PI * 0.7, color=TEAL, stroke_width=3)
            arc.move_to(pt)
            vessels.add(arc)

        # Particles start at vessels and drift back outward via crimson flow
        # Show final state: dense teal band at periphery, empty core
        band = VGroup()
        for deg in range(0, 360, 12):
            rad = math.radians(deg)
            pt = tumor.get_center() + 1.9 * (RIGHT * math.cos(rad) + UP * math.sin(rad))
            band.add(Dot(radius=0.08, color=TEAL).move_to(pt))
            pt2 = tumor.get_center() + 2.05 * (RIGHT * math.cos(rad + 0.05) + UP * math.sin(rad + 0.05))
            band.add(Dot(radius=0.07, color=TEAL).move_to(pt2))

        # Outward flow arrows (crimson)
        flow = VGroup()
        for deg in [60, 130, 200, 280]:
            rad = math.radians(deg)
            start = tumor.get_center() + 0.6 * (RIGHT * math.cos(rad) + UP * math.sin(rad))
            end = tumor.get_center() + 1.75 * (RIGHT * math.cos(rad) + UP * math.sin(rad))
            flow.add(Arrow(start, end, color=CRIMSON, buff=0.0, stroke_width=2.5,
                           max_tip_length_to_length_ratio=0.14))

        # Empty core label
        core_lbl = Text("core stays\nparticle-free", font=SERIF, color=CRIMSON,
                        font_size=22)
        core_lbl.move_to(tumor.get_center())

        rim_lbl = Text("pile-up at rim", font=SERIF, color=TEAL, font_size=22)
        rim_lbl.move_to(DOWN * 3.05 + LEFT * 2.6)
        cap = Text("EPR succeeded → outward pressure pushed particles back",
                   font=SERIF, color=INK, font_size=22)
        cap.move_to(DOWN * 3.4 + RIGHT * 1.1)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(tumor), run_time=0.6)
        self.play(Create(vessels), run_time=0.5)
        self.play(AnimationGroup(*[GrowArrow(a) for a in flow], lag_ratio=0.15),
                  run_time=0.9)
        self.play(FadeIn(band), run_time=1.0)
        self.play(FadeIn(core_lbl), run_time=0.5)
        self.play(FadeIn(rim_lbl), FadeIn(cap), run_time=0.5)
        self.wait(max(0.3, total - 4.4))


# ── B08  Hypoxic core — selection for resistant cells ───────────────────────
class B08_HypoxicCore(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B08", 14.31)

        title = Text("The core selects for survivors",
                     font=DISPLAY, font_size=22, color=INK)
        title.move_to(UP * 3.1)

        tumor = Circle(radius=2.3).set_stroke(INK, 1.8).set_fill(GROUND, 1.0)
        tumor.move_to(ORIGIN + DOWN * 0.15)

        # Hypoxic core — gray-tinted filled circle
        hypoxic = Circle(radius=1.15).set_fill(GRAY, 0.55).set_stroke(GRAY, 1.2)
        hypoxic.move_to(tumor.get_center())

        # Rim particles (teal — drug reached)
        import math
        rim_pts = VGroup()
        for deg in range(0, 360, 20):
            rad = math.radians(deg)
            pt = tumor.get_center() + 1.95 * (RIGHT * math.cos(rad) + UP * math.sin(rad))
            rim_pts.add(Dot(radius=0.075, color=TEAL).move_to(pt))

        # Oxygen icon crossed out
        o2_pos = tumor.get_center() + UP * 0.65 + LEFT * 0.35
        o2 = Text("O₂", font=DISPLAY, color=GRAY, font_size=22, weight=BOLD)
        o2.move_to(o2_pos)
        o2_slash = Line(o2_pos + UP * 0.25 + LEFT * 0.35,
                        o2_pos + DOWN * 0.25 + RIGHT * 0.35,
                        color=CRIMSON, stroke_width=3)

        # Resistant survivor cells inside the core (crimson)
        surv_pts = [
            (0.2, 0.0), (-0.4, -0.3), (0.4, -0.4), (0.0, 0.3), (-0.2, -0.2), (0.35, 0.15)
        ]
        survivors = VGroup()
        for (dx, dy) in surv_pts:
            c = Dot(radius=0.11, color=CRIMSON).move_to(
                tumor.get_center() + RIGHT * dx + UP * dy)
            survivors.add(c)

        # Labels
        rim_lbl = Text("rim: drug reached", font=SERIF, color=TEAL,
                       font_size=22)
        rim_lbl.move_to(UP * 2.3 + RIGHT * 3.5)
        core_lbl = Text("hypoxic core", font=SERIF, color=GRAY,
                        font_size=22)
        core_lbl.move_to(DOWN * 2.0 + LEFT * 3.3)
        surv_lbl = Text("stress-tolerant · drug-resistant survivors",
                        font=SERIF, color=CRIMSON, font_size=22)
        surv_lbl.move_to(DOWN * 3.35)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(tumor), run_time=0.5)
        self.play(FadeIn(rim_pts), FadeIn(rim_lbl), run_time=0.6)
        self.play(FadeIn(hypoxic), FadeIn(core_lbl), run_time=0.6)
        self.play(FadeIn(o2), Create(o2_slash), run_time=0.5)
        self.play(AnimationGroup(*[GrowFromCenter(s) for s in survivors],
                                 lag_ratio=0.1), run_time=1.0)
        self.play(FadeIn(surv_lbl), run_time=0.5)
        self.wait(max(0.3, total - 4.1))


# ── B09  Inside-out quote — editorial highlight card ────────────────────────
class B09_InsideOutQuote(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B09", 10.45)

        # Line 1
        q1 = Text("The rim cells the drug killed",
                  font=SERIF, color=INK, font_size=34)
        q1.move_to(UP * 1.4)
        q2 = Text("were not the ones most likely to cause recurrence.",
                  font=SERIF, color=INK, font_size=28)
        q2.move_to(UP * 0.55)

        # Line 2
        q3 = Text("The core cells it never reached were —",
                  font=SERIF, color=INK, font_size=32)
        q3.move_to(DOWN * 0.5)
        q4 = Text("and the pressure had spent months making them harder to kill.",
                  font=SERIF, color=INK, font_size=24)
        q4.move_to(DOWN * 1.35)

        # Gold highlighter under the pivotal phrase
        target = Text("The core cells it never reached were —",
                      font=SERIF, color=INK, font_size=32)
        target.move_to(q3.get_center())
        hi = Rectangle(width=target.width + 0.3, height=target.height + 0.15)
        hi.set_fill(GOLD, 0.55).set_stroke(width=0)
        hi.move_to(target.get_center() + DOWN * 0.05)

        # Attribution
        attr = Text("Cancer Nanomedicine · ch. 02",
                    font=MONO, color=GRAY, font_size=22)
        attr.move_to(DOWN * 2.6 + RIGHT * 4.1)

        self.play(FadeIn(q1), run_time=0.4)
        self.play(FadeIn(q2), run_time=0.4)
        self.play(FadeIn(hi), run_time=0.4)
        self.play(FadeIn(q3), run_time=0.5)
        self.play(FadeIn(q4), run_time=0.5)
        self.play(FadeIn(attr), run_time=0.3)
        self.wait(max(0.3, total - 2.5))


# ── B10  Two-panel timeline — week 3 vs week 8 ──────────────────────────────
class B10_Example(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B10", 20.16)

        title = Text("Illustrative scenario · rim shrinks, core wins",
                     font=DISPLAY, font_size=24, color=INK)
        title.move_to(UP * 3.2)

        # Divider
        div = Line(UP * 2.7, DOWN * 3.0, color=INK, stroke_width=0.8)

        # LEFT panel — WEEK 3
        left_hdr = Text("WEEK 3", font=DISPLAY, font_size=22, color=INK, weight=BOLD)
        left_hdr.move_to(LEFT * 3.4 + UP * 2.45)

        # Shrunken tumor with core
        w3_rim = Circle(radius=1.0).set_stroke(TEAL, 1.6).set_fill(TEAL, 0.15)
        w3_rim.move_to(LEFT * 3.4 + UP * 0.75)
        w3_core = Circle(radius=0.38).set_stroke(CRIMSON, 1.5).set_fill(GROUND, 1.0)
        w3_core.move_to(w3_rim.get_center())
        w3_core_ring = DashedVMobject(
            Circle(radius=0.5).set_stroke(CRIMSON, 1.4).move_to(w3_rim.get_center()),
            num_dashes=22)

        w3_rim_lbl = Text("rim −60%", font=MONO, font_size=22, color=TEAL)
        w3_rim_lbl.next_to(w3_rim, RIGHT, buff=0.2)
        w3_core_lbl = Text("core: viable, 2 mm", font=MONO, font_size=22, color=CRIMSON)
        w3_core_lbl.next_to(w3_rim, DOWN, buff=0.35)

        # Two gauges under week 3
        w3_g_core = Text("core IFP: 25 mmHg", font=MONO, font_size=22, color=CRIMSON)
        w3_g_core.move_to(LEFT * 3.4 + DOWN * 1.5)
        w3_g_rim = Text("rim IFP: 5 mmHg", font=MONO, font_size=22, color=TEAL)
        w3_g_rim.next_to(w3_g_core, DOWN, buff=0.18, aligned_edge=LEFT)

        # RIGHT panel — WEEK 8
        right_hdr = Text("WEEK 8", font=DISPLAY, font_size=22, color=INK, weight=BOLD)
        right_hdr.move_to(RIGHT * 3.4 + UP * 2.45)

        # Doubled tumor
        w8_tumor = Circle(radius=1.7).set_stroke(CRIMSON, 1.8).set_fill(CRIMSON, 0.13)
        w8_tumor.move_to(RIGHT * 3.4 + UP * 0.5)
        # Outward arrows radiating from center
        import math
        w8_arrows = VGroup()
        for deg in range(0, 360, 60):
            rad = math.radians(deg)
            start = w8_tumor.get_center() + 0.25 * (RIGHT * math.cos(rad) + UP * math.sin(rad))
            end = w8_tumor.get_center() + 1.55 * (RIGHT * math.cos(rad) + UP * math.sin(rad))
            w8_arrows.add(Arrow(start, end, color=CRIMSON, buff=0.0, stroke_width=2.2,
                                max_tip_length_to_length_ratio=0.15))

        w8_lbl = Text("volume 2×", font=MONO, font_size=22, color=CRIMSON, weight=BOLD)
        w8_lbl.move_to(RIGHT * 3.4 + DOWN * 1.5)
        w8_src = Text("origin: core", font=SERIF, font_size=22, color=CRIMSON)
        w8_src.next_to(w8_lbl, DOWN, buff=0.15)

        footer = Text("illustrative numbers · mouse tumor model",
                      font=SERIF, color=GRAY, font_size=22)
        footer.move_to(DOWN * 3.4)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(div), run_time=0.4)
        self.play(FadeIn(left_hdr), FadeIn(right_hdr), run_time=0.4)
        self.play(Create(w3_rim), Create(w3_core), Create(w3_core_ring), run_time=0.7)
        self.play(FadeIn(w3_rim_lbl), FadeIn(w3_core_lbl), run_time=0.5)
        self.play(FadeIn(w3_g_core), FadeIn(w3_g_rim), run_time=0.6)
        self.play(Create(w8_tumor), run_time=0.6)
        self.play(AnimationGroup(*[GrowArrow(a) for a in w8_arrows], lag_ratio=0.1),
                  run_time=0.9)
        self.play(FadeIn(w8_lbl), FadeIn(w8_src), run_time=0.5)
        self.play(FadeIn(footer), run_time=0.4)
        self.wait(max(0.3, total - 5.4))


# ── Batch render helper ──────────────────────────────────────────────────────
SCENES = [
    ("B02_MRICore",             "B02"),
    ("B04_NaivePicture",        "B04"),
    ("B05_PressureBuilds",      "B05"),
    ("B06_OutwardFlow",         "B06"),
    ("B07_ParticlesPushedBack", "B07"),
    ("B08_HypoxicCore",         "B08"),
    ("B09_InsideOutQuote",      "B09"),
    ("B10_Example",             "B10"),
]

if __name__ == "__main__":
    reel = pathlib.Path(__file__).resolve().parent
    manim_dir = reel / "manim"
    manim_dir.mkdir(exist_ok=True)
    failed = []
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    for scene_cls, bid in SCENES:
        if only and scene_cls not in only and bid not in only:
            continue
        print(f"[render] {scene_cls} → manim/{bid}.mp4")
        out_dir = reel / "media" / "videos" / "scenes_std" / "1080p24"
        mp4_src = out_dir / f"{scene_cls}.mp4"
        mp4_dst = manim_dir / f"{bid}.mp4"
        result = subprocess.run(
            [sys.executable, "-m", "manim", "-qh", "--fps", "24",
             "-r", "1920,1080", str(reel / "scenes_std.py"), scene_cls],
            cwd=str(reel), capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"  FAIL: {result.stderr[-800:]}")
            failed.append(scene_cls)
            continue
        if mp4_src.exists():
            shutil.copy2(mp4_src, mp4_dst)
            print(f"  OK → {mp4_dst}")
        else:
            print(f"  ERROR: output not found at {mp4_src}")
            failed.append(scene_cls)
    if failed:
        print(f"\nFailed scenes: {failed}")
        sys.exit(1)
    else:
        print("\nAll scenes rendered.")

#!/usr/bin/env python3
"""
Manim scenes for claude-liam-simple-patchwork.

Palette: cream #FAF9F5 · ink #3D3929 · terracotta #D97757 (ONE per beat).
Manim CE 0.20.1. No stroke_dash_array on constructors — use DashedVMobject.
"""
from manim import *
import numpy as np

GROUND  = "#FAF9F5"
INK     = "#3D3929"
TERRA   = "#D97757"
HAIRLINE = "#B8B3AA"

DISPLAY = "Montserrat"
SERIF   = "EB Garamond"

config.background_color = GROUND


# ═══════════════════════════════════════════════════════════ shared factories

def _file_image(w=1.9, h=2.4):
    """Image file: cream rect + mountain silhouette (no terracotta — added separately)."""
    border = Rectangle(width=w, height=h, color=INK, stroke_width=2.5)
    border.set_fill(GROUND, 1.0)
    tri = Polygon([-0.52, -0.28, 0], [0, 0.42, 0], [0.52, -0.28, 0],
                  color=INK, fill_color=INK, fill_opacity=0.45, stroke_width=0)
    sun = Dot(radius=0.11, fill_color=INK, fill_opacity=0.40, stroke_width=0)
    tri.move_to(border)
    sun.move_to(border.get_top() + DOWN*0.48 + LEFT*0.38)
    return VGroup(border, tri, sun)

def _file_image_marked(w=1.9, h=2.4):
    """Image file WITH terracotta provenance stamp."""
    base = _file_image(w, h)
    stamp = Dot(radius=0.19, fill_color=TERRA, fill_opacity=1.0, stroke_width=0)
    stamp.move_to(base.get_corner(UR) + LEFT*0.30 + DOWN*0.30)
    return VGroup(base, stamp)

def _file_text(w=1.9, h=2.4):
    """Essay/text file: cream rect + text-line strokes (no terracotta)."""
    border = Rectangle(width=w, height=h, color=INK, stroke_width=2.5)
    border.set_fill(GROUND, 1.0)
    strokes = VGroup(
        Line(LEFT*0.67, RIGHT*0.67, color=INK, stroke_width=2.0),
        Line(LEFT*0.67, RIGHT*0.67, color=INK, stroke_width=2.0),
        Line(LEFT*0.67, RIGHT*0.67, color=INK, stroke_width=2.0),
        Line(LEFT*0.67, RIGHT*0.47, color=INK, stroke_width=2.0),
    ).arrange(DOWN, buff=0.27)
    strokes.move_to(border)
    return VGroup(border, strokes)

def _dashed_rect(w, h, color=INK, stroke_width=2.2, num_dashes=22):
    """Dashed-border rectangle via DashedVMobject. No fill — layer a solid rect behind."""
    r = Rectangle(width=w, height=h, color=color, stroke_width=stroke_width)
    r.set_fill(GROUND, 0.0)
    return DashedVMobject(r, num_dashes=num_dashes)

def _rule_eu(w=3.0, h=2.6):
    """EU rule-shape: image + video + audio + text covered."""
    border = Rectangle(width=w, height=h, color=INK, stroke_width=2.2)
    border.set_fill(GROUND, 1.0)
    hdr = Text("EU", font=DISPLAY, color=INK, font_size=30, weight="BOLD")
    media = VGroup(
        Text("image", font=SERIF, color=INK, font_size=20),
        Text("video", font=SERIF, color=INK, font_size=20),
        Text("audio", font=SERIF, color=INK, font_size=20),
        Text("text",  font=SERIF, color=INK, font_size=20),  # recolored in S06
    ).arrange(DOWN, buff=0.10, aligned_edge=LEFT)
    inner = VGroup(hdr, media).arrange(DOWN, buff=0.20, aligned_edge=LEFT)
    inner.move_to(border)
    return VGroup(border, inner)

def _rule_ca(w=3.0, h=2.6):
    """CA rule-shape: image + video + audio — text slot absent."""
    border = Rectangle(width=w, height=h, color=INK, stroke_width=2.2)
    border.set_fill(GROUND, 1.0)
    hdr = Text("CA", font=DISPLAY, color=INK, font_size=30, weight="BOLD")
    media = VGroup(
        Text("image", font=SERIF, color=INK, font_size=20),
        Text("video", font=SERIF, color=INK, font_size=20),
        Text("audio", font=SERIF, color=INK, font_size=20),
    ).arrange(DOWN, buff=0.10, aligned_edge=LEFT)
    absent = Text("(not text)", font=SERIF, color=HAIRLINE,
                  font_size=18, slant=ITALIC)
    inner = VGroup(hdr, media, absent).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
    inner.move_to(border)
    return VGroup(border, inner)


# ═══════════════════════════════════════════════════════════ S01  6.21 s

class S01_FileWithMark(Scene):
    """Marked file · empty rule-slot. TERRA = stamp on file."""
    def construct(self):
        file_grp = _file_image_marked()
        file_grp.shift(LEFT*2.8)

        slot_border = Rectangle(width=2.8, height=2.8, color=HAIRLINE, stroke_width=1.8)
        slot_border.set_fill(GROUND, 1.0)
        slot_lbl = Text("no rule\napplied here", font=SERIF, color=HAIRLINE,
                        font_size=26, line_spacing=1.2, slant=ITALIC)
        slot_lbl.move_to(slot_border)
        empty_slot = VGroup(slot_border, slot_lbl).shift(RIGHT*2.8)

        self.play(FadeIn(file_grp, shift=UP*0.08), run_time=0.9)
        self.play(FadeIn(empty_slot, shift=UP*0.08), run_time=0.7)
        self.wait(4.62)


# ═══════════════════════════════════════════════════════════ S02  3.75 s

class S02_HeldMark(Scene):
    """Hold: mark present, rule absent. TERRA = stamp on file."""
    def construct(self):
        file_grp = _file_image_marked()
        file_grp.shift(LEFT*2.8)

        slot_border = Rectangle(width=2.8, height=2.8, color=HAIRLINE, stroke_width=1.8)
        slot_border.set_fill(GROUND, 1.0)
        slot_lbl = Text("no rule\napplied here", font=SERIF, color=HAIRLINE,
                        font_size=26, line_spacing=1.2, slant=ITALIC)
        slot_lbl.move_to(slot_border)
        empty_slot = VGroup(slot_border, slot_lbl).shift(RIGHT*2.8)

        self.add(file_grp, empty_slot)
        self.wait(3.75)


# ═══════════════════════════════════════════════════════════ S03  5.38 s
# THE ANCHOR — exact layout returns at S13

class S03_TheAnchor(Scene):
    """THE ANCHOR: image file + essay file, shared timestamp. TERRA = timestamp."""
    def construct(self):
        img_f = _file_image()
        txt_f = _file_text()
        pair  = VGroup(img_f, txt_f).arrange(RIGHT, buff=1.2)
        pair.move_to(UP * 0.5)

        ts = Text("same session · same afternoon", font=SERIF,
                  color=TERRA, font_size=26)    # TERRA accent
        ts.next_to(pair, DOWN, buff=0.55)

        self.play(FadeIn(pair, shift=UP*0.08), run_time=0.9)
        self.play(FadeIn(ts, shift=UP*0.06), run_time=0.6)
        self.wait(3.88)


# ═══════════════════════════════════════════════════════════ S04  5.42 s

class S04_BrusselsEffect(Scene):
    """Brussels-effect: one rule radiating globally. TERRA = radiating arrows."""
    def construct(self):
        globe = Circle(radius=1.35, color=INK, stroke_width=2.0)
        globe.set_fill(GROUND, 1.0)

        L = 1.85
        dirs_eu = [UP*L, normalize(UR)*L, RIGHT*L, normalize(DR)*L,
                   DOWN*L, normalize(DL)*L, LEFT*L, normalize(UL)*L]
        rays = VGroup(*[
            Arrow(start=np.array([0,0,0]), end=np.array([d[0], d[1], 0]),
                  color=TERRA, stroke_width=2.2, buff=0, max_tip_length_to_length_ratio=0.18)
            for d in dirs_eu
        ])

        lbl = Text("one rule · everywhere", font=SERIF, color=INK,
                   font_size=28, slant=ITALIC)
        lbl.to_edge(UP, buff=0.65)

        self.play(FadeIn(lbl), FadeIn(globe), run_time=0.8)
        self.play(LaggedStart(*[Create(r) for r in rays],
                              lag_ratio=0.08, run_time=1.6))
        self.wait(3.02)


# ═══════════════════════════════════════════════════════════ S05  7.53 s

class S05_RuleContracts(Scene):
    """EU rule contracts to its nexus. TERRA = nexus boundary circle."""
    def construct(self):
        globe = Circle(radius=2.0, color=INK, stroke_width=2.0)
        globe.set_fill(GROUND, 1.0)

        dirs = [UP, normalize(UR), RIGHT, normalize(DR),
                DOWN, normalize(DL), LEFT, normalize(UL)]
        rays = VGroup(*[
            Arrow(start=[0,0,0], end=[d[0]*2.2, d[1]*2.2, 0],
                  color=HAIRLINE, stroke_width=2.0, buff=0, max_tip_length_to_length_ratio=0.15)
            for d in dirs
        ])

        nexus = Circle(radius=0.90, color=TERRA, stroke_width=3.0)
        nexus.set_fill(TERRA, 0.11)
        nexus_lbl = Text("EU nexus", font=SERIF, color=TERRA, font_size=23)
        nexus_lbl.next_to(nexus, DOWN, buff=0.30)

        note = Text("most files not covered", font=SERIF,
                    color=INK, font_size=26, slant=ITALIC)
        note.to_edge(UP, buff=0.65)

        self.add(globe, rays)
        self.play(FadeIn(note), run_time=0.6)
        self.play(FadeOut(rays), run_time=1.4)
        self.play(FadeIn(nexus), FadeIn(nexus_lbl), run_time=0.9)
        self.wait(4.63)


# ═══════════════════════════════════════════════════════════ S06  5.95 s
# THE RULE-SHAPES — same pair reused in S07 and S14

class S06_TwoRuleShapes(Scene):
    """EU covers text · CA doesn't. TERRA = 'text' item under EU shape."""
    def construct(self):
        eu = _rule_eu().shift(LEFT*2.8)
        ca = _rule_ca().shift(RIGHT*2.8)
        # eu[1] = VGroup(hdr, media_vgroup); eu[1][1] = media; eu[1][1][3] = 'text'
        try:
            eu[1][1][3].set_color(TERRA)
        except Exception:
            pass

        hdr_eu = Text("European Union", font=SERIF, color=INK,
                      font_size=24, slant=ITALIC)
        hdr_ca = Text("California", font=SERIF, color=INK,
                      font_size=24, slant=ITALIC)
        hdr_eu.next_to(eu, UP, buff=0.35)
        hdr_ca.next_to(ca, UP, buff=0.35)

        self.play(FadeIn(eu, shift=UP*0.08), FadeIn(hdr_eu), run_time=0.9)
        self.play(FadeIn(ca, shift=UP*0.08), FadeIn(hdr_ca), run_time=0.7)
        self.wait(4.35)


# ═══════════════════════════════════════════════════════════ S07  5.25 s

class S07_OutOfRegister(Scene):
    """Same two rule-shapes, overlaid and offset. TERRA = gap/offset seam."""
    def construct(self):
        eu = _rule_eu()
        ca = _rule_ca()

        eu.move_to(LEFT*0.55 + UP*0.32)
        ca.move_to(RIGHT*0.55 + DOWN*0.32)
        ca.set_opacity(0.70)

        # TERRA seam between the two misaligned shapes
        seam = DashedLine(
            start=LEFT*4.5 + UP*0.0, end=RIGHT*4.5 + UP*0.0,
            color=TERRA, stroke_width=2.8, dash_length=0.18, dashed_ratio=0.5
        )

        note = Text("do not agree", font=SERIF, color=INK,
                    font_size=26, slant=ITALIC)
        note.to_edge(DOWN, buff=0.70)

        self.play(FadeIn(eu), run_time=0.7)
        self.play(FadeIn(ca), run_time=0.7)
        self.play(Create(seam), FadeIn(note), run_time=0.8)
        self.wait(3.05)


# ═══════════════════════════════════════════════════════════ S08  2.82 s

class S08_Patchwork(Scene):
    """Several rule-shapes scattered: the patchwork. TERRA = outline of one shape."""
    def construct(self):
        specs = [
            (UP*1.65 + LEFT*3.8,  2.2, 1.4, INK),
            (UP*1.65 + LEFT*0.5,  1.8, 1.6, INK),
            (UP*1.65 + RIGHT*3.2, 2.4, 1.3, TERRA),   # the ONE terra shape
            (DOWN*0.95 + LEFT*2.8, 2.0, 1.4, INK),
            (DOWN*0.95 + RIGHT*1.6, 1.8, 1.5, INK),
        ]
        shapes = []
        for pos, w, h, col in specs:
            r = Rectangle(width=w, height=h, color=col, stroke_width=2.2)
            r.set_fill(GROUND, 1.0).move_to(pos)
            shapes.append(r)

        lbl = Text("patchwork", font=SERIF, color=INK, font_size=44,
                   weight="BOLD")
        lbl.to_edge(UP, buff=0.45)

        self.play(FadeIn(lbl), LaggedStart(*[FadeIn(s) for s in shapes],
                                           lag_ratio=0.10, run_time=1.3))
        self.wait(1.52)


# ═══════════════════════════════════════════════════════════ S09  5.44 s

class S09_FourColumns(Scene):
    """Four columns fill in: WHO / WHAT / WHEN / WHERE. TERRA = WHERE header."""
    HEADERS = ["WHO", "WHAT", "WHEN", "WHERE"]
    ROWS = [
        ["maker",   "image+video+…", "varies",  "varies"],
        ["host",    "image+video",   "varies",  "varies"],
        ["any",     "audio",         "varies",  "varies"],
    ]

    def construct(self):
        col_x = [-5.0, -1.7, 1.4, 4.7]
        hdrs  = []
        for i, (h, x) in enumerate(zip(self.HEADERS, col_x)):
            t = Text(h, font=DISPLAY, color=INK, font_size=32, weight="BOLD")
            t.move_to([x, 2.8, 0])
            hdrs.append(t)

        # TERRA underline beneath WHERE header is the ONE accent
        terra_ul = Line([col_x[3]-0.72, 2.47, 0], [col_x[3]+0.72, 2.47, 0],
                         color=TERRA, stroke_width=4.0)

        rule = Line([-6.4, 2.2, 0], [6.4, 2.2, 0], color=INK, stroke_width=1.5)

        row_mobs = []
        for ri, row in enumerate(self.ROWS):
            r_grp = VGroup()
            for ci, (cell, x) in enumerate(zip(row, col_x)):
                t = Text(cell, font=SERIF, color=INK, font_size=28)
                t.move_to([x, 1.2 - ri*1.05, 0])
                r_grp.add(t)
            row_mobs.append(r_grp)

        self.play(LaggedStart(*[FadeIn(h) for h in hdrs], lag_ratio=0.15, run_time=1.0))
        self.play(Create(terra_ul), Create(rule), run_time=0.4)
        for r in row_mobs:
            self.play(FadeIn(r, shift=UP*0.05), run_time=0.55)
        self.wait(1.84)


# ═══════════════════════════════════════════════════════════ S10  6.34 s

class S10_OneFileThreeDuties(Scene):
    """One file · three duty-points (maker, host, advertiser). TERRA = host label."""
    def construct(self):
        file_grp = _file_image()
        file_grp.scale(0.72).move_to(LEFT*5.4)

        # ring_color, lbl_color kept separate so HOST circle stays TERRA (the ONE accent)
        # while HOST label uses INK on cream for WCAG contrast
        parties = [("MAKER", INK, INK, -1.6), ("HOST", TERRA, INK, 1.6), ("ADVERTISER", INK, INK, 4.8)]
        party_grps = []
        for name, ring_color, lbl_color, x in parties:
            circle = Circle(radius=0.52, color=ring_color, stroke_width=2.5)
            circle.set_fill(GROUND, 1.0).move_to([x, 0, 0])
            lbl = Text(name, font=DISPLAY, color=lbl_color, font_size=36, weight="BOLD")
            lbl.next_to(circle, DOWN, buff=0.28)
            party_grps.append(VGroup(circle, lbl))

        arrows = []
        for x in [-1.6, 1.6, 4.8]:
            arrows.append(Arrow(start=[x-1.25, 0, 0], end=[x-0.55, 0, 0],
                               color=INK, stroke_width=2.0, buff=0,
                               max_tip_length_to_length_ratio=0.25))

        note = Text("different duty at each point", font=SERIF,
                    color=INK, font_size=40, slant=ITALIC)
        note.to_edge(DOWN, buff=0.65)

        self.play(FadeIn(file_grp), run_time=0.6)
        for arrow, pg in zip(arrows, party_grps):
            self.play(Create(arrow), FadeIn(pg), run_time=0.65)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.99)


# ═══════════════════════════════════════════════════════════ S11  8.21 s

class S11_FederalSlotEmpty(Scene):
    """Federal slot empty. TERRA = strikethrough on the revoked rule."""
    def construct(self):
        slot = _dashed_rect(4.4, 2.8, color=INK, stroke_width=2.2, num_dashes=28)
        slot.set_fill(GROUND, 1.0).move_to(LEFT*1.0)
        slot_inner = Rectangle(width=4.4, height=2.8, stroke_width=0)
        slot_inner.set_fill(GROUND, 1.0).move_to(LEFT*1.0)
        slot_lbl = Text("FEDERAL RULE", font=DISPLAY, color=HAIRLINE,
                        font_size=32, weight="BOLD")
        slot_lbl.move_to(LEFT*1.0 + UP*0.25)
        empty_txt = Text("(none)", font=SERIF, color=HAIRLINE,
                         font_size=26, slant=ITALIC)
        empty_txt.move_to(LEFT*1.0 + DOWN*0.5)

        # revoked: struck-through
        rev_border = Rectangle(width=2.2, height=1.4, color=HAIRLINE, stroke_width=1.5)
        rev_border.set_fill(GROUND, 1.0).move_to(RIGHT*4.1 + UP*0.7)
        rev_lbl = Text("EO 14110", font=SERIF, color=HAIRLINE, font_size=20)
        rev_lbl.move_to(rev_border)
        strike = Line(rev_border.get_corner(UL), rev_border.get_corner(DR),
                      color=TERRA, stroke_width=3.5)  # TERRA accent

        # bill that didn't pass
        unf_border = Rectangle(width=2.2, height=1.4, color=HAIRLINE, stroke_width=1.5)
        unf_border.set_fill(GROUND, 1.0).set_opacity(0.5)
        unf_border.move_to(RIGHT*4.1 + DOWN*1.0)
        unf_lbl = Text("S.2765\nnot passed", font=SERIF, color=HAIRLINE,
                       font_size=18, line_spacing=1.1)
        unf_lbl.move_to(unf_border).set_opacity(0.5)

        self.play(FadeIn(slot_inner), FadeIn(slot), run_time=0.5)
        self.play(FadeIn(slot_lbl), FadeIn(empty_txt), run_time=0.8)
        self.play(FadeIn(rev_border), FadeIn(rev_lbl), run_time=0.7)
        self.play(Create(strike), run_time=0.7)
        self.play(FadeIn(unf_border), FadeIn(unf_lbl), run_time=0.7)
        self.wait(4.81)


# ═══════════════════════════════════════════════════════════ S12  12.44 s

class S12_TheOneFlag(Scene):
    """THE ONE FLAG: cheap-pipeline hypothesis inside dotted border. TERRA = FLAG chip."""
    def construct(self):
        # Dotted border = the reel's one hedge
        inner = Rectangle(width=9.0, height=3.6, stroke_width=0)
        inner.set_fill(GROUND, 1.0).move_to(ORIGIN)
        box = _dashed_rect(9.0, 3.6, color=INK, stroke_width=2.0, num_dashes=40)
        box.move_to(ORIGIN)

        line1 = Text("one pipeline is cheaper than", font=SERIF, color=INK, font_size=34)
        line2 = Text("sorting users by location", font=SERIF, color=INK, font_size=34)
        explanation = VGroup(line1, line2).arrange(DOWN, buff=0.22)
        explanation.move_to(ORIGIN + UP*0.15)

        caption = Text("reasonable · undocumented", font=SERIF,
                       color=HAIRLINE, font_size=25, slant=ITALIC)
        caption.next_to(explanation, DOWN, buff=0.55)

        # TERRA flag chip (the one terracotta accent)
        flag_text = Text("FLAG", font=DISPLAY, color=GROUND,
                         font_size=24, weight="BOLD")
        flag_bg = Rectangle(
            width=flag_text.width + 0.42,
            height=flag_text.height + 0.30,
            color=TERRA, fill_color=TERRA, fill_opacity=1.0, stroke_width=0
        )
        flag_bg.move_to(box.get_corner(UR) + LEFT*0.82 + DOWN*0.50)
        flag_text.move_to(flag_bg)
        flag_chip = VGroup(flag_bg, flag_text)

        header = Text("one flag on this reel", font=SERIF, color=INK,
                      font_size=26, slant=ITALIC)
        header.to_edge(UP, buff=0.55)

        self.play(FadeIn(header), run_time=0.6)
        self.play(FadeIn(inner), FadeIn(box), run_time=0.7)
        self.play(FadeIn(explanation, shift=UP*0.06), run_time=0.9)
        self.play(FadeIn(caption), run_time=0.6)
        self.play(FadeIn(flag_chip, scale=1.12), run_time=0.8)
        self.wait(8.77)


# ═══════════════════════════════════════════════════════════ S13  7.32 s
# THE ANCHOR RETURNS — identical layout to S03, ONE change: TERRA stamp on image

class S13_AnchorReturns(Scene):
    """THE ANCHOR RETURNS — S03 composition + terracotta mark on image. TERRA = stamp."""
    def construct(self):
        img_f = _file_image_marked()    # TERRA stamp (the ONE accent)
        txt_f = _file_text()
        pair  = VGroup(img_f, txt_f).arrange(RIGHT, buff=1.2)
        pair.move_to(UP * 0.5)

        ts = Text("same session · same afternoon", font=SERIF,
                  color=INK, font_size=26)   # timestamp in INK (stamp is the TERRA)
        ts.next_to(pair, DOWN, buff=0.55)

        img_note = Text("marked", font=SERIF, color=INK,
                        font_size=23, slant=ITALIC)
        txt_note = Text("not marked", font=SERIF, color=INK,
                        font_size=23, slant=ITALIC)
        img_note.next_to(img_f, UP, buff=0.28)
        txt_note.next_to(txt_f, UP, buff=0.28)

        self.play(FadeIn(pair, shift=UP*0.08), run_time=0.9)
        self.play(FadeIn(ts, shift=UP*0.06), run_time=0.5)
        self.play(FadeIn(img_note), FadeIn(txt_note), run_time=0.7)
        self.wait(5.17)


# ═══════════════════════════════════════════════════════════ S14  5.89 s

class S14_TwoFilesRules(Scene):
    """Two files held · two rules pointing. TERRA = rule arrows."""
    def construct(self):
        img_f = _file_image()
        txt_f = _file_text()
        pair  = VGroup(img_f, txt_f).arrange(RIGHT, buff=1.2)
        pair.move_to(UP*1.5).scale(0.72)

        eu = _rule_eu().scale(0.70).move_to(LEFT*2.6 + DOWN*1.2)
        ca = _rule_ca().scale(0.70).move_to(RIGHT*2.6 + DOWN*1.2)

        eu_top    = eu.get_top()
        ca_top    = ca.get_top()
        img_btm   = pair[0].get_bottom()
        txt_btm   = pair[1].get_bottom()

        arrow_eu = Arrow(eu_top, img_btm + DOWN*0.12,
                         color=TERRA, stroke_width=2.8, buff=0.08,
                         max_tip_length_to_length_ratio=0.15)
        arrow_ca = Arrow(ca_top, txt_btm + DOWN*0.12,
                         color=TERRA, stroke_width=2.8, buff=0.08,
                         max_tip_length_to_length_ratio=0.15)

        note = Text("never one rule", font=SERIF, color=INK,
                    font_size=26, slant=ITALIC)
        note.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(pair, shift=UP*0.08), run_time=0.7)
        self.play(FadeIn(eu), FadeIn(ca), run_time=0.7)
        self.play(Create(arrow_eu), Create(arrow_ca), run_time=0.9)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(3.08)


# ═══════════════════════════════════════════════════════════ S15  5.50 s

class S15_DirectionA(Scene):
    """MARK PRESENT → 'A LAW REQUIRED THIS' struck through. TERRA = strikethrough only."""
    def construct(self):
        file_grp = _file_image()   # bare — stamp removed; strikethrough is the ONE TERRA
        file_grp.scale(0.85).move_to(UP*1.4)

        mark_lbl = Text("MARK PRESENT", font=DISPLAY, color=INK,
                        font_size=30, weight="BOLD")
        mark_lbl.next_to(file_grp, UP, buff=0.35)

        arrow = Arrow(start=file_grp.get_bottom() + DOWN*0.05,
                      end=file_grp.get_bottom() + DOWN*0.95,
                      color=INK, stroke_width=2.0, buff=0,
                      max_tip_length_to_length_ratio=0.22)

        conclusion = Text("A LAW REQUIRED THIS", font=SERIF, color=INK, font_size=30)
        conclusion.next_to(arrow.get_end(), DOWN, buff=0.15)

        strike = Line(conclusion.get_corner(UL) + LEFT*0.05,
                      conclusion.get_corner(UR) + RIGHT*0.05,
                      color=TERRA, stroke_width=4.0)   # TERRA accent

        self.play(FadeIn(file_grp), FadeIn(mark_lbl), run_time=0.7)
        self.play(Create(arrow), run_time=0.5)
        self.play(FadeIn(conclusion), run_time=0.6)
        self.play(Create(strike), run_time=0.7)
        self.wait(3.03)


# ═══════════════════════════════════════════════════════════ S16  7.08 s

class S16_DirectionB(Scene):
    """NO MARK → 'NO RULE APPLIES' struck through. Mirrors S15. TERRA = strikethrough."""
    def construct(self):
        file_grp = _file_image()        # bare — no mark
        file_grp.scale(0.85).move_to(UP*1.4)

        no_mark_lbl = Text("NO MARK", font=DISPLAY, color=INK,
                           font_size=30, weight="BOLD")
        no_mark_lbl.next_to(file_grp, UP, buff=0.35)

        arrow = Arrow(start=file_grp.get_bottom() + DOWN*0.05,
                      end=file_grp.get_bottom() + DOWN*0.95,
                      color=INK, stroke_width=2.0, buff=0,
                      max_tip_length_to_length_ratio=0.22)

        conclusion = Text("NO RULE APPLIES", font=SERIF, color=INK, font_size=30)
        conclusion.next_to(arrow.get_end(), DOWN, buff=0.15)

        strike = Line(conclusion.get_corner(UL) + LEFT*0.05,
                      conclusion.get_corner(UR) + RIGHT*0.05,
                      color=TERRA, stroke_width=4.0)   # TERRA accent

        dn1 = Text("platform duty may still attach", font=SERIF, color=INK,
                   font_size=24, slant=ITALIC)
        dn2 = Text("long after the file leaves", font=SERIF, color=INK,
                   font_size=24, slant=ITALIC)
        duty_note = VGroup(dn1, dn2).arrange(DOWN, buff=0.14)
        duty_note.to_edge(DOWN, buff=0.60)

        self.play(FadeIn(file_grp), FadeIn(no_mark_lbl), run_time=0.7)
        self.play(Create(arrow), run_time=0.5)
        self.play(FadeIn(conclusion), run_time=0.6)
        self.play(Create(strike), run_time=0.7)
        self.play(FadeIn(duty_note, shift=UP*0.06), run_time=0.6)
        self.wait(3.98)

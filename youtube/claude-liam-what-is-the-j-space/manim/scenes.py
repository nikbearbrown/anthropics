"""Manim scenes — claude-liam-what-is-the-j-space
Simple 'What is' explainer. Claude stage: cream #FAF9F5, ink #3D3929,
terracotta #D97757, mute #8B7355. LAYOUT LAW + STAGE LAYOUT LAW bind.
4K-safe from authoring: text >= 24, mono uppercase, no stray %/~ runs,
everything inside |x| <= 6.1 title-safe.
"""
from manim import *
import numpy as np, os

CREAM="#FAF9F5"; INK="#3D3929"; TERRA="#D97757"; MUTE="#8B7355"; GRAY="#A89F91"
config.background_color = CREAM
config.frame_rate = 24
config.pixel_height = int(os.environ.get("ART_MANIM_H","1080"))
config.pixel_width  = int(os.environ.get("ART_MANIM_W","1920"))

def _t(s,size=34,color=INK,**kw):
    return Text(s.replace(" ","  "),color=color,font_size=size,font="EB Garamond",**kw)
def _mono(s,size=24,color=MUTE,**kw):
    return Text(s,color=color,font_size=size,font="Menlo",**kw)
def _box(c,h_pad=0.28,v_pad=0.2,stroke=INK,sw=2.0,fill=CREAM,corner=0.12):
    r=RoundedRectangle(corner_radius=corner,width=c.width+2*h_pad,height=c.height+2*v_pad,
                       color=stroke,stroke_width=sw,fill_color=fill,fill_opacity=1)
    r.move_to(c); return VGroup(r,c)
def _rule(scene):
    r=Line(LEFT*6,RIGHT*6,color=INK,stroke_width=2).set_stroke(opacity=0.3)
    r.to_edge(DOWN,buff=0.53); scene.add(r); return r
def _clamp(m,lim=6.1):
    if m.get_right()[0]>lim: m.shift(LEFT*(m.get_right()[0]-lim))
    if m.get_left()[0]<-lim: m.shift(RIGHT*(-lim-m.get_left()[0]))
    return m
def check_overlaps(*mobs,margin=0.12,label=""):
    bb=lambda m:(m.get_left()[0],m.get_bottom()[1],m.get_right()[0],m.get_top()[1])
    v=[]
    for i,a in enumerate(mobs):
        la,ba,ra,ta=bb(a)
        for j,b in enumerate(mobs):
            if j<=i: continue
            lb,bb_,rb,tb=bb(b)
            if la<rb+margin and ra>lb-margin and ba<tb+margin and ta>bb_-margin:
                v.append(f"  {i}x{j}")
    print(f"[BBOX {label}] "+("OK" if not v else f"{len(v)} overlap(s):\n"+"\n".join(v)))

def _ledger(rows,size=26,buff=0.42):
    out=VGroup()
    for k,v in rows:
        key=_t(k,size=size,color=MUTE)
        val=v if isinstance(v,Mobject) else _t(str(v),size=size)
        out.add(VGroup(key,val).arrange(RIGHT,buff=0.32))
    out.arrange(DOWN,buff=buff,aligned_edge=LEFT); return out


class B02_ResidualStream(Scene):
    """12.31s — the scratch vector climbs the stack; the ledger counts layers."""
    def construct(self):
        _rule(self)
        n=12
        bars=VGroup(*[Rectangle(width=3.4,height=0.22,color=INK,stroke_width=1.5,
                     fill_color=CREAM,fill_opacity=1) for _ in range(n)])
        bars.arrange(UP,buff=0.14).move_to(LEFT*2.6+DOWN*0.2)
        self.play(LaggedStart(*[FadeIn(b) for b in bars],lag_ratio=0.06),run_time=1.2)
        chip=_box(_t("scratch",size=24),h_pad=0.14,v_pad=0.09,sw=1.5)
        chip.next_to(bars[0],LEFT,buff=0.3)
        self.play(FadeIn(chip),run_time=0.5)
        layer=Integer(1,color=INK,font_size=48)
        led=_ledger([("LAYER",layer),("OUTPUT",_t("?",size=30,color=TERRA))],size=26,buff=0.55)
        lbox=SurroundingRectangle(led,color=INK,stroke_width=2,buff=0.4,corner_radius=0.12)
        grp=VGroup(lbox,led); grp.move_to(RIGHT*4.3+UP*0.6); _clamp(grp)
        self.play(FadeIn(grp),run_time=0.6)
        tr=ValueTracker(0)
        layer.add_updater(lambda m: m.set_value(1+int(tr.get_value())))
        chip.add_updater(lambda m: m.next_to(bars[min(n-1,int(tr.get_value()))],LEFT,buff=0.3))
        self.play(tr.animate.set_value(n-1),run_time=4.0,rate_func=linear)
        chip.clear_updaters(); layer.clear_updaters()
        ans=_box(_t("answer",size=24),h_pad=0.16,v_pad=0.1)
        ans.next_to(bars[-1],UP,buff=0.25)
        self.play(FadeIn(ans,shift=UP*0.15),run_time=0.6)
        br=Brace(VGroup(*bars[4:8]),RIGHT,color=TERRA)
        tag=VGroup(_t("what is written",size=26,color=TERRA),
                   _t("HERE?",size=26,color=TERRA)).arrange(DOWN,buff=0.12,aligned_edge=LEFT)
        tag.next_to(br,RIGHT,buff=0.25)
        self.play(GrowFromCenter(br),FadeIn(tag),run_time=1.0)
        self.wait(3.4)
        check_overlaps(bars,ans,grp,tag,label="B02")


class B03_OneGradientPerWord(Scene):
    """15.02s — three word-tagged directions grow; the dictionary ledger fills."""
    def construct(self):
        _rule(self)
        plane=RoundedRectangle(corner_radius=0.15,width=4.6,height=2.9,color=INK,
                               stroke_width=2,fill_color=CREAM,fill_opacity=1)
        plane.move_to(LEFT*3.3+UP*0.4)
        pl=_t("one layer's activations",size=24,color=MUTE).next_to(plane,DOWN,buff=0.3)
        self.play(Create(plane),FadeIn(pl),run_time=1.1)
        words=["orange","twenty-one","safe"]; dirs=[UR,UP,RIGHT]
        rows=[]
        led=VGroup(); arrows=VGroup()
        base=plane.get_center()
        for w,d in zip(words,dirs):
            a=Arrow(base,base+d*1.5,color=INK,stroke_width=3,tip_length=0.16,buff=0.1)
            tag=_t(w,size=24).next_to(a.get_end(),d,buff=0.12); _clamp(tag)
            arrows.add(VGroup(a,tag))
        # ledger right
        for w in words:
            glyph=Arrow(ORIGIN,RIGHT*0.6,color=INK,stroke_width=2.5,tip_length=0.12,buff=0)
            rows.append((w.upper(),glyph))
        led=_ledger(rows,size=24,buff=0.42)
        hdr=VGroup(_t("WORD",size=24,color=MUTE),_t("DIRECTION",size=24,color=MUTE)).arrange(RIGHT,buff=0.9)
        panel=VGroup(hdr,led).arrange(DOWN,buff=0.4,aligned_edge=LEFT)
        pbox=SurroundingRectangle(panel,color=INK,stroke_width=2,buff=0.4,corner_radius=0.12)
        grp=VGroup(pbox,panel); grp.move_to(RIGHT*3.7+UP*0.5); _clamp(grp)
        self.play(FadeIn(pbox),FadeIn(hdr),run_time=0.7)
        for ar,row in zip(arrows,led):
            self.play(GrowArrow(ar[0]),FadeIn(ar[1]),FadeIn(row),run_time=1.15)
        foot=_t("a dictionary of directions",size=28)
        foot.next_to(grp,DOWN,buff=0.5); _clamp(foot)
        under=Line(foot.get_left()+DOWN*0.22,foot.get_right()+DOWN*0.22,color=TERRA,stroke_width=2.5)
        self.play(FadeIn(foot),Create(under),run_time=0.9)
        self.wait(6.3)
        check_overlaps(plane,pl,arrows,grp,foot,label="B03")


class B04_TheReadout(Scene):
    """13.67s — projections drop; the ranked list builds; rank 1 underlined."""
    def construct(self):
        _rule(self)
        plane=RoundedRectangle(corner_radius=0.15,width=4.6,height=2.9,color=INK,
                               stroke_width=2,fill_color=CREAM,fill_opacity=1)
        plane.move_to(LEFT*3.3+UP*0.4)
        self.play(Create(plane),run_time=0.7)
        dot=Dot(color=TERRA,radius=0.11).move_to(plane.get_center()+UL*0.5)
        dl=_t("now",size=28,color="#A64A24").next_to(dot,UP,buff=0.12)  # WCAG-deep for TEXT
        self.play(FadeIn(dot),FadeIn(dl),run_time=0.6)
        units=[RIGHT*0.94+DOWN*0.34, RIGHT*0.74+DOWN*0.67, RIGHT*0.36+DOWN*0.93]
        lens=[1.5,1.0,0.6]; names=["orange","lemon","fruit"]
        projs=VGroup()
        for u,l in zip(units,lens):
            a=Arrow(dot.get_center(),dot.get_center()+u*(0.9+l),color=GRAY,
                    stroke_width=2.5,tip_length=0.13,buff=0.12)
            projs.add(a)
        self.play(LaggedStart(*[GrowArrow(a) for a in projs],lag_ratio=0.2),run_time=1.2)
        rows=VGroup()
        for i,(nm,ln) in enumerate(zip(names,lens)):
            rank=_mono(str(i+1),size=28,color=INK)
            bar=Rectangle(width=ln*1.6,height=0.3,color=INK,fill_color=INK,
                          fill_opacity=0.55,stroke_width=0)
            lbl=_t(nm,size=28)
            rows.add(VGroup(rank,bar,lbl).arrange(RIGHT,buff=0.3))
        rows.arrange(DOWN,buff=0.42,aligned_edge=LEFT)
        ttl=_t("top of mind, this layer",size=28,color=MUTE)
        panel=VGroup(ttl,rows).arrange(DOWN,buff=0.4,aligned_edge=LEFT)
        panel.move_to(RIGHT*3.6+UP*0.5); _clamp(panel)
        self.play(FadeIn(ttl),run_time=0.4)
        for r in rows:
            self.play(FadeIn(r,shift=LEFT*0.2),run_time=0.8)
        u=Line(rows[0].get_left()+DOWN*0.28,rows[0].get_right()+DOWN*0.28,
               color=TERRA,stroke_width=3)
        self.play(Create(u),run_time=0.6)
        foot=_t("a ranking, not a prediction",size=28)
        foot.next_to(panel,DOWN,buff=0.55); _clamp(foot)
        self.play(FadeIn(foot),run_time=0.7)
        self.wait(4.6)
        check_overlaps(plane,dot,dl,panel,foot,label="B04")


class B06_TheBand(Scene):
    """18.45s — the stack shades into three regions; the middle band IS the J-space."""
    def construct(self):
        _rule(self)
        col=Rectangle(width=2.2,height=5.2,color=INK,stroke_width=2,
                      fill_color=CREAM,fill_opacity=1)
        col.move_to(LEFT*3.6+UP*0.15)
        self.play(Create(col),run_time=0.8)
        h=col.height; base=col.get_bottom()
        def band(y0,y1,fill,op):
            r=Rectangle(width=2.2,height=(y1-y0)*h,stroke_width=0,
                        fill_color=fill,fill_opacity=op)
            r.move_to(base+UP*((y0+y1)/2*h)); return r
        sens=band(0,0.28,GRAY,0.25); mot=band(0.75,1.0,GRAY,0.25)
        mid=band(0.28,0.75,TERRA,0.3)
        s_l=_t("SENSORY — parsing",size=28).next_to(col,RIGHT,buff=0.3).align_to(sens,DOWN)
        m_l=_t("MOTOR — spelling out",size=28).next_to(col,RIGHT,buff=0.3).align_to(mot,UP)
        j_l=_t("THE J-SPACE",size=30,color=TERRA).next_to(col,RIGHT,buff=0.3)
        j_l.move_to([j_l.get_center()[0],mid.get_center()[1],0])
        self.play(FadeIn(sens),FadeIn(s_l),run_time=1.1)
        self.wait(0.6)
        self.play(FadeIn(mot),FadeIn(m_l),run_time=1.1)
        self.wait(0.6)
        self.play(FadeIn(mid),FadeIn(j_l),run_time=1.3)
        led=_ledger([("REGION","JOB"),("sensory","parses input"),
                     ("motor","writes output"),("middle","holds the thinking")],size=28,buff=0.36)
        layers_row=VGroup(_t("LAYERS",size=28,color=MUTE),
                          _mono("~38-92",size=28,color=INK)).arrange(RIGHT,buff=0.32)
        panel=VGroup(led,layers_row).arrange(DOWN,buff=0.5,aligned_edge=LEFT)
        pbox=SurroundingRectangle(panel,color=INK,stroke_width=2,buff=0.4,corner_radius=0.12)
        grp=VGroup(pbox,panel); grp.move_to(RIGHT*3.3+UP*0.15); _clamp(grp)
        self.play(FadeIn(grp),run_time=1.2)
        self.wait(9.0)
        check_overlaps(col,s_l,m_l,j_l,grp,label="B06")


class B07_TheBudget(Scene):
    """15.06s — a few dots migrate into the J-space box; the share bar stays small."""
    def construct(self):
        _rule(self)
        rng=np.random.default_rng(7)
        pts=rng.uniform([-5.6,-2.2],[-1.2,2.6],size=(70,2))
        dots=VGroup(*[Dot([x,y,0],radius=0.05,color=GRAY) for x,y in pts])
        self.play(FadeIn(dots),run_time=1.0)
        box=RoundedRectangle(corner_radius=0.12,width=2.6,height=1.8,color=TERRA,
                             stroke_width=3,fill_color=CREAM,fill_opacity=0.9)
        box.move_to(RIGHT*0.9+UP*0.4)
        bl=_t("THE J-SPACE",size=26,color=TERRA).next_to(box,UP,buff=0.2)
        self.play(Create(box),FadeIn(bl),run_time=0.9)
        chosen=list(dots[:9])
        targets=rng.uniform([-0.1,-0.2],[1.9,1.0],size=(9,2))
        for d in chosen: d.set_z_index(6)      # above the box fill
        box.set_z_index(2); bl.set_z_index(3)
        self.play(*[d.animate.move_to([tx,ty,0]).set_color(INK).scale(1.4)
                    for d,(tx,ty) in zip(chosen,targets)],run_time=1.8)
        slots=VGroup(_t("SLOTS",size=24,color=MUTE),_t("about 25",size=28)).arrange(RIGHT,buff=0.32)
        share_lbl=VGroup(_t("SHARE",size=24,color=MUTE),
                         _t("under 10%",size=28)).arrange(RIGHT,buff=0.32)
        frame=Rectangle(width=2.6,height=0.32,color=INK,stroke_width=1.5)
        fill=Rectangle(width=0.26,height=0.32,color=INK,fill_color=INK,
                       fill_opacity=0.55,stroke_width=0)
        fill.align_to(frame,LEFT).align_to(frame,DOWN)
        barrow=VGroup(frame,fill)
        panel=VGroup(slots,share_lbl,barrow).arrange(DOWN,buff=0.45,aligned_edge=LEFT)
        panel.move_to(RIGHT*4.7+UP*0.4); _clamp(panel)
        # keep clear of the J-space box (right edge ~2.2)
        if panel.get_left()[0] < box.get_right()[0]+0.4:
            panel.shift(RIGHT*(box.get_right()[0]+0.4-panel.get_left()[0]))
        self.play(FadeIn(slots),run_time=0.7)
        self.play(FadeIn(share_lbl),FadeIn(frame),GrowFromEdge(fill,LEFT),run_time=1.1)
        foot=_t("a thin, privileged slice",size=28)
        foot.next_to(panel,DOWN,buff=0.55); _clamp(foot)
        self.play(FadeIn(foot),run_time=0.7)
        self.wait(7.2)
        check_overlaps(box,bl,panel,foot,label="B07")


class B09_TheSwap(Scene):
    """17.90s — spider swaps for ant; the answer re-prints; the ledger flips."""
    def construct(self):
        _rule(self)
        rid=_box(_t("RIDDLE",size=28),h_pad=0.2,v_pad=0.14)
        js=RoundedRectangle(corner_radius=0.12,width=2.7,height=1.7,color=INK,
                            stroke_width=2.5,fill_color=CREAM,fill_opacity=1)
        jl=_t("J-SPACE",size=28,color=MUTE)
        ans=_box(_t("EIGHT LEGS",size=28),h_pad=0.2,v_pad=0.14)
        chain=VGroup(rid,js,ans).arrange(RIGHT,buff=0.9)
        chain.move_to(LEFT*2.1+UP*0.9); _clamp(chain,5.9)
        jl.next_to(js,UP,buff=0.15)
        # tip_length >= 0.22: at 2160 a 0.14 tip is a 36px blob that GATE T reads
        # as a sub-floor text run (horizontal arrow aspect ~5:1 passes the bar filter)
        a1=Arrow(rid.get_right(),js.get_left(),color=INK,stroke_width=3.5,tip_length=0.24,buff=0.08)
        a2=Arrow(js.get_right(),ans.get_left(),color=INK,stroke_width=3.5,tip_length=0.24,buff=0.08)
        spider=_box(_t("SPIDER",size=28),h_pad=0.16,v_pad=0.1,sw=1.5); spider.move_to(js)
        self.play(FadeIn(rid),FadeIn(js),FadeIn(jl),GrowArrow(a1),run_time=1.0)
        self.play(FadeIn(spider),GrowArrow(a2),FadeIn(ans),run_time=1.0)
        led=_ledger([("HELD CONCEPT",_t("SPIDER",size=28)),
                     ("ANSWER",_t("EIGHT LEGS",size=28))],size=28,buff=0.5)
        pbox=SurroundingRectangle(led,color=INK,stroke_width=2,buff=0.4,corner_radius=0.12)
        grp=VGroup(pbox,led); grp.move_to(RIGHT*0.4+DOWN*1.9); _clamp(grp)
        self.play(FadeIn(grp),run_time=0.8)
        self.wait(2.2)
        ant=_box(_t("ANT",size=28,color="#A64A24"),h_pad=0.16,v_pad=0.1,sw=1.8,stroke="#A64A24")
        ant.move_to(js.get_center()+UP*2.2)
        self.play(FadeIn(ant),run_time=0.5)
        self.play(spider.animate.shift(DOWN*2.2).set_opacity(0),
                  ant.animate.move_to(js.get_center()),run_time=1.3)
        new_ans=_box(_t("SIX LEGS",size=28,color="#A64A24"),h_pad=0.2,v_pad=0.14,stroke="#A64A24")
        new_ans.move_to(ans)
        held_new=_t("ANT",size=28,color="#A64A24").move_to(led[0][1]).align_to(led[0][1],LEFT)
        ansv_new=_t("SIX LEGS",size=28,color="#A64A24").move_to(led[1][1]).align_to(led[1][1],LEFT)
        self.play(Transform(ans,new_ans),
                  Transform(led[0][1],held_new),Transform(led[1][1],ansv_new),run_time=1.2)
        foot=_t("write once — everything downstream follows",size=34)
        foot.next_to(grp,DOWN,buff=0.5)
        foot.move_to([0,foot.get_center()[1],0]); _clamp(foot)
        self.play(FadeIn(foot),run_time=0.8)
        self.wait(6.6)
        check_overlaps(chain,jl,grp,foot,label="B09")

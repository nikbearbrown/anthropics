import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
DUR={}
try:
    _bs=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in _bs["beats"]}
except Exception: pass
def hold(scene,b,u=1): scene.wait(max(.1,DUR.get(b,10)-u))
def heading(t): return Text(t,font=DISPLAY,font_size=29,color=INK).to_edge(UP)
def line(y,w=6,c=INK): return Line(LEFT*w/2,RIGHT*w/2,color=c).shift(UP*y)

class B02_BohrScale(Scene):
    def construct(self):
        levels=VGroup(line(-1.5,7,TEAL),line(.2,7,INK),line(1.6,7,CRIMSON)); labs=VGroup(Text("n=1  −13.6 eV",font=MONO,font_size=27,color=TEAL).next_to(levels[0],RIGHT),Text("n=2  −3.4 eV",font=MONO,font_size=30,color=CRIMSON).next_to(levels[1],RIGHT),Text("n=3  −1.51 eV",font=MONO,font_size=27,color=INK).next_to(levels[2],RIGHT),Text("many states coincide at n=2",font=SERIF,font_size=28,color=INK).shift(DOWN*2.65))
        self.play(FadeIn(heading("ZOOM 1 — THE BOHR/COULOMB SCALE")),LaggedStart(*[Create(x) for x in levels],lag_ratio=.1),FadeIn(labs),run_time=1.2); hold(self,"B02",1.2)

class B03_NotOneRuler(Scene):
    def construct(self):
        g=VGroup(Text("3.4 eV",font=MONO,font_size=48,color=INK),Arrow(LEFT,RIGHT,color=CRIMSON),Text("4.5 × 10⁻⁵ eV",font=MONO,font_size=44,color=TEAL),Text("≈ 75,000× smaller",font=SERIF,font_size=35,color=CRIMSON),Text("magnify — do not fake linear spacing",font=SERIF,font_size=27,color=INK)).arrange(DOWN,buff=.5)
        self.play(FadeIn(heading("A LEVEL DIAGRAM NEEDS A SCALE")),FadeIn(g),run_time=1); hold(self,"B03")

class B04_ThreeCorrections(Scene):
    def construct(self):
        boxes=VGroup(*[RoundedRectangle(width=3.1,height=1.4,corner_radius=.2,color=c) for c in [TEAL,CRIMSON,INK]]).arrange(RIGHT,buff=.45); txt=VGroup(Text("relativistic\nkinetic",font=SERIF,font_size=25,color=TEAL),Text("spin–orbit",font=SERIF,font_size=27,color=CRIMSON),Text("Darwin",font=SERIF,font_size=27,color=INK)); [txt[i].move_to(boxes[i]) for i in range(3)]; arrow=Arrow(DOWN*.5,DOWN*2,color=CRIMSON); out=Text("energy depends on n and j",font=MONO,font_size=34,color=INK).shift(DOWN*2.5)
        self.play(FadeIn(heading("ALL THREE FINE-STRUCTURE TERMS SHARE ONE ORDER")),FadeIn(boxes),FadeIn(txt),GrowArrow(arrow),FadeIn(out),run_time=1.2); hold(self,"B04",1.2)

class B05_FineSplit(Scene):
    def construct(self):
        low=line(-.8,7,TEAL); high=line(1.2,7,CRIMSON); labs=VGroup(Text("2S₁/₂ , 2P₁/₂",font=MONO,font_size=29,color=TEAL).next_to(low,RIGHT),Text("2P₃/₂",font=MONO,font_size=29,color=CRIMSON).next_to(high,RIGHT),Text("ΔE_FS ≈ 4.5 × 10⁻⁵ eV ≈ 11 GHz",font=MONO,font_size=31,color=INK).shift(DOWN*2.45)); arr=DoubleArrow(DOWN*.7,UP*1.1,color=CRIMSON).shift(LEFT*3)
        self.play(FadeIn(heading("ZOOM 2 — FINE STRUCTURE RESOLVES j")),Create(low),Create(high),GrowArrow(arr),FadeIn(labs),run_time=1.2); hold(self,"B05",1.2)

class B06_DiracDegeneracy(Scene):
    def construct(self):
        a=Text("2S₁/₂",font=MONO,font_size=40,color=TEAL).move_to(LEFT*3+UP*.7); b=Text("2P₁/₂",font=MONO,font_size=40,color=CRIMSON).move_to(RIGHT*3+UP*.7); eq=Text("same n, same j  ⇒  same Dirac-Coulomb energy",font=SERIF,font_size=30,color=INK).shift(DOWN*2)
        self.play(FadeIn(heading("THE RELATIVISTIC COULOMB THEORY LEAVES A PAIR")),FadeIn(a),FadeIn(b),Create(line(0,8,INK)),FadeIn(eq),run_time=1); hold(self,"B06")

class B07_ThirdZoom(Scene):
    def construct(self):
        base=line(0,8,INK); upper=line(.75,6,TEAL); lower=line(-.75,6,CRIMSON); mag=Circle(radius=1.2,color=CRIMSON).shift(LEFT*4); labs=VGroup(Text("2S₁/₂",font=MONO,font_size=28,color=TEAL).next_to(upper,RIGHT),Text("2P₁/₂",font=MONO,font_size=28,color=CRIMSON).next_to(lower,RIGHT),Text("~10× more resolution",font=SERIF,font_size=29,color=INK).shift(DOWN*2.55))
        self.play(FadeIn(heading("ZOOM 3 — THE j=1/2 LINE SPLITS")),Create(base),Create(mag),run_time=.7); self.play(ReplacementTransform(base,upper),FadeIn(lower),FadeIn(labs),run_time=.7); hold(self,"B07",1.4)

class B08_LambNumber(Scene):
    def construct(self):
        g=VGroup(Text("ν_Lamb ≈ 1058 MHz",font=MONO,font_size=46,color=TEAL),Text("ΔE = hν",font=MONO,font_size=39,color=INK),Text("≈ 4.4 × 10⁻⁶ eV",font=MONO,font_size=43,color=CRIMSON),Text("2S₁/₂ lies above 2P₁/₂",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.52)
        self.play(FadeIn(heading("THE n=2 LAMB SHIFT")),FadeIn(g),run_time=1); hold(self,"B08")

class B09_QEDBoundary(Scene):
    def construct(self):
        left=VGroup(Text("Dirac–Coulomb",font=DISPLAY,font_size=31,color=TEAL),Text("degenerate pair",font=SERIF,font_size=27,color=INK)).arrange(DOWN,buff=.5).move_to(LEFT*3); right=VGroup(Text("radiative QED",font=DISPLAY,font_size=31,color=CRIMSON),Text("self-energy\nvacuum polarization\nsmaller terms",font=SERIF,font_size=25,color=INK,line_spacing=1.15)).arrange(DOWN,buff=.5).move_to(RIGHT*3); arr=Arrow(LEFT*.8,RIGHT*.8,color=CRIMSON)
        self.play(FadeIn(heading("THE THIRD ZOOM CROSSES A THEORY BOUNDARY")),FadeIn(left),GrowArrow(arr),FadeIn(right),run_time=1.1); hold(self,"B09",1.1)

class B10_SvsP(Scene):
    def construct(self):
        proton=Dot(radius=.18,color=CRIMSON); s=Circle(radius=1.5,color=TEAL,fill_opacity=.12); p=VGroup(Ellipse(width=1.7,height=3,color=INK,fill_opacity=.08).shift(UP*.9),Ellipse(width=1.7,height=3,color=INK,fill_opacity=.08).shift(DOWN*.9)); labs=VGroup(Text("S samples r≈0",font=SERIF,font_size=29,color=TEAL).move_to(LEFT*3+DOWN*2),Text("P has a node at r=0",font=SERIF,font_size=29,color=CRIMSON).move_to(RIGHT*3+DOWN*2)); s.shift(LEFT*3); proton.shift(LEFT*3); p.shift(RIGHT*3)
        self.play(FadeIn(heading("SHORT-DISTANCE SENSITIVITY DIFFERS")),FadeIn(s),FadeIn(proton),FadeIn(p),FadeIn(labs),run_time=1); hold(self,"B10")

class B11_LogHierarchy(Scene):
    def construct(self):
        vals=[("Bohr |E₂|",3.4,INK),("fine split",4.5e-5,TEAL),("Lamb shift",4.4e-6,CRIMSON)]; rows=VGroup()
        for i,(lab,v,c) in enumerate(vals):
            width=2+1.15*(np.log10(v)+6); bar=Rectangle(width=max(.7,width),height=.62,color=c,fill_opacity=.28); text=Text(f"{lab}: {v:.2g} eV",font=MONO,font_size=27,color=c); rows.add(VGroup(text,bar).arrange(RIGHT,buff=.45))
        rows.arrange(DOWN,aligned_edge=LEFT,buff=.5); note=Text("gross→fine ≈ 75,000×     fine→Lamb ≈ 10×",font=MONO,font_size=28,color=INK).shift(DOWN*2.6)
        self.play(FadeIn(heading("ONE LOGARITHMIC RULER")),FadeIn(rows),FadeIn(note),run_time=1); hold(self,"B11")

class B12_SpectrumAudit(Scene):
    def construct(self):
        items=["spectra measure transitions","selection rules choose components","linewidth can hide splittings","fields shift or split levels","resolution controls what separates"]
        rows=VGroup(*[Text("• "+x,font=SERIF,font_size=28,color=TEAL if i%2==0 else CRIMSON) for i,x in enumerate(items)]).arrange(DOWN,aligned_edge=LEFT,buff=.42)
        self.play(FadeIn(heading("A HORIZONTAL LEVEL IS NOT ITSELF A SPECTRAL LINE")),FadeIn(rows),run_time=1); hold(self,"B12")

class B13_YourTurn(Scene):
    def construct(self):
        g=VGroup(Text("YOUR TURN",font=DISPLAY,font_size=35,color=INK),Text("4.5 × 10⁻⁵ eV",font=MONO,font_size=40,color=TEAL),Text("÷  4.4 × 10⁻⁶ eV",font=MONO,font_size=40,color=CRIMSON),Text("extra magnification = ?",font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.55)
        self.play(FadeIn(g),run_time=1); hold(self,"B13")

class B14_Answer(Scene):
    def construct(self):
        g=VGroup(Text("ANSWER",font=DISPLAY,font_size=35,color=INK),Text("≈ 10.2×",font=MONO,font_size=55,color=TEAL),Text("fine → Lamb",font=SERIF,font_size=32,color=CRIMSON),Text("gross → fine ≈ 75,000×",font=MONO,font_size=30,color=INK)).arrange(DOWN,buff=.55)
        self.play(FadeIn(g),run_time=1); hold(self,"B14")

class B15_CorrectTitleOutro(Scene):
    def construct(self):
        self.camera.background_color="#201F1C"; title=Text("Three Zooms Into Hydrogen's n=2 Levels",font=DISPLAY,font_size=34,color="#F2EFE8"); credit=Text("Liam, in for Bear",font=SERIF,font_size=20,color="#D97757").next_to(title,DOWN,buff=.45); self.play(FadeIn(title),FadeIn(credit),run_time=1); hold(self,"B15")
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=14.12
  self.add(bg(),ttl('First zoom: the Coulomb problem. Ignorin'))
  stmt=Text('First zoom: the Coulomb problem',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Ignoring smaller corrections, hydrogen energy depends o',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.37
  self.add(bg(),ttl('At the second zoom, relativistic kinetic'))
  stmt=Text('At the second zoom, relativistic kinetic energy, spin–o',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Together they make the energy depend on total angular m',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: generic reveal with underline
 def construct(self):
  d=13.23
  self.add(bg(),ttl('For n equals two, the fine-structure for'))
  stmt=Text('For n equals two, the fine-structure formula separates ',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The interval is about four-point-five times ten to the ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.22
  self.add(bg(),ttl('But the relativistic Coulomb theory stil'))
  stmt=Text('But the relativistic Coulomb theory still places two-S ',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Same n, same j: the fine-structure formula cannot disti',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.73
  self.add(bg(),ttl('The measured separation is about 1058 me'))
  stmt=Text('The measured separation is about 1058 megahertz, equiva',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('This is the celebrated n-equals-two Lamb shift',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=15.19
  self.add(bg(),ttl('That interval lies beyond the Dirac Coul'))
  stmt=Text('That interval lies beyond the Dirac Coulomb spectrum',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Quantum electrodynamic radiative corrections, especiall',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B10_SDT(Scene):
 # B10 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=12.42
  self.add(bg(),ttl('The S state samples the short-distance r'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The S state samples the short-distance region near the ',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('That makes their radiative shifts unequal',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B11_SDT(Scene):
 # B11 SDT retrofit: generic reveal with underline
 def construct(self):
  d=14.46
  self.add(bg(),ttl('Put the three characteristic energies on'))
  stmt=Text('Put the three characteristic energies on a logarithmic ',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('4 electron volts, forty-five micro-electron-volts, then',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B12_SDT(Scene):
 # B12 SDT retrofit: generic reveal with underline
 def construct(self):
  d=15.94
  self.add(bg(),ttl('Strictly, experiments observe transition'))
  stmt=Text('Strictly, experiments observe transition frequencies be',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Which components appear also depends on selection rules',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B13_SDT(Scene):
 # B13 SDT retrofit: generic reveal with underline
 def construct(self):
  d=14.74
  self.add(bg(),ttl('Your turn. Divide the n-equals-two fine-'))
  stmt=Text('Divide the n-equals-two fine-structure interval, four-p',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('How much extra magnification reveals the third zoom?',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B14_SDT(Scene):
 # B14 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.39
  self.add(bg(),ttl('The ratio is about ten-point-two. So the'))
  stmt=Text('The ratio is about ten-point-two',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('So the Lamb split needs roughly ten times more energy r',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B15_SDT(Scene):
 # B15 SDT retrofit: generic reveal with underline
 def construct(self):
  d=4.91
  self.add(bg(),ttl('Three Zooms Into Hydrogen\'s n=2 Levels. '))
  stmt=Text('Three Zooms Into Hydrogen\'s n=2 Levels',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Liam, in for Bear',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))

import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")));D={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}
def label(a,b,c=TEAL):
 x=Text(a,font=DISPLAY,color=INK,font_size=43,weight=BOLD);y=Text(b,font=SERIF,color=c,font_size=28,slant=ITALIC)
 if x.width>11.5:x.scale_to_fit_width(11.5)
 if y.width>11:y.scale_to_fit_width(11)
 return VGroup(x,y).arrange(DOWN,buff=.4)
def node(t,c=TEAL,w=2.5):
 r=RoundedRectangle(corner_radius=.14,width=w,height=.9).set_fill(GROUND,1).set_stroke(c,3);x=Text(t,font=MONO,color=c,font_size=26).move_to(r)
 if x.width>w*.85:x.scale_to_fit_width(w*.85)
 return VGroup(r,x)
class B02_TwoRecords(Scene):
 def construct(self):
  atom=node("ATOM",SLATE);live=node("LIVE CAT",TEAL,3);dead=node("DEAD CAT",CRIMSON,3);g=VGroup(live,dead).arrange(DOWN,buff=1).to_edge(RIGHT,buff=1.3);ar=VGroup(Arrow(atom.get_right(),live.get_left(),color=TEAL),Arrow(atom.get_right(),dead.get_left(),color=CRIMSON));self.play(FadeIn(atom),run_time=.4);self.play(*[GrowArrow(x) for x in ar],FadeIn(g),run_time=1);self.wait(max(.5,D["B02"]-1.4))
class B03_Recombine(Scene):
 def construct(self):
  l=node("LIVE",TEAL);d=node("DEAD",CRIMSON);g=VGroup(l,d).arrange(DOWN,buff=1).to_edge(LEFT,buff=1.2);screen=node("INTERFERENCE?",SLATE,3.5).to_edge(RIGHT,buff=1.2);ar=VGroup(Arrow(l.get_right(),screen.get_left(),color=TEAL),Arrow(d.get_right(),screen.get_left(),color=CRIMSON));self.play(FadeIn(g),run_time=.4);self.play(*[GrowArrow(x) for x in ar],FadeIn(screen),run_time=1);self.wait(max(.5,D["B03"]-1.4))
class B04_Environment(Scene):
 def construct(self):
  cat=node("CAT",INK,2.2);env=VGroup(*[node(t,c,2.1) for t,c in [("AIR",TEAL),("PHOTONS",CRIMSON),("BOX",SLATE),("INTERNAL",TEAL)]]).arrange_in_grid(rows=2,cols=2,buff=.8);env.scale(.8);ar=VGroup(*[Arrow(x.get_center(),cat.get_center(),color=x[0].get_stroke_color(),buff=.55) for x in env]);self.play(FadeIn(cat),FadeIn(env),run_time=.6);self.play(*[GrowArrow(x) for x in ar],run_time=1);self.wait(max(.5,D["B04"]-1.6))
class B05_WhichBranch(Scene):
 def construct(self):
  l=label("LIVE BRANCH","environment record E_live",TEAL);d=label("DEAD BRANCH","environment record E_dead",CRIMSON);g=VGroup(l,d).arrange(DOWN,buff=.8);self.play(LaggedStart(*[FadeIn(x,shift=RIGHT*.15) for x in g],lag_ratio=.25),run_time=1.2);self.wait(max(.5,D["B05"]-1.2))
class B06_OverlapFalls(Scene):
 def construct(self):
  ax=Axes(x_range=[0,5,1],y_range=[0,1,.25],x_length=8,y_length=4,axis_config={"color":INK,"include_ticks":False});curve=ax.plot(lambda x:np.exp(-1.5*x),x_range=[0,5],color=CRIMSON);lab=Text("branch overlap → 0",font=DISPLAY,color=INK,font_size=40,weight=BOLD).to_edge(UP,buff=.5);self.play(Create(ax),Create(curve),FadeIn(lab),run_time=1.3);self.wait(max(.5,D["B06"]-1.3))
class B07_FastButConditional(Scene):
 def construct(self):
  fast=Text("MACROSCOPIC DECOHERENCE: EXTREMELY FAST",font=DISPLAY,color=CRIMSON,font_size=38,weight=BOLD);factors=Text("depends on size · separation · temperature · coupling",font=SERIF,color=TEAL,font_size=30,slant=ITALIC);g=VGroup(fast,factors).arrange(DOWN,buff=.6);self.play(FadeIn(g),run_time=.8);self.wait(max(.5,D["B07"]-.8))
class B08_LocalMixture(Scene):
 def construct(self):
  left=label("LOCAL DESCRIPTION","classical-looking alternatives",TEAL);right=label("FULL STATE","still system + environment",CRIMSON);g=VGroup(left,right).arrange(RIGHT,buff=1.2);self.play(FadeIn(g),run_time=.9);self.wait(max(.5,D["B08"]-.9))
class B09_PointerBasis(Scene):
 def construct(self):
  stable=VGroup(node("LIVE RECORD",TEAL,3),node("DEAD RECORD",CRIMSON,3)).arrange(DOWN,buff=.5);bad=VGroup(node("LIVE + DEAD",SLATE,3),node("LIVE - DEAD",SLATE,3)).arrange(DOWN,buff=.5);g=VGroup(stable,bad).arrange(RIGHT,buff=1.4);heads=VGroup(Text("STABLE",font=DISPLAY,color=TEAL,font_size=32,weight=BOLD).next_to(stable,UP),Text("FRAGILE",font=DISPLAY,color=SLATE,font_size=32,weight=BOLD).next_to(bad,UP));self.play(FadeIn(g),FadeIn(heads),run_time=1);self.wait(max(.5,D["B09"]-1))
class B10_BasisNotOutcome(Scene):
 def construct(self):
  yes=label("DECOHERENCE EXPLAINS","preferred basis + lost interference",TEAL);no=label("DOES NOT SELECT","this unique outcome",CRIMSON);g=VGroup(yes,no).arrange(DOWN,buff=.8);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.25),run_time=1.2);self.wait(max(.5,D["B10"]-1.2))
class B12_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("Why the Cat Isn't",font=DISPLAY,color=WHITE,font_size=51,weight=BOLD);b=Text("Both Alive and Dead",font=SERIF,color="#D7C8FF",font_size=40,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,D["B12"]-.7))
class B05_SDT(Scene):
 # B05 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Those interactions correlate different e'))
  stmt=Text('Those interactions correlate different environmental st',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('In effect, the surroundings acquire which-branch inform',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.0
  self.add(bg(),ttl('This is decoherence. For ordinary macros'))
  stmt=Text('This is decoherence',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('For ordinary macroscopic objects in ordinary environmen',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=11.0
  self.add(bg(),ttl('The system then behaves, for practical l'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The system then behaves, for practical local prediction',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('That does not mean the full system-plus-environment sta',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Decoherence also helps explain the prefe'))
  stmt=Text('Decoherence also helps explain the preferred basis',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The interaction selects stable pointer states — here, m',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B10_SDT(Scene):
 # B10 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=12.0
  self.add(bg(),ttl('But it does not solve the outcome'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('But it does not solve the outcome problem',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Suppressing interference explains why branches do not l',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B12_SDT(Scene):
 # B12 SDT retrofit: generic reveal with underline
 def construct(self):
  d=8.0
  self.add(bg(),ttl('Why the cat isn\'t both alive and'))
  stmt=Text('Why the cat isn\'t both alive and dead: the environment ',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))

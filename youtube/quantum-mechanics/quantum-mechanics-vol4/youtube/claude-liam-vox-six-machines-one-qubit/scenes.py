import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")));D={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}
def chip(t,c=SLATE,w=2.6):
 r=RoundedRectangle(corner_radius=.12,width=w,height=.82).set_fill(GROUND,1).set_stroke(c,3);x=Text(t,font=MONO,color=c,font_size=24).move_to(r)
 if x.width>w*.84:x.scale_to_fit_width(w*.84)
 return VGroup(r,x)
def title(a,b,c=TEAL):
 x=Text(a,font=DISPLAY,color=INK,font_size=42,weight=BOLD);y=Text(b,font=SERIF,color=c,font_size=28,slant=ITALIC)
 if x.width>11.5:x.scale_to_fit_width(11.5)
 if y.width>11:y.scale_to_fit_width(11)
 return VGroup(x,y).arrange(DOWN,buff=.4)
class B02_FirstPlatforms(Scene):
 def construct(self):
  g=VGroup(chip("SUPERCONDUCTING",TEAL,3.4),chip("TRAPPED ION",CRIMSON,3.2),chip("NEUTRAL ATOM",SLATE,3.2)).arrange(RIGHT,buff=.45);sub=VGroup(*[Text(t,font=SERIF,color=c,font_size=25,slant=ITALIC).next_to(g[i],DOWN,buff=.35) for i,(t,c) in enumerate([("circuit levels",TEAL),("internal states",CRIMSON),("ground / Rydberg",SLATE)])]);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.18),FadeIn(sub),run_time=1.2);self.wait(max(.5,D["B02"]-1.2))
class B03_MorePlatforms(Scene):
 def construct(self):
  g=VGroup(chip("PHOTON",TEAL,2.7),chip("DIAMOND NV",CRIMSON,3),chip("SILICON SPIN",SLATE,3)).arrange(RIGHT,buff=.55);sub=VGroup(*[Text(t,font=SERIF,color=c,font_size=25,slant=ITALIC).next_to(g[i],DOWN,buff=.35) for i,(t,c) in enumerate([("path / polarization",TEAL),("spin sublevels",CRIMSON),("electron / nucleus",SLATE)])]);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.18),FadeIn(sub),run_time=1.2);self.wait(max(.5,D["B03"]-1.2))
class B04_CommonSubspace(Scene):
 def construct(self):
  levels=VGroup(*[Line(LEFT*1.2,RIGHT*1.2,color=c).shift(UP*y) for y,c in [(-1.5,TEAL),(-.2,CRIMSON),(1,SLATE),(2,SLATE)]]);labs=VGroup(Text("|0>",font=MONO,color=TEAL,font_size=28).next_to(levels[0],LEFT),Text("|1>",font=MONO,color=CRIMSON,font_size=28).next_to(levels[1],LEFT));circle=Circle(radius=1.7,color=SLATE).to_edge(RIGHT,buff=2);arrow=Arrow(circle.get_center(),circle.get_center()+UP*1.2+RIGHT*.7,color=CRIMSON,buff=0);arr=Arrow(levels.get_right(),circle.get_left(),color=INK,buff=.4);self.play(FadeIn(levels),FadeIn(labs),run_time=.6);self.play(GrowArrow(arr),Create(circle),GrowArrow(arrow),run_time=1);self.wait(max(.5,D["B04"]-1.6))
class B05_SameRotations(Scene):
 def construct(self):
  c=Circle(radius=2.1,color=SLATE);axes=VGroup(Arrow(ORIGIN,RIGHT*2.8,color=TEAL,buff=0),Arrow(ORIGIN,UP*2.8,color=CRIMSON,buff=0),Arrow(ORIGIN,LEFT*1.5+DOWN*1.7,color=INK,buff=0));labs=VGroup(*[Text(t,font=MONO,color=co,font_size=34).next_to(axes[i].get_end(),d) for i,(t,co,d) in enumerate([("X",TEAL,RIGHT),("Z",CRIMSON,UP),("Y",INK,DOWN)])]);self.play(Create(c),LaggedStart(*[GrowArrow(a) for a in axes],lag_ratio=.2),FadeIn(labs),run_time=1.3);self.wait(max(.5,D["B05"]-1.3))
class B06_DifferentControls(Scene):
 def construct(self):
  rows=VGroup(*[VGroup(chip(a,SLATE,3.2),chip(b,c,3.4)).arrange(RIGHT,buff=.55) for a,b,c in [("circuits / spins","microwaves",TEAL),("ions / atoms","lasers",CRIMSON),("photons","optical elements",TEAL)]]).arrange(DOWN,buff=.35);self.play(LaggedStart(*[FadeIn(r) for r in rows],lag_ratio=.2),run_time=1.2);self.wait(max(.5,D["B06"]-1.2))
class B07_OutsideSubspace(Scene):
 def construct(self):
  core=VGroup(chip("|0>",TEAL,1.5),chip("|1>",CRIMSON,1.5)).arrange(RIGHT,buff=.3);outer=VGroup(*[chip(t,SLATE,2.1) for t in ["higher levels","motion","loss","extra modes"]]).arrange_in_grid(rows=2,cols=2,buff=.6);outer.scale(.85);g=VGroup(core,outer).arrange(DOWN,buff=.8);self.play(FadeIn(core),run_time=.5);self.play(LaggedStart(*[FadeIn(x) for x in outer],lag_ratio=.15),run_time=.9);self.wait(max(.5,D["B07"]-1.4))
class B08_Leakage(Scene):
 def construct(self):
  sub=RoundedRectangle(width=5.5,height=2.2,corner_radius=.15).set_stroke(TEAL,4);q=VGroup(chip("|0>",TEAL,1.4),chip("|1>",CRIMSON,1.4)).arrange(RIGHT,buff=.5).move_to(sub);leak=chip("|2> leakage",SLATE,2.7).shift(RIGHT*4);arr=Arrow(q.get_right(),leak.get_left(),color=CRIMSON,buff=.25);lab=Text("effective model has a boundary",font=SERIF,color=INK,font_size=31,slant=ITALIC).to_edge(DOWN,buff=.7);self.play(FadeIn(sub),FadeIn(q),run_time=.5);self.play(GrowArrow(arr),FadeIn(leak),FadeIn(lab),run_time=1);self.wait(max(.5,D["B08"]-1.5))
class B09_TranslationLayer(Scene):
 def construct(self):
  logical=chip("logical X/2",CRIMSON,3);cal=chip("calibration",SLATE,3);pulse=chip("device pulse",TEAL,3);g=VGroup(logical,cal,pulse).arrange(RIGHT,buff=.65);ar=VGroup(Arrow(logical.get_right(),cal.get_left(),color=INK,buff=.15),Arrow(cal.get_right(),pulse.get_left(),color=INK,buff=.15));self.play(FadeIn(g),run_time=.6);self.play(*[GrowArrow(x) for x in ar],run_time=.7);self.wait(max(.5,D["B09"]-1.3))
class B10_InterfaceNotPhysics(Scene):
 def construct(self):
  same=title("SAME INTERFACE","state · rotations · measurement",TEAL);diff=title("DIFFERENT PHYSICS","noise · coupling · connectivity · leakage",CRIMSON);g=VGroup(same,diff).arrange(DOWN,buff=.8);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.25),run_time=1.2);self.wait(max(.5,D["B10"]-1.2))
class B12_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("Six Machines",font=DISPLAY,color=WHITE,font_size=54,weight=BOLD);b=Text("One Qubit",font=SERIF,color="#D7C8FF",font_size=43,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,D["B12"]-.7))
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('A superconducting qubit uses selected ci'))
  stmt=Text('A superconducting qubit uses selected circuit energy le',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('A trapped ion may use internal atomic states',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B03_SDT(Scene):
 # B03 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('A photonic qubit can use polarization or'))
  stmt=Text('A photonic qubit can use polarization or paths',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('A diamond NV center uses spin sublevels',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.0
  self.add(bg(),ttl('In the ideal two-level model, a controll'))
  stmt=Text('In the ideal two-level model, a controlled Hamiltonian ',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The same abstract X, Y, and Z rotations describe gates ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=11.0
  self.add(bg(),ttl('But the physical controls differ. Microw'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('But the physical controls differ',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Microwave pulses drive superconducting circuits and man',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B10_SDT(Scene):
 # B10 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=11.0
  self.add(bg(),ttl('So six machines share one mathematical i'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('So six machines share one mathematical interface, not i',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Their coherence, connectivity, measurement, gate mechan',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
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
  self.add(bg(),ttl('Six machines, one qubit: one shared math'))
  stmt=Text('Six machines, one qubit: one shared mathematical interf',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))

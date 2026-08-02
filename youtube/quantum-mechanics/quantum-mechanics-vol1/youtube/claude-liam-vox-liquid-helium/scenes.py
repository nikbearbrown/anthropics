import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def atoms(xs,ys,color=TEAL,r=.2): return VGroup(*[Dot(np.array([x,y,0]),radius=r,color=color) for x in xs for y in ys])
class B02_Compare(Scene):
 def construct(self):
  d=DUR.get('B02',9); self.add(bg(),ttl('MOST MATERIALS CRYSTALLIZE · LOW-PRESSURE HELIUM DOES NOT')); crystal=atoms([-4.8,-4,-3.2],[-1,0,1],INK); liquid=VGroup(*[Dot(np.array([x,y,0]),radius=.2,color=CRIMSON) for x,y in [(.8,-.7),(1.7,.5),(2.8,-.4),(3.8,.8),(4.8,-.8),(5,.2),(2.3,1.2)]]); labs=VGroup(Text('localized crystal sites',font=MONO,font_size=26,color=INK).move_to(LEFT*4+DOWN*2.2),Text('helium: delocalized liquid',font=MONO,font_size=26,color=CRIMSON).move_to(RIGHT*3+DOWN*2.2)); self.play(FadeIn(crystal,liquid,labs),run_time=1); self.wait(max(.1,d-1))
class B03_ZeroK(Scene):
 def construct(self):
  d=DUR.get('B03',8); self.add(bg(),ttl('ZERO KELVIN IS NOT ZERO KINETIC ENERGY')); wrong=Text('classical picture: perfectly still',font=MONO,font_size=31,color=SLATE).move_to(UP*1.2); right=Text('quantum picture: lowest allowed state',font=MONO,font_size=38,color=CRIMSON).move_to(DOWN*.3); note=Text('ground state != no motion',font=SERIF,font_size=31,color=TEAL).move_to(DOWN*2); self.play(FadeIn(wrong,right,note),run_time=1); self.wait(max(.1,d-1))
class B04_Localize(Scene):
 def construct(self):
  d=DUR.get('B04',10); self.add(bg(),ttl('TIGHTER LOCALIZATION COSTS KINETIC ENERGY')); wide=Rectangle(width=4,height=1.5,color=TEAL).move_to(LEFT*3); narrow=Rectangle(width=1,height=1.5,color=CRIMSON).move_to(RIGHT*3); waves=VGroup(Text('small Delta p',font=MONO,font_size=27,color=TEAL).move_to(LEFT*3),Text('large Delta p',font=MONO,font_size=27,color=CRIMSON).move_to(RIGHT*3)); eq=Text('Delta x down  ->  Delta p up',font=MONO,font_size=35,color=INK).move_to(DOWN*2.4); self.play(FadeIn(wide,narrow,waves,eq),run_time=1); self.wait(max(.1,d-1))
class B05_ZPE(Scene):
 def construct(self):
  d=DUR.get('B05',9); self.add(bg(),ttl('CONFINEMENT HAS A QUANTUM FLOOR')); bowl=FunctionGraph(lambda x:.15*x*x-2,x_range=[-5,5],color=INK,stroke_width=4); level=Line(LEFT*2.2,RIGHT*2.2,color=CRIMSON,stroke_width=5).move_to(DOWN*1.25); eq=Text('E0 = 1/2 hbar omega',font=MONO,font_size=43,color=CRIMSON).move_to(UP*1.8); self.play(Create(bowl),Create(level),FadeIn(eq),run_time=1); self.wait(max(.1,d-1))
class B06_Mass(Scene):
 def construct(self):
  d=DUR.get('B06',10); self.add(bg(),ttl('LIGHT ATOMS DELOCALIZE MORE')); heavy=Circle(radius=.65,color=INK,fill_color=INK,fill_opacity=.2).move_to(LEFT*3); light=Circle(radius=1.7,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.1).move_to(RIGHT*3); labs=VGroup(Text('heavier: narrower',font=MONO,font_size=27,color=INK).move_to(LEFT*3+DOWN*2),Text('helium: broader',font=MONO,font_size=27,color=CRIMSON).move_to(RIGHT*3+DOWN*2)); eq=Text('lower mass -> larger zero-point spread',font=SERIF,font_size=30,color=TEAL).move_to(UP*2.3); self.play(FadeIn(heavy,light,labs,eq),run_time=1); self.wait(max(.1,d-1))
class B07_Binding(Scene):
 def construct(self):
  d=DUR.get('B07',10); self.add(bg(),ttl('THE HELIUM–HELIUM ATTRACTION IS SHALLOW')); well=FunctionGraph(lambda x:-1.2*np.exp(-((x-1)**2)/2)+.08*(x-1)**4,x_range=[-3,4],color=CRIMSON,stroke_width=4); label=Text('weak dispersion binding',font=MONO,font_size=31,color=INK).move_to(UP*2); no=Text('not gravity',font=SERIF,font_size=33,color=CRIMSON).move_to(DOWN*2.6); self.play(Create(well),FadeIn(label,no),run_time=1); self.wait(max(.1,d-1))
class B08_Lattice(Scene):
 def construct(self):
  d=DUR.get('B08',10); self.add(bg(),ttl('THE WAVEPACKETS OVERLAP THE WOULD-BE LATTICE')); sites=VGroup(*[DashedLine(np.array([x,-2,0]),np.array([x,2,0]),color=SLATE) for x in [-4,-2,0,2,4]]); clouds=VGroup(*[Circle(radius=1.1,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.08).move_to(RIGHT*x) for x in [-4,-2,0,2,4]]); note=Text('localization cost beats shallow binding',font=MONO,font_size=31,color=INK).move_to(DOWN*2.7); self.play(FadeIn(sites,clouds,note),run_time=1); self.wait(max(.1,d-1))
class B09_Liquid(Scene):
 def construct(self):
  d=DUR.get('B09',9); self.add(bg(),ttl('COOLING CANNOT REMOVE GROUND-STATE SPREAD')); temps=VGroup(Text('thermal motion -> 0',font=MONO,font_size=36,color=INK),Text('zero-point spread remains',font=MONO,font_size=40,color=CRIMSON)).arrange(DOWN,buff=.9); liquid=VGroup(*[Dot(np.array([x,y,0]),radius=.18,color=TEAL) for x,y in [(-4,-2),(-2.5,-1.4),(-1,-2.1),(.5,-1.3),(2,-2),(3.5,-1.4),(5,-2.1)]]); self.play(FadeIn(temps,liquid),run_time=1); self.wait(max(.1,d-1))
class B10_Pressure(Scene):
 def construct(self):
  d=DUR.get('B10',10); self.add(bg(),ttl('PRESSURE TIPS THE BALANCE')); left=atoms([-4.5,-3,-1.5],[-.8,.8],CRIMSON); right=atoms([1.8,2.6,3.4,4.2],[0,1],INK); arrows=VGroup(Arrow(LEFT*6,LEFT*5,color=TEAL),Arrow(RIGHT*6,RIGHT*5,color=TEAL)); labs=VGroup(Text('low pressure: liquid',font=MONO,font_size=27,color=CRIMSON).move_to(LEFT*3+DOWN*2.2),Text('about 25 bar+: solid',font=MONO,font_size=27,color=INK).move_to(RIGHT*3+DOWN*2.2)); self.play(FadeIn(left,right,labs),GrowFromCenter(arrows),run_time=1); self.wait(max(.1,d-1))
class B11_Distinction(Scene):
 def construct(self):
  d=DUR.get('B11',9); self.add(bg(),ttl('NOT THE SAME QUESTION AS SUPERFLUIDITY')); a=Text('Why no solid?',font=SERIF,font_size=42,color=CRIMSON).move_to(LEFT*3+UP*.8); b=Text('Why frictionless flow?',font=SERIF,font_size=42,color=TEAL).move_to(RIGHT*3+UP*.8); sep=Line(UP*2,DOWN*2,color=SLATE); notes=VGroup(Text('zero-point delocalization',font=MONO,font_size=25,color=CRIMSON).move_to(LEFT*3+DOWN*.8),Text('collective quantum order',font=MONO,font_size=25,color=TEAL).move_to(RIGHT*3+DOWN*.8)); self.play(FadeIn(a,b,sep,notes),run_time=1); self.wait(max(.1,d-1))
class B12_Recap(Scene):
 def construct(self):
  d=DUR.get('B12',8); self.add(bg(),Text('WHY HELIUM STAYS LIQUID',font=DISPLAY,font_size=34,color=TEAL).move_to(UP*2.3),Text('light atoms + shallow binding',font=MONO,font_size=34,color=INK).move_to(UP*.7),Text('zero-point delocalization wins',font=MONO,font_size=39,color=CRIMSON).move_to(DOWN*.6),Text('pressure can reverse the result',font=SERIF,font_size=31,color=TEAL).move_to(DOWN*2.1)); self.wait(d)
class B02_SDT(Scene):
 # B02 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=9.09
  self.add(bg(),ttl('Most substances reach a temperature wher'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Most substances reach a temperature where binding wins ',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Helium is the conspicuous exception at low pressure',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=9.6
  self.add(bg(),ttl('Try to localize one atom tightly around'))
  stmt=Text('Try to localize one atom tightly around a lattice site',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The uncertainty principle forces a broad momentum sprea',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: derive — sequential step build
 def construct(self):
  d=7.49
  self.add(bg(),ttl('A harmonic estimate captures the floor: '))
  s0=Text('A harmonic estimate captures the floor: every co',font=SERIF,font_size=30,color=CRIMSON).shift(UP*1.5)
  s0.set_max_width(12)
  self.play(Write(s0),run_time=max(0.01,d*0.70))
  self.wait(max(0.01,d*0.3))
class B06_SDT(Scene):
 # B06 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=9.81
  self.add(bg(),ttl('Helium atoms are exceptionally light. Fo'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Helium atoms are exceptionally light',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('For the same confinement scale, lower mass makes the ze',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B08_SDT(Scene):
 # B08 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.69
  self.add(bg(),ttl('At low pressure, the quantum delocalizat'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('At low pressure, the quantum delocalization is large co',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The lattice cannot gain enough binding energy to win',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B10_SDT(Scene):
 # B10 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.73
  self.add(bg(),ttl('Pressure changes the balance. Compressio'))
  stmt=Text('Pressure changes the balance',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Compression brings atoms closer and makes the dense ord',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B11_SDT(Scene):
 # B11 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.37
  self.add(bg(),ttl('Do not confuse this with superfluidity. '))
  stmt=Text('Do not confuse this with superfluidity',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Superfluid flow is another collective quantum phenomeno',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))

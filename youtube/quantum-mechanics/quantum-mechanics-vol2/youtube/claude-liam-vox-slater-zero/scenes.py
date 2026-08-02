import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def matrix(a='chiA(1)',b='chiB(1)',c='chiA(2)',d='chiB(2)'):
 return VGroup(Text('|',font=MONO,font_size=100,color=INK),VGroup(Text(a,font=MONO,font_size=29,color=TEAL),Text(b,font=MONO,font_size=29,color=CRIMSON),Text(c,font=MONO,font_size=29,color=TEAL),Text(d,font=MONO,font_size=29,color=CRIMSON)).arrange_in_grid(2,2,buff=(.8,1.0)),Text('|',font=MONO,font_size=100,color=INK)).arrange(RIGHT,buff=.25)
class B02_History(Scene):
 def construct(self):
  d=DUR.get('B02',15); self.add(bg(),ttl('HISTORY DOES NOT REMOVE THE PHYSICAL INPUT')); line=NumberLine(x_range=[1920,1950,5],length=10,color=SLATE); marks=VGroup(Text('1925 Pauli',font=MONO,font_size=29,color=CRIMSON).move_to(line.n2p(1925)+UP*1),Text('1929 Slater determinant',font=MONO,font_size=29,color=TEAL).move_to(line.n2p(1929)+DOWN*1),Text('1945 Nobel',font=MONO,font_size=29,color=INK).move_to(line.n2p(1945)+UP*1)); note=Text('fermionic antisymmetry = physical input',font=SERIF,font_size=31,color=CRIMSON).move_to(DOWN*2.5); self.play(Create(line),FadeIn(marks,note),run_time=1); self.wait(max(.1,d-1))
class B03_Layout(Scene):
 def construct(self):
  d=DUR.get('B03',13); self.add(bg(),ttl('ROWS: PARTICLES · COLUMNS: SPIN-ORBITALS')); m=matrix(); arrow=CurvedArrow(LEFT*2+DOWN*2,RIGHT*2+DOWN*2,color=CRIMSON); lab=Text('swap rows -> flip sign',font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*2.8); self.play(FadeIn(m),Create(arrow),FadeIn(lab),run_time=1); self.wait(max(.1,d-1))
class B04_Question(Scene):
 def construct(self):
  d=DUR.get('B04',12); self.add(bg(),ttl('WHAT EXACTLY MUST BE DISTINCT?')); left=VGroup(Text('1s alpha',font=MONO,font_size=34,color=TEAL),Text('1s beta',font=MONO,font_size=34,color=CRIMSON),Text('allowed pair',font=SERIF,font_size=29,color=INK)).arrange(DOWN).shift(LEFT*3); right=VGroup(Text('1s alpha',font=MONO,font_size=34,color=CRIMSON),Text('1s alpha',font=MONO,font_size=34,color=CRIMSON),Text('duplicate spin-orbital',font=SERIF,font_size=29,color=CRIMSON)).arrange(DOWN).shift(RIGHT*3); self.play(FadeIn(left,right),run_time=1); self.wait(max(.1,d-1))
class B05_Antisymmetry(Scene):
 def construct(self):
  d=DUR.get('B05',13); self.add(bg(),ttl('DETERMINANTS IMPLEMENT ANTISYMMETRY')); eqs=VGroup(Text('Psi(1,2) = - Psi(2,1)',font=MONO,font_size=42,color=CRIMSON),Text('exchange particles -> swap rows',font=MONO,font_size=32,color=TEAL),Text('swap rows -> determinant changes sign',font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.75); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B06_Distinct(Scene):
 def construct(self):
  d=DUR.get('B06',12); self.add(bg(),ttl('DISTINCT SPIN-ORBITALS: STATE CAN BE NONZERO')); m=matrix(); eq=Text('chiA and chiB linearly independent',font=MONO,font_size=32,color=TEAL).move_to(DOWN*2.5); self.play(FadeIn(m,eq),run_time=1); self.wait(max(.1,d-1))
class B07_Zero(Scene):
 def construct(self):
  d=DUR.get('B07',14); self.add(bg(),ttl('IDENTICAL COLUMNS FORCE EXACTLY ZERO')); m=matrix('chiA(1)','chiA(1)','chiA(2)','chiA(2)'); eq=Text('det = 0   ->   zero-norm proposed state',font=MONO,font_size=35,color=CRIMSON).move_to(DOWN*2.5); self.play(FadeIn(m,eq),run_time=1); self.wait(max(.1,d-1))
class B08_Structure(Scene):
 def construct(self):
  d=DUR.get('B08',14); self.add(bg(),ttl('MATTER NEEDS EXCLUSION PLUS DYNAMICS')); pieces=VGroup(Text('fermion occupation constraints',font=MONO,font_size=31,color=CRIMSON),Text('+ Coulomb attraction',font=MONO,font_size=31,color=TEAL),Text('+ electron repulsion',font=MONO,font_size=31,color=INK),Text('+ quantum dynamics',font=MONO,font_size=31,color=INK),Text('-> shells and chemistry',font=DISPLAY,font_size=35,color=CRIMSON)).arrange(DOWN,buff=.48); self.play(FadeIn(pieces),run_time=1); self.wait(max(.1,d-1))
class B09_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B09',17); self.add(bg(),ttl('YOUR TURN: HELIUM 1s^2')); rows=VGroup(Text('1s alpha + 1s beta  -> allowed',font=MONO,font_size=34,color=TEAL),Text('same spatial orbital · different spin-orbitals',font=SERIF,font_size=29,color=INK),Text('1s alpha + 1s alpha -> determinant zero',font=MONO,font_size=32,color=CRIMSON)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B10_Recap(Scene):
 def construct(self):
  d=DUR.get('B10',16); self.add(bg(),Text('PAULI AS A DETERMINANT ZERO',font=DISPLAY,font_size=37,color=CRIMSON).move_to(UP*2.3),Text('fermionic antisymmetry = input',font=MONO,font_size=33,color=TEAL).move_to(UP*.8),Text('Slater determinant = implementation',font=MONO,font_size=32,color=INK).move_to(DOWN*.4),Text('duplicate spin-orbital -> identical columns -> 0',font=MONO,font_size=29,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=19.43
  self.add(bg(),ttl('Pauli formulated the exclusion principle'))
  stmt=Text('Pauli formulated the exclusion principle in 1925, befor',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('His 1945 Nobel citation recognized the principle',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B03_SDT(Scene):
 # B03 SDT retrofit: generic reveal with underline
 def construct(self):
  d=17.83
  self.add(bg(),ttl('Slater introduced determinant wave funct'))
  stmt=Text('Slater introduced determinant wave functions in 1929',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Put particle coordinates in rows and occupied spin-orbi',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=15.83
  self.add(bg(),ttl('Two electrons occupy distinct spin-orbit'))
  stmt=Text('Two electrons occupy distinct spin-orbitals, so the det',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Now duplicate one complete spin-orbital — spatial shape',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: generic reveal with underline
 def construct(self):
  d=16.77
  self.add(bg(),ttl('The fermion requirement is antisymmetry:'))
  stmt=Text('The fermion requirement is antisymmetry: swap two elect',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('A determinant satisfies that automatically because swap',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: generic reveal with underline
 def construct(self):
  d=14.61
  self.add(bg(),ttl('Take a two-by-two Slater determinant. Ro'))
  stmt=Text('Take a two-by-two Slater determinant',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Row one evaluates spin-orbitals at particle one',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=15.59
  self.add(bg(),ttl('Now set chi B equal to chi'))
  stmt=Text('Now set chi B equal to chi A',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The two columns become identical',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: generic reveal with underline
 def construct(self):
  d=17.81
  self.add(bg(),ttl('Exclusion is essential to shell filling '))
  stmt=Text('Exclusion is essential to shell filling and the periodi',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Without fermionic occupation constraints, matter would ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=15.59
  self.add(bg(),ttl('Your turn. Helium has two electrons in'))
  stmt=Text('Helium has two electrons in the same 1s spatial orbital',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Is that forbidden? No: one occupies 1s alpha and the ot',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B10_SDT(Scene):
 # B10 SDT retrofit: generic reveal with underline
 def construct(self):
  d=16.3
  self.add(bg(),ttl('Why does Pauli appear as a determinant'))
  stmt=Text('Why does Pauli appear as a determinant zero? Fermionic ',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('A Slater determinant implements it',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))

#!/usr/bin/env python3
"""Audit anthropics beat sheets against recent Brutalist rule changes.
Checks (mechanical subset):
  V  voice-lock: engine in {kokoro,nbb}, voice in {am_onyx,af_bella,nbbhuman} (metadata + per-beat)
  E  'elevenlabs' string anywhere
  G  spark GLYPH: 'glyph' string in props (spark LINE via sparkLine is fine)
  F  shot.form: fraction of beats carrying shot.form (SHOT-FORM-SYSTEM migration)
  R  ratio-encoded pattern names (*169 / *916) — frozen legacy, banned for new
  C  closing block: ClaudeVerdictArtifact + closing ClaudeComposerAsk + ClaudeTitleOutro all present
  O  cold open: first beat pattern == ClaudeComposerAsk
  S  PIPELINE-CARD RULE: beats whose build.status is a slate/pipeline card
  A  audio lock: all beats have actual_duration_s
  T  TYPECHECK.md / FACTCHECK.md present in reel folder
"""
import json, os, glob, csv, sys, collections

ROOT = os.path.expanduser('~/mnt/bear-textbooks/books/anthropics')
OUT  = os.path.join(ROOT,'_audit')
OK_ENGINE={'kokoro','nbb'}; OK_VOICE={'am_onyx','af_bella','nbbhuman'}

rows=[]; agg=collections.Counter(); form_beats=0; total_beats=0
sheets=sorted(open(os.path.join(OUT,'sheets.txt')).read().split())
for p in sheets:
    rel=os.path.relpath(p,ROOT); d=os.path.dirname(p)
    v={}
    try:
        raw=open(p,encoding='utf-8',errors='replace').read()
        j=json.loads(raw)
    except Exception as e:
        rows.append({'sheet':rel,'PARSE':'FAIL','issues':str(e)[:80]}); agg['parse_fail']+=1; continue
    md=j.get('metadata',{}) or {}; beats=j.get('beats',[]) or []
    low=raw.lower()
    issues=[]
    eng={str(md.get('engine','')).lower()} | {str(b.get('engine','')).lower() for b in beats}
    eng={e for e in eng if e}
    if not eng <= OK_ENGINE: issues.append('V:engine='+','.join(sorted(eng-OK_ENGINE))); agg['voice_lock']+=1
    voc={str(md.get('voice','')).lower()} | {str(b.get('voice','')).lower() for b in beats}
    voc={x for x in voc if x}
    if not voc <= OK_VOICE: issues.append('V:voice='+','.join(sorted(voc-OK_VOICE))); agg['voice_lock_voice']+=1
    if 'elevenlabs' in low: issues.append('E:elevenlabs'); agg['elevenlabs']+=1
    if 'glyph' in low: issues.append('G:glyph'); agg['glyph']+=1
    nf=sum(1 for b in beats if isinstance(b.get('shot'),dict) and b['shot'].get('form'))
    form_beats+=nf; total_beats+=len(beats)
    if beats and nf==0: agg['no_shot_form']+=1; issues.append('F:no-shot.form')
    pats=[]
    for b in beats:
        sh=b.get('shot') or {}
        rm=sh.get('remotion') or {}
        pat=rm.get('pattern') or rm.get('component') or ''
        pats.append(pat)
    if any(p.endswith('169') or p.endswith('916') for p in pats):
        issues.append('R:ratio-name'); agg['ratio_pattern']+=1
    tail=set(pats[-4:])
    has_close = ('ClaudeVerdictArtifact' in tail) and ('ClaudeTitleOutro' in tail) and ('ClaudeComposerAsk' in tail)
    if not has_close: issues.append('C:no-your-turn-close'); agg['no_close']+=1
    if pats and pats[0]!='ClaudeComposerAsk': issues.append('O:cold-open='+ (pats[0] or 'none')); agg['bad_open']+=1
    slate=sum(1 for b in beats if str((b.get('build') or {}).get('status','')).upper() in ('SLATE','PIPELINE','NEEDS-FILL','REQUEST'))
    if slate: issues.append(f'S:{slate}-slate-beats'); agg['has_slates']+=1
    if beats and not all(b.get('actual_duration_s') for b in beats):
        issues.append('A:unmeasured-audio'); agg['unmeasured']+=1
    tc=os.path.exists(os.path.join(d,'TYPECHECK.md')); fc=os.path.exists(os.path.join(d,'FACTCHECK.md'))
    if not tc: issues.append('T:no-TYPECHECK'); agg['no_typecheck']+=1
    if not fc: issues.append('T:no-FACTCHECK'); agg['no_factcheck']+=1
    if issues: agg['sheets_with_issues']+=1
    rows.append({'sheet':rel,'beats':len(beats),'issues':';'.join(issues) or 'CLEAN'})

with open(os.path.join(OUT,'audit_results.csv'),'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['sheet','beats','issues','PARSE']); w.writeheader()
    for r in rows: w.writerow(r)
summary={'sheets':len(sheets),'beats_total':total_beats,
         'beats_with_shot_form':form_beats,'aggregate':dict(agg)}
json.dump(summary,open(os.path.join(OUT,'audit_summary.json'),'w'),indent=1)
print(json.dumps(summary,indent=1))

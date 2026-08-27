#!/usr/bin/env python3
"""Mechanical VOICE-LOCK fixes on flagged beat sheets. Surgical regex, JSON-validated,
logged to mechfix_log.json. Rules:
 R1 text fields (clock/notes/note/audio_note): 'ElevenLabs' -> 'Kokoro (VOICE-LOCK)'
 R2 "engine":"elevenlabs" -> "kokoro"
 R3 "voice":"Liam" -> "am_onyx"
 R4 "voice":"NikBearBrown|nikbearbrown" -> "nbbhuman"
 voice_id/voice_env legacy EL fields are LOGGED, not rewritten (dead fields; drop at rebuild).
"""
import csv, os, re, json, sys, collections
ROOT=os.path.expanduser('~/mnt/bear-textbooks/books/anthropics')
rows=list(csv.DictReader(open('audit_results.csv')))
targets=sorted({r['sheet'] for r in rows if ('E:elevenlabs' in r['issues'] or 'V:voice=' in r['issues'] or 'V:engine=' in r['issues'])})
s,e=int(sys.argv[1]),int(sys.argv[2]); targets=targets[s:e]
log=[]
FIELD_TXT=re.compile(r'("(?:clock|notes|note|audio_note)"\s*:\s*"[^"]*?)Eleven[ _]?Labs', re.I)
for rel in targets:
    p=os.path.join(ROOT,rel)
    try: raw=open(p,encoding='utf-8').read()
    except Exception as ex: log.append({'sheet':rel,'error':str(ex)[:60]}); continue
    orig=raw; counts=collections.Counter()
    prev=None
    while prev!=raw:
        prev=raw; raw=FIELD_TXT.sub(lambda m:(counts.update(['R1']), m.group(1)+'Kokoro (VOICE-LOCK)')[1], raw, count=1)
    raw,n=re.subn(r'"engine"(\s*:\s*)"elevenlabs"','"engine"\\1"kokoro"',raw,flags=re.I); counts['R2']+=n
    raw,n=re.subn(r'"voice"(\s*:\s*)"Liam"','"voice"\\1"am_onyx"',raw); counts['R3']+=n
    raw,n=re.subn(r'"voice"(\s*:\s*)"(?:NikBearBrown|nikbearbrown)"','"voice"\\1"nbbhuman"',raw); counts['R4']+=n
    legacy=len(re.findall(r'"voice_(?:id|env)"\s*:\s*"[^"]*"',raw)) if 'levenlabs' in raw.lower() else 0
    if raw!=orig:
        try: json.loads(raw)
        except Exception as ex:
            log.append({'sheet':rel,'error':'JSON-INVALID-AFTER-EDIT, reverted: '+str(ex)[:60]}); continue
        open(p,'w',encoding='utf-8').write(raw)
    if raw!=orig or legacy:
        log.append({'sheet':rel,'fixes':dict(counts),'legacy_el_fields_remaining':legacy})
mode='a' if s>0 else 'w'
existing=[]
if mode=='a' and os.path.exists('mechfix_log.json'):
    existing=json.load(open('mechfix_log.json'))
json.dump(existing+log, open('mechfix_log.json','w'), indent=1)
print(f'shard {s}:{e} -> {len(log)} sheets touched/logged')

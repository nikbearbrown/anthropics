#!/usr/bin/env python3
"""queue_scan.py — build the filmloop queue from every beat sheet under --root.

RULES_VERSION = 2
  v2 (2026-08-19): the review deliverable is a SLATE-WITH-AUDIO cut. A reel is
  'done' when a review cut (<slug>.mp4 or <slug>-slate.mp4) exists, is NEWER
  than beat_sheet.json, and carries an audio stream. Silent cuts and stale
  cuts are pending. The rebuild contract (brutalist-art/skills/make/rebuild)
  governs what each invocation does to the sheet.

Usage: python3 queue_scan.py --root <dir> --out <queue.json>
"""
import argparse, json, os, subprocess, sys, collections

RULES_VERSION = 2
SKIP = ('_to_delete', '.filmloop', 'node_modules', '.git')

def has_audio(path):
    try:
        out = subprocess.check_output(['ffprobe','-v','error','-select_streams','a',
            '-show_entries','stream=codec_name','-of','csv=p=0', path],
            stderr=subprocess.DEVNULL, timeout=30)
        return bool(out.strip())
    except Exception:
        return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True); ap.add_argument('--out', required=True)
    a = ap.parse_args()
    items=[]; c=collections.Counter()
    for dirpath, dirnames, filenames in os.walk(a.root):
        dirnames[:] = [d for d in dirnames if d not in SKIP and not d.startswith('.')]
        if 'beat_sheet.json' not in filenames: continue
        d=dirpath; slug=os.path.basename(d)
        sheet=os.path.join(d,'beat_sheet.json')
        try:
            smt=os.path.getmtime(sheet)          # broken symlinks list but do not stat
        except OSError:
            c['skipped_broken']+=1; continue
        status='pending'; note=''
        try:
            for cand in (f'{slug}.mp4', f'{slug}-slate.mp4'):
                mp=os.path.join(d,cand)
                if os.path.exists(mp) and os.path.getmtime(mp) >= smt:
                    if has_audio(mp): status='done'; note=f'review-ready: {cand}'
                    else: note=f'{cand} is SILENT — not review-ready'
                    break
        except OSError as e:
            note=f'stat error: {e}'
        items.append({'dir':d,'slug':slug,'status':status,'note':note,
                      'attempts':0,'worker':''})
        c[status]+=1
    json.dump({'rules_version':RULES_VERSION,'items':items}, open(a.out,'w'), indent=1)
    print(f'queue: {len(items)} reels  ' + ' '.join(f'{k}={v}' for k,v in sorted(c.items())))

if __name__=='__main__':
    main()

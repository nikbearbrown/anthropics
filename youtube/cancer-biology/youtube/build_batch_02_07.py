#!/usr/bin/env python3
"""Batch build script for cancer-biology reels 02-07 (B01/B02/B08 ClaudeWindow cards)."""
import json, re, subprocess, textwrap, os, sys
from pathlib import Path
from datetime import datetime

BASE = Path('/Users/bear/Documents/CoWork/bear-textbooks/books')
ART  = BASE / 'brutalist-art'
RUNTIME = ART / 'runtime' / 'scripts'

def slug_to_title(slug):
    parts = slug.split('-')
    return ' '.join(p.upper() if p.upper() in {'P53','RB','BCL','HPV','MTAP','MGMT','MIR'} else p.capitalize() for p in parts)

def sentences(text):
    raw = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip().rstrip('.') for s in raw if s.strip()]

def make_props(narration, beat, slug):
    sents = sentences(narration) or [narration[:120]]
    title = {'B01':'The mechanism','B02':'The stakes','B08':'The lesson'}[beat]
    heading = slug_to_title(slug)
    if len(sents)<=1:   lines,spark=sents,sents[0]
    elif len(sents)==2: lines,spark=sents[:1],sents[1]
    elif len(sents)==3: lines,spark=sents[:2],sents[2]
    elif len(sents)==4: lines,spark=sents[:3],sents[3]
    else:               lines,spark=sents[:4],sents[-1]
    lines=[textwrap.shorten(l,90,placeholder='…') for l in lines]
    spark=textwrap.shorten(spark,80,placeholder='…')
    return {'view':'artifact','artifactTitle':title,'artifactHeading':heading,'artifactLines':lines,'sparkLine':spark}

REELS = [
    'telomere-crisis','rb-convergence','restriction-point',
    'bypass-track','spindle-checkpoint','clonal-evolution'
]

results = {}

for slug in REELS:
    print(f'\n{"="*60}')
    print(f'REEL: {slug}')
    print(f'{"="*60}')
    reel_dir = BASE / 'cancer-biology' / 'youtube' / f'claude-liam-{slug}'
    bs_path = reel_dir / 'beat_sheet.json'

    if not bs_path.exists():
        print(f'  ERROR: beat_sheet.json not found at {bs_path}')
        results[slug] = 'FAIL: no beat_sheet.json'
        continue

    with open(bs_path) as f:
        d = json.load(f)

    patched = []
    for b in d['beats']:
        bid = b['beat_id']
        if bid not in ('B01','B02','B08'):
            continue
        if b.get('shot',{}).get('source') == 'remotion':
            print(f'  [skip] {bid} already remotion')
            continue
        props = make_props(b['narration_text'], bid, slug)
        b['shot'] = {
            'type': 'GRAPHIC',
            'source': 'remotion',
            'motion': 'fade',
            'remotion': {
                'pattern': 'ClaudeWindow',
                'props': props,
                'rendered': {'out': f'media/{bid}.mp4', 'at': ''}
            }
        }
        b['build'] = {
            'status': 'PENDING',
            'src': f'media/{bid}.mp4',
            'filled_by': 'remotion',
            'at': datetime.now().isoformat(timespec='seconds')
        }
        patched.append(bid)
        print(f'  [patch] {bid}')

    mb = d['metadata'].get('build', {})
    mb['slates'] = []
    mb['filled'] = 11
    d['metadata']['build'] = mb

    with open(bs_path, 'w') as f:
        json.dump(d, f, indent=1)
    print(f'  beat_sheet.json written ({len(patched)} beats patched)')

    # Clear old placeholders
    for bid in ('B01','B02','B08'):
        old = reel_dir / 'media' / f'{bid}.mp4'
        if old.exists():
            old.unlink()
            print(f'  cleared {bid}.mp4')

    # Render remotion
    print(f'  Running remotion_scenes.py...')
    r = subprocess.run(
        [sys.executable, str(RUNTIME / 'remotion_scenes.py'), str(reel_dir)],
        capture_output=True, text=True,
        cwd=str(ART / 'runtime' / 'remotion')
    )
    if r.returncode == 0:
        print(f'  remotion: OK')
        # Show last few lines of output
        last_lines = r.stdout.strip().splitlines()[-4:]
        for line in last_lines:
            print(f'    {line}')
    else:
        print(f'  remotion: FAIL (exit {r.returncode})')
        err_tail = (r.stdout + r.stderr).strip().splitlines()[-8:]
        for line in err_tail:
            print(f'    {line}')
        results[slug] = f'FAIL: remotion exit {r.returncode}'
        continue

    # Compile
    print(f'  Running art run...')
    env = {**os.environ, 'ART_FACTS': '0'}
    r = subprocess.run(
        ['bash', str(BASE / 'brutalist-art' / 'art'), 'run', str(reel_dir)],
        capture_output=True, text=True,
        cwd=str(BASE),
        env=env
    )
    combined = (r.stdout + r.stderr).strip()
    last_lines = combined.splitlines()[-6:]
    print(f'  compile: exit {r.returncode}')
    for line in last_lines:
        print(f'    {line}')

    if r.returncode == 0:
        results[slug] = 'OK'
    else:
        results[slug] = f'FAIL: compile exit {r.returncode}'

print(f'\n{"="*60}')
print('BATCH 02-07 SUMMARY')
print(f'{"="*60}')
for slug, status in results.items():
    print(f'  {slug}: {status}')
print('BATCH 02-07 DONE')

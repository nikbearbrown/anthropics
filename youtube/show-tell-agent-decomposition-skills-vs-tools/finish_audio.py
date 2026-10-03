"""Idempotently add bookend silence and stamp actual measured durations."""
import json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sheet=json.loads((ROOT/'beat_sheet.json').read_text())
for b in sheet['beats']:
    path=ROOT/b['audio_file']
    if b['beat_id'] in ('BIDEA','BOUT'):
        raw=path.with_name(path.stem+'-unpad.mp3')
        if not raw.exists(): path.rename(raw)
        effect='adelay=800:all=1' if b['beat_id']=='BIDEA' else 'apad=pad_dur=1'
        subprocess.run(['ffmpeg','-v','error','-y','-i',str(raw),'-af',effect,'-c:a','libmp3lame','-b:a','192k',str(path)],check=True)
    d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(path)]))
    b['actual_duration_s']=round(d,3)
    if b['beat_id']=='BDEFS': b['shot']['remotion']['props']['durationSeconds']=d
(ROOT/'beat_sheet.json').write_text(json.dumps(sheet,indent=2,ensure_ascii=False)+'\n')
(ROOT/'mp3/timings.json').write_text(json.dumps({b['beat_id']:b['actual_duration_s'] for b in sheet['beats']},indent=2)+'\n')
print('Measured total:',sum(b['actual_duration_s'] for b in sheet['beats']))

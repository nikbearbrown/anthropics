"""Generate complete word-aligned captions and plain upload metadata, no upload."""
import json,subprocess,textwrap,argparse
from pathlib import Path
R=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--staged-description',action='store_true');a=parser.parse_args()
sheet=json.loads((R/'beat_sheet.json').read_text()); slug=sheet['metadata']['slug']
words=json.loads((R/'mp3/words.json').read_text());fps=words['fps']
offsets={};t=0
for b in sheet['beats']:
    bid=b['beat_id'];offsets[bid]=t
    dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(R/'clips'/f'{bid}.mp4')]))
    t+=dur
def stamp(s):
    ms=round(s*1000);h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);sec,ms=divmod(ms,1000)
    return f'{h:02}:{m:02}:{sec:02},{ms:03}'
cues=[];previous=0
for b in sheet['beats']:
    ws=words['beats'][b['beat_id']];j=0
    while j<len(ws):
        group=[]
        while j<len(ws) and len(group)<9:
            group.append(ws[j]);j+=1
            if len(' '.join(w['text'] for w in group))>=60 or (len(group)>=4 and group[-1]['text'].endswith(('.', '?', '!'))):break
        start=max(previous,offsets[b['beat_id']]+group[0]['startFrame']/fps)
        end=max(start+.08,offsets[b['beat_id']]+group[-1]['endFrame']/fps)
        previous=end
        cues.append(f'{len(cues)+1}\n{stamp(start)} --> {stamp(end)}\n'+textwrap.fill(' '.join(w['text'] for w in group),42))
(R/f'{slug}.srt').write_text('\n\n'.join(cues)+'\n')
chapter_names={'BIDEA':'Divide the work, not just the prompt','BDEFS':'Skills, tools, and subagents','B00':'What belongs in the core?','B01':'402 lines to 15: where the instructions went','B02':'Skills load into context','B03':'Tools perform actions','B04':'When a separate worker helps','B05':'An inventory workflow','B06':'Human approval before spending','B07':'Batching: 102 calls to 3 scripts','B08':'What the reported speedup actually means','B09':'Measure the whole workflow','BHTF':'Your turn: justify the boundaries'}
chapters='\n'.join(f'{int(offsets[bid])//60}:{int(offsets[bid])%60:02} {title}' for bid,title in chapter_names.items())
description='''Claude skills, tools, and subagents do different jobs. Learn where to put instructions, actions, and separate workers.

A slow agent does not necessarily need a shorter prompt. This illustrated teardown shows how to divide a workflow: load instructions only when needed, call tools for evidence and action, and delegate only when separate context earns its cost.

Follow an inventory assistant from policy to stock evidence, draft recommendation, and human approval. Then examine Anthropic's StockPilot workshop: a 402-line system prompt became 15 lines, while its daily sweep went from 102 tool calls to 3 scripts and from 488 seconds to about 100. Those are workshop-reported results from several changes together—not a benchmark reproduced here or a guaranteed speedup.

The test is the complete workflow: correctness, elapsed time, and usage. A faster wrong answer is not an improvement.

YOUR TURN
Paste into Claude: "Split my workflow into instructions, actions, and separate workers. Justify each boundary."
Check: can every action be tested? Does every separate worker need its own context?

CHAPTERS
'''+chapters+'''

SOURCES
Anthropic StockPilot workshop:
https://github.com/anthropics/cwc-workshops/blob/main/agent-decomposition/README.md
Claude Code skills:
https://code.claude.com/docs/en/skills
Claude Code subagents:
https://code.claude.com/docs/en/sub-agents

CREDITS
Nik Bear Brown. Narrated by Liam, in for Bear, using a synthetic Kokoro voice. Original animated illustrations; the inventory scenario is a teaching example. Independent educational commentary, not an Anthropic endorsement.

#Claude #AgentSkills #AgenticAI #NikBearBrown
'''
assert len(description.encode())<5000
assert len(','.join(sheet['metadata']['tags']))<500
(R/'description.txt').write_text(description)
(R/f'{slug}.md').write_text('# '+sheet['metadata']['title']+'\n\n'+description+'\n## SEO Keyword Tags\n\n'+', '.join(sheet['metadata']['tags'])+'\n')
if a.staged_description:
    topost=Path('/Users/bear/Documents/CoWork/bear-textbooks/books/youtube/TOPOST')
    (topost/f'{slug}.md').write_text(description)
print(f'{len(cues)} full-text caption cues; {len(description.encode())} description bytes; duration {t:.3f}s')
print(chapters)

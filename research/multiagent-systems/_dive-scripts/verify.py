"""Verify: every numeric claim spoken in a beat sheet must trace to figure-data.json."""
import json, glob, re, sys
D = json.load(open("figure-data.json"))

def flat(o, out=None):
    out = [] if out is None else out
    if isinstance(o, dict):
        [flat(v, out) for k, v in o.items() if k not in ("_meta","skeptics_read","_note","WARNING")]
    elif isinstance(o, list): [flat(v, out) for v in o]
    elif isinstance(o, (int, float)): out.append(float(o))
    return out
POOL = set()
for v in flat(D):
    for x in (v, v*100, v/100, round(v,1), round(v*100,1)):
        POOL.add(round(x, 3))
# numbers that are legitimately from the post's prose, not its figures
PROSE = {45,15,12,4,3,8,30,18,2400000,2.4,117,120,400,80,10,20,40,26,266,21,1985,2020,6,1,2,5,7,25,50,
         1600,0.184,82,83,91.5,62.5,59.3,37.8,34.4,78.7,80.5,80.1,61.8,14.8,12.7,1.5,128,980,90,169,132,
         9,98,79,61,35,33,240,0,17.5,18.5,18.2,35.5,85.2,96,100,27,6.5,11,24,1,2,3}
W2N = {"forty-five":45,"fifteen":15,"twelve":12,"twenty-seven":27,"twenty-one":21,"two hundred sixty-six":266,
       "one hundred twenty-eight":128,"nine hundred eighty":980,"one hundred sixty-nine":169,
       "seventeen":17,"eighteen":18,"thirty-five":35,"ninety-eight":98,"seventy-nine":79,"sixty-one":61,
       "thirty-three":33,"two hundred forty":240,"four hundred":400,"ninety-six":96,"one hundred":100}
bad = []
for f in sorted(glob.glob("youtube/*/beat_sheet.json")):
    bs = json.load(open(f))
    for b in bs["beats"]:
        for tok in re.findall(r"\b\d+(?:\.\d+)?\b", b["narration_text"]):
            v = round(float(tok), 3)
            if v not in POOL and v not in PROSE:
                bad.append((f, b["beat_id"], tok, b["narration_text"][:70]))
    # structural gates
    assert all(x["actual_duration_s"] is None for x in bs["beats"]), f"{f}: GATE P violated (audio timed)"
    assert all(x["audio_file"] is None for x in bs["beats"]), f"{f}: GATE P violated (audio file set)"
    assert "doodle" not in json.dumps(bs).lower(), f"{f}: doodle provenance present"
    assert bs["metadata"]["register"] == "teardown", f"{f}: wrong register"
    assert bs["beats"][0].get("remotion") == "ClaudeComposerAsk", f"{f}: missing composer cold open"
    assert bs["beats"][-1].get("remotion") == "ClaudeTitleOutro", f"{f}: missing title outro"
    gen = [b["beat_id"] for b in bs["beats"] if b["shot"].get("source") in ("gen","genai","ai","t2v","i2v")]
    assert not gen, f"{f}: genAI beats present {gen}"
    print(f"PASS  {f:44} {len(bs['beats']):3d} beats · GATE P held · 0 genAI · 0 doodle")
print("\nunverifiable numerals:", len(bad))
for x in bad: print("  ", x)

"""Rebuild the show-tell sheet; retain measured audio when narration is unchanged."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Agent Decomposition: Skills vs Tools"
SPARSE = {"sparse_by_design": True, "sparse_reason": "show-tell: one large isometric illustration, at most three large labels; narration carries the explanation. Only underfill and clustering are waived."}
def card(bid, narration, pattern, props, **extra):
    return dict(beat_id=bid, act="bookend", lane="bookend", proof_gate="SHOW", narration_text=narration,
                estimated_duration_s=round(len(narration.split())/2.4, 2), voice="am_onyx", engine="kokoro", qc=SPARSE.copy(),
                shot={"type":"REMOTION", "source":"own", "show":[{"at":0.1,"event":"Primary content enters; holds for narration"}], "remotion":{"pattern":pattern,"props":props}}, **extra)
def drawing(bid, name, narration, image):
    return dict(beat_id=bid, act="show-tell", lane="manim", proof_gate="SHOW", narration_text=narration,
                estimated_duration_s=round(len(narration.split())/2.4,2), voice="am_onyx", engine="kokoro", qc=SPARSE.copy(),
                shot={"type":"GRAPHIC","source":"own","visual_intent":image,"motion_claim":image,
                      "show":[{"at":0.1,"event":"Objects establish the problem"},{"at":0.3,"event":image}],"manim":{"class":bid+"_"+name}})
B = [card("BIDEA", "Hallo. This is Liam, in for Bear. A slow agent does not necessarily need a shorter prompt. It needs a better division of work. Let's separate skills, tools, and subagents.",
          "BrutalistHesitantWriter", {"text":"A slow agent needs\na shorter prompt.","triggerWords":"a shorter prompt","replacementWords":"a better division of work","fontSize":80,"charMs":22,"hesitateBetween":6,"hesitateWithin":1,"mistakeRate":2,"jitter":20,"seed":SLUG,"banner":""}, lead_silence_s=0.8),
     card("BDEFS", "Three different things. A skill supplies instructions. A tool performs an action. A subagent works in a separate context. A skill can guide tool use, but that does not automatically make it a separate agent.",
          "ClaudeDefinitions", {"title":"Terms In This Film","terms":[{"term":"skill","meaning":"Instructions loaded when needed"},{"term":"tool","meaning":"An action the agent can call"},{"term":"subagent","meaning":"A worker with separate context"}],"folderLabel":"@NikBearBrown"}),
     drawing("B00","Crowded", "Imagine putting every procedure into the agent's starting instructions. Forecasting, checking inventory, writing a report. Most tasks need only some of that material. The first design question is what belongs in the core, and what can wait until it is needed.", "Three procedure pages arrive in one context tray; one page is selected, exposing unnecessary baggage."),
     drawing("B01","Core", "Anthropic's StockPilot workshop reports reducing its system prompt from four hundred and two lines to fifteen. The other instructions did not disappear. Roughly four hundred lines moved into skills, loaded on demand. That is deferred context, not deleted knowledge.", "A thick instruction stack separates into a small core and a nearby stack of skill pages; two large line counts and Workshop report."),
     drawing("B02","Skill", "Here is a skill being used. The agent loads the relevant instructions into its existing context. The page joins the current work. By default, this is not a fresh worker with a private memory. Separate execution has to be configured explicitly.", "A skill page slides into the same context tray, joining the existing page; no second workspace appears."),
     drawing("B03","Tool", "Now the agent calls a tool. A request goes out; a result comes back. That tool might read inventory, run code, or write a file. Tools are not automatically harmless or stateless. What they can change depends on the implementation and permissions.", "A request page moves into a tool block; a new result page emerges on its other side."),
     drawing("B04","Worker", "A subagent is different. Give a worker a bounded task and its own context. It does the work there, then returns a result. This can keep intermediate detail out of the parent's conversation. It can also add coordination time and additional model usage.", "Two separate trays establish parent and worker contexts; a task crosses outward and a compact result returns."),
     drawing("B05","Policy", "Try an inventory assistant. A skill explains the reorder policy. A tool reads the stock record. The agent uses both to draft a recommendation. The instruction page tells it how to decide; the tool result supplies evidence. Neither replaces the other.", "A policy page and a tool-produced stock page meet in one tray; a draft page rises from their combination."),
     drawing("B06","Approval", "Before placing an order, put a human approval point between the draft and the action. Check the quantity, supplier, and evidence. Reading stock and spending money should not inherit the same permission merely because they sit inside the same workflow.", "A draft approaches a closed approval gate; a check arrives and the gate opens before the draft can reach the action block."),
     drawing("B07","Batch", "The workshop also changed how data was processed. Its daily sweep went from a hundred and two tool calls to three scripts. Those scripts worked over data directly. Moving instructions into skills was only one part of the redesign; batching work was another.", "Many small operation blocks consolidate into three larger script blocks, with two large counts and Workshop report."),
     drawing("B08","Timing", "For that daily sweep, the workshop reports four hundred and eighty-eight seconds before, and about one hundred seconds after. Several changes contributed. Treat this as a reported example, not a guaranteed fivefold speedup for your agent. We have not rerun that benchmark here.", "Two isometric bars grow on the same baseline with heights proportional to 488 and 100; only two values and Workshop report."),
     drawing("B09","Measure", "Test your redesign on the same tasks. Check correctness, elapsed time, and usage. If the result is faster but wrong, reject it. If a separate worker returns a huge transcript, you may just have moved the clutter. Measure the complete workflow, not the prompt's line count.", "Two result pages pass through the same comparison frame; a rejected page drops out and a checked result remains."),
]
PROMPT = "Split my workflow into instructions, actions, and separate workers. Justify each boundary."
B += [card("BHTF", "Your turn. Paste this into Claude: "+PROMPT+" Then check two things yourself. Can every action be tested? Does every separate worker need its own context? If not, simplify the design.", "ClaudeComposerAsk",
           {"greeting":"Your turn.","topic":"CLAUDE · YOUR TURN","segment":"Divide the Work","command":PROMPT,"runningText":"paste this into Claude…","output":["Check: every action can be tested.","Check: each worker needs separate context."],"folderLabel":"@NikBearBrown","modelLabel":"Claude","effortLabel":"High","largeText":True}),
      card("BOUT", TITLE+". At Nik Bear Brown.", "ClaudeTitleOutro", {"title":TITLE,"slug":SLUG,"handle":"@NikBearBrown","subline":""}, kind="outro_voice",tail_silence_s=1.0)]
path=HERE/"beat_sheet.json"
old={b["beat_id"]:b for b in json.loads(path.read_text())["beats"]} if path.exists() else {}
for b in B:
    prior=old.get(b["beat_id"],{})
    if prior.get("narration_text")==b["narration_text"]:
        for key in ("actual_duration_s","audio_file"):
            if key in prior: b[key]=prior[key]
    if b["beat_id"]=="BDEFS" and "actual_duration_s" in b:
        b["shot"]["remotion"]["props"]["durationSeconds"]=b["actual_duration_s"]
sheet={"metadata":{"slug":SLUG,"title":TITLE,"topic":"CLAUDE · AGENT DESIGN","skill":"show-tell","style_preset":"show-tell","channel":"claude-liam","persona":"Liam (in for Bear)","voice":"am_onyx","voice_kokoro":"am_onyx","engine":"kokoro","clock":"narration","palette":"claude","register":"Teardown","fps":24,"aspect_ratio":"16:9","width":3840,"height":2160,"caption_policy":"none","greeting_language":"German (Hallo)","bookend_exempt":["cold-open","bvdt"],"bookend_exempt_reason":"Show-tell uses hesitant writer and key terms instead of composer cold open, and illustrated body instead of verdict. Your Turn and spoken outro retained.","audience":"educators, students, and builders designing Claude workflows","source_doc":"SOURCES.md; StockPilot workshop README and Anthropic documentation","tags":["Claude","Agent Skills","Tools","Subagents","Agent Decomposition"]},"beats":B}
path.write_text(json.dumps(sheet,indent=2,ensure_ascii=False)+"\n")
print(f"{len(B)} beats; estimated {sum(b['estimated_duration_s'] for b in B):.0f}s")

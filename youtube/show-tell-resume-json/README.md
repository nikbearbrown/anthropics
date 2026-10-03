# show-tell-resume-json — Your Resume Is Data, Not a Document

## Executive summary

**What it says.** Keep your resume as a JSON record, not a document. When your resume is a Word file and you ask a model to tune it for a job, the model rewrites — and sometimes inserts a line you never wrote, in the same voice as the real ones, with nothing marking it as added. Professor Bear has known students whose resumes claimed defense skills they did not have because of exactly that. A JSON record fixes it by being checkable per line: you read each field, you mark it attested with a date, and every cover letter and targeted resume is generated *from* the record rather than edited on top of the last version.

**What it shows.** Nine drawn isometric beats: a page being overwritten, a fake line sliding in among the real ones, a magnifier passing over it without stopping, the page becoming a field stack, checks landing row by row, letters peeling off while the record stays put, a missing field filled from a binder, and — the ending — a scan beam that lights only four of the rows.

**The turn at the end.** Bear updated his own file and then found that his own tools cannot see the new sections. The job matcher reads four fields and service is not one of them; the collector that searched 3,446 postings never reads a resume at all. *A field no tool reads is one you have to say out loud yourself.*

**Status.** Planning package complete: beat sheet, fact check. **GATE P is open — no audio has been generated and nothing has been rendered.** 183 s estimated across 13 beats.

---

| File | What it is |
|---|---|
| `make_sheet.py` | writes `beat_sheet.json`; edit narration here, never the JSON |
| `beat_sheet.json` | 13 beats — hesitant writer, terms card, 9 drawn beats, composer Your Turn, spoken outro |
| [`FACTCHECK.md`](FACTCHECK.md) | 9 claims: 7 verified in files, 2 Bear's own testimony, plus what was left out and why |
| `BUILD-PROMPT.md` | how to build it from here |

## The claim the film is built on

It is not "JSON is tidier." It is **provenance**: a document has one state and no memory, so an inserted line is indistinguishable from a written one. A record has fields, so a line can be pointed at, sourced, and dated — and the things you send out become disposable output rather than the only copy.

## What the film does not do

No number for how often models pad resumes — none was found worth standing behind. No watermarking: the failure Bear described is silent insertion, which watermarks do not address. No names, in the film or the résumé JSON.

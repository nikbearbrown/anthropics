# FACTCHECK — show-tell-resume-json

## Executive summary

**What this is.** Every factual claim the narration makes, with where it was checked. The film is about Professor Bear's own record, so the failure mode it warns about — a line nobody verified — is the one it could most easily commit itself.

**Verdict.** Nine checkable claims. **Seven verified in files, two are Bear's own testimony** and are marked as such. One number was deliberately left out.

**The one claim only Bear can stand behind:** the students with defense skills they did not have. There is no document for it and there should not be — it is about identifiable students. It stays in his voice, in the first person, and is never presented as a statistic.

---

| # | Claim in the narration | Status | Where checked |
|---|---|---|---|
| 1 | "My committee work was not in the file at all" | **VERIFIED** | `facts/professor-bear-cv.json` before 2026-09-27 had keys: person, education, experience, awards, publications, sponsored_research, teaching, leadership_in_ai_education, teaching_philosophy. **No `service` key existed.** |
| 2 | "Three committees" | **VERIFIED** | `packet/Appendix-C-Service-Materials.docx` §C0: COE AI for Teaching Committee; Global Education Committee; Academic Senate ITPC task team. |
| 3 | "a task team that surveyed six hundred and seventy-nine students" | **VERIFIED** | Same source, §C0: "surveys of 679 students and hundreds of faculty." Also in `Section-E3-Service-Statement.docx`. The film says only the student figure; "hundreds of faculty" is omitted as imprecise. |
| 4 | "Twenty-five course assistants for courses I do not teach" | **VERIFIED** | §C2: "25+ AI course assistants serving engineering courses beyond my own teaching (Ada — calculus; Newton — physics; Grace — algorithms; Archimedes — structural engineering; CRITIQ — peer review)". Narration says twenty-five, not twenty-five *plus*. |
| 5 | "Seven hundred learners in one course the Dean commissioned" | **VERIFIED** | §C2 and E3: ENGR 0201, "700+ learners, Spring 2025", produced as the entry point for the university-wide Anthropic partnership; E3 says "when the Dean needed an entry-point course". |
| 6 | "My own job matcher reads four fields, and service is not one of them" | **VERIFIED** | `greenhouse_watch.py` line 23: `RESUME_REQUIRED = {"personal": dict, "education": list, "experience": list, "skills": dict}`. `resume_features()` reads only skills, experience titles, personal.location, education degrees. `grep` for service/committee/mentoring in that file: **zero matches.** |
| 7 | "The collector that searched three thousand postings never read the resume at all" | **VERIFIED** | `lectern/collect.py`: `grep -ci resume` → **0**. It matches on `keywords.json`. The run was 3,446 postings, so "three thousand" understates and is safe. |
| 8 | "I have known students whose resumes claimed defense skills they did not have, because a model added them and nobody caught it" | **BEAR'S TESTIMONY** | No document, and there should not be one — it concerns identifiable students. Kept in the first person, never as a rate or a count. |
| 9 | "teaching other people's faculty to use a company's tools well" | **VERIFIED** | E3: trains graduate students to help "faculty outside technology fields adopt AI tools", reaching mathematics faculty in Boston "and, through them, the London campus"; maintains the tool directory in the university's Claude organization and ChatGPT. |

## Left out on purpose

- **The AI Bootcamp's 500+ students** and the **faculty seminar** are both in the dossier and both true. Cut for time, not doubt.
- **Any number for how often models pad a resume.** I could not find one I would stand behind, and the film does not need it — one named mechanism beats an unsourced rate.
- **Names.** No chair, organiser, sponsor, co-lead or student is named, in the film or in the résumé JSON, per that file's privacy rule.
- **"Watermarking."** Bear mentioned it in the brief. It is left out of the narration: the failure he actually described is *insertion nobody noticed*, which has nothing to do with watermarks, and conflating the two would weaken the point.

## What changed in the résumé, and what is not yet attested

`facts/professor-bear-cv.json` gained two sections on 2026-09-27: `service` (three committees, four institutional roles, the nonprofit) and `faculty_development_and_bridge_work` (six lines on teaching faculty to use vendor tools, eight on curricula authored, four on what it qualifies for).

Every line traces to Section E3 or Appendix C. **None of it is attested.** The file's `attestation_note` says so and `pending_owner_review` lists both sections by name. The film's own argument requires this: a section a model assembled and the owner has not read is exactly the thing being warned about.

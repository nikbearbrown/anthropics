# PROMPTS — cc-agentic-loop-not-chatgpt

The exact `claude -p` invocations behind `evidence/`. Reproducible; no live-data spend.

## Common flags

```
Claude Code 2.1.150
--output-format stream-json --verbose
--max-turns 16
--strict-mcp-config
< /dev/null
```

## Run: naive — `evidence/run-naive.jsonl`

```
--session-id 2c015af6-7cef-47bf-a759-0b1d6dc31ae3
--permission-mode acceptEdits
--allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)"
prompt: "add a contact form to my class website"
```

## Run: calibrate — `evidence/run-calibrate.jsonl`

```
--session-id de1f38d5-5b62-49c6-9bfe-b3dec4ad6611
--permission-mode default
--allowedTools "Read,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(wc:*),Bash(git:*)"
prompt (from evidence/ask-calibration.txt):
  Answer five questions before we do anything. Do not change any files, do not create any files.
  1) What files are in this project?
  2) What do you think this project is for?
  3) What would you change if I asked you to add a contact form?
  4) What would you not change?
  5) What are you uncertain about?
```

## The viewer's paste-in (BHTF)

```
Answer 5 questions before we do anything. Do not change any files.
1) What files are in this project?
2) What do you think this project is for?
3) What would you change if I asked you to add feature X?
4) What would you not change?
5) What are you uncertain about?
```

Substitute "feature X" for the change the viewer would otherwise ask for on turn one.

#!/usr/bin/env bash
set -euo pipefail

log_dir="hooks-log"
log_file="$log_dir/writes.log"
mkdir -p "$log_dir"

payload="$(cat)"

tool_name="$(printf '%s' "$payload" | /usr/bin/python3 -c 'import json,sys
d=json.load(sys.stdin)
print(d.get("tool_name",""))')"

file_path="$(printf '%s' "$payload" | /usr/bin/python3 -c 'import json,sys
d=json.load(sys.stdin)
ti=d.get("tool_input",{}) or {}
print(ti.get("file_path",""))')"

ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
printf '%s\t%s\t%s\n' "$ts" "$tool_name" "$file_path" >> "$log_file"

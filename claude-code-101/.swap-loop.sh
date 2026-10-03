#!/usr/bin/env bash
# wait for the running loop to finish its current film (a new DONE/FAILED/BLOCKED line), then swap in cc101loop.sh.new and restart
cd /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics
LOG=claude-code-101/.cc101loop/cc101loop.log; n0=$(grep -c "DONE\|FAILED\|BLOCKED" "$LOG")
while [ "$(grep -c "DONE\|FAILED\|BLOCKED" "$LOG")" -le "$n0" ]; do sleep 5; done
pkill -f "bash ./cc101loop.sh"; sleep 3
mv cc101loop.sh cc101loop.sh.v1 && mv cc101loop.sh.new cc101loop.sh && chmod +x cc101loop.sh
echo "$(date '+%F %T')  swapped to v2 (stream-json digest, --max-turns 800); restarting" >> "$LOG"
nohup ./cc101loop.sh > claude-code-101/.cc101loop/loop-stdout.log 2>&1 &

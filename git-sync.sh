#!/bin/bash
# git-sync.sh — commit local changes, pull remote changes, push. Safe for cron.
# Usage: ./git-sync.sh [folder]   (defaults to the folder this script lives in)
#
# Auth: uses a locally stored GitHub token, never prompts. Lookup order:
#   1. $GITHUB_TOKEN env var
#   2. token file at $TOKEN_FILE (plain text, chmod 600)
#   3. `gh auth token` (if GitHub CLI is logged in)
#   4. macOS Keychain generic password with service name $KEYCHAIN_SERVICE

set -uo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"   # cron has a bare PATH
export GIT_TERMINAL_PROMPT=0   # never block waiting for a username/password

REPO_DIR="${1:-$(cd "$(dirname "$0")" && pwd)}"
NAME="$(basename "$REPO_DIR")"
LOG_DIR="$HOME/Library/Logs/git-sync"
LOG="$LOG_DIR/$NAME.log"
LOCK="/tmp/git-sync-$NAME.lock"
MAX_MB=95   # GitHub rejects files >100MB

TOKEN_FILE="${GIT_SYNC_TOKEN_FILE:-$HOME/.config/git-sync/token}"   # edit to wherever yours lives
KEYCHAIN_SERVICE="github-token"

mkdir -p "$LOG_DIR"
log()  { echo "$(date '+%Y-%m-%d %H:%M:%S') [$NAME] $*" >> "$LOG"; }
fail() {
  log "ERROR: $*"
  osascript -e "display notification \"$*\" with title \"git-sync: $NAME\"" 2>/dev/null
  exit 1
}

get_token() {
  if [ -n "${GITHUB_TOKEN:-}" ]; then printf '%s' "$GITHUB_TOKEN"; return; fi
  if [ -r "$TOKEN_FILE" ]; then tr -d '[:space:]' < "$TOKEN_FILE"; return; fi
  if command -v gh >/dev/null 2>&1; then
    local t; t="$(gh auth token 2>/dev/null)"
    if [ -n "$t" ]; then printf '%s' "$t"; return; fi
  fi
  security find-generic-password -s "$KEYCHAIN_SERVICE" -w 2>/dev/null
}

# One run at a time
mkdir "$LOCK" 2>/dev/null || { log "already running, skipping"; exit 0; }
trap 'rmdir "$LOCK"' EXIT

cd "$REPO_DIR" || fail "cannot cd to $REPO_DIR"
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || fail "not a git repo"

GITDIR="$(git rev-parse --git-dir)"
if [ -d "$GITDIR/rebase-merge" ] || [ -d "$GITDIR/rebase-apply" ] || [ -f "$GITDIR/MERGE_HEAD" ]; then
  fail "repo is mid-merge/rebase — fix manually"
fi

BRANCH="$(git symbolic-ref --short HEAD 2>/dev/null)" || fail "detached HEAD — check out a branch"

# Inject the token for this process only. Passed via GIT_CONFIG_* env vars
# (git 2.31+) so it never hits .git/config, the remote URL, the log, or `ps`.
REMOTE_URL="$(git remote get-url origin 2>/dev/null)" || fail "no 'origin' remote"
case "$REMOTE_URL" in
  https://github.com/*)
    TOKEN="$(get_token)"
    [ -n "$TOKEN" ] || fail "no GitHub token found (env, $TOKEN_FILE, gh, or keychain)"
    AUTH="$(printf 'x-access-token:%s' "$TOKEN" | base64 | tr -d '\n')"
    export GIT_CONFIG_COUNT=2
    export GIT_CONFIG_KEY_0="credential.helper"            # disable helpers so nothing pops up
    export GIT_CONFIG_VALUE_0=""
    export GIT_CONFIG_KEY_1="http.https://github.com/.extraheader"
    export GIT_CONFIG_VALUE_1="AUTHORIZATION: basic $AUTH"
    unset TOKEN AUTH
    ;;
  git@github.com:*|ssh://*)
    log "origin is SSH — token not used, relying on SSH key"
    ;;
esac

# 1. Commit local changes (scoped to this folder only)
if [ -n "$(git status --porcelain -- .)" ]; then
  git add -A -- .

  # Guard against files GitHub will reject
  BIG=""
  while IFS= read -r f; do
    [ -f "$f" ] || continue
    size=$(stat -f%z "$f")
    if [ "$size" -gt $((MAX_MB * 1024 * 1024)) ]; then BIG="$BIG $f"; fi
  done < <(git diff --cached --name-only --relative)
  if [ -n "$BIG" ]; then
    git reset -q
    fail "files over ${MAX_MB}MB, add to .gitignore:$BIG"
  fi

  git commit -q -m "auto-sync: $(date '+%Y-%m-%d %H:%M')" >> "$LOG" 2>&1 || fail "commit failed"
  log "committed local changes"
fi

# 2. Pull remote changes
git fetch -q origin >> "$LOG" 2>&1 || fail "fetch failed (network or auth)"
if git rev-parse --verify -q "origin/$BRANCH" >/dev/null; then
  if ! git rebase -q --autostash "origin/$BRANCH" >> "$LOG" 2>&1; then
    git rebase --abort >> "$LOG" 2>&1
    fail "conflict with remote — local commit kept, rebase aborted, resolve manually"
  fi
fi

# 3. Push
git push -q -u origin "$BRANCH" >> "$LOG" 2>&1 || fail "push failed"
log "synced $BRANCH @ $(git rev-parse --short HEAD)"
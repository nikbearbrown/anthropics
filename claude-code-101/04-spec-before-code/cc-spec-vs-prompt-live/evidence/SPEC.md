# login — spec

## Purpose
Sign a returning member into the study-group web app.

## Signature
`login(username: str, password: str, conn) -> str | None`
Returns a session token (a hex string, 32 chars) on success, `None` on failure.

## Password storage
- Passwords are stored as **bcrypt** hashes (cost >= 12) in a SQLite `users` table with columns `username TEXT PRIMARY KEY, pw_hash TEXT NOT NULL`.
- Never MD5. Never SHA-1. Never plain text. Never a Python dict.
- All SQL is parameterized. No string formatting into queries. Ever.

## Rejection rules
- Empty username → `None`.
- Empty password → `None` (never allow "" as valid).
- User not found → `None` after a bcrypt no-op to keep timing flat.
- Wrong password → `None`.

## Session token
- 32-char hex, from `secrets.token_hex(16)`.
- Where the caller keeps it (cookie, response body, header) is **out of scope for this function** — but if you cannot tell from the code base which the caller expects, ask before coding.

## Errors
- Any database error propagates. Do not swallow.

## Definition of done
`python3 check.py` prints `PASS`. It checks: bcrypt import, no md5/sha1 import, no `USERS = {`, no `format(` / f-string / `%` inside a SQL string, empty-password rejection, no-user timing at least 20 ms.

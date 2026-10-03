# SPEC — auth.py

## Interface

- `hash_password(password: str) -> str` — returns a storable hash string.
- `verify_password(password: str, stored: str) -> bool` — returns True/False.

## Invariants (must hold)

1. `hash_password("")` and `verify_password("", stored)` raise `ValueError("empty password")`.
2. The stored string must not contain `password` in any form (never plaintext).
3. Use `hashlib.pbkdf2_hmac` with `sha256` and at least 100 000 iterations. A fresh 16-byte salt per call, from `secrets.token_bytes`.
4. `verify_password` must be constant-time on the digest compare (use `hmac.compare_digest`).
5. Stored format is a single string; the module chooses the layout, but round-trips through `verify_password`.

## Boundary

- Touch `auth.py` only. Do not create any other file. No network. No disk writes beyond `auth.py`. No new dependencies — Python standard library only.

## Handoff

Done means `python3 -m unittest test_auth.py` reports `OK` with 5 tests run.

"""Password hashing and login verification, stdlib only."""

import hashlib
import hmac
import secrets


SALT_BYTES = 16
PBKDF2_ITERATIONS = 200_000
HASH_ALGO = "sha256"


def hash_password(password: str) -> str:
    salt = secrets.token_bytes(SALT_BYTES)
    derived = hashlib.pbkdf2_hmac(
        HASH_ALGO, password.encode("utf-8"), salt, PBKDF2_ITERATIONS
    )
    return f"pbkdf2_{HASH_ALGO}${PBKDF2_ITERATIONS}${salt.hex()}${derived.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        scheme, iterations, salt_hex, hash_hex = stored.split("$")
    except ValueError:
        return False
    if scheme != f"pbkdf2_{HASH_ALGO}":
        return False
    derived = hashlib.pbkdf2_hmac(
        HASH_ALGO, password.encode("utf-8"), bytes.fromhex(salt_hex), int(iterations)
    )
    return hmac.compare_digest(derived.hex(), hash_hex)


def login(username: str, password: str, users: dict[str, str]) -> bool:
    stored = users.get(username)
    if stored is None:
        # Run verify anyway to keep timing similar for missing users.
        verify_password(password, f"pbkdf2_{HASH_ALGO}$1$00$00")
        return False
    return verify_password(password, stored)

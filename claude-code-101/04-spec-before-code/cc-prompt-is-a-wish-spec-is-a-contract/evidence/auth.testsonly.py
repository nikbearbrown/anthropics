"""auth.py — password hashing for the study group's practice project.

PBKDF2-HMAC-SHA256, stdlib only. Stored form: `pbkdf2_sha256$<iters>$<salt_hex>$<hash_hex>`.
"""
import hashlib
import hmac
import os

_ALGO = "pbkdf2_sha256"
_ITERS = 200_000
_SALT_BYTES = 16
_HASH_BYTES = 32


def hash_password(password: str) -> str:
    if not password:
        raise ValueError("password must not be empty")
    salt = os.urandom(_SALT_BYTES)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, _ITERS, _HASH_BYTES)
    return f"{_ALGO}${_ITERS}${salt.hex()}${digest.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        algo, iters_s, salt_hex, hash_hex = stored.split("$")
        if algo != _ALGO:
            return False
        iters = int(iters_s)
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(hash_hex)
    except (ValueError, AttributeError):
        return False
    candidate = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iters, len(expected))
    return hmac.compare_digest(candidate, expected)

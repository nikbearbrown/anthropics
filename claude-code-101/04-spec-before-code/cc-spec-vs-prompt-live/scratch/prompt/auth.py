import hashlib
import hmac
import secrets
import time

_PBKDF2_ROUNDS = 200_000
_SESSION_TTL_SECONDS = 60 * 60 * 8

_users = {}
_sessions = {}


def register(username, password):
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, _PBKDF2_ROUNDS)
    _users[username] = (salt, digest)


def login(username, password):
    record = _users.get(username)
    if record is None:
        _reject()
        return None

    salt, expected = record
    candidate = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, _PBKDF2_ROUNDS)
    if not hmac.compare_digest(candidate, expected):
        return None

    token = secrets.token_urlsafe(32)
    _sessions[token] = (username, time.time() + _SESSION_TTL_SECONDS)
    return token


def whoami(token):
    entry = _sessions.get(token)
    if entry is None:
        return None
    username, expires_at = entry
    if time.time() >= expires_at:
        _sessions.pop(token, None)
        return None
    return username


def logout(token):
    _sessions.pop(token, None)


def _reject():
    # Constant-work path so a missing user takes about as long as a bad password.
    hashlib.pbkdf2_hmac("sha256", b"", b"\x00" * 16, _PBKDF2_ROUNDS)

"""Sign a returning member into the study-group web app."""
import secrets
import bcrypt

# Precomputed bcrypt hash of a random string, used as a no-op check when the
# user is not found so lookup time doesn't leak account existence.
_DUMMY_HASH = bcrypt.hashpw(b"no-such-user", bcrypt.gensalt(rounds=12))


def login(username: str, password: str, conn) -> str | None:
    if not username or not password:
        return None

    cur = conn.cursor()
    cur.execute("SELECT pw_hash FROM users WHERE username = ?", (username,))
    row = cur.fetchone()

    if row is None:
        bcrypt.checkpw(password.encode("utf-8"), _DUMMY_HASH)
        return None

    pw_hash = row[0]
    if isinstance(pw_hash, str):
        pw_hash = pw_hash.encode("utf-8")

    if not bcrypt.checkpw(password.encode("utf-8"), pw_hash):
        return None

    return secrets.token_hex(16)

"""Login for the study-group app. bcrypt hashes + parameterized sqlite lookups."""
import bcrypt


def login(username, password, connection):
    if not password:
        return None
    if connection is None:
        return None
    row = connection.execute(
        "SELECT pw_hash FROM users WHERE username = ?",
        (username,),
    ).fetchone()
    if row is None:
        return None
    stored = row[0]
    if isinstance(stored, str):
        stored = stored.encode("utf-8")
    if bcrypt.checkpw(password.encode("utf-8"), stored):
        return username
    return None

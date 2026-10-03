"""Tests only. No prose. Passing these does not imply the design is right."""
import sqlite3, unittest
from auth import login

def db():
    c = sqlite3.connect(":memory:")
    c.executescript("CREATE TABLE users (username TEXT PRIMARY KEY, pw_hash TEXT NOT NULL);")
    return c

class T(unittest.TestCase):
    def test_empty_password_rejected(self):
        self.assertIsNone(login("someone", "", db()))
    def test_unknown_user_returns_none(self):
        self.assertIsNone(login("ghost", "whatever", db()))

if __name__ == "__main__":
    unittest.main()
